from scripts.helpful_scripts import fund_with_link, get_account
from brownie import AdvancedCollectible


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("Collectible created !!!!!!!")
