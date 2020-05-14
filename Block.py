# -*- coding: utf-8 -*-
"""
Block creation

@author: Pa1n4ndT3rr0R
"""

import datetime
import hashlib

# Block Bauplan
class Block:
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
    # Erster Block "Genesis" in der Liste
    @staticmethod
    def create_genesis_block():
        return Block("0", "0", datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.previous_block_hash) +
                      str(self.data) +
                      str(self.timestamp))
        # Hashing über SHA256 
        # inner_hash -> encode vorheriger  Blockhash
        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
        # outer_hash -> erneutes Hashing mit inner_hash enthalten
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash