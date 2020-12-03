# Projet-Scrum-Groupe04
Projet Scrum Groupe04
Alexandre Jallade
Julien Bouloc
Joackim Orciere (Scrum Master)


# A simple pdf to xml parser

Its goal is to parse a pdf document, extract revelant parts
such as the Title, authors, Introduction etc.. in xml tags
or in plain texts.


## Dependencies

    * python 3
    * pdftotext

## Usage 

    python parser -o <targetFolder> 

    options for -o: 
    -t          # plain text output
    -x          # xml output

example :
    
    python parser -x ~/Documents/CORPUS/

