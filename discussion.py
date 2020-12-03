from references import *

def findDiscussionParagraph( text ):
    text = text.split("\n\n")

    i = len( text ) - 1
    while( i >= 0 ):
        if( re.search( 'discussion', text[i], re.IGNORECASE )):
                break
        i += -1 
    return i


def getDiscussion(text):
    if( re.search( 'discussion', text[i], re.IGNORECASE )):
        x = findDiscussionParagraph(text)
        y = findReferenceParagraph(text)

       par = text[i].split('discussion', re.IGNORECASE  )

        discussion = ''
        if( len(par) > 1 ):
            discussion = par[1]
        
        while( x < y ):
            discussion += text[1]
            i += 1

        return discussion
 
    else: # could not find discussion section
        return ''
  





