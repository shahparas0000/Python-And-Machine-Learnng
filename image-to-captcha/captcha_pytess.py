#Method 1 (Pytesseract)
#Reference - Pytesseract Documentation
#Link - https://pypi.org/project/pytesseract/#:~:text=Python-tesseract%20is%20an%20optical%20character%20recognition%20%28OCR%29%20tool,is%20a%20wrapper%20for%20Google%E2%80%99s%20Tesseract-OCR%20Engine%20.
import pytesseract as pyt
pyt.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import easygui

originalImage=easygui.fileopenbox()
captchaImage = Image.open(originalImage)
text = pyt.image_to_string(captchaImage)
#box = pyt.image_to_boxes(captchaImage)

print(text)
#print(box)
