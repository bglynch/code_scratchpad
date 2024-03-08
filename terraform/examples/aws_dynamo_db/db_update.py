import os
import time

import boto3
from boto3.dynamodb.conditions import Key

os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
os.environ["AWS_PROFILE"] = "aws-profile"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TestTable')


def query_customer_from_gsi(customer_id=None):
    if not customer_id:
      customer_id ="customer_1"
    response = table.query(
      IndexName='CustomerIndex',
      KeyConditionExpression=Key('customer').eq(customer_id)
    )
    items = response['Items']
    for item in items:
      update_unique_id(item)

def update_unique_id(item):
  pass

if __name__ == "__main__":
  response = table.update_item(
      Key={
          'unique_id': 'e8489cd4-039b-4fc7-bafa-f27e3c5754c1',
      },
      UpdateExpression='SET unique_id = :val1',
      ExpressionAttributeValues={
          ':val1': 'customer_1#e8489cd4-039b-4fc7-bafa-f27e3c5754c1'
      }
  )
  print(response)
  # response = table.get_item(
  #   Key={
  #       'unique_id': 'ffa21fdd-e0ed-4f11-9bd2-30f37d984aaf',
  #   }
  # )
  # print(response)
  