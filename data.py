from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime
from datetime import timedelta
import os,pickle,time,getpass,shutil,sqlite3

dir_path= os.path.dirname(os.path.realpath(__file__)) #to take File path`
db_path=f"{dir_path}\\Data\\AppData.db"

dir_path= os.path.dirname(os.path.realpath(__file__)) #to take File path`
class CommonFunction():
    def t_time(self):
        with open(f"{dir_path}\\Data\\Data_EM.dat",'wb') as time:
                pass
        class_data=Data()
        class_data.counter_label()
        total_time=self.sqlite_cmd(path=db_path,data=None,e_type='one',command="""SELECT * FROM CounterData WHERE name IS counter""",capture_output=True)
        timet = datetime.fromtimestamp(total_time)
        time_t = timet.strftime("%H:%M:%S")
        self.time_t_var.set(time_t)
    def check_time_format(self,text,start_time_var=None,compare=False,end_time_var=None):
        """
        Checks time format i.e if its in 24hr format, not char ect
        """
        if compare==True and end_time_var!=None and start_time_var!=None:
            if start_time_var==end_time_var:
                mb.askretrycancel("Your Health Campanian - ERROR","Please do not Enter same time in both Entries.\nExample: entry1=00:00:00, \nentry2=23:59:59\nIf you want to monitor for 24 Hours (24 - Hour format only)")
                return False
        else:
            pass
        a=text.split(":")
        try:
            for i in a:
                b=int(i)
                if int(a[0])<0 or int(a[0])>24 or int(a[1])<0 or int(a[1])>60 or int(a[2])<0 or int(a[2])>60:
                    mb.askretrycancel("Your Health Campanian - ERROR","Invaild Time, please retry")
                    return False
                else:
                    return True
        except:
            mb.askretrycancel("Your Health Campanian - ERROR","Invaild Time, please retry")
            return False

    def time_format(self,var,widget):
        """
        Adds ':' to every 2nd and 5th index, also limits data entry to 6 numbers(total 8 including ':')
        """
        a=var.get()
        text_len=len(a)-1
        if text_len+1>=9:
            var.set(a[0:8])
        if text_len==2 and ":" not in a[2] or text_len==5 and ":" not in a[5]:
            widget.insert(text_len,":")
        else:
            pass
    
    def round_rectangle(canvas,x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
            x1+radius, y1,
            x2-radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1+radius,
            x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def sqlite_cmd(self,path,command,e_type='one',data=None,show_s_succes=False,capture_output=False,output_cmd=None,commit=False):
        conn=sqlite3.connect(path)
        c=conn.cursor()
        if e_type=='one':
            if data !=None:
                c.execute(command,data)
            else:
                c.execute(command)
        else:
            c.executemany(command,data)
        if commit==True:
            conn.commit()
        if show_s_succes==True:
            mb.showinfo("Succesfull","Data Saved Successfully")
        if capture_output==True:
            r_item=c.fetchall()
            return r_item


class Data(CommonFunction):
    def counter_label(self):
        file_exits=os.path.isfile(F"{dir_path}\\Data\\Data_EM.dat")
        counter=self.sqlite_cmd(path=db_path,e_type='one',capture_output=True,command="""SELECT * FROM CounterData""")
        print(counter)
        if counter==[]:
            counter = 66600
            self.sqlite_cmd(path=db_path,e_type='one',capture_output=False,commit=True,command=f"""INSERT INTO CounterData VALUES("counter",{counter})""")
            self.counter_label()
        else:
            
            shown=False
            while file_exits==False:
                timet = datetime.fromtimestamp(counter)
                time_t = timet.strftime("%H:%M:%S")
                t_time_1=time_t.split(":")
                file_exits=os.path.isfile(F"{dir_path}\\Data\\Data_EM.dat")
                time.sleep(1)
                counter+=1
                time_now=datetime.now()
                time_now=time_now.strftime("%H:%M:%S")
                t1 = timedelta(hours=int(limit_1[0]), minutes=int(limit_1[1]),seconds=int(limit_1[2]))
                t2 = timedelta(hours=int(t_time_1[0]), minutes=int(t_time_1[1]),seconds=int(t_time_1[2]))
                dif=t1-t2
                with open(f"{dir_path}\\Data\\CounterData.dat",'wb') as time_1:
                    pickle.dump(counter,time_1)
                if time_now==end_time_main or time_now==start_time_main:
                    counter = 66600
                    with open(f"{dir_path}\\Data\\CounterData.dat",'wb') as time_1:
                        pickle.dump(counter,time_1)
                if "00:00:00" or "0:00:00" or "-" in dif and shown==False:
                    mb.showinfo("Daily Screen limit execeded","Your daily Screen time limit is over.")
                    shown=True

    def stopwatch(self):
        index=0
        with open(f"{dir_path}\\Data\\restdata.dat",'rb') as rest:
            restdata=pickle.load(rest)
        restdata=restdata.split(',')
        frequency=restdata[1].split(":")
        hour=frequency[0]
        mins=frequency[1]
        sec=frequency[2]
        hour1=int(hour)
        mins1=int(mins)
        sec1=int(sec)
        if hour1>0:
            hour1=hour1*3600
        if mins1>0:
            mins1=mins1*60
        if sec1>0:
            sec1=sec1
        total=hour1+mins1+sec1
        while 1:
            time.sleep(1)
            index+=1
            if index==total:
                self.main()
                os.startfile(f"{dir_path}\\start_up.pyw")
                break
    
    def start_up(filepath,startpath):
        a=os.listdir(startpath)
        b=0
        if ".lnk" in a:
            b+=1
        else:
            try:
                shutil.copy(filepath,startpath)    
            except Exception as e:
                print(e)

    def __init__(self):
        self.pass_index=0
        self.dir_path= os.path.dirname(os.path.realpath(__file__)) #to take File path`
        self.user=getpass.getuser()
        self.start=r"C:\Users\Udsadfsafsafsafsafsaortu9046ngvb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        # self.start=self.start.replace("Udsadfsafsafsafsafsaortu9046ngvb",self.user)
        # with open(f"{dir_path}\\Data\\sysdata.dat",'rb') as sys:
        #     self.sysdata=pickle.load(sys)
        # with open(f"{dir_path}\\Data\\customdata.dat",'rb') as custom:
        #     self.customdata=pickle.load(custom)
        # with open(f"{dir_path}\\Data\\restdata.dat",'rb') as rest:
        #     self.restdata=pickle.load(rest)
        # self.sysdata=self.sysdata.split(',')
        # self.customdata=self.customdata.split(',')
        # self.restdata=self.restdata.split(',')
        # self.timer=self.restdata[2]
        # self.timer=self.timer.split(":")
        # self.title=self.customdata[0]
        # self.msg=self.customdata[1]
        

    def Base(self,quit=0,sound=0):
        if sound==1:
            from playsound import playsound
            playsound(f"{dir_path}\\Audio\\1.mp3",False)
            time.sleep(2)
        self.root=Tk()
        self.root.title("Rest_Your_Eye")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.resizable(False,False)
        self.mycolor = '#d3d3d3'
        self.root.configure(background=self.mycolor)
        self.root.wm_attributes("-topmost", 1)
        self.root.attributes("-fullscreen", True)
        def disable_event():
            pass
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
        hour.set(self.timer[0])
        minute.set(self.timer[1])
        second.set(self.timer[2])
        

        if quit==1:
            Button(text="Click here to quit",command=self.root.destroy,padx=10,pady=10,bg="#f4f5f0", font="sublime 20 bold italic").place(x=525,y=450)
        else:
            self.root.protocol("WM_DELETE_WINDOW", disable_event)
        
        Label(self.root,text=self.title, font="Sublime 70 bold",bg="#d3d3d3").place(x=300,y=150)
        Label(self.root,text=self.msg,bg="#d3d3d3", font="Sublime 20 bold").place(x=415,y=250)
        hourEntry= Entry(self.root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
        hourEntry.place(x=450,y=300)
        minuteEntry= Entry(self.root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
        minuteEntry.place(x=600,y=300)
        
        secondEntry= Entry(self.root, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
        secondEntry.place(x=750,y=300)

        
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            self.root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                time.sleep(2)
                self.root.destroy()
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
        self.root.mainloop()

    def simple_noti(self):
        from plyer import notification
        notification.notify(
            title = self.title,
            message=self.msg,
            app_name="Rest_Your_Eyes",
            # displaying time
            timeout=10)

    def main(self):
        if int(self.restdata[1])==1:
            self.simple_noti()
        else:
            self.Base(quit=self.restdata[3],sound=self.restdata[4])
        os.startfile(f"{dir_path}\\start_up.pyw")

# import threading

# eye_daemon=Data()
# a=threading.Thread(target=eye_daemon.counter_label).start()
# eye_daemon.stopwatch()