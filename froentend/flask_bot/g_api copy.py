from flask import Blueprint, request, jsonify
import google.generativeai as genai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

# Configure the Gemini API key
genai.configure(api_key="AIzaSyA3MzKibpGjCn3VCUvE3oo4-ZRtB9H9I4M")

g_api_bp = Blueprint('g_api', __name__)

# Define the feature classes for models
class OpRiskFeatures(BaseModel):
    year: int = Field(default=2024)
    month: int = Field(default=8)
    NPA_to_Advances_Ratio: float = Field(default=0.35)

# Other classes like BankRiskFeatures, ValueAtRiskFeatures, etc.

feature_mappings = {
    "operations risk model": {"class": OpRiskFeatures},
    # Add other mappings here
}

# Model setup
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', api_key="AIzaSyA3MzKibpGjCn3VCUvE3oo4-ZRtB9H9I4M")

def preprocess_and_invoke_model(sentence):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract information from the following phrase.\nFormatting Instructions: {format_instructions}"),
        ("human", "{phrase}")
    ])

    class ExtractModel(BaseModel):
        model: str = Field(description="the name of the model")
        ingredients: str = Field(description="store all the text")

    parser = JsonOutputParser(pydantic_object=ExtractModel)
    chain = LLMChain(prompt=prompt, llm=model, output_parser=parser)
    result = chain.run({"phrase": sentence})
    model_name = result['model'].lower()

    feature_info = feature_mappings.get(model_name)
    if feature_info:
        parser_new = JsonOutputParser(pydantic_object=feature_info["class"])
        new_chain = LLMChain(prompt=prompt, llm=model, output_parser=parser_new)
        feature_dict = new_chain.run({"phrase": result['ingredients']})
        return feature_dict, model_name
    else:
        raise ValueError(f"No feature class defined for the model: {model_name}")

def send_features_to_api(model_name, feature_data):
    endpoints = {
        "operations risk model": "http://127.0.0.1:8000/predict",
        "bank risk model": "http://127.0.0.1:8001/predict",
        "value at risk model": "http://127.0.0.1:8002/predict",
        "credit risk model": "http://127.0.0.1:8003/predict"
    }

    endpoint = endpoints.get(model_name.lower())
    if not endpoint:
        return f"Endpoint for model '{model_name}' not found."

    response = requests.post(endpoint, json=feature_data)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to send data. Status code: {response.status_code}, Error: {response.text}"

@g_api_bp.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    sentence = data.get('sentence')

    try:
        feature_dict, model_name = preprocess_and_invoke_model(sentence)
        api_response = send_features_to_api(model_name, feature_dict)
        return jsonify({'features': feature_dict, 'api_response': api_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@g_api_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)

    reply = response.candidates[0].content.parts[0].text
    return jsonify({'response': reply})

