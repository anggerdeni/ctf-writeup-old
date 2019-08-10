# robot-o
## 250 points | 27 solves

### Description
> Robot-o, robot buatan Friska, masih dalam tahap pengembangan sehingga terdapat corrupt pada audio yang dikeluarkan robot-o. > Bisakah kamu memperbaikinya?
> format flag: hacktoday{flag}
> author: deomkicer

### Identification
```bash
$ file robot-o.voice
robot-o.voice: RIFF (little-endian) data, WAVE audio
```

Coba langsung buka file itu:
```bash
Playing: /home/l0l/CTF/CTF/Soal/Writeup/ctf-writeup/HackToday-2019/Forensic/robot-o/challenge/robot-o.voice
[ffmpeg/demuxer] wav: no 'fmt ' or 'XMA2' tag found
[lavf] avformat_open_input() failed
[ffmpeg/demuxer] wav: no 'fmt ' or 'XMA2' tag found
[lavf] avformat_open_input() failed
Failed to recognize file format.
```

Hmm sepertinya ada error di header, coba cek spesifikasi file RIFF WAVE.  
- [Reference1](http://www.topherlee.com/software/pcm-tut-wavformat.html)
- [Reference2](http://soundfile.sapp.org/doc/WaveFormat/)

Header file yang kita terima: 
``` bash
$ xxd robot-o.voice |head
00000000: 5249 4646 d40a 0400 5741 5645 0000 0000  RIFF....WAVE....
00000010: 1000 0000 0100 0100 401f 0000 401f 0000  ........@...@...
00000020: 0100 0800 0000 0000 b00a 0400 8083 91ab  ................
00000030: cbe3 ecdf bd8d 582b 0c04 1437 699e cef0  ......X+...7i...
00000040: fcf2 d3a5 703e 1805 0923 4e82 b6e0 f8fa  ....p>...#N.....
00000050: e6bf 8d58 2a0d 0412 3565 9aca edfc f4d7  ...X*...5e......
00000060: a974 421a 0608 2049 7db1 dcf7 fbe9 c392  .tB... I}.......
00000070: 5d2e 0e04 1031 6095 c6eb fcf6 daae 7946  ]....1`.......yF
00000080: 1d07 071d 4578 add9 f5fc ebc8 9661 3211  ....Ex.......a2.
00000090: 040e 2d5b 90c2 e8fb f7dd b27e 4a20 0806  ..-[.......~J ..
```

Setelah baca-baca referensi, terlihat jelas kita kekurangan 2 jenis header field: 
- Format ('fmt ')  
- Subchunk2ID ('data')

Saya tertipu oleh Referensi1 yang menyatakan bahwa 
`13-16 	"fmt " 	Format chunk marker. Includes trailing null` saya mengira berarti kita isi kan dengan byte 'fmt\x00'.
Ternyata setelah baca referensi lain terdapat tanda `<spasi>` di akhir kata fmt.  
Tinggal kita edit header filenya.
```bash
$ xxd robot-o-fixed.voice  | head
00000000: 5249 4646 d40a 0400 5741 5645 666d 7420  RIFF....WAVEfmt
00000010: 1000 0000 0100 0100 401f 0000 401f 0000  ........@...@...
00000020: 0100 0800 6461 7461 b00a 0400 8083 91ab  ....data........
00000030: cbe3 ecdf bd8d 582b 0c04 1437 699e cef0  ......X+...7i...
00000040: fcf2 d3a5 703e 1805 0923 4e82 b6e0 f8fa  ....p>...#N.....
00000050: e6bf 8d58 2a0d 0412 3565 9aca edfc f4d7  ...X*...5e......
00000060: a974 421a 0608 2049 7db1 dcf7 fbe9 c392  .tB... I}.......
00000070: 5d2e 0e04 1031 6095 c6eb fcf6 daae 7946  ]....1`.......yF
00000080: 1d07 071d 4578 add9 f5fc ebc8 9661 3211  ....Ex.......a2.
00000090: 040e 2d5b 90c2 e8fb f7dd b27e 4a20 0806  ..-[.......~J ..
```

Setelah akhirnya bisa diputar, ternyata audio ini adalah pesan morse, langsung saja saya decode pake [onlinedecoder](https://morsecode.scphillips.com/labs/audio-decoder-adaptive/) (males ngedecode sendiri)

Hasilnya agak kacau : 
> A TTTT T TTTT TTIAG IS 8AE8CC93E223D5F957CE8B078D2020E7

Tapi masih bisa kebaca

### Flag
hacktoday{8AE8CC93E223D5F957CE8B078D2020E7}