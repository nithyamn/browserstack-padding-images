import os
from PIL import Image
  

directory = '/FilePath/Test Images/'
store_pad_dir='/FilePath/Output Images/'
rot_pad_dir='/FilePath/Rotated Images/'



# Normal image padding value (no rotation)
right = 10
left = 10
top = 10
bottom = 10

# Rotated image padding value - 70 for android iOS - right-1000, left-1000, top-120, bottom-120
#ios
rot_right=1000
rot_left=1000
rot_top=120
rot_bottom=120

#android
# rot_right=70
# rot_left=70
# rot_top=70
# rot_bottom=70

# Deg to be rotated (multiples of 90 only)
# deg_to_rotate=90 
deg_to_rotate=90

#270 for android and 90 for iOS


for filename in os.listdir(directory):
    # Open the image
    im = Image.open(directory + filename)
    resized_image = im.resize((1474, 1058)) #resizing all images to have uniform padding - this was the ideal image size based on the findings from multiple iteration
    #(1474, 1058), (1080, 920)
    resized_image.save(directory + filename)

    width, height = resized_image.size
    new_width = width + right + left
    new_height = height + top + bottom
    

    
    # Add the padding
    result = Image.new(resized_image.mode, (new_width, new_height), (255, 255, 255))
    result.paste(resized_image, (left,top))
    
    # Save the padded image as JPG
    result.save(store_pad_dir + filename.split(".")[0] + "_padded.png", "PNG")

    # Rotate Image
    rot_vals = {0: None, 90: Image.ROTATE_90, 180: Image.ROTATE_180,
                    270: Image.ROTATE_270, 360:None}

    rotated_image = resized_image.transpose(rot_vals[deg_to_rotate])

    # Add Padding to rotated image
    rot_width, rot_height = rotated_image.size
    rot_new_width = rot_width + rot_right + rot_left
    rot_new_height = rot_height + rot_top + rot_bottom
    rot_result = Image.new(rotated_image.mode, (rot_new_width, rot_new_height), (255, 255, 255))
    rot_result.paste(rotated_image, (rot_left,rot_top))

    #Save rotated and padded image
    rot_result.save(rot_pad_dir + filename.split(".")[0] + "_rot_padded.png", "PNG")
