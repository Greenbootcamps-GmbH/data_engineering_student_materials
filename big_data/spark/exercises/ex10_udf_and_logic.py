from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("Exercise 10").getOrCreate()

def age_group(age):
    if age < 30:
        return "Young"
    elif age < 40:
        return "Adult"
    else:
        return "Senior"

age_group_udf = udf(age_group, StringType())

df = spark.read.csv("data/people.csv", header=True, inferSchema=True)

df.withColumn("age_group", age_group_udf(df.age)).show()

spark.stop()