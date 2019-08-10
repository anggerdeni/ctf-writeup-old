# intro
## 250 points | 26 solves

### Description
> hi i want to introduce my self. My name is friska and .............  
> format flag: hacktoday{uppercase_flag}  
> author: monhack  

Setelah dibuka pake wireshark, keliatannya usb capture file. Coba analisis dengan tshark:  
```
$ tshark -r intro.pcapng -q -z io,phs

===================================================================
Protocol Hierarchy Statistics
Filter:

usb                                      frames:7936 bytes:530824
  text                                   frames:15 bytes:1085
  usb.capdata                            frames:2850 bytes:205195
===================================================================
```

Terdapat usb.capdata. Langsung coba dump semua hasilnya:  
`$ tshark -r ../challenge/intro.pcapng -T fields -e usb.capdata > capdata`

Langsung edit script yang ada di [sini](https://medium.com/@ali.bawazeeer/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4)

```
friska is the fast section <del>  <del>  <del> ion of the csardas a hungarian folk dance or of most of liszt hungarian rhapsodies which take <del>  <del>  <del>  <del> take their fr <del> orm this dance the fis <del>  <del> riska is generally either turbulent or jubilant in tone griff holland togehter <del>  <del>  <del>  <del> ther with ed bo <del> rown founded the business in 209 <del>  <del> 09 <del> 09 based on a principle i <del> of <del>  <del> f  <del> ivering fell  <del>  <del>  <del> el good food mas <del> de from fres  <del> h quality and responbility  <del>  <del>  <del>  <del>  <del>  <del>  <del> sibly <del>  <del> y source <del>  <del> ced ingredients both founders are insed <del>  <del> ider 42 under 42 alumni the company cy <del> urrently operates fl <del> our brancehe <del>  <del>  <del> hes near high disenty <del>  <del>  <del>  <del>  <del>  <del> ensity office building <del>  <del>  <del>  <del> dings whith <del>  <del>  <del>  <del> ith 70 per cent of its revene <del> ues coming from lunchtime trade i saw him wal <del>  <del> lkinh  <del>  <del> h  <del>  <del> g around the backyard like somethings troubling him <del> m flag is  <del>  <del>  <del>  <del>  is i-l3arn-us8-c4ptu <del>  <del>  <del> ptu <del> ur3 i called him in ad <del> d <del> nd when ii  <del>  <del>  asked whats going on he just said can i go out for a while i kon <del>  <del> w <del> now he just  <del>  <del>  <del>  <del>  <del> just trying to change the subject then again maybe he just mee <del>  <del>  <del> needed soe  <del>  <del> me fres air to clear i <del> his md <del> ind so i ssid yes the en <del>  <del> nest  <del>  <del>  <del> xt day i saw him washing my neighbours car and when he came home i asked him why he would do that <del>  <del>  <del>  <del> hat <del>  <del> th <del>  <del>  <del> ta <del> hat he just said he told me to so i told him to take a bo <del> athn <del>  and do this <del>  <del> os  <del>  <del>  <del>  <del>  <del> his homewe <del> ork h <del> when he was done i told him that he din <del> dnt have to wash th  <del> e car because it sax <del>  <del>  <del> was not his responsibilitie <del>  <del> ies heLetfArrowLetfArrowLetfArrowLetfArrowLetfArrowRightArrowRightArrowRightArrowRightArrowRightArrow kj <del> j <del>  <del> just nod
```
[solver](./solution/solve.py)

`flag is  <del>  <del>  <del>  <del>  is i-l3arn-us8-c4ptu <del>  <del>  <del> ptu <del> ur3`

### Flag
hacktoday{I-L3ARN-US8-C4PTUR3}