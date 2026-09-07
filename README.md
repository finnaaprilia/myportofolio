Nama : Finna Aprilia

NPM : 2506538110

Kelas : PBP E


# Portofolio Web App

- Frontend: HTML5, CSS

Tugas 1 : membuat section baru pada website mengenai Education. Section ini berisi 3 item konten, yakni latar belakang pendidikan yang mencakup jenjang S1 (yang saat ini sedang ditempuh), jenjang SMA, hingga SMP.

### Tugas 1

``` Pertanyaan Reflektif ```

1. Bagaimana elemen semantik HTML5 membantu dalam membuat static web?
Iya, saya menggunakan elemen semantik HTML5 tetapi hanya <section> saja, tidak mencakup <article> ataupun <aside>. Dalam pembuatan static web, elemen <section> akan menjadi cara kode untuk membagi kode ke dalam kelompok-kelompok dengan tema nya masing-masing. Dalam Tugas 1 ini, saya menambahkan elemen <section> baru untuk membuat kode terkait latar belakang pendidikan saya. Ini saya bedakan dari <section> sebelumnya dari Tutorial 1 yang isinya mencakup identitas nama, NPM, nama jurusan, nama instansi terkait, media sosial, serta profile photo.

2. Saat mengatur CSS agar tetap responsive, tantangan tata letak apa yang ditemukan?
Saya pada awalnya menggunakan padding-left agar section baru ini tetap berada di kiri. Namun ternyata, penggunaan padding-left ini menyebabkan section terus menempel di kiri secara permanen ("terkunci"), sehingga tidak interaktif ketika layar kecilkan.

Mengenai bagaimana cara mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile, itu dilihat berdasarkan prioritas kontennya. Judul section yakni "Education" serta elemen semi-pendukung yaitu nama instansi, harus dapat terbaca jelas dan karena akan menjadi hal yang dilihat pertama. Selanjutnya, elemen pendukung seperti nama fakultas jurusan menggunakan padding-left 1rem (ukurannya kecil saja) hanya sebagai indentasi tipis.

3. Website yang dibuat saat ini adalah static web murni. Batasan apa yang dirasakan saat mencoba menyajikan informasi pada portofolio secara optimal?
Dalam hal skalabilitas, semakin banyak konten yang dimasukkan dalam website portofolio, struktur file index.html semakin panjang dan cenderung repetitif. Fungsionalitas dinamis yang ingin dipersiapkan dan ditambahkan pada iterasi proyek berikutnya ialah penggunaan Django Template. Dengan adanya Django ini, ketika ingin menambah konten baru, cukup disimpan dalam database. Dan nanti melalui html dengan template Django tadi cukup dilakukan pemanggilan. Konten disimpan dalam database.


``` Dokumentasi & AI Disclosure ```

Untuk pengerjaan Tugas 1 ini, saya dibantu dengan Gemini dengan pertanyaan seputar:

1. Berikan penjelasan mengenai elemen <dl>, <dd>, dan <dt> yang ada pada html
Pertanyaan ini digunakan untuk membantu saya dalam pembuatan section baru di file html dimana riwayat pendidikan berada dalam ketiga elemen tersebut.

2. Bagaimana cara membuat teks dengan indentasi di html?
Pertanyaan ini saya gunakan untuk membuat indentasi pada nama Fakultas di bagian riwayat pendidikan S1 dan nama jurusan di bagian riwayat pendidikan Sekolah Menengah Atas (SMA). Bagian ini sebagai detail pada latar belakang pendidikan sehingga posisinya tidak saya sejajarkan dengan nama instansi terakit (saya buat lebih menjuru ke dalam).

3. Apakah padding-left menjadikan konten selalu terkunci di bagian kiri tanpa bisa menjadi interaktif mengikuti ukuran layar?
Saya cukup kesulitan dan belum tahu bagaimana caranya agar posisi konten bisa mengikuti dan menyesuaikan dengan sendirinya ketika layar diperlebar maupun diperkecil. Ternyata, saya bisa menggunakan container yang sudah tersedia untuk section sebelumnya. Dan menggunakan padding-left yang berukuran kaku (dan dengan ukuran yang juga cukup besar seperti 5rem) itu tidak perlu.
