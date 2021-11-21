from PIL import Image
import numpy as np


def discretize(number, step):
    """Дискретизирует значение с данным шагом

    >>> discretize(27, 5)
    25

    >>> discretize(101, 100)
    100
    """
    return int(number//step) * step


def apply_filter(png_image):
    """Проходит по изображению и применяет фильтр к каждой клетке"""
    for x in range(0, width-filter_size+1, filter_size):
        for y in range(0, height-filter_size+1, filter_size):
            filter_cell = png_image[x:x+filter_size, y:y+filter_size]
            average = np.average(filter_cell)
            average = discretize(average, step_size)
            filter_cell.fill(average)


def crop(png_image):
    """Обрезает изображение под размер фильтра"""
    cropped_width = (width//filter_size) * filter_size
    cropped_height = (height//filter_size) * filter_size
    return png_image[:cropped_width, :cropped_height]


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
