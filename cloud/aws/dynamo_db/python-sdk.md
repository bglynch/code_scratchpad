# DynamoDB - Python SDK

### Create Client or Resource

> ```
> 
> ```
>
> 







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
>       batch.put_item(
>           Item={
>               'partition_key': 'p1',
>               'sort_key': 's1',
>               'other': '111',
>           }
>       )
>       batch.put_item(
>           Item={
>               'partition_key': 'p1',
>               'sort_key': 's1',
>               'other': '222',
>           }
>       )
>       batch.delete_item(
>           Key={
>               'partition_key': 'p1',
>               'sort_key': 's2'
>           }
>       )
>       batch.put_item(
>           Item={
>               'partition_key': 'p1',
>               'sort_key': 's2',
>               'other': '444',
>           }
>       )
> ```

### Querying and scanning

> #### Query
>
> #### kwargs
>
> - **IndexName**: name of an index to query
> - **Limit**: maximum number of items to evaluate. Will return **LastEvaluatedKey** to apply in a subsequent operation
> - **KeyConditionExpression**: The condition(s) a key(s) must meet.
> - **FilterExpression**: The condition(s) an attribute(s) must meet
> - **ExclusiveStartKey**: primary key of the first item that this operation will evaluate. Use the value that was returned for `LastEvaluatedKey` in the previous operation
> - **ProjectionExpression**: A string that identifies one or more attributes to retrieve from the table
> - **ExpressionAttributeNames**: One or more substitution tokens for attribute names in an expression
> - **ExpressionAttributeValues**: One or more values that can be substituted in an expression.
>
> - You must provide the **name of the partition key attribute** and a **single value for that attribute**
> - `KeyConditionExpression` parameter to provide a specific value for the partition key.
> - `FilterExpression` to refine the query down
>   - `FilterExpression` is applied after a `Query` finishes, but before the results are returned
>
> ```python
> from boto3.dynamodb.conditions import Key, Attr
> 
> # This queries for all of the users whose username key equals johndoe
> response = table.query(
>  KeyConditionExpression=Key('username').eq('johndoe')
> )
> items = response['Items']
> print(items)
> ```
>
> > [!NOTE]
> >
> > The number of capacity units consumed will be the same whether you request all of the attributes (the default behavior) or just some of them (using a projection expression). 
> > The number will also be the same whether or not you use a `FilterExpression`.
>
> > [!WARNING]
> >
> > A single `Query` operation will read up to the maximum number of items set (if using the `Limit` parameter) or 
> > a **maximum of 1 MB of data** and then apply any filtering to the results using `FilterExpression`
>
> ##### Nexus Examples
>
> ```python
> response = table.query(
>   IndexName='internal_brain_id_gsi',
>   KeyConditionExpression=Key("internal_brain_id").eq("saas-manual-testing"),
> )
> 
> table.query(
>   IndexName='internal_brain_id_gsi',
>   KeyConditionExpression=Key("internal_brain_id").eq("saas-manual-testing"),
>   Limit=2
> )
> # returns LastEvaluatedKey
>  'LastEvaluatedKey': {
>    'sk': 'connector',
>    'internal_brain_id': 'saas-manual-testing', 
>    'pk': 'sid_01j21qpd46ex389kpa4ys14pf2',
>   	'operating_state': 'active'
>  }
> ```
>
> ### [Quey Paginator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/Query.html)
>
> #### kwargs
>
> - **TableName**(required): name of the table or ARN
> - **IndexName**: name of an index to query
> - **Select**: attributes to be returned in the result
>   - ALL_ATTRIBUTES / ALL_PROJECTED_ATTRIBUTES / COUNT / SPECIFIC_ATTRIBUTES
> - **ReturnConsumedCapacity**:  level of detail about consumption that is returned in the response
>   - INDEXES / TOTAL / NONE
> - **ProjectionExpression**: A string that identifies one or more attributes to retrieve from the table
> - **FilterExpression**: A string that contains conditions that DynamoDB applies after the `Query` operation
> - **KeyConditionExpression**: condition that specifies the key values for items to be retrieved by the `Query` action
> - .....not complete
>
> ```python
> paginator = client.get_paginator('query')
> 
> query_params = {
>     'TableName': TABLE_NAME,
>     'IndexName': 'internal_brain_id_gsi',
>     'KeyConditionExpression': '#pk = :pkval',
>     'ExpressionAttributeNames': {
>         '#pk': 'internal_brain_id'
>     },
>     'ExpressionAttributeValues': {
>         ':pkval': {'S': 'saas-manual-testing'}
>     },
>     'Limit': 2
> }
> paginator.paginate(**query_params)
> next(response_iterator.__iter__())
> 
> query_params = {
>     'TableName': TABLE_NAME,
>     'IndexName': 'internal_brain_id_gsi',
>     'KeyConditionExpression': '#pk = :pkval',
>     'ExpressionAttributeNames': {
>         '#pk': 'internal_brain_id'
>     },
>     'ExpressionAttributeValues': {
>         ':pkval': {'S': 'saas-manual-testing'}
>     },
>     'PaginationConfig': {
>       'MaxItems': 2,
>       'PageSize': 2,
>       'StartingToken': None
>   } 
> }
> paginator.paginate(**query_params)
> next(response_iterator.__iter__())
> 
> # return NextToken
> # https://github.com/awslabs/visual-asset-management-system/blob/8ba219a25581b2671bf1214f95f479080ac9e2bf/backend/backend/handlers/assets/assetCount.py#L20
> query_params = {
>     'TableName': TABLE_NAME,
>     'IndexName': 'internal_brain_id_gsi',
>     'KeyConditionExpression': '#pk = :pkval',
>     'ExpressionAttributeNames': {
>         '#pk': 'internal_brain_id'
>     },
>     'ExpressionAttributeValues': {
>         ':pkval': {'S': 'saas-manual-testing'}
>     },
>     'PaginationConfig': {
>       'MaxItems': 2,
>       'PageSize': 2,
>   }
> }
> paginator.paginate(**query_params).build_full_result()
> 
> page_iterator = paginator.paginate(
>   TableName=TABLE_NAME, 
>   IndexName='internal_brain_id_gsi',
>   KeyConditionExpression=Key("internal_brain_id").eq("saas-manual-testing"),
>   PaginationConfig={
>       'MaxItems': 2,
>       'PageSize': 2,
>       'StartingToken': None
>   }  
> )
> ```
>
> look into
>
> ```python
> # https://stackoverflow.com/questions/56328270/dynamodb-pagination-via-boto3-nexttoken-is-not-present-but-lastevaluatedkey-is
> from botocore.paginate import TokenEncoder
> encoder = TokenEncoder()
> for page in scan_iterator:
>     if "LastEvaluatedKey" in page:
>             encoded_token = encoder.encode({"ExclusiveStartKey": page["LastEvaluatedKey"]})
> ```
>
> 



> #### Scan
>
> ```python
> #  scans for all the users whose age is less than 27
> response = table.scan(
>  FilterExpression=Attr('age').lt(27)
> )
> items = response['Items']
> print(items)
> 
> 
> # scans for all users whose first_name starts with J and whose account_type is super_user
> response = table.scan(
>  FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
> )
> items = response['Items']
> print(items)
> 
> 
> # scan based on conditions of a nested attribute. For example this scans for all users whose state in their address is CA
> response = table.scan(
>  FilterExpression=Attr('address.state').eq('CA')
> )
> items = response['Items']
> print(items)
> ```

### Delete a Table

> ```python
> table.delete()
> ```



## Recipes

#### Get Table info with Scan

> #### Table info
>
> ```python
> session = boto3.Session(profile_name=AWS_PROFILE, region_name=AWS_REGION)
> dynamodb = session.resource("dynamodb")
> table = dynamodb.Table(TABLE_NAME)
> 
> print(f"Table row count:  {table.item_count}")
> print(f"Table schema:     {table.key_schema}")
> print(f"Table attributes: {table.attribute_definitions}")
> print(f"Table global secondary indexes")
> for item in table.global_secondary_indexes:
>    	print(f"  Name:   {item.get('IndexName')}")
>    	print(f"  Schema: {item.get('KeySchema')}")
> 
> response = table.scan(ReturnConsumedCapacity='TOTAL')
> ```
>
> #### Info
>
> ```python
> from collections import Counter
> 
> Counter([item['internal_brain_id'] for item in  response['Items']]).most_common()
> ```
>
> 
>
> #### Using `LastEvaluatedKey` to get paginated results
>
> ```python
> response = table.scan(Limit=2)
> 
> data = response['Items']
> 
> while response.get('LastEvaluatedKey'):
>     response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
>     data.extend(response['Items'])
> ```
>
> > [!NOTE]
> >
> > `response['LastEvaluatedKey']` is a dict with the row identifier
> >
> > ```python
> > 'LastEvaluatedKey': {'pk': 'id-2', 'sk': 'sk-2'},
> > ```
>
> > [!IMPORTANT]
> >
> >  *If LastEvaluatedKey is empty, then the "last page" of results has been processed and there is no more data to be retrieved.* So the test I'm using is `while response.get('LastEvaluatedKey')` rather than `while 'LastEvaluatedKey' in response`
>
> #### Similar with paginator
>
> ```python
> client = session.client('dynamodb')
> paginator = client.get_paginator('scan')
> 
> scan_params = {
>     'TableName': TABLE_NAME,
>     'Limit': 5
> }
> response_iterator = paginator.paginate(**scan_params)
> first_page = next(iter(response_iterator))
> 
> last_evaluated_key_first_page = first_page.get('LastEvaluatedKey', None)
> scan_params['ExclusiveStartKey'] = last_evaluated_key_first_page
> response_iterator = paginator.paginate(**scan_params)
> second_page = next(iter(response_iterator))
> 
> # option 2
> scan_params = {
>     'TableName': TABLE_NAME,
>     'PaginationConfig': {'MaxItems': 5, 'PageSize':5, 'StartingToken': None}
> }
> ```
>
> > [!WARNING]
> >
> > Event though the docs state that the response contains a **'NextToken': 'string'**, this is not true.
> > The scan returns **'LastEvaluatedKey'**
>
> 

### Quey

> c
>
> ```python
> from boto3.dynamodb.conditions import And, Attr, Equals, Key
> from collections import Counter
> 
> response = table.scan(ReturnConsumedCapacity='TOTAL')
> Counter([item['internal_brain_id'] for item in  response['Items']]).most_common()
> 
> 
> table.query(
>   IndexName='internal_brain_id_gsi', 
>   KeyConditionExpression=Key("internal_brain_id").eq("saas-manual-testing"),
> )
> 
> 
> ```
>
> 
