# Slash-Slash (50 Poin)

## Link Soal

[Slash-Slash](http://152.118.201.254:8000/challenges#Slash-Slash)

## Deskripsi Soal

Format: `/NETSOS{\D+\d+[F-P]+[^A-Z]+\d{3}_(wepe|jelek)}/`

## Solusi

Terlihat jelas dari deskripsi soalnya kita disuruh submit flag sesuai dengan format regex tersebut. Karena gue gak terlalu hafal gimana cara kerja format regex, akhirnya gue coba nyari string yang match lewat https://regexr.com/.

Oke, gue akan membagi perbagian apa yang harus dilakukan dengan _regex_ ini.

- `NETSOS{`
  Jadi di bagian ini biasa aja, emang string yang dimasukkan harus sama dengan yang diinginkan yaitu 'NETSOS{'.

- `\D`
  Ini kalo menurut penjelasan di regexr adalah _not digit_, jadi langsung aja gue tambahin 'a'.

- `\d`
  Kalo yang ini _digit_, langsung tambah lagi '0'.

- `[F-P]`
  Ini namanya _character set_, jadi harus match dengan karakter apapun yang ada di dalam situ, nambah lagi 'F'.

- `[^A-Z]`
  Ini _negated set_, mirip kayak _character set_ tapi bedanya gak boleh ada karakter yg terdapat di dalam situ, tambahin aja 'a'.

- `\d{3}`
  Ini juga _digit_ cuma bedanya harus ada 3 karakter, jadi nambahin '012'.

- `_`
  Ini match biasa harus nambah karakter '\_'.

- `(wepe|jelek)`
  Kalo kata regexr ini namanya _capturing group_, jadi harus nambahin antara 'wepe' atau 'jelek'. Karena gue kasihan sama FwP, jadinya gue tambahin 'wepe'

- `}`
  Ya sama kayak sebelumnya, cuma match karakter '}' doang.

Kemudian jadilah string `NETSOS{a0Fa012_wepe}` dan ternyata match saat dicek, langsung aja submit dan AC :)
