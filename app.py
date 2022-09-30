#!/usr/bin/env python3

import aws_cdk as cdk

from my_wallet.my_wallet_stack import MyWalletStack


app = cdk.App()
MyWalletStack(app, "my-wallet")

app.synth()
