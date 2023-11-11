from fastapi import FastAPI,File,UploadFile,Request
from fastapi.middleware.cors import CORSMiddleware
from keras.models import load_model
from PIL import Image
import os
import numpy as np
import cv2
import uvicorn
from werkzeug.utils import secure_filename



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model('ALZHEIMER.h5')

def get_classname(class_no):
    if class_no == 0:
        return "Mild Demented"
    elif class_no == 1:
        return "Moderate Demented"
    elif class_no == 2:
        return "Non Demented"
    elif class_no == 3:
        return "Very Mild Demented"
    else:
        return "Cannot be determined"


def get_results(img_path):
    image = cv2.imread(img_path)
    image = Image.fromarray(image, 'RGB')
    image = image.resize((64, 64))
    input_img = np.expand_dims(image, axis=0)

    result = model.predict(input_img)[0][0]

    return result

@app.get("/")
async def root():
    return {"message":"Hello World"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    path = "static/" + secure_filename(file.filename)

    with open(path,"wb+") as save_file:
        save_file.write(file.file.read())

    value = get_results(path)
    result = get_classname(value)

    os.remove(path)

    return {"message":result}

@app.post("/contact")
async def feedback(request:Request):
    
    data = await request.json()

    path = "feedbacks/" + secure_filename(data.get("email")) + '.txt'

    with open(path,"w") as file:
        file.write(f"firstname - {data.get('firstname')}")
        file.write(f"lastname - {data.get('lastname')}")
        file.write(f"email - {data.get('email')}")
        file.write(f"phone - {data.get('phone')}")
        file.write(f"message - {data.get('message')}")
    

    return {"message":"Success"}

    
if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)