#!/bin/python
import pdftotext
import glob
import sys
import os
import re

def testLine( line ):
    return re.search( ':|\(|\)|,', line )

def getTitle( txt ):

    txt = txt.split("\n\n")
    # print( re.search(':|(|)|,|', txt[0] ))
    txt = txt[0].split("\n")

    ret = ''

    if( not testLine( txt[0] )):
        ret += txt[0] + " "
    if( len(txt) > 1 and not testLine( txt[1] )):
        ret += txt[1] + " "

    return ret
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

        for i in range(1,z-1):
            a+=paragraphe[i]
            a+=" "


        endVar=len(paragraphe[z-1])
        if('1' in paragraphe[z-1][endVar-1]):
            for f in range(0,endVar-2):
                a+=paragraphe[z-1][f]
        else:
            a+=paragraphe[z-1]

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
    for m in range(0,len(paragraphe)):

        if('Abstract' in paragraphe[m] or 'abstract' in paragraphe[m] or 'ABSTRACT' in paragraphe[m]):
            position1=m


        if('Introduction' in paragraphe[m] or 'introduction' in paragraphe[m] or 'INTRODUCTION' in paragraphe[m]):
            position2=m



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


if( len(sys.argv) <= 1 ):
    print("/!\\ Usage: $./parse directory")
    exit()

dirpath = sys.argv[1]

exist = os.path.isdir( dirpath)
if( not exist ):
    print("/!\\ directory '" + dirpath + "' cannot be found.")
    exit()

if( dirpath[-1:] != '/' ):
    dirpath += '/'

pdf_files = glob.glob( dirpath + '*' );

plainpath = dirpath + 'plainTexts'
abstractpath = dirpath + 'abstractTexts'

if( not os.path.isdir( plainpath )):
    os.mkdir( plainpath );
if( not os.path.isdir( abstractpath )):
    os.mkdir( abstractpath );

for pdf_file in pdf_files :
    if( os.path.splitext( pdf_file )[1] != '.pdf' ): # skip files that not pdf
        continue

    target = plainpath + '/' + os.path.splitext(os.path.basename( pdf_file ))[0] + '.txt'
    abstractTarget = abstractpath + '/' + os.path.splitext(os.path.basename( pdf_file ))[0] + '.txt'


    filename = os.path.splitext(os.path.basename( pdf_file ))[0]

    os.system( 'pdftotext -f 1 -l 1 ' + pdf_file + ' ' + target )


    file = open( target, 'r' );

    string = file.read()

    title = getTitle( string )

    abstract = getAbstract( string )

    file.close()

    file = open( abstractTarget, 'w')
    file.write( filename  )
    file.write( "\n---------\n" )
    file.write( title  )
    file.write( "\n---------\n" )
    file.write( abstract  )

    file.close
