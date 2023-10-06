#!/usr/bin/env python3
try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from dotenv import dotenv_values

# from stacks.db import KycoDB
from stacks.chaliceapp import ChaliceApp

stacks_envs = [
    # ("dev", "../.dev"),
    # ("staging", "../.staging"),
    ("prod", "../.prod"),
]
app = cdk.App()

for env, env_file in stacks_envs:
    env_vars = dict(dotenv_values(env_file))
    app_name = f"Kyco{env.capitalize()}"
    # ChaliceApp(app, app_name, env_vars=env_vars)


# KycoDB(app, "kyco-db", env_vars=env_vars)
ChaliceApp(app, "kyco-chalice-id", env_vars=env_vars)
# ReactApp(app, "kyco-ui-id", env_vars=env_vars)

app.synth()
