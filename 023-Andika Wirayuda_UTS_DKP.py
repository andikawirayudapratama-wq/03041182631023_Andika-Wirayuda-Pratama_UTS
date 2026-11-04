data_arus = [1.6, 2.2, 3.5, 4.1, 5.4, 2.8, 6.0, 3.9, 1.9, 4.8, 5.1, 2.6, 3.2, 4.4, 5.8, 1.3, 6.6, 0.7, 6.7, 2.9,] 
tegangan = 220 # int
def hitung_daya(tegangan, arus):
    return round (tegangan * arus, 3)
for arus in data_arus:
    P = hitung_daya(tegangan, arus)
def status_beban(P):
    if P >= 1000:
        return "Beban Tinggi"
    elif P <= 700:
       return "Normal"
    else:
       return "Warning"
def rata_rata(data):
    return sum(data) / len(data)

print("   BESAR DAYA           STATUS")
data_daya = []
for arus in data_arus:
    P = hitung_daya(tegangan, arus)
    data_daya.append(P)
    if P >= 1000:
        print("DAYA:", P, "Watt | STATUS:", status_beban(P))
    else :
        print("DAYA:", P, "Watt  | STATUS:", status_beban(P))
print("")
print("Ringkasan")
print("Rata-rata daya:", round(rata_rata(data_daya), 2), "Watt")
print("Total data    :", len(data_arus))
print("Daya maksimum :", max(data_daya), "Watt")
print("Daya minimum  :", min(data_daya), "Watt")