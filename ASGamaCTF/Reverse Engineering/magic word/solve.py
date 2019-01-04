string = list("mbO`^Ifco^DfifPqf@buMf^iFal@flRqQr")

for i in range(0x64):
    string[-1] = chr(ord(string[-1])+1)
    string = string[1:]+list(string[0])

print ''.join(string)