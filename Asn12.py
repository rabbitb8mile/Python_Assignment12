import package.add as a 
import package.subtract as s
import package.multiple as m
import package.divide as d
import package.modulars as mo


n="1"
while n=="1":
     print("\n1)Add \n2)Subtract \n3)Multiply \n4)Divide\n5)Modulars")
     ch = int(input("Enter your Choice: "))
     if ch==1:
         a.p_add()
     elif ch==2:
         s.p_sub()
     elif ch==3:
         m.p_mul()
     elif ch==4:
         d.p_div()
     elif ch==5:
         mo.p_mod()
     else:
         print("invalid choice ")
     n=input("press 1 to continue or enter to exit ")
     if n!="1":
         exit()
