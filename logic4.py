import base64

def toImg(encoded_data,output_path):
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(encoded_data))