from PIL import Image
import numpy as np


def apply_filter(image):
    for x in range(0, width-filter_size+1, filter_size):
        for y in range(0, height-filter_size+1, filter_size):
            filter = image[x:x+filter_size, y:y+filter_size]
            average = np.average(filter)
            average = int(average//step_size) * step_size
            filter.fill(average)


def crop(image):
    cropped_width = (width//filter_size) * filter_size
    cropped_height = (height//filter_size) * filter_size
    return image[:cropped_width, :cropped_height]


input_path = "img2.jpg"
output_path = "res.jpg"
filter_size = 10
step_count = 5
step_size = 256 / step_count

input_image = Image.open(input_path)
image = np.array(input_image)
width, height, _ = image.shape

image = crop(image)
apply_filter(image)

result_image = Image.fromarray(image)
result_image.save(output_path)
