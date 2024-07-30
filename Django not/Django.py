^^December 13/2019 Friday 14.00
##Simply, I have website.com also i have a blog for instance. I create an app named blog. Then I create a function inside the views.py . #
#Then I call it with urls.py . To call website.com/blog/functions or website.com/blog , i need to connect this to urls.py inside the website.(not the app)

^^ # that I created that code..

#I created a project. Then opened the terminal and hit:
pip install django
django-admin startproject pyshop .
python3 manage.py startapp products


#Products.views:
from django.http import HttpResponse
from django.shortcuts import render #ne işe yarıyo bilmiyom ama vardı.

def index(request):
	return HttpResponse('Hello World') # bir response ekledim.
#Whenever i defined a new functions inside the views, i need to connect it to app's urls.py. Inside the products app, I create a new file urls.py:
from . import views      # I ımport views file
from django.urls import path

urlpatterns = [
	path('',views.index) ##not writing index() because we just pass it as a reference. (index is the name i gave to my mainpage)
]           

##I created all these inside my products app. I need to connect it  to my site. So I return to Pyshop folder and open the urls.py:
from django.contrib import admin
from django.urls import path,include ^^^

urlpatterns=[
	path('admin/',admin.site.urls),
	path('products/',include('products.urls')) ^^^^ 
]

^^^^^#^^^^^Models^^^^^
#products(app ) içinde models.py açıyorum ve içine bir class açıyorum.
# db browser for sqlite indirdim.
class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	stock = models.IntegerField()
	image_url = models.CharField(max_length=2083)##2083 url için standart

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

# daha sonra terminale yazdım : python3 manage.py makemigrations diyorum. products
#ana settings.py dosyamı açtım. Installed alt kısmına products/apps.py içinde olan ProductsConfig isimli classı ekledim.
'products.apps.ProductsConfig'
#python3 manage.py migrate  Her modelden sonra migrate. python3 manage.py makemigrations

#products içinde admin.py açtım.
from . models import Product
admin.site.register(Product)


#admin oluşturmak için terminale yaz:
python3 manage.py createsuperuser

# sitede admin kısmına girdim. Ve kullanıcı ekle kısmının altında Add products kısmı oluştu. Buradan bir ürün ekledim ve foto linki koydum.KAydettim. Ama kayıtta orange yazmıyor.Devam et
^^Customizing Admin^^^
#tekrar admin dosyasını açtım ve ekledim:
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')                   #models icinde product classımda 4 öge var. image_url uzun olduğu için bunu depolamasın.
#ve aynı dosya içinde admin.site.register(Product) a ekleme yaptım.
admin.site.register(Product,ProductAdmin)
#Şimdi sayfayı yeniledim ve product object yerine adını koydugum orange yazıyor. Bir de strawberry ya da başka bir şey ekleyeyim.
^^ Eklediğim offerları kullanma egzersizi^^^
#admin.py içine from. models import Product yanına , Offer classı ekle.
from . models import Product, Offer
#yeni bir class ekle
class OfferAdmin(admin.Model.Admin):
	list_display = ('code','discount')
admin.site.register(Offer,OfferAdmin)  #siteye ayarını ekledim. Sitede offers diye bir yer oluşturdum. Yeni bir offer oluşturup ASLAN2020 koydum. Discount 0.1 yazdım.


^^^^TEMPLATES^^^^^^
#views.py açtım tepeye eklediö
from . models import Product
#def index(request) altına ve returndaki yeri değiştiriyorum
def index(request):
	products = Product.objects.all()                   #all yerine save, filter veya get komutları da mevcuttur.
	return render(request,'index.html',{'products':products}) # içine products object ekledim.

^^#Products app içine templates adında bir directory açtım.içine yeni bir file oluşturdum; index.html İçine ekledim;
<h1>Products</h1>
<ul>
    {% for product in products %}
        <li>{{product.name}}</li>
    {%endfor%}

</ul>

## sonra sitede products kısmına gittim ve alt alta ögelerim sıralandı. Orange ve strawberry.
#Şimdi de bunların fiyatını görmek istiyorum:
<h1>Products</h1>
<ul>
    {% for product in products %}
        <li>{{product.name}} (${{product.price}})</li>
    {%endfor%}
</ul>


^^^Bootstrap(önizleme)^^^^
# https://getbootstrap.com/docs/4.4/components/card/		sonra anasayfa /documentation kısmına gir. Aşağıda Starter Template kodunu kopyala. templates klasörüne dön ve içine base.html isimli dosya atıp kodu yapıştır.


<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>


####Body kısmında altta olan hello worldlü linei sil ve ekle:
{%block content%}
{%endblock%}

#index.html e geçtim ve en tepeye ekledim;
{%extends 'base.html'%}
#altını ise böyle yapıp indentliyorum. Bu kod dizisini block content yapıyorum.
{%block content%}
	<h1>Products</h1>
	<ul>
	    {% for product in products %}
	        <li>{{product.name}} (${{product.price}})</li>
	    {%endfor%}
	</ul>
{%endblock%}

###Şimdi products sayfamdaki orange ve strawberry yazılarını bootstrape çevireceğim:
#https://getbootstrap.com/docs/4.4/components/card/ buradan bir tane kartın kodunu kopyaladım.
#index.html dosyamın içinde block content altında h1 productsın hemen altına div.row yazdım ve tab'a bastım. şu kod oluştu: <div class="row"></div>
#ortasında entere bastım ve </div> kısmını alta altım. iki kodun arasında yazdım. div.col ve tab bastım>> <div class="col"></div>
#bunun da içinde kart oluşturmak istiyorum. içine kopyaladığım kodu yazıyorum.
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>


# sonrasında ise aşağıdaki şu kodu kesiyorum: {% for product in products %}  ve <div class="row"> altına koyuyorum. Sonra <div class="col"> satır dizisini küçültüp
# altına {%endfor%} ekliyorum. Ve en alttaki div bitişi sonrasındaki diğer gereksiz kodları siliyorum

{%extends 'base.html'%}

{%block content%}
<h1>Products</h1>
<div class="row">
    {% for product in products %}
    <div class="col">
        <div class="card" style="width: 18rem;">
            <img src="..." class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                    card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
    </div>
    {%endfor%}
</div>

{%endblock%}

## Şimdi de class=col altında img src içine {{product.image_url}}

<h5 class="card-title">{{product.name}}</h5>
<p class="card-text">${{product.price}}</p>
<a href="#" class="btn btn-primary">Add to Cart</a>


^^^^^^^^^^^^^Güncel kodlar^^^^^^^^^^3

{%extends 'base.html'%}

{%block content%}
<h1>Products</h1>
<div class="row">
    {% for product in products %}
    <div class="col">
        <div class="card" style="width: 18rem;">
            <img src="{{product.image_url}}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{product.name}}</h5>
                <p class="card-text">${{product.price}}</p>
                <a href="#" class="btn btn-primary">Add to Cart</a>
            </div>
        </div>
    </div>
    {%endfor%}
</div>

{%endblock%}

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^NAVBAR^^^^
#bootstrap sitesinde documentation-components-navbar. Kodu kopyaladım base.html(çünkü basede olmasını istiyorum) içine bodynin hemen altına yapıştırdım
<!-- As a link -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
</nav>

......3^^
#PYSHOP DİZİNİNE templates ADINDA BİR DİZİN OLUŞTURDUM. base.html i bunun içine taşıdım. Ama site bu templates dosyasını nasıl görecek? Bunun için
# settings.py açıp TEMPLATES =[] kısmına DIRS içine:
'DIRS':[os.path.join(BASE_DIR, 'templates')]
##Son olarak padding için, ürünlerimi hizalayacağım. Bunun için base.html içinde {%block content%} in tam üstüne bir div classs açıp blockcontent
#endblock'u içine alıyorum
<div class="container">
{%block content%}
{%endblock%}
</div>

