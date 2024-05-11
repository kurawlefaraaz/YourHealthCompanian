from tkinter import *
from tkinter import messagebox as mb
import tkinter.ttk as tk
from PIL import ImageTk,Image
from datetime import datetime
from data import Data
import os,pickle

dir_path= os.path.dirname(os.path.realpath(__file__)) #to take File path`
remove_list=[]
class YourHealth(Tk):
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
    def save(self):
        with open(f"{dir_path}\\Data\\restdata.dat",'wb') as restdata:
            pickle.dump(f"{self.radiovar.get()},{self.hourvar.get()}:{self.minsvar.get()}:{self.secvar.get()},{self.hour_len_var.get()}:{self.mins_len_var.get()}:{self.sec_len_var.get()},{self.checkvar1.get()},{self.checkvar2.get()}",restdata)
        with open(f"{dir_path}\\Data\\customdata.dat",'wb') as customdata:
            pickle.dump(f"{self.rest_title_var.get()},{self.rest_msg_var.get()}",customdata)
        with open(f"{dir_path}\\Data\\sysdata.dat",'wb') as sysdata:
            pickle.dump(f"{self.checkvar.get()}",sysdata)
        mb.showinfo("Succesfull","Data Saved Successfully")

    def customization(self,root):
        self.rest_title_var=StringVar()
        resttitle=Label(root,text="Rest Title",font="Sublime 11 italic underline ",bg='White')
        resttitle.place(x=15,y=30)
        self.rest_title=Entry(root,width=20,font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.rest_title_var)
        self.rest_title_var.set("Have Some Rest!")
        self.rest_title.place(x=30,y=60)

        self.rest_msg_var=StringVar()
        restmsg=Label(root,text="Rest Message",font="Sublime 11 italic underline ",bg='White')
        restmsg.place(x=15,y=100)
        self.rest_msg=Entry(root,width=30,font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.rest_msg_var)
        self.rest_msg_var.set("Rest your eyes and grab some water!")
        self.rest_msg.place(x=30,y=130)
        next_btn=tk.Button(root,text="Save",command=lambda:self.Notebook_main.select(self.system_frame))
        next_btn.pack(anchor='se',side='bottom',expand=YES)

    def system(self,root):
        self.checkvar=IntVar()
        runatboot=Checkbutton(root,text="Run on boot",font="Sublime 11 italic underline ",variable=self.checkvar)
        runatboot.place(x=15,y=30)
        next_btn=tk.Button(root,text="Save",command=self.save)
        next_btn.pack(anchor='se',side='bottom',expand=YES)
    def rest(self,rest_frame):
        #Rest body
        #Notifications
        self.radiovar=IntVar()
        a=Label(rest_frame,text="Notify me using",font="Sublime 11 italic underline ",bg='White')
        a.place(x=15,y=30)
        notify1=Radiobutton(rest_frame,text="Fullscreen Notifications",font="Sublime 10 bold",variable=self.radiovar,value=1,relief=SUNKEN)
        notify1.place(x=30,y=60)
        notify1.select()
        notify2=Radiobutton(rest_frame,text="Simple Notifications     ",font="Sublime 10 bold",variable=self.radiovar,value=2,relief=SUNKEN)
        notify2.place(x=30,y=90)
        #Rest Frequency
        self.hourvar=StringVar()
        self.minsvar=StringVar()
        self.secvar=StringVar()
        b=Label(rest_frame,text="Rest Frequency",font="Sublime 11 italic underline ",bg='White')
        b.place(x=15,y=140)
        hour=Entry(rest_frame,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.hourvar)
        hour.place(x=30,y=170)
        mins=Entry(rest_frame,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.minsvar)
        mins.place(x=60,y=170)
        sec=Entry(rest_frame,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.secvar)
        sec.place(x=90,y=170)
        self.hourvar.set("00")
        self.minsvar.set("20")
        self.secvar.set("00")
        #Rest Lenth
        self.hour_len_var=StringVar()
        self.mins_len_var=StringVar()
        self.sec_len_var=StringVar()
        c=Label(rest_frame,text="Rest Lenth",font="Sublime 11 italic underline ",bg='White')
        c.place(x=15,y=210)
        hour1=Entry(rest_frame,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.hour_len_var)
        hour1.place(x=30,y=240)
        mins1=Entry(rest_frame,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.mins_len_var)
        mins1.place(x=60,y=240)
        sec1=Entry(rest_frame,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=self.sec_len_var)
        sec1.place(x=90,y=240)
        self.hour_len_var.set("00")
        self.mins_len_var.set("02")
        self.sec_len_var.set("00")
        #Check Buttons 
        self.checkvar1=IntVar()
        self.checkvar2=IntVar()
        d=Label(rest_frame,text="Options",font="Sublime 11 italic underline ",bg='White')
        d.place(x=15,y=280)
        soundcheck=Checkbutton(rest_frame,text="Playsound while starting the rest?",font="Sublime 9 bold",variable=self.checkvar1)
        soundcheck.place(x=30,y=300)
        endrestcheck=Checkbutton(rest_frame,text="Allow End Rest?                                  ",font="Sublime 9 bold",variable=self.checkvar2)
        endrestcheck.place(x=30,y=320)
        next_btn=tk.Button(rest_frame,text="Save",command=lambda:self.Notebook_main.select(self.custom_frame))
        next_btn.pack(anchor='se',side='bottom',expand=YES)
    
    # Internals of Home #For total time
    def t_time(self):
        with open(f"{dir_path}\\Data\\Data_EM.dat",'wb') as time:
                pass
        class_data=Data()
        class_data.counter_label()
        with open(f"{dir_path}\\Data\\CounterData.dat",'rb') as time:
            total_time=pickle.load(time)
        timet = datetime.fromtimestamp(total_time)
        time_t = timet.strftime("%H:%M:%S")
        self.time_t_var.set(time_t)
    
            
    # Internals of time_input()
    def check_time_format(self,text,start_time_var=None,compare=False,end_time_var=None):
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

    # Internals of time_input()
    def time_format(self,var,widget):
        a=var.get()
        text_len=len(a)-1
        if text_len+1>=9:
            var.set(a[0:8])
        if text_len==2 and ":" not in a[2] or text_len==5 and ":" not in a[5]:
            widget.insert(text_len,":")
        else:
            pass
    def take_limit(self,widget_name,entry_var):
        self.submit_data=2
        for i in self.r_list:
            i.destroy()
        username=entry_var.get()
        widget_name.destroy()
        self.submit_btn.config(text="Submit")
        self.limit_time_var=StringVar()
        self.labelframe.config(text="Screen Limit(HH:MM:SS)",font=("sublime 15 bold"),width=500)
        
        self.labelframe.update()
        limit_time_label=Label(self.labelframe,text="Screen Limit: ",font="sublime 10 bold",bg="#71d9ce",fg="#585858")
        limit_time_label.place(x=7,y=23)
        self.limit_time=Entry(self.labelframe,textvariable=self.limit_time_var,bg="#ffff76",justify="center",font="sublime 15 bold",fg="#585858")
        limit_time_trace=lambda d,b,c:self.time_format(var=self.limit_time_var,widget=self.limit_time)
        self.limit_time_var.trace('w',limit_time_trace)
        self.limit_time.place(x=170,y=25)
 
    #Internalls of create_data()
    def time_data_input(self,widget_name,entry_var):
        self.submit_btn.place(x=200,y=140)
        self.label_name.config(font="sublime 32 bold",width=20)
        username=entry_var.get()
        widget_name.destroy()
        self.start_time_var=StringVar()

        self.labelframe.config(text="Monitoring Start/End Time (HH:MM:SS)",font=("sublime 15 bold"),width=500)
        start_time_trace=lambda d,b,c:self.time_format(var=self.start_time_var,widget=start_time)
        self.start_time_var.trace('w',start_time_trace)
        self.labelframe.update()

        start_time_label=Label(self.labelframe,text="Start Time: ",font="sublime 20 bold",bg="#71d9ce",fg="#585858")
        start_time_label.place(x=7,y=23)
        start_time=Entry(self.labelframe,textvariable=self.start_time_var,bg="#ffff76",justify="center",font="sublime 20 bold",fg="#585858")
        start_time.place(x=170,y=25)
        remove_list.append(start_time)
        remove_list.append(start_time_label)

        self.end_time_var=StringVar()
        end_time_label=Label(self.labelframe,text="End Time: ",font="sublime 20 bold",bg="#71d9ce",fg="#585858")
        end_time_label.place(x=7,y=97)
        end_time_trace=lambda d,b,c:self.time_format(var=self.end_time_var,widget=end_time)
        end_time=Entry(self.labelframe,textvariable=self.end_time_var,bg="#ffff76",justify="center",font="sublime 20 bold",fg="#585858")
        self.end_time_var.trace('w',end_time_trace)
        end_time.place(x=170,y=100)
        self.r_list=[]
        self.r_list.append(end_time_label)
        self.r_list.append(end_time)
        self.r_list.append(start_time_label)
        self.r_list.append(start_time)


    #Button fuction
    def create_data_submit(self,entry_var,btn_var,widget_name,labelframe):
        username=self.username=entry_var.get()
        print("#",self.submit_data)
        if self.submit_data==False:
            self.time_data_input(widget_name=widget_name,entry_var=entry_var)
            self.submit_data=1
        elif self.submit_data==1:
            start_time=self.start_time_var.get()
            end_time=self.end_time_var.get()
            start=self.check_time_format(text=start_time,start_time_var=start_time,compare=True,end_time_var=end_time)
            end=self.check_time_format(text=end_time,start_time_var=end_time,end_time_var=start_time,compare=True)
            if start==True and end==True:
                self.submit_data==2
                self.take_limit(widget_name=widget_name,entry_var=entry_var)
        elif self.submit_data==2:
            start_time=self.start_time_var.get()
            end_time=self.end_time_var.get()
            limit=self.limit_time_var.get()
            start=self.check_time_format(text=start_time,start_time_var=start_time,compare=True,end_time_var=end_time)
            limit_check=self.check_time_format(text=limit)
            end=self.check_time_format(text=end_time,start_time_var=end_time,end_time_var=start_time,compare=True)
            if start==True and end==True and limit_check==True:
                data=[f"username={username}",f"start_time={start_time}",f"end_time={end_time}",f"Screen_limit={limit}"]
                with open(f"{dir_path}\\Data\\BasicData.dat",'wb') as dump_location:
                    pickle.dump(data,dump_location)
                mb.showinfo("Success","Data Saved Successfully")
                btn_var.set(0)
                self.main_program(self.username)
            else:
                mb.showerror("Error","Please enter time in correct format i.e in 24 hour format.") 
        else:
            pass

    def typing_effect(self,*arg,words,size,text_att,):
        root=self
        #Style call 
        style=tk.Style()
        self.label_var=StringVar()
        label_name=tk.Label(root,textvariable=self.label_var,width=29,style="Heading.TLabel",relief="flat")
        style.configure("Heading.TLabel",font=f"Sublime {size} {text_att}",relief="flat",anchor="center",background=arg[0],foreground=arg[1],padding="0 15 2 5")
        remove_list.append(label_name)
        label_name.place(x=127,y=315)
        index=0
        a=style.layout("TLabel")
        #styling 
        for i in words:
            root.after(70)
            self.label_var.set(f"{words[0:index]}{i}")
            label_name.update()
            index+=1
            if index==len(words)-1:
                author_name=Label(root,text="By Faraaz Kurawle",bg="white",fg="#6f6f6f",font="sublime 15 bold italic")
                remove_list.append(author_name)
                author_name.place(x=350,y=400)

    def __init__(self):
        super().__init__()
        # root attributes
        self.program_index=1
        height=700
        width=900
        self.geometry(f"{width}x{height}")
        self.title("  Your Health Companion")
        self.resizable(False,False)
        self.config(bg='white')
        
        
        # TOTAL TIME LABEL VAR 
        self.time_t_var=StringVar()
        
        #Images
        self.background_img=Image.open(f"{dir_path}\\Icon\\start_up_bg.png")
        self.background_img=self.background_img.resize((width-2,height-2),Image.ANTIALIAS)
        self.background_img=ImageTk.PhotoImage(self.background_img)
        background_label=Label(self,image=self.background_img)
        remove_list.append(background_label)
        background_label.image=self.background_img
        background_label.pack()

        #Start_up logo
        bg_img=Image.open(f"{dir_path}\\Icon\\start.png")
        bg_img=ImageTk.PhotoImage(bg_img)
        bg=Label(self,image=bg_img)
        remove_list.append(bg)
        bg.image=bg_img
        bg.place(relx=0.5,rely=0.5,anchor="center")

        word="Your Health Companion"
        self.typing_effect("white","#585858",words=word,size="30",text_att="bold")
        
    def create_data(self):
        self.submit_data=False
        try:
            for labels in remove_list:
                labels.destroy()
        except:
            pass
        background_label=Label(self,image=self.background_img)
        remove_list.append(background_label)
        background_label.image=self.background_img
        background_label.pack()
        words=f"Hi, This is Faraaz"
        label_var=StringVar()
        self.label_name=Label(self,textvariable=label_var,font=f"Sublime 40 bold",bg="#71d9ce",fg="#d0edea",relief="groove",anchor="w",width=18,bd=5)
        remove_list.append(self.label_name)
        self.label_name.place(relx=0.053,rely=0.25)
        index=0
        
        for i in words:
            self.after(50)
            label_var.set(f"{words[0:index]}{i}")
            self.label_name.update()
            index+=1
        self.after(1000)

        
        self.labelframe = LabelFrame(self,bd=7,text="What shall I call you?",height=200,width=600,bg="#71d9ce",font="sublime 20 bold",fg="#dedede")
        self.labelframe.place(x=50,y=250)

        name_var=StringVar()
        name=Entry(self.labelframe,textvariable=name_var,justify="left",font="Sublime 40 bold",bg="#2f2066",relief="sunken",bd=5,fg="#71d9ce")
        remove_list.append(name)
        name.pack(anchor="center")

        self.submit_var = IntVar()
        self.submit_btn=tk.Button(self.labelframe,text="Next",command=lambda:self.create_data_submit(entry_var=name_var,labelframe=self.labelframe,widget_name=name,btn_var=self.submit_var))
        self.submit_btn.pack(pady=10)
        remove_list.append(self.submit_btn)
        self.submit_btn.wait_variable(self.submit_var)

    def custom_notifier(self):
        pass
    def notifier(self):
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i==self.notifier_button:
                i["state"]=DISABLED
            else:
                i['state']=NORMAL
        # Notebook
        self.Notebook_main=tk.Notebook(self,height=600,width=640,style='main.TNotebook')
        self.Notebook_main.pack(expand=YES,fill="both")
        remove_list.append(self.Notebook_main)

        Custom_Notification_Frame=Frame(self,bg="white")
        Custom_Notification_Frame.pack(expand=YES,fill="both")

        Eye_daemon_frame=Frame(self,bg="white")
        Eye_daemon_frame.pack(expand=YES,fill="both")
        self.Notebook_main.add(text="Custom Notification",child=Custom_Notification_Frame)
        self.Notebook_main.add(text="Eye Daemon",child=Eye_daemon_frame)
        


        self.Notebook_sub=tk.Notebook(Eye_daemon_frame,style='sub.TNotebook')
        self.Notebook_sub.pack(expand=YES,fill="both")
        style=tk.Style()
        style.theme_use('default')
        style.configure('main.TNotebook', background="#384042",padding=[10,10,10,10],foreground="white")
        style.configure('main.TNotebook.Tab', background="#384042",padding=[64,10,64,10],foreground="white")
        style.map("main.TNotebook.Tab", background= [("selected", "#43727c")],foreground= [('selected',"white")])

        style.configure('sub.TNotebook', background="#384042",foreground="white")
        style.configure('sub.TNotebook.Tab', background="#384042",foreground="white")
        style.map("sub.TNotebook.Tab", background= [("selected", "#43727c")],foreground= [('selected',"white")])

        self.rest_frame=Frame(Eye_daemon_frame,bg='white')
        self.rest(self.rest_frame)
        self.rest_frame.pack(expand=YES,fill='both')
        self.custom_frame=Frame(Eye_daemon_frame,bg='white')
        self.customization(self.custom_frame)
        self.custom_frame.pack(expand=YES,fill='both')
        self.system_frame=Frame(Eye_daemon_frame,bg='white')
        self.system(self.system_frame)
        self.system_frame.pack(expand=YES,fill='both')

        self.Notebook_sub.add(child=self.rest_frame,text="Rest Settings")
        self.Notebook_sub.add(text="Customization",child=self.custom_frame)
        self.Notebook_sub.add(text="System",child=self.system_frame)
        
    

    def contact_me(self):
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i==self.contact_me_button:
                i["state"]=DISABLED
            else:
                i['state']=NORMAL

    def settings(self):
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i==self.setting_button:
                i["state"]=DISABLED
            else:
                i['state']=NORMAL
    
    def home_limit_file_write(self,e,data_name,data_var_or_data,var_exits=True):
        # Internal of HOME
        if var_exits==True:
            data=data_var_or_data.get()
        else:
            data=data_var_or_data
        check=self.check_time_format(text=data)

        if check==True:
            with open(f"{dir_path}\\Data\\BasicData.dat",'rb') as app_data:
                a=pickle.load(app_data)
            check_exits=set([(i,j) if data_name in j else 0 for i,j in enumerate(a)])
            if len(check_exits)==1:
                a.append(f"{data_name}={data}")
            else:
                check_exits=list(check_exits)
                check_exits.remove(0)
                check_exits=check_exits[0]
                a[check_exits[0]]=f"{data_name}={data}"


            with open(f"{dir_path}\\Data\\BasicData.dat",'wb') as app_data:
                a=pickle.dump(a,app_data)
            mb.showinfo("Success","Data saved\changed succesfully")
            self.home(self.name)
        else:
            pass
        

    def home(self,name_of_user):
        basic_data_exits=os.path.isfile(F"{dir_path}\\Data\\BasicData.dat")
        with open(f"{dir_path}\\Data\\BasicData.dat",'rb') as app_data:
            basic_data_list_content=pickle.load(app_data)

        #Image Loading
        import PIL
        self.notebook_bg_img=Image.open(f"{dir_path}\\Icon\\notebook_bg.png")
        self.r_notebook_bg_img=ImageTk.PhotoImage(self.notebook_bg_img)
        self.l_notebook_bg_img = self.notebook_bg_img.rotate(180, PIL.Image.NEAREST, expand = 1)
        self.l_notebook_bg_img=ImageTk.PhotoImage(self.l_notebook_bg_img)

        self.program_index+=1
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i==self.home_button:
                i["state"]=DISABLED
            else:
                i['state']=NORMAL
        #styles
        time_remaining_var=StringVar()
        styles=tk.Style()
        styles.theme_use('default')
        # Total limit //TO-DO

        #Label
        self.home_title_var=StringVar()
        home_title_lable=tk.Label(textvariable=self.home_title_var,style="head_title.TLabel")
        remove_list.append(home_title_lable)
        home_title_lable.pack()
        
        styles.configure("head_title.TLabel",foreground="#00938e",background="white",font="sublime 15 bold")
        
        #Label text
        name_of_user=name_of_user
        home_title_words=f"Welcome, {name_of_user}"
        self.home_title_var.set(home_title_words)

        styles.configure('Mynotebook.TNotebook', background="#d3d3d3",)
        styles.configure('Mynotebook.TNotebook.Tab', background="#384042",padding=[61,10,60,10],foreground="white")
        styles.map("Mynotebook.TNotebook.Tab", background= [("selected", "#43727c")],foreground= [('selected',"white")],border=[('selected','black')])


        styles.configure('Mynotebook_usage.TNotebook', background="#d3d3d3",)
        styles.configure('Mynotebook_usage.TNotebook.Tab', background="#384042",foreground="white",width=40)
        
        styles.map("Mynotebook_usage.TNotebook.Tab", background= [("selected", "#43727c")],foreground= [('selected',"white")],border=[('selected','black')])

        # Time data
        NoteBook_frame=Frame(height=200,width=565,bg="white")
        remove_list.append(NoteBook_frame)
        NoteBook_frame.place(x=50,y=300)

        nb = tk.Notebook(NoteBook_frame,height=150,width=500,style="Mynotebook.TNotebook")

        remove_list.append(nb)
        
        pc_total_time= Frame(nb, width= 400, height=180,bg="#76cece")
        app_total_time = Frame(nb, width= 400, height=180,bg='#76cece')

        #Pc Total Time
        self.t_time()
        
        self.Total_time_label=Label(pc_total_time,textvariable=self.time_t_var,font="sublime 80 bold",fg="white",bg="#76cece")
        remove_list.append(self.Total_time_label)
        self.Total_time_label.place(relx=0.5,rely=0.5,anchor="center")
        
        nb.add(pc_total_time, text= 'Total PC Usage Today: ')
        nb.add(app_total_time, text= 'App Total Usage Today: ')
        
        
        r_border=Label(NoteBook_frame,image=self.r_notebook_bg_img,bg="white")
        remove_list.append(r_border)
        r_border.config(image=self.r_notebook_bg_img)
        
        l_border=Label(NoteBook_frame,image=self.l_notebook_bg_img,bg="white")
        l_border.config(image=self.l_notebook_bg_img)
        remove_list.append(l_border)


        nb.place(x=33,y=00)
        r_border.place(x=530,y=0)
        l_border.place(x=0,y=1)

        ########################################################################
        Usage_NoteBook_frame=Frame(height=200,width=565,bg="white")
        remove_list.append(Usage_NoteBook_frame)
        Usage_NoteBook_frame.place(x=50,y=100)

        # SHow data notebook
        time_setting_nb = tk.Notebook(Usage_NoteBook_frame,height=165,width=500,style="Mynotebook_usage.TNotebook")
        remove_list.append(time_setting_nb)
        
        Time_show_data_frame= Frame(time_setting_nb, width= 400, height=180,bg="#76cece")
        Time_take_data_frame = Frame(time_setting_nb, width= 400, height=180,bg='#76cece')

        # Take data frame
        self.start_time_var=StringVar()
        start_time_label=Label(Time_take_data_frame,text="Start Time: ",font="sublime 20 bold",bg="#76cece",fg="#585858")
        start_time_label.place(x=7,y=60)
        self.start_time_entry=Entry(Time_take_data_frame,textvariable=self.start_time_var,bg="#ffff76",justify="center",font="sublime 20 bold",fg="#585858")
        start_time_trace=lambda d,b,c:self.time_format(var=self.start_time_var,widget=self.start_time_entry)
        self.start_time_var.trace('w',start_time_trace)
        self.start_time_entry.place(x=170,y=65)

        self.end_time_var=StringVar()
        end_time_label=Label(Time_take_data_frame,text="End Time: ",font="sublime 20 bold",bg="#76cece",fg="#585858")
        end_time_label.place(x=7,y=120)
        
        self.end_time_entry=Entry(Time_take_data_frame,textvariable=self.end_time_var,bg="#ffff76",justify="center",font="sublime 20 bold",fg="#585858")
        end_time_trace=lambda d,b,c:self.time_format(var=self.end_time_var,widget=self.end_time_entry)
        self.end_time_var.trace('w',end_time_trace)
        self.end_time_entry.place(x=170,y=125)

        self.time_limit_var=StringVar()
        total_limit_trace=lambda d,b,c:self.time_format(var=self.time_limit_var,widget=time_limit_entry)
        self.time_limit_var.trace('w',total_limit_trace)
        time_limit_label=Label(Time_take_data_frame,text="Screen Limit: ",font="sublime 10 bold",fg="#585858",bg="#76cece")
        time_limit_label.place(x=60,rely=0.2,anchor="center")
        Note_label=Label(Time_take_data_frame,text="Note: Press Enter\Return to apply changes.",font="sublime 8 bold",fg="#585858",bg="#76cece")
        Note_label.place(x=380,rely=0.2,anchor="center")
        time_limit_entry=Entry(Time_take_data_frame,textvariable=self.time_limit_var,font="sublime 10 bold",bg="#ffff76",justify="center",fg="#585858")
        time_limit_entry.place(x=180,rely=0.2,anchor="center")

        with open(f"{dir_path}\\Data\\Data_EM.dat",'wb') as time:
            pass
        basic_data_list_content_limit_check=tuple(set([1 if "Screen_limit=" in i else 0 for i in basic_data_list_content]))
        basic_data_list_content_end_start_check=tuple(set([1 if "end_time=" and "start_time=" in i else 0 for i in basic_data_list_content]))
        self.start_time_entry.bind("<Return>",lambda e:self.home_limit_file_write(data_name="start_time=",data_var_or_data=self.start_time_var,e=e))
        self.end_time_entry.bind("<Return>",lambda e:self.home_limit_file_write(data_name="start_time=",data_var_or_data=self.end_time_var,e=e))
        time_limit_entry.bind("<Return>",lambda e: self.home_limit_file_write(data_name="Screen_limit",data_var_or_data=self.time_limit_var,e=e))

        if 1 in basic_data_list_content_limit_check and 1 in basic_data_list_content_end_start_check:
            from datetime import timedelta
            self.start_time_var.set(basic_data_list_content[1].replace("start_time=",""))
            self.end_time_var.set(basic_data_list_content[2].replace("end_time=",""))
            limit=basic_data_list_content[3].replace("Screen_limit=","")
            limit=limit.replace("limit=","")
            self.time_limit_var.set(limit)
            time_remaining_var=StringVar()
            limit_1=limit.split(":")
            t_time_1=self.time_t_var.get()
            t_time_1=t_time_1.split(":")
            t1 = timedelta(hours=int(limit_1[0]), minutes=int(limit_1[1]),seconds=int(limit_1[2]))
            t2 = timedelta(hours=int(t_time_1[0]), minutes=int(t_time_1[1]),seconds=int(t_time_1[2]))
            if t1<t2:
                time_remain="Times up!"
            else:
                time_remain=t1-t2
            time_remaining_var.set(f"Time Remaining: {time_remain}")
            self.update()
            
        else:
            time_limit_entry.focus()
            self.time_limit_var.set("HH:MM:SS, Press Enter to pass data.")
            

        # Show data frame
        time_limit_label=Label(Time_show_data_frame,textvariable=time_remaining_var,font="sublime 10 bold",bg="#ffff76",fg="#585858",width=22)
        time_limit_label.place(x=20,y=20)
        time_exceded=f"Time Exceded: {t2-t1}"
        time_exceded_label=Label(Time_show_data_frame,text=time_exceded,font="sublime 10 bold",bg="#ffff76",fg="#585858",width=22,justify=LEFT)
        time_exceded_label.place(x=20,y=60)
        
        start_time_label_show_data=f"Start Time: {self.start_time_var.get()}"
        end_time_label_show_data=f"End Time: {self.start_time_var.get()}"
        show_start_time_label=Label(Time_show_data_frame,text=start_time_label_show_data,font="sublime 10 bold",bg="#ffff76",fg="#585858",width=22,justify=LEFT)
        show_start_time_label.place(x=290,y=20)
        
        show_end_time_label=Label(Time_show_data_frame,text=end_time_label_show_data,font="sublime 10 bold",bg="#ffff76",fg="#585858",width=22,justify=LEFT)
        show_end_time_label.place(x=290,y=60)

        # Adding the frames
        time_setting_nb.add(Time_show_data_frame, text= 'Usage')
        time_setting_nb.add(Time_take_data_frame, text= 'Edit Basic Setting')
        
        r_border_usage=Label(Usage_NoteBook_frame,image=self.r_notebook_bg_img,bg="white")
        remove_list.append(r_border_usage)
        r_border_usage.config(image=self.r_notebook_bg_img)
        
        l_border_usage=Label(Usage_NoteBook_frame,image=self.l_notebook_bg_img,bg="white")
        l_border_usage.config(image=self.l_notebook_bg_img)
        remove_list.append(l_border_usage)

        time_setting_nb.place(x=33,y=00)
        r_border_usage.place(x=530,y=0)
        l_border_usage.place(x=0,y=1)
        
    def sleep_lock(self):
        for i in self.button_list:
            if i==self.sleep_lock_button:
                i["state"]=DISABLED
            else:
                i['state']=NORMAL
        for labels in remove_list:
            labels.destroy()
        
    def main_program(self,name_of_user):
        for label1 in remove_list:
            label1.destroy()
        self.name=name_of_user
        #Buttons Frame
        button_frame=Frame(bg="#7accf9",width=35,relief=SUNKEN)
        button_frame.pack(fill=Y,side=LEFT)

        home_icon_img=Image.open(f"{dir_path}\\Icon\\home-button.png")
        home_icon_img=home_icon_img.resize((30,30))
        home_icon_img=ImageTk.PhotoImage(home_icon_img)
        self.home_button=Button(button_frame,image=home_icon_img,bg="#7accf9",borderwidth=0,activebackground="#7accf9",command=lambda:self.home(name_of_user))
        self.home_button.image=home_icon_img
        self.home_button.place(x=1,y=60)

        sleep_lock_img=Image.open(f"{dir_path}\\Icon\\sleep_lock.png")
        sleep_lock_img=sleep_lock_img.resize((27,27))
        sleep_lock_img=ImageTk.PhotoImage(sleep_lock_img)
        self.sleep_lock_button=Button(button_frame,image=sleep_lock_img,bg="#7accf9",borderwidth=0,activebackground="#7accf9",command=self.sleep_lock)
        self.sleep_lock_button.image=sleep_lock_img
        self.sleep_lock_button.place(x=3,y=140)

        notifier_icon_img=Image.open(f"{dir_path}\\Icon\\notifier.png")
        notifier_icon_img=notifier_icon_img.resize((27,27))
        notifier_icon_img=ImageTk.PhotoImage(notifier_icon_img)
        self.notifier_button=Button(button_frame,image=notifier_icon_img,bg="#7accf9",borderwidth=0,activebackground="#7accf9",command=self.notifier)
        self.notifier_button.image=notifier_icon_img
        self.notifier_button.place(x=3,y=220)

        contact_me_icon_img=Image.open(f"{dir_path}\\Icon\\contact_me.png")
        contact_me_icon_img=contact_me_icon_img.resize((27,27))
        contact_me_icon_img=ImageTk.PhotoImage(contact_me_icon_img)
        self.contact_me_button=Button(button_frame,image=contact_me_icon_img,bg="#7accf9",borderwidth=0,activebackground="#7accf9",command=self.contact_me)
        self.contact_me_button.image=contact_me_icon_img
        self.contact_me_button.place(x=3,y=300)

        setting_icon_img=Image.open(f"{dir_path}\\Icon\\Setting_icon.png")
        setting_icon_img=setting_icon_img.resize((30,30))
        setting_icon_img=ImageTk.PhotoImage(setting_icon_img)
        self.setting_button=Button(button_frame,image=setting_icon_img,bg="#7accf9",borderwidth=0,activebackground="#7accf9",command=self.settings)
        self.setting_button.image=setting_icon_img
        self.setting_button.place(x=1,y=660)
        self.button_list=[self.home_button,self.sleep_lock_button,self.notifier_button,self.contact_me_button,self.setting_button]

        fixed_height = 700
        self.main_bg_img=setting_icon_img=Image.open(f"{dir_path}\\Icon\\MainBg.png")
        height_percent = (fixed_height / float(self.main_bg_img.size[1]))
        width_size = int((float(self.main_bg_img.size[0]) * float(height_percent)))
        import PIL
        self.main_bg_img = self.main_bg_img.resize((width_size, fixed_height), PIL.Image.NEAREST)
        # self.main_bg_img=self.main_bg_img.resize((750,650))
        self.main_bg_img=ImageTk.PhotoImage(self.main_bg_img)
        self.main_bg_label=tk.Label(master=self,image=self.main_bg_img,style="head_title.TLabel")
        self.main_bg_label.image=self.main_bg_img
        self.main_bg_label.place(x=85,y=0)
        
        if self.program_index==1:
            self.home(name_of_user)
a=YourHealth()
Basic_File_exits=os.path.isfile(F"{dir_path}\\Data\\BasicData.dat")
try:
    if Basic_File_exits==False: 
        a.create_data()
    else:
        with open(f"{dir_path}\\Data\\BasicData.dat",'rb') as names1:
            file_data=pickle.load(names1)
        name=str(file_data[0])
        start_time_main=str(file_data[1])
        end_time_main=str(file_data[2])
        name=name.replace("username=","")
        start_time_main=start_time_main.replace("start_time=","")
        end_time_main=end_time_main.replace("end_time=","")
        a.main_program(name)
    a.mainloop()
except Exception as e:
    print(e)
finally:
    os.remove(F"{dir_path}\\Data\\Data_EM.dat")
