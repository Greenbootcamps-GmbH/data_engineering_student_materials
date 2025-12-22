from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 9").getOrCreate()

people = spark.read.csv("data/people.csv", header=True, inferSchema=True)
sales = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

result = people.join(
    sales,
    people.id == sales.person_id,
    "inner"
)

result.select("name", "amount").show()

spark.stop()