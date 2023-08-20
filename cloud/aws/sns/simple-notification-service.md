# AWS SQS

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available **hosted queue** that lets you integrate and decouple distributed software systems and components.

#### Queue Types

- FIFO (First In First Out)
  - designed to enhance messaging between applications when the order of operations and events is critical, or where duplicates can't be tolerated.
  - FIFO queues also provide exactly-once processing
  -  FIFO queue must end with the `.fifo` suffix

### Retention

Amazon SQS automatically deletes messages that have been in a queue for more than the maximum message retention period. The default message retention period is 4 days. However, you can set the message retention period to a value from 60 seconds to 1,209,600 seconds (14 days) using the `SetQueueAttributes` action.

## Documentation Links

[AWS CLI Docs](https://docs.aws.amazon.com/cli/latest/reference/sqs/)

[AWS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

[AWS Pyhton Code Samples](https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-python-example_code-sqs.html)

[Boto3 SQS Examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-examples.html)

[Boto3 SQS Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html)



| Permissions                                                  | Queues                                                       | Messages                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [AddPermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html) | [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) | [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) |
| [RemovePermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_RemovePermission.html) | [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html) | [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) |
|                                                              | [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) | [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) |
|                                                              | [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) | [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html) |
|                                                              | [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) | [DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html) |
|                                                              | [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html) | [ChangeMessageVisibility](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html) |
|                                                              | [ListQueueTags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html) | [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html) |
|                                                              | [PurgeQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html) |                                                              |
|                                                              | [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) |                                                              |
|                                                              | [TagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_TagQueue.html) |                                                              |
|                                                              | [UntagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_UntagQueue.html) |                                                              |

## AWS CLI

```bash
aws sqs add-permission
aws sqs remove-permission

aws sqs create-queue
aws sqs delete-queue
aws sqs list-dead-letter-source-queues
aws sqs list-queue-tags
aws sqs list-queues
aws sqs purge-queue
aws sqs set-queue-attributes
aws sqs tag-queue
aws sqs untag-queue
aws sqs get-queue-attributes
aws sqs get-queue-url

aws sqs send-message
aws sqs receive-message
aws sqs delete-message
aws sqs send-message-batch
aws sqs delete-message-batch
aws sqs change-message-visibility
aws sqs change-message-visibility-batch
```

### Create Queue

```bash
create-queue --queue-name <value>
[--attributes <value>] [--tags <value>] [--cli-input-json <value>] [--generate-cli-skeleton <value>]
```

#### Example

Creates a queue with the specified name, sets the message retention period to 3 days (3 days * 24 hours * 60 minutes * 60 seconds), and sets the queue's dead letter queue to the specified queue with a maximum receive count of 1,000 messages

###### Command Line

```bash
aws sqs create-queue --queue-name MyQueue --attributes file://create-queue.json
```

##### create-queue.json

```json
{
  "RedrivePolicy": "{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:80398EXAMPLE:MyDeadLetterQueue\",\"maxReceiveCount\":\"1000\"}",
  "MessageRetentionPeriod": "259200"
}
```

##### Output

```json
{
  "QueueUrl": "https://queue.amazonaws.com/80398EXAMPLE/MyQueue"
}
```



### List Queue

##### List Queue

```bash
list-queues
[--queue-name-prefix <value>] [--cli-input-json <value>] [--starting-token <value>]
[--page-size <value>] [--max-items <value>] [--generate-cli-skeleton <value>]
```

#### Example

List all queues

```bash
aws sqs list-queues
```

lists only queues that start with "My"

```
aws sqs list-queues --queue-name-prefix My
```



### Get Queue URL

```bash
get-queue-url --queue-name <value>
[--queue-owner-aws-account-id <value>] [--cli-input-json <value>] [--generate-cli-skeleton <value>]
```

##### Example

Get "MyQueue" url

```bash
aws sqs get-queue-url --queue-name MyQueue
```

Output

```json
{
  "QueueUrl": "https://queue.amazonaws.com/80398EXAMPLE/MyQueue"
}
```



### Send Message

```bash
send-message --queue-url <value> --message-body <value>
[--delay-seconds <value>] [--message-attributes <value>] [--message-system-attributes <value>]
[--message-deduplication-id <value>] [--message-group-id <value>] [--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

#### Example

sends a message with the specified message body, delay period, and message attributes, to the specified queue

```bash
aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue 
--message-body "Information about the largest city in Any Region." 
--delay-seconds 10 
--message-attributes file://send-message.json
```

```json
// send-message.json
{
  "City": {
    "DataType": "String",
    "StringValue": "Any City"
  },
  "Greeting": {
    "DataType": "Binary",
    "BinaryValue": "Hello, World!"
  },
  "Population": {
    "DataType": "Number",
    "StringValue": "1250800"
  }
}
```

##### Output

```json
{
  "MD5OfMessageBody": "51b0a325...39163aa0",
  "MD5OfMessageAttributes": "00484c68...59e48f06",
  "MessageId": "da68f62c-0c07-4bee-bf5f-7e856EXAMPLE"
}
```



### Recieve Message

```bash
receive-message --queue-url <value>
[--attribute-names <value>] [--message-attribute-names <value>] [--max-number-of-messages <value>]
[--visibility-timeout <value>] [--wait-time-seconds <value>] [--receive-request-attempt-id <value>]
[--cli-input-json <value>] [--generate-cli-skeleton <value>]
```

#### Example

receives up to 10 available messages, returning all available attributes

```bash
aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue 
--attribute-names All --message-attribute-names All --max-number-of-messages 10
```

##### Output

```json
{
  "Messages": [
    {
      "Body": "My first message.",
      "ReceiptHandle": "AQEBzbVv...fqNzFw==",
      "MD5OfBody": "1000f835...a35411fa",
      "MD5OfMessageAttributes": "9424c491...26bc3ae7",
      "MessageId": "d6790f8d-d575-4f01-bc51-40122EXAMPLE",
      "Attributes": {
        "ApproximateFirstReceiveTimestamp": "1442428276921",
        "SenderId": "AIDAIAZKMSNQ7TEXAMPLE",
        "ApproximateReceiveCount": "5",
        "SentTimestamp": "1442428276921"
      },
      "MessageAttributes": {
        "PostalCode": {
          "DataType": "String",
          "StringValue": "ABC123"
        },
        "City": {
          "DataType": "String",
          "StringValue": "Any City"
        }
      }
    }
  ]
}
```



---

