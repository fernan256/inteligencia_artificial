from PIL import Image, ImageOps

def get_pixels(images):
    img = Image.open(images) # 'images/1A4353.jpg'


    im2 = ImageOps.grayscale(img)

    pixel = list(im2.getdata())

    res = []
    # res.append(1)

    for elem in pixel:
        result = elem / 1000
        res.append(result)
    #print(f"f: {res}")

    # print(len(res))

    return res

# get_pixels('images/2B4698.jpg')
