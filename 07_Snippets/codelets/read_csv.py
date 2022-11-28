# Read the data
dataset_sample = pd.read_csv(dataset_source_public,nrows=5)
                                   
# Use the next code cell to print the first five rows of the data.
dataset_sample.head()

print(dataset_sample.to_string())

# Shape of training data (num_rows, num_columns)
# print(dataset_sample.head())