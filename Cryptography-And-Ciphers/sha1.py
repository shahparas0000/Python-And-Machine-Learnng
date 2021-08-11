import hashlib
result = hashlib.sha1('Paras Shah'.encode()) 
print("Hash Value :", result)
print("Hexadecimal Equivalent :", result.hexdigest())