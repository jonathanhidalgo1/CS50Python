from PIL import Image, ImageOps
import sys

images = []
try:
    if len(sys.argv) > 3:
        print("too many arguments")
        sys.exit
    elif ".jpg" not in sys.argv[1:] or ".png" not in sys.argv[1:]:
        print("not png or jpeg")
        sys.exit
    else:
        for arg in sys.argv[1:]:
            image = Image.open(arg)
            images.append(image)


        images[0] = ImageOps.fit(images[0], (600, 600), method = 1,
                        bleed = 0.0, centering =(0.5, 0.5))
        images[0].paste(images[1], (0,0), images[1])
        images[0].save("teste2.png")

except FileNotFoundError:
    print("file not found")
    
except IndexError:
    print("too few arguments")