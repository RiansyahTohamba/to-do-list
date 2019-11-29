# 1806280520-practice

Muh Riansyah T  - 1806280520 - MIK 2018 - PMPL B - Practice Repo

my homepage url is https://riansyah-pmpl.herokuapp.com/

# Cerita Exercise 3
Seksi ini akan menceritakan proses test isolation pada exercise 3

## Proses Test Isolation
Test Isolasi menjamin tiap test tidak saling mempengaruhi satu sama lain test. Dengan test isolasi, tiap state harus dibersihkan ketika test sudah selesai dilakukan. State yang dibersihkan setiap test pada exercise 3 adalah data "to-do" yang ada pada database. 
Pada exercise 3 terdapat kode "LiveServerTestCase" yang membantu dalam pembuatan database test dan menghapus database test jika test telah dilakukan.


# Exercise Bab 7 : keterhubungan perubahan kode dengan materi Bab 7
pada commit '[testinggoat/ch7 802ba19] tidak meng-import bootstrap sehingga posisi konten tidak tengah lagi dan FT gagal'
Bootstrap tidak di-import oleh programmer,sehingga class 'text-center' yang  dipasang pada beberapa element 'div'  tidak berfungsi. Sementara pada FT kita menetapkan bahwa beberapa element 'div' berada di tengah layar.
Untuk memenuhi FT, maka bootstrap nya harus di-import. 

Materi bab 7 mengajarkan kita bahwa test layout dan style bukan dimaksudkan untuk menguji nilai dari atribute CSS yang kita tetapkan, seperti menguji warna atau dimana letak pastinya suatu element html. Test layout dan style ditujukan untuk memastikan apakah file CSS yang telah kita buat sudah ter-upload atau belum.

Hubungan dengan perubahan import bootstrap dengan materi bab 7 adalah kita men-simulasikan jika bootstrap belum terupload. Hasilnya, melalui FT, programmer bisa mengetahui apakah bootstrap telah terupload dengan benar atau belum. 


# Perbedaan antara Manual Mocking dan menggunakan Mock library 
Pada chapter 19, Manual Mocking dilakukan dengan meng-override method yang sudah dibuat oleh django dengan scope tertentu. Sedangkan dengan Mock Library, kita tinggal menggunakan method patch dari library untuk membuat mock pada kelas yang ingin kita mock


# Perbedaan Functional Test pada ch. 20.1 vs ch. 18.3
Functional Test pada ch. 20.1 sudah menggunakan pre-creating session dengan menggunakan .Selain itu, pada ch.20 juga sudah menggunakan cookie. Sehingga saat menjalankan FT, user tidak perlu authentifikasi lagi. Pada ch. 18.3 adalah masih belum menggunakan pre-creating session dan cookie sehingga kita harus melalui proses auth. tiap kali menjalankan FT.

## Mengapa implementasi Functional Test untuk fitur login lebih baik menggunakan implementasi subbab 20.1 dibandingkan 18.3?
Pada ch. 20, user tidak perlu melalui proses auth. lagi sehingga proses FT menjadi lebih cepat.