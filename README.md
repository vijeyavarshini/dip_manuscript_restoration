# dip_manuscript_restoration
# 🧠 AI-Assisted Image Restoration of Ancient Manuscripts

## 📜 Overview
Historical manuscripts and old documents often suffer from **ink fading, stains, and paper degradation**, making them hard to read or digitize.  
This project combines **Digital Image Processing (DIP)** and **Deep Learning (DE-GAN)** to restore and enhance such ancient texts.

By preprocessing with traditional image filters and restoring via a **Generative Adversarial Network (GAN)**,  
the system produces **clean, readable, and preservation-ready** versions of old manuscripts.

---

## 🎯 Objectives
- Preprocess degraded manuscript images using classical DIP enhancement techniques.  
- Restore document quality using the **DE-GAN** deep learning model.  
- Compare classical thresholding vs AI-based restoration.  
- Support **heritage preservation** through automated document cleanup.

---

## 🧩 Project Pipeline

### 1️⃣ DIP Preprocessing
Classical image processing applied before AI-based restoration.

**Steps:**
1. **Noise Removal:** Median / Gaussian filters  
2. **Contrast Enhancement:** CLAHE (Adaptive Histogram Equalization)  
3. **Thresholding:** Otsu / Adaptive thresholding  
4. **Morphological Operations:** Opening / Closing to remove small noise

**Output:** Cleaned preprocessed document ready for restoration.

---

### 2️⃣ AI Restoration (DE-GAN)
Implements a **Document Enhancement GAN (DE-GAN)** model trained to restore degraded documents.

**Reference:** [DE-GAN GitHub Repository](https://github.com/dali92002/DE-GAN)

**Model Highlights:**
- **Generator:** U-Net–like encoder-decoder structure  
- **Discriminator:** Classifies real vs restored patches  
- **Loss Function:** Combination of pixel (L1) and adversarial loss  

**Input:** Preprocessed grayscale document  
**Output:** High-quality restored and binarized image  

---

## 🧱 Implementation Workflow

Input Image
↓
[DIP Preprocessing]
↓
Preprocessed Image
↓
[AI Restoration (DE-GAN)]
↓
Restored Output Image


---

## 💻 Folder Structure

AI_Manuscript_Restoration/
│
├── models/
│ └── models.py # DE-GAN Generator & Discriminator models
├── input_images/ # Original test manuscript images
├── preprocessed/ # DIP preprocessed images
├── restored/ # Final DE-GAN restored outputs
├── inference.py # Script for restoration & saving outputs
├── AI_Manuscript_Restoration.ipynb # Jupyter Notebook (demo + visualization)
├── binarization_generator_weights.h5 # Pretrained DE-GAN generator weights


 ---
