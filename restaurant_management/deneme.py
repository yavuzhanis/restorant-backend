import pandas as pd

# Öğrenci Bilgileri Tablosu
columns_student_info = [
    "Bölüm/Fakülte",
    "Öğrenci Numarası",
    "Ad Soyad",
    "Siber Güvenlik Başlangıç",
    "Siber Güvenlik İleri Seviye",
    "Front End Development Başlangıç",
    "Front End Development İleri Seviye",
    "Backend Development Başlangıç",
    "Backend Development İleri Seviye",
    "Network Başlangıç",
    "Network İleri Seviye",
]

# Öğrenci Bilgileri Verisi
data_student_info = [
    [
        "Fakülte A",
        "12345",
        "Ali Veli",
        "Başlangıç",
        "İleri Seviye",
        "Orta Seviye",
        "Başlangıç",
        "Başlangıç",
        "İleri Seviye",
        "İleri Seviye",
        "Orta Seviye",
    ]
]

# Yazılım Dili Yetkinlik Tablosu
columns_software_skills = ["Yazılım Dili", "Başlangıç", "Orta Seviye", "İleri Seviye"]
data_software_skills = [
    ["PYTHON", "Başlangıç", "Orta Seviye", "İleri Seviye"],
    ["JAVASCRIPT", "Başlangıç", "Orta Seviye", "İleri Seviye"],
    ["PHP", "Başlangıç", "Orta Seviye", "İleri Seviye"],
    ["Java", "Başlangıç", "Orta Seviye", "İleri Seviye"],
    ["C++", "Başlangıç", "Orta Seviye", "İleri Seviye"],
    ["C#", "Başlangıç", "Orta Seviye", "İleri Seviye"],
]

# DataFrame'ler oluşturuluyor
df_student_info = pd.DataFrame(data_student_info, columns=columns_student_info)
df_software_skills = pd.DataFrame(data_software_skills, columns=columns_software_skills)

# Excel dosyasına kaydetme
file_path = "/Users/yavuzhanis/Desktop/ogrenci_bilgileri_with_skills.xlsx"

with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
    # Öğrenci Bilgileri Tablosunu yazıyoruz
    df_student_info.to_excel(writer, sheet_name="Öğrenci Bilgileri", index=False)

    # Yazılım Dili Yetkinlik Tablosunu yazıyoruz
    df_software_skills.to_excel(
        writer, sheet_name="Yazılım Dili Yetkinlikleri", index=False
    )

print(f"Dosya başarıyla kaydedildi: {file_path}")
