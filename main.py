data_arus = [1.6, 2.2, 3.5, 4.1, 5.4, 2.8, 6.0, 3.9, 1.9, 4.8, 5.1, 2.6, 3.2, 4.4, 5.8, 1.3, 6.6, 0.7, 6.7, 2.9]
tegangan = 220  # Volt

def hitung_daya(tegangan, arus):
    return tegangan * arus

def status_beban(daya):
    if daya > 1000:
        return "BEBAN TINGGI"
    elif daya <= 700:
        return "NORMAL"
    else:
        return "WARNING"

def rata_rata(data):
    return sum(data) / len(data)

def hitung_kategori(data_status):
    jumlah_normal = data_status.count("NORMAL")
    jumlah_warning = data_status.count("WARNING")
    jumlah_tinggi = data_status.count("BEBAN TINGGI")
    return jumlah_normal, jumlah_warning, jumlah_tinggi

data_daya = []
data_status = []
print("             MONITORING BEBAN / DAYA LISTRIK")
print("-" * 62)
print(f"{'No.':<5}{'Arus (A)':<15}{'Daya (W)':<17}{'Status'}")
print("-" * 62)

for nomor, arus in enumerate(data_arus, start=1):
    daya = hitung_daya(tegangan, arus)
    status = status_beban(daya)

    data_daya.append(daya)
    data_status.append(status)
    print(f"{nomor:<5}{arus:<15.2f}{daya:<17.2f}{status}")
jumlah_normal, jumlah_warning, jumlah_tinggi = hitung_kategori(data_status)
print("-" * 62)
print("RINGKASAN:")
print(f"Total data          : {len(data_arus)}")
print(f"Jumlah NORMAL       : {jumlah_normal}")
print(f"Jumlah WARNING      : {jumlah_warning}")
print(f"Jumlah BEBAN TINGGI : {jumlah_tinggi}")
print(f"Rata-rata daya      : {rata_rata(data_daya):.2f} W")
print(f"Daya maksimum       : {max(data_daya):.2f} W")
print(f"Daya minimum        : {min(data_daya):.2f} W")