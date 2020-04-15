
import sys
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import Row
from pyspark.sql.functions import format_string
from csv import reader

spark = SparkSession.builder.getOrCreate()

# Create dataframes from csv files
parking = spark.read.format('csv').options(header='true', \
inferschema='true').load(sys.argv[1])

# Register dataframes as SQL view
parking.createOrReplaceTempView("parking")

# Find the frequencies of the violation_types in parking_violations.csv
result = spark.sql("""SELECT violation_code, COUNT(violation_code) AS value_freq FROM parking GROUP BY violation_code""")
result.show()

# Write dataframe to a file
result.select(format_string('%d\t%d',result.violation_code,result.value_freq)).write.save("task2-sql.out",format="text")