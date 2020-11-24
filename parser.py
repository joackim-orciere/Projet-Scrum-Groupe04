#!/bin/python
import glob
import sys
import os

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
    if( os.path.splitext( pdf_file )[1] != '.pdf' ):
        continue

    os.system( 'pdftotext ' + pdf_file + ' ' + plainpath + '/' 
            + os.path.splitext(os.path.basename( pdf_file ))[0] + '.txt' )


    #    file = open('myfile.dat', 'a+')
    #   file.write("appended text")

