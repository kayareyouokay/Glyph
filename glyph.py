import argparse
from PIL import Image


ASCII_CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def load_image(path):
    img = Image.open(path).convert('RGB')
    print(f'loaded {img.width}x{img.height}')
    return img


def resize_image(img, target_width):
    # keep aspect ratio — divide height by 2 since chars are ~2x taller than wide
    ratio = img.height / img.width
    new_height = int(target_width * ratio / 2)
    return img.resize((target_width, new_height))


def get_pixels(img):
    pixels = []
    for y in range(img.height):
        row = []
        for x in range(img.width):
            row.append(img.getpixel((x, y)))
        pixels.append(row)
    return pixels


def to_brightness(r, g, b, method='average'):
    if method == 'average':
        return (r + g + b) / 3
    return (r + g + b) / 3


def to_ascii(brightness):
    idx = int(brightness / 255 * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[idx]


def render(pixels):
    for row in pixels:
        line = ''
        for (r, g, b) in row:
            b_val = to_brightness(r, g, b)
            line += to_ascii(b_val) * 3
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert image to ascii art')
    parser.add_argument('image', help='path to image')
    parser.add_argument('--width', type=int, default=120, help='output width in chars')
    args = parser.parse_args()

    img = load_image(args.image)
    img = resize_image(img, args.width)
    pixels = get_pixels(img)
    render(pixels)
