# API Gateway

### What is an API

#### Example: REST API

- Client makes a request to an API
- API will talk to services behind it (AWS Lambda)
- API returns a response to the Client

<img src="api-gateway.assets/image-20230502140345271.png" alt="image-20230502140345271" style="zoom: 33%;" /> 

### What is API Gateway

- A fully managed service that makes it easy for developers to create, publish, maintain, monitor and secure APIs at any scale.

### Architecture

> ![image-20230502141041084](api-gateway.assets/image-20230502141041084.png)

### How to talk to API Gateway

- Edge optimised
  - designed for globally distributed set of clients
- Regional
  - recommended for **general use cases**
  - used for **clients in the same region**
- Private
  - Only accessible from withing a VPC(and networks connected to a VPC)
  - APIs used internally or by private microservices



### What can API Gateway talk to?

- AWS Services
  - Lambda
- Stuff inside VPC
- Anything that has an HTTP endpoint



### Supported Protocols

<img src="api-gateway.assets/image-20230502141415081.png" alt="image-20230502141415081" style="zoom: 33%;" /> 

- HTTP
  - Request and Response
  - "I'm asking you something, and you tell me something back"
- Websocket
  - "I'm going to connect to you....and youre going to be connected to me......amd we're going to be sending info back and forth as needed"
  - Good for chat clients



### Integrations

> <img src="api-gateway.assets/image-20230502142025220.png" alt="image-20230502142025220" style="zoom: 33%;" /> 



### Lambda funciton Integration Options

#### Proxy Connection

> <img src="api-gateway.assets/image-20230502142344457.png" alt="image-20230502142344457" style="zoom:33%;" /> 
>
> - Client sends request
>
> - API Gateway wraps it with some metadata
>
>   - adds contextual data you may need on the backend
>
> - Lambda get that and sends it back
>
>   - API Gateway doesnt handle status codes, headers etc...
>
>   > <img src="api-gateway.assets/image-20230502142617224.png" alt="image-20230502142617224" style="zoom:33%;" /> 

#### Integration

> <img src="api-gateway.assets/image-20230502142905654.png" alt="image-20230502142905654" style="zoom:33%;" /> 
>
> - Client sends request
>
> - VTL used to modify the request
>
>   - can use logic
>   - can use static data
>
> - Lambda gets that and send back response
>
>   > <img src="api-gateway.assets/image-20230502143101646.png" alt="image-20230502143101646" style="zoom:33%;" /> 
>   >
>   > - response can be modified again using VTL
>
> #### VTL Example
>
> <img src="api-gateway.assets/image-20230502143204416.png" alt="image-20230502143204416" style="zoom:40%;" /> 

#### Integration Flow

<img src="api-gateway.assets/image-20230502143513644.png" alt="image-20230502143513644" style="zoom:40%;" /> 

- Method Request
  - Can you validation before a request goes to the Lambda service



### Authorization

<img src="api-gateway.assets/image-20230502143851518.png" alt="image-20230502143851518" style="zoom:33%;" /> 

Can attached Authoriser to API Gateway



## Optimising

### Caching

<img src="api-gateway.assets/image-20230502144352586.png" alt="image-20230502144352586" style="zoom:33%;" /> 

- Can turn on caching
- Managed through API Gateway
- Can be set up for stage
  - Can have caching turned off for dev and turned on for prod

### Throttling

<img src="api-gateway.assets/image-20230502144429688.png" alt="image-20230502144429688" style="zoom:33%;" /> 



### VPC

<img src="api-gateway.assets/image-20230502145539558.png" alt="image-20230502145539558" style="zoom:45%;" /> 



### Web Applicaiton Firewall

<img src="api-gateway.assets/image-20230502145940391.png" alt="image-20230502145940391" style="zoom:33%;" /> 

- Can blacklist
  - IP address
  - geolocation
  - request size limit

### Resource Policies

<img src="api-gateway.assets/image-20230502150241770.png" alt="image-20230502150241770" style="zoom:50%;" />

### Client Certificates

<img src="api-gateway.assets/image-20230502150351384.png" alt="image-20230502150351384" style="zoom:50%;" /> 

### Swagger/OpenAPI import and export

<img src="api-gateway.assets/image-20230502150601639.png" alt="image-20230502150601639" style="zoom:50%;" />



---

## Links

- Youtube: [AWS re:Invent 2019: [REPEAT 2] I didn’t know Amazon API Gateway did that (SVS212-R2)](https://www.youtube.com/watch?v=yfJZc3sJZ8E&ab_channel=AWSEvents)

