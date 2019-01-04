# __ASGama CTF__ 
## _Berantas Terorisme_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 150 | l0l

**Description:** 

> Mohon bantuannya, negara saat ini sedang mengalami ancaman terrorisme. Untungnya kami berhasil mendapatkan data percakapan pada website yang kami curigai sebagai media komunikasi bagi terroris. Sayangnya tim kami tidak dapat mengetahui isi percakapan tersebut dikarenakan terenkripsi pada sisi client dengan menggunakan algoritma yang tidak kami ketahui. Oleh karena itu kami percayakan masa depan NKRI kepadamu, karena hanya kamulah yang kami andalkan untuk dapat membongkar percakapan mereka agar kami bisa cepat bertindak untuk memberantas terrorisme.
>
> [captured_info](./captured_info.pcap)

### Berantas Terorisme  
Langsung buka dengan wireshark. Isinya tidak banyak, hanya beberapa network dump saja yang tersedia. Pilih saja yang paling atas lalu `Follow TCP Stream`  

Terdapat sebuah fungsi enkripsi dalam javascript: 
```js
function send(){
    var msg = $("#message").val();
    var tmp = "";
    for(var i=msg.length-1; i >= 0; i--) tmp += msg[i];
    tmp = btoa(tmp);
    var tmp2 = "";
    for(var i=0; i < tmp.length; i++) tmp2 += tmp.charCodeAt(i) + "$eNcRYpt3D$";
    $.ajax({
        method: "POST",
        url: "proc.php",
        data: {msg: tmp2}
        })
        .done(function( data ) {
            alert("Pesan terkirim");
    });
}
```

Lalu jika kita lihat, fungsi tersebut melakukan `ajax request` ke `proc.php` dengan data `{msg:tmp2}` dimana tmp2 adalah hasil enkripsi. Coba cari di bawah lagi, terdapat beberapa hasil dump request `/proc.php` lalu coba lihat isinya :  
```
msg=84%24eNcRYpt3D%2486%24eNcRYpt3D%2466%24eNcRYpt3D%2484%24eNcRYpt3D%2477%24eNcRYpt3D%24122%24eNcRYpt3D%2473%24eNcRYpt3D%24120%24eNcRYpt3D%24101%24eNcRYpt3D%2468%24eNcRYpt3D%2465%24eNcRYpt3D%24103%24eNcRYpt3D%2479%24eNcRYpt3D%24109%24eNcRYpt3D%2449%24eNcRYpt3D%24112%24eNcRYpt3D%2499%24eNcRYpt3D%24109%24eNcRYpt3D%24108%24eNcRYpt3D%24110%24eNcRYpt3D%2498%24eNcRYpt3D%24109%24eNcRYpt3D%2486%24eNcRYpt3D%2481%24eNcRYpt3D%24


msg=73%24eNcRYpt3D%2472%24eNcRYpt3D%2449%24eNcRYpt3D%24108%24eNcRYpt3D%2498%24eNcRYpt3D%2488%24eNcRYpt3D%2477%24eNcRYpt3D%24120%24eNcRYpt3D%2499%24eNcRYpt3D%24106%24eNcRYpt3D%2466%24eNcRYpt3D%24121%24eNcRYpt3D%2499%24eNcRYpt3D%24106%24eNcRYpt3D%2478%24eNcRYpt3D%2485%24eNcRYpt3D%2488%24eNcRYpt3D%2449%24eNcRYpt3D%24112%24eNcRYpt3D%24104%24eNcRYpt3D%24100%24eNcRYpt3D%2471%24eNcRYpt3D%2452%24eNcRYpt3D%2448%24eNcRYpt3D%2499%24eNcRYpt3D%24106%24eNcRYpt3D%2478%24eNcRYpt3D%24105%24eNcRYpt3D%24101%24eNcRYpt3D%2448%24eNcRYpt3D%2490%24eNcRYpt3D%2485%24eNcRYpt3D%2481%24eNcRYpt3D%2450%24eNcRYpt3D%2470%24eNcRYpt3D%24116%24eNcRYpt3D%2489%24eNcRYpt3D%2485%24eNcRYpt3D%2499%24eNcRYpt3D%24103%24eNcRYpt3D%2473%24eNcRYpt3D%2471%24eNcRYpt3D%24104%24eNcRYpt3D%24104%24eNcRYpt3D%2498%24eNcRYpt3D%2471%24eNcRYpt3D%2470%24eNcRYpt3D%24107%24eNcRYpt3D%2489%24eNcRYpt3D%2483%24eNcRYpt3D%2466%24eNcRYpt3D%24112%24eNcRYpt3D%2499%24eNcRYpt3D%2450%24eNcRYpt3D%2470%24eNcRYpt3D%2450%24eNcRYpt3D%2497%24eNcRYpt3D%2488%24eNcRYpt3D%2482%24eNcRYpt3D%24114%24eNcRYpt3D%2489%24eNcRYpt3D%2483%24eNcRYpt3D%2466%24eNcRYpt3D%24108%24eNcRYpt3D%2490%24eNcRYpt3D%2471%24eNcRYpt3D%2457%24eNcRYpt3D%24114%24eNcRYpt3D%2473%24eNcRYpt3D%2467%24eNcRYpt3D%24120%24eNcRYpt3D%24116%24eNcRYpt3D%2489%24eNcRYpt3D%2487%24eNcRYpt3D%24120%24eNcRYpt3D%24104%24eNcRYpt3D%2498%24eNcRYpt3D%2483%24eNcRYpt3D%2466%24eNcRYpt3D%24114%24eNcRYpt3D%2498%24eNcRYpt3D%2451%24eNcRYpt3D%2478%24eNcRYpt3D%24108%24eNcRYpt3D%2489%24eNcRYpt3D%24105%24eNcRYpt3D%2466%24eNcRYpt3D%24117%24eNcRYpt3D%2489%24eNcRYpt3D%2487%24eNcRYpt3D%24116%24eNcRYpt3D%24114%24eNcRYpt3D%2489%24eNcRYpt3D%2487%24eNcRYpt3D%2482%24eNcRYpt3D%24108%24eNcRYpt3D%2498%24eNcRYpt3D%2471%24eNcRYpt3D%24108%24eNcRYpt3D%24107%24eNcRYpt3D%2473%24eNcRYpt3D%2472%24eNcRYpt3D%2466%24eNcRYpt3D%24104%24eNcRYpt3D%2497%24eNcRYpt3D%2488%24eNcRYpt3D%2477%24eNcRYpt3D%24103%24eNcRYpt3D%2498%24eNcRYpt3D%2487%24eNcRYpt3D%2457%24eNcRYpt3D%2467%24eNcRYpt3D%24


msg=90%24eNcRYpt3D%2450%24eNcRYpt3D%2453%24eNcRYpt3D%24104%24eNcRYpt3D%2499%24eNcRYpt3D%2450%24eNcRYpt3D%2470%24eNcRYpt3D%24119%24eNcRYpt3D%2499%24eNcRYpt3D%24109%24eNcRYpt3D%2486%24eNcRYpt3D%2448%24eNcRYpt3D%2473%24eNcRYpt3D%2471%24eNcRYpt3D%24104%24eNcRYpt3D%24104%24eNcRYpt3D%2490%24eNcRYpt3D%2472%24eNcRYpt3D%2486%24eNcRYpt3D%24122%24eNcRYpt3D%2473%24eNcRYpt3D%2471%24eNcRYpt3D%2449%24eNcRYpt3D%24118%24eNcRYpt3D%2489%24eNcRYpt3D%24105%24eNcRYpt3D%2465%24eNcRYpt3D%24115%24eNcRYpt3D%2499%24eNcRYpt3D%2450%24eNcRYpt3D%2457%24eNcRYpt3D%24105%24eNcRYpt3D%2473%24eNcRYpt3D%2472%24eNcRYpt3D%2474%24eNcRYpt3D%24118%24eNcRYpt3D%2499%24eNcRYpt3D%2471%24eNcRYpt3D%2470%24eNcRYpt3D%2477%24eNcRYpt3D%24
```

Sekarang kita sudah mendapatkan algoritma enkripsi dan juga pesan yang terenkripsi. Sisanya hanya perlu decrypt.

Dalam enkripsi ini, mula-mula pesan asli direverse dahulu lalu diencode `base64` lalu simpan dalam variable tmp.

Lalu setiap karakter dalam tmp diambil nilai asciinya lalu masukkan ke variable tmp2 dengan ditambah "$eNcRYpt3D$".


### Payload
```py
def decrypt(msg):
    print ''.join(map(lambda x: chr(int(x)),msg.replace("%24eNcRYpt3D%24"," ").split(' ')[:-1])).decode('base64')[::-1]

msg = ["84%24eNcRYpt3D%2486%24eNcRYpt3D%2466%24eNcRYpt3D%2484%24eNcRYpt3D%2477%24eNcRYpt3D%24122%24eNcRYpt3D%2473%24eNcRYpt3D%24120%24eNcRYpt3D%24101%24eNcRYpt3D%2468%24eNcRYpt3D%2465%24eNcRYpt3D%24103%24eNcRYpt3D%2479%24eNcRYpt3D%24109%24eNcRYpt3D%2449%24eNcRYpt3D%24112%24eNcRYpt3D%2499%24eNcRYpt3D%24109%24eNcRYpt3D%24108%24eNcRYpt3D%24110%24eNcRYpt3D%2498%24eNcRYpt3D%24109%24eNcRYpt3D%2486%24eNcRYpt3D%2481%24eNcRYpt3D%24","73%24eNcRYpt3D%2472%24eNcRYpt3D%2449%24eNcRYpt3D%24108%24eNcRYpt3D%2498%24eNcRYpt3D%2488%24eNcRYpt3D%2477%24eNcRYpt3D%24120%24eNcRYpt3D%2499%24eNcRYpt3D%24106%24eNcRYpt3D%2466%24eNcRYpt3D%24121%24eNcRYpt3D%2499%24eNcRYpt3D%24106%24eNcRYpt3D%2478%24eNcRYpt3D%2485%24eNcRYpt3D%2488%24eNcRYpt3D%2449%24eNcRYpt3D%24112%24eNcRYpt3D%24104%24eNcRYpt3D%24100%24eNcRYpt3D%2471%24eNcRYpt3D%2452%24eNcRYpt3D%2448%24eNcRYpt3D%2499%24eNcRYpt3D%24106%24eNcRYpt3D%2478%24eNcRYpt3D%24105%24eNcRYpt3D%24101%24eNcRYpt3D%2448%24eNcRYpt3D%2490%24eNcRYpt3D%2485%24eNcRYpt3D%2481%24eNcRYpt3D%2450%24eNcRYpt3D%2470%24eNcRYpt3D%24116%24eNcRYpt3D%2489%24eNcRYpt3D%2485%24eNcRYpt3D%2499%24eNcRYpt3D%24103%24eNcRYpt3D%2473%24eNcRYpt3D%2471%24eNcRYpt3D%24104%24eNcRYpt3D%24104%24eNcRYpt3D%2498%24eNcRYpt3D%2471%24eNcRYpt3D%2470%24eNcRYpt3D%24107%24eNcRYpt3D%2489%24eNcRYpt3D%2483%24eNcRYpt3D%2466%24eNcRYpt3D%24112%24eNcRYpt3D%2499%24eNcRYpt3D%2450%24eNcRYpt3D%2470%24eNcRYpt3D%2450%24eNcRYpt3D%2497%24eNcRYpt3D%2488%24eNcRYpt3D%2482%24eNcRYpt3D%24114%24eNcRYpt3D%2489%24eNcRYpt3D%2483%24eNcRYpt3D%2466%24eNcRYpt3D%24108%24eNcRYpt3D%2490%24eNcRYpt3D%2471%24eNcRYpt3D%2457%24eNcRYpt3D%24114%24eNcRYpt3D%2473%24eNcRYpt3D%2467%24eNcRYpt3D%24120%24eNcRYpt3D%24116%24eNcRYpt3D%2489%24eNcRYpt3D%2487%24eNcRYpt3D%24120%24eNcRYpt3D%24104%24eNcRYpt3D%2498%24eNcRYpt3D%2483%24eNcRYpt3D%2466%24eNcRYpt3D%24114%24eNcRYpt3D%2498%24eNcRYpt3D%2451%24eNcRYpt3D%2478%24eNcRYpt3D%24108%24eNcRYpt3D%2489%24eNcRYpt3D%24105%24eNcRYpt3D%2466%24eNcRYpt3D%24117%24eNcRYpt3D%2489%24eNcRYpt3D%2487%24eNcRYpt3D%24116%24eNcRYpt3D%24114%24eNcRYpt3D%2489%24eNcRYpt3D%2487%24eNcRYpt3D%2482%24eNcRYpt3D%24108%24eNcRYpt3D%2498%24eNcRYpt3D%2471%24eNcRYpt3D%24108%24eNcRYpt3D%24107%24eNcRYpt3D%2473%24eNcRYpt3D%2472%24eNcRYpt3D%2466%24eNcRYpt3D%24104%24eNcRYpt3D%2497%24eNcRYpt3D%2488%24eNcRYpt3D%2477%24eNcRYpt3D%24103%24eNcRYpt3D%2498%24eNcRYpt3D%2487%24eNcRYpt3D%2457%24eNcRYpt3D%2467%24eNcRYpt3D%24","90%24eNcRYpt3D%2450%24eNcRYpt3D%2453%24eNcRYpt3D%24104%24eNcRYpt3D%2499%24eNcRYpt3D%2450%24eNcRYpt3D%2470%24eNcRYpt3D%24119%24eNcRYpt3D%2499%24eNcRYpt3D%24109%24eNcRYpt3D%2486%24eNcRYpt3D%2448%24eNcRYpt3D%2473%24eNcRYpt3D%2471%24eNcRYpt3D%24104%24eNcRYpt3D%24104%24eNcRYpt3D%2490%24eNcRYpt3D%2472%24eNcRYpt3D%2486%24eNcRYpt3D%24122%24eNcRYpt3D%2473%24eNcRYpt3D%2471%24eNcRYpt3D%2449%24eNcRYpt3D%24118%24eNcRYpt3D%2489%24eNcRYpt3D%24105%24eNcRYpt3D%2465%24eNcRYpt3D%24115%24eNcRYpt3D%2499%24eNcRYpt3D%2450%24eNcRYpt3D%2457%24eNcRYpt3D%24105%24eNcRYpt3D%2473%24eNcRYpt3D%2472%24eNcRYpt3D%2474%24eNcRYpt3D%24118%24eNcRYpt3D%2499%24eNcRYpt3D%2471%24eNcRYpt3D%2470%24eNcRYpt3D%2477%24eNcRYpt3D%24"]

for i in msg: 
    decrypt(i)
```

### Result
Pengirim: 0x123SPM
Bom siap diledakkan besok malam, kode aktivasi adalah  GamaCTF{b3r4ntaZ_T3rr0r1sme} 
Lapor bos, bom sudah terpasang


### Flag
GamaCTF{b3r4ntaZ_T3rr0r1sme}