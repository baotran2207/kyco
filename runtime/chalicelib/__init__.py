# import boto3
# import json


# class Observer:
#     def update(self, message):
#         pass


# class SQSObserver(Observer):
#     def __init__(self, queue_url):
#         self.queue_url = queue_url
#         self.sqs_client = boto3.client("sqs")

#     def update(self, message):
#         # Send the message to the SQS queue
#         self.sqs_client.send_message(
#             QueueUrl=self.queue_url, MessageBody=json.dumps(message)
#         )


# class SNSObserver(Observer):
#     def __init__(self, topic_arn):
#         self.topic_arn = topic_arn
#         self.sqs_client = boto3.client("sqs")
#         self.sns_client = boto3.client("sns")

#     def update(self, message):
#         # Subscribe the SQS queue to the SNS topic
#         queue_url = self.sqs_client.create_queue(QueueName="my-queue")["QueueUrl"]
#         subscription_arn = self.sns_client.subscribe(
#             TopicArn=self.topic_arn,
#             Protocol="sqs",
#             Endpoint=queue_url,
#         )["SubscriptionArn"]

#         # Receive the message from the SQS queue
#         response = self.sqs_client.receive_message(
#             QueueUrl=queue_url, MaxNumberOfMessages=1
#         )
#         if "Messages" in response:
#             message = response["Messages"][0]["Body"]
#             print("Received message:", message)

#             # Delete the message from the SQS queue
#             receipt_handle = response["Messages"][0]["ReceiptHandle"]
#             self.sqs_client.delete_message(
#                 QueueUrl=queue_url, ReceiptHandle=receipt_handle
#             )

#         # Unsubscribe the SQS queue from the SNS topic
#         self.sns_client.unsubscribe(SubscriptionArn=subscription_arn)

#         # Delete the SQS queue
#         self.sqs_client.delete_queue(QueueUrl=queue_url)


# class Observable:
#     def __init__(self):
#         self.observers = []

#     def attach(self, observer):
#         self.observers.append(observer)

#     def detach(self, observer):
#         self.observers.remove(observer)

#     def notify(self, message):
#         for observer in self.observers:
#             observer.update(message)


# class SNSPublisher(Observable):
#     def __init__(self):
#         super().__init__()
#         self.sns_client = boto3.client("sns")
#         self.topic_arn = self.sns_client.create_topic(Name="my-topic")["TopicArn"]

#     def publish(self, message):
#         # Publish the message to the SNS topic
#         self.sns_client.publish(TopicArn=self.topic_arn, Message=json.dumps(message))

#         # Notify the observers of the message
#         self.notify(message)


# # Create an SNS publisher and two observers (one for SQS and one for SNS)
# sns_publisher = SNSPublisher()
# sqs_observer = SQSObserver(
#     queue_url="https://sqs.ap-southeast-1.amazonaws.com/730353997858/KycoGeneric"
# )
# sns_observer = SNSObserver(
#     topic_arn="arn:aws:sns:ap-southeast-1:730353997858:KycoPublisher"
# )

# # Attach the observers to the SNS publisher
# sns_publisher.attach(sqs_observer)
# sns_publisher.attach(sns_observer)

# # Publish a message to the SNS topic
# message = {"data": "hello world"}
# sns_publisher.publish(message)
