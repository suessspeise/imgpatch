import sys
from PIL import Image
from os import listdir, getcwd, makedirs
from os.path import isfile, join, exists


# working directory
cwd = getcwd()
print("working directory: ", cwd)

# list of files
files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
files = [ f for f in files if f.endswith( ('.JPG','.jpg', 'jpeg') ) ]
print("files used:\n", files, "\n")
# list of images
images = []
for f in files:
	images.append(Image.open(f))

# create new empty image with dimensions as sum of images
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
print("new image dimensions: ", total_width, max_height)
new_im = Image.new('RGB', (total_width, max_height))

#paste together
x_offset = 0
for im in images:
	new_im.paste(im, (x_offset,0))
	x_offset += im.size[0]

# save
# new_im.show()
print("\nsaving image...")
directory = "doppel"
if not exists(directory):
	makedirs(directory)
new_im.save(directory + '/test.jpg')