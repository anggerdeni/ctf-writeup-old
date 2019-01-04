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
    <?php
        $secret = "==REDACTED==";
        if(isset($_GET["password"])){
            $password = $_GET["password"];
            if(strcmp($password, $secret) == 0){ 
                echo "==REDACTED==";
            }else{
                echo "Password Salah";
            }
        }
    ?>
</body>
</html>