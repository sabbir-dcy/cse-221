def task4(mark, id):
  lent = len(mark)
  swap = False # flag check

  for i in range(lent-1):
    for j in range(lent-i-1):
      if mark[j] < mark[j+1]:
        swap = True
        mark[j], mark[j+1] = mark[j+1], mark[j]
        id[j], id[j+1] = id[j+1], id[j]
      elif mark[j] == mark[j+1]:
        if id[j] > id[j+1]:
          id[j], id[j+1] = id[j+1], id[j]
    # check if any swap happens
    if not swap:
      return
  
  for i in range(lent):
    print(f'ID: {id[i]} Mark: {mark[i]}', file=op)

if __name__=='__main__':
  f = open(r'C:\Users\sas\Desktop\New folder\python\lab1\input4.txt','r')
  op = open(r'C:\Users\sas\Desktop\New folder\python\lab1\output4.txt','w')

  f.readline()

  arr = []
  id = f.readline().split(' ')
  mark = f.readline().split(' ')
  
  for i in range(len(id)):
    arr.append({int(id[i]),int(mark[i])})
  print(arr)

