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
        script_dir = os.path.dirname(__file__)
        #get the current branch in HEAD
        with open(os.path.join(script_dir, '.git/HEAD')) as f:
            
            currentBranch = list(filter(None, f.readlines()[0].split("/")))[-1][:-1]
        re_path = '.git/refs/heads/' + currentBranch
        abs_file_path = os.path.join(script_dir, re_path)
        with open(abs_file_path) as f: 
            sha1 = f.readlines()[0][0:-1] #get the sha1 of the last commit in .git/refs/heads/currentbranch and exclude the new line character

        #Use git cat-file to get the info of the last commit 
        cmd = ('git', 'cat-file','-p',sha1) 
        process = subprocess.run(cmd, capture_output=True, text=True)

        info = process.stdout

        #Get the author info
        arr = list(filter(None, info.split("\n")))
        authorInfo = list(filter(None, arr[2].split()))

        print('Author:', authorInfo[1], authorInfo[2])
        print("")
        #get the tree sha
        shaCommit = arr[0][5:]
        #get the list of blob sha
        cmd = ('git', 'cat-file','-p',shaCommit) 
        process = subprocess.run(cmd, capture_output=True, text=True)

        infoList = list(filter(None, process.stdout.split("\n")))
        #get the sha associated with the specified file
        fileSha1 = ""
        for info in infoList:
            if info.split()[3] == fileN:
                fileSha1 = list(filter(None,info.split()))[2]
                print("SHA-1 for", fileN, ':',fileSha1)
                break

        print("")   
        #get the content of the file     
        cmd = ('git', 'cat-file','-p',fileSha1) 
        process = subprocess.run(cmd, capture_output=True, text=True)
        print(process.stdout)

else:
    print('File does not exist')