# # Get user input for the two numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# # Add the numbers
# sum_result = num1 + num2
#
# # Print the result
# print(f"The sum of {num1} and {num2} is: {sum_result}")
# from statistics import mean, median, mode
#
# # Define a list of numbers
# numbers = [1, 3, 6, 6, 6, 7, 9, 9, 10, 11]
#
# # Calculate mean
# mean_value = mean(numbers)
#
# # Calculate median
# median_value = median(numbers)
#
# # Calculate mode
# try:
#     mode_value = mode(numbers)
# except StatisticsError as e:
#     mode_value = f"No unique mode found: {e}"
#
# # Print the results
# print(f"Mean: {mean_value}")
# print(f"Median: {median_value}")
# print(f"Mode: {mode_value}")

# import matplotlib.pyplot as plt
#
# # Sample data
# data = [12, 18, 16, 20, 14, 25, 21, 17, 29, 24, 15]
#
# # Create a box plot
# plt.boxplot(data)
#
# # Add a title and labels
# plt.title('Box Plot Example')
# plt.xlabel('Data')
# plt.ylabel('Values')
#
# # Display the plot
#plt.show()

# import pandas as pd
#
# # Read the CSV file
# df = pd.read_csv('stock+portfolio+performance.csv')  # Replace with your actual file path
#
# # Display the first few rows
# print(df.head())
import pandas as pd

# Load Excel file
import pandas as pd

# Read the CSV file
df = pd.read_csv('stocksdata.csv')  # Replace with your actual file path

# Display the first few rows
print(df.head())
