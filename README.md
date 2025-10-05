# 🧠 AI-Assisted Image Restoration of Ancient Manuscripts  
**Repository Name:** `dip_manuscript_restoration`

---

## 📜 Project Summary

**AI-Assisted Image Restoration of Ancient Manuscripts** integrates **Digital Image Processing (DIP)** and **Generative Adversarial Networks (GANs)** for the digital preservation of degraded historical texts.  
The project’s core contribution is a **two-stage restoration framework** combining classical image enhancement (DIP) and deep learning restoration (DE-GAN).

The DIP phase ensures **pixel-level control** and clarity enhancement, while the AI model performs **context-aware restoration** of faded or stained text regions.  
Together, they form a hybrid pipeline capable of generating **high-contrast, machine-readable manuscripts** for archiving and OCR digitization.

---

## 🎯 1. Objective and Problem Justification

| Focus | Rationale |
|-------|------------|
| **Preservation Need** | Historical documents suffer from ink fading, stains, and uneven illumination, resulting in information loss during digitization. |
| **Project Goal** | To create a hybrid restoration pipeline that combines traditional DIP precision with the contextual intelligence of AI models. |
| **OCR Readiness** | Enhanced binarization improves the accuracy of OCR (Optical Character Recognition) engines by producing clean text-background separation. |
| **Research Significance** | Demonstrates how AI and classical DIP can be combined for cultural heritage conservation. |

---

## ⚙️ 2. Technical Core: Dual-Phase Restoration Pipeline

| **Pipeline Stage** | **Method Implemented** | **Technical Justification** |
|--------------------|------------------------|-----------------------------|
| **Noise Reduction** | Gaussian / Median Filtering | Removes background noise and uneven illumination while preserving text edges. |
| **Contrast Enhancement** | CLAHE (Adaptive Histogram Equalization) | Expands local contrast to reveal faded ink patterns. |
| **Thresholding** | Adaptive & Otsu Methods | Converts grayscale images into clean binary text using dynamic region-based thresholds. |
| **Morphological Refinement** | Opening / Closing | Repairs fragmented strokes and fills small voids in letter structures. |
| **AI Restoration (DE-GAN)** | Deep GAN-based Restoration Network | Learns contextual structure of text to recover missing or smeared regions using adversarial and pixel-level loss. |

---

## 🔬 3. Comparative Analysis and Findings

### 🧩 Successes of the DIP Stage
| **Success Area** | **Observation** | **Technical Implication** |
|------------------|-----------------|----------------------------|
| **Noise Mitigation** | Spatial filtering successfully removed stains and dust artifacts. | Confirms DIP’s role in producing stable, noise-free GAN inputs. |
| **Contrast Recovery** | CLAHE enhanced faded characters and localized uneven background illumination. | Proves local contrast equalization helps preserve text detail before binarization. |
| **Baseline Effectiveness** | Otsu thresholding performed well on uniformly degraded regions. | Validates the theoretical foundation of statistical thresholding. |

### ⚠️ Limitations of DIP Alone
| **Failure Mode** | **Observation** | **Justification for AI Integration** |
|------------------|-----------------|--------------------------------------|
| **Severe Ink Bleed & Stains** | Traditional thresholding classifies large stains as text. | GAN learns semantic text structure and corrects misclassification. |
| **Uneven Illumination** | Global thresholds fail in locally shaded areas. | AI adapts to local context via learned features. |
| **Text Fragmentation** | Thin or faint characters often break during morphological cleanup. | GAN reconstructs natural stroke patterns using learned texture priors. |

---

## 🧱 4. Implementation Architecture

Input Image
↓
[DIP Preprocessing: Filtering + CLAHE + Thresholding]
↓
Preprocessed Image
↓
[AI Restoration (DE-GAN)]
↓
Restored Output (Binarized Manuscript)

---


**Core Components:**
- **DIP Pipeline:** Implemented using OpenCV and scikit-image.  
- **AI Model:** DE-GAN Generator (U-Net-based) trained on H-DIBCO dataset.  
- **Evaluation Metrics:** Structural Similarity Index (SSIM), PSNR.  

---

## 🧠 5. Project Highlights

- Combines **traditional DIP** and **modern AI** methods for document enhancement.  
- Provides a reproducible workflow for **image-to-image restoration**.  
- Demonstrates improvement in **text readability** and **visual clarity**.  
- Supports **cultural heritage digitization and preservation efforts**.  

---

## 📚 6. References

1. Dali, A., & Benouareth, A. (2020). *DE-GAN: Document Enhancement using Generative Adversarial Networks.* [GitHub](https://github.com/dali92002/DE-GAN)  
2. Ntirogiannis, K., Gatos, B., & Pratikakis, I. (2016). *ICDAR 2016 Handwritten Document Image Binarization Contest (H-DIBCO 2016).* [Dataset](https://vc.ee.duth.gr/h-dibco2016/benchmark/)  
3. Goodfellow, I. et al. (2014). *Generative Adversarial Nets.* [Paper](https://arxiv.org/abs/1406.2661)  
4. Ronneberger, O. et al. (2015). *U-Net: Convolutional Networks for Biomedical Image Segmentation.* [Paper](https://arxiv.org/abs/1505.04597)  
5. Gatos, B., Pratikakis, I., & Perantonis, S. J. (2006). *Adaptive Degraded Document Image Binarization.* *Pattern Recognition, 39(3), 317–327.*  

---

✅ **How to use it:**
1. Copy everything above into a file named `README.md`.  
2. Place it in your project root (same level as `inference.py`).  
3. Commit and push to GitHub — it will render perfectly with all sections formatted.  

---


