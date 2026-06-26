# from pyspark.sql import SparkSession
import yaml
import os
from pyspark.sql import SparkSession
from pyspark.pandas import read_parquet

with open('config/clusters.yaml') as f:
    cfg = yaml.safe_load(f)

os.environ["PYARROW_IGNORE_TIMEZONE"] = "1" 
builder = SparkSession.builder.appName(cfg["spark"]["app_name"]).master(cfg['spark']['master'])

for key, value in cfg['spark']['configs'].items():
    builder = builder.config(key, value)

spark = builder.getOrCreate()

df = spark.read.parquet('data/food.parquet')


df_single = df.select("known_ingredients_n").dropna()
print(f'Hello count: {df_single.count()}')
from pyspark.ml.clustering import KMeans


from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=["known_ingredients_n"],
    outputCol="features"
)

df2 = assembler.transform(df.fillna(0, subset=["known_ingredients_n"]))
kmeans = KMeans(featuresCol='features',k=2)
model = kmeans.fit(df2)
predictions = model.transform(df2)

centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

print(spark)
spark.stop()