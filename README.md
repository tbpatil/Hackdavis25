# VisinEx

[Live App](https://visinex.streamlit.app/)  
[Demo Video](https://www.youtube.com/watch?v=ES_KuHOyD0k&feature=youtu.be)  
[Figma Prototype](https://www.figma.com/proto/UgSEhHk4Uke5XowFps4USm/Untitled?node-id=0-1&t=0tZ3sClDyHPKSfNG-1)

---

## Inspiration

Diabetes is one of the most prevalent chronic disorders, affecting millions in the U.S. alone. Poorly managed blood sugar can damage blood vessels in the eyes, potentially leading to blindness—a condition known as **diabetic retinopathy**.

Early detection is key. **VisinEx** was built to provide low cost, rapid, accessible screening for diabetic retinopathy using machine learning and an intuitive user interface.

---

## Problem Statement

Diabetic retinopathy often goes undiagnosed until it's too late. Access to ophthalmological exams can be limited or expensive. We aimed to create a tool that could empower individuals to screen themselves using just their phone.

---

## What It Does

VisinEx enables users to:
- Upload or capture a **retinal fundus image**
- Get predictions of **diabetic retinopathy severity** (None, Mild, Moderate, Severe, Proliferative)
- Receive **AI-generated explanations and management advice** in patient-friendly language

---

## How We Tackled It

We divided our project into three key components:
1. **ML Model**: ResNet18-based image classifier to predict retinopathy severity
2. **Gemini API**: Generates simple explanations and condition management advice
3. **Streamlit App**: Provides an easy-to-use interface for users

### Hardware Protopye
We desiged a custom-built smartphone fundus camera attachment for smartphones used for retinal imaging:

![Fundus Camera](https://raw.githubusercontent.com/tbpatil/Hackdavis25/main/assets/fundus_camera.jpg)
<img width="900" alt="Screenshot_2024-02-14_at_11 15 30_AM" src="https://github.com/tbpatil/HackDavis25/assets/84110959/bb06c1a6-84fb-4634-b9d7-65fcee27cd72">
<p align="center">
  <img src="assets/fundus_camera.jpg" width="400" alt="Fundus Camera Prototype">
</p>

![Fundus Camera Prototype (Internal)](assets/fundus_camerav2.jpg)
<p align="center">
  <img src="assets/fundus_camerav2.jpg" width="400" alt="Fundus Camera Prototype">
</p>


---

## Tech Stack

- `Python`
- `PyTorch` – ML model (ResNet18 + Transfer Learning)
- `Gemini` – AI-generated health explanations
- `Streamlit` – Web app deployment
- `Figma` – UI/UX design

---

## Contributors

Made with 💙 by the VisinEx team at HackDavis 2025:

- Toniya Patil - [@tbpatil](https://github.com/tbpatil)
- Joselyn Romero - [@Joselyn15](https://github.com/Joselyn15)  
- Abrar Sadikeen - [@AbrarSadikeen](https://github.com/AbrarSadikeen)

