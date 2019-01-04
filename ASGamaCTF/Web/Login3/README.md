# __ASGama CTF__ 
## _Login 3_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 40 | l0l

**Description:** 

> http://ctf.asgama.web.id:40106

### Login 3
Sama seperti login 2, autentikasi dilakukan dengan javascript, namun kali ini script diobfuscate sehingga sulit dibaca.

#### http://ctf.asgama.web.id:40106/script.js
```js
var _0x6ea9=["\x76\x61\x6C","\x23\x70\x61\x73\x73\x77\x6F\x72\x64","\x72\x34\x68\x34\x73\x31\x34\x34\x34","\x52\x32\x46\x74\x59\x55\x4E\x55\x52\x6E\x74\x76\x59\x6E\x4E\x6D\x64\x57\x4E\x68\x64\x47\x6C\x76\x62\x6C\x39\x70\x63\x31\x39\x75\x62\x33\x52\x66\x5A\x32\x39\x76\x5A\x46\x39\x70\x5A\x47\x56\x68\x66\x51\x3D\x3D","\x68\x74\x6D\x6C","\x23\x6D\x73\x67","\x50\x61\x73\x73\x77\x6F\x72\x64\x20\x73\x61\x6C\x61\x68"];function login(){var _0x2309x2=$(_0x6ea9[1])[_0x6ea9[0]]();if(_0x2309x2== _0x6ea9[2]){var _0x2309x3=atob(_0x6ea9[3]);$(_0x6ea9[5])[_0x6ea9[4]](_0x2309x3)}else {alert(_0x6ea9[6])}}
```

Namun teknik obfuscation seperti ini dapat dengan mudah kita tangani dengan [beautifier-javascript](https://beautifier.io/). 

Tinggal masukkan script disana dan kita dapatkan versi `cantik` nya.

```js
function login() {
    var _0x2309x2 = $('#password')['val']();
    if (_0x2309x2 == 'r4h4s1444') {
        var _0x2309x3 = atob('R2FtYUNURntvYnNmdWNhdGlvbl9pc19ub3RfZ29vZF9pZGVhfQ==');
        $('#msg')['html'](_0x2309x3)
    } else {
        alert('Password salah')
    }
}
```

Terlihat bahwa password yang benar adalah r4h4s1444. Atau jika ingin langsung mendapatkan flag nya, dapat kita decode langsung string yang terencode base64 disana.

### Payload
```
$ echo R2FtYUNURntvYnNmdWNhdGlvbl9pc19ub3RfZ29vZF9pZGVhfQ== | base64 -d
```

### Result
```
GamaCTF{obsfucation_is_not_good_idea}
```

### Flag
GamaCTF{obsfucation_is_not_good_idea}

