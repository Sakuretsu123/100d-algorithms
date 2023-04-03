#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  c = 0 
  a1 = a
  b1 = b
  i = 0
  p = 0
  number = 0
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """

    
 
  myList = ["94"]
  myList.append(str(a))
  myList.append(str(b))
  
  
  while a != a1 and b != b1 or i == 0: 
      i += 1
      c = int(a) + int(b) 
      if c < 10 : 
        myList[p]
        myList.append(str(c))
        a = myList[-1]
        b = myList[-2]
        a = int(a)
        b = int(b)
      elif c > 10: 
        c = str(c)
        a = c[0]
        b = c[1]
        a = int(a)
        b = int(b)
      

  print(myList)
  return None






def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
