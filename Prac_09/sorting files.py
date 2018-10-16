import os
import shutil
hello=[]
for filename in os.listdir("FilesToSort"):
    temp=filename.split(".")
    hello.append(temp[1])

for exe in hello:
    try:
        os.mkdir("FilesToSort/"+exe)
    except FileExistsError:
        pass
for i in os.listdir("FilesToSort"):
    if
    shutil.move("FilesToSort", )
