from webbrowser import get
from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_breed, get_account, OPENSEA_URL

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"Number of Collectibles: {number_of_advanced_collectibles}")

    for tokenId in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
        if not advanced_collectible.tokenURI(tokenId).startswith("https://"):
            print(f"Setting tokenURI of {tokenId}")
            set_tokenURI(tokenId, advanced_collectible, dog_metadata_dic[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Hit refresh after around 20 minutes")
