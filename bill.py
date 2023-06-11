import main_menu
import bill
#bill
def BI_MENU() :
      print("-----------------------------------------------------")
      print("                 BILL")
      print("--------------------------------")
      ans="y"
      while ans=="y" :
            bill.bill_data()
            ans=input("want to print more bill?(y/n)=")
def bill_data() :
      print("S.NO.       NAME                FEES")
      print(" 1.      Room Charge         750 per day")
      print(" 2.      Bed charge          500 per day")
      print(" 3.      Doctor charge       500 per patient")
      print(" 4.      Blood Test charge   300 per person")
      print(" 5.      B.P. Test           300 per person")
      print(" 6.      Ultrasound          700 per person")
      print(" 7.      C.T. Scan           1500 per person")
      print(" 8.      Sugar Test          500 per person")
      print("-------------------------------------------------")
      a=input("enter name=")
      b=int(input("enter room charge="))
      c=int(input("enter bed charge="))
      d=int(input("enter test charge="))
      e=int(input("enter doctor fee="))
      f=int(input("enter medicine amount="))
      g=int(input("mob.no.="))
      i=b+c+d+e+f
      print("--------------------------------------------")
      print("Mr./Mrs.",a,"your total amount is Rs",i)
      print("-----------------------------------------------")
      print("            THANKYOU FOR COMING")
      print("-----------------------------------------------")

      
