# -*- coding: utf-8 -*-

import pickle
from domain import *
import random


class Repository():
    def __init__(self):
        self.__populations = []
        self.createRandomMap()
        

    def createPopulation(self, args): 
        # args = [startX, startY, populationSize, individualSize]
        population = Population(self.__cmap, args[0], args[1], args[2], args[3])
        self.__populations.append(population)

        return population


    def addNewPopulation(self, population):
        self.__populations.append(population)
        

    def getMap(self):
        return self.__cmap


    def createRandomMap(self):
        self.__cmap = Map()
        self.__cmap.randomMap()

    
    def loadMap(self, fileName):
        self.__cmap = Map()
        self.__cmap.loadMap(fileName)


    def saveMap(self, fileName):
        self.__cmap.saveMap(fileName)


    def getTheMostRecentPopulation(self):
        if len(self.__populations) == 0:
            raise Exception("There are no populations in the repository.")
        return self.__populations[-1]


    def mergePopulations(self):
        population = self.__populations[0]
        for i in range(1, len(self.__populations)):
            population = population.merge(self.__populations[i])

        self.__populations = [population]

    def resetRepository(self):
        self.__populations = []
        self.createRandomMap()