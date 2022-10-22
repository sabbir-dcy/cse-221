def task1a(nums):

  for n in nums:
    n = int(n)
    print(f'{n} is odd', file=op) if n % 2 != 0 else print(f'{n} is even', file=op) 

if __name__== '__main__':
  inp = open(r'/content/sample_data/input1a.txt','r')
  op = open(r'/content/sample_data/output1a.txt','w')

  nums = inp.readlines()
  task1a(nums)