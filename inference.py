import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from models.models import generator_model  # import generator from your models.py

# =========================
# CONFIGURATION
# =========================
input_folder = "input_images"
output_folder = "restored"
preprocessed_folder = "preprocessed"
weights_path = "binarization_generator_weights.h5"
image_size = (256, 256)

os.makedirs(output_folder, exist_ok=True)
os.makedirs(preprocessed_folder, exist_ok=True)

# =========================
# 1. LOAD GENERATOR MODEL
# =========================
print("[INFO] Loading generator model...")
generator = generator_model()
generator.load_weights(weights_path)
print("[INFO] Model weights loaded successfully.\n")

# =========================
# 2. IMAGE PREPROCESSING
# =========================
def preprocess_image(img_path):
    """Apply DIP enhancement before GAN restoration"""
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # 🟢 Step 1: Denoise (Gaussian Blur)
    denoised = cv2.GaussianBlur(img, (5, 5), 0)

    # 🟢 Step 2: Contrast Enhancement (Histogram Equalization)
    enhanced = cv2.equalizeHist(denoised)

    # 🟢 Step 3: Adaptive Threshold (binarization)
    thresh = cv2.adaptiveThreshold(
        enhanced, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    # 🟢 Step 4: Resize for model input
    img_resized = cv2.resize(thresh, (256, 256))
    norm = (img_resized / 127.5) - 1.0

    # 🟢 Step 5: Save preprocessed image in original size
    pre_path = os.path.join(preprocessed_dir, os.path.basename(img_path))
    cv2.imwrite(pre_path, thresh)

    return norm, img, (h, w)


# =========================
# 3. INFERENCE (RESTORATION)
# =========================
def restore_image(image_path):
    """Run inference and resize restored output back to original size"""
    img, (h, w) = preprocess_image(image_path)
    restored = generator.predict(img)[0, :, :, 0]
    restored = (restored * 255).astype(np.uint8)
    restored = cv2.resize(restored, (w, h))  # resize to original dimensions
    return restored


# =========================
# 4. PROCESS ALL IMAGES
# =========================
print("[INFO] Starting inference on all input images...\n")
input_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not input_files:
    print("⚠️ No input images found in 'input_images/' folder.")
else:
    for filename in input_files:
        input_path = os.path.join(input_folder, filename)
        print(f"[INFO] Processing: {filename}")

        restored_img = restore_image(input_path)
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, restored_img)

        # Show side-by-side comparison
        orig = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.imshow(orig, cmap='gray')
        plt.title("Original")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(restored_img, cmap='gray')
        plt.title("Restored / Binarized")
        plt.axis('off')

        plt.show()

    print("\n✅ All images processed and saved in:", output_folder)
