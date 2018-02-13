#import struct
import random
from ff6Dict import ff6CharCompressionDict

rom_file = open(r'Final Fantasy III (USA).sfc', "rb")
rom_data = rom_file.read()

#start of dialogue is 0xD02B0 and end is EF2FF

def translateToAlphabet(binSegment):
	constructed = []
	for x in range(len(binSegment)):
		#print("the range is " + str(len(binSegment)))
		#print("the hex number is " + str(hex(binSegment)))
		#print(str(gameBinToChar(binSegment[x])))
		constructed.append(gameBinToChar(binSegment[x]))
	return ''.join(constructed)


def gameBinToChar(hexChar):
	#this function converts a byte of compressed FF6 text to an ascii char
	if hexChar in ff6CharCompressionDict:
		return ff6CharCompressionDict[hexChar]
	else:
		return "\n"


#rangestart = 0xD02B3


def findRangeStart():
	rangeVar = random.randrange(0xD02B3,0xEF2FF,1)
	while rom_data[rangeVar-1] != 0 | 0x13:
		rangeVar = random.randrange(0xD02B3,0xEF2FF,1)
	return rangeVar

def getQuote(maxLength):
       rangestart = findRangeStart()
       rangeend = maxLength
       rom_slice = rom_data[rangestart:rangestart+rangeend]
       outputString = translateToAlphabet(rom_slice)

       while len(outputString) > maxLength:
       	stringList = outputString.split('\n')
       	stringList.pop()
       	outputString = '\n'.join(stringList)

       return outputString

def getQuoteAndBin(maxLength):
       rangestart = findRangeStart()
       rangeend = maxLength
       rom_slice = rom_data[rangestart:rangestart+rangeend]
       outputString = translateToAlphabet(rom_slice)

       while len(outputString) > maxLength:
              stringList = outputString.split('\n')
              stringList.pop()
              outputString = '\n'.join(stringList)

       return [outputString, rom_slice]

#outputString = translateToAlphabet(rom_data[rangestart:rangestart+rangeend])
#print("\n")
#print("=======")
#print(outputString)
#print("=======")
#print("\n Character Count: (" + str(len(outputString)) +")")
