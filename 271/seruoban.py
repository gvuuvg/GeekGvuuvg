from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def rndColor():
    return random.randint(210, 220), random.randint(114, 116), random.randint(140, 152)
    # return 213,116,152

def rndColor2():
    return random.randint(219, 220), random.randint(115, 116), random.randint(145, 152)
    # return random.randint(150, 160), random.randint(200, 210), random.randint(190, 200)
    # return 159,204,194

def rndChar():
    return chr(random.randint(65, 90))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('ygyxsziti2.0.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# image = image.filter(ImageFilter.BLUR)
image.save('code1.jpg', 'jpeg')
