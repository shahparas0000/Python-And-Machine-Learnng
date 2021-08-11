print("This is Diffie-Hellman Cipher.")
print("Enter a prime number : ")
p = int(input())
print("Enter another prime number from 2 to",p-1,": ")
g = int(input())

print("Enter a secret number for person A : ")
xa = int(input())
ya = (g**xa)%p

print("Enter a secret number for person B : ")
xb = int(input())
yb = (g**xb)%p

akey = (yb**xa)%p
bkey = (ya**xb)%p

print("The secret shared key for A is :", akey)
print("The secret shared key for B is :", bkey)
