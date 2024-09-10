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

## // Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
13. Membuat Project pada PWS dan menghubungkan direktori lokal
14. Melakukan mantra git add, commit, push kepada GitHub dan PWS

Setelah melakukan hal tersebut, taraa~~ jadi deh proyeknya


### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


### Jelaskan fungsi git dalam pengembangan perangkat lunak!

Dalam pengembangan perangkat lunak, *pada umumnya* dilakukan oleh dua orang atau lebih sehingga dengan adanya git kita dapat melakukan kolaborasi dan kerjasama antar pengembang, tanpa harus khawatir dengan perubahan yang akan mereka buat akan saling bertabrakan, dengan cara branching. Selain itu, dengan git para pengembang juga dapat melihat riwayat atau history dari perubahan-perubahan yang ada karena dapat dilihat dari commitnya. Hal ini, tentulah sangat bermanfaat untuk tracking perubahan atau versi yang telah diubah/diupdate. Jika terjadi konflik pada perubahan pun, para pengembang bisa menyelesaikan / meresolvenya dengan mudah.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django dapat menjadi pintu masuk utama yang relatif lebih mudah dicerna karena dari segi bahasa yang digunakan aja sudah lebih enak dimengerti, yaitu python. Lalu, dengan arsitekturnya yang berbasis Model-View-Template (MVT), yang mana arsitektur ini memisahkan komponen logika aplikasi, tampilan, dan pengelolaan data sehingga akan mudah dicerna secara intuitif untuk mempelajari pengembahan perangkat lunak ini.

### Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM karena Django pakai Object-Relational Mapping buat ngehubungin antara model yang kita bikin di Python sama tabel di database. Jadi, kita bisa ngatur data di database cukup dengan kode Python aja tanpa perlu repot-repot nulis SQL manual. Dengan ORM ini, semuanya jadi lebih gampang dan enak dimengerti, terutama jika kita yang pingin fokus ke logika aplikasi tanpa pusing mikirin detail interaksi dengan database.