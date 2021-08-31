import random

def mymain():
  #print("Keep it logically awesome Dude.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #last = 13
  last = len(quotes) - 1
  rnd = random.randint(0, last)


  #print(quotes)
  #print(quotes[0]) #First quote
  #print(quotes[-1]) # Print the last one!
  #adding comment
  print(quotes[rnd])

if __name__== "__main__":
  mymain()
