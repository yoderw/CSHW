import math
from math import sqrt
from statistics import mean, pstdev, stdev, pvariance, variance

class County:
    def __init__(self, name, values):
        self.name = name
        self.values = values
    def distance(self, othervals):
        dist = 0
        for i in range(len(self.values)):
            dist += abs(self.values[i]-othervals[i])
        return dist

class Cluster:
    def __init__(self):
        self.centroid = []
        self.contents = []
    def updateCentroid(self):
        #your code here (replace "pass" with code)
        pass
    def names(self):
        names = ""
        for c in self.contents:
            names += c.name + "; "
        return names
    def clear(self):
        self.contents = []

def readData(filename):
    counties = []
    with open(filename, "r") as data:
        for line in data:
            line = line.split(";")
            name = line[0]
            if name != "Areaname":
                values = line[2:-1]
                landarea = float(line[-1][:-1])
                values = [float(i) for i in values]
                values[1] /= landarea
                counties.append(County(name, values))
    return counties

def normalizeCounties(counties):
    meanls = [0 for i in range(16)]
    stdevls = [0 for i in range(16)]
    for i in range(16):
        values = [county.values[i] for county in counties]
        meanls[i] = mean(values)
        stdevls[i] = pstdev(values)
        for county in counties:
            county.values[i] -= meanls[i]
            county.values[i] /= stdevls[i]

def normalizeCounties(counties):
    sumls = [0 for i in range(16)]
    meanls = [0 for i in range(16)]
    varls = [0 for i in range(16)]
    stdevls = [0 for i in range(16)]
    for i in range(16):
        for county in counties:
            sumls[i] += county.values[i]
        meanls[i] = sumls[i] / len(counties)
        squareDevls = []
        for county in counties:
            squareDevls.append((county.values[i] - meanls[i]) ** 2)
        varls[i] = sum(squareDevls) / len(squareDevls)
        stdevls[i] = sqrt(varls[i])
        for county in counties:
            county.values[i] -= meanls[i]
            county.values[i] /= stdevls[i]


def initClusters(counties, num):
    clusters = []
    for i in range(num):
        newcluster = Cluster()
        newcluster.centroid = counties[i].values[:]
        clusters.append(newcluster)
    return clusters

def distance(p, q):
    if len(p) == len(q):
        values = [0 for i in range(len(p))]
        for i in range(len(p)):
            diff = p[i] - q[i]
            square = diff ** 2
            values[i] = square
        sumVals = sum(values)
        return sqrt(sumVals)

def placeCounties(counties, clusters):
    for county in counties:
        centroidDiff = [0 for i in range(len(clusters))]
        for cluster in clusters:
            i = clusters.index(cluster)
            centroid = cluster.centroid
            values = county.values
            centroidDiff[i] = distance(values, centroid)
        minCentroid = min(centroidDiff)
        i = centroidDiff.index(minCentroid)
        closestCluster = clusters[i]
        closestCluster.contents.append(county)

def updateCentroids(clusters):
    for c in clusters:
        c.updateCentroid()

def clearClusters(clusters):
    for c in clusters:
        c.clear()

def writeOutput(clusters, filename):
    #your code here (replace "pass" with code)
    pass

def kmeans(infile, outfile, k, cycles):
    counties = readData(infile)
    normalizeCounties(counties)
    clusters = initClusters(counties, k)
    for i in range(cycles):
        clearClusters(clusters)
        placeCounties(counties, clusters)
        updateCentroids(clusters)
    writeOutput(clusters, outfile)

#TESTING
counties = readData("counties.txt")
normalizeCounties(counties)
print(counties[0].name, counties[0].values == [-1.1360914508849485, -0.09761783122525876, 0.25867007626415933, -0.8362612914682693, 0.6968800072452435, -0.4406592158742433, 0.6383515401822617, -0.2273153386303384, -0.09175952352172007, -0.01810789455986609, -0.45829273443586077, -0.07551781560439914, -0.5314595738793548,0.25284846795399535, 0.6831337952039793, -0.7296777754952319])
clusters = initClusters(counties, 30)
placeCounties(counties, clusters)
print(len(clusters[0].contents), len(clusters[0].contents) == 208)
print(len(clusters[1].contents), len(clusters[1].contents) == 261)
#END

# You can use the line below to test your kmeans code once you've
# completed the coding for all five exercises.  Compare the text file
# "output.txt" produced by the code below against the sample output
# file called "output30x120.txt" included in this folder.
#
# Please comment out this line when you hand in your code for each
# exercise, otherwise our tests might time out, taking too long to
# load your code. (Our tests use other means to verify your code.)
#

#kmeans("counties.txt", "output.txt", 30, 120)
