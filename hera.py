import data
data.loadFile()

def cariwahana() :
    print ("Jenis batasan umur :")
    print ("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan :")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    x = int(input("Batasan umur pemain :"))
    y = int(input("Batasan tinggi badan :"))
    
    if x == 1 and y==1:
        for i in data.wahana["Data"]:
            if i["Batasan_Umur"] == "Anak-anak" and i["Batasan_Tinggi"] == ">=170" :
                print(i["ID_Wahana"],'|',i["Nama_Wahana"],'|',i["Harga_Tiket"])
    elif x==1 and y == 2 :
        for i in data.wahana["Data"]:
            if i["Batasan_Umur"] == "Anak-anak" and i["Batasan_Tinggi"] == "tanpa batasan" :
                print(i["ID_Wahana"],'|',i["Nama_Wahana"],'|',i["Harga_Tiket"])
    elif x==2 and y==1 :
        for i in data.wahana["Data"]:
            if i["Batasan_Umur"] == "dewasa" and i["Batasan_Tinggi"]==">=170" :
                print(i["ID_Wahana"],'|',i["Nama_Wahana"],'|',i["Harga_Tiket"])
    elif x==2 and y==2 :
        for i in data.wahana["Data"]:
            if i["Batasan_Umur"] == "dewasa" and i["Batasan_Tinggi"] == "tanpa batasan" :
                print(i["ID_Wahana"],'|',i["Nama_Wahana"],'|',i["Harga_Tiket"])
    elif x==3 and y==1 :
        for i in data.wahana["Data"]:
             if i["Batasan_Umur"] == "semua umur" and i["Batasan_Tinggi"]== ">=170" :
                print(i["ID_Wahana"],'|',i["Nama_Wahana"],'|',i["Harga_Tiket"])
    elif x==3 and y==2 :
        for i in data.wahana["Data"]:
            if i["Batasan_Umur"] == "semua umur" and i["Batasan_Tinggi"]== "tanpa batasan" :
                print(i["ID_Wahana"],'|',i["Nama_Wahana"],'|',i["Harga_Tiket"])
                

def lihat_laporan():
    r = len(data.kritik_dan_saran["Data"]) 
    L=['a' for i in range(r)]
    h=0
    for i in data.kritik_dan_saran["Data"] :
        L[h]=i["ID_Wahana"]
        h=h+1
    S=sorted(L)
    for k in range(r):
        for i in data.kritik_dan_saran["Data"] :
            if S[k]== i["ID_Wahana"]:
                print(i["ID_Wahana"],'|',i["Tanggal_Kritik"],'|',i["Username"],'|',i["Isi_Kritik"])
          

def refund(user):
    a = input("Masukkan ID wahana : ")
    b = int(input("Jumlah tiket yang di-refund : "))
    c = input("Masukkan tanggal refund dd/mm/yy : ")
    x = 0
    for i in data.kepemilikan_tiket["Data"]:
        if user["Username"] == i["Username"] and i["ID_Wahana"]==a:
            x=int(i["Jumlah_Tiket"])
    print(x)
    if b <= x:
        for i in data.wahana["Data"]:
            if a==i["ID_Wahana"]:
                refund = b*int(i["Harga_Tiket"])
        for i in data.kepemilikan_tiket["Data"]:
            if user["Username"]==i["Username"] and a==i["ID_Wahana"]:
                i["Jumlah_Tiket"]=str(int(i["Jumlah_Tiket"])-b)
        for i in data.user["Data"]:
            if user["Username"]==i["Username"]:
                i["Saldo"]=str(int(i["Saldo"])+refund)
        dataRefund = {
                "Username" : user["Username"],
                "Tanggal_Refund" : c,
                "ID_Wahana" : a,
                "Jumlah_Tiket" : b
        }
        data.refund_tiket["Data"].append(dataRefund)
        data.saveFile()
    else :
        print("Anda tidak memiliki tiket terkait.")
user = {'Nama': 'Andi', 'Tanggal_Lahir': '01/01/2001', 'Username': 'hello_again', 'Password': "b'$2b$12$dbJej0PgToXSuLD0UYvEUe7bIt.H/.5T3d8mrrmPV9paYZY9NrA5O'", 'Role': 'Pemain', 'Saldo': '40000', 'Tinggi_Badan': '176', 'gold': '1'} 
refund(user)