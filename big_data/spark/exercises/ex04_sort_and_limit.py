from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 4").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.orderBy(df.age.desc()).show()
df.orderBy(df.age).limit(2).show()

spark.stop()