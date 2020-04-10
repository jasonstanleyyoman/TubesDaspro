import data
import bcrypt
data.loadFile()
def goldAccount():
    while True:
        username = input("Masukkan username yang ingin di-upgrade (Harga Upgrade = 75000): ")
        found = False
        for i in data.user["Data"]:
            if i["Username"] == username:
                found = True
                if i["gold"] == "1":
                    print("Akun ini sudah gold")
                else:
                    if int(i["Saldo"]) >= 75000:
                        i["Saldo"] = str(int(i["Saldo"]) - 75000)
                        i["gold"] = "1"
                        print("Selamat Akun Anda Sudah gold")
                    else:
                        print("Maaf Saldo Anda Tidak Cukup")
        if not found:
            print("Tidak ada user dengan username seperti itu")
        
        response = None
        while True:
            response = input("Apakah Anda masih ingin lanjut ?? (y/n) : ")
            if response == "y" or response == "n":
                break
            else:
                print("Masukkan antara (y/n)")
        if response == "y":
            continue
        elif response == "n":
            break
            
    data.saveFile()

def encrypt_password(password):
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password,salt)
    return hashed
def check_password(hashed,password):
    password = password.encode("utf-8")
    return bcrypt.checkpw(password,hashed)