# TubesDaspro
Pastikan sudah ada potongan kode ini:

```python
  import data
  data.loadFile()
```

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
Saldo defaulnya Rp.0.<br/>
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
Prosedur ini tidak menerima parameter apapun. <br/>
Prosedur akan meminta beberapa faktor<br/>
Faktornya liat di pdf tugasnya aja ya<br/>
Prosedur ini mirip prosedur pencarian_pemain.<br/>
Di prosedur ini ingat untuk mevalidasi input faktor tersebut.

### Pembelian Tiket
Untuk prosedur ini, anggap proses login sudah selesai.<br/>
Prosedur ini menerima input berupa data pengguna yang sudah login.<br/>
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
    # OR
    data.kepemilikan_tiket["Data"][0]["Jumlah_Tiket"] = ...
    data.saveFile()
```
Contoh pemanggilan
```python
  user = {'Username': 'Zizi-zizi', 'Nama': 'ZuZu', 'Saldo': '0', 'Tanggal_Lahir': '13/05/2005', 'Role': 'Pemain', 'Password': 'Zazi_798'}
  pembelian_tiket(user)
```
Ingat untuk mevalidasi.<br/>
Yang harus divalidasi baca di pdf tugas ya.

### Menggunakan Tiket
Untuk prosedur ini, anggap proses login sudah selesai.<br/>
Prosedur ini menerima input berupa data pengguna yang sudah login.<br/>
Speknya tinggal liat di pdf tugas.
Contoh:
```python
  import data
  data.loadFile()
  def menggunakan_tiket(userInfo):
    ...
    ...
    data.kepemilkan_tiket = ...
    data.penggunaan_tiket = ...
    # OR
    data.kepemilikan_tiket["Data"][0]["Jumlah_Tiket"] = ...
    data.saveFile()
    
```
Ingat juga untuk mevalidasi

### Refund
Sama juga kea prosedur menggunakan_tiket dan pembelian_tiket<br/>
Contoh:
```python
  import data
  data.loadFile()
  def pembelian_tiket(userInfo):
    ...
    ...
    data.kepemilkan_tiket = ...
    data.refund_tiket = ...
    # OR
    data.kepemilikan_tiket["Data"][0]["Jumlah_Tiket"] = ...
    data.saveFile()
```
### Kritik Dan Saran
Sama juga kea prosedur menggunakan_tiket dan pembelian_tiket.(Parameternya info pengguna yang login)<br/>
Nanti tinggal tambah data di kritik_dan_saran.csv

### Melihat Kritik Dan Saran
Ini merupakan sebuah prosedur <br/>
Tidak menerima parameter apapun.<br/>
Tinggal looping semua data di kritik_dan_saran.csv

### Menambahkan Wahana Baru
Ini merupakan sebuah prosedur.<br/>
Prosedur ini tidak menerima parameter apapun.<br/>
Ini udh diasumsikan semua input valid

### Top up Saldo
Sama juga kea prosedur menggunakan_tiket dan pembelian_tiket<br/>
Ini prosedur ya.<br/>
Tidak ada parameter
### Melihat Riwayat Pengguna Wahana
Ini prosedur ya<br/>
tidak menerima parameter<br/>
tinggal looping semua data di penggunaan_wahana.csv

### Melihat Jumlah Tiket pemain
Ez lah ya wkwkwk<br/>
sama kea yang di atas

### Exit
Fungsi yang tidak menerima paramter<br/>
mengembalikan True/False



## Nanti Kira-Kira Program utamanya Begini
```python
import data
# import segala macam file python dari yang sudah dibuat
data.loadFile()
user = None

while True:
  if user == None:
    # Nanti disini ditampilkan menu 
    # 1. Login
    # 2. Pencarian Wahana
    # 3. Exit
    userInput = input()
    if userInput == 1:
      user = user_login()
    elif userInput == 2:
      pencarian_wahana()
    elif userInput == 3:
      break
  elif user["Role"] == "Pemain":
    # Tampilkan menu pemain
  elif user["Role"] == "Admin":
    # Tampilkan menu Admin
