import speech_recognition as SR 
import mysql.connector as mc
import pyttsx3
# from word2number import w2n
engine = pyttsx3.init()
engine.setProperty("rate" ,170)


mydb=mc.connect(host = "localhost",user = "root",password = "itisthatis",database = "speech")

def query(voice):
    mycursor = mydb.cursor()
    tablename1 = "voidion"
    t1c1="RegNo"
    t1c2="Name"
    t1c3="Salary"
    tablename2 = "contact"
    t2c1="RegNo"
    t2c2="Phone"

    #ADD data
    if((voice.find("add")!=-1) or (voice.find("insert")!=-1)):
        r = SR.Recognizer()
        try:
            with SR.Microphone() as source:

                engine.say("What is the name of the employee")
                engine.runAndWait()

                print("What is the name of the employee")
                audio = r.listen(source,10,3)
                print("Recognizing...")
                EmpName = r.recognize_google(audio)
                print("User Said : ", EmpName)

                engine.say("What is the register number of the employee")
                engine.runAndWait()

                print("What is the register number of the employee")
                audio = r.listen(source,15,3)
                print("Recognizing...")
                EmpReg= r.recognize_google(audio)
                print("User Said : ", EmpReg)

                engine.say("What is the contact number of the employee")
                engine.runAndWait()

                print("What is the contact number of the employee")
                audio = r.listen(source,20,10)
                print("Recognizing...")
                Cont= r.recognize_google(audio)
                EmpCont=Cont.replace(" ","")
                print("User Said : ", EmpCont)

                engine.say("What is the salary of the employee")
                engine.runAndWait()

                print("What is the salary of the employee")
                audio = r.listen(source,10,3)
                print("Recognizing...")
                Sal= r.recognize_google(audio)
                print("User Said : ", Sal)
                EmpSal=Sal.replace(",","")

                cmd="INSERT INTO voidion (RegNo,Name,Salary) VALUES("+EmpReg+",'"+EmpName+"','"+EmpSal+"')"
                mycursor.execute(cmd)
                mydb.commit()
                
                cmd="INSERT INTO contact (RegNo,Phone) VALUES("+EmpReg+",'"+EmpCont+"')"
                mycursor.execute(cmd)
                mydb.commit()

                engine.say("record Inserted")
                engine.runAndWait()
                print("record Inserted.")
                   
        except SR.UnknownValueError:
            engine.say("Could not understand audio")
            engine.runAndWait()

            print("Could not understand audio")
        except SR.RequestError as e:
            engine.say("Could not request results; {0}".format(e))
            engine.runAndWait()

            print("Could not request results; {0}".format(e))
        except:
            engine.say("Un expected Error")
            engine.runAndWait()

            print("Un expected Error")

    #update
    elif((voice.find("update")!=-1) or (voice.find("change")!=-1)):
        r = SR.Recognizer()
        try:
            with SR.Microphone() as source:

                engine.say("What is the register number of the employee")
                engine.runAndWait()

                print("What is the register number of the employee")
                audio = r.listen(source,15,3)
                print("Recognizing...")
                EmpReg= r.recognize_google(audio)
                print("User Said : ", EmpReg)

                engine.say("What is the NEW name of the employee")
                engine.runAndWait()

                print("What is the NEW name of the employee")
                audio = r.listen(source,10,3)
                print("Recognizing...")
                EmpName = r.recognize_google(audio)
                print("User Said : ", EmpName)

                engine.say("What is the NEW contact number of the employee")
                engine.runAndWait()

                print("What is the NEW contact number of the employee")
                audio = r.listen(source,30,3)
                print("Recognizing...")
                Cont= r.recognize_google(audio)
                EmpCont=Cont.replace(" ","")
                print("User Said : ", EmpCont)

                engine.say("What is the UPDATED salary of the employee")
                engine.runAndWait()

                print("What is the UPDATED salary of the employee")
                audio = r.listen(source,10,3)
                print("Recognizing...")
                Sal= r.recognize_google(audio)
                print("User Said : ", Sal)
                EmpSal=Sal.replace(",","")

                cmd="UPDATE voidion SET RegNo="+EmpReg+",Name='"+EmpName+"',Salary='"+EmpSal+"' WHERE RegNo="+EmpReg
                mycursor.execute(cmd)
                mydb.commit()
                
                cmd="UPDATE contact SET RegNo="+EmpReg+",Phone='"+EmpCont+"' WHERE RegNo="+EmpReg
                mycursor.execute(cmd)
                mydb.commit()

                engine.say("Record Updated")
                engine.runAndWait()
                print("Record Updated.")
                   
        except SR.UnknownValueError:
            engine.say("Could not understand audio")
            engine.runAndWait()
            print("Could not understand audio")
        except SR.RequestError as e:
            engine.say("Could not request results; {0}".format(e))
            engine.runAndWait()
            print("Could not request results; {0}".format(e))
        except:
            engine.say("Un expected Error")
            engine.runAndWait()
            print("Un expected Error")


    #Delete
    elif((voice.find("delete")!=-1) or (voice.find("remove")!=-1)):
        r = SR.Recognizer()
        try:
            with SR.Microphone() as source:

                engine.say("What is the register number of the employee")
                engine.runAndWait()

                print("What is the register number of the employee")
                audio = r.listen(source,15,3)
                print("Recognizing...")
                EmpReg= r.recognize_google(audio)
                print("User Said : ", EmpReg)

                engine.say("Say YES to CONFIRM")
                engine.runAndWait()

                print("Say YES to CONFIRM")
                audio = r.listen(source,15,3)
                print("Recognizing...")
                Conf= r.recognize_google(audio)
                print("User Said : ", Conf)

                if(Conf.find("yes")!=-1):
                    cmd="DELETE FROM voidion WHERE RegNo="+EmpReg
                    mycursor.execute(cmd)
                    mydb.commit()
                    cmd="DELETE FROM contact WHERE RegNo="+EmpReg
                    mycursor.execute(cmd)
                    mydb.commit()

                    engine.say("Record Deleted")
                    engine.runAndWait()
                    print("Record Deleted.")

                else:
                    engine.say("Delete Cancelled")
                    engine.runAndWait()
                    print("Delete Cancelled.")
                    
        except SR.UnknownValueError:
            engine.say("Could not understand audio")
            engine.runAndWait()
            print("Could not understand audio")
        except SR.RequestError as e:
            engine.say("Could not request results; {0}".format(e))
            engine.runAndWait()
            print("Could not request results; {0}".format(e))
        except:
            engine.say("Un expected Error")
            engine.runAndWait()
            print("Un expected Error")

    #display  
    elif ((voice.find("tell") != -1) or (voice.find("display") != -1) or (voice.find("show") != -1) or (voice.find("give") != -1)):
        Regid=""
        for i in voice:
            if i.isdigit():
                Regid=Regid+i
        #all details
        if((voice.find("all") != -1) and ((voice.find("details") != -1) or (voice.find("detail") != -1) or (voice.find("datas") != -1) or (voice.find("data") != -1) )):
            if(Regid.isdigit()):
                cmd="select voidion.Regno, voidion.Name, contact.Phone, voidion.salary from voidion inner join contact on (voidion.Regno=contact.Regno) and voidion.RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Datas\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                else:
                    for i in rows:
                        engine.say("REG NO.     : "+str(i[0]))
                        engine.say("NAME        : "+str(i[1]))
                        engine.say("CONTACT NO. : "+str(i[2]))
                        engine.say("SALARY      : "+str(i[3]))
                        engine.runAndWait()
                        print("REG NO.     : "+str(i[0]))
                        print("NAME        : "+str(i[1]))
                        print("CONTACT NO. : "+str(i[2]))
                        print("SALARY      : "+str(i[3])+"\n")
            else:
                cmd="select voidion.Regno, voidion.Name, contact.Phone, voidion.salary from voidion inner join contact on voidion.Regno=contact.Regno"
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Datas\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                else:
                    for i in rows:
                        engine.say("REG NO.     : "+str(i[0]))
                        engine.say("NAME        : "+str(i[1]))
                        engine.say("CONTACT NO. : "+str(i[2]))
                        engine.say("SALARY      : "+str(i[3]))
                        engine.runAndWait()
                        print("REG NO.     : "+str(i[0]))
                        print("NAME        : "+str(i[1]))
                        print("CONTACT NO. : "+str(i[2]))
                        print("SALARY      : "+str(i[3])+"\n")

        #only names
        elif( (not Regid.isdigit() ) and ((voice.find("all") != -1) or(voice.find("only") != -1)) and ((voice.find("name") != -1) or (voice.find("names") != -1)) and ((voice.find("salary") == -1) or (voice.find("salaries") == -1)) and ((voice.find("contacts") == -1) or (voice.find("contact") == -1) or (voice.find("numbers")==-1) or (voice.find("number")==-1)or (voice.find("phone")==-1))):
            cmd="select Name from voidion"
            mycursor.execute(cmd)
            rows=mycursor.fetchall()
            print("Datas\n")
            if(not rows):
                engine.say("Not Nound")
                engine.runAndWait()
                print("Not Nound\n")
            else:
                for i in rows:
                    engine.say("NAME : "+str(i[0]))
                    engine.runAndWait()
                    print("NAME : "+str(i[0])+"\n")


        #only name and salary (change)
        elif( (not Regid.isdigit() ) and ((voice.find("all") != -1) or(voice.find("only") != -1)) and ((voice.find("name") != -1) or (voice.find("names") != -1)) and ((voice.find("salary") != -1) or (voice.find("salaries") != -1)) and ((voice.find("contacts") == -1) or (voice.find("contact") == -1) or (voice.find("numbers")==-1) or (voice.find("number")==-1)or (voice.find("phone")==-1))):
            cmd="select Name, Salary from voidion"
            mycursor.execute(cmd)
            rows=mycursor.fetchall()
            print("Datas\n")
            if(not rows):
                engine.say("Not Nound")
                engine.runAndWait()
                print("Not Nound\n")
            else:
                for i in rows:
                    engine.say("NAME   : "+str(i[0]))
                    engine.say("SALARY : "+str(i[1]))
                    engine.runAndWait()
                    print("NAME   : "+str(i[0]))
                    print("SALARY : "+str(i[1])+"\n")


        #only name and contact (change)
        elif( (not Regid.isdigit() ) and ((voice.find("all") != -1) or(voice.find("only") != -1)) and ((voice.find("name") != -1) or (voice.find("names") != -1)) and ((voice.find("contact") != -1) or (voice.find("contacts") != -1) or (voice.find("phone") != -1) or (voice.find("number") != -1) or (voice.find("numbers") != -1)) and ((voice.find("salary") == -1) or (voice.find("salaries") == -1))):
            cmd="select voidion.Name, contact.Phone from voidion inner join contact on voidion.Regno=contact.Regno"
            mycursor.execute(cmd)
            rows=mycursor.fetchall()
            print("Datas\n")
            if(not rows):
                engine.say("Not Nound")
                engine.runAndWait()
                print("Not Nound\n")
            else:
                for i in rows:
                    engine.say("NAME    : "+str(i[0]))
                    engine.say("CONTACT : "+str(i[1]))
                    engine.runAndWait()

                    print("NAME    : "+str(i[0]))
                    print("CONTACT : "+str(i[1])+"\n")


        elif(Regid.isdigit()):

            #name alone
            if( (voice.find("name") != -1) and (voice.find("salary") == -1) and ((voice.find("number") == -1) or (voice.find("contact") == -1) or (voice.find("phone") == -1) ) ):
                cmd="select Name from voidion where RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Datas\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                else:
                    for i in rows:
                        engine.say("NAME : "+str(i[0]))
                        engine.runAndWait()
                        print("NAME : "+str(i[0])+"\n")


            #salary alone
            elif((voice.find("salary") != -1) and (voice.find("name") == -1) and ((voice.find("number") == -1) or (voice.find("contact") == -1) or (voice.find("phone") == -1) )):
                cmd="select Salary from voidion where RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Data\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                else:
                    for i in rows:
                        engine.say("SALARY : "+str(i[0]))
                        engine.runAndWait()
                        print("SALARY : "+str(i[0])+"\n")


            #contact alone
            elif( ( (voice.find("name") == -1) and (voice.find("salary") == -1) ) and ( (voice.find("number") != -1) or (voice.find("contact") != -1) or (voice.find("phone") != -1) )):
                cmd="select Phone from contact where RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Datas\n")
                if(not rows):
                    engine.say("Not Found")
                    engine.runAndWait()
                    print("Not Found\n")
                else:
                    for i in rows:
                        engine.say("CONTACT : "+str(i[0]))
                        engine.runAndWait()
                        print("CONTACT : "+str(i[0])+"\n")

            #name and salary
            elif( ( (voice.find("name") != -1) and (voice.find("salary") != -1) ) and ( (voice.find("number") == -1) or (voice.find("contact") == -1) or (voice.find("phone") == -1) )):
                cmd="select Name,Salary from voidion where RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Datas\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                    
                else:
                    for i in rows:
                        engine.say("NAME   : "+str(i[0]))                        
                        engine.say("SALARY : "+str(i[1]))
                        engine.runAndWait()

                        print("NAME   : "+str(i[0]))
                        print("SALARY : "+str(i[1])+"\n")
                        

            #name and contact
            elif( ( (voice.find("name") != -1) and (voice.find("salary") == -1) ) and ( (voice.find("number") != -1) or (voice.find("contact") != -1) or (voice.find("phone") != -1) )):
                cmd="select voidion.Name, contact.Phone from voidion inner join contact on (voidion.Regno=contact.Regno) and voidion.RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Datas\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                    
                else:
                    for i in rows:
                        engine.say("NAME    : "+str(i[0]))
                        engine.say("CONTACT : "+str(i[1]))
                        engine.runAndWait()

                        print("NAME    : "+str(i[0]))
                        print("CONTACT : "+str(i[1])+"\n")
                        

            #salary and contact
            elif( ( (voice.find("name") == -1) and (voice.find("salary") != -1) ) and ( (voice.find("number") != -1) or (voice.find("contact") != -1) or (voice.find("phone") != -1) )):
                cmd=" select voidion.salary, contact.Phone from voidion inner join contact on (voidion.Regno=contact.Regno) and voidion.RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Data is\n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                    

                else:
                    for i in rows:
                        engine.say("SALARY :"+str(i[0]))
                        engine.say("CONTACT : "+str(i[1]))
                        engine.runAndWait()

                        print("SALARY  : " + str(i[0]))
                        print("CONTACT : " + str(i[1]) + "\n")
                        
            #name salary contact
            elif( ( (voice.find("name") != -1) and (voice.find("salary") != -1) ) and ( (voice.find("number") != -1) or (voice.find("contact") != -1) or (voice.find("phone") != -1) )):
                cmd="select voidion.Name, voidion.salary, contact.Phone from voidion inner join contact on (voidion.Regno=contact.Regno) and voidion.RegNo="+Regid
                mycursor.execute(cmd)
                rows=mycursor.fetchall()
                print("Data is \n")
                if(not rows):
                    engine.say("Not Nound")
                    engine.runAndWait()
                    print("Not Nound\n")
                    
                else:
                    for i in rows:
                        engine.say("NAME :"+str(i[0]))                        
                        engine.say("SALARY :"+str(i[1]))
                        engine.say("CONTACT :"+str(i[2]))
                        engine.runAndWait()

                        print("NAME    : " + str(i[0]))
                        print("SALARY  : " + str(i[1]))
                        print("CONTACT : " + str(i[2]) + "\n")
                        
        else:
            engine.say("Could not Identify Query")
            engine.runAndWait()
            print("Could not Identify Query")
    else:
        engine.say("Could not Identify Query")
        engine.runAndWait()
        print("Could not Identify Query")


while(True):
    r = SR.Recognizer()
    with SR.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        
        audio = r.listen(source,20,3)
        print("Recognizing...")
        engine.say("Recognizing")
        engine.runAndWait()
        
        try:
            voicenote = r.recognize_google(audio)
            print("User Said : ", voicenote)
            if(voicenote=="exit" or voicenote=="end" or voicenote=="quit"):

                engine.say("THANKS FOR USING ME")
                engine.runAndWait()
                print("\n THANKS FOR USING ME")
                break
            
            else:
                query(voicenote)
        except SR.UnknownValueError:
            engine.say("Could not understand audio")
            engine.runAndWait()
            print("Could not understand audio...")
            
        except SR.RequestError as e:
            engine.say("Could not request results {0}".format(e))
            engine.runAndWait()
            print("Could not request results; {0}".format(e))