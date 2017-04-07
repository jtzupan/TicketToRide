#
#
#

#import string
#from boardSetup import * as bs
import random
import boardSetup as bs


def load_map(mapFilename):
    '''

    '''

    board = bs.map()
    file_in = open(mapFilename, 'r')
    cityList = []
    for cityINST in file_in:
        x = cityINST.rstrip('\n').split(',')
        cityInfo = []
        cityInfo.append(bs.city(x[0]))
        cityInfo.append(bs.city(x[1]))
        cityInfo.append(x[2])
        cityList.append(cityInfo)
    
    for i in cityList:
        try:
            board.addCity(i[0])
        except:pass #print 'fail city 1'
        try:
            board.addCity(i[1])
        except: pass#print 'fail city 2'
        try:
            board.addRail(bs.rail(i[0], i[1], i[2]))
            #print type(i[0]), type(i[1]), type(i[2])
        except: pass#print 'failed edge'
    #print board.childrenOf(bs.city('atlanta'))
    return board


 
def shortestRail(graph, start, end, path = []):
    path = path + [bs.city(start)]
    if start == end:
        return [path]
    if graph.childrenOf(bs.city(start)) == []:
        return []
    paths = []
    for city1 in graph.childrenOf(bs.city(start)):
        #TODO: change childrenOf function to return only city name, not distance as well
        if city1[0] not in path:
            newpaths = shortestRail(graph, city1[0].getName(), end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def commonRails(r1, r2):
    r1Path = None
    r2Path = None
    commonCount = 0
    for i in r1:
        for j in r2:
            length = len(list(set(i).intersection(j)))
            if length > commonCount:
                r1Path = i
                r2Path = j
                commonCount = length
    return r1Path, r2Path, commonCount 


def makeDeck():
    deck = []
    for i in range(12):
        deck.append('purple')
        deck.append('white')
        deck.append('blue')
        deck.append('yellow')
        deck.append('orange')
        deck.append('black')
        deck.append('red')
        deck.append('green')
        deck.append('wild')
    deck.append('wild')
    deck.append('wild')
    return deck

def dealCard(deck):
    while True:
        userInput = raw_input('(1)see next card (2)remove random card (3)remove known card (4)shuffle\n')
        if userInput == 'q':
            break
        elif int(userInput) == 1:
            x = random.choice(deck)
            print x
            userChoice = raw_input('(1)keep card (2)ignore card\n')
            if int(userChoice) == 1:
                deck.remove(x)
        elif int(userInput) == 2:
            deck.remove(random.choice(deck))
        elif int(userInput) == 3:
            removeChoice = raw_input('what color to remove?\n')
            try:
                deck.remove(removeChoice)
                print 'removed %s' %removeChoice
            except:
                print 'could not remove card, reselect choice 3'
        elif int(userChoice) == 4:
            deck = makeDeck()
            dealCard(deck)
        else:
            print 'please enter 1-4'
            















