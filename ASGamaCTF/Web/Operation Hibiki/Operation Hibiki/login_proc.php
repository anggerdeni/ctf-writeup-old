<?php

    include "core/koneksi.php";

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

?>