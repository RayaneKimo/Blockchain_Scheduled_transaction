from web3 import Web3
import os
from dotenv import load_dotenv
import time
from web3 import exceptions
import sys

load_dotenv()
#Se connecter au réseau etherium de Ganache
network = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

#On prend comme users de test les 3 premières addresses
accounts = network.eth.accounts[:3]

users = {"Alice" : accounts[0] , "Bob" : accounts[1] ,"Eve" : accounts[2] }

#Bytecode et l'abi de mon smart contrat
bytecode = "608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610c73806100606000396000f3fe6080604052600436106100745760003560e01c8063781e51e41161004e578063781e51e4146101295780639fcc127c14610145578063d7cc802714610161578063e6d25245146101a25761007b565b8063030d1f9a1461008057806316ada547146100c157806350c87043146100ec5761007b565b3661007b57005b600080fd5b34801561008c57600080fd5b506100a760048036038101906100a29190610949565b6101be565b6040516100b8959493929190610a07565b60405180910390f35b3480156100cd57600080fd5b506100d6610241565b6040516100e39190610afa565b60405180910390f35b3480156100f857600080fd5b50610113600480360381019061010e91906108e2565b610249565b6040516101209190610a9f565b60405180910390f35b610143600480360381019061013e9190610949565b610282565b005b61015f600480360381019061015a91906108a2565b6105da565b005b34801561016d57600080fd5b5061018860048036038101906101839190610949565b610754565b604051610199959493929190610a07565b60405180910390f35b6101bc60048036038101906101b79190610875565b6107d7565b005b60016020528060005260406000206000915090508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060020154908060030154908060040160009054906101000a900460ff16905085565b600042905090565b6000848484846040516020016102629493929190610a5a565b604051602081830303815290604052805190602001209050949350505050565b60006001600083815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050600060016000848152602001908152602001600020600301549050600060016000858152602001908152602001600020600201549050600015156001600086815260200190815260200160002060040160009054906101000a900460ff1615151461035d576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161035490610aba565b60405180910390fd5b81421161039f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161039690610ada565b60405180910390fd5b8273ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051600060405180830381858888f193505050501580156103e5573d6000803e3d6000fd5b50600180600086815260200190815260200160002060040160006101000a81548160ff02191690831515021790555060016000858152602001908152602001600020600260008681526020019081526020016000206000820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060028201548160020155600382015481600301556004820160009054906101000a900460ff168160040160006101000a81548160ff02191690831515021790555090505060016000858152602001908152602001600020600080820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff0219169055600282016000905560038201600090556004820160006101000a81549060ff0219169055505050505050565b60006105e883833433610249565b90506040518060a001604052808473ffffffffffffffffffffffffffffffffffffffff1681526020013373ffffffffffffffffffffffffffffffffffffffff168152602001348152602001838152602001600015158152506001600083815260200190815260200160002060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550604082015181600201556060820151816003015560808201518160040160006101000a81548160ff0219169083151502179055509050507ff760c4735d60e37a81846da3703ad6f7228cbec08926c227a4b6a54bcfe9bd57816040516107479190610a9f565b60405180910390a1505050565b60026020528060005260406000206000915090508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060020154908060030154908060040160009054906101000a900460ff16905085565b8073ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f1935050505015801561081d573d6000803e3d6000fd5b5050565b60008135905061083081610be1565b92915050565b60008135905061084581610bf8565b92915050565b60008135905061085a81610c0f565b92915050565b60008135905061086f81610c26565b92915050565b60006020828403121561088b5761088a610b8a565b5b600061089984828501610821565b91505092915050565b600080604083850312156108b9576108b8610b8a565b5b60006108c785828601610836565b92505060206108d885828601610860565b9150509250929050565b600080600080608085870312156108fc576108fb610b8a565b5b600061090a87828801610821565b945050602061091b87828801610860565b935050604061092c87828801610860565b925050606061093d87828801610821565b91505092959194509250565b60006020828403121561095f5761095e610b8a565b5b600061096d8482850161084b565b91505092915050565b61097f81610b38565b82525050565b61098e81610b26565b82525050565b61099d81610b4a565b82525050565b6109ac81610b56565b82525050565b60006109bf600a83610b15565b91506109ca82610b8f565b602082019050919050565b60006109e2601483610b15565b91506109ed82610bb8565b602082019050919050565b610a0181610b80565b82525050565b600060a082019050610a1c6000830188610976565b610a296020830187610985565b610a3660408301866109f8565b610a4360608301856109f8565b610a506080830184610994565b9695505050505050565b6000608082019050610a6f6000830187610985565b610a7c60208301866109f8565b610a8960408301856109f8565b610a966060830184610985565b95945050505050565b6000602082019050610ab460008301846109a3565b92915050565b60006020820190508181036000830152610ad3816109b2565b9050919050565b60006020820190508181036000830152610af3816109d5565b9050919050565b6000602082019050610b0f60008301846109f8565b92915050565b600082825260208201905092915050565b6000610b3182610b60565b9050919050565b6000610b4382610b60565b9050919050565b60008115159050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b600080fd5b7f6e6f74206c697374656400000000000000000000000000000000000000000000600082015250565b7f796f752063616e27742073656e64206e6f772021000000000000000000000000600082015250565b610bea81610b26565b8114610bf557600080fd5b50565b610c0181610b38565b8114610c0c57600080fd5b50565b610c1881610b56565b8114610c2357600080fd5b50565b610c2f81610b80565b8114610c3a57600080fd5b5056fea2646970667358221220766ba8676814be5f150d761e7740966a7df548df199f022ad7fc8ae4996a33ce64736f6c63430008070033"
abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "ID",
                "type": "bytes32"
            }
        ],
        "name": "ident",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address payable",
                "name": "_dest",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_timestamp",
                "type": "uint256"
            }
        ],
        "name": "ScheduleTo",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            }
        ],
        "name": "sendTo",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "ID",
                "type": "bytes32"
            }
        ],
        "name": "SendWhenTime",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_dest",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_timestamp",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "_sender",
                "type": "address"
            }
        ],
        "name": "GetId",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "name": "tableau_transaction_done",
        "outputs": [
            {
                "internalType": "address payable",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "timestamp",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "done",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "name": "tableau_transaction_remain",
        "outputs": [
            {
                "internalType": "address payable",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "timestamp",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "done",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "time",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

#l'adresse du contrat déja deployé
contract = '0x4847146857688B5CC80D01D8d975799d4584cE1B'

storage = network.eth.contract(address = contract, abi= abi)


#function qui signe et envoie une transaction
def sendTransaction(transction : str, me : str) :
    sign_store = network.eth.account.sign_transaction(transction, private_key=os.getenv(me))
    send_store = network.eth.send_raw_transaction(sign_store.rawTransaction)
    store_receip = network.eth.wait_for_transaction_receipt(send_store)
    return store_receip


# function qui planifie l'envoi d'une transaction

def ScheduleTo(me : str, reveiver : str, amount : int, timeSchedule : int) :
    dest =users[reveiver]     # destinataire
    timestamp = int(time.time() + 60 * float(timeSchedule))   # le temps planifié  # timeSchedule en minutes
    amount = amount                     # montant en ether

    transaction_scheduled = storage.functions.ScheduleTo(dest, timestamp).buildTransaction({
        "gasPrice" : network.eth.gas_price,
        "value" : network.toWei(amount, 'ether') ,
        "chainId": network.eth.chain_id,
        "from": users[me],
        "nonce": network.eth.getTransactionCount(users[me])
    })

    #Premier envoi : du sender vers le smart contrat
    receip_scheduled = sendTransaction(transaction_scheduled, me)

    #Prendre l'ID (unique) de cette transaction déclanché par l'event
    ID_scheduled = receip_scheduled["logs"][0]["data"]


    while int(time.time()) < timestamp + 3  :   #COMPTEUR

        try :
            end_transaction = storage.functions.SendWhenTime(ID_scheduled).buildTransaction({
                "gasPrice" : network.eth.gas_price,
                "chainId": network.eth.chain_id,
                "from": users[me],
                "nonce": network.eth.getTransactionCount(users[me])
            })

            #Second envoi : du smart contrat vers le destinataire quand le temps arrive
            end_receip = sendTransaction(end_transaction, me)

            return end_receip, ID_scheduled



        except exceptions.SolidityError as error:
            #Ce block d'exception est la cause du (revert) du smart contrat lorsque Now < timestamp
            remaining = timestamp + 3 - int(time.time())  # temps restant pour l'envoi
            print('\033[93m'+"Transaction will be sent in : {}".format(time.strftime('%H:%M:%S', time.gmtime(remaining))) + '\033[0m', end='\r')
            if(int(time.time()) > timestamp + 12 ) :
                break             # En cas d'erreur et on a dépassé le timestamp planifié de 12s alors on annule le processus
            time.sleep(1)         # endormir le processus pour l'efficacité du processeur





if __name__ == "__main__":
    result, ID = ScheduleTo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(result)
    print('\x1b[6;30;42m' + "Transaction ID : {} sent successfully ! ".format(ID) + '\x1b[0m' )


