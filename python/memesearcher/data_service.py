import pytesseract
import cv2
import numpy as np
from PIL import Image, ImageEnhance
from image_text import ImageText

def list_all():
    all_texts = ImageText.objects()
    return all_texts

def recognise_text(img_ref):
    for u in list_all():
        if u.image_ref == img_ref:
            return 
    cv2_image = cv2.imread(img_ref)

    text_without_anything = pytesseract.image_to_string(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB), lang='eng+rus')
    
    enhancer = ImageEnhance.Contrast(Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)))
    
    high_enhance = enhancer.enhance(4)
    text_with_high_enhance = pytesseract.image_to_string(high_enhance, lang='eng+rus')

    low_enhance = enhancer.enhance(0.5)
    text_with_low_enhance = pytesseract.image_to_string(low_enhance, lang='eng+rus')

    gray_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    gray_text = pytesseract.image_to_string(cv2_image, lang='eng+rus')

    lab = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    clahe_image = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
    CLAHE_text = pytesseract.image_to_string(clahe_image, lang='eng+rus')

    thresh, black_and_white_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
    black_and_white_text = pytesseract.image_to_string(black_and_white_image, lang='eng+rus') 

    image_text = ImageText()

    image_text.image_ref = img_ref.lower()
    image_text.text_without_anything = text_without_anything.lower()
    image_text.text_with_low_enhancer = text_with_low_enhance.lower()
    image_text.text_with_high_enhancer = text_with_high_enhance.lower()
    image_text.gray_text = gray_text.lower()
    image_text.text_with_CLAHE = CLAHE_text.lower()
    image_text.only_black_and_white_text = black_and_white_text.lower()

    image_text.save()

    return image_text
