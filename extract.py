import pandas as pd

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Extract").getOrCreate()

print("Extract Data")
data = [(101, "Ram", 29), (102, "Raj", 34), (103, "Raja", 42)]
df = spark.createDataFrame(data, ["Id", "Name", "Age"])
df.show()

# Save to GCS (requires Hadoop-GCS connector configured)
df.write \
  .format("csv") \
  .option("path", "gs://dev-cloud-storage-1/temp") \
  .option("header", "true") \
  .save()