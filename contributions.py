import sys
import subprocess

#There are two authors with the same email address in my repository,
#so it'd print ngoc.tran@hope.edu twice
cmd = ('git', 'shortlog','-sne','--all') 
process = subprocess.run(cmd, capture_output=True, text=True)

infoList = list(filter(None, process.stdout.split('\n')))
authorArr = []
for info in infoList:
    # print(info)
    eachLine = list(filter(None, info.split()))

    commandD = ('git', 'log', '--author='+eachLine[1], '--reverse')

    processD = subprocess.run(commandD, capture_output=True, text=True)
    date = list(filter(None, processD.stdout.split('\n')))[2]
    breakTheDate1 = list(filter(None, date.split()))

    temp = (eachLine[2][1:-1] + ',', eachLine[0] + ',', breakTheDate1[2], breakTheDate1[3] + ',', breakTheDate1[5] + ',')
 
    commandD = ('git', 'log', '--author='+eachLine[1], '-1')

    processD = subprocess.run(commandD, capture_output=True, text=True)
    date = list(filter(None, processD.stdout.split('\n')))[2]
    breakTheDate = list(filter(None, date.split()))
    print(eachLine[2][1:-1] + ',', eachLine[0] + ',', breakTheDate1[2], breakTheDate1[3] + ',', breakTheDate1[5] + ',', breakTheDate[2], breakTheDate[3] + ',', breakTheDate[5])


