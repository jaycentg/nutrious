# Nutrious
## Nama-Nama Anggota Kelompok
1. Stelline Claudia - 2106700933
2. Dhafin Raditya Juliawan - 2106650304
3. Johannes Setiawan - 2106750345
4. Muhammad Faris Umar Rahman - 2106702402
5. Jaycent Gunawan Ongris - 2106750231
6. Annava Wisha Sikoko - 2106635493

## Tautan Aplikasi Heroku
[Dapat diklik di sini](https://nutrious.herokuapp.com/)

## Cerita Aplikasi yang Diajukan dan Manfaatnya
Kesehatan global adalah salah satu topik yang menjadi perhatian dari berbagai pemimpin dunia. Kami sebagai mahasiswa yang aktif melihat isu terkait kesehatan ini sebagai hal yang perlu ditingkatkan demi tercapainya kualitas hidup yang lebih baik di Indonesia. Oleh karena itu, kami membuat **Nutrious**, sebuah aplikasi berbasis web yang diharapkan dapat membantu dalam meningkatkan standar nutrisi masyarakat. Aplikasi ini tidak hanya memiliki fitur yang bermanfaat untuk diri sendiri saja, seperti *calorie tracker*, tetapi juga pengguna bisa berkontribusi untuk meningkatkan standar nutrisi masyarakat lain dengan cara melakukan penggalangan dana untuk orang kelaparan dan memberikan informasi terkait pembagian makanan, jika ada makanan yang ingin dibagikan oleh pengguna. Selain itu, pengguna juga bisa membagikan resep makanan kepada orang lain dan bisa membagikan pemikirannya terkait nutrisi, gizi, serta kesehatan melalui fitur *app* blog yang kami sediakan. 

## Daftar Modul yang Diimplementasikan
1. Modul Utama (Django App: `home`)<br>
Terdiri dari halaman utama (*landing page*), *login page*, *registration page*, serta *authorization* dan *authentication* dari aplikasi. Selain itu, modul ini juga menyediakan model yang akan dijadikan sebagai *foreign key* untuk model-model lainnya pada *project*.
2. Fundraising (Django App: `donation`)<br>
Fitur bagi *user* untuk melakukan penggalangan dana. Semua *user* dapat melakukan donasi dengan memasukkan nominal uang yang akan didonasikan pada *form* yang diberikan, tetapi hanya *user* yang sudah terverifikasi saja yang boleh membuka penggalangan dana untuk mencegah *user* menyalahgunakan fitur ini. Selain itu, untuk meningkatkan keamanan, tiap penggalangan dana yang dibuka harus diverifikasi oleh *admin* terlebih dahulu sebelum *user* bisa melakukan donasi.
3. Food-Sharing (Django App: `foodsharing`)<br>
Fitur bagi *user* yang ingin membagikan makanannya kepada orang yang membutuhkan. Hanya *user* yang sudah terverifikasi saja yang dapat membagikan informasi alamat pembagian makanan untuk mencegah hal yang tidak diinginkan, tetapi semua pengakses web dapat melihat lokasi pembagian makanan yang sedang terbuka pada waktu tersebut.
4. Calorie Tracker (Django App: `calorietracker`)<br>
Fitur bagi *user* untuk mencatat *log* terkait aktivitas yang dilakukan dan berkaitan dengan penambahan atau pembakaran kalori. Semua *user* yang sudah *logged in* dapat menggunakan fitur ini. Agar fitur ini relevan, data yang disimpan pada aplikasi ini akan diperbaharui oleh *user* tiap harinya, sehingga dalam kurun waktu satu hari, semua *log* yang sudah dicatat akan terhapus secara otomatis. Hal ini berarti *user* tidak dapat melihat *log* yang dicatat untuk waktu lebih dari satu hari sebelumnya.
5. Food Recipes (Django App: `recipe`)<br>
Fitur bagi *user* untuk membagikan resep makanan sehat. Semua *user* yang sudah *logged in* dapat menggunakan fitur ini dan semua pengakses web dapat melihat resep-resep apa saja yang sudah dibagikan oleh *user*.
6. Blog (Django App: `blog`)<br>
Fitur bagi *user* untuk membagikan pemikirannya terkait nutrisi, gizi, dan kesehatan melalui blog. Semua *user* yang sudah *logged in* dapat menggunakan fitur ini dan memberikan *upvote* atau *downvote* pada *post* yang dibuat oleh *user* lain ataupun *post* yang dibuat oleh *user* itu sendiri. Sementara itu, semua pengakses web dapat melihat *post* yang dibuat oleh *user* yang *logged in*, akan tetapi tidak bisa memberikan *upvote* atau *downvote* pada *post* tersebut. *User* juga dapat mencari *post* apa yang tersedia pada aplikasi berdasarkan kata kunci yang dimasukkan oleh pembuat *post* tersebut.

## Daftar Role dan Deskripsinya
1. Unverified User<br>
*User* yang belum terverifikasi dapat melakukan donasi untuk penggalangan dana, membuat *log* terkait aktivitas yang berkaitan dengan penambahan atau pembakaran kalori, membagikan resep makanan sehat, serta membuat blog dan melakukan *upvote* atau *downvote* pada *post* tersebut. *User* yang belum terverifikasi juga dapat mengirimkan pesan kepada *admin* melalui halaman utama.
2. Verified User<br>
*User* yang sudah terverifikasi dapat membuka penggalangan dana dan membagikan informasi terkait pembagian makanan. Semua *user* yang sudah terverifikasi dapat mengakses fitur yang juga dapat diakses oleh *user* yang belum terverifikasi.
3. Admin<br>
*Admin* mempunyai tugas untuk melakukan verifikasi terhadap *user* dan penggalangan dana yang dibuat oleh *user*. *Admin* juga dapat dikirimi pesan oleh *user*.