## Setting Up Env to Work with DynamoDB

### Locally

#### Run on Localstack for DynamoDB

```yaml
# docker-compose.yml
version: '3.0'

services:
  localstack:
    image: localstack/localstack:latest
    environment:
      - AWS_DEFAULT_REGION=us-east-1
      - EDGE_PORT=4566
      - SERVICES=dynamodb
    ports:
      - '4566:4566'
    volumes:
      - "${TMPDIR:-/tmp/localstack}:/tmp/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

```bash
# command line
docker compose up
```

```bash
# command line
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_REGION=us-east-1

aws --endpoint-url http://localhost:4566 <aws command>
```

#### DynamoDB Local

```yaml
# docker-compose.yml
version: '3.8'
services:
  dynamodb-local:
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
```

```bash
# command line
docker-compose up
```

```bash
# command line
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_REGION=us-east-1

aws --endpoint-url http://localhost:8000 <aws command>
```

