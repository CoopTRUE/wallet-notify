from config import ADDRESS, COIN_ADDRESS, RPC, ABI
from web3 import Web3
from win10toast import ToastNotifier
import time

toast = ToastNotifier()

web3 = Web3(Web3.HTTPProvider(RPC))
if web3.isConnected():
  print("Connected to RPC")
else:
  raise Exception("Could not connect to RPC")

contract = web3.eth.contract(address=COIN_ADDRESS, abi=ABI)
def get_balance():
  balance = contract.functions.balanceOf(ADDRESS).call()
  return round(web3.fromWei(balance, 'ether'), 2)

current_balance = get_balance()
while True:
  print("Waiting 10 seconds...")
  time.sleep(10)
  new_balance = get_balance()
  if (new_balance > current_balance):
    toast.show_toast(
      f"Received {new_balance - current_balance}!",
      f"New balance: {new_balance}",
      duration=10,
      threaded=True
    )
  if (new_balance < current_balance):
    toast.show_toast(
      f"Lost {current_balance - new_balance}!",
      f"New balance: {new_balance}",
      duration=10,
      threaded=True
    )
  current_balance = new_balance