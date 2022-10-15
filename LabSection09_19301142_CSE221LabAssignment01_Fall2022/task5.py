def task5(arr):
  train = []
  dept = []
  destination = []

  for str in arr:
    name = str.split(' ')[0]
    time = str.split(' ')[-1]
    dest = str.split(' ')[-3]
    train.append(name)
    dept.append(time)
    destination.append(dest)

  bubbleSort(train, dept,destination)

def bubbleSort(train, dept,destination):
  lent = len(train)
  swap = False # flag check

  for i in range(lent-1):
    for j in range(lent-i-1):
      if train[j] > train[j+1]:
        swap = True
        train[j], train[j+1] = train[j+1], train[j]
        dept[j], dept[j+1] = dept[j+1], dept[j]
        destination[j], destination[j+1] = destination[j+1], destination[j]
      elif train[j] == train[j+1]:
        if dept[j] < dept[j+1]:
          dept[j], dept[j+1] = dept[j+1], dept[j]
          destination[j], destination[j+1] = destination[j+1], destination[j]

    # check if any swap happens
    if not swap:
      return
  
  output(train, dept, destination)
    
def output(train, dept, destination):
  for i in range(len(train)):
    print(f'{train[i]} will departure for {destination[i]} at {dept[i]} ', file=op)

if __name__=='__main__':
  f = open(r'/content/sample_data/input5.txt','r')
  op = open(r'/content/sample_data/output5.txt','w')

  f.readline()
  arr = f.readlines()
  task5(arr)