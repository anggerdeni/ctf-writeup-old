# __Angstrom CTF 2019__ 
## _Half and Half_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Rev | 60 | l0l

**Description:** 

> 50points 358 solves
> Mm, coffee. Best served with half and half!

>Author: defund
>
> Given : [half_and_half](./half_and_half.py)


### Half and Half  
```py
...
assert len(flag) % 2 == 0

half = len(flag)//2
milk = flag[:half]
cream = flag[half:]

assert xor(milk, cream) == '\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"'
```
Cukup sederhana flag dibagi menjadi dua bagian lalu dixor. Hasilnya sama dengan '\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"' dengan panjang hasil xor = 12 huruf.


#### Solve
Karena kita tahu 5 huruf pertama dari flag pasti adalah 'actf{', maka kita juga dapat mengetahui 5 huruf bagian kedua. Dan kita juga tahu huruf terakhir pastilah '}'
```py
xor('\x15\x02\x07\x12\x1e','actf{')
'taste'
xor('"','}')
'_'
```
Kita dapatkan flag sementara :  
 a c t f { . . . . . . _
 t a s t e . . . . . . }

Sisa cipher = '\x10 0 \x01 \t \n \x01'
Kita tahu bahwa yang mungkin mengikuti 'taste' hanya 's' atau '_' atau 'd'
```py
>>> xor('\x10','_')
'O'
>>> xor('\x10','s')
'c'
>>> xor('\x10','d')
't'
```

Lalu dengan tebakan berdasarkan deskripsi, coba saja kita masukkan 'coffee'
```py
>>> xor('actf{coffee_','\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"')
'tastes_good}'
```

### Flag 
actf{coffee_tastes_good}