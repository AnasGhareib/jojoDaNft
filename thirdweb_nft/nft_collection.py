from thirdweb import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
from thirdweb.types.settings.metadata import NFTCollectionContractMetadata
import os

load_dotenv()

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

RPC_URL = "https://mumbai.rpc.thirdweb.com/ed043a51ae23b0db3873f5a38b77ab28175fa496f15d3c53cf70401be89b622a"

provider = Web3(Web3.HTTPProvider(RPC_URL))

signer = Account.from_key(PRIVATE_KEY)

sdk = ThirdwebSDK(provider, signer) # type: ignore


nft_collection = sdk.get_nft_collection("0x8C43ed08bF43c151FD7F6bD9CCcC1D3Ab49b1Af0")

# sdk.deployer.deploy_nft_collection(NFTCollectionContractMetadata(name="jojoDaNft Smart Contract"))



