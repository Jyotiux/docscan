from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import shutil, os, uuid
from scanner import preprocess
import cv2

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists

@app.get("/")
def home(request: Request):
    """
    Render the homepage with upload form.
    """
    return templates.TemplateResponse("index.html", {"request": request, "processed_image": None})

@app.post("/scan/")
async def scan(
    request: Request,
    file: UploadFile = File(...),
    effect: str = Form("grayscale"),
    contrast: float = Form(1.0),
    brightness: int = Form(0)
):
    """
    Handle uploaded image, apply chosen effect, and return processed image.
    """

    # Validate file type
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return {"error": "Invalid file type. Upload PNG or JPG images."}

    # Save uploaded file with a unique name to avoid overwriting
    unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        return {"error": f"Failed to save file: {str(e)}"}

    # Load image
    img = preprocess.load_image(file_path)
    if img is None:
        return {"error": "Failed to read uploaded image."}

    # Apply chosen effect
    try:
        if effect == "grayscale":
            processed = preprocess.to_gray(img, contrast, brightness)
        elif effect == "sepia":
            processed = preprocess.to_sepia(img, contrast, brightness)
        elif effect == "invert":
            processed = preprocess.invert_image(img, contrast, brightness)
        elif effect == "sketch":
            processed = preprocess.sketch_image(img, contrast, brightness)
        elif effect == "threshold":
            processed = preprocess.threshold_image(img, contrast, brightness)
        else:
            processed = preprocess.to_gray(img, contrast, brightness)
    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}

    # Save processed image
    output_filename = f"processed_{uuid.uuid4().hex}.jpg"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)
    cv2.imwrite(output_path, processed)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "processed_image": f"/static/{output_filename}"}
    )
