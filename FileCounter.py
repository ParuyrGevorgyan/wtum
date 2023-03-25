import os

def fileCount(directory: str):
    dir_path = directory
    count = 0
    
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
            
    return count