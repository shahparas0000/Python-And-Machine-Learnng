import hashlib
result = hashlib.md5('password'.encode()) 
print("Hash Value :", result)
print("Hexadecimal Equivalent :", result.hexdigest())