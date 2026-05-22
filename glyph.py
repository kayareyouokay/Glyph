import argparse
from PIL import Image


ASCII_CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def load_image(path):
    img = Image.open(path).convert('RGB')
    print(f'loaded {img.width}x{img.height}')
    return img


def resize_image(img, target_width):
    ratio = img.height / img.width
    new_height = int(target_width * ratio / 2)
    return img.resize((target_width, new_height))


def get_pixels(img):
    # pillow loads top-left origin, iterate rows first
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
    elif method == 'minmax':
        return (max(r, g, b) + min(r, g, b)) / 2
    elif method == 'luminosity':
        # magic number from the luminosity formula
        return 0.21 * r + 0.72 * g + 0.07 * b
    return (r + g + b) / 3


def to_ascii(brightness, invert=False):
    if invert:
        brightness = 255 - brightness
    idx = int(brightness / 255 * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[idx]


def render(pixels, method='average', invert=False, color=False):
    for row in pixels:
        line = ''
        for (r, g, b) in row:
            b_val = to_brightness(r, g, b, method)
            char = to_ascii(b_val, invert) * 3
            if color:
                # ansi truecolor escape: \033[38;2;R;G;Bm
                line += f'\033[38;2;{r};{g};{b}m{char}'
            else:
                line += char
        if color:
            line += '\033[0m'
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert image to ascii art')
    parser.add_argument('image', help='path to image')
    parser.add_argument('--width', type=int, default=120)
    parser.add_argument('--method', choices=['average', 'minmax', 'luminosity'], default='average')
    parser.add_argument('--invert', action='store_true')
    parser.add_argument('--color', action='store_true')
    args = parser.parse_args()

    img = load_image(args.image)
    img = resize_image(img, args.width)
    pixels = get_pixels(img)
    render(pixels, args.method, args.invert, args.color)
