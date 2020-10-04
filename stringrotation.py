def splitnum(string,r):
    splitlist=[string[y-r:y]for y in range(r,len(string)+r,r)]

t=int(input())
for test in range(t):
    newx=list()
    string=input()
    r=int(input())
    return splitnum(string,r)
    for split in splitlist:
        word=split
        newx.append(word[1:]+word[0])
    print("".join(newx))
    

    # newsplits = [splits[::-1] for splits in splitlist]
    # # for splits in splitlist:
    # #      newsplitss = [splits[::-1] for splits in splitlist]
    # print(newsplits)