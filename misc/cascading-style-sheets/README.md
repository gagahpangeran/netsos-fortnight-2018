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

![Tanpa Dark Mode](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/cascading-style-sheets/img/css2.png?token=AEvCeXe4R-ZgQoZ3WoXVVfBLD0vIHt1Tks5cDJBQwA%3D%3D)

Pertama inspect element di halaman tersebut. Kemudian di dalam div _greeting_ terdapat div lagi tanpa nama class. Kemudian di dalam div tersebut terdapat banyak tag span yang di dalamnya terdapat flag.

![Greeting div](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/cascading-style-sheets/img/css3.png?token=AEvCeRXSGhLHOm0O13qzyCxkqMv9DbKFks5cDJCTwA%3D%3D)

Jika kalian perhatikan di bagian style terdapat banyak _pseudo_ element yang dibuat oleh css tersebut yang merupakan flag.

![Style](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/cascading-style-sheets/img/css4.png?token=AEvCeUYICpjxR0_N6Om1w2AC0kex31tPks5cDJC6wA%3D%3D)

Karena tidak ingin lelah mengambil potongan flag ini satu per satu, kita kembali ke div tanpa nama class tadi. Ternyata warna text dari text tersebut adalah `#fdfdfd` atau warna hampir putih sehingga teks nya tidak akan terlihat karena background nya juga putih.

![Color text](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/cascading-style-sheets/img/css5.png?token=AEvCeewqWkUN-aL3Ng6kUh0SAivLBOOfks5cDJDUwA%3D%3D)

Maka kita tinggal edit saja menjadi hitam (atau kalau gue lebih suka ngetik `#000`). Kemudian warna teks pun menjadi hitam dan didapatkanlah flag `NETSOS{C5S_is_cool_bro!}`

![Get Flag](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/cascading-style-sheets/img/css6.png?token=AEvCee9j17GbVsJx0y3DW8NU0_DbwnNxks5cDJDzwA%3D%3D)
