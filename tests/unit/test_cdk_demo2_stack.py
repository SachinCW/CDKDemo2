import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_demo2.cdk_demo2_stack import CdkDemo2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo2/cdk_demo2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDemo2Stack(app, "cdk-demo2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
