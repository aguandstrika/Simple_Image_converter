import sys
import time
import logging
import glob, os, shutil
from constant import FOLDER_PATH, FOLDER_PATH1, DEST_PATH
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
#constants 

def converter():
    for img in os.listdir(FOLDER_PATH):
        if img.endswith(".webp"):
            for file in glob.glob("*.webp"):
                im = Image.open(file)
                rgb_im =im.convert("RGB")
                rgb_im.save(file.replace("webp", "jpg"), quality=95)
        #print(img)
'''
copying function not working yet 
def copy():
    print("copy def")
    for item in os.listdir(FOLDER_PATH1):
        print("fold dir")
        if not os.path.isfile(item):
            print("is the file here")
            for file in os.listdir(item):
                print(file, "i see")
                #print("listdir")
                if file.endswith(".jpg"):
                    print("files ending in jpg")
                    shutil.move(FOLDER_PATH1, file, DEST_PATH)
                print(file, "i see 2")
'''

'''
#deleting .webp img

this funtion does not work properly
def delete():
    for img in os.listdir(FOLDER_PATH):
        if img.endswith(".webp"):
            os.unlink(FOLDER_PATH + img)
            print("image deleted")
'''

#deleting .webp img


#making functions to display actions 
def on_created(event):
    print("Created")
def on_deleted(event):
    print("Deleted")
def on_modified(event):
    print("Modified")
def on_moved(event):
    print("Moved")

if __name__ == "__main__":

    event_handler = FileSystemEventHandler()
    #calling event handler fuctions 
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved
    #
    #defining path
    path = "C:/Users/black/Desktop/imageconpy"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    # the loop thats watching the folder
    try:
        print("moniroting")
        while True:
            converter()
            copy()  
            time.sleep(4)
            delete()
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
               
        print("bye")
    observer.join()
