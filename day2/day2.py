fileName = 'input.txt'

with open(fileName, 'r') as f:
  instructions = [i for i in f.read().splitlines()]

def part_1():

  horPoz = 0
  depth = 0

  for instruction in instructions:
    command = instruction.split(' ')[0]
    distance = int(instruction.split(' ')[1])

    if command == 'forward':
      horPoz += distance
    elif command == 'down':
      depth += distance
    elif command == 'up':
      depth -= distance

  return horPoz*depth

def part_2():
  horPoz = 0
  depth = 0
  aim = 0

  for instruction in instructions:
    command = instruction.split(' ')[0]
    distance = int(instruction.split(' ')[1])

    if command == 'forward':
      horPoz += distance
      depth += aim * distance
    elif command == 'down':
      aim += distance
    elif command == 'up':
      aim -= distance 

  return horPoz*depth


if __name__ == "__main__":
  print (part_1())
  print (part_2())