def postfix_operator(string):
     list=[]
     for i in string:
          if i.isdigit():
               list.append(int(i))
          elif i=="+" or i== "-" or i=="*" or i=="/":
               num1=list.pop()
               num2=list.pop()
               if(i=='+'):
                    list.append(num1+num2)
               if(i=='-'):
                    list.append(num1-num2)
               if(i=='*'):
                    list.append(num1*num2)
               if(i=="/"):
                    list.append(num1/num2)
          else:
               return "invalid"
     return list[0]




