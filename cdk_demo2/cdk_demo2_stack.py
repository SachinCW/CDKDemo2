from aws_cdk import (
    aws_sqs as sqs,
    Stack
)
from constructs import Construct

class CdkDemo2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(self, "TestingCdkQueue",
                          fifo=True,  # Enable FIFO mode
                          queue_name="testingcdk.fifo")  # Specify the queue name



