# Cascading Style Sheets (75 Poin)

## Link Soal

[Cascading Style Sheetst](http://152.118.201.254:8000/challenges#Cascading%20Style%20Sheets)

## Files

[hello.html](https://github.com/gagahpangeran/Netsos-Fortnight-2018/tree/master/misc/cascading-style-sheets/files/hello.html)

## Deskripsi Soal

To view, or to inspect? That is the question.

## Solusi

Setelah membuka file nya ternyata gue langsung dapat flag nya karena waktu itu firefox gue mengaktifkan darkmode :v

![Dark Mode](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/cascading-style-sheets/img/css.png?token=AEvCeWZMdYqhC7cpmax1G-6Ww2bNhyUIks5cDIwDwA%3D%3D)

Oke, gimana solusi benarnya kalo kalian gak ada dark mode di browser?

Pertama inspect element di halaman tersebut. Kemudian di dalam div _greeting_ terdapat div lagi tanpa nama class. Kemudian di dalam div tersebut terdapat banyak tag span yang di dalamnya terdapat flag. Jika kalian perhatikan di bagian style terdapat banyak _pseudo_ element yang dibuat oleh css tersebut yang merupakan flag.

Karena tidak ingin lelah mengambil potongan flag ini satu per satu, kita kembali ke div tanpa nama class tadi. Ternyata warna text dari text tersebut adalah `#fdfdfd` atau warna hampir putih sehingga teks nya tidak akan terlihat karena backgroudn nya juga putih. Maka kita tinggal edit saja menjadi hitam (atau kalau gue lebih suka ngetik `#000`). Kemudian warna teks pun menjadi hitam dan didapatkanlah flag `NETSOS{C5S_is_cool_bro!}`
