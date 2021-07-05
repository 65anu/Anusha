import random
maxticketsavailable=int(input("Enter the maximum tickets available"))
participants=[]
for temp in range(maxticketsavailable):
  st = "Enter the participant name - "+ str(temp+1) +" - "
  name=input(st)
  participants.append(name)
print("All our participants -", participants)
n=random.randint(0,maxticketsavailable-1)
print("Winner of the lottery-", participants [n])
