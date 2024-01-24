import json
import boto3
def lambda_handler(event, context):
    client = boto3.client('ec2', region_name= 'ap-south-1')
    response = client.run_instances(
           ImageId='ami-00952f27cf14db9cd',
           InstanceType='t2.micro',
           KeyName='terraform_mumbai',
           MaxCount=1,
           MinCount=1
           )

