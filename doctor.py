import main_menu
import doctor
#doctor data
def DOC_MENU() :
      while True :
            print("-----------------------------------------------------------------------")
            print("                         DOCTORS Data ")
            print("                        **************")
            print("-------------------------------------------------------------------------")
            print("enter your choice")
            print("1. Add Doctor")
            print("2. See all doctors data")
            print("3. Search Doctor")
            print("4. Go To Mainmenu")
            print("-----------------------------")
            a=int(input("enter your choice here="))
            if a==1 :
                  doctor.add()
            elif a==2:
                  doctor.search()
            elif a==3 :
                  doctor.show()
            elif a==4:
                  return
            else:
                  print("EROOR: Invalid choice ,try again...")
                  conti="Press any key to return to main menu.."
def add() :
      import pickle
      a={}
      b=open("doctor.dat","wb")
      ans="y"
      while ans=="y" :
            print("---------------------------------------------------")
            c=int(input("enter s.no.="))
            d=input("enter doctor name=")
            e=input("enter department name=")
            f=int(input("age="))
            g=input("address=")
            h=int(input("enter mobile no.="))
            i=int(input("enter salary ="))
            a["s.no."]=c
            a["name"]=d
            a["deparment"]=e
            a["age"]=f
            a["mob.no."]=g
            a["address"]=h
            a["salary"]=i
            pickle.dump(a,b)
            print("-----------------------------------")
            ans=input("want to enter more data?(y/n)=")
      b.close()
def search():
      import pickle
      a={}
      found=False
      b=open("doctor.dat","rb")
      ans="y"
      while ans=="y" :
            print("-------------------------------------")
            c=input("enter doctor name which you want to search=")
            try:
                  a=pickle.load(b)
                  if a["name"]==c :
                        print(a)
                        found=True
            except:
                  if found==False :
                        print("no such record found in file")
                  else :
                        print("search successful")
                        print("-----------------------------------")
                  ans=input("want to search more data?(y/n)=")
                  b.close()
def show() :
      import pickle
      a={}
      b=open("doctor.dat","rb")
      try :
            while True :
                  a=pickle.load(b)
                  print("-----------------------------------")
                  print(a)
      except :
            b.close()

      
            
