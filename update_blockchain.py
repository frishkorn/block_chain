#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[Blockchain Update Script]

This script fetches the latest ISS postion and adds it to the blockchain.
"""

import hashlib, datetime, json, os, requests
from geopy.geocoders import Nominatim

class Block:
    def __init__(self, index, data, geo_loc, previous_hash, timestamp=None):
        self.index = index
        self.timestamp = timestamp or datetime.datetime.utcnow()
        self.data = data
        self.geo_loc = geo_loc
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

    def add_block(self, data, geo_loc):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, geo_loc, previous_block.hash)
        self.chain.append(new_block)
        print("Blockchain updated.")

    def serialize(self):
        serialized_chain = []
        for block in self.chain:
            serialized_block = {
                "index": block.index,
                "timestamp": str(block.timestamp),
                "data": block.data,
                "geo_loc": block.geo_loc,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }
            serialized_chain.append(serialized_block)
        return serialized_chain

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.serialize(), file, indent=4)

    @classmethod
    def deserialize(cls, serialized_chain):
        blockchain = []
        for block_data in serialized_chain:
            index = block_data['index']
            timestamp = datetime.datetime.strptime(block_data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            block = Block(index, block_data['data'], block_data['geo_loc'], block_data['previous_hash'], timestamp)
            block.hash = block_data['hash']
            blockchain.append(block)
        return blockchain

def fetch_iss_location():
    api_url = "http://api.open-notify.org/iss-now.json"
    geolocator = Nominatim(user_agent="block_iss")  # Replace "your_app_name" with a unique identifier

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        # Reverse geocode to get the city name from coordinates
        location = geolocator.reverse([latitude, longitude], language='en')

        # Check if the location is found
        if location and location.address and len(location.address.split(",")) >= 3:
            geo_location = location.address
        else:
            geo_location = "Unknown or Ocean"

        print(f"Current ISS Location: Latitude {latitude}, Longitude {longitude}", geo_location)
        return f"Current ISS Location: Latitude {latitude}, Longitude {longitude}", geo_location

    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS location: {e}")

if __name__ == "__main__":

    # File to store blockchain data
    file_name = "blockchain_data.json"

    # Load the blockchain.
    blockchain = Blockchain()
    
    location = fetch_iss_location()

    # Add block to the blockchain
    blockchain.add_block(location[0], location[1])

    # Save the blockchain to a file
    blockchain.save_to_file(file_name)

