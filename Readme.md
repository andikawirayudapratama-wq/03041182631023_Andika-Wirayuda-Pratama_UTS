Judul       : Program Monitoring Beban/Daya Listrik
Nama        : Andika Wirayuda Pratama
NIM         : 03041182631023
Kelompok    : A
Mata kuliah : DKP
IPO         : Input = 20 data_arus listrik dan tegangan 220v
              Proses= Menghitung daya menggunakan rumus P = V × I, menentukan status, dan menghitung statistik daya
              Output= Daya, status, jumlah kategori, rata-rata, daya maksimum, dan minimum
Ketentuan   : P>1000      : Beban Tinggi
              P<=700      : Normal
              700<P<=1000 : Warning
Function    : hitung_daya  = menghitung daya listrik berdasar arus dan tegangan
              status_beban = menentukan status beban berdasarkan daya
              rata_rata    = menghitung rata-rata daya dengan menjumlahkan semua daya lalu dibagi dengan jumlahnya
List        : menyimpan 20 data arus listrik.
Loop        : memproses seluruh data arus.
If/Elif/Else: menentukan kategori daya.
Function    : membagi program menjadi beberapa fungsi.
Return      : mengembalikan hasil perhitungan fungsi.
data tambah : [1.3, 6.6, 0.7, 6.7, 2.9,]
AI          : Tidak memakai AI hanya menggunakan ekstension, AI digunakan hanya untuk search cara membuat file readme