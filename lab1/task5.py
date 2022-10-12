def task5(arr):
  ar = []

  for str in arr:
    obj = {str.split(' ')[0], str.split(' ')[-1]}
    ar.append(obj)

  print(ar)


if __name__=='__main__':
  f = open(r'C:\Users\sas\Desktop\New folder\python\lab1\input5.txt','r')
  op = open(r'C:\Users\sas\Desktop\New folder\python\lab1\output5.txt','w')

  f.readline()
  arr = f.readlines()
  task5(arr)