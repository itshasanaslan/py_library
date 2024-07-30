import random
from colorama import Fore, Style,init
init()

green = Style.BRIGHT + Fore.GREEN
red = Style.BRIGHT + Fore.RED
blue = Style.BRIGHT + Fore.BLUE

ilk = ["b bilgi              Bir öğrencinin matematik dersinde dört işlem bilgisini taşıması.",
       "b bilgi              Felsefe dersinde akımlarla ilgili temel sınıflamaları hatırlama.",
       "b bilgi              Kurtuluş savaşı ile ilgili tarihleri söyleme. ",
       "b bilgi              Program geliştirme ile ilgili kavramların tanımını bilme. ",
       "b bilgi              Coğrafya dersinde bölgelerin adını sayma. ",
       "b kavrama            Türkiye’deki yağış durumuna ilişkin bilgileri grafiğe dönüştürebilme yeteneği.",
       "b kavrama            Nüfus artışıyla ilgili geleceğe dönük çıkarımda bulunabilme.",
       "b kavrama            Anne sütünün yararlarını farklı örneklerle açıklama.",
       "b kavrama            Yabancı bir dilde verilen bir cümleyi Türkçe’ye çevirebilme.",
       "b uygulama           Dört işlemle ilgili bir problemi çözme.",
       "b uygulama           Bilimsel yöntemleri kullanarak ödev hazırlama.",
       "b uygulama           Fizikte kuvvet konusuyla ilgili problemleri çözme.",
       "b uygulama           Tasarlanmış modellere göre bir elbise dikme.",
       "b analiz             Bir cümleyi doğru olarak öğelerine ayırabilme.",
       "b analiz             Değişmenin olumlu ve olumsuz yönlerini tespit etme.",
       "b analiz             Avrupa birliğinin ortaklık ilkelerini belirleyebilme.",
       "b analiz             Aile ve toplum arasındaki ilişkileri belirleyebilme.",
       "b sentez             Bir öğrencinin turizm konusunda özgün bir kompozisyon yazması.",
       "b sentez             Kültür konusunda orijinal bir makale yazma.",
       "b sentez             Deniz kirliliğini önlemek için bir takım projeler tasarlayıp geliştirebilme.",
       "b sentez             Demokrasinin,insan hayatındaki önemini kendine has bir üslup kullanarak açıklayabilme.",
       "b değerlendirme      Bir çocuk kitabını olması gereken özelliklere göre eleştirebilme.",
       "b değerlendirme      Kişinin gelişim düzeyine uygun bir yazıyı,makale kurallarına göre değerlendirmesi.",
       "b değerlendirme      Bir tartışmadaki mantıksal yazıları ortaya koyabilme.",
       "b değerlendirme      İyi bir sınavda bulunması gereken temel ilkeleri tartışabilme.",
       "d alma olgusu        Bir sergideki resimlere dikkatle bakmak.",
       "d alma olgusu        Toplumsal sorunlara duyarlılık göstermek.",
       "d alma olgusu        Trafik kurallarına uymanın farkında olma.",
       "d alma olgusu        Eğitimle ilgili yayınları seçmede dikkatli davranma.",
       "d olguya cevap       Bir sanat eseri ile ilgili tartışmaya katılma.",
       "d olguya cevap       Okul ve trafik kurallarına uyma. ",
       "d olguya cevap       Toplumsal kuruluşlarda çalışmaya gönüllü olma.",
       "d olguya cevap       Boş zamanlarında kitap okumaktan zevk alma. Verilen bir görevi itiraz etmeden gereğine uygun olarak yapma.",
       "d değerlendirme      Etkili konuşma ve yazma yeteneğini geliştirmeye sürekli istek gösterme.",
       "d değerlendirme      Demokratik hayatın önemini takdir etme.",
       "d değerlendirme      'Yurtta sulh, dünyada sulh' ilkesini takdir etme.",
       "d değerlendirme      Vatanın ve milletin bölünmez bütünlüğünü korumaya kendini adama.",
       "d organizasyon       Bir takım mesleki sorunların giderilmesi için yeni değerler oluşturmaya kararlılık. ",
       "d organizasyon       Bir sanat dergisine abone olma.",
       "d organizasyon       Problem çözmede planlamanın rolünü benimseme.",
       "d organizasyon       Beğendiği bir sanat eserinin özelliklerini yakından tanımaya çalışma.",
       "d karakterize etme   Arkadaşları arasında bir sanat aşığı olarak tanınma.",
       "d karakterize etme   Grup etkinliklerinde işbirliğine uyum sağlama.",
       "d karakterize etme   Kanunlara karşı sorumlu olmayı alışkanlık haline getirme",
       "d karakterize etme   Kanıtlar karşısında, yargılarını ve davranışlarını değiştirmeye alışık olma.Çevresinde yardım sever kişiliği ile tanınma.",
       "p algı               Çalışmakta olan bir makinenin sesinden, çalışma güçlüklerini tanıma.",
       "p algı               Dikiş yapmaya başlamadan, iğnenin dikiş makinesinin neresine takılacağını fark etme.",
       "p algı               Müziği dans biçimine bağlama yeteneği.",
       "p algı               Beden eğitimi dersinde yapılan vücut hareketlerini gözleyebilme.",
       "p yerleştirme        Yemek yapmada belirli bir tarifeyi takip etme.",
       "p yerleştirme        Penaltı atışında kalecinin uygun pozisyona geçmesi.",
       "p yerleştirme        Klavyede on parmak yazı yazmak için elleri hazır pozisyona getirme.",
       "p yerleştirme        Araba kullanmak için uygun biçimde koltuğa oturma.",
       "p güdümlü yanıt      Bilgisayarla, öğretmen denetiminde bir konu ile ilgili sunu hazırlama.",
       "p güdümlü yanıt      Öğretmen denetiminde öğrencilerin portre çalışması yapması.",
       "p güdümlü yanıt      Bir dansın adımlarını usta sanatçıya bakarak yapmaya çalışma.",
       "p güdümlü yanıt      En iyi pantolon ütüleme yöntemini, çeşitli yollar deneyerek bulma.",
       "p mekanizma          Düzgün ve okunaklı bir yazı yazma becerisi gösterme.",
       "p mekanizma          Bir elbise desenini, bir kumaşa uygulayarak, elbise kesme.",
       "p mekanizma          İstenilen nitelikte bilgisayar masası yapabilme.",
       "p mekanizma          On parmakla daktiloda yardımsız yazı yazabilme.",
       "p karmaşık açık      Word programını kullanan birinin Excel programını da kullanması.",
       "p karmaşık açık      Suyun akış biçimine göre yüzme stilini değiştirme.",
       "p karmaşık açık      Bir müzik aletini çalmak için kazandığı becerilerle, diğer müzik aletlerini çalabilme.",
       "p karmaşık açık      Basketbol oyununda kazandığı becerileri, hentbol oynarken rahatça kullanabilme.",
       "p icat               Yeni bir dans figürü ortaya koyabilme.",
       "p icat               Farklı biçimde bir masa yapabilme.",
       "p icat               Orijinal bir resim yapabilme.",
       "p icat               Yeni bir topa vuruş tekniği geliştirme.",
       "i Öğrenciye Uygunluk     **Okul öncesinde düz anlatım yöntemi nadiren kullanılırken, oyun etkinlikleri çok sık kullanılır.",
       "i Yaşama yakınlık       **Eğitim fakültelerinde öğretmen adaylarına materyal tasarlama becerisinin öğretilmesi..",
       "i Somuttan soyuta       **Toplama işlemi öğreten öğretmenin önce renkli sayı fasülyelerini sonra rakamları kullanması.",
       "i Etkin Katılım         **Öğrenciler yakın çevredeki ağaç türlerini inceledikten sonra sınıfta bir gözlem raporu yazar.Sonrasında ekip çalışmasıyla raporları analiz eder,\n üzerinde tartışır ve değerlendirme yapar.",
       "i Açıklık               ** Öğretmenin Çanakkale savaşı konusunu anlaşılır bir üslupla anlatırken, fotoğraflar göstererek örnek vermesi…",
       "i Ekonomiklik           **Halka açık yerlerde hizmet alırken sıraya geçmenin önemini işleyen öğretmenin drama yöntemi kullanarak para harcamadan \nkısa sürede öğrencilerine hem bilgi hem beceri hemde tutum kazandırması.",
       "i Güncellik             **Öğrenciler çevrede, dünyada olanlardan farkında olsun.Bilinç düzeyi yüksek olsun.Olaylardan bi haber değil haberdar olsun\nÖğretmen yazılı ve görsel medya haberlerini sınıfa taşıması.",
       "i Bilinendenbi          **Denk küme konusunu işlemeden önce küme, eleman ve eleman sayısı konularını hatırlatmak.",
       'i Yakından uzağa        **Köyde görev yapan bir sınıf öğretmeninin yaşadığımız yer isimli üniteyi “köyümüz”, “ilçemiz”, “ilimiz”, “bölgemiz”, “ülkemiz” ve “dünyamız” sırasıyla işlemesi…',
       "i Basitten karmaşığa    **Dört işlem öğretirken “toplama”, “çıkarma”, “çarpma” ve “bölme” sırasının kullanılması.\nBeden eğitimi dersinde önce düz sonra ters taklanın öğretilmesi…",
       'i Bütünlük              **“Gelişim bir bütündür” ilkesi temel alınır.Öğrenci fiziksel, zihinsel, psikolojik ve soyal açıdan bütün olarak ele alınır.\nKonular ve konulara dayalı sürdürülecek etkinlikler bir bütünlük içinde ele alınmalıdır.',
       "i Sosyallik             **Milli eğitimdeki proje ödev konularını öğretmen belirleyip sınıfa taşır.(Otoriteye İtaat)\nöğrenciler bu konular arasında istediğini seçip yapar.(Özgürlük)",
       "i Bilgi ve Becerinin Güvence Altına Alınması  **Yapılandırmacı öğrenme yaklaşımında bu ilkenin geçerliliği yoktur.Çünkü yapılandırmacılıkta bilgi öznel ve değişkendir.",
       ]
questions = []
only_ilke=False

def question_func():
    which_one = input('''           Sadece duyuşşal için "1"
           Sadece ilkeler için "2"
           Karışık için "3"\n>>>>>>>>''')

    if which_one == "1":
        while True:
            rastgele = random.choice(ilk)
            if rastgele not in questions and rastgele.startswith("d"):
                questions.append(rastgele)
            if len(questions) == 20:
                print("completed")
                break
    elif which_one == "2":
        while True:
            only_ilke=True
            rastgele = random.choice(ilk)
            if rastgele not in questions and rastgele.startswith("i"):
                questions.append(rastgele)
                if len(questions) == 13:
                    print("completed")
                    break
    elif which_one == "3":
        while True:
            rastgele = random.choice(ilk)
            if rastgele not in questions:
                questions.append(rastgele)
            if len(questions) == len(ilk):
                print("completed")
                break


question_func()

soru = 0
skor = 0
for a in questions:
    soru+=1
    if only_ilke:
        print(f"{green}{soru}/{len(questions)} {a[20:]}")
        ans = input(">")
    else:
        print(f"{green}{soru}/{len(questions)} {a[18:]}")
        ans = input(">")
    if ans in a[:18].lower():
        skor += 1
    elif ans == "1":
        skor += 1
        if a.startswith("i"):
            print(f"{blue}{a[0:24]}")
        else:
            print(f"{blue}{a[0:18]}")
    elif ans == "q":
        print(f"{blue}Doğru soru sayısı: {skor}")
        break
    else:
        if a.startswith("i"):
            print(f"{red}Hayır {a[2:25]}!")
        else:
            print(f"{red}Hayır {a[2:18]}!")
        a += "\n"
        with open('deneme.txt', "a") as f:
            f.write(a)

print(f"{blue}Doğru soru sayısı: {skor}")
