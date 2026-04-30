# 🌫️ Air Quality Analysis Dashboard

Proyek ini bertujuan untuk menganalisis kualitas udara di Beijing berdasarkan data dari 12 stasiun monitoring periode Maret 2013 hingga Februari 2017.

---

## 📊 Pertanyaan Bisnis

1. Distrik mana di Beijing yang dapat diklasifikasikan memiliki kualitas udara baik dan buruk berdasarkan konsentrasi PM2.5 menggunakan standar AQI dengan target akurasi model klasifikasi minimal 80% berdasarkan data dari 12 stasiun monitoring periode Maret 2013 hingga Februari 2017?
2. Faktor polutan apa yang paling dominan memengaruhi klasifikasi kualitas udara buruk di berbagai distrik Beijing berdasarkan feature importance model klasifikasi, dan rekomendasi apa yang dapat diberikan berdasarkan perbandingan karakteristik distrik dengan kualitas udara baik selama periode Maret 2013 hingga Februari 2017?

---

## 📁 Struktur Folder

```
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.parquet
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## ⚙️ Setup Environment

### Anaconda

```
conda create --name air-quality python=3.9
conda activate air-quality
pip install -r requirements.txt
```

### Terminal / CMD

```
pip install streamlit pandas matplotlib seaborn scikit-learn pyarrow
```

---

## 🚀 Menjalankan Dashboard

```
cd dashboard
python -m streamlit run dashboard.py
```

---

## 📌 Hasil Analisis

### Pertanyaan 1

* Distrik dengan rata-rata PM2.5 tinggi dikategorikan memiliki kualitas udara buruk.
* Distrik dengan nilai PM2.5 rendah dikategorikan memiliki kualitas udara baik.
* Model klasifikasi Random Forest berhasil mencapai akurasi ≥ 80%.

### Pertanyaan 2

* PM10 merupakan faktor paling dominan dalam menentukan kualitas udara buruk.
* NO2 dan SO2 juga memiliki pengaruh signifikan terhadap kondisi polusi.

---

## 📈 Insight Data

* Dataset terdiri dari 420.768 data dan 18 kolom.
* Terdapat missing values pada beberapa parameter polusi (PM2.5, PM10, SO2, NO2, CO, O3).
* Tidak ditemukan data duplikat.
* Distribusi PM2.5 cenderung tidak merata (skewed).

---

## 🧹 Data Preprocessing

* Missing values ditangani menggunakan imputasi median.
* Outlier pada PM2.5 ditangani menggunakan metode IQR.
* Data kemudian digunakan untuk analisis dan modeling.

---

## 📌 Rekomendasi

* Mengurangi emisi kendaraan di distrik dengan polusi tinggi.
* Meningkatkan pengawasan terhadap industri penyumbang polutan.
* Mendorong penggunaan energi ramah lingkungan.

---

## 📎 Catatan

* Visualisasi menggunakan Matplotlib dan Seaborn.
* Model klasifikasi menggunakan Random Forest.
* Dashboard dibuat menggunakan Streamlit.
