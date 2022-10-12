def task1a(nums):

  for n in nums:
    n = int(n)
    print(f'{n} is odd', file=op) if n % 2 != 0 else print(f'{n} is even', file=op) 

if __name__== '__main__':
  inp = open(r'C:\Users\sas\Desktop\New folder\python\lab1\input1a.txt','r')
  op = open(r'C:\Users\sas\Desktop\New folder\python\lab1\output1a.txt','w')

  nums = inp.readlines()
  task1a(nums)