#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[Blockchain Validation Script]

This script calculates the hashes of the blockchain to check if blockchain has been tampered with.
"""

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
        self.load_chain()

    def load_chain(self):
        file_name = "blockchain_data.json"
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                serialized_chain = json.load(file)
                self.chain = self.deserialize(serialized_chain)
        else:
            print("No blockchain data found.")

    @classmethod
    def deserialize(cls, serialized_chain):
        blockchain = []
        for block_data in serialized_chain:
            index = block_data['index']
            timestamp = datetime.datetime.strptime(block_data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            block = Block(index, block_data['data'], block_data['previous_hash'], timestamp)
            block.hash = block_data['hash']
            blockchain.append(block)
        return blockchain

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

if __name__ == "__main__":

    # Load the blockchain.
    blockchain = Blockchain()

    # Validation
    is_valid = blockchain.validate_chain()

    if is_valid:
        print("Blockchain is valid.")
    else:
        print("Blockchain is not valid.")
