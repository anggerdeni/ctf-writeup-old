# __ASGama CTF__ 
## _Ndasmu_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 15 | l0l

**Description:** 

> http://ctf.asgama.web.id:40102


### Ndasmu
Dari judul soal sudah cukup jelas bahwa ada sesuatu di header. Maka coba akses dengan curl..


### Payload
```
curl -I http://ctf.asgama.web.id:40102 # -I hanya menampilkan header
```

### Result
```
HTTP/1.1 200 OK
Host: ctf.asgama.web.id:40102
Date: Fri, 28 Dec 2018 15:05:54 +0000
Connection: close
X-Powered-By: PHP/7.2.6
BENDERA: GamaCTF{check_your_head}
Content-type: text/html; charset=UTF-8
```

### Flag
GamaCTF{check_your_head}