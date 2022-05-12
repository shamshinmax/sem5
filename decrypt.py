import random
import hashlib
 #ord - kod po simvoly 
 # chr- simvol po kody
a = chr(random.randint(0,256))+chr(random.randint(0,256))
print(a)
hash_object = hashlib.sha512(a.encode())
hex_dig = 'c37e1eb53bd65fb10ec40202ea8c219b02843320fff1f2c2249258c11fca074ac0d4fcfaee690177220c4a130bb24491aae42d0a8c67fa35eab7cfc51e76f5ef'
print(hex_dig)
def fun(passw):
    for i in range(256):
        sym = chr(i)
        sec_hash = hashlib.sha512(sym.encode()).hexdigest()
        if  sec_hash == passw:
            print('Пароль:', chr(i))
            break
        else:
            for j in range(256):
                sym2 = chr(j) + sym
                sec_hash = hashlib.sha512(sym2.encode()).hexdigest()
                if  sec_hash == passw:
                    print('Пароль:', sym2)
                    break
fun(hex_dig)
