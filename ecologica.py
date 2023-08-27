import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data from the CSV file (replace 'your_data.csv' with your actual file path)
data = pd.read_csv('Biomass.csv')

# Extract features (latitude, longitude, and years 2010 to 2017) and target variable (biomass for 2010 to 2017)
features = data[['Latitude', 'Longitude', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']]
target = data[['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']]

# Initialize the linear regression model
model = LinearRegression()

# Train the model using the entire available data
model.fit(features, target)

# Predict the biomass percentage for 2018 and 2019 using the trained model
predictions_2018 = model.predict(features)
predictions_2019 = model.predict(features)

# Add the predictions for 2018 and 2019 to the DataFrame
data['Predicted_2018'] = predictions_2018[:, -1]  # Predicted biomass for 2018 (last column)
data['Predicted_2019'] = predictions_2019[:, -1]  # Predicted biomass for 2019 (last column)

# Save the entire DataFrame to an Excel file (replace 'predicted_data.xlsx' with the desired file name)
data.to_excel('predicted_data.xlsx', index=False)

print("Data saved to 'predicted_data.xlsx'.")
