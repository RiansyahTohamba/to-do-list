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


