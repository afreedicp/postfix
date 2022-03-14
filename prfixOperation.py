def prefix_operator(s):
     list=[]
     for i in s:
          if i.isdigit():
               list.append(int(i))
          elif i=="+" or i== "-" or i=="*" or i=="/":
               num1=list.pop()
               num2=list.pop()
               if(i=='+'):
                    list.append(int(num1+num2))
               if(i=='-'):
                    list.append(int(num1-num2))
               if(i=='*'):
                    list.append(int(num1*num2))
               if(i=="/"):
                    list.append(int(num1/num2))
               return list[0]
          else:
               return "invalid"




