import sys
from PIL import Image


ASCII_CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def load_image(path):
    img = Image.open(path).convert('RGB')
    print(f'loaded {img.width}x{img.height}')
    return img


def get_pixels(img):
    # pillow loads top-left origin, iterate rows first
    pixels = []
    for y in range(img.height):
        row = []
        for x in range(img.width):
            row.append(img.getpixel((x, y)))
        pixels.append(row)
    return pixels


if __name__ == '__main__':
    img = load_image(sys.argv[1])
    pixels = get_pixels(img)
    print(pixels[0][0])
