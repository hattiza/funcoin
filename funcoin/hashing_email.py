from hashlib import sha256

secret_code = "3PK"


def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    # combined.encode() --> b"<content of combined>"
    # can also use b'string' as input to sha256, then no encode() needed
    return sha256(combined.encode()).hexdigest()


email_body = (
    "Hey Bob, I think you should learn about Blockchains! "
    "I've been investing in Bitcoin and currently have exactly 12.03 BTC in my account."
)


print(email_body + f"\nHash: {get_hash_with_secret_phrase(email_body, secret_code)}")
