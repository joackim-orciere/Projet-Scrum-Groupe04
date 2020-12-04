#!/bin/python
import pdftotext
import glob
import sys
import os
import re


from abstract import *
from references import *
from introduction import *
from discussion import *
from corps import *
from conclusion import *

def wrongUsage():
    print("/!\\ Usage: $./parse -o directory")
    print("options: \n\t-t \t# plain text output\n\t-x \t# xml output")
    exit()

def testLine( line ):
    return re.search( ':|\(|\)|,', line )

def getTitle( txt ):


    phrase=txt.split("\n")

    # title = str(phrase[0:2])
    title = phrase[0] + '\n' + phrase[1]

    return title

def getAutor( txt ):

    phrase=txt.split("\n")
    posab=4

    for j in range(0, 50):
        if('Abstract' in phrase[j] or 'ABSTRACT' in phrase[j]):

            posab=j

    # autor = str(phrase[2:posab])
    autor = phrase[2]
    i = 2
    for i in range( i, i + posab ):
        autor += '\n' + phrase[i]


    return autor


if( len(sys.argv) <= 2 ):
    wrongUsage()

xml = False

if( sys.argv[1] != '-x' and sys.argv[1] != '-t' ):
    wrongUsage();
else:
    if( sys.argv[1] == '-x' ):
        xml = True

dirpath = sys.argv[2]

exist = os.path.isdir( dirpath)
if( not exist ):
    print("/!\\ directory '" + dirpath + "' cannot be found.")
    exit()

if( dirpath[-1:] != '/' ):
    dirpath += '/'

pdf_files = glob.glob( dirpath + '*.pdf' );

# Select files from directory
promptedFiles = []  # liste des fichier contenues dans le dossier passé en argument

print("Veuillez choisir les fichiers à transcrire: \n")
for i, file in enumerate( pdf_files ) :
    filename = os.path.basename( file )

    print( i+1, ' \t', filename )
    promptedFiles.append( [i+1, file] )

s = input("-> ").split()

selected = [] # liste des index selectionnés


# verifications des inputs
for i, item in enumerate( s ):
    try:
        tmp = int( item )
        if( tmp > len( pdf_files )):
            print("l'index '" + item + "' ne correspond à aucun index")
        else:
            selected.append( tmp )
    except:
        print("la chaîne '" + item + "' ne correspond à aucun index")


if( len( selected ) <= 0 ):
    print("Aucun index valide rentré, termination du programme.")
    exit()

selectedFiles = [] # list des fichiers selectionnés

for i, file in enumerate( promptedFiles ):
    if( file[0] in selected and file[1] not in selectedFiles ):
        selectedFiles.append( file[1] )


plainpath = dirpath + 'plainTexts'
abstractpath = dirpath + 'abstractTexts'

if( not os.path.isdir( plainpath )):
    os.mkdir( plainpath );
if( not os.path.isdir( abstractpath )):
    os.mkdir( abstractpath );



for pdf_file in selectedFiles :
    if( os.path.splitext( pdf_file )[1] != '.pdf' ): # skip files that not pdf
        continue

    target = plainpath + '/' + os.path.splitext(os.path.basename( pdf_file ))[0] + '.txt'
    abstractTarget = abstractpath + '/' + os.path.splitext(os.path.basename( pdf_file ))[0] + '.txt'


    filename = os.path.splitext(os.path.basename( pdf_file ))[0]

    os.system( 'pdftotext ' + pdf_file + ' ' + target )


    file = open( target, 'r' );
    string = file.read()
    file.close()

    file = open( abstractTarget, 'w')

    if( xml == True ):
        file.write('<article>')

        file.write('\t<preamble>')
        file.write(filename + '\n')
        file.write('\t</preamble>\n')

        file.write('\t<titre>')
        file.write(getTitle(string) + '\n')
        file.write('\t</titre>\n')

        file.write('\t<auteur>')
        file.write(getAutor(string))    # not done yet
        file.write('\t</auteur>\n')

        file.write('\t<abstract>')
        file.write(getAbstract(string) + '\n')
        file.write('\t</abstract>\n')

        file.write('\t<introduction>')
        file.write(getIntroduction(string) + '\n')
        file.write('\t</introduction>\n')

        file.write('\t<corps>')
        file.write(getCorps(string) + '\n')
        file.write('\t</corps\n')

        file.write('\t<discussion>')
        file.write(getDiscussion(string) + '\n')
        file.write('\t</discussion>\n')

        file.write('\t<conclusion>')
        file.write(getConclusion(string) + '\n')
        file.write('\t</conclusion>\n')

        file.write('\t<biblio>')
        file.write(getReferences(string) + '\n')
        file.write('\t</biblio>\n')

        file.write('</article>')

    else:
        file.write(filename + '\n\n')
        file.write('-TITLE-\n\n' + getTitle(string) + '\n\n')
        file.write('-AUTOR-\n\n' + getAutor(string) + '\n\n')
        file.write('-ABSTRACT-\n\n' + getAbstract(string) + '\n\n')
        file.write('-INTRODUCTION-\n\n' + getIntroduction(string) + '\n\n')
        file.write('-CORPS-\n\n' + getCorps(string) + '\n\n')
        file.write('-DISCUSSION-\n\n' + getDiscussion(string) + '\n\n')
        file.write('-CONCLUSION-\n\n' + getConclusion(string) + '\n\n')
        file.write('-REFERENCES-\n\n' +getReferences(string) + '\n\n')

    file.close
