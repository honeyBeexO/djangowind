import cv2 # type: ignore
import os
import qrcode # type: ignore
import segno
from PIL import Image, ImageDraw,ImageOps
import random

# Define the file path to the QR code image using os.path.join
img1_path = os.path.join('static', 'images', 'qs', 'Q4.png')

import numpy as np # type: ignore
import pyboof as pb # type: ignore

pb.__init_memmap() #Optional
result1 = "DC04FR0500011FE81FE80701FR60TONY/SERGE ROBERT 62PASQUIER 65ID66L90BR0348 67FR68M6CFR MSGE4XLWEK3URUBD6TE3DMXC5OSJ7QFYCQXRICI6M73AANL5ULEJVTGMGNVNTGLDUE6LKEJT4BMGHYHHTL4LZPTLVX7WOBNTG7CEAHQ"
result2 = "DC04FR0500011FE81FE80701FR60TONY/SERGE ROBERT62PASQUIER65ID66L90BR034867FR68M6CFRMSGE4XLWEK3URUBD6TE3DMXC5OSJ7QFYCQXRICI6M73AANL5ULEJVTGMGNVNTGLDUE6LKEJT4BMGHYHHTL4LZPTLVX7WOBNTG7CEAHQ"


class QR_Extractor:
    def __init__(self):
        self.detector = pb.FactoryFiducial(np.uint8).qrcode()
    
    def extract(self, img_path):
        if not os.path.isfile(img_path):
            print('File not found:', img_path)
            return None
        image = pb.load_single_band(img_path, np.uint8)
        self.detector.detect(image)
        qr_codes = []
        for qr in self.detector.detections:
            qr_codes.append({
                'text': qr.message,
                'points': qr.bounds.convert_tuple()
            })
        return qr_codes
# qr_scanner = QR_Extractor()
# output = qr_scanner.extract(img1_path)
# print(output)

from qrcode.image.pil import PilImage # type: ignore
from PIL import Image, ImageDraw # type: ignore
import random
import string
import base64


class SegnoQRGen:
    data = result1
    width, height = 0,0
    back_color=(143, 155, 169)
    
    def __init__(self):
        # Generate the QR code without finder patterns
        data = result1
        qr = segno.make(data, error='H')

        # Save the QR code as an image
        qr.save('qr_code_with_finder_patterns.png')

        # Define the size of the random pattern
        pattern_size = 8

        # Generate the random pattern
        pattern_img = Image.new('RGB', 
                                (pattern_size, pattern_size), 
                                
                            )
        draw = ImageDraw.Draw(pattern_img)
        for _ in range(10):  # Draw random lines to create a pattern
            x1, y1, x2, y2 = random.randint(0, pattern_size), random.randint(0, pattern_size), random.randint(0, pattern_size), random.randint(0, pattern_size)
            draw.line([(x1, y1), (x2, y2)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=1)

        # Open the saved image using PIL
        img = Image.open('qr_code_with_finder_patterns.png')

        # Paste the random pattern over the finder pattern areas
        width, height = img.size
        self.width = width
        self.height = height
        finder_pattern_coords = [(4, 4, 12, 12), (width - 14, 4, width-4, 10), (4, height - 8, 12, height-4)]
        for coord in finder_pattern_coords:
            img.paste(pattern_img.resize((coord[2] - coord[0], coord[3] - coord[1])), coord)
            
        # Save the modified QR code image with the random pattern
        img.save("qr_code_with_random_finder_pattern.png")
        
    def draw_borders(self):
        # Open the image with the random pattern
        img = Image.open('qr_code_with_random_finder_pattern.png')

        # Add borders around the image
        img_with_borders = ImageOps.expand(img, border=2, fill='black')

        # Save the image with borders
        img_with_borders.save("qr_code_with_borders.png")

    def draw_axis_with_ticks(self):
        # Open the image with the random pattern
        img = Image.open('qr_code_with_random_finder_pattern.png')

        # Draw the axis with ticks on the image
        draw = ImageDraw.Draw(img)
        width, height = img.size
        line_width = 1
        tick_width = 1
        
        x_axis_coords =[(4, height // 2), (width - 5, height // 2)]
        y_axis_coords =[(width // 2, 4), (width // 2, height -5)]
        
        left_border_coords = [(4, 4), (4, height - 4)]  # Top Left to Bottom Left
        bottom_border_coords = [(4, height - 4), (width - 4, height - 4)]  # Bottom Left to Bottom Right
        
        draw.line(x_axis_coords, fill="black", width=line_width)
        draw.line(y_axis_coords, fill="black", width=line_width)
        
        # Draw the borders
        draw.line(left_border_coords, fill="black", width=line_width)
        draw.line(bottom_border_coords, fill="black", width=line_width)
        
        # Draw ticks along the x-axis
        for x in range(4, width, 10):
            draw.line([(x, height // 2 - 1), (x, height // 2 + 1)], fill="black", width=tick_width)
        
        # Draw ticks along the y-axis
        for y in range(4, height, 10):
            draw.line([(width // 2 - 2, y), (width // 2 + 2, y)], fill="black", width=tick_width)

        # Save the image with the axis and ticks
        img.save("qr_code_with_axis_and_ticks.png")




gen = SegnoQRGen()
gen.draw_axis_with_ticks()
# gen.draw_borders()



# Generate random bytes for encoding
# data_length = 20  # Length of random data
# data = bytes([random.randint(0, 255) for _ in range(data_length)])

# # Encode the random bytes using Base64 encoding
# base64_data = base64.b64encode(data)

# # Create a QR code instance without finder patterns
# class NoFinderImpl(qrcode.util.OptimalDivisionFinder):
#     def find(self, *args, **kwargs):
#         return []


    
# border_sized = 4
# # Create a QR code instance
# # qr = qrcode.QRCode(
# #     version=1,
# #     error_correction=qrcode.constants.ERROR_CORRECT_L,
# #     box_size=10,
# #     border=1,  # Adjust border size as needed
# # )
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=1,
#     finder_pattern=None,
#     alignment_pattern=None,
#     timing_pattern=None,
#     format_information=None,
#     version_information=None,
#     mask_pattern=None,
#     optimize=0,
#     optimize_rounds=2
#     )


# # Add data to the QR code
# data = "Your QR code data here".encode('utf-8')
# qr.add_data(base64_data)
# qr.make(fit=True)

# # Create an image from the QR code instance with custom background color
# img = qr.make_image(fill_color=(0, 0, 0), back_color=(143, 155, 169))

# # Convert the image to a format compatible with PIL
# img_pil = img._img.convert('RGB')

# # Create a PIL ImageDraw object
# draw = ImageDraw.Draw(img_pil)

# # Draw custom plan axis alignment pattern
# width, height = img_pil.size
# line_width = 5
# draw.line([(0, height // 2), (width, height // 2)], fill="black", width=line_width)
# draw.line([(width // 2, 0), (width // 2, height)], fill="black", width=line_width)

# # Draw ticks along the y-axis
# for y in range(0, height, 10):
#     draw.line([(width // 2 - 5, y), (width // 2 + 5, y)], fill="black", width=3)

# # Draw ticks along the x-axis
# for x in range(0, width, 10):
#     draw.line([(x, height // 2 - 5), (x, height // 2 + 5)], fill="black", width=3)

# # Draw borders from top left to bottom left and from bottom left to bottom right
# draw.line([(0, 0), (0, height)], fill="black", width=line_width)  # Top left to bottom left
# draw.line([(0, height), (width, height)], fill="black", width=8)  # Bottom left to bottom right

# finder_pattern_coords = [(0, 0, 7, 7), (width - 8, 0, width, 7), (0, height - 8, 7, height)]
# # Fill the finder pattern areas with the background color
# for coord in finder_pattern_coords:
#     draw.rectangle(coord, fill=(255, 255, 255))  # Replace (255, 255, 255) with your desired background color
    
# # Save the QR code image with alignment pattern, ticks, and customized borders
# img_pil.save("qr_code_custom_styling.png")



    
