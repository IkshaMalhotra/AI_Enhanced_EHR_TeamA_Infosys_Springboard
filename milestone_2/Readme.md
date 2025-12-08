# **Milestone 2 — Medical Image Enhancement**

Milestone 2 focuses on enhancing the visual quality of medical images collected in Milestone 1 using both AI-based and classical image processing techniques. The goal is to enhance clinical readability by correcting common quality issues such as noise, blur, low contrast, and poor resolution.

This milestone prepares the imaging data for accurate downstream tasks including:

* AI-assisted diagnosis
* Automated clinical documentation
* ICD-10 code prediction
* Decision support systems

The enhancement process ensures that medical images are visually optimized without compromising important diagnostic features.

---

## **Objective of Milestone 2**

The primary objectives of this milestone are:

* To understand real-world medical image quality issues
* To apply suitable AI-based and image processing techniques
* To generate before-and-after enhancement comparisons
* To analyze how enhancement improves clinical interpretability
* To prepare enhanced images for ICD-10 automation and AI training

---

## **Image Selection Criteria**

A subset of **20–30 medical images** was selected from the structured dataset created in Milestone 1 based on the following criteria:

* Low brightness
* Low contrast
* Presence of noise
* Blur and poor edge clarity
* Uneven illumination
* Low resolution

For consistency, images were selected across specific **modalities and body regions**, including:

* X-ray images
* Bone scan images

---

## **Image Quality Issue Analysis**

Each selected image was manually analyzed to identify the following problems:

* Gaussian and salt-and-pepper noise
* Poor contrast affecting visibility of structures
* Blurred anatomical boundaries
* Low spatial resolution
* Uneven lighting

These observations guided the selection of appropriate enhancement techniques.

---

## **Enhancement Techniques Applied**

The following enhancement methods were applied using **Python and OpenCV**:

### **1. Noise Reduction**

* **Median Filtering**
* Used to remove salt-and-pepper noise while preserving edges.

### **2. Sharpening**

* **Laplacian Sharpening**
* Enhances edges and fine anatomical details.

### **3. Contrast Enhancement**

* **CLAHE (Contrast Limited Adaptive Histogram Equalization)**
* Improves visibility in low-contrast X-ray and bone scan images.

### **4. Resolution Enhancement (Super Resolution)**

* **Bicubic Interpolation**
* Improves spatial resolution and image clarity.

### **5. Standardization**

* All images were resized to a **single uniform resolution** for consistency across the dataset.

---

## **Modality-wise Enhancements Performed**

| Modality       | Techniques Applied                            |
| -------------- | --------------------------------------------- |
| X-ray          | CLAHE, Laplacian Sharpening                   |
| Bone Scan      | Median Filtering, CLAHE, Laplacian Sharpening, Bicubic Interpolation (Super Resolution)      |

---

## **Before and After Comparison Generation**

For every enhanced image:

* A **side-by-side comparison** was created
* The **original image** was placed next to the **enhanced version**
* These comparisons visually demonstrate:

  * Noise suppression
  * Improved contrast
  * Sharper anatomical boundaries
  * Enhanced resolution

This allows easy evaluation of enhancement effectiveness.

---

## **Clinical Impact of Image Enhancement**

The applied enhancements directly support clinicians by:

* Improving visibility of anatomical structures
* Reducing visual fatigue during interpretation
* Supporting accurate diagnosis
* Improving clarity for automated report generation
* Enabling more reliable ICD-10 prediction

Each enhancement step was chosen specifically to improve **diagnostic confidence and interpretability**.

---

## **Tools & Technologies Used**

* **Python**
* **OpenCV**
* **Image Processing Filters**
* **Super Resolution Techniques**
* **AI-based Enhancement Concepts**

(Exploration of PyTorch, TensorFlow, and Azure OpenAI Vision APIs is recommended for future extension.)

---

## **Workflow Summary**

1. Selection of low-quality medical images
2. Manual quality issue analysis
3. Application of 2–3 enhancement techniques per image
4. Generation of side-by-side comparison images
5. Documentation of enhancement logic
6. Upload to GitHub with structured folders

---

## **Milestone 2 Summary**

* 20–30 medical images selected and enhanced
* Multiple enhancement techniques applied
* Visual comparison generated
* Clinical relevance documented
* Images prepared for:

  * Automated documentation
  * ICD-10 mapping
  * AI-based diagnosis models
* Strong foundation created for future automation and predictive modeling
