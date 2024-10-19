# BabyBlocks

Follow-along for a book "Learn Blockchain by Building One: A Concise Path to Understanding Cryptocurrencies" by Daniel van Flymen

## Chapter 3: Initial blockchain

```python
Created block 0
>>> bc.chain
[{'index': 0, 'timestamp': '2024-06-16T23:11:38.976814+00:00', 'transactions': [], 'previous_hash': None, 'hash': '027269c40c9cb100cfe8155434672f43fa950e7ad7bc85bd1624e376e69066f8'}]
>>> bc.new_block('027269c40c9cb100cfe8155434672f43fa950e7ad7bc85bd1624e376e69066f8')
Created block 1
{'index': 1, 'timestamp': '2024-06-16T23:12:36.097752+00:00', 'transactions': [], 'previous_hash': '027269c40c9cb100cfe8155434672f43fa950e7ad7bc85bd1624e376e69066f8', 'hash': '9a89f4066e60afb8877a880f331f02c3722abc3116c2f359b36acc6d9bd46096'}
>>> exit()
```

### Observations

Since the timestamp is included in the genesis block, it is not reproducible, but have it not been part of the block it could be. It would be interesting to use blockchain to create a final sha for a step of actions when validating only the last sha would allow you to validate all actions. For example a series of security questions displayed in particular order. Say given 3 questions and only 3 valid answers, a server could present them to the user in specific order, sent the hash back from the last block and validate that without sending answers, kin dof like with passwords, except allowing multiple values. Huh! I discovered something :) I am sure someone already uses, but it is fun nevertheless. Onward!  