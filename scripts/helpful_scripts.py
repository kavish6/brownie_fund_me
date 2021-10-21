from brownie import accounts,network,config,MockV3Aggregator
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]
DECIMAL =8
STARTING_PRICE=200000000000
def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])  
def deploy_mocks():
     print(f"the active network is ${network.show_active()}")
     print(f"deploying mocks...")
     if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(DECIMAL,STARTING_PRICE,{"from":get_account()})
     print(f"mocks deployed") 
     #Todo:add ganache ui to network list under ethereum