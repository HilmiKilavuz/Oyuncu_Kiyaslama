# bu projede girilen iki futbolcu değerlerini imagechart servere sayaesinde 
# grafiker börintüde birbiri ile kıyaslamaya çalıştık
#burda import edilmesi gereken modülleri import ettim
import requests
from PIL import Image
from io import BytesIO
#bir oyuncu classı oluşturarak oyuncu bilgilerini alıp, kıyas yapıp , işleyip en sonunda grafiği vermeyi amaçaladım.

class Oyuncu():
    #gerekli özellikleri aldım
    def __init__(self) :
        self.isim = ""
        self.hız = 0
        self.şut = 0
        self.pas = 0
        self.dribling = 0
        self.defans = 0
        self.fizik = 0
#aldığımız oyuncu verileri direkt serveren istediği versiyonda olmadığı için aralarına 
# virgül koyma amacıyla bir metod tanımladık ve join metodunu  kullandım
    def yetenek_hazirla(self):
      #bu grafik yapısında bir çember oluşturduğu için ilk argümanı en son tekrar verilmesi gerekmekte
      return  ",".join([
            str(self.hız),
            str(self.şut),
            str(self.pas),
            str(self.dribling),
            str(self.defans),
            str(self.fizik),
            str(self.hız)
        ])

        

#burada aldığım verileri grafik haline getirmek için server urlsinin aldım.
# Ardından girilmesi gereken parametreleri girdim.
    def gorsellestirme(self):
        data_url="https://image-charts.com/chart"
        payload={
            "chco":"3092de",
            "chd":"t:{}".format(self.yetenek_hazirla()),
            "chdl": self.isim,
            "chdlp":"b",
            "chs":"480x480",
            "cht":"r" ,
            "chtt":"Futbolcu Özellikleri",
            "chl":"Hız|Şut|Pas|Dribling|Defans|Fizik",
            "chxl":"0:|0|20|40|60|80|100",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm":"B,AAAAAABB,0,0,0"
                }

        response = requests.post(data_url,data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()
        #Bu metod da ise alınan iki oyuncu arasında kıyas yapabilmek için 
        # yapılan veri alma yöntemini biraz değiştirerek kıyas yapabilme şansı verdim.
    def yetenek_kiyasla(self,rakip_oyuncu):
        data_url="https://image-charts.com/chart"
        payload={
            "chco":"3092de,027182",
            "chd":"t:{}|{}".format(self.yetenek_hazirla(),rakip_oyuncu.yetenek_hazirla()),
            "chdl": self.isim +"|"+rakip_oyuncu.isim,
            "chdlp":"b",
            "chs":"480x480",
            "cht":"r" ,
            "chtt":"Futbolcu Özellikleri",
            "chl":"Hız|Şut|Pas|Dribling|Defans|Fizik",
            "chxl":"0:|0|20|40|60|80|100",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm":"B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0"
                }

        response = requests.post(data_url,data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()
#kullanıcıdan kıyas yapılacak özellikleri alan fonksiyon        
    def deger_al(self):
        # İsim değeri
        while True:
            name = input("Oyuncunun adını giriniz: ")
            if name.isalpha() :
                self.isim = name
                break
            else:
                print("Girdiğiniz değer bir isim değildir, tekrar deneyin.")

        # Hız değeri
        while True:
            speed = input("{} hızını giriniz: ".format(self.isim))
            if speed.isdigit() and int(speed)<=100 and int(speed)>0:
                self.hız = int(speed)
                break
            else:
                print("Girdiğiniz değer bir sayı değildir, tekrar deneyin.")

        # Şut değeri
        while True:
            shoot = input("{} şutunu giriniz: ".format(self.isim))
            if shoot.isdigit() and int(shoot) <=100 and int(shoot)>0:
                self.şut = int(shoot)
                break
            else:
                print("Girdiğiniz değer bir sayı değildir, tekrar deneyin.")

        # Pas değeri
        while True:
            player_pass = input("{} pasını giriniz: ".format(self.isim))
            if player_pass.isdigit() and int(player_pass)<=100 and int(player_pass)>0:
                self.pas = int(player_pass)
                break
            else:
                print("Girdiğiniz değer bir sayı değildir, tekrar deneyin.")

        # Dribling değeri
        while True:
            player_dribling = input("{} driblingini giriniz: ".format(self.isim))
            if player_dribling.isdigit() and int(player_dribling)<=100 and int(player_dribling)>0:
                self.dribling = int(player_dribling)
                break
            else:
                print("Girdiğiniz değer bir sayı değildir, tekrar deneyin.")

        # Defans değeri
        while True:
            defanse = input("{} defansını giriniz: ".format(self.isim))
            if defanse.isdigit() and int(defanse)  <=100 and int(defanse) >0:
                self.defans = int(defanse)
                break
            else:
                print("Girdiğiniz değer bir sayı değildir, tekrar deneyin.")

        # Fizik değeri
        while True:
            physical = input("{} fiziğini giriniz: ".format(self.isim))
            if physical.isdigit() and int(physical)<=100 and int(physical)>0:
                self.fizik = int(physical)
                break
            else:
                print("Girdiğiniz değer bir sayı değildir, tekrar deneyin.")





#en son olarak değerleri girdim
oyuncu1= Oyuncu()
oyuncu1.deger_al()
oyuncu2=Oyuncu()
oyuncu2.deger_al()
#burada ise kimin kim ile kıyas yapılacağını girdim.

oyuncu1.yetenek_kiyasla(oyuncu2)