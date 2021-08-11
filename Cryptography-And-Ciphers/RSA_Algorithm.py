p=int(input("Enter a prime number : "))
q=int(input("Enter another prime number : "))
n=(p*q)
qn=(p-1)*(q-1)

m=int(input("Enter the message : "))

def gcd(a,b):
    if (b==0):
        return a
    else:
        return (gcd(b,a%b))

for r in range(2,qn):
    if (gcd(r,qn)==1):
        e=r
        break
print("Public key (e) =",e)

for r in range(1,qn):
    if (e*r)%qn==1:
        d=r
        break
print("Private key (d) =",d)

ct=(m**e)%n
print("Cipher text =",ct)
pt=(ct**d)%n
print("Plain text =",pt)
