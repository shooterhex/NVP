import cv2
import numpy as np
import os

def transfer_16bit_to_8bit(image_path, output_path):
    image_16bit = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    min_16bit = np.min(image_16bit)
    max_16bit = np.max(image_16bit)
    # image_8bit = np.array(np.rint((255.0 * (image_16bit - min_16bit)) / float(max_16bit - min_16bit)), dtype=np.uint8)
    # 或者下面一种写法
    image_8bit = np.array(np.rint(255 * ((image_16bit - min_16bit) / (max_16bit - min_16bit))), dtype=np.uint8)
    print(image_16bit.dtype)
    print('16bit dynamic range: %d - %d' % (min_16bit, max_16bit))
    print(image_8bit.dtype)
    print('8bit dynamic range: %d - %d' % (np.min(image_8bit), np.max(image_8bit)))
    cv2.imwrite(output_path, image_8bit)

input_folder = './OUTPUT2/'
output_folder = './output_8bit'

for file_name in os.listdir(input_folder):
    if file_name.endswith('.png'):  # 只处理以 .jp2 结尾的文件
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '_8bit.png')

        transfer_16bit_to_8bit(input_path, output_path)