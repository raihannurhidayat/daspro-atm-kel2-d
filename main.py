import os

repeat = "no"
logged = False
isused = "yes"
lang = True
bahasa = None
security = "yes"

data_user = [
    {
        "id": "1",
        "noRekening": 237006108,
        "pin": "123",
        "username": "jaja",
        "saldo": 1000000,
    },
    {
        "id": "2",
        "noRekening": 237006109,
        "pin": "54321",
        "username": "otong",
        "saldo": 1000000,
    },
]


def cekLogin(p):
    for x in data_user:
        if x["pin"] == p:
            return x
    return False


def cekUser(id):
    for i in range(len(data_user)):
        if data_user[i]["id"] == str(id):
            return int(i)
    return -1


while isused == "yes":
    while logged == False:
        os.system("cls")
        count = 3
        print("")

        while security == "yes":
            os.system("cls")
            print("===selamat datang di ATM===")
            pin = input("Masukkan PIN: ")
            print("")
            dataUserlogin = cekLogin(pin)
            if dataUserlogin != False:
                os.system("cls")
                print("Selamat datang, " + dataUserlogin["username"])
                userid = dataUserlogin["id"]
                logged = True
                repeat = "yes"
            elif count == 1:
                security = "no"
                logged = None
                isused = "no"
                input("acount atm anda telah terblokir")
            else:
                count = count - 1
                print("Kode PIN ada salah ")
                print(f"Percobaan anda sisa {count}")
                input("enter untuk login...")

            while repeat == "yes" and logged == True:
                print("1. Cek saldo")
                # untuk modul cek saldo
                print("2. Tarik Tunai")
                # untk modul tarik tunai
                print("3. Deposit")
                # untuk deposit
                print("4. logout")

                print("5. Keluar")
                selected = int(input("Pilih Menu (masukkan nomor): "))

                if selected == 4:
                    logged = False
                if selected == 5:
                    logged = None
                    isused = "no"
                    security = "no"
