import sys
import re



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

def cleanInput(input, action=None):
  actions = ["add","multiply"]
  numbers = []
  skipTo = None

  #just an integer was passed to the function
  if len(input) == 1:
    return float(re.sub("()","",input[0]))

  for index, item in enumerate(input):
    if skipTo and index <= skipTo:
      continue

    if item[0] == "(":
      item = item.replace("(","")
      if item in actions:
        if action == None:
          action = item
        else:
          #find the substring that contains all the info for the new operation
          subActions = 1
          for subIndex, subItem in enumerate(input[index+1:]):
            if subItem[0] == "(":
              subActions += 1

            if ")" in subItem:
              subActions -= subItem.count(")")
            
            if subActions <=0:
              skipTo = subIndex+index+1
              result = cleanInput(input[index+1:subIndex+index+2], item)
              numbers.append(result)
              break

      else:
        raise Exception("An invalid action of " + item +" was passed to the program.")

    elif ")" in item:
      item = item.replace(")","")
      num = float(item)
      numbers.append(num)
      break
    
    else:
      num = float(item)
      numbers.append(num)

  #broke down data set until 2 numbers are present with an action
  return doMath(numbers,action)


input = sys.argv[1]
print(cleanInput(input.split()))

