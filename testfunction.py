def countwords():
    file=input('enter the file name')
    numberofwords=0
    f=open(file,'r')
    for line in f:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print('numberofwords:')
    print(numberofwords)
countwords()        