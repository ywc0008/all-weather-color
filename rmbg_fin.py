import io
import os
import requests
from rembg import remove

input_path = '4.jpg'
output_path = '4_rb.jpg'

if not os.path.exists(input_path):
    print(f'Input image not found: {input_path}')
    exit()

with open(input_path, 'rb') as f:
    input_data = f.read()

output_data = remove(input_data)

with open(output_path, 'wb') as f:
    f.write(output_data)

print(f'Output image saved: {output_path}')