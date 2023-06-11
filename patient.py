import main_menu
import patient
#module(patient data)
def PATI_MENU():
      while True :
            print("------------------------------------------------------------------------------")
            print("                                      PATIENT DATA")
            print("                                    ****************")
            print("enter your choice=")
            print("1. Patient Registration")
            print("2. Show Patient Detail")
            print("3. Search From Patient Record")
            print("4. Update patient data")
            print("5. Go To Mainmenu")
            a=int(input("enter your choice="))
            if a==1 :
                  patient.registration()
            elif a==2 :
                  patient.show()
            elif a==3 :
                  patient.search()
            elif a==4 :
                  patient.update()
            elif a==5:
                  return
            else:
                  print("EROOR: Invalid choice ,try again...")
                  conti="Press any key to return to main menu.."
def registration() :
      import pickle
      a={}
      b=open("registration.dat","wb")
      ans="y"
      while ans=="y" :
            print("-------------------------------------")
            c=int(input("enter s.no.="))
            d=input("enter patient name=")
            e=input("enter guardian name=")
            f=int(input("age="))
            g=input("disease=")
            h=int(input("enter mobile no.="))
            a["s.no."]=c
            a["name"]=d
            a["guardian"]=e
            a["age"]=f
            a["disease"]=g
            a["mob.no."]=h
            pickle.dump(a,b)
            ans=input("want to enter more data?(y/n)=")
      b.close()
def show() :
      import pickle
      emp={}
      empfile=open("registration.dat","rb")
      try:
            while True:
                  emp=pickle.load(empfile)
                  print(emp)
      except:
            empfile.close()
def search():
      import pickle
      a={}
      found=False
      b=open("registration.dat","rb")
      ans="y"
      while ans=="y" :
            print("----------------------------------")
            c=input("enter name which you want to search=")
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
                  ans=input("want to search more data?(y/n)=")
                  b.close()
def update() :
      print("--------------------------------------------")
      print("1. Want to update name")
      print("2. Want to update mobile no.")
      print("--------------------------------------")
      a=int(input("enter your choice="))
      if a==1 :
            import pickle
            a={}
            f=False
            upd=open("registration.dat","rb+")
            try:
                  while True:
                        r=upd.tell()
                        a=pickle.load(upd)
                        y=int(input("s.no.="))
                        z=input("enter changing name=")
                        if a["s.no."]==y:
                              a["name"]=z
                              upd.seek(r)
                              pickle.dump(a,upd)
                              f=True
            except:
                  if f==False:
                        print("sorry,no matching record file found.")
                  else:
                        print("Record successfuly updated")
                  upd.close()
      elif a==2 :
            import pickle
            a={}
            f=False
            upd=open("registration.dat","rb+")
            try:
                  while True:
                        r=upd.tell()
                        a=pickle.load(upd)
                        y=int(input("s.no."))
                        z=int(input("enter changing number="))
                        if a["s.no."]==y:
                              a["mob.no."]=z
                              upd.seek(r)
                              pickle.dump(a,upd)
                              f=True
            except:
                  if f==False:
                        print("sorry,no matching record file found.")
                  else:
                        print("Record successfuly updated")
                  upd.close()

