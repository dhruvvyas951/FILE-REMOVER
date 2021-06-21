import time, os, shutil

path = input("Enter the folder path to be cleared: ")
date = time.time()
days = 0
seconds = time.time() - (days * 60 * 60)

if os.path.exists(path) == True:
    for root, dirs, files in os.walk(path, topdown = True):
        for name in files:
            os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            if seconds >= ctime:
                os.remove(path)
                print('Deleted the path successfully!')

        for name in dirs:
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime
            if seconds >= ctime:
                shutil.rmtree(path)
                print('Deleted the path successfully!')   