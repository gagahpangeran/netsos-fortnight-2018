# I was once safe (75 Poin)

## Link Soal

[I was once safe](http://152.118.201.254:8000/challenges#I%20was%20once%20safe)

## Files

[app.py](https://github.com/gagahpangeran/Netsos-Fortnight-2018/tree/master/misc/i-was-once-safe/files/app.py)

## Deskripsi Soal

Hey look I found this old program form the 90s! Would you take a look?

Connect with: `nc 152.118.201.254 8103`

## Solusi

Pertama yang harus dilakukan tentu saja membuka file app.py yang sudah diberikan lalu menganalilisnya. Program tersebut merupakan program login yang jika kita berhasil menebak username dan password nya maka akan mendapatkan flag.

Pertama yang harus dilihat adalah bagian ini

```python
users = {
    'm_delima': {
        'hashed_password': "42b1f9f860e2be044fa45b82a361f235",
        'is_admin': True,
    },
}
```

Terlihat bahwa username yang tersedia untuk login adalah `m_delima`, lalu apa passwordnya?

Kalau diperhatikan saat memasukkan password, maka password akan di _hash_ dengan fungsi `hash_password`

```python
def hash_password(password):
    """Hashes a string with md5 and returns the hex of the hash."""
    hashed = hashlib.md5()
    hashed.update(password.encode())
    return hashed.hexdigest()
```

Dari fungsi tersebut dapat ditarik kesimpulan bahwa password yang akan dimasukkan akan di hash dengan md5. Karena md5 ini sangat mudah di decrypt maka gue hanya tinggal mencari plain text dari password yang sudah di hash.

Ternyata untuk mencari website decrypt md5 cukup mudah, gue menemukan [md5online](https://www.md5online.org/md5-decrypt.html). Kemudian hash password yang ada di program tadi gue masukkan dan didapatkanlah password `it is not safe`.

![MD5 decrypt](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/i-was-once-safe/img/md5.png?token=AEvCeexnnkWY2_DLNS-BHPFaBsCVPofYks5cDJblwA%3D%3D)

Selanjutnya hanya tinggal mengeksekusi program dan didaparkanlah flag `NETSOS{d0nt_h4sH_pA5sWoRDz_w1tH_md5_it_is_no_longer_safe}`.

![Get Flag](https://raw.githubusercontent.com/gagahpangeran/Netsos-Fortnight-2018/master/misc/i-was-once-safe/img/app.png?token=AEvCebKeQEQY4sZgx6KFIj8LDVotsw5eks5cDJcSwA%3D%3D)
