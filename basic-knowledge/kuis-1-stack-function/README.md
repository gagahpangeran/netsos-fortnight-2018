# Kuis - 1 - Stack & Function (25 Poin)

## Link Soal

[Kuis - 1 - Stack & Function](http://152.118.201.254:8000/challenges#Kuis%20-%201%20-%20Stack%20&%20Function)

## Deskripsi Soal

outputkan NETSOS{A_B_C}

A : register di intel asm amd64 yang dipakai saat fungsi return

B : register di intel asm amd64 yang dipakai sebagai acuan variabel lokal

C : register di intel asm amd64 yang dipakai sebagai penanda top of stack

misal A = r1, B = r2, C = r3, maka flagnya adalah NETSOS{r1_r2_r3}

## Solusi

Setelah googling sana sini dan kebanyakan malah menemukan arsitektur x86, akhirnya bisa menemukan satu halaman yang (mungkin) berguna yaitu halaman [ini](http://6.035.scripts.mit.edu/sp17/x86-64-architecture-guide.html).

Pertama baca langsung dapat register saat fungsi return yaitu **rax**. Selanjutnya adalah mencari register sebagai acuan variabel lokal dan penanda top of stack. Setelah baca-baca lagi, kemudian menemukan yang namanya register rsp dan rbp. Setelah yakin kemudian coba submit flag `NETSOS{rax_rsp_rbp}` dan kemudian AC.
