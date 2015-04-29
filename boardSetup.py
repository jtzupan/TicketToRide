#this file will read in the board, create the cities, and create the line between cities

class city(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class rail(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

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
         dest = rail.getDestination()
         if not (src in self.cities and dest in self.cities):
             raise ValueError('city not in graph')
         self.rails[src].append(dest)
         #rev = rail(rail.getDestination(), rail.getSource())
         revSrc = rail.getDestination()
         revDest = rail.getSource()
         self.rails[revSrc].append(revDest)
    def childrenOf(self, city):
        return self.rails[city]
    def hasCity(self, city):
        return city in self.cities
    def __str__(self):
        res = ''
        for i in self.rails:
            for j in self.rails[i]:
                res += str(i) + '->' + str(j) + '\n'
        return res[:-1]

#TODO: add a function to load the map
