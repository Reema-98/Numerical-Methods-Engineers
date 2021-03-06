from math import *

def milne_simpson(f,t, y, p, h,y_values):
  n = int((p-t)/h)
  print(n)
  time = [t+i*h for i in range(n+1)]
  
  print(y_values)
 
  a=4

  for i in range(4, n+1):
    milne = y_values[i-4] + 4/3*h*(2*f(time[i-1], y_values[i-1]) - f(time[i-2], y_values[i-2]) + 2*f(time[i-3], y_values[i-3]))
    y_values[i] = y_values[i-2] + h/3*(f(time[i],milne) + 4*f(time[i-1], y_values[i-1]) + f(time[i-2], y_values[i-2]))

  print("fn:::")
  print(f(time[i],milne))
  print("Predictor answer")
  print(milne)
  milne=y_values[i]
  for k in range(a):
    
    d= y_values[i-2] + h/3*(f(time[i],milne) + 4*f(time[i-1], y_values[i-1]) + f(time[i-2], y_values[i-2]))
    print(str(f(time[i],milne))+" function answer")
    milne=d
    y_values.append(d) 


  print(f"Milne-Simpson Method")
  print("-"*70)
  print(f'\t|\tEstimate\t')
  print("-"*70)

  for i in range(len(y_values)):
    print(f'\t|\t{y_values[i]:.9f}\t')
  print("-"*70)

def rk4(f, t, y):
  k1 = h*f(t, y)
  k2 = h*f(t + h/2, y + k1/2)
  k3 = h*f(t + h/2, y + k2/2)
  k4 = h*f(t + h, y + k3)
  return y + (k1 + 2*k2 + 2*k3 + k4)/6

if __name__ == '__main__':

  f = lambda t, y: y*y + t*t



  t = float(input("t0: "))
  y = float(input("y0: "))
  p = float(input("Evaluation point: "))
  h = float(input("Step size: "))
  n = int((p-t)/h)
  y_values = [0]*(n+1)
  y_values[0] = y
  for i in range(1, 4):
    y_values[i]= float(input("values"))
  milne_simpson(f, t, y, p, h,y_values)