import pandas as pd

# Load the Excel data into a pandas dataframe
df = pd.read_excel('feedback.xlsx')

# Extract the chunk of columns with the two types of words in the column name
word1_to_match = 'Select your Personal Details' # replace 'word1' with the first common word or phrase in the column names
word2_to_match = 'Quality of lecture' # replace 'word2' with the second common word or phrase in the column names
chunk_of_columns = df.filter(regex=f'{word1_to_match}|{word2_to_match}')

# Write the chunk of columns to a new Excel file
chunk_of_columns.to_excel('new_excel_file.xlsx', index=False) # set index=False to exclude the index column in the output file
