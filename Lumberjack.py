"""Lumberjack -  A simple template for parsing multiple logs at once."""

import time
from datetime import datetime
from pathlib import Path
import sys, os

def readInputs():
    inputFiles = Path(".\\input").glob("*.*")
    inputList = []
    for inputName in inputFiles:
        inputFile = open(inputName, "r", encoding="utf8")
        inputList.append((inputName, inputFile.readlines()))
        inputFile.close()
    return inputList

def parseInput(inputTuple):
    #inputTuple as ( input_file_name, input_file_readlines() )
    
    #get the base name of the file.
    baseFileName = os.path.basename(os.path.normpath(inputTuple[0]))
    outputName = baseFileName.split('.')[0]
    
    #parse the input's text as needed.
    outputText = parseInputText(inputTuple[1])
    
    return (outputName, outputText)

def writeOutputs(parsedFiles):
    outputPath = Path(".\\output")
    
    #clear the output folder
    outputFiles = outputPath.glob("*.*")
    for outputFile in outputFiles:
        os.remove(outputFile)
    
    #write all the files to the output folder
    for parsedFile in parsedFiles:
        outputFile = open(f"{outputPath}\\{parsedFile[0]}.txt", "w+", encoding = "utf8")
        outputFile.writelines(parsedFile[1])
        outputFile.close()
    return

def main():
    inputFiles = readInputs()
    parsedFiles = list(map(lambda x: parseInput(x), inputFiles))
    writeOutputs(parsedFiles)

##### Modify the below method to change how the text for each file is handled. ######

def parseInputText(inputText):
    return inputText

#####################################################################################

main()
