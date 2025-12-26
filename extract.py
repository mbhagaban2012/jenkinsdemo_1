import pandas as pd

print("Extract Data")

# Sample data
data = {
    'Id': [101, 102, 103],
    'Name': ['Ram', 'Raj', 'Raja'],
    'Age': [29, 34, 42]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Write to gcs file

df.write.format('CSV') \
.option('path',' dev-cloud-storage-1/temp') \
.mode('append') \
.save()