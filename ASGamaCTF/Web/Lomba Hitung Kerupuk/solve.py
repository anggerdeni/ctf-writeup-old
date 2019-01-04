from requests import *
from sys import *

target = 'http://gamactf.asgama.web.id:41001/'
cookies = dict(PHPSESSID="b579c620c76da61bdcf7595dc012acb2")

def main():
    current_correct = 0
    while current_correct < 730:
        r = get(target,cookies=cookies)
        jumlah = len(r.text[r.text.find("KERUPUK"):r.text.find(" </body>")].split(' '))
        r = get(target+"?jumlah={}".format(jumlah),cookies=cookies)

        current_correct = int(r.text[r.text.find("Total")+13:r.text.find("/730")])
        stdout.flush()
        stdout.write("\r{}".format(current_correct))

    print
    print "Finished : "
    print r.text

if __name__ == "__main__":
    main()