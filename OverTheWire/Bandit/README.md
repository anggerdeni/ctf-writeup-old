# __OverTheWire__ 
## _Bandit_

### Bandit 0

#### Level Goal
> The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

#### Commands you may need to solve this level
> ssh

#### Helpful Reading Material
> [Secure Shell (SSH)](http://en.wikipedia.org/wiki/Secure_Shell)  
> [How to use SSH](http://en.wikipedia.org/wiki/Secure_Shell)

#### Solve  
Di level ini kita hanya perlu connect ke ssh pada host dan port yang diberikan.  
`$ ssh bandit0@bandit.labs.overthewire.org -p 2220`  
Dengan password `bandit0`  

### Bandit 0 -> Bandit 1

#### Level Goal
> The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find

#### Solve  
Seperti perintah, kita hanya harus membaca isi file `readme` pada home directory.  
```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
bandit0@bandit:~$ 
```

#### Password 
boJ9jbbUNNfktd78OOpsqOltutMc3MY1

### Bandit 1 -> Bandit 2

#### Level Goal
> The password for the next level is stored in a file called - located in the home directory

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find

#### Helpful Reading Material
> [Google Search for “dashed filename”](https://www.google.com/search?q=dashed+filename)
> [Advanced Bash-scripting Guide - Chapter 3 - Special Characters](http://tldp.org/LDP/abs/html/special-chars.html)

#### Solve
- Conect ke server dengan user `bandit1` dan password `boJ9jbbUNNfktd78OOpsqOltutMc3MY1`  
    `$ ssh bandit1@bandit.labs.overthewire.org -p 2220`
- List isi home directory
    ```
    bandit1@bandit:~$ ls -la
    total 24
    -rw-r-----  1 bandit2 bandit1   33 Oct 16 14:00 -
    drwxr-xr-x  2 root    root    4096 Oct 16 14:00 .
    drwxr-xr-x 41 root    root    4096 Oct 16 14:00 ..
    -rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
    -rw-r--r--  1 root    root    3526 May 15  2017 .bashrc
    -rw-r--r--  1 root    root     675 May 15  2017 .profile
    ```
- Untuk dapat membaca file tersebut tidak bisa menggunakan perintah `cat` seperti biasa. Ada beberapa cara:
    1. Dengan memberikan fullpath `$ cat ./`
    2. Dengan perintah `$ cat < -`
    3. Dengan python `$ python -c "print open('-','r').read()"`

#### Password
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

### Bandit 2 -> Bandit 3

#### Level Goal
> The password for the next level is stored in a file called spaces in this filename located in the home directory

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find

#### Helpful Reading Material
> [Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)

#### Solve
- Conect ke server dengan user `bandit2` dan password `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`  
    `$ ssh bandit2@bandit.labs.overthewire.org -p 2220`
- List isi home directory
    ```
    bandit2@bandit:~$ ls -lah
    total 24K
    drwxr-xr-x  2 root    root    4.0K Oct 16 14:00 .
    drwxr-xr-x 41 root    root    4.0K Oct 16 14:00 ..
    -rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
    -rw-r--r--  1 root    root    3.5K May 15  2017 .bashrc
    -rw-r--r--  1 root    root     675 May 15  2017 .profile
    -rw-r-----  1 bandit3 bandit2   33 Oct 16 14:00 spaces in this filename
    ```
- Untuk dapat menampilkan isi file yang namanya ada spasinya, ada beberapa cara :
    1. `$ cat spaces\ in\ this\ filename`
    2. `$ cat s*`
    3. `$ grep ^ spaces\ in\ this\ filename`

#### Password
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

### Bandit 3 -> Bandit 4

#### Level Goal
> The password for the next level is stored in a hidden file in the inhere directory.

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find

#### Solve
- Conect ke server dengan user `bandit3` dan password `UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK`  
    `$ ssh bandit3@bandit.labs.overthewire.org -p 2220`
- List isi directory
    ```
    bandit3@bandit:~$ ls
    inhere
    bandit3@bandit:~$ ls inhere/
    bandit3@bandit:~$ ls -la inhere/
    total 12
    drwxr-xr-x 2 root    root    4096 Oct 16 14:00 .
    drwxr-xr-x 3 root    root    4096 Oct 16 14:00 ..
    -rw-r----- 1 bandit4 bandit3   33 Oct 16 14:00 .hidden
    ```
- Terlihat ada hidden file di directory inhere. Langsung `cat` saja
    `$ cat inhere/.hidden`

#### Password 
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

### Bandit 4 -> Bandit 5

#### Level Goal
> The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find

#### Solve
- Conect ke server dengan user `bandit4` dan password `pIwrPrtPN36QITSp3EQaw936yaFoFgAB`  
    `$ ssh bandit4@bandit.labs.overthewire.org -p 2220`
- Masuk ke directory inhere lalu analisa
    ```
    bandit4@bandit:~$ cd inhere/
    bandit4@bandit:~/inhere$ ls -la
    total 48
    drwxr-xr-x 2 root    root    4096 Oct 16 14:00 .
    drwxr-xr-x 3 root    root    4096 Oct 16 14:00 ..
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file00
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file01
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file02
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file03
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file04
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file05
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file06
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file07
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file08
    -rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file09
    bandit4@bandit:~/inhere$ file *
    file: Cannot open `ile00' (No such file or directory).
    file: Cannot open `ile01' (No such file or directory).
    file: Cannot open `ile02' (No such file or directory).
    file: Cannot open `ile03' (No such file or directory).
    file: Cannot open `ile04' (No such file or directory).
    file: Cannot open `ile05' (No such file or directory).
    file: Cannot open `ile06' (No such file or directory).
    file: Cannot open `ile07' (No such file or directory).
    file: Cannot open `ile08' (No such file or directory).
    file: Cannot open `ile09' (No such file or directory).
    bandit4@bandit:~/inhere$ file ./-*
    ./-file00: data
    ./-file01: data
    ./-file02: data
    ./-file03: data
    ./-file04: data
    ./-file05: data
    ./-file06: data
    ./-file07: ASCII text
    ./-file08: data
    ./-file09: data
    ```
- Terlihat hanya `-file07` yang isinya ASCII text. Langsung saja tampilkan isinya `$ cat ./-file07`

#### Password
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

### Bandit 5 -> Bandit 6

#### Level Goal
> The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
> -   human-readable
> -   1033 bytes in size
> -   not executable

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find

#### Solve
- Conect ke server dengan user `bandit5` dan password `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`  
    `$ ssh bandit5@bandit.labs.overthewire.org -p 2220`

- Gunakan perintah `find` dengan beberapa argumen yang sesuai dengan ketentuan.
    ```
    $ find ./inhere -size 1033c -readable \! -executable
    ./inhere/maybehere07/.file2
    ```

    `-size 1033c` menunjukkan size nya 1033 bytes  
    `-readable` menunjukkan readable file  
    `\! -executable` menunjukkan file non-executable

- Ditemukan hanya 1 file yang match. Langsung tampilkan isinya dengan perintah `$ cat ./inhere/maybehere07/.file2`

#### Password 
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

### Bandit 6 -> Bandit 7

#### Level Goal
> The password for the next level is stored somewhere on the server and has all of the following properties:
> -    owned by user bandit7
> -    owned by group bandit6
> -    33 bytes in size

#### Commands you may need to solve this level
> ls, cd, cat, file, du, find, grep

#### Solve
`$ find / -user bandit7 -group bandit6 -size 33c `

