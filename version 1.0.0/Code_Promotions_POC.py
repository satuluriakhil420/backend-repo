# This is for Dev-1 Env

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1707808768629 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://testing01010/testfolder/Code_promotions_POC/input/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1707808768629",
)

# Script generated for node Amazon S3
AmazonS3_node1707808783914 = glueContext.write_dynamic_frame.from_options(
    frame=AmazonS3_node1707808768629,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://testing01010/testfolder/Code_promotions_POC/output/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1707808783914",
)

job.commit()
