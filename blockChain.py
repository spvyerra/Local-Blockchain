from block import Block

class BlockChain:
    def __init__ (self):
        self.chain = []
        self.unconfirmedTransactions = []
        self.genesisBlock()

    def genesisBlock(self):
        transactions = []
        genesisBlock = Block(transactions, "0")
        genesisBlock.generatehash()
        self.chain.append(genesisBlock)

    def addBlock(self, transactions):
        previousHash = (self.chain[len(self.chain) - 1]).hash
        newBlock = Block(transactions, previousHash)
        newBlock.generatehash
        proof = self.proofOfWork(newBlock)
        self.chain.append(newBlock)
    
    def printBlocks (self):
        for i in range(len(self.chain)):
            currentBlock = self.chain[i]
            print("Block {} {}".format(i, currentBlock))
            currentBlock.printContents

    def validateChoice(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if (current.hash != current.generatehash):
                print("Block " + i + " of Blockchain has been tampered with. (current != currentGenerated)")
                return False
            
            if (current.previousHash != previous.generatehash):
                print("Block " + i + " of Blockhcain has been tampered with. (currentPHash != prevGenerated)")
                return False
        return True

    def proofOfWork(self, block, difficulty = 2):
        proof = block.generatehash

        while (proof[ :difficulty] != '0' * difficulty):
            block.nonce +=1
            proof = block.generatehash
        
        block.nonce = 0
        return proof