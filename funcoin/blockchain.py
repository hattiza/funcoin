import json
import random
from datetime import datetime, UTC
from hashlib import sha256
from timeit.timit import timer_decorator


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        print("Creating genesis block")
        self.chain.append(self.new_block())

    def get_nonce(self):
        return format(random.getrandbits(64), "x")

    def new_block(self, previous_hash=None):
        block = {
            "index": len(self.chain),
            "timestamp": datetime.now(UTC).isoformat(),
            "transactions": self.pending_transactions,
            "previous_hash": previous_hash,
            "nonce": self.get_nonce(),  # nonsense string
        }
        block_hash = self.hash(block)
        block["hash"] = block_hash
        self.pending_transactions = []

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append(
            {
                "recipient": recipient,
                "sender": sender,
                "amount": amount,
            }
        )

    @timer_decorator
    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break

        self.chain.append(new_block)
        print("Found a new block", new_block)

    def valid_block(self, block):
        return block["hash"].startswith("0000")


bc = Blockchain()
