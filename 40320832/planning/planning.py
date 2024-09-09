#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fractions import Fraction
from collections import defaultdict
from sys import argv

# A module to read files and process the input data
def processInputFile(input_filename):
    '''
    Process the input file and return reactions, demands and itemSet.

    ### Input:
        - the directory of input file(string)

    ### Output:
        - reactions (dictionary)
        - demands (dictionary)
        - itemSet (tuple of 3 sets)
    '''
    reactions = {}
    demands = defaultdict(Fraction)
    materialSet = set()
    productSet = set()
    naturalMaterialSet = set()

    def readLines(input_filename):
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
        # Remove the '\n' at the end of each line
        lines = [line.strip() for line in lines]

        # Split the reaction equations and the demands
        reactionLines = lines[:lines.index('Q:')]
        demandLines = lines[lines.index('Q:')+1:]

        return reactionLines, demandLines

    def readReactionEquation(reactionLines):
        # Deal with the reaction equations
        for line in reactionLines:
            # Skip comments start with '#'
            if line.startswith('#') or not line:
                continue

            # Split the materials and product of the reaction
            materialList, product = line.split(' -> ')

            # Deal with the product side of the reaction
            productQuantity, productName = product.split(' ')
            productQuantity = int(productQuantity)
            productSet.add(productName)

            # Deal with the materials side of the reaction
            materials = materialList.split(' + ')
            materialGroup = []
            for material in materials:
                materialQuantity, materialName = material.split(' ')
                materialQuantity = int(materialQuantity)
                materialGroup.append((materialQuantity, materialName))
                materialSet.add(materialName)
            reactions[productName] = (productQuantity, materialGroup)

        return reactions

    def readDemands(demandLines):
        # Deal with the demands
        for line in demandLines:
            # Skip comments start with '#'
            if line.startswith('#') or not line:
                continue

            demand, quantity = line.split(' ')
            demands[demand] += Fraction(quantity)

        return demands

    reactionLines, demandLines = readLines(input_filename)
    reactions = readReactionEquation(reactionLines)
    demands = readDemands(demandLines)

    naturalMaterialSet = materialSet - productSet

    return reactions, demands, (materialSet, productSet, naturalMaterialSet)

# Calculate the required material with the given reactions and demands
# We can make it with depth-first search, path compression and recursion
def calculateRequiredMaterial(reactions, demands, itemSet):
    '''
    Calculate the required material with the given reactions and demands.

    ### Input:
        - reactions (dictionary)
        - demands (dictionary)
        - materialSet (set)
        - productSet (set)
        - naturalMaterialSet (set)

    ### Output:
        - requiredMaterial (dictionary)
    '''
    requiredMaterial = defaultdict(Fraction)
    reactionsMemo = defaultdict(Fraction)
    materialSet, productSet, naturalMaterialSet = itemSet
    allMaterialSet = materialSet | productSet

    def dfs(product, quantity):
        if product in naturalMaterialSet:
            requiredMaterial[product] += quantity
            return
        if product in reactionsMemo:
            factor = quantity / reactionsMemo[product][0]
            for materialQuantity, materialName in reactionsMemo[product][1]:
                dfs(materialName, factor * materialQuantity)
            return
        else:
            productQuantity, materialGroup = reactions[product]
            reactionsMemo[product] = (productQuantity, materialGroup)
            factor = quantity / productQuantity
            for materialQuantity, materialName in materialGroup:
                dfs(materialName, factor * materialQuantity)
            return

    for product, quantity in demands.items():
        if product not in allMaterialSet:
            requiredMaterial[product] += quantity
            continue
        dfs(product, quantity)

    return requiredMaterial

# A module to print the output data
def writeOutputFile(output_filename, needed):
    '''
    Write the needed material to the output file.

    ### Input:
        - the directory of output file(string)
        - needed (dictionary)

    ### Output:
        - a file with the needed material
    '''
    sortedRequiredMaterial = sorted(needed.items(), key=lambda x: (-x[1], x[0]))
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for material, quantity in sortedRequiredMaterial:
            output_file.write(f"{material} {quantity}\n")

def main():
    '''
    The main function to run the program, which is to read the input file,
    calculate the required material and write the output file.

    ### Input:
        - the directory of input file(string)
        - the directory of output file(string)

    ### Output:
        - a file with the needed material
    '''
    input_filename, output_filename = argv[1:3]
    reactions, demands, itemSet = processInputFile(input_filename)
    requiredMaterial = calculateRequiredMaterial(reactions, demands, itemSet)
    writeOutputFile(output_filename, requiredMaterial)

if __name__ == '__main__':
    main()
