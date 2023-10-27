import pandas as pd
import random

# Create an empty DataFrame with the specified columns
data = pd.DataFrame(columns=['Age', 'Training_Hours_Per_Week', 'Performance_Score', 'Gender', 'Calories_Required', 'Height', 'Weight', 'Training_Complexity_Range'])

# Generate 10000 random dummy data entries
for _ in range(10000):
    age = random.randint(18, 45)
    training_hours = round(random.uniform(5, 30), 0)  # Round to nearest whole number
    performance_score = round(random.uniform(1, 10), 0)  # Round to 2 decimal places
    gender = random.choice(['Male', 'Female'])
    calories_required = round(random.uniform(1500, 3500), 0)  # Round to nearest whole number
    height = round(random.uniform(150, 190), 0)  # Round to nearest whole number
    weight = round(random.uniform(50, 100), 0)  # Round to nearest whole number
    training_complexity_range = random.choice(['Low', 'Medium', 'High'])

    # Append the data to the DataFrame
    new_data = pd.DataFrame({
        'Age': [age],
        'Training_Hours_Per_Week': [training_hours],
        'Performance_Score': [performance_score],
        'Gender': [gender],
        'Calories_Required': [calories_required],
        'Height': [height],
        'Weight': [weight],
        'Training_Complexity_Range': [training_complexity_range]
    })

    data = pd.concat([data, new_data], ignore_index=True)

# Save the data to a CSV file
data.to_csv('dummy_data_final.csv', index=False)
