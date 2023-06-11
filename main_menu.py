import main_menu
import appointment
import patient
import doctor
import bill
while True :
      #Home Page Of Hospital With Main Menus:-
      print("******************************************************************************")
      print("*                                     HOSPITAL MANAGEMENT SYSTEM                                       *")
      print("******************************************************************************")
      print("*                                        VARANASI HOSPITAL                                                             *")
      print("*                  --*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--                 *")
      print("*                                     Kerakatpur, Lohta road, Varanasi                                              *")
      print("*                  --*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--                 *")
      print("******************************************************************************")
      print(" ")
      print("=> Choose your desired option :-")
      print("1. About Hospital -")
      print("2. Facilities -")
      print("3. Appointment -")
      print("4. Patient Data -")
      print("5. Doctor Data -")
      print("6. Medicine Store -")
      print("7. Bill -")
      print("8. Exit -")
      print("----------------------------------------------------------------------------------------------")
      print(" ")
      choice=int(input("Enter Your Choice :-"))
      if choice==1:
            a=open("about.txt",'r')
            b=a.read()
            print(b)
            a.close()
      if choice==2 :
            a=open("facility.txt",'r')
            b=a.read()
            print(b)
            a.close()
      if choice==6 :
            a=open("medicine.txt",'r')
            b=a.read()
            print(b)
            a.close()
      if choice==3 :
            appointment.APP_MENU()
      if choice==4:
            patient.PATI_MENU()
      if choice==5 :
            doctor.DOC_MENU()
      if choice==7 :
            bill.BI_MENU()
      if choice==8 :
            break
      else :
            print("ERROR-Invalid Choice.....")
            conti="press any key"
    

