# **Assigment Day 2 |Python 1|**
kelompok = "kelompok 1"
anggota_kelompok = "Khairunisa Fitri, M Arif Rahman, Noer Amalia Puspita, Nurhayati, Rahman Zuhri Maulana"
print ("Kami dari {satu}, dengan anggota kelompok 1 adalah {dua}". format(satu=kelompok, dua=anggota_kelompok))
# **Assigment 1**


str_val = "Balonku ada lima"
str_val = str_val.replace("o", "a")
str_val = str_val.replace("u", "a")
str_val = str_val.replace("i", "a")
print(str_val)
# **Assigment 2**
Class_held = 20

Students = ["Asnawi", "Haaland", "Hazard", "Maudy Ayunan", "Marselino", "Dembele"]

Class_attended = [18, 19, 10, 20, 17, 13]

attendance = [(attendend / Class_held) * 100 for attendend in Class_attended]

for i, student in enumerate(Students):
    print(f" Kehadiran {student} , attendance: {attendance[i]:.2f}% Boleh Mengikuti ujian")

attendance

# perubahan nur amalia puspita 
# tugas python 1 day 2 / dibimbing.id