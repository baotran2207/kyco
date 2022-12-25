#!/usr/bin/env python3
try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from dotenv import load_dotenv
from stacks.chaliceapp import ChaliceApp

load_dotenv("../.prod")

app = cdk.App()
ChaliceApp(app, "BaoTran-Backend")

app.synth()
