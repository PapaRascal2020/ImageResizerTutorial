# Import python libraries
import glob
import os
from PIL import Image

# Get Script Path
scriptPath = os.path.dirname(os.path.realpath(__file__))

# Set config
maxDimensions = [1980, 1400]
megaPixelLimit = 4.0
imageExtensions = ['gif', 'jpg', 'png']
inputDirectory = scriptPath+"/input"
outputDirectory = scriptPath+"/output"
totalImages = 0
imagesResized = 0

# Look in the inputDirectory for images
imagesToResize = []

for imageExtension in imageExtensions:
	imagesToResize.extend(glob.glob(inputDirectory+"/*.{imageExtension}".format(imageExtension=imageExtension)))

print ("""
*****************************
Image Resize Tutorial
*****************************
""");

totalImages = len(imagesToResize)

if(totalImages >= 1):

	for image in imagesToResize:

		filename = os.path.basename(image)

		print ("Checking: {filename}".format(filename=filename))
		
		file = Image.open(image)
		width, height = file.size

		aspectRatio = float(width)/float(height);
		megaPixels = (float(width)*float(height)) / 1000000;

		if megaPixels > megaPixelLimit:
			file.thumbnail(maxDimensions)
			file.save(outputDirectory+"/{filename}".format(filename=filename))
			imagesResized += 1;

	print("\nFinished, Processed {totalImages} files, Resized {imagesResized} files. END\n".format(totalImages=totalImages, imagesResized=imagesResized))

else:
	print("No images to process. END\n")
