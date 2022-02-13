import tkinter as tk
from tkinter import ttk
import mysql.connector                
from tkinter import font  as tkfont 


my_conn= mysql.connector.connect(user='root', password='rootroot',
                              host='127.0.0.1',
                              database='RRS')

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('RRS')
        self.geometry('1200x650')
        self.title_font = tkfont.Font(family='Helvetica', size=15, weight="bold", slant="italic")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Railway Reservation System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Retrive Info by Name",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Retrive Info by Age",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Retrive no.of passengers",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Retrive bookings by date",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageFour"))
        button5 = tk.Button(self, text="Retrive bookings by Train name",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageFive"))
        button6 = tk.Button(self, text="Make a reservation",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageSix"))
        button7 = tk.Button(self, text="Cancel a reservation",width=25,highlightbackground='#00cec9',
                            command=lambda: controller.show_frame("PageSeven"))
        button1.pack(side='top',pady=8)
        button2.pack(side='top',pady=8)
        button3.pack(side='top',pady=8)
        button4.pack(side='top',pady=8)
        button5.pack(side='top',pady=8)
        button6.pack(side='top',pady=8)
        button7.pack(side='top',pady=8)
        
        

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter First & Last name to retrieve bookings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label1=tk.Label(self, text="First name")
        Label1.pack(side="top")
        Entry1=tk.Entry(self)
        Entry1.pack(side="top")

        Label2=tk.Label(self, text="Second name")
        Label2.pack(side="top")
        Entry2=tk.Entry(self)
        Entry2.pack(side="top")

        cursor = my_conn.cursor()

        
        def delete():
            self.tree.destroy()   
    
            
        
        
        def infoByName():
            query="SELECT * FROM  Passenger where firstName='{0}' and lastName='{1}'".format(Entry1.get(),Entry2.get())
            cursor.execute(query)
            myresult = cursor.fetchall()
            res = [list(ele) for ele in myresult]
            if len(myresult)!=0:
                columns = ('firstName', 'lastName', 'Age','Address','status','TrainNum','DOJ','category')
                self.tree = ttk.Treeview(self, columns=columns, show='headings')
                self.tree.pack()
                self.tree.heading('firstName', text='First Name')
                self.tree.heading('lastName', text='Last Name')
                self.tree.heading('Age', text='Age')
                self.tree.heading('Address', text='Address')
                self.tree.heading('status', text='Status')
                self.tree.heading('TrainNum', text='Train Number')
                self.tree.heading('DOJ', text='Date of Journey')
                self.tree.heading('category', text='Category')
                for i in res:
                    self.tree.insert('', tk.END, values=i)
            
            else:
                
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                
                self.tree.insert('', 'end', text=" No Records found here ")
                    

        button3=tk.Button(self, text="Submit",highlightbackground='#6c5ce7',command=lambda:infoByName())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",highlightbackground='#636e72',command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top",pady=20)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter Minimum & Maximum Age to retrieve information", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        Label1=tk.Label(self, text="Min Age")
        Label1.pack(side="top")
        Entry1=tk.Entry(self)
        Entry1.pack(side="top")

        Label2=tk.Label(self, text="Max Age")
        Label2.pack(side="top")
        Entry2=tk.Entry(self)
        Entry2.pack(side="top")

        cursor = my_conn.cursor()
        
        
        
        def delete():
            self.tree.destroy()
              
            
        
       
        
        
        def infoByAge():
            query=("""SELECT Train.TrainNum, Train.TrainName, Train.Source, Train.Dest, Passenger.firstName, Passenger.Address, Passenger.category, Passenger.status FROM Passenger
                  INNER JOIN Train ON Passenger.TrainNum=Train.TrainNum where Passenger.Age between '{0}' and '{1}';""").format(int(Entry1.get()),int(Entry2.get()))
            cursor.execute(query)
            myresult = cursor.fetchall()
            
            
            res = [list(ele) for ele in myresult]
            if len(myresult)!=0:
                columns = ('TrainNum', 'TrainName', 'Source','Dest','firstName','Address','category','status')
                self.tree = ttk.Treeview(self, columns=columns, show='headings')
                self.tree.pack()
                self.tree.heading('TrainNum', text='Train number')
                self.tree.heading('TrainName', text='Train Name')
                self.tree.heading('Source', text='Source')
                self.tree.heading('Dest', text='Destination')
                self.tree.heading('firstName', text='Frist name')
                self.tree.heading('Address', text='Address')
                self.tree.heading('category', text='Category')
                self.tree.heading('status', text='Status')
                for i in res:
                    self.tree.insert('', tk.END, values=i)
                
                
            else:
                
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                
                self.tree.insert('', 'end', text=" No Records found here ")
                
                
                
                
            
                
        
                
        
        
            
        
        button3=tk.Button(self, text="Submit",highlightbackground='#6c5ce7',command=lambda:infoByAge())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",highlightbackground='#636e72',command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda:controller.show_frame("StartPage"))
        button.pack(side='top')
       
       


class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Get no.of Passengers", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        
        cursor = my_conn.cursor()
        
        
        
        def delete():
            self.tree.destroy()   
        
        

        
        query=("SELECT Train.TrainNum, count(Passenger.firstName) FROM Passenger INNER JOIN Train ON Passenger.TrainNum=Train.TrainNum group by Train.TrainNum;")
        cursor.execute(query)
        myresult = cursor.fetchall()
        
        
        res = [list(ele) for ele in myresult]
        if myresult!=None:
            columns = ('TrainNum', 'Count')
            self.tree = ttk.Treeview(self, columns=columns, show='headings')
            self.tree.pack()
            self.tree.heading('TrainNum', text='Train number')
            self.tree.heading('Count', text='Count')
            
            for i in res:
                self.tree.insert('', tk.END, values=i)
    
        else:
                
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                self.tree.insert('', 'end', text=" No Records found here ")
        
        
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFour(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter Date to retrieve bookings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        Label1=tk.Label(self, text="Date (YYYY-MM-DD)")
        Label1.pack(side="top")
        Entry1=tk.Entry(self)
        Entry1.pack(side="top")
        cursor = my_conn.cursor()
        def delete():
            self.tree.destroy()   
        def infoDay():
            query=("select * from Passenger where DOJ='{0}' and status='confirmed';").format(Entry1.get())
            cursor.execute(query)
            myresult = cursor.fetchall()
            print(myresult)
            res = [list(ele) for ele in myresult]
            if myresult!=None:
                columns = ('firstName', 'lastName', 'Age','Address','status','TrainNum','DOJ','category')
                self.tree = ttk.Treeview(self, columns=columns, show='headings')
                self.tree.pack()
                self.tree.heading('firstName', text='First Name')
                self.tree.heading('lastName', text='Last Name')
                self.tree.heading('Age', text='Age')
                self.tree.heading('Address', text='Address')
                self.tree.heading('status', text='Status')
                self.tree.heading('TrainNum', text='Train Number')
                self.tree.heading('DOJ', text='Date of Journey')
                self.tree.heading('category', text='Category')
                for i in res:
                    self.tree.insert('', tk.END, values=i)
        
            else:
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                self.tree.insert('', 'end', text=" No Records found here ")
           
        button3=tk.Button(self, text="Submit",highlightbackground='#6c5ce7',command=lambda:infoDay())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",highlightbackground='#636e72',command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageFive(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter Train name to retrieve bookings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        Label1=tk.Label(self, text="Choose Train Name")
        Label1.pack(side="top")
        
        
  
        # Dropdown menu options
        options = [
            "AUHO",
            "CHHY",
            "CHNY",
            "NYCH",
            "SASA"
        ]
        
        
       
        clicked = tk.StringVar()
        clicked.set( "AUHO" )
        
        # Create Dropdown menu
        drop = tk.OptionMenu( self , clicked , *options )
        drop.pack()
        cursor = my_conn.cursor()
        
        def delete():
            self.tree.destroy()   
        def infoTrainName():
            query=("SELECT Passenger.firstName, Passenger.lastName, Passenger.Age,Passenger.Address, Passenger.DOJ, Passenger.category FROM Passenger INNER JOIN Train ON Passenger.TrainNum=Train.TrainNum where Train.TrainName='{0}' and Passenger.status='confirmed';").format(clicked.get())
            cursor.execute(query)
            myresult = cursor.fetchall()
            print(myresult)
            
            
            res = [list(ele) for ele in myresult]
            if myresult!=None:
                columns = ('firstName', 'lastName', 'Age','Address','DOJ','category')
                self.tree = ttk.Treeview(self, columns=columns, show='headings')
                self.tree.pack()
                self.tree.heading('firstName', text='First Name')
                self.tree.heading('lastName', text='Last Name')
                self.tree.heading('Age', text='Age')
                self.tree.heading('Address', text='Address')
                self.tree.heading('DOJ', text='Date of Journey')
                self.tree.heading('category', text='Category')
                for i in res:
                    self.tree.insert('', tk.END, values=i)
        
            else:
                
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                
                self.tree.insert('', 'end', text=" No Records found here ")
           
        button3=tk.Button(self, text="Submit",highlightbackground='#6c5ce7',command=lambda:infoTrainName())
        button3.pack(side='top',pady=14)
        button4=tk.Button(self, text="clear",highlightbackground='#636e72',command=lambda:delete())
        button4.pack(side='top',pady=14)
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageSix(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Make a reservation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        Label1=tk.Label(self, text="First name")
        Label1.pack(side="top")
        Entry1=tk.Entry(self)
        Entry1.pack(side="top")

        Label2=tk.Label(self, text="Last name")
        Label2.pack(side="top")
        Entry2=tk.Entry(self)
        Entry2.pack(side="top")

        Label3=tk.Label(self, text="Age")
        Label3.pack(side="top")
        Entry3=tk.Entry(self)
        Entry3.pack(side="top")

        Label4=tk.Label(self, text="Address")
        Label4.pack(side="top")
        Entry4=tk.Entry(self)
        Entry4.pack(side="top")
        """
        Label5=tk.Label(self, text="status")
        Label5.pack(side="top")
        Entry5=tk.Entry(self)
        Entry5.pack(side="top")
        """
        Label6=tk.Label(self, text="TrainNum")
        Label6.pack(side="top")
        options1 = [
            "456",
            "789",
            "123",
            "111",
            "222"
        ] 
        # datatype of menu text
        clicked1 = tk.StringVar()
        
        # initial menu text
        clicked1.set("456")
        
        # Create Dropdown menu
        drop1 = tk.OptionMenu( self , clicked1 , *options1 )
        drop1.pack(side='top')

        Label7=tk.Label(self, text="DOJ")
        Label7.pack(side="top")
        Entry7=tk.Entry(self)
        Entry7.pack(side="top")

        Label8=tk.Label(self, text="category")
        Label8.pack(side="top")
        options2 = [
            "General",
            "Premium"
        ]
        
        
        # datatype of menu text
        clicked2 = tk.StringVar()
        
        # initial menu text
        clicked2.set("General")
        
        # Create Dropdown menu
        drop2 = tk.OptionMenu( self , clicked2 , *options2 )
        drop2.pack(side='top')
       
        def booking():
            cursor = my_conn.cursor()
            querry=("select count(*) from Passenger where TrainNum='{0}' and category='{1}';").format(int(clicked1.get()),clicked2.get())
            cursor.execute(querry)
            result = cursor.fetchall()
            seats=int(result[0][0])
        
            if seats<=10:
                temp='Confirmed'
            else:    
                temp='Waiting'
            query="INSERT INTO Passenger values(%s,%s,%s,%s,%s,%s,%s,%s)"
            value=(Entry1.get(),Entry2.get(),Entry3.get(),Entry4.get(),temp,int(clicked1.get()),Entry7.get(),clicked2.get())
            cursor.execute(query, value)
            my_conn.commit()
            print(cursor.rowcount, "record inserted.")
            
            query3= ("select count(*) from Passenger where TrainNum='{0}' and DOJ='{1}' and status='Confirmed';").format(int(clicked1.get()),Entry7.get())
            cursor.execute(query3)
            result3=cursor.fetchall()
            noOfSeats=int(result3[0][0])
            
            query2=("SELECT EXISTS(SELECT * from trainStatus WHERE TrainNum='{0}' and DOJ='{1}');").format(int(clicked1.get()),Entry7.get())
            cursor.execute(query2)
            result2=cursor.fetchall()
            opt=int(result2[0][0])
            if opt==0:
                query1="INSERT INTO trainStatus values(%s,%s,%s,%s)"
                seatsavailable=20-noOfSeats
                value1=(int(clicked1.get()),Entry7.get(),seatsavailable,noOfSeats)    
                cursor.execute(query1, value1)
                my_conn.commit()
            elif opt==1:
                sql3 = ("UPDATE trainStatus SET seatsAvailable = %s and seatsOccupied= %s where TrainNum= %s and DOJ= %s")
                val3=(int(20-noOfSeats),int(noOfSeats),int(clicked1.get()),Entry7.get())
                cursor.execute(sql3,val3)
                my_conn.commit()
            


            query=("select * from Passenger")
            cursor.execute(query)
            myresult = cursor.fetchall()
            
            res = [list(ele) for ele in myresult]
            if myresult!=None:
                columns = ('firstName', 'lastName', 'Age','Address','status','TrainNum','DOJ','category')
                self.tree = ttk.Treeview(self, columns=columns, show='headings')
                self.tree.pack()
                self.tree.heading('firstName', text='First Name')
                self.tree.heading('lastName', text='Last Name')
                self.tree.heading('Age', text='Age')
                self.tree.heading('Address', text='Address')
                self.tree.heading('status', text='Status')
                self.tree.heading('TrainNum', text='Train Number')
                self.tree.heading('DOJ', text='Date of Journey')
                self.tree.heading('category', text='Category')
                for i in res:
                    self.tree.insert('', tk.END, values=i)
        
            else:
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                self.tree.insert('', 'end', text=" No Records found here ")
        
        def delete():
            self.tree.destroy()    
        button3=tk.Button(self, text="Submit",highlightbackground='#6c5ce7',command=lambda:booking())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",highlightbackground='#636e72',command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageSeven(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Cancel a ticket", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        Label1=tk.Label(self, text="First name")
        Label1.pack(side="top")
        Entry1=tk.Entry(self)
        Entry1.pack(side="top")

        Label2=tk.Label(self, text="Last name")
        Label2.pack(side="top")
        Entry2=tk.Entry(self)
        Entry2.pack(side="top")

        Label6=tk.Label(self, text="TrainNum")
        Label6.pack(side="top")
        options1 = [
            "456",
            "789",
            "123",
            "111",
            "222"
        ] 
        # datatype of menu text
        clicked1 = tk.StringVar()
        
        # initial menu text
        clicked1.set("456")
        
        # Create Dropdown menu
        drop1 = tk.OptionMenu( self , clicked1 , *options1 )
        drop1.pack(side='top')

        Label7=tk.Label(self, text="DOJ")
        Label7.pack(side="top")
        Entry7=tk.Entry(self)
        Entry7.pack(side="top")

       
        def cancel():
            cursor = my_conn.cursor()
            sql = ("DELETE FROM Passenger where firstName='{0}' and lastName='{1}' and trainNum='{2}' and DOJ='{3}';").format(Entry1.get(),Entry2.get(),clicked1.get(),Entry7.get())
            cursor.execute(sql)
            my_conn.commit()
            print(cursor.rowcount, "record(s) deleted")

            waitingquery=("SELECT count(Passenger.status) FROM Passenger INNER JOIN Train ON Passenger.TrainNum=Train.TrainNum where Passenger.status='waiting' and Passenger.trainNum='{0}' and Passenger.DOJ='{1}';").format(clicked1.get(),Entry7.get())
            cursor.execute(waitingquery)
            myresult1 = cursor.fetchall()
            if int(myresult1[0][0]) >0:
                sql2 = ("UPDATE Passenger SET status = 'Confirmed' WHERE status = 'Waiting' and trainNum='{0}' and DOJ='{1}' LIMIT 1;").format(clicked1.get(),Entry7.get())
                cursor.execute(sql2)
                my_conn.commit()
                print(cursor.rowcount, "record(s) updated")

            
            query=("select * from Passenger where trainNum='{0}' and DOJ='{1}'").format(clicked1.get(),Entry7.get())
            cursor.execute(query)
            myresult = cursor.fetchall()
            print(myresult)
            res = [list(ele) for ele in myresult]
            if myresult!=None:
                columns = ('firstName', 'lastName', 'Age','Address','status','TrainNum','DOJ','category')
                self.tree = ttk.Treeview(self, columns=columns, show='headings')
                self.tree.pack()
                self.tree.heading('firstName', text='First Name')
                self.tree.heading('lastName', text='Last Name')
                self.tree.heading('Age', text='Age')
                self.tree.heading('Address', text='Address')
                self.tree.heading('status', text='Status')
                self.tree.heading('TrainNum', text='Train Number')
                self.tree.heading('DOJ', text='Date of Journey')
                self.tree.heading('category', text='Category')
                for i in res:
                    self.tree.insert('', tk.END, values=i)
        
            else:
                self.tree = ttk.Treeview(self)
                self.tree.pack()
                self.tree.insert('', 'end', text=" No Records found here ")
        
        def delete():
            self.tree.destroy()    
        button3=tk.Button(self, text="Submit",highlightbackground='#6c5ce7',command=lambda:cancel())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",highlightbackground='#636e72',command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",highlightbackground='#273c75',command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
