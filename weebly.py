#weebly.py

theList = []

def fix(x):
	for i in range(len(x)):
		if  isinstance(x[i], list):
			fix(x[i])
		else:
			theList.append(x[i])


sampleList = ["abc", ["efg", [["h", "i", "j"], "kl"], "mnop"], "qrs"]
fix(sampleList)
print theList