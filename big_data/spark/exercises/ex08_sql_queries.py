from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercise 8").getOrCreate()

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("people")

spark.sql("""
    SELECT city, AVG(age) AS avg_age
    FROM people
    GROUP BY city
""").show()

spark.stop()