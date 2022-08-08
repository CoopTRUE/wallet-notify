from web3 import Web3
from config import ADDRESS, RPC, ABI

web3 = Web3(Web3.HTTPProvider(RPC))
if web3.isConnected():
  print("Connected to RPC")
else:
  raise Exception("Could not connect to RPC")

contract = web3.eth.contract(address=ADDRESS, abi=ABI)