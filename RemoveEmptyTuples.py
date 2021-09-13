sampleTuples = [(),(),(","),('a','b','c'),('a','b'),('d')]
resultTuples = []

def is_empty(x):
    len(x) != 0 and resultTuples.append(x)

for x in sampleTuples:
    is_empty(x)
print(resultTuples)