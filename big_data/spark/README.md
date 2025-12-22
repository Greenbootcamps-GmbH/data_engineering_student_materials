# Getting Started

⸻

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Install Python extension
Open Extensions → search Python → ensure it’s installed.

## Ensure VS Code is using the correct Python interpreter
	1.	Press Cmd+Shift+P → Python: Select Interpreter
	2.	Choose the interpreter: ./.venv/bin/python

# Apache Spark Exercises

⸻

## How to run an exercise
spark-submit exercises/<script_name>
ex. spark-submit exercises/ex01_create_dataframe.py

⸻

# Exercise 1 — Create a SparkSession & DataFrame

File: exercises/ex01_create_dataframe.py

Goal
	•	Learn how to start Spark
	•	Create a DataFrame from Python data
	•	Display DataFrame contents

Expected Output

A small table with id, name, and age columns:

+---+-----+---+
| id| name|age|
+---+-----+---+
|  1|Alice| 25|
|  2|  Bob| 30|
+---+-----+---+


⸻

# Exercise 2 — Select & Rename Columns

File: exercises/ex02_basic_columns.py

Goal
	•	Select specific columns
	•	Rename columns using alias

Expected Output

Tables showing:
	•	Only name and age
	•	A renamed column (person_name)

⸻

# Exercise 3 — Filter Rows

File: exercises/ex03_filter_rows.py

Goal
	•	Filter rows using conditions
	•	Apply numeric and string filters

Expected Output
	•	People older than 30
	•	People who live in London

⸻

# Exercise 4 — Sort and Limit

File: exercises/ex04_sort_and_limit.py

Goal
	•	Sort DataFrame rows
	•	Limit number of results

Expected Output
	•	Data sorted by age (ascending and descending)
	•	Only the youngest two people

⸻

# Exercise 5 — Group By

File: exercises/ex05_groupby.py

Goal
	•	Group data by a column
	•	Count records per group

Expected Output

Number of people in each city:

+--------+-----+
|    city|count|
+--------+-----+
|London  |  2  |
|New York|  2  |
|Sydney |  1  |
+--------+-----+


⸻

# Exercise 6 — Aggregations

File: exercises/ex06_aggregations.py

Goal
	•	Perform aggregations on grouped data
	•	Use avg and max

Expected Output

Average and maximum age per city.

⸻

# Exercise 7 — Read & Write CSV

File: exercises/ex07_read_write_csv.py

Goal
	•	Read data from CSV files
	•	Write Spark output to disk

Expected Output
	•	A new folder created:

output/people_output/


	•	Inside the folder, Spark-generated CSV files

Note: Spark writes folders, not single files.

⸻

# Exercise 8 — Spark SQL

File: exercises/ex08_sql_queries.py

Goal
	•	Use SQL queries on Spark DataFrames
	•	Create temporary views

Expected Output

Average age per city calculated using SQL syntax.

⸻

# Exercise 9 — Join DataFrames

File: exercises/ex09_join_dataframes.py

Goal
	•	Join two DataFrames
	•	Combine people and sales data

Expected Output

A table showing:
	•	Person name
	•	Sale amount

Example:

+-----+------+
| name|amount|
+-----+------+
|Alice|  200 |
|Alice|  300 |
|Bob  |  150 |
+-----+------+


⸻

# Exercise 10 — User Defined Function (UDF)

File: exercises/ex10_udf_and_logic.py

Goal
	•	Apply custom Python logic in Spark
	•	Create a new column using a UDF

Expected Output

An additional column showing age category:

+-----+---+---------+
|name |age|age_group|
+-----+---+---------+
|Alice|25 |Young    |
|Bob  |30 |Adult    |
|David|40 |Senior   |
+-----+---+---------+


⸻

Happy Learning