
# How to schedule a transaction of etherium using python


The main principle is that : I'm splitting a transaction in two. The first from the sender to the Contract by storing its ID (calculated),
the second as soon as the time arrives, this ID is used to restore the attributes from a mapping and then send a transaction from the Contract
to the recipient.

This ID is artificial (not the ID returned by the blockchain) calculated from 4 parameters (recipient, timestamp, amount and sender) which makes it unique.

## How to Setup it :
1. Start your Ganache network for the testing purposes.
2. Deploy the smart contract in the blockchain using the **Contract_deploiment.ipynb**
3. Get the adress of the contract and paste it in the **Scheduler_Sender.py**
4. Just create a '.env' file in the same folder as the '.py' and '.ipynb' files containing the Private keys as values and the user names as variables.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in the same folder of your python code, each one having his primary key (you can get them from Ganache app ) :

`Alice`

`Bob`

`Eve`



## Test
Get into your terminal and tap :
```
python Scheduler_Sender.py "Sender" "Receiver" amount timestamp(minutes)
```



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.rayanekimouche.tech)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rayane-kimouche-092589172)

