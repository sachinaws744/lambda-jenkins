import boto3
lambda_Client = boto3.client('lambda', region_name='ap-south-1')
response =lambda_Client.create_function(
          Code={
                'S3Bucket': 'pratibha007',
                'S3Key': 'lambda.py.zip', #how can i create or fetch this S3Key
          },
          Description='Process image objects from Amazon S3.',
          FunctionName="check",
          Handler='lambda.lambda_handler',
          Publish=True,
          Role='arn:aws:iam::351246850509:role/lambda_admin',
          Runtime='python3.12'
          )
