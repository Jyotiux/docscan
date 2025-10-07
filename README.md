# Custom Document Scanner Web App

A **web-based document scanner** built with **FastAPI** and **OpenCV** that allows users to upload images and apply **customizable image effects**. Users can preview the processed document and download it.

---

## **Features**

- Upload images of documents (JPEG, PNG, etc.)
- Apply customizable effects:
  - **Grayscale**
  - **Sepia**
  - **Invert / Negative**
  - **Sketch / Pencil**
  - **Threshold / Binarize**
- Adjust **contrast** and **brightness** dynamically
- Preview processed image in browser
- Download the processed document
- Fully modular and easy to extend with more effects

---

## **Folder Structure**

```

docscanner/
│
├─ app.py                  # FastAPI main application
├─ requirements.txt        # Python dependencies
│
├─ scanner/                # Image processing module
│   ├─ __init__.py
│   └─ preprocess.py       # Effects and customization logic
│
├─ static/                 # Static files
│   └─ processed.jpg       # Output file
│
└─ templates/              # HTML templates
└─ index.html          # Upload form, preview, download button

````

---

## **Installation**

1. Clone the repository:

```bash
git clone <repository-url>
cd docscanner
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## **Usage**

1. Start the FastAPI server:

```bash
uvicorn app:app --reload
```

2. Open a browser and navigate to:

```
http://127.0.0.1:8000/
```

3. Upload your document, select an effect, adjust **contrast** and **brightness**, then click **Process Document**.
4. Preview the processed document and download it using the **Download button**.

---

## **Technologies Used**

* **Python 3.x**
* **FastAPI** - Backend API and web server
* **OpenCV** - Image processing
* **Jinja2** - HTML templating
* **Python-Multipart** - Handling file uploads
* **NumPy** - Image array manipulations

---

## **Future Enhancements**

* Add **OCR (text extraction)** for scanned documents
* Real-time preview with sliders for effect, contrast, and brightness
* Multi-page PDF export
* Mobile-friendly responsive design


---

