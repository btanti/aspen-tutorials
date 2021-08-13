import os

rootdir ='.\\Tutorial Videos'

def renameDirectories():
    for root, dirs, files, in os.walk(rootdir):
        for dir in dirs:
            oldFile = os.path.join(root,dir)
            newFile = os.path.join(root, dir.replace(' ',''))

            num = int(newFile[-1])
            if (num >= 4):
                newFile = newFile.replace(f'{num}',f'{num+1}')

            os.rename(oldFile,newFile)

def renameFiles():
    for root, dirs, files, in os.walk(rootdir):
        for dir in dirs:
            newPath = os.path.join(rootdir,dir)
            for root2, dirs2, files2 in os.walk(newPath):
                for file in files2:
                    num = root2[-1]
                    oldFile = os.path.join(root2, file)
                    newFile = os.path.join(root2, num + file[1:])
                    os.rename(oldFile,newFile)
                

renameFiles()