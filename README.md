# pec


NOTES: Cara saya membuat Aplikasi PEC
STEP-STEP Buat Aplikasi Djanggo
1. Membuat Repo baru untuk aplikasi yang ingin dibuat pada akun Github. (dengan centang README.md)
2. Buatlah folder aplikasi pada direktori lokal. Contoh folder pec (utama)
3. Lalu clone repo tersebut ke dalam direktori lokal agar kita dapat mengerjakannya secara lokal (akan berisi README.md)
4. Bukalah terminal pada folder pec (utama). Lalu, membuat virtual environment dengan "python -m venv env".
5. Jalankan/nyalakan virtual environtment dengan "env\Scripts\activate", maka akan terlihat tanda (env) pada terminal.
Tujuan env:
    Agar kita dapat mengisolasi dependencies ( komponen/modul yang diperlukan, seperti library, framework, atau package ) proyek yang kita kerjakan dari sistem dan proyek lain yang ada di komputer kita. Hal ini dapat membantu menghindari konflik antara versi library yang berbeda
6. Pada direktori pec (utama), kita buat file requirements.txt, yang berisi dependencies:

django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3

7. Lakukan Instalasi dependencies pada file requirements, dengan perintah "pip install -r requirements.txt"
8. Langkah akhir membuat proyek Djanggo, kita bisa menjalankan perintah "django-admin startproject pec ."
Setelah Langkah 8, maka akan terbuat subdirektori pec dengan file-file yang akan kita gunakan (__init__, settings, asgi, urls, dan sebagainya) dan manage.py

x