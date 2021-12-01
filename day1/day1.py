inputFileName = "input.txt"

previous = None
current = None
increaseCount = 0

with open(inputFileName) as inputList:

  for row in inputList:
    current = row.strip()

    if previous is None:
      previous = current
      continue
    elif previous < current:
      increaseCount += 1 

    previous = current


print (increaseCount)