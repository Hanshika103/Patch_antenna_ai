AI-Based Inverse Design System for Rectangular Microstrip Patch Antennas

Project Overview

This project implements an AI-based inverse design system for Rectangular Microstrip Patch Antennas (RMPA). The system predicts antenna dimensions from a user-specified operating frequency.

Traditionally, antenna designers calculate dimensions using multiple electromagnetic equations. This project automates the process using Machine Learning, enabling fast prediction of antenna dimensions.

The current implementation assumes a standard FR4 substrate and generates:

- Patch Width (W)
- Patch Length (L)
- Ground Width (Wg)
- Ground Length (Lg)

from a single input parameter:

- Operating Frequency (GHz)

---

Problem Statement

Designing a microstrip patch antenna requires several mathematical calculations and engineering knowledge.

The objective of this project is to develop a machine learning system that learns the relationship between operating frequency and antenna dimensions and predicts antenna dimensions instantly.

---

Objectives

- Generate an antenna design dataset using standard antenna equations.
- Train a machine learning model.
- Predict antenna dimensions from frequency.
- Reduce manual calculations.
- Create a foundation for future AI-based antenna optimization systems.

---

Technologies Used

1. Python

Why Python?

Python provides extensive support for:

- Machine Learning
- Numerical Computing
- Data Processing
- Scientific Applications

Why Not C/C++?

Although C/C++ is faster, Python provides rich machine learning libraries and significantly reduces development time.

---

2. NumPy

Purpose

NumPy is used for:

- Numerical computations
- Mathematical operations
- Antenna equation calculations

Why NumPy?

NumPy provides optimized array operations and scientific computing functions.

Why Not Traditional Loops?

Traditional loops are slower and less efficient for numerical computations.

---

3. Pandas

Purpose

Pandas is used to:

- Create datasets
- Store antenna parameters
- Export CSV files
- Manage structured data

Why Pandas?

Pandas simplifies dataset handling and preprocessing.

Why Not Excel?

Excel is useful for visualization but not suitable for automated dataset generation and machine learning workflows.

---

4. Scikit-Learn

Purpose

Scikit-Learn is used for:

- Machine Learning model training
- Model evaluation
- Prediction

Why Scikit-Learn?

Scikit-Learn is lightweight, reliable, and ideal for regression-based engineering applications.

Why Not TensorFlow or PyTorch?

TensorFlow and PyTorch are powerful deep learning frameworks but introduce unnecessary complexity for this regression problem.

Scikit-Learn is sufficient and easier to explain during academic evaluations.

---

5. Random Forest Regressor

Purpose

Random Forest is used to predict:

- Patch Width
- Patch Length
- Ground Width
- Ground Length

Why Random Forest?

Advantages:

- High accuracy
- Handles nonlinear relationships
- Robust against overfitting
- Easy to train
- Easy to explain

Why Not Linear Regression?

Antenna parameter relationships are nonlinear.

Random Forest captures nonlinear patterns more effectively.

Why Not Neural Networks?

Neural Networks require:

- Larger datasets
- More training time
- More computational resources

Random Forest provides strong performance with lower complexity.

---

6. Joblib

Purpose

Joblib saves trained machine learning models.

Why Joblib?

- Fast serialization
- Efficient model storage
- Simple deployment

---

7. Streamlit (Optional UI)

Purpose

Provides a web-based user interface.

Why Streamlit?

- Simple
- Fast deployment
- No frontend expertise required

Why Not React?

React requires:

- JavaScript
- API integration
- Backend communication

Streamlit enables rapid ML application development using only Python.

---

Dataset Generation

The dataset is generated using standard Rectangular Microstrip Patch Antenna design equations.

The following parameters are fixed:

Parameter| Value
Substrate Material| FR4
Dielectric Constant| 4.4
Substrate Height| 1.6 mm
Antenna Type| Rectangular Microstrip Patch Antenna

---

Input Parameter

Parameter| Unit
Frequency| GHz

---

Output Parameters

Parameter| Unit
Patch Width (W)| mm
Patch Length (L)| mm
Ground Width (Wg)| mm
Ground Length (Lg)| mm

---

Machine Learning Workflow

Step 1:
Generate antenna dataset.

Step 2:
Train Random Forest Regressor.

Step 3:
Save trained model.

Step 4:
Provide frequency input.

Step 5:
Predict antenna dimensions.

---

Project Architecture

Frequency Input
↓
Dataset Generation
↓
Machine Learning Training
↓
Random Forest Model
↓
Dimension Prediction
↓
User Interface

---

Features

- Automated antenna dimension prediction
- Frequency-based inverse design
- Machine learning powered
- Scalable architecture
- Easy future extension

---

Current Limitations

Current version assumes:

- FR4 substrate
- Fixed dielectric constant
- Fixed substrate thickness

Therefore, each frequency corresponds to one standard antenna configuration.

---

Future Scope

Future versions can include:

- Multiple substrate materials
- Variable dielectric constants
- Variable substrate heights
- Gain optimization
- Bandwidth optimization
- Feed point prediction
- CST simulation integration
- Deep learning-based inverse design
- Automated antenna layout generation

---

Conclusion

This project demonstrates the application of Machine Learning in antenna engineering. By learning from antenna design data, the model predicts antenna dimensions directly from operating frequency, reducing design time and providing a foundation for advanced AI-assisted antenna design systems.
