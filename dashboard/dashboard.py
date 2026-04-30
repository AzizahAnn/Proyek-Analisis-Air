import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os
import pandas as pd

# unzip jika belum diekstrak
if not os.path.exists('main_data.csv'):
    with zipfile.ZipFile('main_data.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

# load data
df = pd.read_csv('main_data.csv')

# CONFIG
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

# LOAD DATA
df = pd.read_csv('main_data.csv')

st.title("🌫️ Air Quality Dashboard Beijing")
st.markdown("Analisis kualitas udara berdasarkan PM2.5 dan polutan lainnya")

# SIDEBAR FILTER 
st.sidebar.header("Filter Data")

stations = st.sidebar.multiselect(
    "Pilih Distrik",
    options=df['station'].unique(),
    default=df['station'].unique()
)

years = st.sidebar.multiselect(
    "Pilih Tahun",
    options=sorted(df['year'].unique()),
    default=sorted(df['year'].unique())
)

df_filtered = df[
    (df['station'].isin(stations)) &
    (df['year'].isin(years))
]

# ===== METRICS =====
col1, col2, col3 = st.columns(3)

col1.metric("Rata-rata PM2.5", round(df_filtered['PM2.5'].mean(), 2))
col2.metric("PM2.5 Maksimum", round(df_filtered['PM2.5'].max(), 2))
col3.metric("Jumlah Data", len(df_filtered))

# ===== VISUALISASI 1 =====
st.subheader("Rata-rata PM2.5 per Distrik")

station_avg = df_filtered.groupby('station')['PM2.5'].mean().sort_values()

fig1, ax1 = plt.subplots()
station_avg.plot(kind='bar', ax=ax1)
plt.xticks(rotation=45, ha='right')
plt.ylabel("PM2.5")
plt.title("Rata-rata PM2.5")
plt.tight_layout()

st.pyplot(fig1)

# Visualisasi 2 - Feature Importance
st.subheader("Feature Importance (Polutan)")

# simple model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df_filtered = df_filtered.dropna()

df_filtered['AQI_Class'] = df_filtered['PM2.5'].apply(lambda x: 'Baik' if x <= 50 else 'Buruk')

X = df_filtered[['PM10','SO2','NO2','CO','O3']]
y = df_filtered['AQI_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

importances = model.feature_importances_

fig2, ax2 = plt.subplots()
sns.barplot(x=importances, y=X.columns, ax=ax2)
plt.title("Feature Importance")

st.pyplot(fig2)

# Visualisasi 3 - Tren PM2.5 er tahun
st.subheader("📈 Tren PM2.5 per Tahun")

trend = df_filtered.groupby('year')['PM2.5'].mean()

fig3, ax3 = plt.subplots()
trend.plot(ax=ax3)
plt.title("Tren PM2.5")
plt.ylabel("PM2.5")

st.pyplot(fig3)

# Footer
st.markdown("---")
st.caption("Dibuat untuk Proyek Analisis Data")
