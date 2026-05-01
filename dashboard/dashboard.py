import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# CONFIG
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

# LOAD DATA
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_parquet(os.path.join(BASE_DIR, 'main_data.parquet'))

df.fillna(df.median(numeric_only=True), inplace=True)

Q1 = df['PM2.5'].quantile(0.25)
Q3 = df['PM2.5'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['PM2.5'] >= Q1 - 1.5*IQR) & (df['PM2.5'] <= Q3 + 1.5*IQR)]

# ===== SIDEBAR FILTER =====
st.sidebar.header("Filter")

stations = st.sidebar.multiselect(
    "Pilih Distrik",
    df['station'].unique(),
    default=df['station'].unique()
)

years = st.sidebar.multiselect(
    "Pilih Tahun",
    sorted(df['year'].unique()),
    default=sorted(df['year'].unique())
)

df = df[(df['station'].isin(stations)) & (df['year'].isin(years))]

# ===== TITLE =====
st.title("🌫️ Air Quality Dashboard Beijing")
st.markdown("Analisis kualitas udara berdasarkan PM2.5 dan polutan")

# ===== METRICS =====
col1, col2, col3 = st.columns(3)

col1.metric("Rata-rata PM2.5", round(df['PM2.5'].mean(),2))
col2.metric("PM2.5 Maks", round(df['PM2.5'].max(),2))
col3.metric("Jumlah Data", len(df))

# =====================================================
# PERTANYAAN 1
# =====================================================
st.header("Persentase Kualitas Udara per Distrik")

threshold = 50
df['is_bad'] = df['PM2.5'] > threshold

bad_ratio = df.groupby('station')['is_bad'].mean() * 100
bad_ratio = bad_ratio.sort_values()

fig1, ax1 = plt.subplots()
bad_ratio.plot(kind='bar', ax=ax1)
plt.title("Persentase Waktu PM2.5 > Ambang AQI")
plt.ylabel("Persentase (%)")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig1)

# Insight otomatis
best = bad_ratio.idxmin()
worst = bad_ratio.idxmax()

st.subheader("Insight")
st.write(f"✔ Distrik terbaik (udara paling bersih): **{best}**")
st.write(f"✔ Distrik terburuk (polusi tertinggi): **{worst}**")

# =====================================================
# PERTANYAAN 2
# =====================================================
st.header("Analisis Polutan Dominan")

pollutants = ['PM2.5','PM10','SO2','NO2','CO','O3']

# rata-rata
avg_pollutants = df[pollutants].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots()
avg_pollutants.plot(kind='bar', ax=ax2)
plt.title("Rata-rata Konsentrasi Polutan")
st.pyplot(fig2)

# bulanan
monthly = df.groupby('month')[pollutants].mean()

fig3, ax3 = plt.subplots()
monthly.plot(ax=ax3)
plt.title("Pola Bulanan Polutan")
st.pyplot(fig3)

# insight otomatis
top_pollutant = avg_pollutants.idxmax()

st.subheader("Insight")
st.write(f"Polutan paling dominan: **{top_pollutant}**")
st.write("Terlihat adanya pola perubahan konsentrasi polutan tiap bulan (indikasi musiman)")

# =====================================================
# ANALISIS LANJUTAN
# =====================================================
st.header("Tren Tahunan PM2.5")

trend = df.groupby('year')['PM2.5'].mean()

fig4, ax4 = plt.subplots()
trend.plot(ax=ax4)
plt.title("Tren PM2.5 per Tahun")
st.pyplot(fig4)

# =====================================================
# REKOMENDASI
# =====================================================
st.header("Rekomendasi")

st.write("""
- Mengurangi emisi kendaraan di distrik dengan polusi tinggi  
- Meningkatkan pengawasan industri penyumbang polusi  
- Mendorong penggunaan energi ramah lingkungan  
""")

# Footer
st.markdown("---")
st.caption("Proyek Analisis Data - Ani Nuri Azizah")
