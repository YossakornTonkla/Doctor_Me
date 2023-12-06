import requests
import json
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

def ocr_space_file(filename, overlay=False, api_key='K81865024888957', language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'OCREngine': 2
               }
    with open(filename, 'rb') as f:

        r = requests.post('https://api.ocr.space/parse/image', files={filename: f}, data=payload)
        
    return  json.loads(r.content.decode())


def manual_crop_page_1(image_path, output_path, col): 
    # Open the image file
    img = Image.open(image_path)
    if col == 1:
      left = 660
      top = 110
      right = 815
      bottom = 800
    # Crop the image to the specified region
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)

    img_bytes = io.BytesIO()
    cropped_img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return img_bytes








@app.post("/crop-image1/")
async def crop_image(col: int, file: UploadFile = File(...)):
    output_path = f"output_1{file.filename}"
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    manual_crop_page_1(file.filename, output_path, col)

    return {"message": "Image cropped successfully", "output_path": output_path}

    cropped_img_bytes = manual_crop_page_1(random_filename, col)
    return FileResponse(cropped_img_bytes, media_type="image/png", filename="cropped_image.png")



def manual_crop_page_2(image_path, output_path, col): # edit by jr
    # Open the image file
    img = Image.open(image_path)
    if col == 1:
      left = 660
      top = 200
      right = 850
      bottom = 850
    # Crop the image to the specified region
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)





@app.post("/crop-image2/")
async def crop_image(col: int, file: UploadFile = File(...)):
    output_path = f"output_2{file.filename}"
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    manual_crop_page_2(file.filename, output_path, col)

    return {"message": "Image cropped successfully", "output_path": output_path}





def manual_crop_page_2_2(image_path, output_path, col): # edit by jr
    # Open the image file
    img = Image.open(image_path)
    if col == 1:
      left = 800
      top = 200
      right = 980
      bottom = 850
    # Crop the image to the specified region
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)

@app.post("/crop-image2.2/")
async def crop_image(col: int, file: UploadFile = File(...)):
    output_path = f"output_2.2{file.filename}"
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    manual_crop_page_2_2(file.filename, output_path, col)

    return {"message": "Image cropped successfully", "output_path": output_path}






def manual_crop_page_3(image_path, output_path, col): # edit by jr
    # Open the image file
    img = Image.open(image_path)
    if col == 1:
      left = 700
      top = 100
      right = 950
      bottom = 600
    # Crop the image to the specified region
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)


@app.post("/crop-image3/")
async def crop_image(col: int, file: UploadFile = File(...)):
    output_path = f"output_3{file.filename}"
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    manual_crop_page_3(file.filename, output_path, col)

    return {"message": "Image cropped successfully", "output_path": output_path}






def manual_crop_page_4(image_path, output_path, col): # edit by jr
    # Open the image file
    img = Image.open(image_path)
    if col == 1:
      left = 840
      top = 110
      right = 1000
      bottom = 1400
    # Crop the image to the specified region
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)


@app.post("/crop-image4/")
async def crop_image(col: int, file: UploadFile = File(...)):
    output_path = f"output_4{file.filename}"
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    manual_crop_page_4(file.filename, output_path, col)

    return {"message": "Image cropped successfully", "output_path": output_path}





def manual_crop_page_5(image_path, output_path, col): # edit by jr
    # Open the image file
    img = Image.open(image_path)
    if col == 1:
      left = 750
      top = 570
      right = 1000
      bottom = 750
    # Crop the image to the specified region
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)


@app.post("/crop-image5/")
async def crop_image(col: int, file: UploadFile = File(...)):
    output_path = f"output_5{file.filename}"
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    manual_crop_page_5(file.filename, output_path, col)

    return {"message": "Image cropped successfully", "output_path": output_path}





