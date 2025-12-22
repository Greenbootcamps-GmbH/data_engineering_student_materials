from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max

spark = SparkSession.builder.appName("Exercise 6").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.groupBy("city").agg(
    avg("age").alias("avg_age"),
    max("age").alias("max_age")
).show()

spark.stop()