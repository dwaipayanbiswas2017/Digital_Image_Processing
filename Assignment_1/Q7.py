import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS

image = "resources/TestPIC.jpg"

for (tag,value) in Image.open(image)._getexif().items():
	print('%s = %s' % (TAGS.get(tag), value))