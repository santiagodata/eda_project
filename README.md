# 📊 Proyecto de Análisis Exploratorio de Datos (EDA) con Python

Este repositorio contiene un proyecto completo de **Análisis Exploratorio de Datos (EDA)** realizado en Python sobre un dataset sintético de clientes de e-commerce.

El objetivo del proyecto es **comprender la estructura, calidad y patrones de los datos** antes de aplicar transformaciones avanzadas, inferencia estadística o modelos predictivos.

El análisis se enmarca en la fase de **Data Understanding** del enfoque CRISP-DM.

---

## 📁 Dataset

**Ruta:** `data/customers_ecommerce_churn.csv`

El dataset simula información de clientes de una plataforma de e-commerce y fue diseñado intencionalmente para reflejar escenarios reales de negocio, incluyendo:

- Valores faltantes  
- Registros duplicados  
- Outliers  
- Variables numéricas, categóricas y temporales  
- Variable objetivo binaria: `churned`  

La descripción detallada de cada columna se encuentra en `DATA_DICTIONARY.md`.

---

## 🧠 Alcance del análisis

El proyecto se centra **exclusivamente en Análisis Exploratorio de Datos (EDA)**.

Incluye:

- Inspección de estructura y tipos de datos  
- Evaluación de calidad (valores faltantes y duplicados)  
- Análisis descriptivo de variables numéricas y categóricas  
- Comparaciones bivariadas contra `churned`  
- Tasas de churn por segmentos  
- Correlación entre variables numéricas  

**Fuera de alcance (intencionalmente):** ingeniería de variables, pruebas estadísticas formales, modelos predictivos y recomendaciones prescriptivas.

---

## 🗂️ Estructura del proyecto

```text
.
├── data/
│   └── customers_ecommerce_churn.csv
├── src/
│   └── eda.py
├── notebooks/
│   └── EDA_Customers_Churn.ipynb
├── reports/
│   ├── EDA_Report.md
│   ├── eda_summary.json
│   └── figures/
│       └── *.png
├── DATA_DICTIONARY.md
├── requirements.txt
└── README.md
```

---

## ▶️ Ejecución

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m src.eda
```

---

## 📤 Salidas generadas

Al ejecutar el script se generan automáticamente:

- **`reports/eda_summary.json`**  
  Resumen estructurado (métricas descriptivas, valores faltantes, duplicados y correlaciones).

- **`reports/figures/*.png`**  
  Gráficos del EDA (histogramas, boxplots por churn, tasas de churn por segmento y matriz de correlación).

- **[`reports/EDA_Report.md`](reports/eda_report.md)**   
  Informe del EDA con narrativa analítica y gráficos embebidos.

---

## 📅 Información adicional

- Lenguaje: **Python**
- Librerías principales: `pandas`, `numpy`, `matplotlib`, `seaborn`
- Fecha de generación del análisis: **2026-01-06**

---

## 📝 Nota final

Este proyecto prioriza la **comprensión profunda de los datos**, la comunicación clara de hallazgos y la separación explícita entre exploración y modelado.
