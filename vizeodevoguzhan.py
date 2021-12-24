Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class tarifler :
    def tarif_add(self) :
        tarifadi = input("Tarıf adi : ")
        tarif.append(tarifadi)
        while True :
            tarifyapilisasama = input('Tarif Yapılış Aşaması Ekle(Aşamalarınız Sonlandıysa "53" yazınız.) : ')
            if tarifyapilisasama == "53" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifyapilisasama)


    def show(self) :
        number = len(tarifler_listesi)
        print("Bütün Tarifler")
        for adim in tarif :
                print(adim)




def menu() :
    while True :
        print("\Tarif Ekle : 1\nTarifleri Goster : 2\n Çıkış Yap : 3 ")
        secim = input("Yapmak İstediğiniz İşlem Numarasını Giriniz: ")
        islem = tarifler()
        if secim == "1" :
            islem.tarif_add()
        elif secim == "2" :
            islem.show()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatalı Giriş Yaptınız.")



tarifler_listesi = []
tarif = []

menu()