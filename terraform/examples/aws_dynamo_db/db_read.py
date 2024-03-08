import os
import time

import boto3
from boto3.dynamodb.conditions import Key

# Set AWS variables
os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
os.environ["AWS_PROFILE"] = "aws-profile"

# instanciate dynamodb client and dynamodb table
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('TestTable')


def query_customer_from_gsi(customer_id="customer_1"):
    startTime = time.time()
    response = table.query(
      IndexName='CustomerIndex',
      KeyConditionExpression=Key('customer').eq(customer_id)
    )
    items = response['Items']
    print('Response time: ' + str(time.time() - startTime))
    print(f"{sum(int(item['size']) for item in items)} bytes for {len(items)} items \n")

def query_all_customers_by_gsi():
  for customer in ['customer_1','customer_2','customer_3','customer_4','customer_5']:
    query_customer_from_gsi(customer)


if __name__ == "__main__":
  query_all_customers_by_gsi()

  # Response time: 0.875748872756958
  # 49649968 bytes for 985 items

  # Response time: 0.09122705459594727
  # 49547121 bytes for 995 items

  # Response time: 0.3428640365600586
  # 253371442 bytes for 4979 items

  # Response time: 0.15478014945983887
  # 102420775 bytes for 2048 items

  # Response time: 0.09377813339233398
  # 50352886 bytes for 993 items