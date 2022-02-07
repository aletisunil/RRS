from cgitb import text
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

        self.title_font = tkfont.Font(family='Helvetica', size=15, weight="bold", slant="italic")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Railway Reservation System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Retrive Info by Name",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Retrive Info by Age",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Retrive no.of passengers",
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Retrive bookings by date",
                            command=lambda: controller.show_frame("PageFour"))
        button5 = tk.Button(self, text="Retrive bookings by Train name",
                            command=lambda: controller.show_frame("PageFive"))
        
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        

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
                    

        button3=tk.Button(self, text="Submit",command=lambda:infoByName())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",command=lambda: controller.show_frame("StartPage"))
        button.pack(side="bottom")


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
                
                
                
                
            
                
        
                
        
        
            
        
        button3=tk.Button(self, text="Submit",command=lambda:infoByAge())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",command=lambda:controller.show_frame("StartPage"))
        button.pack(side='bottom')
       
       


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
        
        
        button = tk.Button(self, text="Home Page",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFour(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter Date to retrieve bookings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        Label1=tk.Label(self, text="Date")
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
           
        button3=tk.Button(self, text="Submit",command=lambda:infoDay())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",command=lambda: controller.show_frame("StartPage"))
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
        
        
        # datatype of menu text
        clicked = tk.StringVar()
        
        # initial menu text
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
           
        button3=tk.Button(self, text="Submit",command=lambda:infoTrainName())
        button3.pack(side='top')
        button4=tk.Button(self, text="clear",command=lambda:delete())
        button4.pack(side='top')
        button = tk.Button(self, text="Home Page",command=lambda: controller.show_frame("StartPage"))
        button.pack()


