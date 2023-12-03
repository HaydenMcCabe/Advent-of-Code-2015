import hashlib

i = 0
key = "bgvyzdsv"

while True:
    hash_input = ("%s%d" % (key, i)).encode('utf-8')
    hash = hashlib.md5(hash_input)
    if hash.hexdigest().startswith("00000"):
        print("Value: %d" % i)
        break
    i += 1
