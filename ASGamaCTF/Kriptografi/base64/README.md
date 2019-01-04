# __ASGama CTF__ 
## _base64_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 5 | l0l

**Description:** 

> QVNHYW1he2phbGFuX2hla2Vsa3VfbXVsYWlfZGFyaV9iZWxhamFyX2VuY29kaW5nfQ==
>
> Format: ASGama{}

### base64
Sesuai judulnya, hanya perlu didecode base64.

### Payload
```py
print "QVNHYW1he2phbGFuX2hla2Vsa3VfbXVsYWlfZGFyaV9iZWxhamFyX2VuY29kaW5nfQ==".decode('base64')
```

### Result
```
>>> print "QVNHYW1he2phbGFuX2hla2Vsa3VfbXVsYWlfZGFyaV9iZWxhamFyX2VuY29kaW5nfQ==".decode('base64')
ASGama{jalan_hekelku_mulai_dari_belajar_encoding}
```

### Flag
ASGama{jalan_hekelku_mulai_dari_belajar_encoding}