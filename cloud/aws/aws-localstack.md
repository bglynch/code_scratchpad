# AWS CLI & Localstack

## Localstack

https://docs.localstack.cloud/references/internal-endpoints/

```
http://localhost:4566/health
```

## Localstack

```bash
# set aws env vars
export AWS_ACCESS_KEY_ID=mock-access-key-id
export AWS_SECRET_ACCESS_KEY=mock-access-key

# get log group name
aws --endpoint-url http://localhost:4566 --region us-east-1 logs describe-log-groups | cat

# get stream of logs using log group
aws --endpoint-url http://localhost:4566 --region us-east-1 logs tail /aws/lambda/local-sensible-version-1 --follow
```



```bash
# AWS allows you to tail the logs now. Exactly like tail -f. use the following command
# https://stackoverflow.com/questions/34018931/how-to-view-aws-log-real-time-like-tail-f
aws logs tail <log group name> --follow
```



### Make AWS CLI easier to use with Localstack

```bash
code ~/.aws/config

# add the following
[profile localstack]
aws_access_key_id = mock-access-key-id
aws_secret_access_key = mock-access-key
region = us-east-1
output = json

code ~/.zprofile

# add the following
alias aws-local="aws --endpoint-url http://localhost:4566 --profile localstack"

# load in command line
source ~/.aws/config
source ~/.zprofile
```



### Cheatsheet

```bash
# --API Gateway
aws-local apigateway get-rest-apis | jq .
aws-local apigateway get-resources --rest-api-id 79c0tfbke1 | jq -r '.items[ ] | .id+" "+.path'  

# --DynamoDB
aws-local dynamodb list-tables | jq -r .TableNames                      # get tables
aws-local dynamodb describe-table --table-name <table-name> | jq .      # describe a table

# --Lambda
aws-local lambda list-functions | jq . # list all lambda functions

# --S3
aws-local s3 ls   # list buckets
aws-local s3 ls s3://<bucket-name> --recursive # list all files in a bucket
```



```
./bin/local-deploy.js                # deploy
./bin/local-deploy.js --skip-build   # deploy
./bin/local-deploy.js --delete-state # delete 
```
