from flask import Blueprint, request, jsonify
import requests
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chains import LLMChain  # Use LLMChain instead of SimpleChain
from langchain.llms import AzureOpenAI  # Correctly import the OpenAI model with Azure integration

# Configuration for Azure OpenAI API
API_KEY = "a1924363e6f24b9489bb3f5e3e5a2cce"
ENDPOINT = "https://azureopenainija.openai.azure.com/openai/deployments/miti-gpt4o/chat/completions?api-version=2024-02-15-preview"

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Define the feature classes for different models
class OpRiskFeatures(BaseModel):
    year: int = Field(default=2024, description="the year")
    month: int = Field(default=8, description="the month")
    NPA_to_Advances_Ratio: float = Field(default=0.35, description="NPA to Advances Ratio")

class BankRiskFeatures(BaseModel):
    FinancialMetrics: list[float] = Field(
        default_factory=lambda: [0.1, 0.2, 0.3],
        description="A list of financial metrics used to assess financial risk."
    )
    OperationalMetrics: list[float] = Field(
        default_factory=lambda: [0.4, 0.5, 0.6],
        description="A list of operational metrics used to evaluate operational risk."
    )
    MarketRiskMetrics: list[float] = Field(
        default_factory=lambda: [0.7, 0.8, 0.9],
        description="A list of market risk metrics to assess market-related risks."
    )
    CreditRiskMetrics: list[float] = Field(
        default_factory=lambda: [1.0, 1.1, 1.2],
        description="A list of credit risk metrics to measure credit-related risks."
    )
    EconomicIndicators: list[float] = Field(
        default_factory=lambda: [1.3, 1.4, 1.5],
        description="A list of economic indicators to evaluate economic factors affecting risk."
    )
    OtherRelevantFactors: list[float] = Field(
        default_factory=lambda: [1.6, 1.7, 1.8],
        description="A list of other relevant factors affecting overall risk assessment."
    )

class BankInterestFeatures(BaseModel):
    gdp_growth_rate: float = Field(
        default=2.5,
        description="The annual GDP growth rate as a percentage."
    )
    inflation_rate: float = Field(
        default=1.8,
        description="The annual inflation rate as a percentage."
    )
    unemployment_rate: float = Field(
        default=5.2,
        description="The unemployment rate as a percentage."
    )
    cpi: float = Field(
        default=102.5,
        description="The Consumer Price Index (CPI) value."
    )
    stock_market_index: float = Field(
        default=2950.5,
        description="The current value of the stock market index."
    )

class ValueAtRiskFeatures(BaseModel):
    returns: float = Field(
        default=0.05,
        description="The return value used in the Value at Risk (VaR) calculation."
    )

class CreditRiskFeatures(BaseModel):
    features: list[float] = Field(
        default_factory=lambda: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
                                 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0,
                                 11.1, 12.1, 10.1],
        description="features used in credit risk assessment."
    )

# Mappings for feature classes
feature_mappings = {
    "operations risk model": {
        "class": OpRiskFeatures,
    },
    "bank risk model": {
        "class": BankRiskFeatures,
    },
    "value at risk model": {
        "class": ValueAtRiskFeatures,
    },
    "credit risk model": {
        "class": CreditRiskFeatures,
    },
    "bank interest model": {
        "class": BankInterestFeatures,
    }
}

g_api_bp = Blueprint('g_api', __name__)

def preprocess_input(sentence):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract information from the following phrase.\nFormatting Instructions: {format_instructions}"),
        ("human", "{phrase}")
    ])

    class Extract_Model(BaseModel):
        model: str = Field(description="the name of the model")
        ingredients: str = Field(description="store all the text")

    parser = JsonOutputParser(pydantic_object=Extract_Model)

    # Initialize the LLM with Azure configuration
    llm = AzureOpenAI(api_key=API_KEY, endpoint=ENDPOINT)
    chain = LLMChain(prompt=prompt, llm=llm, output_parser=parser)

    # Invoke the chain to process the input sentence
    result = chain.invoke({
        "phrase": sentence,
        "format_instructions": parser.get_format_instructions()
    })

    model_name = result['model'].lower()
    feature_info = feature_mappings.get(model_name)
    if feature_info:
        parsernew = JsonOutputParser(pydantic_object=feature_info["class"])
        newchain = LLMChain(prompt=prompt, llm=llm, output_parser=parsernew)
        result2 = newchain.invoke({
            "phrase": result['ingredients'],
            "format_instructions": parsernew.get_format_instructions()
        })
        return result2, model_name
    else:
        raise ValueError(f"No feature class defined for the model: {model_name}")

def call_azure_openai(message):
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that helps people find information."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.RequestException as e:
        return f"Failed to make the request. Error: {e}"

@g_api_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    sentence = data.get('message')

    # Preprocess the input using LangChain
    feature_dict, model_name = preprocess_input(sentence)

    # Use Azure OpenAI API for further processing or explanation
    explanation = call_azure_openai(f"Model: {model_name}, Features: {feature_dict}")

    return jsonify({'response': explanation})

@g_api_bp.route('/api/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'response': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'response': 'No selected file'})

    return jsonify({'response': f'File {file.filename} uploaded successfully'})
