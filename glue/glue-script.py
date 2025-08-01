import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame
import gs_derived

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1754073615681 = glueContext.create_dynamic_frame.from_options(format_options={}, connection_type="s3", format="parquet", connection_options={"paths": ["s3://b3-tech-challenge-maida-raw/raw-data/"], "recurse": True}, transformation_ctx="AmazonS3_node1754073615681")

# Script generated for node Derived Column
DerivedColumn_node1754073728558 = AmazonS3_node1754073615681.gs_derived(colName="part", expr="CAST(REGEXP_REPLACE(part, ',', '.') AS DOUBLE )")

# Script generated for node Derived Column
DerivedColumn_node1754073816550 = DerivedColumn_node1754073728558.gs_derived(colName="theoricalQty", expr="REGEXP_REPLACE(theoricalQty, '\\\\.', '') AS BIGINT")

# Script generated for node Change Schema
ChangeSchema_node1754073914170 = ApplyMapping.apply(frame=DerivedColumn_node1754073816550, mappings=[("cod", "string", "codigo", "string"), ("asset", "string", "acao", "string"), ("type", "string", "tipo", "string"), ("part", "double", "participacao", "double"), ("theoricalQty", "string", "qtde_teorica", "bigint"), ("data_corrente", "string", "data_corrente", "string")], transformation_ctx="ChangeSchema_node1754073914170")

# Script generated for node SQL Query
SqlQuery3404 = '''
select acao, data_corrente, sum(participacao) as soma_part
from tb_acoes GROUP BY acao, data_corrente ORDER BY acao
'''
SQLQuery_node1754074390719 = sparkSqlQuery(glueContext, query = SqlQuery3404, mapping = {"tb_acoes":ChangeSchema_node1754073914170}, transformation_ctx = "SQLQuery_node1754074390719")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1754074390719, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1754073563225", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1754074796003 = glueContext.getSink(path="s3://b3-tech-challenge-maida-refined/refined/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["data_corrente", "acao"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1754074796003")
AmazonS3_node1754074796003.setCatalogInfo(catalogDatabase="default",catalogTableName="tb_soma_part")
AmazonS3_node1754074796003.setFormat("glueparquet", compression="snappy")
AmazonS3_node1754074796003.writeFrame(SQLQuery_node1754074390719)
job.commit()