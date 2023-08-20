# DynamoDB - Python SDK



### Create a Table

> ```python
> import boto3
> 
> # Get the service resource.
> dynamodb = boto3.resource('dynamodb')
> 
> # Create the DynamoDB table.
> table = dynamodb.create_table(
>  TableName='users',
>  KeySchema=[
>      {
>          'AttributeName': 'username',
>          'KeyType': 'HASH'
>      },
>      {
>          'AttributeName': 'last_name',
>          'KeyType': 'RANGE'
>      }
>  ],
>  AttributeDefinitions=[
>      {
>          'AttributeName': 'username',
>          'AttributeType': 'S'
>      },
>      {
>          'AttributeName': 'last_name',
>          'AttributeType': 'S'
>      },
>  ],
>  ProvisionedThroughput={
>      'ReadCapacityUnits': 5,
>      'WriteCapacityUnits': 5
>  }
> )
> 
> # Wait until the table exists.
> table.meta.client.get_waiter('table_exists').wait(TableName='users')
> 
> # Print out some data about the table.
> print(table.item_count)
> ```

### Get Existing Table

> ```python
> import boto3
> 
> # Get the service resource.
> dynamodb = boto3.resource('dynamodb')
> 
> # Instantiate a table resource object without actually creating a DynamoDB table. 
> # Note: the attributes of this table are lazy-loaded: a request is not made nor are the attribute
> # values populated until the attributes on the table resource are accessed or its load() method is called.
> table = dynamodb.Table('users')
> 
> # Print out some data about the table.
> # This will cause a request to be made to DynamoDB and its attribute values will be set based on the response.
> print(table.creation_date_time)
> ```
>

### Create a new item

> ```python
> table.put_item(
>    Item={
>         'username': 'janedoe',
>         'first_name': 'Jane',
>         'last_name': 'Doe',
>         'age': 25,
>         'account_type': 'standard_user',
>     }
> )
> ```
> 

### Get an item

> ```python
> response = table.get_item(
>     Key={
>         'username': 'janedoe',
>         'last_name': 'Doe'
>     }
> )
> item = response['Item']
> print(item)
> ```

### Update an item

> ```python
> table.update_item(
>     Key={
>         'username': 'janedoe',
>         'last_name': 'Doe'
>     },
>     UpdateExpression='SET age = :val1',
>     ExpressionAttributeValues={
>         ':val1': 26
>     }
> )
> ```

### Delete an item

> ```python
> table.delete_item(
>     Key={
>         'username': 'janedoe',
>         'last_name': 'Doe'
>     }
> )
> ```

### Batch Write

> ```python
> with table.batch_writer() as batch:
>     batch.put_item(
>         Item={
>             'account_type': 'standard_user',
>             'username': 'johndoe',
>             'first_name': 'John',
>             'last_name': 'Doe',
>             'age': 25,
>             'address': {
>                 'road': '1 Jefferson Street',
>                 'city': 'Los Angeles',
>                 'state': 'CA',
>                 'zipcode': 90001
>             }
>         }
>     )
>     batch.put_item(
>         Item={
>             'account_type': 'super_user',
>             'username': 'janedoering',
>             'first_name': 'Jane',
>             'last_name': 'Doering',
>             'age': 40,
>             'address': {
>                 'road': '2 Washington Avenue',
>                 'city': 'Seattle',
>                 'state': 'WA',
>                 'zipcode': 98109
>             }
>         }
>     )
>     ...
> ```

### Batch Write with Deduplication

> ```python
> with table.batch_writer(overwrite_by_pkeys=['partition_key', 'sort_key']) as batch:
>     batch.put_item(
>         Item={
>             'partition_key': 'p1',
>             'sort_key': 's1',
>             'other': '111',
>         }
>     )
>     batch.put_item(
>         Item={
>             'partition_key': 'p1',
>             'sort_key': 's1',
>             'other': '222',
>         }
>     )
>     batch.delete_item(
>         Key={
>             'partition_key': 'p1',
>             'sort_key': 's2'
>         }
>     )
>     batch.put_item(
>         Item={
>             'partition_key': 'p1',
>             'sort_key': 's2',
>             'other': '444',
>         }
>     )
> ```

### Querying and scanning

> ```python
> from boto3.dynamodb.conditions import Key, Attr
> 
> # This queries for all of the users whose username key equals johndoe
> response = table.query(
>     KeyConditionExpression=Key('username').eq('johndoe')
> )
> items = response['Items']
> print(items)
> 
> 
> #  scans for all the users whose age is less than 27
> response = table.scan(
>     FilterExpression=Attr('age').lt(27)
> )
> items = response['Items']
> print(items)
> 
> 
> # scans for all users whose first_name starts with J and whose account_type is super_user
> response = table.scan(
>     FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
> )
> items = response['Items']
> print(items)
> 
> 
> # scan based on conditions of a nested attribute. For example this scans for all users whose state in their address is CA
> response = table.scan(
>     FilterExpression=Attr('address.state').eq('CA')
> )
> items = response['Items']
> print(items)
> ```

### Delete a Table

> ```python
> table.delete()
> ```

