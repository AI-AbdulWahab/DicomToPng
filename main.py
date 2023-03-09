import pydicom
import os
import numpy as np
from PIL import Image
def Dicom_to_Img(Path):
    img = pydicom.dcmread(Path)
    # Instance_Number = int(img.get(0x00200013).value)  # Get actual slice instance number from tag (0020, 0013)
    image = img.pixel_array.astype(float)
    rescale_image = (np.maximum(image, 0) / image.max()) * 255
    rescale_image=255-rescale_image
    int_image = np.uint8(rescale_image)
    final_image = Image.fromarray(int_image)
    return final_image  #,Instance_Number
    # final_image.show()
    # final_image.save('472.png')


def image_dispatcher():
    fetch_path = os.listdir('./Data/')
    for dcms in fetch_path:
        Output_Img = Dicom_to_Img("./Data/"+dcms)
        Output_Img.save('./PNG'+"/"+os.path.splitext(dcms)[0]+ '.png')
image_dispatcher()