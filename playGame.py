#
#
#

import string
from boardSetup import *


def load_map(mapFilename):
    '''

    '''

    board = map()
    file_in = open(mapFilename, 'r')
    cityList = []
    for cityINST in file_in:
        x = cityINST.rstrip('\n').split(',')
        cityInfo = []
        cityInfo.append(city(x[0]))
        cityInfo.append(city(x[1]))
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
            board.addRail(rail(i[0], i[1], i[2]))
            print type(i[0]), type(i[1]), type(i[2])
        except: pass#print 'failed edge'
    print board.childrenOf(city('atlanta'))
    return board

def load_maptest(fileName):
    file_in = open(fileName, 'r')
    cityList = []
    for city in file_in:
        x = city.rstrip('\n').split(',')
        if x[0] not in cityList:
            cityList.append(x[0])
        if x[1] not in cityList:
            cityList.append(x[1])
    finalList = []
    for i in cityList:
        #finalList.append(city(i))
        print i
    g = map()
    for n in finalList:
        g.addCity(n)
    g.addRail(rail(finalList[0], finalList[1]))
    g.addRail(rail(finalList[1], finalList[2]))
    g.addRail(rail(finalList[3], finalList[2]))
    return g

def l1():
    denver = city('denver')
    toronto =city('toronto')
    atlanta = city('atlanta')
    phoenix = city('phoenix')
    dt = rail(denver, toronto, 6)
    ta = rail(toronto, atlanta, 7)
    ap = rail(atlanta, phoenix, 3)
    tp = rail(toronto, phoenix, 4)
    pd = rail(phoenix, denver, 5)
    g = map()
    g.addCity(atlanta)
    g.addCity(denver)
    g.addCity(phoenix)
    g.addCity(toronto)
    g.addRail(dt)
    g.addRail(ta)
    g.addRail(tp)
    g.addRail(ap)
    g.addRail(pd)
    print g.childrenOf(atlanta)
    return g

def shortestRail(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    #if not graph.childrenOf(start):
    #    return []
    paths = []
    for city in graph[start]:
        if city not in path:
            newpaths = shortestRail(graph, city, end, path)
            for newpath in newpaths:
                paths.append(newpaths)
    return paths
