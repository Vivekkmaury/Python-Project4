import main_menu
import appointment
#appointment
def APP_MENU():
      while True :
            print("---------------------------------------")
            print("                      APPOINTMENT")
            print("--------------------------------------------")
            print("1. Appointment")
            print("2. show Appointment data")
            print("3. Go To Mainmenu")
            print("-------------------------------------------")
            a=int(input("enter your choice="))
            if a==1 :
                  appointment.appoint()
            elif a==2 :
                  appointment.show()
            elif a==3:
                  return
            else:
                  print("EROOR: Invalid choice ,try again...")
                  conti="Press any key to return to main menu.."
def appoint() :
      import csv
      a=open("appointment.csv","w")
      b=csv.writer(a)
      b.writerow(["s.no","name","father_name","doctor_name","mob.no."])
      ans="y"
      while ans=="y" :
            print("-----------------------------------")
            c=int(input("enter s.no.="))
            d=input("enter patient name=")
            e=input("enter father name=")
            f=input("enter doctor name=")
            g=int(input("enter mob. no.="))
            h=[c,d,e,f,g]
            b.writerow(h)
            print("--------------------------------------")
            ans=input("want to enter more data?(y/n)")
            print("Successfully entered")
      a.close()
def show() :
      import csv
      with open("appointment.csv","r",newline='\r\n') as a :
            b=csv.reader(a)
            for c in b :
                  print("----------------------------------")
                  print(c)
      
