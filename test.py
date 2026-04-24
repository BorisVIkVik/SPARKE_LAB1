# from pyspark.sql import SparkSession
import os
from pyspark.sql import SparkSession
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1" # без этой строчки у нас будет возникать постоянное предупреждение с просьбой установить эту переменную в значение 1, что мы заранее и делаем
spark = SparkSession.builder.appName("MyApp").master("local[*]").getOrCreate()

# url = "sc://10.247.46.112:15002/;token=your_token;use_ssl=true"
# spark = SparkSession.builder.remote(url).getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

df = spark.createDataFrame([(1, "test")], ["id", "value"])
df.show()

# import os
# try:
#     while True:
#         a = 1 
#         print(a)
# except KeyboardInterrupt as e:
#     print(e)

print(spark)
spark.stop()