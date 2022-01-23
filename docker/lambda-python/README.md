# AWS Lambda Python

Useful Links

https://towardsdatascience.com/aws-lambda-with-custom-docker-images-as-runtime-9645b7baeb6f

https://aws-lambda-for-python-developers.readthedocs.io/en/latest/02_event_and_context/

### What is needed?

- Dockerfile
- Python file with a handler function

## Dockerfile

```dockerfile
FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "app.handler" ]
```

#### Comments

`public.ecr.aws/lambda/python:3.8`: this is Amazond version of Linux, which is CentOS-based

Enviornment variables of the Image

```bash
HOME=/root
HOSTNAME=246baa64dd3f
LAMBDA_RUNTIME_DIR=/var/runtime
LAMBDA_TASK_ROOT=/var/task
LANG=en_US.UTF-8
LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
PWD=/var/task
SHLVL=1
TERM=xterm
TZ=:/etc/localtime
_=/usr/bin/env
```

To install packages on the Image, use `yum`

```bash
yum install iputils  # installs iputils, e.g ping
```



## Python File

##### app.py

```python
import json

def handler(event, lambda_context):
    environment_variables = {k:v for k, v in sorted(os.environ.items())}
    print(event)
    print(vars(lambda_context))
    print(environment_variables)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
```



### Command Line

Build the docker image and run a container on port 8080.
The run command runs the image as a container and starts up an endpoint locally at `localhost:9000/2015-03-31/functions/function/invocations`

```bash
$ docker build -t docker-lambda .

$ docker run -d -p 8080:8080 docker-lambda
3ad8a3a5a5aca2452d6b03e8549d80b816e9175669ad481377be2c80fa3c4e98
```

Test the application locally.

POST Request

```bash
$ curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'

{
  "statusCode": 200,
  "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {\"payload\": \"hello world!\"}}"
}
```

View print statement using docker logs.

```bash
$ docker logs 3ad8a3a5a5ac  # 3ad8a3a5a5ac is the container Id

START RequestId: 74e8952b-cd47-483b-87df-e20130d86f1e Version: $LATEST
# print(event)
{'payload': 'hello world!'}

# print(vars(lambda_context))
{
	'aws_request_id': '74e8952b-cd47-483b-87df-e20130d86f1e', 
	'log_group_name': '/aws/lambda/Functions', 
	'log_stream_name': '$LATEST', 
	'function_name': 'test_function', 
	'memory_limit_in_mb': '3008', 
	'function_version': '$LATEST', 
	'invoked_function_arn': 'arn:aws:lambda:us-east-1:012345678912:function:test_function', 
	'client_context': None, 
	'identity': <__main__.CognitoIdentity object at 0x7f03638e9970>, 
	'_epoch_deadline_time_in_ms': 1633089355620
}

# print(environment_variables)
{
	'AWS_ACCESS_KEY_ID': '', 
	'AWS_EXECUTION_ENV': 'AWS_Lambda_python3.8', 
	'AWS_LAMBDA_FUNCTION_MEMORY_SIZE': '3008', 
	'AWS_LAMBDA_FUNCTION_NAME': 'test_function', 
	'AWS_LAMBDA_FUNCTION_VERSION': '$LATEST', 
	'AWS_LAMBDA_LOG_GROUP_NAME': '/aws/lambda/Functions', 
	'AWS_LAMBDA_LOG_STREAM_NAME': '$LATEST', 
	'AWS_LAMBDA_RUNTIME_API': '127.0.0.1:9001', 
	'AWS_SECRET_ACCESS_KEY': '', 
	'AWS_SESSION_TOKEN': '', 
	'HOME': '/root', 
	'HOSTNAME': 'cb3405736b73', 
	'LAMBDA_RUNTIME_DIR': '/var/runtime', 
	'LAMBDA_TASK_ROOT': '/var/task', 
	'LANG': 'en_US.UTF-8', 
	'LD_LIBRARY_PATH': '/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib', 
	'PATH': '/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin', 
	'PWD': '/var/task', 
	'PYTHONPATH': '/var/runtime', 
	'SHLVL': '0', 
	'TZ': ':/etc/localtime', 
	'_HANDLER': 'app.handler'
}

END RequestId: 74e8952b-cd47-483b-87df-e20130d86f1e
```



GET Request

As this is a request to a lambda function it expects an event, making a GET request with no body results in an error

```bash
$ curl "http://localhost:8080/2015-03-31/functions/function/invocations"

{
	"errorMessage": "Unable to unmarshal input: Expecting value: line 1 column 1 (char 0)", 
	"errorType": "Runtime.UnmarshalError", 
	"stackTrace": []
}
```

```bash
$ curl "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{}'

{
	"statusCode": 200, 
	"body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {}}"
}
```

