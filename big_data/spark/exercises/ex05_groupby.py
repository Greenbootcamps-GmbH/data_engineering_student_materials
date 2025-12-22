from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 5").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.groupBy("city").count().show()

spark.stop()