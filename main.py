__author__ = 'robbie'
from PIL import Image

# New Image
# im = Image.new("RGB", (512, 512), "white")

def createNoise(imageNamw, newName, procentNoise):
    derp = Image.open("boot.JPG")
    pixels = derp.load()
    width, height = derp.size
    for y in range(height):
        for x in range(width):
            print(pixels[x, y])


def gray(imageName, newName):
    derp = Image.open(imageName)
    pixels = derp.load()
    width, height = derp.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            I = int((r + g + b) / 3)
            pixels[x, y] = (I, I, I)
    derp.save(newName)

def nonContextualSegmentation(imageName, newName, treshold):
    derp = Image.open(imageName)
    pixels = derp.load()
    width, height = derp.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            I = int((r + g + b) / 3)
            if I > treshold:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)
    derp.save(newName)

def regionGrowing(imageName, newName, seeds):
    derp = Image.open(imageName)
    pixels = derp.load()
    width, height = derp.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            I = int((r + g + b) / 3)
            if I > treshold:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)
    derp.save(newName)

#gray("boot.JPG", "grayScale.JPG")
#nonContextualSegmentation("boot.JPG", "nCS.JPG", 129)


def neighborhoodOperation(mask, imageName, newName):
    #print(sum(map(sum, mask)))
    #SUM = sum(map(sum, mask))
    derp = Image.open(imageName)
    pixels = derp.load()
    width, height = derp.size
    # Calculate the new values
    newValues = []
    for eachPixelOperationY in range(height - len(mask) + 1):
        row = []
        for eachPixelOperationX in range(width - len(mask[0]) + 1):
            #operation on a single pixel
            total = 0
            for y in range(len(mask)):
                for x in range(len(mask[0])):
                    total += mask[y][x] * pixels[x + eachPixelOperationX, y + eachPixelOperationY][0]
            row.append(int(total))
        newValues.append(row)
    # Apply the calculated values on the picture
    for y in range(height - 2):
        for x in range(width - 2):
            pixels[x + 1, y + 1] = (newValues[y][x], newValues[y][x], newValues[y][x])
    derp.save(newName)

mask = [
[0.5, 1, 0.5],
[1, -6, 1],
[0.5, 1, 0.5],
]

#neighborhoodOperation(mask, "grayScale.JPG", "neighborhoodOperationD.JPG")

nonContextualSegmentation("neighborhoodOperationD.JPG", "NeiHoodNonContSeg.JPG", 15)