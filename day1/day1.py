inputFileName = "input.txt"


def part_1():
  previous = 0
  current = 0
  increaseCount = 0

  with open(inputFileName) as inputList:

    for row in inputList:
      current = int(row.strip())

      if previous == 0:
        previous = current
        continue
      elif current > previous:
        increaseCount += 1 

      previous = current

  return increaseCount

def part_2():
  # chunkSize = 3
  # arrayList = []
  # previous = 0
  # increaseCount = 0

  # with open(inputFileName) as inputList:
  #   arrayList = inputList.read().split('\n')

  # # for row in [arrayList[i:i+chunkSize] for i in range(len(arrayList))[::chunkSize]]:
  # #   total = sum(list(map(int, row)))
  # #   if total > previous:
  # #     increaseCount += 1

  # #   previous = total

  # # return increaseCount


  # for x in range(len(arrayList)):
  #   if x+1 == len(arrayList):
  #     current = arrayList[x]
  #   elif x+2 == len(arrayList):
  #     current = arrayList[x] + arrayList[x+1]
  #   else:
  #     current = arrayList[x] + arrayList[x+1] + arrayList[x+2]


  #   if previous == 0:
  #     previous = current
  #     continue
  #   elif current > previous:
  #     increaseCount += 1 

  #   previous = current
  with open(inputFileName, 'r') as f:
      nums = [int(i) for i in f.read().splitlines()]

  return sum(nums[i] > nums[i-3] for i in range(3, len(nums)))


## Group each into 


if __name__ == "__main__":
  print (part_1())
  print (part_2())