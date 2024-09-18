# Pacil Electronic Center

Nama : Muhammad Zaid Ats Tsabit
NPM : 2306224410
Kelas : PBP D

Nama Aplikasi : Pacil Elektronic Center ( PEC )
Link : http://muhammad-zaid31-pec.pbp.cs.ui.ac.id/


## Cara membuat Aplikasi PEC STEP-by-STEP

### // Membuat sebuah proyek Django baru.
1. Setup Repo pada Github. Lalu, meng-clone repo tersebut ke dalam lokal komputer. Dengan melakukan ini, secara otomatis repo lokal akan terhubung dengan repo pada GitHub.
2. Membuat virtual environtment dan menyalakannya.
3. Setelah itu, membuat file requirements.txt pada direktori utama lokal dan lakukan installasi dependencies pada file requirements.txt

Isi file requeirements.txt:
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3

4. Langkah akhir membuat proyek Djanggo, dengan menjalankan perintah "django-admin startproject pec ." (pec nama proyeknya)

### // Membuat aplikasi dengan nama main pada proyek tersebut
5. Menjalankan "python manage.py startapp main" untuk membuat aplikasi main
 
### // Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
6. Pada folder proyek (subnama proyek), lakukan penambahan 'main' pada file settings.py di variable INSTALLED_APPS. Dengan ini, main sudah terdaftarkan pada proyek kita

### // Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
7. Memodifikasi file models.py dengan class dan atau attribut yang diinginkan. Dalam kasus ini adalah, class Produk dengan attribut name, price, dan description.
8. Langkah terakhirnya, jangan lupa melakukan migrasi model yang sudah dibuat

### // Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
9. Membuat terlebih dahulu direktori templates dengan berisi file html yang ingin ditampilkan nantinya. (konteks disini: main.html)
10. Pada aplikasi main, dalam file views.py, saya menambahkan dictionary ( pada context ) untuk menyimpan variabel yang ingin ditampilkan pada templates nanti.

### // Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
11. Melakukan routing pada file urls.py dalam direktori main, dengan menambahkan path views agar terhubung dengan context / variable yang ingin ditampilkan nantinya.
12. Melakukan konfigurasi routing pada urls proyek, hal ini dapat dilakukan dengan menambahkan path pada urls pattern sehingga urls tersebut terhubung ke tampilan main.
13. Setelah itu, konfigurasi proyek agar bisa menjalankan server. Hal ini bisa dilakukan dengan menambahkan ALLOWED_HOST pada file settings.py (localhost dan pws).

### // Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
13. Membuat Project pada PWS dan menghubungkan direktori lokal
14. Melakukan mantra git add, commit, push kepada GitHub dan PWS

Setelah melakukan hal tersebut, taraa~~ jadi deh proyeknya


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![mindmap](img/mindmap.png)

Request user akan diteruskan kepada framework Django dimana disana request akan dipetakan melalui urls.py untuk diarahkan kepada views.py yang diinginkan. Setelah diterima oleh views.py, request tersebut akan diproses dengan mengambil/menulis data pada models.py karena hal tersebut merupakan bagian dari database. Lalu, setelah mengambil/menulis data, maka views kembali memproses templates yang berisi html untuk menampilkan display yang diinginkan. Setelah semua data tersebut didapatkan, maka semua  hasil tersebut akan diteruskan dan ditampilkan pada user.


## Jelaskan fungsi git dalam pengembangan perangkat lunak!

Dalam pengembangan perangkat lunak, *pada umumnya* dilakukan oleh dua orang atau lebih sehingga dengan adanya git kita dapat melakukan kolaborasi dan kerjasama antar pengembang, tanpa harus khawatir dengan perubahan yang akan mereka buat akan saling bertabrakan, dengan cara branching. Selain itu, dengan git para pengembang juga dapat melihat riwayat atau history dari perubahan-perubahan yang ada karena dapat dilihat dari commitnya. Hal ini, tentulah sangat bermanfaat untuk tracking perubahan atau versi yang telah diubah/diupdate. Jika terjadi konflik pada perubahan pun, para pengembang bisa menyelesaikan / meresolvenya dengan mudah.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django dapat menjadi pintu masuk utama yang relatif lebih mudah dicerna karena dari segi bahasa yang digunakan aja sudah lebih enak dimengerti, yaitu python. Lalu, dengan arsitekturnya yang berbasis Model-View-Template (MVT), yang mana arsitektur ini memisahkan komponen logika aplikasi, tampilan, dan pengelolaan data sehingga akan mudah dicerna secara intuitif untuk mempelajari pengembahan perangkat lunak ini.

## Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM karena Django pakai Object-Relational Mapping buat ngehubungin antara model yang kita bikin di Python sama tabel di database. Jadi, kita bisa ngatur data di database cukup dengan kode Python aja tanpa perlu repot-repot nulis SQL manual. Dengan ORM ini, semuanya jadi lebih gampang dan enak dimengerti, terutama jika kita yang pingin fokus ke logika aplikasi tanpa pusing mikirin detail interaksi dengan database.

# TUGAS 3

## Implementasi Tugas 3

### Menyiapkan Kerangka HTML
1. Melakukan penambahan base.html pada direktori baru, yaitu templates pada root folder dan mendaftarkannya pada  Templates settings.
2. Mengubah primary key menjadi uuid pada class model agar id unik dan aman. Lalu, mengmigrasikannya.

### Membuat input form untuk menambahkan objek model pada app sebelumnya + Routing
3. Membuat file baru, forms.py, pada aplikasi atau direktori main. Lalu, mengassign model yang akan digunakan yaitu product dan field yang akan diisi pada form.

```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```

4. Pada file views.py, menambahkan fungsi baru yaitu create_product dengan isi menampilkan halaman form input data yang mana jika berhasil akan kembali ke menu utama.

5. Lalu, pada fungsi show_main pada views.py, ambil seluruh database dalam product dan menggsingnya kedalam dictionary context untuk di render.

6. Menambahkan pada direktori main/templates, create_product.html, dengan mengextend base.html isi pada halaman tersebut adalah menampilkan input form database. Lalu, menambahkan code untuk menampilkan product pada main.html.

7. Melakukan routing pada main/urls.py agar create_product.html dapat terakses.

###  Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
8.  Menambahkan fungsi pada views.py untuk dapat melihat format XML, JSON, XML by ID, dan JSON by ID

```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Pada show xml dan json, sebelum mereturn hasil data dalam bentuk xml/json, kita perlu mengambil seluruh data pada product baru menambahkannya pada parameter serialize agar diconvert kedalam bentuk xml/json. Hal ini berbeda pada by id dimana kita mengambil data hanya dengan id yang kita inginkan.

9. Melakukan routing pada main/urls.py agar kita dapat menampilkan halaman-halaman tersebut

```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
Diatas adalah bentuk akhir routing pada Tugas 3 kali ini.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Sebuah platform itu membutuhkan suatu cara untuk mengirimkan data antara server dan client. Nah sehingga dengan data delivery inilah yang memungkinkan server mengirim data ke client atau sebaliknya untuk ditampilkan/diolah. Tanpa data delivery, suatu platform akan kesulitan dalam menyamakan data ( jika terdapat perubahan atau penambahan/pengurangan ) sehingga nantinya tidak akan bisa mengupdate informasi/data secara real-time dan dapat menimbulkan kebingungan dalam segi database. Oleh karena itu, kita memerulkan data delivery dalam mengimplementasikan sebuah platform.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya pribadi, JSON lebih baik dari pada XML karena dari sintaksnya aja lebih mudah dibaca dibanding XML dan juga self describing. Dengan format dictionary,  value yang ada pada data JSON ini kita bisa mengambilnya dengan relatif lebih mudah, contohnya kita bisa memanggil keynya dalam bahasa python. Selain itu, pada umumnya juga JSON lebih sering digunakan dalam pengembahan di berbagai aplikasi.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() ini digunakan untuk memvalidasi data yang diinput oleh user, dengan method ini kita dapat memastikan bahwa data yang diinput telah sesuai, misal field sudah terisi semua, tipe data yang sesuai, dan batas panjang yang sesuai. Jika valid, method ini mengembalikan nilai True dan data dapat disimpan atau diproses. Validasi ini tentunya sangatlah penting agar data yang diterima sesuai dengan apa yang kita harapkan dan tentunya dapat mencegah kesalahan atau bahkan keamanan suatu aplikasi, terutama bagian datanya.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan csrf_token untuk melindungi aplikasi dari serangan Cross-Site Request Forgery ( CSRF ), di mana penyerang bisa menyamar sebagai user yang valid, lalu mengirimkan sebuah request "sah" yang berbahaya tanpa sepengatahuan user. Request ini bisa dimanfaatkan oleh penyerang untuk mengobrak-abrik data pengguna, bahkan dapat merugikan pengguna secara langsung jika terkait dengan form transaksi.

## hasil akses URL pada Postman

### Show XML
![showxml](img/show_xml.png)

### Show XML by Id
![showxmlbyid](img/show_xml_by_id.png)

### Show JSON
![showjson](img/show_json.png)

### Show JSON by Id
![showjsonbyid](img/show_json_by_id.png)