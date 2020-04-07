# TubesDaspro
Pastikan sudah ada potongan kode ini:

```python
  import data
  data.loadFile()
```

## BATCH 1
### Sign Up User

Ini adalah sebuah prosedur.<br/>
Prosedur ini akan menambahkan data pada
```python
  data.user["Data"]
```
Jangan lupa juga mevalidasi data yang diinput

### Login User
Fungsi ini tidak menerima parameter apapun.<br/>
Fungsi ini mengembalikan data pengguna yang berhasil login.<br/>
Saldo defaulnya Rp.0.
Jangan lupa juga mevalidasi data yang diinput
contoh:
```python
  def login_user():
    ...
    ...
    return {'Username': 'Zizi-zizi', 'Nama': 'ZuZu', 'Saldo': '0', 'Tanggal_Lahir': '13/05/2005', 'Role': 'Pemain', 'Password': 'Zazi_798'}
```
### Pencarian Pemain
Ini adalah sebuah prosedur.<br/>
Prosedur akan meminta input username <br/>
Jika tidak ada pengguna dengan username terkait, tampilkan pesan error.<br/>
Ingat user yang dapat dicari hanya user yang memiliki role "Pemain"
Contoh:
```python
  def pencarian_pemain():
    username = input()
    ...
    ...
    print("Nama pemain : .....")
    print("Tinggi Pemain : ......")
    ...
    ...
    
```

### Pencarian Wahana
Ini adalah sebuah prosedur<br/>
Prosedur akan meminta beberapa faktor<br/>
Faktornya liat di pdf tugasnya aja ya<br/>
Prosedur ini mirip prosedur pencarian_pemain.<br/>
Di prosedur ini ingat untuk mevalidasi input faktor tersebut.

### Pembelian Tiket
Untuk prosedur ini, anggap proses login sudah selesai.
Fungsi ini menerima input berupa data pengguna yang sudah login.
Waktu pengerjaan, ingat data yang harus diubah adalah:
```python
  data.kepemilikan_tiket
  data.pembelian_tiket
```
Contoh:
```python
  import data
  data.loadFile()
  def pembelian_tiket(userInfo):
    ...
    ...
    data.kepemilkan_tiket = ...
    data.pembelian_tiket = ...
```
Contoh pemanggilan
```python
  user = {'Username': 'Zizi-zizi', 'Nama': 'ZuZu', 'Saldo': '0', 'Tanggal_Lahir': '13/05/2005', 'Role': 'Pemain', 'Password': 'Zazi_798'}
  pembelian_tiket(user)
```

