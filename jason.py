import data
data.loadFile()
def pencarian_pemain():
    username = input("Username : ")
    found = False
    for i in data.user["Data"]:
        if username == i["Username"]:
            found = True
            print("Nama Pemain : ",i["Nama"])
            print("Tinggi Pemain : ",i["Tinggi_Pemain"])
            print("Tanggal Lahir : ",i["Tanggal_Lahir"])
    if not found:
        print("Tidak ada pemain dengan username ",username)

def kritik_dan_saran(userInfo):
    id_wahana = input("Masukkan ID Wahana : ")
    tanggal_pelaporan = input("Masukkan Tanggal Pelaporan (dd/mm/yy) : ")
    kritik_saran = input("Kritik/Saran Anda : ")
    kritikData = {
        "Username" : userInfo["Username"],
        "Tanggal_Kritik" : tanggal_pelaporan,
        "ID_Wahana" : id_wahana,
        "Isi_Kritik" : kritik_saran
    }
    data.kritik_dan_saran["Data"].append(kritikData)
    data.saveFile()
def melihat_riwayat_pengguna_wahana():
    ID_Wahana = input("Masukkan ID Wahana : ")
    for i in data.penggunaan_tiket["Data"]:
        if i["ID_Wahana"] == ID_Wahana:
            print("{} | {} | {}".format(i["Tanggal_Penggunaan"],i["Username"],i["Jumlah_Tiket"]))
def exit():
    response = input("Apakah Anda Yakin Ingin Keluar??(Y/N)")
    if response == "Y":
        return True
    elif response == "N":
        return False