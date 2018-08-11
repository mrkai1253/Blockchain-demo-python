import datetime
import hashlib
import json 
from flask import Flask, jsonify



class BlockChain:
    def __init__(self):
        self.chain = []  #initialising the chain
        #Creating the genisis block
        self.create_block(proof = 1 , prev_hash = '0')

        #function to create block
    def create_block(self,proof,prev_hash):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : datetime.datetime.now(),
            'proof' : proof,
            'prev_hash' : prev_hash,
            }
        self.chain.append(block)

        return block

    def get_prev_block(self):
        return self.chain[-1]

#The proof of work miners have to solve
    def pow(self, prev_proof):
        #checking if the new proof is below certain value
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        #converting dictionary to block 
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def is_chain_valid(self, chain):
        prev_block = chain[0]
        block_i = 1 #block index
        while block_i < len(chain):
            block = chain[block_i]
            if block['prev_hash'] != self.hash(prev_block):
                return False
            prev_proof = prev_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

        

