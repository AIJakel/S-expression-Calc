import sys
import re

"""
Takes a list of numbers and performs the mathmatical action on the list
numbers array
action string
returns float
"""
def doMath(numbers, action):
  if action.lower() == "add":
    result = 0
    for num in numbers:
      result += num
    return(result)

  elif action.lower() == "multiply":
    result = 1
    for num in numbers:
      result *= num
    return(result)

"""
Iterates through an array of strings it records the mathmatical operation or action.
If numbers are found they are stored until the end of the action is found then the numbers are evaluated.
If another action is found then re-call this function but only with the substring pertaining to that action.
input array of strings
action string
returns float
"""
def evaluate(input, action=None):
  actions = ["add","multiply"]
  numbers = []
  skipTo = None

  #handles the only input being an integer
  if len(input) == 1:
    return float(re.sub("()","",input[0]))

  for index, item in enumerate(input):
    #if item is containted within a sub action skip it
    if skipTo and index <= skipTo:
      continue

    #is the item an action?
    if item[0] == "(":
      item = item.replace("(","")
      if item in actions:
        if action == None:
          action = item
        else:
          #find the substring that contains all the info for the sub action
          subActions = 1
          for subIndex, subItem in enumerate(input[index+1:]):
            if subItem[0] == "(":
              subActions += 1

            if ")" in subItem:
              subActions -= subItem.count(")")
            
            if subActions <=0:
              skipTo = subIndex+index+1
              result = evaluate(input[index+1:subIndex+index+2], item)
              numbers.append(result)
              break

      else:
        raise Exception("An invalid action of " + item +" was passed to the program.")

    # item is the end of an action
    elif ")" in item:
      item = item.replace(")","")
      num = float(item)
      numbers.append(num)
      break
    
    else:
      num = float(item)
      numbers.append(num)

  return doMath(numbers,action)


input = sys.argv[1]
print(evaluate(input.split()))

