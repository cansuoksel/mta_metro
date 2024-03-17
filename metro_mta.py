import pandas as pd

mta_data = pd.read_csv('mta_data.csv')

print(mta_data.head())

print(mta_data.describe())

print(mta_data.isnull().sum())

mta_data.dropna(inplace=True) 

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.lineplot(data=mta_data, x='transit_timestamp', y='ridership')
plt.xlabel('Tarih')
plt.ylabel('Giriş Sayısı')
plt.title('Günlük Yolcu Giriş Sayısı')
plt.xticks(rotation=45)
plt.show()

station_entries = mta_data.groupby('station_complex')['ridership'].mean().reset_index()
station_entries = station_entries.sort_values(by='ridership', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=station_entries.head(10), x='ridership', y='station_complex')
plt.xlabel('Ortalama Giriş Sayısı')
plt.ylabel('İstasyon')
plt.title('En Yüksek 10 İstasyon (Ortalama Giriş Sayısı)')
plt.xticks(rotation=45, ha='right')  # İstasyon isimlerini yatay olarak düzenleme
plt.tight_layout()  # Görseli sığdırmak için
plt.show()

