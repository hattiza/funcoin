class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def new_block(self):
        pass

    @staticmethod
    def hash(block):
        pass

    def last_block(self):
        pass


    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount,
        })