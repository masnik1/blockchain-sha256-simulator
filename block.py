"""
BLOCKCHAIN SIMULATOR EXAMPLE IN PYTHON
CODE BASED ON: https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531

MADE BY:
PAULO MASNIK
"""

import hashlib
import json
from time import time

#Criando uma classe chamada blockchain
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="TESTE", proof=100)

    def new_block(self, proof, previous_hash=None):
        #Definindo o bloco
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash_block(self.chain[-1])
        }
        #Limpando transacoes pendentes
        self.pending_transactions = []
        self.chain.append(block)

        #Retorna o bloco
        return block

    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash_block(self, block):
        #Adicionando a "criptografia = sha256 mesma do BTC"
        string_obj = json.dumps(block, sort_keys=True)
        block_str = string_obj.encode()

        raw_hash = hashlib.sha256(block_str)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
first_trade = blockchain.new_transaction("Paulo", "Joe", "0.0005 BTC")
blockchain.new_block(12345)

second_trade = blockchain.new_transaction("Paulo", "Julie", "0.5 BTC")
blockchain.new_block(6789)

print(f"Blockchain: {blockchain.chain}")