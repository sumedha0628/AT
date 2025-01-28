import pytesseract
from PIL import Image

#doing the preprocessing
def preprocessing_img(image_path):
    image= Image.open(image_path)
    image= Image.convert("L") 
    return image

#extracting the text
def extract(image):
    text= pytesseract.image_to_string(image)
    return text

#saving and display
def save(text, file_path="output.txt"):
    with open(file_path, "w", encoding="utf-8") as file :
      file.write(str(text))

    
    
#TTS
import pyttsx3

def tts(text):
    engine= pyttsx3.init(text)
    engine.say(text)
    engine.runAndWait()

#running
def main():
    image_path= input("Please enter the image path")
    image= preprocessing_img(image_path)
    text= extract(image)
    tts(text)
    
main()

