from scripts.helpful_scripts import get_account
from brownie import OurToken, network, config


def deploy_our_token():
    account = get_account()
    our_token = OurToken.deploy(
        config["networks"][network.show_active()]["initialSupply"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("deploy completato")
    return our_token


def main():
    deploy_our_token()
