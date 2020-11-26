#!/bin/python
import os
import glob
import re




def checkIfRefChars( paragraph ):
    return re.search( '\.', paragraph ) and re.search( ',', paragraph ) and \
        re.search( '[0-9]', paragraph ) and re.search( '-', paragraph )
        

def findReferenceParagraph( text ):
    text = text.split("\n\n")

    found = False
    i = 0
    while( i < len( text ) and found == False ):
        if( re.search( '^references', text[i], re.IGNORECASE )):
            if( len( text[i] ) < 50):
                i += 1
            found = True
        i += 1
    i = i - 1
    encountered = False
    if( found == False ):
        i = i - 1
        while( i > 0 and not found):
            if( len( text[i] ) < 100 and not encountered ):
                    i = i - 1
                    continue
            if( checkIfRefChars( text[i] )):
                encountered = True
                i = i - 1
                continue
            else:
                if( encountered ):
                    i = i + 1
                    found = True
                i = i + 1
                found = True
                break
        i -= 1
    return i

def getReferences( text, name ):

    i = findReferenceParagraph( text )

    text = text.split("\n\n")
    print( "    ----    ")
    print( name, ': ', i, '\n', text[i][:100] )

    
    """ # used for testing
text_files = glob.glob( 'CORPUS_TEST/plainTexts/*' );

for text_file in text_files:

    file = open( text_file, 'r' );
    text = file.read()

    n = os.path.splitext(os.path.basename( text_file ))[0]

    getReferences( text, n )
    """
