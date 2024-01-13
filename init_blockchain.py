import hashlib, datetime, json, os

class Block:
    def __init__(self, index, data, previous_hash, timestamp=None):
        self.index = index
        self.timestamp = timestamp or datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_data.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        if not self.chain:
            genesis_block = Block(0, "Genesis Block", "0")
            self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def serialize(self):
        serialized_chain = []
        for block in self.chain:
            serialized_block = {
                "index": block.index,
                "timestamp": str(block.timestamp),
                "data": block.data,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }
            serialized_chain.append(serialized_block)
        return serialized_chain

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.serialize(), file, indent=4)

# File to store blockchain data
file_name = "blockchain_data.json"

# Load the blockchain or create a new one
blockchain = Blockchain()

# Save the blockchain to a file
blockchain.save_to_file(file_name)

# Print the blockchain
for block in blockchain.chain:
    print(f"Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Previous Hash: {block.previous_hash}, Hash: {block.hash}\n")
