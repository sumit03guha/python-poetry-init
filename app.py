# Import the Web3 module from the web3 package
from web3 import Web3

# Create a Web3 instance and connect to an Ethereum node via HTTP
w3 = Web3(Web3.HTTPProvider("https://rpc.mevblocker.io"))

# Retrieve the balance of the account associated with the ENS name 'vitalik.eth'
# The balance is initially in wei (the smallest denomination of ETH)
balance_wei = w3.eth.get_balance("vitalik.eth")

# Convert the balance from wei to ether for a more readable format
balance_eth = Web3.from_wei(balance_wei, "ether")

# Print the balance in ether
print(f"The balance of Vitalik on Ethereum mainnet is {balance_eth} ETH")
