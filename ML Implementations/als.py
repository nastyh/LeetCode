from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ALSExample").getOrCreate()

# Load data
ratings = spark.read.option("header", "true").option("inferSchema", "true").csv("ratings.csv")

# Drop any rows with missing values
ratings = ratings.dropna()

# Split data into training and test sets
(training, test) = ratings.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS on the training data
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")

model = als.fit(training)

# Evaluate the model by computing the RMSE on the test data
predictions = model.transform(test)

evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")

rmse = evaluator.evaluate(predictions)

print("Root-mean-square error = " + str(rmse))