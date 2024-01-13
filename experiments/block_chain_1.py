import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_data = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_data.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

# Create a blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block("Transaction 1")
my_blockchain.add_block("Transaction 2")

# Print the blockchain
for block in my_blockchain.chain:
    print(f"Timestamp: {block.timestamp}, Data: {block.data}, Previous Hash: {block.previous_hash}, Hash: {block.hash}\n")
