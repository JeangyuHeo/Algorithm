import hashlib

input = input().encode()
print(hashlib.sha256(input).hexdigest())
