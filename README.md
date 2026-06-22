# AI-Based Inverse Design System for Rectangular Microstrip Patch Antennas

## Project Overview

This project implements an **AI-based inverse design system for Rectangular Microstrip Patch Antennas (RMPA)**.

The system predicts antenna dimensions from a user-specified operating frequency using Machine Learning.

Traditionally, antenna designers calculate dimensions using multiple electromagnetic equations. This project automates the design process by learning the relationship between operating frequency and antenna parameters, enabling fast prediction of antenna dimensions.

The current implementation assumes a standard **FR4 substrate** and predicts:

- Patch Width (W)
- Patch Length (L)
- Ground Width (Wg)
- Ground Length (Lg)

from a single input parameter:

- Operating Frequency (GHz)

---

# Problem Statement

Designing a microstrip patch antenna requires multiple mathematical calculations and engineering knowledge.

The objective of this project is to develop a machine learning system that learns the relationship between frequency and antenna dimensions and predicts antenna parameters instantly.

---

# Objectives

- Generate an antenna design dataset using standard antenna equations.
- Train a machine learning regression model.
- Predict antenna dimensions from operating frequency.
- Reduce manual antenna design calculations.
- Create a foundation for future AI-based antenna optimization systems.

---

# Technologies Used

## 1. Python

### Purpose

Python is used as the primary programming language for:

- Machine Learning
- Numerical Computing
- Data Processing
- Scientific Applications

### Why Python?

Python provides extensive libraries for machine learning and scientific computing, reducing development time.

### Why Not C/C++?

Although C/C++ provides better execution speed, Python offers a much larger ecosystem for AI and machine learning development.

---

# 2. NumPy

## Purpose

NumPy is used for:

- Numerical calculations
- Mathematical operations
- Antenna design equation implementation

## Why NumPy?

NumPy provides optimized array operations and efficient scientific computation.

### Why Not Traditional Loops?

Traditional loops are slower and less efficient for large numerical operations.

---

# 3. Pandas

## Purpose

Pandas is used for:

- Dataset generation
- Data organization
- CSV file creation
- Structured data handling

## Why Pandas?

Pandas simplifies dataset management and preprocessing for machine learning workflows.

### Why Not Excel?

Excel is mainly useful for manual analysis and visualization but is not suitable for automated machine learning pipelines.

---

# 4. Scikit-Learn

## Purpose

Scikit-Learn is used for:

- Machine learning model training
- Model evaluation
- Prediction

## Why Scikit-Learn?

Scikit-Learn is lightweight, reliable, and suitable for regression-based engineering problems.

### Why Not TensorFlow or PyTorch?

TensorFlow and PyTorch are powerful deep learning frameworks but require:

- Larger datasets
- More computational resources
- More complex architectures

For this regression problem, Scikit-Learn provides sufficient performance with lower complexity.

---

# 5. Random Forest Regressor

## Purpose

Random Forest Regression is used to predict:

- Patch Width
- Patch Length
- Ground Width
- Ground Length

## Why Random Forest?

Advantages:

- Handles nonlinear relationships
- High prediction accuracy
- Resistant to overfitting
- Requires less training time
- Easy to interpret

## Why Not Linear Regression?

Antenna parameters have nonlinear relationships with frequency. Random Forest captures these complex patterns more effectively.

## Why Not Neural Networks?

Neural Networks generally require:

- Large datasets
- Longer training time
- Higher computational resources

Random Forest provides strong performance with lower complexity.

---

# 6. Joblib

## Purpose

Joblib is used for saving and loading the trained machine learning model.

## Why Joblib?

Advantages:

- Fast serialization
- Efficient model storage
- Easy deployment

---

# 7. Streamlit (Optional UI)

## Purpose

Streamlit provides a simple web interface for interacting with the ML model.

## Why Streamlit?

Advantages:

- Simple implementation
- Fast deployment
- No frontend development required

## Why Not React?

React requires:

- JavaScript knowledge
- API development
- Frontend-backend integration

Streamlit allows rapid ML application development using Python only.

---

# Dataset Generation

The dataset is generated using standard **Rectangular Microstrip Patch Antenna design equations**.

## Fixed Parameters

| Parameter | Value |
|-----------|-------|
| Substrate Material | FR4 |
| Dielectric Constant | 4.4 |
| Substrate Height | 1.6 mm |
| Antenna Type | Rectangular Microstrip Patch Antenna |

---

# Input Parameter

| Parameter | Unit |
|-----------|------|
| Operating Frequency | GHz |

---

# Output Parameters

| Parameter | Unit |
|-----------|------|
| Patch Width (W) | mm |
| Patch Length (L) | mm |
| Ground Width (Wg) | mm |
| Ground Length (Lg) | mm |

---

# Machine Learning Workflow

```
Frequency Input
        |
        ↓
Dataset Generation
        |
        ↓
Feature Processing
        |
        ↓
Random Forest Training
        |
        ↓
Trained ML Model
        |
        ↓
Dimension Prediction
        |
        ↓
User Interface
```

---

# Project Architecture

```
User Frequency Input

        ↓

Antenna Equation Based Dataset Generation

        ↓

Machine Learning Model Training

        ↓

Random Forest Regression Model

        ↓

Predicted Antenna Dimensions
```

---

# Features

- AI-based antenna inverse design
- Frequency-based dimension prediction
- Automated antenna parameter calculation
- Machine learning powered prediction system
- Scalable architecture
- Easy extension for optimization tasks

---

# Current Limitations

The current version assumes:

- Fixed FR4 substrate
- Constant dielectric constant
- Fixed substrate thickness

Therefore, every frequency corresponds to a single standard antenna configuration.

---

# Future Scope

Future improvements can include:

- Multiple substrate material support
- Variable dielectric constant
- Variable substrate thickness
- Gain optimization
- Bandwidth optimization
- Feed point prediction
- CST simulation integration
- Deep learning based inverse design
- Automated antenna layout generation

---

# Installation and Usage

## Clone Repository

```bash
git clone https://github.com/Hanshika103/Patch_antenna_ai.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# Project Structure

```
Patch_antenna_ai/

│
├── app.py
├── generate_dataset.py
├── train_model.py
├── antenna_dataset.csv
├── requirements.txt
├── README.md
└── antenna_model.pkl
```

---

# Conclusion

This project demonstrates the application of Machine Learning in antenna engineering.

By learning the relationship between operating frequency and antenna parameters, the model predicts antenna dimensions automatically, reducing manual calculations and providing a foundation for advanced AI-assisted antenna design systems.

---

## Author

**Hanshika Mukati**

AI-Based Inverse Design System for Rectangular Microstrip Patch Antennas
