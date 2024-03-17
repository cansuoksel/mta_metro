import pandas as pd

# Veri setini yükleme
mta_data = pd.read_csv('mta_data.csv')

# Veri setinin ilk 5 satırını gösterme
print(mta_data.head())

# Veri setinin temel istatistikleri
print(mta_data.describe())

# Eksik değerleri kontrol etme
print(mta_data.isnull().sum())

# Eksik değerleri doldurma veya silme
mta_data.dropna(inplace=True)  # Eksik satırları silme

import matplotlib.pyplot as plt
import seaborn as sns

# Örnek bir görselleştirme: Günlük yolcu giriş çıkışları
plt.figure(figsize=(10, 6))
sns.lineplot(data=mta_data, x='transit_timestamp', y='ridership')
plt.xlabel('Tarih')
plt.ylabel('Giriş Sayısı')
plt.title('Günlük Yolcu Giriş Sayısı')
plt.xticks(rotation=45)
plt.show()

# Örnek bir analiz: İstasyon bazında ortalama giriş sayısı
station_entries = mta_data.groupby('station_complex')['ridership'].mean().reset_index()
station_entries = station_entries.sort_values(by='ridership', ascending=False)

# En yüksek 10 istasyonu görselleştirme
# En yüksek 10 istasyonu görselleştirme (görsel boyutunu ayarlayarak)
plt.figure(figsize=(10, 6))
sns.barplot(data=station_entries.head(10), x='ridership', y='station_complex')
plt.xlabel('Ortalama Giriş Sayısı')
plt.ylabel('İstasyon')
plt.title('En Yüksek 10 İstasyon (Ortalama Giriş Sayısı)')
plt.xticks(rotation=45, ha='right')  # İstasyon isimlerini yatay olarak düzenleme
plt.tight_layout()  # Görseli sığdırmak için
plt.show()

