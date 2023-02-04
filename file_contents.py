import sys
import subprocess
import os
# Main program
# name of the file: tree_sha.py
fileN = sys.argv[1]
if os.path.exists(fileN):
    if os.path.isdir(fileN):
        print(fileN, 'is not a file but a directory')
    else:  
        cmd = ('git', 'log','-n','1', '--',fileN) #use another command
        process = subprocess.run(cmd, capture_output=True, text=True)

        info = process.stdout

        #print(info)

        arr = list(filter(None, info.split("\n")))
        author = arr[1]

        print(author)
        print("")

        shaCommit = arr[0][7:]

        cmd = ('git', 'cat-file','-p',shaCommit) 
        process = subprocess.run(cmd, capture_output=True, text=True)

        shaTree = list(filter(None,process.stdout.split("\n")))[0][5:]
        cmd = ('git', 'cat-file','-p',shaTree) 
        process = subprocess.run(cmd, capture_output=True, text=True)

        infoList = list(filter(None, process.stdout.split("\n")))

        for info in infoList:
            if info.split()[3] == fileN:
                print("SHA-1 for", fileN, list(filter(None,info.split()))[2])
                break

        print("")

        with open(sys.argv[1]) as f:
            lines = f.readlines()


        for line in lines:
            print(line)
else:
    print('File does not exist')