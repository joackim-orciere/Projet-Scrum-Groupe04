from references import *

def findDiscussionParagraph( text ):
    text = text.split("\n\n")

    i = len( text ) - 1
    while( i >= 0 ):
        if( re.search( 'Discussion', text[i] ) or re.search( 'DISCUSSION', text[i] ) ):
                break
        i += -1 
    return i


def getDiscussion(text):
    target = "Discussion"
    if( not re.search( target, text )):
        target = "DISCUSSION"

    if( re.search( "Discussion", text ) or re.search( "DISCUSSION", text )):

        x = findDiscussionParagraph(text)
        y = findReferenceParagraph(text)

        text = text.split("\n\n")

        par = text[x].split( target )

        discussion = ''
        if( len(par) > 1 ):
            discussion = par[1]
        
        while( x < y ):
            discussion += text[x]
            x += 1

        return discussion
 
    else: # could not find discussion section
        return ''
  





