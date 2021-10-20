from scripts.helpful_scripts import get_account
from brownie import OurToken, network, config
from web3 import Web3

# metodo PatrickCollins1
initial_supply = Web3.toWei(21000000, "ether")

def deploy_our_token():
    account = get_account()
    our_token = OurToken.deploy(
        # metodo Fedro1
        # config["networks"][network.show_active()]["initialSupply"]
        # metodo PatrickCollins2
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("deploy completato")
    return our_token


def main():
    deploy_our_token()
