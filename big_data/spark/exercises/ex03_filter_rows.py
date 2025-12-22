from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 3").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.filter(df.age > 30).show()
df.filter(df.city == "London").show()

spark.stop()