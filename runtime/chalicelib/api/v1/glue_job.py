from chalice import Blueprint


S3_Source = 's3://awsglue-datasets/examples/us-legislators/all'

glue_routes = Blueprint(__name__)

@glue_routes.route('/glue_jobs')
def simple_example1():
    return S3_Source



