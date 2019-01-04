# __ASGama CTF__ 
## _Hidup Itu Aneh_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 100 | l0l

**Description 1:** 

> Hidup itu aneh..... But let me introduce you someone The storm is coming. Arcadia Bay is going to be destroyed. What can I do? Should I order Grab-Bike? Grab-Car? Or Grab-Taxi. Oh wait, I think I should invite Chloe. I cannot let her die. I can't..... Deskripsinya mulai aneh, sesuai dengan judulnya. Tetaplah, hidup itu aneh. Tulisannya pun campur campur inggris indo. Format FLAG : GAMACTF{}
>
> [source](./hidup-itu-aneh.zip)

**Description 2:**
> Hidup itu aneh..... But let me introduce you someone
>
>Max is geeky, quite introverted and slightly self-conscious, particularly when it comes to her photography. According to herself, she rather likes to observe the world around her than actually participate in it; that's why several students including Juliet Watson think she wouldn't really care for others. But on the contrary, she makes a genuine effort to show kindness to all of Blackwell's students. She's a clear, deductive thinker, smart and sneaky, but practical, reasonable, and mature for her age, especially compared to her best friend, Chloe. She is also brave, placing herself in harm's way to protect those she cares about. I wonder what abilities she can do....
>
>Deskripsinya mulai aneh, sesuai dengan judulnya. Tetaplah, hidup itu aneh. Tulisannya pun campur campur inggris indo.
>
>I wish I had abilities like you, Max. Also, I have another good information. This challenge is the sequel of "Hidup itu Aneh episode 1" challenge. And this is git challenge Format FLAG : GAMACTF{}


### Hidup Itu Aneh 1
Dari deskripsi soalnya sepertinya mengarah kepada `grep`.

### Hidup Itu Aneh 2
Kali ini deskripsi soal mengarah pada `waktu`, lebih spesifik lagi `git` karena dengan git kita bisa kembali ke versi sebelumnya. Dan memang folder hasil extract dari file yang diberikan merupakan repository git.

Coba-coba saja checkout ke beberapa commit sebelumnya sambil `grep -r`

### Payload 1
```
grep -r GAMACTF
```

### Payload 2
```
$ git checkout c351e89 
$ grep -R GAMACTF
```


### Result 1
```
app/User.php:     * GAMACTF{Even angels need angels, Max}
```

### Result 2
```
storage/app/public/FLAG.txt:GAMACTF{I wish I could stay in this moment forever}
```

### Flag
GAMACTF{Even angels need angels, Max}
GAMACTF{I wish I could stay in this moment forever}