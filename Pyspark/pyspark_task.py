from pyspark.sql import SparkSession
from pyspark.sql.functions import avg,std

# Create a Spark session
spark = SparkSession.builder.appName('GCSFilesRead').getOrCreate()

# Set the Hadoop home directory
spark._jsc.hadoopConfiguration().set("hadoop.home.dir", "C:/path/to/winutils")

# Set the GCS credentials path
keyfile_path = r"D:\Product Task\Pyspark\jagan.json"
spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", keyfile_path)

# Specify GCS bucket and file path
bucket_name = "sparktask"
file_path = f"gs://{bucket_name}/sparkdata.csv"

# Read CSV file from GCS
df = spark.read.csv(file_path, header=True)

# Show the DataFrame
df.show()

# 1. Standard deviation and average for an integer column
df.select(avg("Color").alias("avg_Color"),std("Color").alias("std_Color")).show()

# 2. Top 5 frequency in any one of the string based column
from pyspark.sql.functions import col
freq_data = df.groupBy("Location").count()
top5_freq = freq_data.orderBy(col("count").desc()).limit(5).show()

# 3. To get the minimum, 25th percentile, median, 75th percentile , and max of a numeric column.
df.select("Bitterness","Temperature","pH_Level","Gravity","Alcohol_Content").summary("min", "25%", "75%", "max").show()


# 4. Rename a column name.
renamed_col = df.withColumnRenamed("Location", "Place").show()

# 5. To calculate the number of characters in each word in a string column.
from pyspark.sql.functions import length
wordsLengthsDF =df.select(length('Location').alias('lengths'),"Location").show()

