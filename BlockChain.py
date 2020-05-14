# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:50:27 2020

@author: Pa1n4ndT3rr0r
"""

from Block import Block
import datetime
# Anzahl an zu generierenden Blöcken
num_blocks_to_add = 10
# Hinzufügen von Genesis
block_chain = [Block.create_genesis_block()]

print("The genesis block has been created.")
print("Genesis-Block Hash: %s" % block_chain[0].hash)
print("----")

# Erstellen der Blockchain
for i in range(1, num_blocks_to_add):
    block_chain.append(Block(block_chain[i-1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)
    print("----")