from datetime import datetime, timedelta
from decimal import Decimal
import random
import uuid
import os
import boto3
import time

os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
os.environ["AWS_PROFILE"] = "aws-profile"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TestTable')
print(table.creation_date_time)

def get_random_date():
    """Get random date and time from last 30 days"""
    now = datetime.now()
    start = now - timedelta(days=1)
    random_date = now - (now - start) * random.random()
    return Decimal(random_date.strftime("%y%m%d.%H%M"))

def get_random_size():
  return str(random.randint(1000, 100000))

def get_random_customer():
  customers = [
    'customer_1',
    'customer_2',
    'customer_3',
    'customer_3',
    'customer_3',
    'customer_3',
    'customer_3',
    'customer_4',
    'customer_4',
    'customer_5',
    ]
  return random.choice(customers)



#  Normal Write: 1000 => 29.92773 => 33 items/sec
def write_items():
  startTime = time.time()
  for i in range(1000):
    if i%50 == 0:
      print(f"writing {i}")
    table.put_item(
      Item={
            'unique_id': str(uuid.uuid4()),
            'customer': get_random_customer(),
            'date': get_random_date(),
            'size': get_random_size()
        }
    )
  executionTime = (time.time() - startTime)
  print('Execution time in seconds: ' + str(executionTime))


# Batch write: 1000 => 1.52600 => 655 items/sec
# Batch write: 2800 => 4.34805 => 644 items/sec
# Batch write: 5000 => 7.78437 => 644 items/sec
def batch_write_items():
  startTime = time.time()
  with table.batch_writer() as batch:
    for i in range(5000):
      if i%50 == 0:
        print(f"writing {i}")
      batch.put_item(
        Item={
              'unique_id': str(uuid.uuid4()),
              'customer': get_random_customer(),
              'date': get_random_date(),
              'size': get_random_size()
          }
      )
  executionTime = (time.time() - startTime)
  print('Execution time in seconds: ' + str(executionTime))



if __name__ == "__main__":
  batch_write_items()