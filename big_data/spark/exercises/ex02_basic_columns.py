from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 2").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.select("name", "age").show()
df.select(df.name.alias("person_name")).show()

spark.stop()