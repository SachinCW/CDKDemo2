#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_demo2.cdk_demo2_stack import CdkDemo2Stack


app = cdk.App()
CdkDemo2Stack(app, "CdkDemo2Stack",
    )

app.synth()
