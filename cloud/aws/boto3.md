# boto3

boto3 is a **Python SDK** for interacting with services on AWS

Comprised of 2 packages

- botocore (the library providing the low-level functionality shared between the Python SDK and the AWS CLI)
- boto3 (the package implementing the Python SDK itself)



## Configuration

Boto3 adheres to the following lookup order when searching through sources for configuration values:

- A Config object that’s created and passed as the config parameter when creating a client
- Environment variables
- The `~/.aws/config` file

#### Example

> ```python
> import boto3
> from botocore.config import Config
> 
> my_config = Config(
>     region_name = 'us-west-2',
>     signature_version = 'v4',
>     client_context_params={
>         'my_great_context_param': 'foo'
>     }  
>     retries = {
>         'max_attempts': 10,
>         'mode': 'standard'
>     }
> )
> 
> client = boto3.client('kinesis', config=my_config)
> ```

#### Set via env vars

- **AWS_ACCESS_KEY_ID**
  The access key for your AWS account.
- **AWS_SECRET_ACCESS_KEY**
  The secret key for your AWS account.
- **AWS_SESSION_TOKEN**
  The session key for your AWS account. This is only needed when you are using temporary credentials. The AWS_SECURITY_TOKEN environment variable can also be used, but is only supported for backward-compatibility purposes. AWS_SESSION_TOKEN is supported by multiple AWS SDKs in addition to Boto3.
- **AWS_DEFAULT_REGION**
  The default AWS Region to use, for example, us-west-1 or us-west-2.
- **AWS_PROFILE**
  The default profile to use, if any. If no value is specified, Boto3 attempts to search the shared credentials file and the config file for the default profile.
- **AWS_CONFIG_FILE**
  The location of the config file used by Boto3. By default this value is ~/.aws/config. You only need to set this variable if you want to change this location.
- **AWS_SHARED_CREDENTIALS_FILE**
  The location of the shared credentials file. By default this value is ~/.aws/credentials. You only need to set this variable if you want to change this location.
- **AWS_METADATA_SERVICE_TIMEOUT**
  The number of seconds before a connection to the instance metadata service should time out. When attempting to retrieve credentials on an Amazon EC2 instance that is configured with an IAM role, a connection to the instance metadata service will time out after 1 second by default. If you know you’re running on an EC2 instance with an IAM role configured, you can increase this value if needed.
- **AWS_METADATA_SERVICE_NUM_ATTEMPTS**
  When attempting to retrieve credentials on an Amazon EC2 instance that has been configured with an IAM role, Boto3 will make only one attempt to retrieve credentials from the instance metadata service before giving up. If you know your code will be running on an EC2 instance, you can increase this value to make Boto3 retry multiple times before giving up.
- **AWS_MAX_ATTEMPTS**
  The total number of attempts made for a single request. For more information, see the max_attempts configuration file section.
- **AWS_RETRY_MODE**
  Specifies the types of retries the SDK will use. For more information, see the retry_mode configuration file section.



## Credentials

The mechanism in which Boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which Boto3 searches for credentials is:

1. Passing credentials as parameters in the `boto.client()` method

   ```python
   import boto3
   
   # option 1
   client = boto3.client(
       's3',
       aws_access_key_id=ACCESS_KEY,
       aws_secret_access_key=SECRET_KEY,
       aws_session_token=SESSION_TOKEN
   )
   # option 2
   session = boto3.Session(
       aws_access_key_id=ACCESS_KEY,
       aws_secret_access_key=SECRET_KEY,
       aws_session_token=SESSION_TOKEN
   )
   ```

2. Passing credentials as parameters when creating a `Session` object

3. Environment variables

4. Shared credential file (`~/.aws/credentials`) using profile

   ```
   session = boto3.Session(profile_name='dev')
   dev_s3_client = session.client('s3')
   ```

   

5. AWS config file (`~/.aws/config`)

6. Assume Role provider



## Events

Boto3 emits a set of events that users can register to customize clients or resources and modify the behavior of method calls.
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/events.html#boto3-specific-events



## Client (low level)

- provide a low-level interface to AWS whose methods map close to 1:1 with service APIs
- Clients are generated from a JSON service definition file

#### Creation

> ```python
> # Option 01: Create a low-level client with the service name
> sqs = boto3.client('sqs')
> 
> # Option 01: Get from existing resource
> sqs_resource = boto3.resource('sqs')
> # Get the client from the resource
> sqs = sqs_resource.meta.client
> ```

#### Waiters

- Waiters use a client’s service operations to poll the status of an AWS resource and suspend execution until the AWS resource reaches the state that the waiter is polling for or a failure occurs while polling.

> ```python
> # Retrieve waiter instance that will wait till a specified
> # S3 bucket exists
> s3 = boto3.client('s3')
> s3_bucket_exists_waiter = s3.get_waiter('bucket_exists')
> # Begin waiting for the S3 bucket, mybucket, to exist
> s3_bucket_exists_waiter.wait(Bucket='mybucket')
> ```



## Resource (higher level)

> [!NOTE]
>
> SDK team does not intend to add new features to the resources interface in boto3.
> Customers can find access to newer service features through the client interface.

- object-oriented interface to Amazon Web Services
- higher-level abstraction than the raw, low-level calls made by service clients

#### Creation

> ```python
> # Get resources from the default session
> sqs = boto3.resource('sqs')
> s3 = boto3.resource('s3')
> ```

#### Identifiers and attributes

- An identifier is a unique value that is used to call actions on the resource
- An identifier is set at instance creation-time

> ```python
> # SQS Queue (url is an identifier)
> queue = sqs.Queue(url='http://...')
> print(queue.url)
> 
> # S3 Object (bucket_name and key are identifiers)
> obj = s3.Object(bucket_name='boto3', key='test.py')
> print(obj.bucket_name)
> print(obj.key)
> 
> # Raises exception, missing identifier: key!
> obj = s3.Object(bucket_name='boto3')
> ```

#### Actions

- method which makes a call to the service
- Actions may return a low-level response, a new resource instance or a list of new resource instances

> ```python
> # SQS Queue
> messages = queue.receive_messages()
> 
> # SQS Message
> for message in messages:
>     message.delete()
> 
> # S3 Object
> obj = s3.Object(bucket_name='boto3', key='test.py')
> response = obj.get()
> data = response['Body'].read()
> ```



## Session

- A session manages state about a particular configuration.
- When creating a client/resource a default session is crated
- Sessions typically store the following:
  - Credentials
  - AWS Region
  - Other configurations related to your profile

#### Default Session

> ```python
> # Using the default session
> sqs = boto3.client('sqs')
> s3 = boto3.resource('s3')
> ```

#### Custom Session

> ```python
> import boto3
> import boto3.session
> 
> # Create your own session
> my_session = boto3.session.Session()
> 
> # Now we can create low-level clients or resource clients from our custom session
> sqs = my_session.client('sqs')
> s3 = my_session.resource('s3')
> 
> # localstack session
> session = boto3.Session(aws_access_key_id="accesskey", aws_secret_access_key="secretkey")
> ```
>
> You can configure each session with specific credentials, AWS Region information, or profiles. The most common configurations you might use are:
>
> - `aws_access_key_id` - A specific AWS access key ID.
> - `aws_secret_access_key` - A specific AWS secret access key.
> - `region_name` - The AWS Region where you want to create new connections.
> - `profile_name` - The profile to use when creating your session.



## Collections

- A collection provides an iterable interface to a group of resources
- Similar to Django QuerySets
- A collection **seamlessly handles pagination for you**, making it possible to easily iterate over all items from all pages of data

> ```python
> # iteration
> for bucket in s3.buckets.all():
>     print(bucket.name)
>     
> # convert to list
> buckets = list(s3.buckets.all())
> 
> # batch actions
> s3.Bucket('my-bucket').objects.delete()
> ```

#### Page Size

> ```python
> # S3 iterate over all objects 100 at a time
> for obj in bucket.objects.page_size(100):
>     print(obj.key)
> ```



## Paginators

- *Paginators* are a feature of boto3 that act as an abstraction over the process of iterating over an entire result set of a truncated API operation.

#### Creation

- created via the `get_paginator()` method of a boto3 client
- The `get_paginator()` method accepts an operation name and returns a reusable `Paginator` object
- hen call the `paginate` method of the Paginator, passing in any relevant operation parameters to apply to the underlying API operation

> #### Create Paginator
>
> ```python
> # Create a client
> client = boto3.client('s3', region_name='us-west-2')
> 
> # Create a reusable Paginator
> paginator = client.get_paginator('list_objects_v2')
> 
> # Create a PageIterator from the Paginator
> page_iterator = paginator.paginate(Bucket='my-bucket')
> 
> for page in page_iterator:
>     print(page['Contents'])
> ```
>
> #### Customise
>
> - `paginate` method accepts a `PaginationConfig` named argument that can be used to customize the pagination
> - Options
>   - **MaxItems**
>     Limits the maximum number of total returned items returned while paginating.
>   - **StartingToken**
>     Can be used to modify the starting marker or token of a paginator. This argument if useful for resuming pagination from a previous token or starting pagination at a known position.
>   - **PageSize**
>     Controls the number of items returned per page of each result.
>
> ```py
> paginator = client.get_paginator('list_objects_v2')
> page_iterator = paginator.paginate(Bucket='my-bucket',
>                                    PaginationConfig={'MaxItems': 10})
> ```
>
> #### Filtering
>
> - Many Paginators can be filtered server-side with options that are passed through to each underlying API call
>
> ```python
> import boto3
> 
> client = boto3.client('s3', region_name='us-west-2')
> paginator = client.get_paginator('list_objects_v2')
> operation_parameters = {'Bucket': 'my-bucket',
>                         'Prefix': 'foo/baz'}
> page_iterator = paginator.paginate(**operation_parameters)
> for page in page_iterator:
>     print(page['Contents'])
> ```
>
> 



### Links

- [AWS re:Invent 2014 | (DEV307) Introduction to Version 3 of the AWS SDK for Python (Boto)](https://www.youtube.com/watch?v=Cb2czfCV4Dg&list=LL&index=3&ab_channel=AmazonWebServices)
- 