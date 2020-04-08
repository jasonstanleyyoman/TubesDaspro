import data # Mengimport utility dari file data, file ini dapat digunakan untuk membaca file dan save file.
'''
    file data.py mempunyai dua fungsi 
    1. loadFile()
        fungsi loadFile() akan membaca seluruh file csv yang akan digunakan dan menyimpannya dalam variabel.
        Variabelnya akan dijelaskan setelah ini.
    2. saveFile()
        fungsi saveFile() akan menyimpan seluruh file csv setelah melakukan perubahan. fungsi ini tidak berjalan 
        otomatis ketika ada file yang diubah. Pengguna harus memanggil fungsi ini ketika ingin save file setelah 
        melakukan perubahan dalam file.
    
    variabel-variabel yang terkait:
        1. data.user
        2. data.wahana
        3. data.kepemilikan_tiket
        4. data.penggunaan_tiket
        5. data.pembelian_tiket
        6. data.refund_tiket
        7. data.kritik_dan_saran
        Coba aja nanti print variabel2 ini.

    pertama-tama, program memanggil fungsi loadFile() dari file data.py. Caranya adalah data.loadFile()

'''
data.loadFile()
'''
    Setelah itu variabel-variabel yang disebutka diatas sudah terisi dan dapat diakses.

    Contoh:
    print(data.user)
    akan menghasilkan:
    {'Column': ['Nama', 'Tanggal_Lahir', 'Username', 'Password', 'Role', 'Saldo'], 
    'Data': [
        {'Username': 'hello_world', 'Nama': 'Andi', 'Saldo': '40000', 'Tanggal_Lahir': '01/01/2001', 'Role': 'Pemain', 'Password': 'Andi_123'}, 
        {'Username': 'budi_budi', 'Nama': 'Budi', 'Saldo': '0', 'Tanggal_Lahir': '02/01/2001', 'Role': 'Admin', 'Password': 'Budi_123'}, 
        {'Username': 'caca_caca', 'Nama': 'Caca', 'Saldo': '30000', 'Tanggal_Lahir': '03/04/2001', 'Role': 'Pemain', 'Password': 'Caca_123'}, 
        {'Username': 'didi_didi', 'Nama': 'Didi', 'Saldo': '0', 'Tanggal_Lahir': '12/12/2001', 'Role': 'Admin', 'Password': 'Didi_123'}, 
        {'Username': 'edu_adu', 'Nama': 'Edu', 'Saldo': '134000', 'Tanggal_Lahir': '23/05/2015', 'Role': 'Pemain', 'Password': 'Adu_123'}, 
        {'Username': 'fafa_fafi', 'Nama': 'Fafa', 'Saldo': '24000', 'Tanggal_Lahir': '13/09/2012', 'Role': 'Pemain', 'Password': 'Fafa_2020'}, 
        {'Username': 'Gaga-gaga', 'Nama': 'Gaga', 'Saldo': '5000', 'Tanggal_Lahir': '12/05/2005', 'Role': 'Pemain', 'Password': 'Gagi_045'}
        ]
    }
    contoh cara mengakses:
        1.data.user["Column"]
            akan menghasilkan
                ['Nama', 'Tanggal_Lahir', 'Username', 'Password', 'Role', 'Saldo']
        2. data.user["Data"]
            akan menghasilkan
                [
                    {'Username': 'hello_world', 'Nama': 'Andi', 'Saldo': '40000', 'Tanggal_Lahir': '01/01/2001', 'Role': 'Pemain', 'Password': 'Andi_123'}, 
                    {'Username': 'budi_budi', 'Nama': 'Budi', 'Saldo': '0', 'Tanggal_Lahir': '02/01/2001', 'Role': 'Admin', 'Password': 'Budi_123'}, 
                    {'Username': 'caca_caca', 'Nama': 'Caca', 'Saldo': '30000', 'Tanggal_Lahir': '03/04/2001', 'Role': 'Pemain', 'Password': 'Caca_123'}, 
                    {'Username': 'didi_didi', 'Nama': 'Didi', 'Saldo': '0', 'Tanggal_Lahir': '12/12/2001', 'Role': 'Admin', 'Password': 'Didi_123'}, 
                    {'Username': 'edu_adu', 'Nama': 'Edu', 'Saldo': '134000', 'Tanggal_Lahir': '23/05/2015', 'Role': 'Pemain', 'Password': 'Adu_123'}, 
                    {'Username': 'fafa_fafi', 'Nama': 'Fafa', 'Saldo': '24000', 'Tanggal_Lahir': '13/09/2012', 'Role': 'Pemain', 'Password': 'Fafa_2020'}, 
                    {'Username': 'Gaga-gaga', 'Nama': 'Gaga', 'Saldo': '5000', 'Tanggal_Lahir': '12/05/2005', 'Role': 'Pemain', 'Password': 'Gagi_045'}
                ] 
        3. data.user["Data"][0]
                akan menghasilkan
                    {'Username': 'hello_world', 'Nama': 'Andi', 'Saldo': '40000', 'Tanggal_Lahir': '01/01/2001', 'Role': 'Pemain', 'Password': 'Andi_123'}
        4. data.user["Data"][0]["Username"]
                akan menghasilkan
                    'hello_world'
        5. data.user["Data"][0]["Role"]
                akan menghasilkan
                    'Pemain'
        
    
'''

'''
    Seluruh data dalam bentuk string. Jadi misalnya Anda ingin menambah saldo pengguna yang berada di indeks 0:
    data.user["Data"][0]["Saldo"] = str(int(data.user["Data"][0]["Saldo"]) + 20000)
    
    Setelah itu, datanya di save
    
    data.saveFile()
'''
print("data.user")
print(data.user)
print()
print("data.user[\"Data\"]")
print(data.user["Data"])
print()
print("data.user[\"Data\"][0]")
print(data.user["Data"][0])
print()
print("data.user[\"Data\"][0][\"Username\"]")
print(data.user["Data"][0]["Username"])

 

