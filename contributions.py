import sys
import subprocess
import os
from datetime import datetime
#There are two authors with the same email address in my repository,
#so it'd print ngoc.tran@hope.edu twice

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

contriDict ={

}
while True:
        #Get the author info
    arr = list(filter(None, info.split("\n")))
    authorInfo = list(filter(None, arr[2].split()))

    authorEmail = authorInfo[2][1:-1]

    timeCommit = authorInfo[3] 

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
    timeFormat = datetime.utcfromtimestamp(int(timeCommit)).strftime('%B %d, %Y')

    try:
        contriDict[authorEmail][0] +=1 #count the number of commits
        contriDict[authorEmail][1] = timeFormat #if the author was in the dict, increase the # of commits and record new date,
                                                #by the end, this is the date of the oldest commit
    except:
        contriDict[authorEmail] = [1, '',timeFormat] #if never recorded that author, create new entry in the dict
                                                    # the date of th most recent commit recorded

    if 'parent' not in info:
        break    
    #get the parent sha
    parentSha = arr[1][7:]
    cmd = ('git', 'cat-file','-p',parentSha) 
    process = subprocess.run(cmd, capture_output=True, text=True)

    info = process.stdout

for contri in contriDict:
    print(contri + ', ' + str(contriDict[contri][0]) +', ' + contriDict[contri][1] +', ' + contriDict[contri][2])




