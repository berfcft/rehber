import sqlite3

class TelefonRehberi:
    def __init__(self,TelefonRehberi):
        self.conn = sqlite3.connect(TelefonRehberi)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS rehber
                               (isim TEXT PRIMARY KEY, numara TEXT)''')
        self.conn.commit()

    def kisi_ekle(self, isim, numara):
        try:
            self.cursor.execute("INSERT INTO rehber (isim, numara) VALUES (?, ?)", (isim, numara))
            self.conn.commit()
            print(f"{isim} rehbere eklendi.")
        except sqlite3.IntegrityError:
            print(f"{isim} zaten rehberde bulunuyor.")

    def kisileri_listele(self):
        self.cursor.execute("SELECT * FROM rehber")
        kisiler = self.cursor.fetchall()
        for kisi in kisiler:
            print(f"{kisi[0]}: {kisi[1]}")

    def __del__(self):
        self.conn.close()

# SQLite veritabanı dosyası oluşturalım veya var olanı açalım
rehberim = TelefonRehberi("telefon_rehberi.db")

# Kullanıcıdan bilgileri alarak kişi ekleyelim
isim = input("Kişinin adını girin: ")
numara = input("Kişinin numarasını girin: ")
rehberim.kisi_ekle(isim, numara)

# Rehberdeki kişileri listeleme
print("\nRehberdeki Kişiler:")
rehberim.kisileri_listele()