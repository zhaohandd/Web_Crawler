import pytesseract
from PIL import Image

#识别效果并不好，需要手动训练
img = Image.open('yzm.jpg')
code = pytesseract.image_to_string(img)
print(code)