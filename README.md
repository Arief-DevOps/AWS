This project consist of three challenges

Challenge #1

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

Resources need to be created / installed :

Custom VPC

2 Subnets (Public)

1 Subnet (Private)

2 EC2 Instances

Security Group

Elastic IP

NAT Gateway

Internet Gateway

Route Table

Application Load Balancer

Apache Webserver

MySQL DB

![image](https://user-images.githubusercontent.com/119723513/205814663-54c66fe7-0f57-41d6-b4c9-56bf79e3c7d1.png)


Challenge #2

We need to write code that will query the meta data of an instance within AWS and provide a json formatted output. The choice of language and implementation is up to you. Bonus Points The code allows for a particular data key to be retrieved individually Hints · Aws Documentation (https://docs.aws.amazon.com/) · Azure Documentation (https://docs.microsoft.com/en-us/azure/?product=featured) · Google Documentation (https://cloud.google.com/docs)

Challenge #3

We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you. Example Inputs object = {“a”:{“b”:{“c”:”d”}}} key = a/b/c object = {“x”:{“y”:{“z”:”a”}}} key = x/y/z value = a
