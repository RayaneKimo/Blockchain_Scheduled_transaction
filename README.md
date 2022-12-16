# How to schedule a transaction of etherium using python

The main principle is that : I'm splitting a transaction in two. The first from the sender to the Contract by storing its ID (calculated),
the second as soon as the time arrives, this ID is used to restore the attributes from a mapping and then send a transaction from the Contract
to the recipient.

This ID is artificial (not the ID returned by the blockchain) calculated from 4 parameters (recipient, timestamp, amount and sender) which makes it unique.

How to Setup it :
1- Start your Ganache network for the testing purposes.
2 - Deploy the smart contract in the blockchain using the 
3 - 
2 - Just create a '.env' file in the same folder as the '.py' and '.ipynb' files containing the Private keys as values and the user names as variables.
2 - Deploy a new contract and replace its address in the "Scheduler_Sender.py" file
3 - To launch the file, just type in the terminal: python Scheduler_Sender.py "Sender" "Receiver" amount timestamp(minutes)
