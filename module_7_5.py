import os
import time

directory = 'f:\\_sb'

for root, dirs, files in os.walk(directory):
    print("Directory path: %s" % root)
    print("Directory Names: %s" % dirs)
    print("Files Names: %s" % files)





