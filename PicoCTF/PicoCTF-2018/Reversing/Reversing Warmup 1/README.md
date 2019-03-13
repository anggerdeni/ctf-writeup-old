# __PicoCTF 2018__ 
## _Reversing_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reversing | 50 | l0l

**Description:** 

>  Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_3_7c0eade7faf60ffe3485e12098e2a6c2 on the shell server and run this program to retreive the flag? 
>
>
> Hints
> If you are searching online, it might be worth finding how to exeucte a program in command line.
>
> [run](./run)

### Reversing Warmup 1
```
$ file run 
run: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=3f4cbb89ad8989bad12dfa913e40072f3d21c96d, not stripped
```

```
$ ls -l run 
-rw-rw-r-- 1 l0l l0l 7420 Jan 28 19:19 run
```

Diberikan sebuah file executable dengan permission rw. Kita diminta menjalankan file ini. 

Maka tambah permission executable dengan perintah `$ chmod +x run`, lalu jalankan file ini dengan perintah `./run`.

```
$ ls -l run
-rwxrwxr-x 1 l0l l0l 7420 Jan 28 19:19 run

$ ./run
picoCTF{welc0m3_t0_r3VeRs1nG}
```



### Payload
```
$ chmod +x run
$ ./run
```

### Result 
```
$ ./run
picoCTF{welc0m3_t0_r3VeRs1nG}
```

### Flag 
picoCTF{welc0m3_t0_r3VeRs1nG}