import datetime
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash):
        self.timeStamp = datetime.datetime.now
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generatehash()

    def generatehash(self):
        blockHeader = str(self.timeStamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        blockHash = sha256(blockHeader.encode)
        return blockHash.hexdigest()
    
    def printContents(self):
        print("timestamp: ", self.timeStamp)
        print("transactions: " , self.transactions)
        print("current hash: ", self.generatehash)
        print("previous hash: ", self.previous_hash)
