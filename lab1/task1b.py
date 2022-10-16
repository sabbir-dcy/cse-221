import operator as optr

def task1b(operations):

  for operation in operations:
    var = operation.split(' ')[1:4]
    ops = {
      '+': optr.add,
      '-':optr.sub,
      '*':optr.mul,
      '/':optr.truediv
    }

    a = int(var[0])
    b = int(var[2])
    sign = var[1]
    
    print(f'The result of {a} {sign} {b} is {ops[sign](a,b)}', file=op)

if __name__ == '__main__':
  # assign input file
  inp = open(r'/content/sample_data/input1b.txt','r')

  # assign output file
  op = open(r'/content/sample_data/output1b.txt','w')

  # read first line
  inp.readline()

  operations = inp.readlines()
  task1b(operations)