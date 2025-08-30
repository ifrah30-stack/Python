# Image processing and manipulation
from PIL import Image, ImageFilter, ImageEnhance
import os

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.original = self.image.copy()
    
    def show_info(self):
        print(f"Format: {self.image.format}")
        print(f"Size: {self.image.size}")
        print(f"Mode: {self.image.mode}")
    
    def resize(self, width, height):
        return self.image.resize((width, height), Image.Resampling.LANCZOS)
    
    def apply_filter(self, filter_name):
        filters = {
            'blur': ImageFilter.BLUR,
            'contour': ImageFilter.CONTOUR,
            'detail': ImageFilter.DETAIL,
            'edge_enhance': ImageFilter.EDGE_ENHANCE,
            'emboss': ImageFilter.EMBOSS,
            'sharpen': ImageFilter.SHARPEN,
            'smooth': ImageFilter.SMOOTH
        }
        
        if filter_name in filters:
            return self.image.filter(filters[filter_name])
        return self.image
    
    def adjust_brightness(self, factor):
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(factor)
    
    def adjust_contrast(self, factor):
        enhancer = ImageEnhance.Contrast(self.image)
        return enhancer.enhance(factor)
    
    def convert_to_grayscale(self):
        return self.image.convert('L')
    
    def save_image(self, output_path, format='JPEG'):
        self.image.save(output_path, format=format)
        print(f"Image saved to {output_path}")
    
    def create_thumbnail(self, size=(128, 128)):
        self.image.thumbnail(size)
        return self.image

# Usage example (uncomment to use)
# processor = ImageProcessor('input.jpg')
# processor.show_info()
# grayscale = processor.convert_to_grayscale()
# grayscale.show()
# processor.save_image('output.jpg')
