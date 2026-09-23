import matplotlib.pyplot as plt
from Harlacher_S01_Aufg2 import Harlacher_S01_Aufg2

[x,p,dp,pint] = Harlacher_S01_Aufg2([[2,1,3]],-5,5)


y1 = p
y2 = dp
y3 = pint

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.legend(['polynomial','derivative','integral'])
plt.grid()
plt.show()