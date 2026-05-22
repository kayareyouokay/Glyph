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


def to_brightness(r, g, b, method='average'):
    if method == 'average':
        return (r + g + b) / 3
    elif method == 'minmax':
        return (max(r, g, b) + min(r, g, b)) / 2
    elif method == 'luminosity':
        # magic number from the luminosity formula
        return 0.21 * r + 0.72 * g + 0.07 * b
    return (r + g + b) / 3


def to_ascii(brightness):
    idx = int(brightness / 255 * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[idx]


def render(pixels):
    for row in pixels:
        line = ''
        for (r, g, b) in row:
            b_val = to_brightness(r, g, b)
            # triple each char to fix aspect ratio — terminals are ~2:1 tall
            line += to_ascii(b_val) * 3
        print(line)


if __name__ == '__main__':
    img = load_image(sys.argv[1])
    pixels = get_pixels(img)
    render(pixels)
