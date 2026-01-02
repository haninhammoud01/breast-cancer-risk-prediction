# 🧠 Breast Cancer Prediction  

---
## 🚀 Project Overview

Repository ini merupakan **Tugas Kelompok 4** pada mata kuliah **Proyek Sains Data**. Proyek ini berfokus pada implementasi teknik **Machine Learning** untuk memprediksi kanker payudara (jinak atau ganas) berdasarkan karakteristik sel hasil pemeriksaan **Fine Needle Aspiration (FNA)**.

Dataset yang digunakan adalah *Breast Cancer Wisconsin Original Dataset*, yang berisi data numerik hasil observasi morfologi sel oleh ahli patologi. Proyek ini mencakup seluruh pipeline data science, mulai dari *data understanding*, *preprocessing*, *handling imbalance*, *modeling*, hingga *evaluasi model*.

---

## 🎯 Objectives

* Menerapkan tahapan data science secara end-to-end
* Membangun dan membandingkan beberapa model klasifikasi
* Menghasilkan model prediksi kanker payudara yang akurat dan dapat digunakan kembali

---

## 📊 Dataset

* **Name**: Breast Cancer Wisconsin Original Dataset
* **Source**: Kaggle – Breast Cancer Wisconsin Original Dataset
  [https://www.kaggle.com/datasets/schizzika/breast-cancer-data-winconsin-original/data](https://www.kaggle.com/datasets/schizzika/breast-cancer-data-winconsin-original/data)*
* **Type**: Medical diagnostic data (numeric features)

**Target Classes**:

* Benign (Jinak)
* Malignant (Ganas)

---

## 🧩 Project Architecture

```
Proyek-Sains-Data/
├── presentation/
│   └── ProjectAkhir_Kelompok4.pptx      # Project presentation slides
├── app.py                               # Streamlit web app (inference)
├── pipeline.py                          # Preprocessing & training pipeline
├── Breast_Cancer_ML_Pipeline.ipynb      # EDA, experiments, and modeling
├── breast_cancer.csv                    # Dataset
├── model_rf.pkl                         # Trained Random Forest model
├── requirements.txt                     # Project dependencies
└── .gitignore
```

Keterangan:

* `app.py` : File utama untuk melakukan prediksi (inference)
* `pipeline.py` : Pipeline preprocessing dan pelatihan model
* `Breast_Cancer_ML_Pipeline.ipynb` : Notebook eksplorasi data, preprocessing, dan modeling
* `model_rf.pkl` : Model Random Forest terlatih
* `presentation/` : Folder berisi slide presentasi proyek

---

## 🛠️ Techniques & Methods

* Data Cleaning & Preprocessing
* Deteksi Outlier (LOF)
* Penanganan Imbalanced Data (SMOTE)
* Model Klasifikasi:

  * Random Forest
  * Decision Tree
  * Naive Bayes
  * K-Nearest Neighbor (KNN)

---

## ⚙️Tools & Library

* Python
* Pandas, NumPy
* Scikit-learn
* Imbalanced-learn
* Matplotlib & Seaborn
* Joblib

---

## 🖥️ How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 🌐 Live Demo & Resources

* 🔗 **Live Deployment**:
  [https://prediksibreastcancerwinconsin.streamlit.app/](https://prediksibreastcancerwinconsin.streamlit.app/)

* 📦 **GitHub Repository**:
  [https://github.com/haninhammoud01/breast-cancer-risk-prediction](https://github.com/haninhammoud01/breast-cancer-risk-prediction)

* 📓 **Model Development (Google Colab)**:
  [https://colab.research.google.com/drive/1iTuq6NdzNznLI62a9ZCfrUxx43EYTm1h](https://colab.research.google.com/drive/1iTuq6NdzNznLI62a9ZCfrUxx43EYTm1h)

* 📽️ **Project Presentation Slides**:
  Available in `presentation/` folder or via Google Drive

---
