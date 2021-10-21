from brownie import FundMe,MockV3Aggregator,accounts,network,config
from scripts.helpful_scripts import (get_account,deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS)

def deploy_fund_me():
    account=get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address=config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
    fund_me=FundMe.deploy(price_feed_address,{"from":account})
    print(f"contract deployed to ${fund_me.address}")
    return fund_me

   
def main():
    deploy_fund_me()