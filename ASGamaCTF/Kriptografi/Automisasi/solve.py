from string import printable

guess = "GamaCTF"
def enc(flag):
    encrypt = ''
    for x in range(len(flag)):
        for y in range(x):
            for z in range(y):
                encrypt+=str(ord(flag[z]) + ord(flag[x]) - ord(flag[y]))
    return encrypt

encrypted = open("encrypted","r").read()

counter = 0
while(True):
    if counter > len(guess): 
        break
    for i in printable:
        temp = guess+i
        cek = enc(temp)
        if(cek==encrypted[0:len(cek)]):
            guess = temp
            break
    counter+=1
print guess