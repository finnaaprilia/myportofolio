Nama : Finna Aprilia

NPM : 2506538110

Kelas : PBP E


# Portofolio Web App

- Frontend: HTML5, CSS


## Tugas 1

Tugas 1 : Membuat section baru pada website mengenai Education. Section ini berisi 3 item konten, yakni latar belakang pendidikan yang mencakup jenjang S1 (yang saat ini sedang ditempuh), jenjang SMA, hingga SMP.

``` Pertanyaan Reflektif ```

1. Bagaimana elemen semantik HTML5 membantu dalam membuat static web?

— Iya, saya menggunakan elemen semantik HTML5 tetapi hanya 'section' saja, tidak mencakup 'article' ataupun 'aside'. Dalam pembuatan static web, elemen 'section' akan menjadi cara kode untuk membagi kode ke dalam kelompok-kelompok dengan tema nya masing-masing. Dalam Tugas 1 ini, saya menambahkan elemen 'section' baru untuk membuat kode terkait latar belakang pendidikan saya. Ini saya bedakan dari 'section' sebelumnya dari Tutorial 1 yang isinya mencakup identitas nama, NPM, nama jurusan, nama instansi terkait, media sosial, serta profile photo.

2. Saat mengatur CSS agar tetap responsive, tantangan tata letak apa yang ditemukan?

— Saya pada awalnya menggunakan padding-left agar section baru ini tetap berada di kiri. Namun ternyata, penggunaan padding-left ini menyebabkan section terus menempel di kiri secara permanen ("terkunci"), sehingga tidak interaktif ketika layar kecilkan.

— Mengenai bagaimana cara mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile, itu dilihat berdasarkan prioritas kontennya. Judul section yakni "Education" serta elemen semi-pendukung yaitu nama instansi, harus dapat terbaca jelas dan karena akan menjadi hal yang dilihat pertama. Selanjutnya, elemen pendukung seperti nama fakultas jurusan menggunakan padding-left 1rem (ukurannya kecil saja) hanya sebagai indentasi tipis.

3. Website yang dibuat saat ini adalah static web murni. Batasan apa yang dirasakan saat mencoba menyajikan informasi pada portofolio secara optimal?

— Dalam hal skalabilitas, semakin banyak konten yang dimasukkan dalam website portofolio, struktur file index.html semakin panjang dan cenderung repetitif. Fungsionalitas dinamis yang ingin dipersiapkan dan ditambahkan pada iterasi proyek berikutnya ialah penggunaan Django Template. Dengan adanya Django ini, ketika ingin menambah konten baru, cukup disimpan dalam database. Dan nanti melalui html dengan template Django tadi cukup dilakukan pemanggilan. Konten disimpan dalam database.


``` Dokumentasi & AI Disclosure ```

Untuk pengerjaan Tugas 1 ini, saya dibantu dengan Gemini dengan pertanyaan seputar:

1. Berikan penjelasan mengenai elemen 'dl', 'dd', dan 'dt' yang ada pada html.

— Pertanyaan ini digunakan untuk membantu saya dalam pembuatan section baru di file html dimana riwayat pendidikan berada dalam ketiga elemen tersebut.

2. Bagaimana cara membuat teks dengan indentasi di html?

— Pertanyaan ini saya gunakan untuk membuat indentasi pada nama Fakultas di bagian riwayat pendidikan S1 dan nama jurusan di bagian riwayat pendidikan Sekolah Menengah Atas (SMA). Bagian ini sebagai detail pada latar belakang pendidikan sehingga posisinya tidak saya sejajarkan dengan nama instansi terakit (saya buat lebih menjuru ke dalam).

3. Apakah padding-left menjadikan konten selalu terkunci di bagian kiri tanpa bisa menjadi interaktif mengikuti ukuran layar?

— Saya cukup kesulitan dan belum tahu bagaimana caranya agar posisi konten bisa mengikuti dan menyesuaikan dengan sendirinya ketika layar diperlebar maupun diperkecil. Ternyata, saya bisa menggunakan container yang sudah tersedia untuk section sebelumnya. Dan menggunakan padding-left yang berukuran kaku (dan dengan ukuran yang juga cukup besar seperti 5rem) itu tidak perlu.


## Tugas 2

Tugas 2 : Implementasi Model-View-Template (MVT) pada Django

``` Pertanyaan Reflektif ```

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

— ketika pengguna membuka halaman portofolio baru, browser akan mengirimkan permintaan (HTTP request) ke server Django.

— Django menerima HTTP request dan mengecek berkas urls.py di direktori proyek. Django mencocokkan awalan URL dan mengarahkan ke urls.py dengan direktori aplikasi yang sesuai, dengan fungsi include().

* keterangan:  urls.py proyek berada dalam direktori proyek portofolio dan urls.py aplikasi berada dalam direktori aplikasi main. URLs akan menjadi memetakan antara URL path expressions dan Python functions (views).

— Pada urls.py aplikasi, Django mencari pola URL yang sama dengan yang diminta.

— urls.py akan memanggil kelas View. Django views sendiri bertugas untuk mengambil permintaan HTTP dan mengembalikan respons HTTP. Fungsi ini terletak pada file views.py. Setelah menerima permintaan, views akan mengecek database, lalu meminta Model untuk mengambil data.

— Model memungkinkan kita untuk bekerja dengan data, tanpa harus mengubah atau mengunggah file dalam prosesnya. Model menjembatani kode Python dengan database, dan akan mengembalikannya ke View.

— View mengambil data dari Model, lalu memasukannya ke dalam dictionary context. View lalu memenggil berkas template HTML yang sesuai dan me-render template tersebut bersama data konteks yang telah disiapkan.

— Django menerjemahkan gabungan Template HTML menjadi berkas HTTML murni dan akan dikembalikan ke browser pengguna.


2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi. 

— Data untuk bagian portofolio baru sebaiknya disimpan pada model, supaya tidak membuat kode menjadi semakin panjang dan rumit. Data baru yang dimasukkan ke dalam model artinya data tersebut disimpan dalam database, bukan di file HTML langsung. Hal ini akan memudahkan dalam pemeliharaan (karena kode menjadi tidak terlalu complicated secara struktur) dan dalam pengembangan (karena tinggal menambahkan input data tanpa harus menambah kode secara langsung di html).

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

— Fungsi makemigrations bertanggung jawab atas pembuatan migrasi yang baru berdasarkan perubahan yang telah dilakukan. Sementara fungsi migrate bertanggung jawab untuk memutuskan apakah akan memberlakukan atau tidak memberlakukan perpindahan. Contoh perubahan model, misal perubahan nama model. Ini adalah perubahan yang telah dilakukan sebelumnya, dimana terdapat perubahan nama model dari "Hobby" menjadi "Interest" (hal ini sekaligus merubah field category yang ada di dalamnya).


``` Dokumentasi & AI Disclosure ```

Untuk pengerjaan Tugas 2 ini, saya dibantu dengan Gemini dengan pertanyaan seputar:

1. Bagaimana cara membuat agar ketiga box yang ada dalam section Education bisa berjejer ke samping? Bukan menurun ke bawah?

— Jadi, di proyek Tugas 2 ini, juga dilakukan perbaikan dan pembetulan tampilan design dari halaman Profile. Pada awalnya, di section Education, hanya menampilkan tulisan institusi dimana saya menempuh pendidikan. Tapi disini, ditambahkan foto / gambar dari intitusi terkait dan ditambahkan efek, agar ketika kursor mengarah ke foto tersebut, maka akan ada efek blur pada gambar sekaligus memunculkan nama institusinya.

— Di salah satu bagian kode yang ada pada file style.css yang didapat dari tutorial sebelumnya, terdapat kelas container yang memiliki fungsinya masing-masing. Pada dasarnya, dalam dunia web design, kelas container adalah kelas yang digunakan untuk mengatur tata letak elemen dalam halaman web. Class ini dipakai untuk membuat kotak atau wadah (container) di dalam halaman web yang berisi elemen lain, seperti teks, gambar, dan video. Class container biasanya digunakan sebagai salah satu cara untuk membuat tata letak yang responsif pada halaman web, sehingga elemen-elemen di dalamnya dapat menyesuaikan dengan ukuran layar yang berbeda.

(1) Container Utama sebagai Pembatas Lebar Halaman

.container {
    max-width: 960px;  ---> membatasi lebar maksimal konten agar tidak melebar memenuhi seluruh layar monitor
    margin: 0 auto;    ---> membuat kotak kontainer otomatis berada di tengah-tengah layar (center-aligned)
    padding: 0 1.5rem; ---> memberikan jarak di sisi kiri dan kanan agar konten tidak menempel langsung ke pinggir layar saat dibuka di HP
}

(2) Pengatur Tata Letak Header
.site-header .container {
    display: flex;      ---> mengaktifkan mode Flexbox (membuat header Nama dan Navigation Bar berjejer ke samping)
    justify-content: space-between;   ---> mendorong header Nama ke ujung paling kiri, dan Navigation Bar ke ujung paling kanan. Ruang kosong di antaranya akan dibagi otomatis.
    align-items: center;    ---> membuat header nama dan Navigation Bar sejajar secara vertikal (lurus di tengah-tengah tinggi header, tidak ada yang terlalu ke atas atau ke bawah)
    padding: 1.25rem 1.5rem;   ---> mengatur jarak dalam (atas-bawah 1.25rem dan kiri-kanan 1.5rem) agar header memiliki ruang.
}

(3) Mengatur Baris Item
.edu-container {
    display: flex;  ---> mengaktifkan mode Flexbox (membuat box berjejer ke samping)
    flex-wrap: wrap; ---> membuat box otomatis menurun ke bawah (wrap) jika layar diperkecil
    gap: 1.5rem;     ---> memberi jarak antar kotak sejauh 1.5rem
}

---> Class container (3) yang digunakan untuk membuat box pada section Education berjejer ke samping.

2. Jika ada perubahan pada model yang telah dibuat, apakah jika mengganti nama model sekaligus mengganti field yang ada di dalamnya maka harus melakukan migrasi lagi? Mengapa?

— Jika ada perubahan, maka harus dilakukan migrasi lagi. Tujuannya, untuk sinkronisasi antara struktur kode python (model) dengan basis data (database). Apabila tidak menjalankan proses migrasi, akan terjadi error akibat ketidaksesuaian (mismatch) antara kode Python dengan struktur database yang asli.


``` Referensi ```
(1) https://docs.djangoproject.com/

(2) https://www.w3schools.com/django/

(3) https://id.linkedin.com/pulse/ini-dia-mengapa-class-container-sangat-penting-dalam-desain-afifudin
