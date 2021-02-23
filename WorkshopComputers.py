##  BİLGİSAYAR SINIFI OLUŞTURALIM ##
import time
class Computers():
    def __init__(self,marka="BİLGİ YOK",model="BİLGİ YOK",fiyat=0.0,sepetim = []):
        self.marka = marka
        self.model = model 
        self.fiyat = fiyat
        self.sepetim = sepetim
    def sepetOnay(self):
        print("SEPETE EKLEMEK İÇİN 1'e , ANA MENÜYE DÖNMEK İÇİN İÇİN SIFIRA BASINIZ..")
        sepet= input("ONAY:")
        if (sepet=="1"):
            print("SEÇİMİNİZ BAŞARIYLA EKLENDİ... ")       
        else :
            self.marka = "SEÇİM YAPILMADI"
            self.model = "SEÇİM YAPILMADI"
            self.fiyat = 0.0
            print("ANA MENÜYE DÖNÜYORUM...")
    def MonsterModel(self):
        Monster_serisi = ["ABRA","TULPAR","SEMRUK"]
        self.marka = "MONSTER"
        print(self.marka," MARKA İLE İLGİLİ MODELLER YÜKLENİYOR..")
        time.sleep(1)
        i = 1
        for seriler in Monster_serisi:
            print("MODEL {i} : ".format(i = i),seriler)
            i+=1
        print("FİYAT ARALIKLARI YÜKLENİYOR... \n1. 5999-7999 \n2. 7999- 9999 \n3. 9999-12999")
        fiyat_secim = input("FİYAT ARALIĞI BELİRLEYİNİZ:")
        if (fiyat_secim == "1"):
            self.model = "ABRA"
            self.fiyat = 7500
            print("BU FİYATA EN UYGUN PC : ",self.model ,"=>", self.fiyat,"TL")           
        elif (fiyat_secim == "2") :
            self.fiyat = 9500
            self.model = "TULPAR"
            print("BU FİYATA EN UYGUN PC : ",self.model ,"=>", self.fiyat, "TL")
        elif (fiyat_secim == "3") :
            self.fiyat = 10500
            self.model = "SEMRUK"
            print("BU FİYATA EN UYGUN PC : ",self.model ,"=>", self.fiyat, "TL")           
    def AsusModel(self):
        Asus_serisi = ["TUF GAMİNG","ROG","VİVOBOOK"]
        self.marka = "ASUS"
        print(self.marka," MARKA İLE İLGİLİ MODELLER YÜKLENİYOR..")
        time.sleep(1)
        i = 1
        for seriler in Asus_serisi:
            print("MODEL {i} : ".format(i = i) ,seriler)
            i+=1
        print("FİYAT ARALIĞI YÜKLENİYOR... \n1. 6999-9999 \n2. 9999- 12999 \n3. 12999-14999")
        fiyat_secim = input("FİYAT ARALIĞI BELİRLEYİNİZ: ")
        if (fiyat_secim == "1"):
            self.model = "TUF GAMING"
            self.fiyat = 9000
            print("BU FİYATA EN UYGUN PC: ",self.model ,"=>", self.fiyat, "TL")
        elif (fiyat_secim == "2") :
            self.model = "ROG"
            self.fiyat = 10000
            print("BU FİYATA EN UYGUN PC :",self.model ,"=>", self.fiyat, "TL")
        elif (fiyat_secim == "3") :
            self.model = "VİVOBOOK"
            self.fiyat = 12000
            print("BU FİYATA EN UYGUN PC :",self.model ,"=>", self.fiyat, "TL")
    def MsiModel(self):
        Msi_serisi = ["GF63","STİN","LEOPARD"]
        self.marka = "MSİ"
        print(self.marka," MARKA İLE İLGİLİ MODELLER YÜKLENİYOR..")
        time.sleep(1)
        i = 1
        for seriler in Msi_serisi:
            print("MODEL {i} : ".format(i = i),seriler)
            i+=1
        print("FİYAT ARALIĞI YÜKLENİYOR... \n1. 6999-9999 \n2. 9999- 12999 \n3. 12999-14999")
        fiyat_secim = input("FİYAT ARALIĞI BELİRLEYİNİZ:")
        if (fiyat_secim == "1"):
            self.model = "GF63"
            self.fiyat = 9000
            print("BU FİYATA EN UYGUN PC : GF63 => 9000 TL")
        elif (fiyat_secim == "2") :
            self.model = "STİN"
            self.fiyat = 11000
            print("BU FİYATA EN UYGUN PC :",self.model ," => ",self.fiyat)
        elif (fiyat_secim == "3") :
            self.model = "LEOPARD"
            self.fiyat = 13000
            print("BU FİYATA EN UYGUN PC :",self.model, " => ",self.fiyat)
    def __str__(self):
        print("ÜRÜN BİLGİLERİ YÜKLENİYOR...")
        time.sleep(1)
        return "MARKA : {} \nMODEL: {} \nFİYAT: {} TL  \n ".format(self.marka,self.model,self.fiyat)   
computer = Computers()
print("""
**********
YEE.com İLE EN İYİ BİLGİSAYARI SEÇİYORUZ
HANGİ BİLGİSAYAR İLE İLGİLİ BİLGİ ALMAK İSTERSİNİZ ?
1. MONSTER
2. ASUS
3. MSİ

**********
""")
while True:
    secim = input("ALMAK İSTEDİĞİNİZ BİLGİSAYAR: ")
    if (secim == "1"):
        computer.MonsterModel()
        computer.sepetOnay()
        print(computer)
    elif (secim == "2"):
        computer.AsusModel()
        computer.sepetOnay()
        print(computer)
    elif (secim == "3"):
        computer.MsiModel()
        computer.sepetOnay()
        print(computer)
    else:
        print("OOPS! BİR ŞEYLER YANLIŞ GİTTİ GALİBA...")
        break
    print("ANA MENÜYE DÖNÜYORUM...")
    



