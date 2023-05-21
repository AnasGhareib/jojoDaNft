from thirdweb import ThirdwebSDK
from dotenv import load_dotenv
import os

load_dotenv()

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, "mumbai") # type: ignore

nft_collection = sdk.get_nft_collection("0x8C43ed08bF43c151FD7F6bD9CCcC1D3Ab49b1Af0")



