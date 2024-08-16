# %%
# Load Data:

# %%
import pandas as pd
import mysql.connector

# Database connection parameters
db_config = {
    'user': 'root',
    'password': 'sunDay01@new',
    'host': 'localhost',
    'database': 'BankFinancialRiskDB'
}

# Create a connection to the database
conn = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = conn.cursor()

# Define a function to execute a query and load data into a pandas DataFrame
def load_data(query):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    return df

# Queries to select data from each table
queries = {
    'FinancialMetrics': 'SELECT * FROM FinancialMetrics',
    'OperationalMetrics': 'SELECT * FROM OperationalMetrics',
    'MarketRiskMetrics': 'SELECT * FROM MarketRiskMetrics',
    'CreditRiskMetrics': 'SELECT * FROM CreditRiskMetrics',
    'EconomicIndicators': 'SELECT * FROM EconomicIndicators',
    'OtherRelevantFactors': 'SELECT * FROM OtherRelevantFactors'
}

# Load data into pandas DataFrames
dataframes = {}
for table_name, query in queries.items():
    dataframes[table_name] = load_data(query)

# Close the cursor and connection
cursor.close()
conn.close()

# Display the first few rows of each DataFrame
for table_name, df in dataframes.items():
    print(f"\n{table_name}:")
    print(df.head())


# %%
dataframes['CreditRiskMetrics']

# %%
import pandas as pd
from sklearn.preprocessing import StandardScaler

def standard_scale(df, columns):
    """
    Standardizes the specified columns of the DataFrame to have mean 0 and variance 1.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    columns (list): The list of column names to standardize.

    Returns:
    pd.DataFrame: The DataFrame with standardized columns.
    """
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

# Example usage:
# df = standard_scale(df, ['gdp_growth_rate', 'inflation_rate', 'unemployment_rate', 'cpi', 'stock_market_index'])


# %%
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encode(data, columns):
    """
    Perform label encoding on specified columns of a dataframe.

    Args:
    data (pd.DataFrame): The input dataframe.
    columns (list): List of column names to label encode.

    Returns:
    pd.DataFrame: The dataframe with label encoded columns.
    """
    label_encoders = {}
    for column in columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data

# Example usage:
df_t = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue'], 'Size': ['S', 'M', 'L', 'M']})
a = label_encode(df_t, ['Color', 'Size'])
print(a)


# %%
import pandas as pd

def one_hot_encode(data, columns):
    """
    Perform one-hot encoding on specified columns of a dataframe.

    Args:
    data (pd.DataFrame): The input dataframe.
    columns (list): List of column names to one-hot encode.

    Returns:
    pd.DataFrame: The dataframe with one-hot encoded columns.
    """
    data = pd.get_dummies(data, columns=columns, drop_first=True)
    return data

# Example usage:
# df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue'], 'Size': ['S', 'M', 'L', 'M']})
# df = one_hot_encode(df, ['Color', 'Size'])
# print(df)


# %%
import pandas as pd

def drop_columns(data, columns):
    """
    Drop specified columns from a dataframe.

    Args:
    data (pd.DataFrame): The input dataframe.
    columns (list): List of column names to drop.

    Returns:
    pd.DataFrame: The dataframe with the specified columns dropped.
    """
    return data.drop(columns=columns)

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
# df = drop_columns(df, ['B', 'C'])
# print(df)


# %%
##### lable encoding on 'MarketSentiment' and drop 'id ' then merge

# %%
lable_encoding=['CreditRating','MarketSentiment']
drop_col=['BankID','IndicatorID']

# %%
lable_encoding[0]

# %%


# %%
dataframes['CreditRiskMetrics']

# %%
dataframes['OtherRelevantFactors']

# %%
dataframes['CreditRiskMetrics'] = label_encode(dataframes['CreditRiskMetrics'], [lable_encoding[0]])
dataframes['OtherRelevantFactors'] = label_encode(dataframes['OtherRelevantFactors'], [lable_encoding[1]])

# %%
dataframes['EconomicIndicators']

# %%
#EconomicIndicators
dataframes['EconomicIndicators']=dataframes['EconomicIndicators'].drop(drop_col[1],axis=1)

# %%


# %%
#count=1
for key, df in dataframes.items():
    print(key)
    dataframes[key] = dataframes[key].drop(drop_col[0], axis=1)
    #count+=1


# %%


# %%
## FinancialMetrics

# %%
FinancialMetrics_numerical=dataframes['FinancialMetrics'].columns

# %%
#dataframes['FinancialMetrics']=standard_scale(dataframes['FinancialMetrics'], FinancialMetrics_numerical)

# %%
## OperationalMetrics

# %%
dataframes['OperationalMetrics']

# %%
OperationalMetrics_numerical=dataframes['OperationalMetrics'].columns

# %%
#dataframes['OperationalMetrics']=standard_scale(dataframes['OperationalMetrics'], OperationalMetrics_numerical)

# %%
## MarketRiskMetrics

# %%
dataframes['MarketRiskMetrics']

# %%
MarketRiskMetrics_numerical=dataframes['MarketRiskMetrics'].columns

# %%
#dataframes['MarketRiskMetrics']=standard_scale(dataframes['MarketRiskMetrics'], MarketRiskMetrics_numerical)

# %%
## CreditRiskMetrics

# %%
dataframes['CreditRiskMetrics']

# %%
CreditRiskMetrics_numerical=dataframes['CreditRiskMetrics'].columns.drop('CreditRating')

# %%
CreditRiskMetrics_numerical

# %%
#dataframes['CreditRiskMetrics']=standard_scale(dataframes['CreditRiskMetrics'], CreditRiskMetrics_numerical)

# %%
## EconomicIndicators

# %%
dataframes['EconomicIndicators']

# %%
EconomicIndicators_numerical=dataframes['EconomicIndicators'].columns

# %%
#dataframes['EconomicIndicators']=standard_scale(dataframes['EconomicIndicators'], EconomicIndicators_numerical)

# %%
## OtherRelevantFactors

# %%
dataframes['OtherRelevantFactors']

# %%
OtherRelevantFactors_numerical=dataframes['OtherRelevantFactors'].columns.drop('MarketSentiment')

# %%
#dataframes['OtherRelevantFactors']=standard_scale(dataframes['OtherRelevantFactors'], OtherRelevantFactors_numerical)

# %%
### merging tables:

# %%
import pandas as pd

def merge_dataframes_columnwise(dataframes):
    """
    Merge a list of DataFrames with different column names into a single DataFrame column-wise.

    Args:
    dataframes (list of pd.DataFrame): The list of DataFrames to merge.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    merged_df = pd.concat(dataframes, axis=1)
    return merged_df

# Example usage:
df1 = pd.DataFrame({
    'id1': [1, 2, 3],
    'value1': [10, 20, 30]
})

df2 = pd.DataFrame({
    'id2': [4, 5, 6],
    'value2': [40, 50, 60]
})

df3 = pd.DataFrame({
    'id3': [7, 8, 9],
    'value3': [70, 80, 90]
})

dataframes_test = [df1, df2, df3]
merged_df = merge_dataframes_columnwise(dataframes_test)

print(merged_df)


# %%
dataframes_list = list(map(lambda key: dataframes[key], dataframes))

# %%
merged_df = merge_dataframes_columnwise(dataframes_list)

# %%
### target column


# %%
import numpy as np
target = {
    'date': pd.date_range(start='2024-01-01', periods=20, freq='MS'),

    'money_supply': [1800000000000.00 + i * 10000000000.00 for i in range(20)],
    'trade_balance': [500000000.00 + i * 10000000.00 for i in range(20)],

    'Risk': np.random.choice([True, False], size=20).astype(int)
}

# %%
target_df = pd.DataFrame(target)

# %%
merged_df.dtypes

# %%


# %%
# neural network :

# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, confusion_matrix


# %%
data=merged_df

# %%
# Ensure all boolean columns are converted to integers
boolean_columns = data.select_dtypes(include=['bool']).columns
data[boolean_columns] = data[boolean_columns].astype(int)

# Ensure all data is numeric
data = data.apply(pd.to_numeric, errors='coerce')

# Check for and handle missing values
data = data.fillna(0)

# %%
pre_nums_col=[FinancialMetrics_numerical,OperationalMetrics_numerical,MarketRiskMetrics_numerical,CreditRiskMetrics_numerical,EconomicIndicators_numerical,OtherRelevantFactors_numerical]

# %%
# Assuming `df` is your DataFrame with features and `target` is the Series with the target column 'Risky'
X = data
y = target_df['Risk']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
for nums_col in pre_nums_col:
    X_train[nums_col] = scaler.fit_transform(X_train[nums_col])
    X_test[nums_col] = scaler.transform(X_test[nums_col])

# Convert target variable to categorical (if necessary)
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)


# %%
# Initialize the model
model = Sequential()

# Add input layer and hidden layers
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=16, activation='relu'))

# Add output layer
model.add(Dense(units=1, activation='sigmoid'))  # 'sigmoid' for binary classification

# Print model summary
model.summary()


# %%
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)


# %%
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)


# %%
# Save the model
model.save('Bank_financial_risk_model.h5')


# %%
import joblib

# Save the scaler
joblib.dump(scaler, 'Bank_financial_risk_model_scaler.pkl')


# %%


# %%


# %%


# %%



