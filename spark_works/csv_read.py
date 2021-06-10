from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SimpleApp')\
        .config('spark.driver.bindAddress', '127.0.0.1')\
        .getOrCreate()


df = spark.read.csv('../datasets/aapl.csv', header=True)
# print(df.show())
df.createOrReplaceTempView('aapl_view')
#
print(spark.sql('select * from aapl_view where Close > 100').show())
spark.stop()
