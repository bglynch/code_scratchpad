# DynamoDB CLI

## AWS CLI

#### Credentials

> ```bash
> # with keys
> export AWS_ACCESS_KEY_ID=sample-access-key
> export AWS_SECRET_ACCESS_KEY=sample-secret-key
> export AWS_DEFAULT_REGION=eu-west-1
> 
> # with profile
> export AWS_PROFILE=profile-name
> export AWS_DEFAULT_REGION=eu-west-1
> ```

### Create a Table

> ###### Aim
>
> Create a `Music` table 
>
> - Partition Key - `Artist`
> - Sort Key - `SongTitle`
>
> ```bash
> aws dynamodb create-table \
>     --table-name Music \
>     --attribute-definitions \
>         AttributeName=Artist,AttributeType=S \
>         AttributeName=SongTitle,AttributeType=S \
>     --key-schema \
>         AttributeName=Artist,KeyType=HASH \
>         AttributeName=SongTitle,KeyType=RANGE \
>     --provisioned-throughput \
>         ReadCapacityUnits=10,WriteCapacityUnits=5
> ```
>
> Console Output
>
> ```json
> {
>   "TableDescription":{
>     "AttributeDefinitions":[
>       {
>         "AttributeName":"Artist",
>         "AttributeType":"S"
>       },
>       {
>         "AttributeName":"SongTitle",
>         "AttributeType":"S"
>       }
>     ],
>     "TableName":"Music",
>     "KeySchema":[
>       {
>         "AttributeName":"Artist",
>         "KeyType":"HASH"
>       },
>       {
>         "AttributeName":"SongTitle",
>         "KeyType":"RANGE"
>       }
>     ],
>     "TableStatus":"ACTIVE",
>     "CreationDateTime":"2021-09-01T16:40:02.950000+01:00",
>     "ProvisionedThroughput":{
>       "LastIncreaseDateTime":"1970-01-01T00:00:00+00:00",
>       "LastDecreaseDateTime":"1970-01-01T00:00:00+00:00",
>       "NumberOfDecreasesToday":0,
>       "ReadCapacityUnits":10,
>       "WriteCapacityUnits":5
>     },
>     "TableSizeBytes":0,
>     "ItemCount":0,
>     "TableArn":"arn:aws:dynamodb:us-east-1:000000000000:table/Music"
>   }
> }
> ```

### Check Table Status

> ```bash
> aws dynamodb describe-table --table-name Music | grep TableStatus
> or
> aws dynamodb describe-table --table-name Music | jq .Table.TableStatus
> ```
>
> Console Output
>
> ```json
> "TableStatus": "ACTIVE",
> ```

### Insert Data into Table

> ```bash
> aws dynamodb put-item \
>  --table-name Music  \
>  --item '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'
> ```
>
> Console Output
>
> ```json
> {
> "ConsumedCapacity":{
>  "TableName":"Music",
>  "CapacityUnits":1.0
> }
> }
> ```

### Read Table

> ```bash
> aws dynamodb scan --table-name Music
> ```
>
> Console Output
>
> ```json
> {
> "Items":[
>  {
>    "Artist":{
>      "S":"No One You Know"
>    },
>    "AlbumTitle":{
>      "S":"Somewhat Famous"
>    },
>    "Awards":{
>      "N":"1"
>    },
>    "SongTitle":{
>      "S":"Call Me Today"
>    }
>  }
> ],
> "Count":1,
> "ScannedCount":1,
> "ConsumedCapacity":null
> }
> ```

