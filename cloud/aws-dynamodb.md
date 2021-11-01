

# AWS DynamoDB

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. 

## Key Concepts

### Tables, Items and Attributes

Tables, items, and attributes are the core building blocks of DynamoDB.
A ***table*** is a grouping of data records.                                e.g Users Table
An ***item*** is a single data record in a table.                          e.g Single User
***Attributes*** are pieces of data attached to a single item.    e.g. User's name

#### Attribute Types

| Type       | Identifier | Example                                                    |
| ---------- | ---------- | ---------------------------------------------------------- |
| String     | S          | `"Name": { "S": "Alex DeBrie" }`                           |
| Number     | N          | `"Age": { "N": "29" }`                                     |
| Binary     | B          | `"SecretMessage": { "B": "bXkgc3VwZXIgc2VjcmV0IHRleHQh" }` |
| Boolean    | BOOL       | `"IsActive": { "BOOL": "false" }`                          |
| Null       | NULL       | `"OrderId": { "NULL": "true" }`                            |
| List       | L          | `"Roles": { "L": [ "Admin", "User" ] }`                    |
| Map        | M          | below                                                      |
| String Set | SS         | `"Roles": { "SS": [ "Admin", "User" ] }`                   |
| Number Set | NS         | `"RelatedUsers": { "NS": [ "123", "456", "789" ] }`        |
| Binary Set | BS         | below                                                      |

```json
// Map type
"FamilyMembers": {
  "M": {
    "Bill Murray": {
      "Relationship": "Spouse",
      "Age": 65
    },
    "Tina Turner": {
      "Relationship": "Daughter",
      "Age": 78,
      "Occupation": "Singer"
    }
  }
}

// Binary Set
"SecretCodes": { "BS": [ 
	"c2VjcmV0IG1lc3NhZ2UgMQ==", 
	"YW5vdGhlciBzZWNyZXQ=", 
	"dGhpcmQgc2VjcmV0" 
] }
```



### Primary Key

Each **item** in a table is uniquely identified by a **primary key**. 
2 types of primary key:

1. **Partition Key** : A simple primary key, composed of one attribute known as the *partition key*.
2. **Composite Key**: key is composed of two attributes. The first attribute is the *partition key*, and the second attribute is the *sort key*.

### Secondary Indexes

A *secondary index* lets you query the data in the table using an alternate key
2 types of primary key:

1. **Global secondary index** – An index with a partition key and sort key that can be different from those on the table.
2. Local secondary index – An index that has the same partition key as the table, but a different sort key.

### DynamoDB Streams

Captures data modification events in DynamoDB tables.
DynamoDB Streams writes a stream record whenever one of the following events occurs:

- A new item is added to the table
- An item is updated
- An item is deleted from the table

---

## DynamoDB API

### Control Plane

*Control plane* operations let you create and manage DynamoDB tables

### Data Plane

Lets you perform CRUD operations on items in a Table.
Can use PartiQL or Classic APIs to do this.

### DynamoDB Streams

*DynamoDB Streams* operations let you enable or disable a stream on a table, and allow access to the data modification records contained in a stream

### Transactions

*Transactions* provide atomicity, consistency, isolation, and durability (ACID) enabling you to maintain data correctness in your applications more easily.
Can use PartiQL or Classic APIs to do this.

---

## Local Setup

Can be deployed locally either

- [amazon/dynamodb-local](amazon/dynamodb-local) Docker image
- Localstack
- Localstack + Terraform

---

## Access DynamoDB

- AWS Management Console
- AWS CLI
- API
  - Python: [boto3](https://aws.amazon.com/sdk-for-python/)
- AWS NoSQL Workbench

---

## AWS CLI

### Create a Table

Create a Music Table with Columns for Artist and Song Title

```bash
aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
--provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
```

Console Output

```json
{
  "TableDescription":{
    "AttributeDefinitions":[
      {
        "AttributeName":"Artist",
        "AttributeType":"S"
      },
      {
        "AttributeName":"SongTitle",
        "AttributeType":"S"
      }
    ],
    "TableName":"Music",
    "KeySchema":[
      {
        "AttributeName":"Artist",
        "KeyType":"HASH"
      },
      {
        "AttributeName":"SongTitle",
        "KeyType":"RANGE"
      }
    ],
    "TableStatus":"ACTIVE",
    "CreationDateTime":"2021-09-01T16:40:02.950000+01:00",
    "ProvisionedThroughput":{
      "LastIncreaseDateTime":"1970-01-01T00:00:00+00:00",
      "LastDecreaseDateTime":"1970-01-01T00:00:00+00:00",
      "NumberOfDecreasesToday":0,
      "ReadCapacityUnits":10,
      "WriteCapacityUnits":5
    },
    "TableSizeBytes":0,
    "ItemCount":0,
    "TableArn":"arn:aws:dynamodb:us-east-1:000000000000:table/Music"
  }
}
```

### Check Table Status

```bash
aws dynamodb describe-table --table-name Music | grep TableStatus
or
aws dynamodb describe-table --table-name Music | jq .Table.TableStatus
```

Console Output

```json
"TableStatus": "ACTIVE",
```

### Insert Data into Table

```bash
aws-local dynamodb put-item \
    --table-name Music  \
    --item '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'
```

Console Output

```json
{
  "ConsumedCapacity":{
    "TableName":"Music",
    "CapacityUnits":1.0
  }
}
```

### Read Table

```bash
aws-local dynamodb scan --table-name Music
```

Console Output

```json
{
  "Items":[
    {
      "Artist":{
        "S":"No One You Know"
      },
      "AlbumTitle":{
        "S":"Somewhat Famous"
      },
      "Awards":{
        "N":"1"
      },
      "SongTitle":{
        "S":"Call Me Today"
      }
    }
  ],
  "Count":1,
  "ScannedCount":1,
  "ConsumedCapacity":null
}
```



---

## Python SDK

### Create a Table

```python
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)
```

### Get Existing Table

```python
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually creating a DynamoDB table. 
# Note: the attributes of this table are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes on the table resource are accessed or its load() method is called.
table = dynamodb.Table('users')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute values will be set based on the response.
print(table.creation_date_time)
```

### Create a new item

```python
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)
```

### Get an item

```python
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)
```

### Update an item

```python
table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
```

### Delete an item

```python
table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
```

### Batch Write

```python
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'account_type': 'standard_user',
            'username': 'johndoe',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25,
            'address': {
                'road': '1 Jefferson Street',
                'city': 'Los Angeles',
                'state': 'CA',
                'zipcode': 90001
            }
        }
    )
    batch.put_item(
        Item={
            'account_type': 'super_user',
            'username': 'janedoering',
            'first_name': 'Jane',
            'last_name': 'Doering',
            'age': 40,
            'address': {
                'road': '2 Washington Avenue',
                'city': 'Seattle',
                'state': 'WA',
                'zipcode': 98109
            }
        }
    )
    ...
```

### Batch Write with Deduplication

```python
with table.batch_writer(overwrite_by_pkeys=['partition_key', 'sort_key']) as batch:
    batch.put_item(
        Item={
            'partition_key': 'p1',
            'sort_key': 's1',
            'other': '111',
        }
    )
    batch.put_item(
        Item={
            'partition_key': 'p1',
            'sort_key': 's1',
            'other': '222',
        }
    )
    batch.delete_item(
        Key={
            'partition_key': 'p1',
            'sort_key': 's2'
        }
    )
    batch.put_item(
        Item={
            'partition_key': 'p1',
            'sort_key': 's2',
            'other': '444',
        }
    )
```

### Querying and scanning

```python
from boto3.dynamodb.conditions import Key, Attr

# This queries for all of the users whose username key equals johndoe
response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print(items)


#  scans for all the users whose age is less than 27
response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print(items)


# scans for all users whose first_name starts with J and whose account_type is super_user
response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print(items)


# scan based on conditions of a nested attribute. For example this scans for all users whose state in their address is CA
response = table.scan(
    FilterExpression=Attr('address.state').eq('CA')
)
items = response['Items']
print(items)
```

### Delete a Table

```python
table.delete()
```

