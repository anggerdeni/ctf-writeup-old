# flag.io
## 250 points | 45 solves

### Description
> Come play and join with us on our brand new io game!
> http://not.codepwnda.id:50001
> author: idzharbae

Ketika buka page, kita diberi tahu bahwa server telah mengirim flag, `you just wont listen`.  
![](./solution/1.png)  
Maka kita coba buka tab network pada console browser, lalu inspeksi salah satu response yang kita terima.  
![](./solution/2.png)  
Terlihat seperti base64, langsung decode:  
![](./solution/3.png)

### Flag
hacktoday{As_you_Humans_say,_Im_all_ears}