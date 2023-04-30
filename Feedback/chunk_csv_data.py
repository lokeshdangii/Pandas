import pandas as pd

# Load the CSV data into a pandas dataframe
df = pd.read_csv('feedbackcsv.csv')

# Extract the chunk of columns with the same word in the column name
word_to_match = 'Communication' # replace 'common_word' with the common word or phrase in the column names
chunk_of_columns = df.filter(like=word_to_match)

# Write the chunk of columns to a new CSV file
chunk_of_columns.to_csv('newfile.csv', index=False) # set index=False to exclude the index column in the output file
