from fastapi import FastAPI ,File , UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware


MODEL = tf.keras.models.load_model("my_model.h5", compile=False)
CLASS_NAME = ["Early Blight", "Late Blight", "Healthy"]


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    img = image.resize((256, 256), Image.Resampling.LANCZOS)
    img = np.array(img)
    return img

@app.get('/ping')
async def ping():
    return "Hello World"

@app.post('/predict')
async def predict(file:UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAME[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }   