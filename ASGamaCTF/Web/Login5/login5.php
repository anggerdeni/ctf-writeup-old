<?php
    if(isset($_POST["login"])){
        $user = "root";
        $pass = "";
        $conn = new PDO('mysql:host=localhost;dbname= --REDACTED--', $user, $pass);

        $username = $_POST["username"];
        $password = $_POST["password"];
        $query = $conn->prepare("SELECT * FROM users where username = '$username' and password = '$password'");
        $query->execute();
        
        $loggedin = $query->rowCount();
        $data = $query->fetch();

        $name = $data["username"];
        if($loggedin == 1){
            echo "Selamat datang $name, Flag: ==REDACTED==";
        }else{
            echo "Username atau password salah ea :v<br>";
            if($query->errorInfo()[1]){
                echo $query->errorInfo()[2];
            }
        }
    }
?>