import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from flask import Flask
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA384
from base64 import b64decode,b64encode
from flask_cors import CORS, cross_origin

import requests
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def register_node(self, address):
        """
        Add a new node to the list of nodes

        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid

        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.

        :return: True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def getBalance(self, user):
        balance = 0
        for i in self.chain:
            for j in i['transactions']:
                if j['recipient'] == user:
                    balance += int(j['amount'])
                elif j.sender == user:
                    balance -= int(j['amount'])
        for i in self.current_transactions:
            if i['recipient'] == user:
                balance += int(i['amount'])
            elif i['sender'] == user:
                balance -= int(i['amount'])
        return balance

    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount, balance, privKeyb64):
        """
        Creates a new transaction to go into the next mined Block

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        # pubkey = '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'
        
        keyDER = b64decode(privKeyb64)
        keyPriv = RSA.importKey(keyDER)
        sigObj = pkcs1_15.new(keyPriv)
        dataHash = SHA384.new()

        dataList = []

        dataList.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount, 
        })
        dataJSON = json.dumps(dataList).encode()

        dataHash.update(dataJSON)
        signature = sigObj.sign(dataHash)

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            "balance": balance,
            "signature": b64encode(signature).decode('UTF-8'),
        })

        return self.last_block['index'] + 1
    
    def generateBankKeyPair(self):
        key = RSA.generate(2048)
        public = key.publickey()
        self.privateBank = key.exportKey('PEM')
        self.publicBank = public.exportKey('PEM')
        self.bankBalance = 1000000 ########
        self.publicBank = self.publicBank[26:]
        self.publicBank = self.publicBank[:-24]
        self.privateBank = self.privateBank[31:]
        self.privateBank = self.privateBank[:-29]

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof
         
        :param last_block: <dict> last Block
        :return: <int>
        """
        for i in self.current_transactions:
            pubKeyb64 = i['sender']
            keyDER = b64decode(pubKeyb64)
            keyPub = RSA.importKey(keyDER)
            sigObj = pkcs1_15.new(keyPub)  
            dataHash = SHA384.new()

            dataList = []
            dataList.append({
                'sender': i['sender'],
                'recipient': i['recipient'],
                'amount': i['amount'], 
            })
            dataJSON = json.dumps(dataList).encode()

            dataHash.update(dataJSON)
            try:
                sigObj.verify(dataHash, b64decode(i['signature'].encode('utf_8')))
            except:
                index = self.current_transactions.index(i)
                self.current_transactions.pop(index)
                
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Validates the Proof

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.

        """

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# Instantiate the Node
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    if (len(blockchain.current_transactions) < transactions_per_block):
        response = {
            'message': f'Insufficient number of transactions to close the block (minimum: {transactions_per_block})',
        }
        return jsonify(response), 400
    proof = blockchain.proof_of_work(last_block)
    miner = request.args.get("user")
    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    if blockchain.bankBalance > 0:
        blockchain.new_transaction(
            sender=blockchain.publicBank.decode('utf-8'),
            recipient=miner,
            amount=1,
            balance=blockchain.getBalance(miner)+1,
            privKeyb64=blockchain.privateBank
        )
        blockchain.bankBalance-=1

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount', 'privKey']
    if not all(k in values for k in required):
        return 'Missing values', 400

    if values['sender'] == "0":
        values['sender'] = blockchain.publicBank.decode('utf_8')
        values['privKey'] = blockchain.privateBank

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'], blockchain.getBalance(values['recipient'])+int(values['amount']), values['privKey'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')

    reflect = values.get('reflect')

    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)
    if reflect:
        for node in blockchain.nodes:
            if f'http://{node}' not in nodes:
                response = requests.post(f'http://{node}/nodes/register', json={"nodes":nodes, "reflect":False})
            else:
                response = requests.post(f'http://{node}/nodes/register', json={"nodes":[w.replace(node, request.headers.get("Host")) for w in blockchain.nodes], "reflect":False}) #TODO: fix this
            #if response.status_code == 200:
                #print("Response from node "+node+": "+response.text)



    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes', methods=['GET'])
def nodes_list():
    response = {
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201   

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    parser.add_argument('-t', '--tran', default=5, type=int, help='numero di transazioni minime per chiudere un blocco')
    args = parser.parse_args()
    port = args.port
    transactions_per_block = args.tran
    blockchain.generateBankKeyPair()

    app.run(host='0.0.0.0', port=port)
