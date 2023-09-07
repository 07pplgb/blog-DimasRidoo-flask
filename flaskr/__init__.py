# import aplikasi flask untuk di pakai di web kita
from flask import Flask

# mengatur nama aplikasi
app = Flask(__name__)

# mengatur URI (universal resource identifier), dan apa yang ditampilkan jika URI tersenut diakses
@app.route('/') # ketika alamat http://127.0.0.1;5000/ dipanggil, maka server akan mengeksekusi fungsi hello()
def hello(): # function dengan nama hello
    return 'Hello, World!'

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika di akses di alamat URI http://127.o.o.1:5000/login
@app.route("/login")
def login():
    return 'halaman login'  