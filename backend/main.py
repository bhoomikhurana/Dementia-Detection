# from fastapi import FastAPI,File,UploadFile,Request
# from fastapi.middleware.cors import CORSMiddleware
# from keras.models import load_model
# from PIL import Image
# import os
# import numpy as np
# import cv2
# import uvicorn
# from werkzeug.utils import secure_filename



# app = FastAPI()

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# model = load_model('ALZHEIMER.h5')

# def get_classname(class_no):
#     if class_no == 0:
#         return "Mild Demented"
#     elif class_no == 1:
#         return "Moderate Demented"
#     elif class_no == 2:
#         return "Non Demented"
#     elif class_no == 3:
#         return "Very Mild Demented"
#     else:
#         return "Cannot be determined"


# def get_results(img_path):
#     image = cv2.imread(img_path)
#     image = Image.fromarray(image, 'RGB')
#     image = image.resize((64, 64))
#     input_img = np.expand_dims(image, axis=0)

#     result = model.predict(input_img)[0][0]

#     return result

# @app.get("/")
# async def root():
#     return {"message":"Hello World"}


# @app.post("/upload")
# async def upload_image(file: UploadFile = File(...)):

#     path = "static/" + secure_filename(file.filename)

#     with open(path,"wb+") as save_file:
#         save_file.write(file.file.read())

#     value = get_results(path)
#     result = get_classname(value)

#     os.remove(path)

#     return {"message":result}

# @app.post("/contact")
# async def feedback(request:Request):
    
#     data = await request.json()

#     path = "feedbacks/" + secure_filename(data.get("email")) + '.txt'

#     with open(path,"w") as file:
#         file.write(f"firstname - {data.get('firstname')}")
#         file.write(f"lastname - {data.get('lastname')}")
#         file.write(f"email - {data.get('email')}")
#         file.write(f"phone - {data.get('phone')}")
#         file.write(f"message - {data.get('message')}")
    

#     return {"message":"Success"}

    
# if __name__ == "__main__":
#     uvicorn.run("main:app",reload=True)
# from fastapi import FastAPI, File, UploadFile, Request
# from fastapi.middleware.cors import CORSMiddleware
# from keras.models import load_model
# from PIL import Image
# import os
# import numpy as np
# import cv2
# import uvicorn
# from werkzeug.utils import secure_filename
# from pymongo import MongoClient

# # Initialize FastAPI app
# app = FastAPI()

# # Configure CORS
# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load the model
# model = load_model('ALZHEIMER.h5')

# # MongoDB Connection
# connection_string = "mongodb+srv://bhoomi:Ember%401206@cluster0.lz56fsb.mongodb.net/"
# client = MongoClient(connection_string)
# db = client['dementia']  # Replace with your database name
# feedback_collection = db['contact']  # Replace with your collection name

# # Helper functions
# def get_classname(class_no):
#     if class_no == 0:
#         return "Mild Demented"
#     elif class_no == 1:
#         return "Moderate Demented"
#     elif class_no == 2:
#         return "Non Demented"
#     elif class_no == 3:
#         return "Very Mild Demented"
#     else:
#         return "Cannot be determined"

# def get_results(img_path):
#     image = cv2.imread(img_path)
#     image = Image.fromarray(image, 'RGB')
#     image = image.resize((64, 64))
#     input_img = np.expand_dims(image, axis=0)

#     result = model.predict(input_img)[0][0]

#     return result

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/upload")
# async def upload_image(file: UploadFile = File(...)):
#     path = "static/" + secure_filename(file.filename)

#     with open(path, "wb+") as save_file:
#         save_file.write(file.file.read())

#     value = get_results(path)
#     result = get_classname(value)

#     os.remove(path)

#     return {"message": result}

# @app.post("/contact")
# async def feedback(request: Request):
#     data = await request.json()

#     # Save feedback to MongoDB
#     feedback_data = {
#         "firstname": data.get("firstname"),
#         "lastname": data.get("lastname"),
#         "email": data.get("email"),
#         "phone": data.get("phone"),
#         "message": data.get("message"),
#     }
    
#     # Insert feedback into the collection
#     feedback_collection.insert_one(feedback_data)

#     return {"message": "Success"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)

# # Ensure to close the MongoDB client connection when the app shuts down.
# @app.on_event("shutdown")
# def shutdown_event():
#     client.close()
# from fastapi import FastAPI, File, UploadFile, Request
# from fastapi.middleware.cors import CORSMiddleware
# from keras.models import load_model
# from PIL import Image
# import os
# import numpy as np
# import cv2
# import uvicorn
# from werkzeug.utils import secure_filename
# from pymongo import MongoClient

# # Initialize FastAPI app
# app = FastAPI()

# # Configure CORS
# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load the model
# model = load_model('ALZHEIMER.h5')

# # MongoDB Connection
# connection_string = "mongodb+srv://bhoomi:Ember%401206@cluster0.lz56fsb.mongodb.net/"
# client = MongoClient(connection_string)
# db = client['dementia']  # Replace with your database name
# feedback_collection = db['contact']  # Replace with your collection name

# # Helper functions
# def get_classname(class_no):
#     class_mapping = {
#         0: "Mild Demented",
#         1: "Moderate Demented",
#         2: "Non Demented",
#         3: "Very Mild Demented"
#     }
#     return class_mapping.get(class_no, "Cannot be determined")

# def get_results(img_path):
#     image = cv2.imread(img_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format
#     image = Image.fromarray(image)
#     image = image.resize((64, 64))  # Resize image to match model input
#     input_img = np.expand_dims(image, axis=0)  # Add batch dimension

#     # Normalize the image if required by your model
#     input_img = input_img / 255.0  # Example normalization

#     result = model.predict(input_img)
#     return np.argmax(result, axis=1)[0]  # Return the class index

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/upload")
# async def upload_image(file: UploadFile = File(...)):
#     path = f"static/{secure_filename(file.filename)}"

#     with open(path, "wb+") as save_file:
#         save_file.write(file.file.read())

#     value = get_results(path)
#     result = get_classname(value)

#     os.remove(path)  # Clean up the saved file

#     return {"message": result}

# @app.post("/contact")
# async def feedback(request: Request):
#     data = await request.json()

#     # Save feedback to MongoDB
#     feedback_data = {
#         "firstname": data.get("firstname"),
#         "lastname": data.get("lastname"),
#         "email": data.get("email"),
#         "phone": data.get("phone"),
#         "message": data.get("message"),
#     }

#     # Insert feedback into the collection
#     feedback_collection.insert_one(feedback_data)

#     return {"message": "Success"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)

# # Ensure to close the MongoDB client connection when the app shuts down.
# @app.on_event("shutdown")
# def shutdown_event():
#     client.close()
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from keras.models import load_model
from PIL import Image
import os
import numpy as np
import cv2
import uvicorn
from werkzeug.utils import secure_filename
from pymongo import MongoClient
import certifi  # Import certifi for SSL certificates

# Set the SSL certificate environment variable
os.environ['SSL_CERT_FILE'] = certifi.where()

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
model = load_model('ALZHEIMER.h5')

# MongoDB Connection
connection_string = "mongodb+srv://bhoomi:Ember%401206@cluster0.lz56fsb.mongodb.net/"
client = MongoClient(connection_string)
db = client['dementia']  # Replace with your database name
feedback_collection = db['contact']  # Replace with your collection name

# Helper functions
def get_classname(class_no):
    class_mapping = {
        0: "Mild Demented",
        1: "Moderate Demented",
        2: "Non Demented",
        3: "Very Mild Demented"
    }
    return class_mapping.get(class_no, "Cannot be determined")

def get_results(img_path):
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format
    image = Image.fromarray(image)
    image = image.resize((64, 64))  # Resize image to match model input
    input_img = np.expand_dims(image, axis=0)  # Add batch dimension

    # Normalize the image if required by your model
    input_img = input_img / 255.0  # Example normalization

    result = model.predict(input_img)
    return np.argmax(result, axis=1)[0]  # Return the class index

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    path = f"static/{secure_filename(file.filename)}"

    with open(path, "wb+") as save_file:
        save_file.write(file.file.read())

    value = get_results(path)
    result = get_classname(value)

    os.remove(path)  # Clean up the saved file

    return {"message": result}

@app.post("/contact")
async def feedback(request: Request):
    data = await request.json()

    # Save feedback to MongoDB
    feedback_data = {
        "firstname": data.get("firstname"),
        "lastname": data.get("lastname"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "message": data.get("message"),
    }

    # Insert feedback into the collection
    feedback_collection.insert_one(feedback_data)

    return {"message": "Success"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# Ensure to close the MongoDB client connection when the app shuts down.
@app.on_event("shutdown")
def shutdown_event():
    client.close()
