# 🧹 Le Nettoyeur Excel (Data Sanitizer & SQLite Migrator)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📋 Executive Summary
**Le Nettoyeur** is an automated ETL (Extract, Transform, Load) microservice designed for industrial B2B environments. 

Many businesses operate on fragile, human-error-prone Excel files containing mixed data types, invisible spaces, and inconsistent formatting. This Streamlit application acts as a "Washing Machine," taking chaotic Excel files, automatically restructuring them using Pandas and Regex, and migrating the clean data into a secure **SQLite Database** while providing a highly formatted Excel output for the end-user.

## 🏗️ Core Features

* **🔍 Real-Time Data Audit:** Instantly calculates duplicates, empty cells, and row integrity before any transformation occurs.
* **🧠 Smart Regex Extraction:** Automatically detects and isolates numbers from contaminated strings (e.g., converting `"150 UNITS"` to `150`).
* **✨ Intelligent Text Standardization:** Strips hidden characters (`\t`, `\n`), enforces uppercase standardizations, and contextually fills missing data (e.g., `DATE INCONNUE` vs. `INCONNU`).
* **🎨 Dynamic Excel Styling (`openpyxl`):** Auto-adjusts column widths, applies B2B color grading, injects local currency formatting (MAD), and highlights critical stock levels in red/green.
* **🗄️ SQL Migration:** Safely duplicates the cleansed data into a local `.db` SQLite vault, preparing it for Power BI or Azure ingestion.

## 🚀 How to Run Locally

### 1. Install Dependencies
Ensure you have Python installed, then set up your environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Launch the Application
```bash
streamlit run app.py
```

### 3. Test with "Chaos Data"
A `generate_messy_data.py` script is included in the repository to simulate a severe industrial "Data Nightmare" (mixed types, bad dates, ghost rows). Generate the file and upload it to the Streamlit UI to watch the cleaning engine in action.

---

## 👤 Author
**El Walid El Alaoui Fels**
* Consultant en Ingénierie de la Donnée & Automatisation
* [LinkedIn](https://www.linkedin.com/in/el-walid-el-alaoui-fels-51491538b/)
