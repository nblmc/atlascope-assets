import os
import sys
import shutil
import subprocess



#gets the root directory
rootdir = os.getcwd()

#creates a folder to store index
index_path=os.path.join(rootdir,"Index")
if not os.path.exists(index_path):
    os.makedirs(index_path)


#check to see if plate-index.txt  already exists, and if so remove
if os.path.exists(os.path.join(rootdir, "plate-index.txt")):
    os.remove(os.path.join(rootdir, "plate-index.txt"))
#create tile index input txt file containing path names to all clipped images
with open(os.path.join(rootdir, "plate-index.txt"),"w+") as txt_file:
    for f in os.listdir(rootdir):
        if f.endswith(".tif"):
            txt_file.write(f + "\n")
input = os.path.join(rootdir, "plate-index.txt")
output = os.path.join(index_path, "index.geoJSON")

#create the command to create the tile index
tile_index_command = ("gdaltindex", "-tileindex", "identifier", "-f", "GeoJSON", output, "--optfile", input)
#call the command to create tile index
subprocess.call(tile_index_command)
print('\n')
print("Index created successfully.")
