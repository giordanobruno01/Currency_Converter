from requests.models import Response
import requests
class currencyCorverter:

    def converter(self, curCur, newCur, amount):
  
      url = "https://api.exchangerate-api.com/v4/latest/" + curCur
      req = requests.get(url)
      rates = req.json()["rates"]
      curConversionRate = rates[newCur]

      convertedAmount = amount*curConversionRate
      print(convertedAmount)  



reader = open("currencies.txt", "r")
curList = reader.read().split("\n")
stop = True
cont = True
ob = currencyCorverter() 
print("\nCurrency List\n")
for i in range(len(curList)):
    print(i+1 , " for ", curList[i])
  
while(cont):
  stop = True
  while(stop):
      curCur = int(input("what is your current currency? "))-1
      newCur = int(input("what currency do you want to convert to? "))-1
      
      if(curCur>20 or newCur>20):
          print("invalid currency")
      else:
          stop = False
  curCur = curList[curCur][len(curList[curCur])-4:len(curList[curCur])-1]
  newCur = curList[newCur][len(curList[newCur])-4:len(curList[newCur])-1]
  print("what is the amount of ", curCur," you want to convert to ", newCur,"?")
  money = int(input())

  ob.converter(curCur, newCur, money)
  
  v = input("press any key to continue or n ").lower()
  if(v=="n"):
    cont = False

