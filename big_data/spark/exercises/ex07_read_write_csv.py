from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 7").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.write.mode("overwrite").csv("output/people_output", header=True)

spark.stop()