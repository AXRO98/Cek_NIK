"""
[=======================================================================]
 Copyright (C) 2023 axroc98. Seluruh hak cipta dilindungi undang-undang.
[=======================================================================]
 Pesan ini dimaksudkan untuk melindungi hak cipta karya yang terdapat dalam dokumen ini.
 Semua materi dalam dokumen ini, termasuk tetapi tidak terbatas pada teks, gambar, grafik, audio, video, dan materi lainnya, adalah milik eksklusif axroc98 kecuali dinyatakan sebaliknya.
 Tidak diizinkan untuk menggandakan atau mendistribusikan keseluruhan atau sebagian konten dalam dokumen ini tanpa izin dari axroc98.
 Dilarang keras melakukan modifikasi, reproduksi, atau mempublikasikan ulang konten ini tanpa izin tertulis dari pemilik hak cipta. 
 Pelanggaran tersebut merupakan tindakan yang melanggar hak-hak eksklusif dan dapat dikenai tindakan hukum sesuai dengan peraturan yang berlaku.
 axroc98 berhak mengambil langkah-langkah yang diperlukan untuk melindungi hak cipta dan kekayaan intelektualnya.
 Penggunaan merek dagang atau merek layanan yang terlihat dalam dokumen ini tidak mengimplikasikan adanya dukungan atau hubungan apapun antara axroc98 dan pemilik merek dagang tersebut.
 Untuk pertanyaan atau permohonan terkait hak cipta, silakan menghubungi kami melalui kontak email yang tercantum dalam dokumen ini.
 Terima kasih atas pengertian dan kepatuhan Anda terhadap hak cipta ini. Kami berharap dokumen ini memberikan manfaat dan informasi berharga, serta tetap menjadi aset yang dilindungi dengan baik.
 © 2023 axroc98. Seluruh hak cipta dilindungi oleh undang-undang.

[==========================]
 Kontak Saya:
 Email: axroc98@proton.me
[==========================]
"""

import json

# Memuat data dari code_wilayah_indonesia.json
with open('code_wilayah_indonesia.json', 'r') as file:
    data = json.load(file)

def get_location_info(provinsi_code, kabupaten_code, kecamatan_code):
    # Mencari nama provinsi
    provinsi = None
    for provinsi in data['provinsi']:
        if provinsi['id'] == provinsi_code:
            provinsi = provinsi
            break

    if not provinsi:
        return "Kode provinsi tidak valid"

    # Mencari nama kabupaten
    kabupaten = None
    for kabupaten in provinsi['kabupaten']:
        if kabupaten['id'] == kabupaten_code:
            kabupaten = kabupaten
            break

    if not kabupaten:
        return "Kode kabupaten tidak valid"

    # Mencari nama kecamatan
    kecamatan = None
    if 'kecamatan' in kabupaten:
        for kecamatan in kabupaten['kecamatan']:
            if kecamatan['id'] == kecamatan_code:
                kecamatan = kecamatan
                break

    if not kecamatan:
        return "Kode kecamatan tidak valid"

    return f"Provinsi: {provinsi['nama']}\nKabupaten: {kabupaten['nama']}\nKecamatan: {kecamatan['nama']}"

def parse_nik(nik):
    if len(nik) != 16:
        return "Format NIK tidak valid"
    
    provinsi_code = nik[0:2]
    kabupaten_code = nik[0:4]
    kecamatan_code = nik[0:6]
    birthday = nik[6:12]
    index = nik[12:]

    # Mengambil tanggal, bulan, dan tahun dari tanggal lahir
    day = birthday[:2]
    month = birthday[2:4]
    year = birthday[4:]

    # Memeriksa apakah tanggal dan bulan dalam rentang yang valid
    if int(day) > 31 or int(month) > 12:
        return "Format NIK tidak valid"

    # Memeriksa apakah orang tersebut perempuan (DD + 40)
    is_female = False
    if int(day) > 40:
        day = str(int(day) - 40)
        is_female = True

    # Menentukan jenis kelamin berdasarkan NIK yang diberikan
    gender = 'Perempuan' if is_female else 'Laki-laki'

    # Menentukan abad berdasarkan NIK yang diberikan
    century = ''
    if int(year) >= 00 and int(year) <= 21:
        century = '20'
    elif int(year) >= 22 and int(year) <= 99:
        century = '19'

    # Menambahkan abad ke tahun
    year = century + year

    # Menambahkan nol di depan tanggal dan bulan jika diperlukan
    day = day.zfill(2)
    month = month.zfill(2)

    location_info = get_location_info(provinsi_code, kabupaten_code, kecamatan_code)
    if "Kode" in location_info:
        return location_info

    return f"{location_info}\nTanggal Lahir: {day}-{month}-{year}\nJenis Kelamin: {gender}\nNo Urut: {index}"

# Contoh penggunaan
nik_number = input("NIK: ")
result = parse_nik(nik_number)
print(result)