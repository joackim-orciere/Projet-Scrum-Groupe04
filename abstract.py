def cleanResume(text):
    a=""
    paragraphe=text.split(" ")
    z=len(paragraphe)
    save=""
    for t in range(0,z):
        if('Introduction' in paragraphe[t] or 'introduction' in paragraphe[t] or 'INTRODUCTION' in paragraphe[t]):
            for r in range(0,t):
                save+=paragraphe[r]
                save+=" "
            paragraphe=""
            paragraphe+=save
            paragraphe=save.split(" ")
            z=len(paragraphe)
            break

    if('Abstract' in paragraphe[0] or 'abstract' in paragraphe[0] or 'ABSTRACT' in paragraphe[0]):
        if(len(paragraphe[0])>7):
            for k in range(8,len(paragraphe[0])):
                a+=paragraphe[0][k]
            a+=" "

        for i in range(1,z):
            a+=paragraphe[i]
            a+=" "


        # endVar=len(paragraphe[z-1])
        # print(endVar)
        # if('1' in paragraphe[z-1][endVar-1]):
        #     for f in range(0,endVar-2):
        #          a+=paragraphe[z-1][f]
        # else:
        #      a+=paragraphe[z-1]"

        return a

    for s in range(0,len(paragraphe)):
        a+=paragraphe[s]
        a+=" "
    return a

def getAbstract(text):
    paragraphe=text.split("\n\n")
    a=""
    position1=0
    position2=0
    test1=True
    test2=True
    for m in range(0,len(paragraphe)):

        if(('Abstract' in paragraphe[m] or 'abstract' in paragraphe[m] or 'ABSTRACT' in paragraphe[m]) and (test1==True)):
            position1=m
            test1=False



        if(('Introduction' in paragraphe[m] or 'introduction' in paragraphe[m] or 'INTRODUCTION' in paragraphe[m]) and (test2==True)):
            position2=m
            test2=False




    if(position1!=0 and position2!=0):

        for k in range(position1,position2):
            a+=paragraphe[k]
        return(cleanResume(a))

    if(position1!=0 and position2==0):
        i=position1
        a=""
        a+=paragraphe[i]
        #while(len(paragraphe[i+1])>150):
          #i=i+1
          #a+=paragraphe[i]
        return(cleanResume(a))

    if(position1==0 and position2!=0):
        i=position2
        j=i
        a=""
        while(len(paragraphe[i-1])>300):
          i=i-1
        for k in range(i,j+1):
          a+=paragraphe[k]
        return(cleanResume(a))
    return "FAILED TO RETREIVE ABSTRACT OR INTRODUCTION"
