class currencyCorverter:

    def converter(self):
        pass

cur = input("what currency do you want to convert? ")

reader = open("currencies.txt", "r") 
curList = reader.read().split("\n")
print(curList)
for i in range(len(curList)):
