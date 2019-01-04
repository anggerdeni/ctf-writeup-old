# __ASGama CTF__ 
## _Caesar_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 10 | l0l

**Description:** 

> BvhvXOA{xvzzn5vm_nj_zut}

### Caesar
Sesuai judulnya, caesar cipher, merupakan algoritme enkripsi classic dengan 'menggeser' nilai huruf pada string sebanyak nilai tertentu.

### Payload
```py
from string import uppercase, lowercase
cipher = "BvhvXOA{xvzzn5vm_nj_zut}"

def decrypt(c,rotation):
 ret = ""
 for i in c:
  if i in uppercase:
   index = uppercase.find(i)
   index += rotation
   ret += uppercase[index % 26]
  elif i in lowercase:
   index = lowercase.find(i)
   index += rotation
   ret += lowercase[index % 26]
  else :
   ret +=i

 return ret

for i in range(1,14):
 print i,decrypt(cipher,i)
```

### Result
```
1 CwiwYPB{ywaao5wn_ok_avu}
2 DxjxZQC{zxbbp5xo_pl_bwv}
3 EykyARD{ayccq5yp_qm_cxw}
4 FzlzBSE{bzddr5zq_rn_dyx}
5 GamaCTF{caees5ar_so_ezy}
6 HbnbDUG{dbfft5bs_tp_faz}
7 IcocEVH{ecggu5ct_uq_gba}
8 JdpdFWI{fdhhv5du_vr_hcb}
9 KeqeGXJ{geiiw5ev_ws_idc}
10 LfrfHYK{hfjjx5fw_xt_jed}
11 MgsgIZL{igkky5gx_yu_kfe}
12 NhthJAM{jhllz5hy_zv_lgf}
13 OiuiKBN{kimma5iz_aw_mhg}
```

### Flag
GamaCTF{caees5ar_so_ezy}