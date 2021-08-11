import hashlib
import time

text="Hello, Paras here."
md5_1=time.time()
result = hashlib.md5(text.encode())
print("MD5 Hexadecimal Equivalent :", result.hexdigest())
md5_2=time.time()

sha1_1=time.time()
result = hashlib.sha1(text.encode())
print("SHA1 Hexadecimal Equivalent :", result.hexdigest())
sha1_2=time.time()

print("Time taken by MD5 algorithm :", md5_2-md5_1, "seconds")
print("Time taken by SHA1 algorithm :", sha1_2-sha1_1, "seconds")