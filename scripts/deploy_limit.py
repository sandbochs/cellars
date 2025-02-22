from brownie import CellarPoolShareLimitETHUSDT, accounts

def main():
    acct = accounts.load("deployer_account")
    name = "Cellar Pool Share Limited Test ETH USDT"
    symbol = "CPST"
    token0 = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    token1 = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    cellarTickInfo = [[0,-180000,-210000,1]]
    CellarPoolShareLimitETHUSDT.deploy(name, symbol, token0, token1, 3000, cellarTickInfo, {"from":acct})