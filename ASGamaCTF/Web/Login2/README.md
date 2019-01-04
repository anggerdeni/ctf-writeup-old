# __ASGama CTF__ 
## _Login 2_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 30 | l0l

**Description:** 

> http://ctf.asgama.web.id:40105/


### Login 2
Lakukan pengamatan  
`$ curl http://ctf.asgama.web.id:40105/`  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login 2</title>
</head>
<body>
    <h1>Login 2</h1>
    Password: <input type="password" name="password" id="password"><br>
    <button onclick="login();" id="submit">Login</button>
    <div id="msg"></div>
    <script   src="https://code.jquery.com/jquery-3.3.1.min.js"
			  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
              crossorigin="anonymous">
    </script>
    <script src="script.js"></script>
</body>
</html>
```

Ada javascript file yang diload. Kita coba akses file tersebut.  
`$ curl http://ctf.asgama.web.id:40105/script.js`  
```js
function login(){
    var password = $('#password').val();
    if(password == "s3cr333t"){
        var msg = atob(atob(atob("VWpKR2RGbFZUbFZTYm5SeFl6RTVhR1JZVW05WU0xSjJZakU1YVZsWFVqaz0=")));
        $("#msg").html(msg);
    }else{
        alert("Password salah");
    }
}
```

Dari script tersebut terlihat bahwa password yang benar adalah "s3cr333t". Atau kita bisa juga langsung mendecode message yang ada.


### Payload
```
$ echo VWpKR2RGbFZUbFZTYm5SeFl6RTVhR1JZVW05WU0xSjJZakU1YVZsWFVqaz0= | base64 -d | base64 -d | base64 -d

GamaCTF{js_auth_too_bad}
```

### Result
```
GamaCTF{js_auth_too_bad}
```

### Flag
GamaCTF{js_auth_too_bad}