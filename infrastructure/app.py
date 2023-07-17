#!/usr/bin/env python3
try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from dotenv import dotenv_values, load_dotenv

# from stacks.db import KycoDB
from stacks.chaliceapp import ChaliceApp
from stacks.ui import ReactApp

load_dotenv("../.prod")

env_vars = dict(dotenv_values("../.prod"))

app = cdk.App()

# KycoDB(app, "kyco-db", env_vars=env_vars)
ChaliceApp(app, "kyco-chalice-id", env_vars=env_vars)
# ReactApp(app, "kyco-ui-id", env_vars=env_vars)

app.synth()
