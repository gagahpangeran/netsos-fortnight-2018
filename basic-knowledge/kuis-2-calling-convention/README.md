# Kuis - 2 - Calling Convention (25 Poin)

## Link Soal

[Kuis - 2 - Calling Convention](http://152.118.201.254:8000/challenges#Kuis%20-%202%20-%20Calling%20Convention)

## Deskripsi Soal

Dalam arsitektur intel amd64, ketika kita memanggil fungsi, 6 parameter pertama tidak dipush ke stack namun dimasukkan ke register. Register apakah itu?

outputkan dalam NETSOS{A_B_C_D_E_F} dimana A,B,C,D,E,F adalah register yang menampung berturut-turut parameter ke-1,2,3,4,5,6.

## Solusi

Sama seperti solusi [Kuis 1](https://github.com/gagahpangeran/Netsos-Fortnight-2018/tree/master/tutorial/sample-flag), masih menggunakan halaman [ini](http://6.035.scripts.mit.edu/sp17/x86-64-architecture-guide.html) sebagai acuan untuk mendapatkan flag.

Di tabel paling atas terlihat jelas pembagian register untuk menampung 6 parameter tersebut. Didapatkanlah flag `NETSOS{rdi_rsi_rdx_rcx_r8_r9}` kemudian submit dan AC.
