c = open("encrypted.txt",'r').read().decode('hex')

key = "Qk3j4cnmb8"
flag = [' ' for i in range(len(c))]

for i in range(len(key)):
    a = i
    for j in range(len(flag)/len(key)):
        flag[a] = chr(ord(c[i*(len(flag)/len(key))+j])^ord(key[i]))
        a+=len(key)

print ''.join(flag)