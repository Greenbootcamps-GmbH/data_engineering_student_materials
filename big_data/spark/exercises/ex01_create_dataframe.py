from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 1").getOrCreate()

data = [
    (1, "Alice", 25),
    (2, "Bob", 30)
]

df = spark.createDataFrame(data, ["id", "name", "age"])

df.show()

spark.stop()