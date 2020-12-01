#!/bin/python
import pdftotext
import glob
import sys
import os
import re

from abstract import *
from references import *

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

    os.system( 'pdftotext ' + pdf_file + ' ' + target )


    file = open( target, 'r' );

    string = file.read()

    title = getTitle( string )
    abstract = getAbstract( string )
    references = getReferences( string )

    file.close()

    file = open( abstractTarget, 'w')
    file.write( filename  )
    file.write( "\n---------\n" )
    file.write( title  )
    file.write( "\n---------\n" )
    file.write( abstract  )
    file.write( "\n---------\n" )
    file.write( references  )

    file.close
