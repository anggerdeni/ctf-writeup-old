<?php
    if(isset($_POST["login"])){
        $user = "root";
        $pass = "";
        $conn = new PDO('mysql:host=localhost;dbname=rahasia_lah', $user, $pass);

        $username = $_POST["username"];
        $password = $_POST["password"];
        $query = $conn->prepare("SELECT * FROM users where username = '$username' and password = '$password'");
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
    }
?>