test = True
count = 0
total = 0
while test:
  userInput = input("Enter a number:")
  try:
      if userInput == 'done':
          break
      userInput = int(userInput)
  except:
      print("Bad Data")
      continue
  count+= 1
  total += userInput
average = total/count
print("Amount of numbers enter:" ,count, " Sum of numbers:", total ,"The average of numbers:" ,average)
