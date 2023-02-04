import sys
import subprocess
import os
#main program:
#SHA-1: 3b54452c683ab37a1b565f0b559f6e26e1df79d9
# cmd = ('git', 'cat-file','-p',sys.argv[1]) #use another command
# process = subprocess.run(cmd, capture_output=True, text=True)

#SHA-1 commit: 3b54452c683ab37a1 - tree_sha.py
#sha1 commit: 7470e0fcaa786087af2849be1 - aFile.txt

fileN = sys.argv[1]
if os.path.exists(fileN):
    if os.path.isdir(fileN):
        print(fileN, 'is not a file but a directory')
    else:

        for argv in sys.argv[2:]:
            # print(argv)
            # cmd = ('git', 'log','--name-only','--',sys.argv[1]) #use another command
            # process = subprocess.run(cmd, capture_output=True, text=True)
            # treeCode = process.stdout.split("\n")
            #cmd = ('git', 'log','--name-only','--',sys.argv[1]) #use another command
            cmd = ('git', 'cat-file', '-t', argv)
            process = subprocess.run(cmd, capture_output=True, text=True)
            cmdType = process.stdout
            if cmdType == '':
                print(argv, 'does not represent a valid Git object')
                break
            if 'blob' in cmdType:
                print(argv, 'is a tree object, not a commit object')
                break
            cmd = ('git', 'cat-file','-p',argv) 
            process = subprocess.run(cmd, capture_output=True, text=True)
            shaTree = process.stdout.split("\n")[0][5:]
            cmd = ('git', 'cat-file','-p',shaTree) 
            process = subprocess.run(cmd, capture_output=True, text=True)

            infoList = list(filter(None, process.stdout.split("\n")))
            isValid = False
            for info in infoList:
                # print(info)
                infoArr = list(filter(None, info.split()))
                # print(infoArr)
                # print(infoArr[0])
                fName = infoArr[3]
                if fName == fileN:
                    isValid = True
                    break
            # print('')

        if not isValid:
            print('False')
        else:
            print('True')
else:
    print('File does not exist')

    