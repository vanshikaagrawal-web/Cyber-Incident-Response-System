import hashlib

PREVIOUS_HASH = "0" * 64

def generate_hash_chain(text):
    global PREVIOUS_HASH
    combined = text + PREVIOUS_HASH
    new_hash = hashlib.sha256(combined.encode()).hexdigest()
    PREVIOUS_HASH = new_hash

    print("\nChained SHA256 Hash:")
    print(new_hash)
