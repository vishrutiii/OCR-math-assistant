#bodmas calc
class Calculator:
	def __init__(self, Input):
		Input = Input.replace(" ", "")
		inputList = [y for x,y in enumerate(Input)]
		self.numList = [] 
		self.operList = [] 
		self.tempNum = ''
		self.numbers = ['1','2','3','4','5','6','7','8','9','0', '.']
		numList, operList = self.formNumber(inputList) 
		numList, operList = self.solve(numList, operList)
		while ('+' in operList) or ('-' in operList) or ('*' in operList) or ('/' in operList) or ('^' in operList):
			numList, operList = self.solve(numList, operList)
		self.result = numList[0]

	def solveBrackets(self, Input):
		inputList = [y for x,y in enumerate(Input)]
		numList, opList = [], []
		tempNum = ''
		for y,x in enumerate(inputList):
			if str(x) in self.numbers:
				tempNum += str(x)
			else:
				if tempNum != '':
					numList.append(float(tempNum))
				tempNum = ''
				opList.append(x)
			if y+1 is len(inputList):
				if tempNum != '':
					numList.append(float(tempNum))
				tempNum = ''
		numList, opList = self.solve(numList, opList)
		while ('+' in opList) or ('-' in opList) or ('*' in opList) or ('/' in opList) or ('^' in opList):
			numList, opList = self.solve(numList, opList)
		return numList[0]

	def formNumber(self, inputList):
		tempNum = ''
		numList = []
		opList = []
		brackets = False
		for y,x in enumerate(inputList):
			if str(x) == '(':
				brackets = True 
				continue 
			elif str(x) == ')':
				brackets = False 
				tempNum = self.solveBrackets(tempNum)
				numList.append(tempNum)
				continue
			if brackets:
				tempNum += str(x)
			else:
				if str(x) in self.numbers:
					tempNum = tempNum + str(x) 
				else:
					if tempNum != '':
						numList.append(float(tempNum))
					tempNum = ''
					opList.append(x)
				if y+1 is len(inputList):
					numList.append(float(tempNum))
					tempNum = ''
		return numList, opList 

	def solve(self, numList, opList):
		for x,y in enumerate(opList):
			if y == '^':
				numList[x] = float(numList[x]) ** numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y == '/':
				numList[x] = float(numList[x]) / numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y== '*':
				numList[x] = float(numList[x]) * numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y == '+':
				numList[x] = float(numList[x]) + numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y == '-':
				numList[x] = float(numList[x]) - numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		return numList, opList 
# cal = Calculator(input()) #input mai to have text
# print(cal.result)

# while True:
# 	try:
		
# 	except:
# 		print("Sorry There's an error")
