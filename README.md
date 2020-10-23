# Simple_Image_converter
Made this simple image coonverter in python. will be adding more futures, right now it convters .webp to .jpg

This script when running is monitoring a folder with watchdog. This script looks for files with the extension .webp and will converter it .jpg, Then move the .jpg files to a new folder and delete thew .webp files. 
Issues:1
The .jpg files are not move to a new folder with using shutil.
 I notice the debugger skips over “shutil.move(FOLDER_PATH1, file, DEST_PATH)”
Error/ issue  constant.cpython-38.pyc
