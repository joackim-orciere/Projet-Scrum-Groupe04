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

def getAbstract(text):
    paragraphe=text.split("\n\n")
    if('Abstract' in paragraphe and 'Introduction' in paragraphe):##condition ideale (on a introduction et abstract)
        i = paragraphe.index("Abstract")
        j = paragraphe.index("Introduction")
        a=""
        for k in range(i+1,j):
            a+=paragraphe[k]
        return a

    else:##si jamais on a uniquement introduction ou abstract
        if('Introduction' in paragraphe):
            i = paragraphe.index("Introduction")
            j=i
            i=i-1
            a=""
            while(len(paragraphe[i-1])>80):
                i=i-1
            for k in range(i,j):
                a+=paragraphe[k]
            return(a);

        if('Abstract' in paragraphe):
            i = paragraphe.index("Abstract")
            i=i+1
            a=""
            a+=paragraphe[i]
            while(len(paragraphe[i+1])>80):
                i=i+1
                a+=paragraphe[i]
            return a;
    return "FAILED"


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

if( not os.path.isdir( plainpath )):
    os.mkdir( plainpath );

for pdf_file in pdf_files :
    if( os.path.splitext( pdf_file )[1] != '.pdf' ): # skip files that not pdf
        continue

    target = plainpath + '/' + os.path.splitext(os.path.basename( pdf_file ))[0] + '.txt' 

    filename = os.path.splitext(os.path.basename( pdf_file ))[0]

    os.system( 'pdftotext -f 1 -l 1 ' + pdf_file + ' ' + target )

    file = open( target, 'r' );

    string = file.read()

    title = getTitle( string )

    abstract = getAbstract( string )

    file.close()

    file = open( target, 'w')
    file.write( filename  )
    file.write( "\n---------\n" )
    file.write( title  )
    file.write( "\n---------\n" )
    file.write( abstract  )
    file.write( "\n---------\n" )

    file.close


