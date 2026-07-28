# 📡 AI Patch Antenna Designer

> **An Intelligent AI-Based Microstrip Patch Antenna Design System using Machine Learning and Interactive 3D Visualization**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-success)
![Plotly](https://img.shields.io/badge/Plotly-3D%20Visualization-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

AI Patch Antenna Designer is an intelligent web application that predicts the optimal dimensions of a rectangular microstrip patch antenna using Machine Learning.

Instead of performing repetitive manual calculations, users simply enter the antenna design parameters and the AI model instantly predicts the required antenna dimensions. The application also generates an interactive 3D visualization of the predicted antenna, providing an intuitive engineering-oriented design experience.

This project combines Artificial Intelligence, Machine Learning, RF Engineering, and Interactive Visualization into a single professional application.

---

# ✨ Key Features

### 🤖 AI-Powered Prediction

* Predicts antenna dimensions instantly
* XGBoost Regression model
* High prediction accuracy
* Fast inference
* User-friendly interface

---

### 📐 Input Parameters

Users provide:

* Center Frequency (GHz)
* Dielectric Constant (εr)
* Substrate Height
* Loss Tangent
* Copper Thickness
* Substrate Material

---

### 📊 Predicted Outputs

The AI model predicts:

* Patch Width
* Patch Length
* Ground Width
* Ground Length

---

### 🛰️ Interactive 3D Antenna Visualization

The application automatically generates an interactive 3D model after prediction.

Features include:

* 360° Rotation
* Zoom
* Pan
* Ground Plane
* Substrate Layer
* Copper Patch
* Feed Line
* Professional Lighting
* Dynamic Geometry

---

### 📷 Multiple Camera Views

Users can inspect the antenna from multiple perspectives.

* Top View
* Front View
* Side View
* Isometric View
* Reset View

---

### 📄 Report Generation

Generate downloadable reports including:

* Input Parameters
* Predicted Dimensions
* Model Information
* Design Summary
* CSV Export
* PDF Report
* 3D Model Snapshot (optional)

---

## 🧠 Machine Learning Model

Current Model:

* XGBoost Regressor

Model Comparison:

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

Evaluation Metrics:

* R² Score
* MAE
* RMSE

The best-performing model is selected for deployment.

---

# 🏗️ Technology Stack

## Frontend

* Streamlit

## Machine Learning

* Scikit-learn
* XGBoost

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly
* Matplotlib

## Model Storage

* Joblib

## Report Generation

* ReportLab

---

# 📂 Project Structure

```text
AI_Patch_Antenna_Designer/
│
├── app.py
├── antenna_dataset.csv
├── antenna_model.pkl
├── requirements.txt
├── README.md
│
├── utils/
│   ├── antenna_3d.py
│   ├── predictor.py
│   └── report_generator.py
│
├── assets/
│
└── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Patch-Antenna-Designer.git
```

Move to project directory

```bash
cd AI-Patch-Antenna-Designer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Workflow

```
User Inputs
      │
      ▼
AI Prediction
      │
      ▼
Predicted Antenna Dimensions
      │
      ▼
Interactive 3D Antenna Model
      │
      ▼
Download Report
```

---

# 💡 Future Enhancements

* CST/HFSS compatible export
* AI-based antenna optimization
* Multi-band antenna support
* Slot antenna design
* Circular patch antenna prediction
* SHAP explainability
* Cloud deployment
* API integration
* Antenna performance estimation
* Radiation pattern prediction

---

# 🎯 Applications

* RF Engineering
* Wireless Communication
* Antenna Design
* Educational Learning
* AI-Assisted Engineering
* Research and Development
* Academic Projects

---

# 📈 Highlights

* AI-Based Engineering Application
* Machine Learning Driven Prediction
* Interactive 3D Visualization
* Professional User Interface
* Industry-Oriented Project
* Real-Time Design Prediction
* Engineering Report Generation

---

# 👩‍💻 Author

**Hanshika Mukati**

B.Tech – Computer Science and Engineering

Machine Learning | Artificial Intelligence | Full Stack Development | Cyber Security Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.
