#this file will read in the board, create the cities, and create the line between cities

class city(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return self.name
    def __hash__(self):
        return self.name.__hash__()

class rail(object):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')->' + str(self.dest)

class map(object):
    def __init__(self):
        self.cities = set([])
        self.rails = {}
    def addCity(self, city):
        if city in self.cities:
            raise ValueError('Duplicate city')
        else:
            self.cities.add(city)
            self.rails[city] = []

    def addRail(self, rail):
         src = rail.getSource()
         revDest = rail.getSource()
         dest = rail.getDestination()
         revSrc = rail.getDestination()
         if not (src in self.cities and dest in self.cities):
             raise ValueError('city not in graph')
         x = rail.getWeight()
         self.rails[src].append([dest,x])
         self.rails[revSrc].append([revDest, x])


         #self.rails[revSrc].append(revDest)
    def childrenOf(self, city):
        return self.rails[city]
    def hasCity(self, city):
        return city in self.cities
    def __str__(self):
        res = ''
        for i in self.rails:
            for j in self.rails[i]:
                #res += str(i) + '->' + str(j) + '\n'
                res += '{0}->{1} ({2})\n'.format(i, j[0], j[1])
        return res[:-1]

#TODO: add a function to load the map
