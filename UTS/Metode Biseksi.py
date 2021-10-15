def bisection(f, a, b, e=0.5, N = 100):
  x_a = a
  x_b = b
  
  if f(x_a)*f(x_b) >= 0:
    print("Use another guess range")
    return None
  
  for n in range (1,N):
    x_m = (x_a + x_b)/2
    if abs(f(x_m)) < e:
      return x_m, n
    else:
      if f(x_a)*f(x_m) < 0:
        x_b = x_m
      elif f(x_b)*f(x_m) < 0:
        x_a = x_m
  return x_m, n


f = lambda x: 2*x**3-4*x**2-24
a = 2
b = 9

x_root, iteration = bisection(f,a,b)
print('Result : ',"%.4f" % x_root)
print('In %d iteration' %iteration)