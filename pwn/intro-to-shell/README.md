# Intro to Shell (25 Poin)

## Link Soal

[Intro to Shell](http://152.118.201.254:8000/challenges#Intro%20to%20Shell)

## Deskripsi Soal

Halo, jadi ini adalah dasar buanggetttt dari binary exploitation. Kamu akan diberi sebuah shell. Gunakan command line dari shell untuk membaca file. silakan baca2 di sini : https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners

nc 152.118.201.254 8001

## Solusi

Jadi soal ini _straightforward_ aja langung nc ke server yg dimaksud, karena menurut soal ini kayak shell biasa, gue coba apakah command bash bisa dilakukan. Ternyata bisa dan didapatkanlah list file yang ada.

Terlihat ada file flag.txt, yaudah langsung aja cat file tersebut dan dapat flag `FORTNIGHT{in_the_future_we_will_hunting_this}`
