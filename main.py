import math

def tothepower(x, y):
  g = math.pow(x, y);
  return g

amount = float(input('Amount: '))
percentage = float(input('Percentage: '))
period = float(input('Time (days): '))
percentage /= 100
percentage += 1
a = (tothepower(percentage, period))
b = amount * a

print (b)


#70(percentage)^period