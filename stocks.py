import sys,numpy,shlex,csv,os

def lagrange(data):
   points=[]
   for i in np.arange(-5.,5.,(10./(n))):
      points.append([i,1./(1.+i**2.)])
   points.append([5.,1./(1.+5.**2.)])
   P = 0
   start = time.time()
   for i in points:
      ls = points[:]
      ls.remove(i)
      L  = 1
      for k in ls:
#         x = sympy.Symbol('x')
         x = 1
         y = (x-k[0])/(i[0]-k[0])
         L = L * y
#      print f
      f2= sympy.simplify(L)
#      print f2
      P = P + (i[1]*L)
   end = time.time()
   Pn = sympy.simplify(P)
   print "The legrange Polynomail is: " + str(Pn)
   print "It took  " + str(end-start) + " seconds to calculate"
   Pu = sympy.lambdify(x, P, 'numpy')
   Pe = i[1]- Pu(i[0])
   print "The error is: " +  str(Pe)
   return Pu


def getInput():
   header = map(int,shlex.split(sys.stdin.readline()))
   newdata = []
   for k in xrange(header[1]):
      j = sys.stdin.readline()
      newdata.append(shlex.split(j))
   print newdata
   if( not os.path.isfile("data.csv") ):
      f = open("data.csv","wb")
      out = csv.writer(f, delimiter=',',dialect='excel')
      for row in newdata:
         out.writerow(row)
      f.close
   return newdata

def updatedata(newdata):
   fw = open("data.csv","rb")
   cr = csv.reader(fw,delimiter=',',dialect='excel')
   completedata = []
   for row in cr:
        completedata.append(list(row))
   print completedata
   fw.close
   for row in completedata:
      for row2 in newdata:
         if(row[0] == row2[0]):
            row.append(row2[-1])
   f = open("data.csv","wb")
   out = csv.writer(f, delimiter=',',dialect='excel')
   for row in completedata:
      out.writerow(row)
   f.close

def buy_or_sell():
   fw = open("data.csv","rb")
   cr = csv.reader(fw,delimiter=',',dialect='excel')
   completedata = []
   for row in cr:
        completedata.append(list(row))
   fw.close
   

if( not os.path.isfile("data.csv") ):
   getInput()
else:
   updatedata(getInput())

buy_or_sell()
