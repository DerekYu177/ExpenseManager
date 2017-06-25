import shared

# required for image processing
from PIL import Image as img
from PIL import ImageEnhance as img_enhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = shared.global_constants.PYTESSERACT_LOCATION

def text_from_image(image):
    return pytesseract.image_to_string(
        img.open(shared.global_variables.IMAGE_LOCATION + image)
    )

def enhance(image, enhance_factor, contrast_factor, sharpen_factor):
    # TODO: Does this even work?
    enhanced_image = img_enhance._Enhance(image)
    enhanced_image.enhance(enhance_factor)

    contrasted_image = img_enhance.Contrast(enhanced_image)
    contrasted_image.enhance(contrast_factor)

    sharpened_image = img_enhance.Sharpness(contrasted_image)
    sharpened_image.enhance(sharpen_factor)

    return sharpened_image
