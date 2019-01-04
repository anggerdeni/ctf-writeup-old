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