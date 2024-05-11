import os
import sqlite3
import tkinter.messagebox as mb
from tkinter import *
import tkinter.ttk as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from datetime import datetime
from data import Data, CommonFunction

dir_path = os.path.dirname(os.path.realpath(__file__))  # to take File path`
db_path = f"{dir_path}\\Data\\AppData.db"
remove_list = []


class Pomodora(CommonFunction):
    def pomodoro(self, frame):
        Notify_label = Label(frame, text="Notify: ",
                             font="Sublime 15 bold", fg="#585858", bg='white')
        Notify_label.pack(side=LEFT, anchor='nw', padx=10, pady=20)


class Start_up(Tk):
    def typing_effect(self, *arg, words, size, text_att,):
        root = self
        # Style call
        style = ttk.Style()
        self.label_var = StringVar()
        label_name = ttk.Label(root, textvariable=self.label_var,
                               width=29, style="Heading.TLabel", relief="flat")
        style.configure("Heading.TLabel", font=f"Sublime {size} {text_att}", relief="flat",
                        anchor="center", background=arg[0], foreground=arg[1], padding="0 15 2 5")
        remove_list.append(label_name)
        label_name.place(x=127, y=315)
        index = 0
        a = style.layout("TLabel")
        # styling
        for i in words:
            root.after(70)
            self.label_var.set(f"{words[0:index]}{i}")
            label_name.update()
            index += 1
            if index == len(words)-1:
                author_name = Label(root, text="By Faraaz Kurawle",
                                    bg="white", fg="#6f6f6f", font="sublime 15 bold italic")
                remove_list.append(author_name)
                author_name.place(x=350, y=400)

    def __init__(self):
        super().__init__()
        # root attributes
        self.program_index = 1
        height = 700
        width = 900
        self.geometry(f"{width}x{height}")
        self.title("  Your Health Companion")
        self.resizable(False, False)
        self.config(bg='white')

        # TOTAL TIME LABEL VAR
        self.time_t_var = StringVar()

        # Images
        self.background_img = Image.open(f"{dir_path}\\Icon\\start_up_bg.png")
        self.background_img = self.background_img.resize(
            (width-2, height-2), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(self.background_img)
        background_label = Label(self, image=self.background_img)
        remove_list.append(background_label)
        background_label.image = self.background_img
        background_label.pack()

        # Start_up logo
        bg_img = Image.open(f"{dir_path}\\Icon\\start.png")
        bg_img = ImageTk.PhotoImage(bg_img)
        bg = Label(self, image=bg_img)
        remove_list.append(bg)
        bg.image = bg_img
        bg.place(relx=0.5, rely=0.5, anchor="center")

        word = "Your Health Companion"
        self.typing_effect("white", "#585858", words=word,
                           size="30", text_att="bold")


class NewUser(CommonFunction):
    def take_limit(self, widget_name):
        self.submit_data = 2
        for i in self.r_list:
            i.destroy()
        widget_name.destroy()
        self.submit_btn.config(text="Submit")
        self.limit_time_var = StringVar()
        self.labelframe.config(text="Screen Limit(HH:MM:SS)",
                               font=("sublime 15 bold"), width=500)

        self.labelframe.update()
        limit_time_label = Label(self.labelframe, text="Screen Limit: ",
                                 font="sublime 10 bold", bg="#71d9ce", fg="#585858")
        limit_time_label.place(x=7, y=23)
        self.limit_time = Entry(self.labelframe, textvariable=self.limit_time_var,
                                bg="#ffff76", justify="center", font="sublime 15 bold", fg="#585858")
        def limit_time_trace(d, b, c): return self.time_format(
            var=self.limit_time_var, widget=self.limit_time)
        self.limit_time_var.trace('w', limit_time_trace)
        self.limit_time.place(x=170, y=25)

    def time_data_input(self, widget_name):
        self.submit_btn.place(x=200, y=140)
        self.label_name.config(font="sublime 32 bold", width=20)

        widget_name.destroy()
        self.start_time_var = StringVar()

        self.labelframe.config(
            text="Monitoring Start/End Time (HH:MM:SS)", font=("sublime 15 bold"), width=500)

        def start_time_trace(d, b, c): return self.time_format(
            var=self.start_time_var, widget=start_time)
        self.start_time_var.trace('w', start_time_trace)
        self.labelframe.update()

        start_time_label = Label(self.labelframe, text="Start Time: ",
                                 font="sublime 20 bold", bg="#71d9ce", fg="#585858")
        start_time_label.place(x=7, y=23)
        start_time = Entry(self.labelframe, textvariable=self.start_time_var,
                           bg="#ffff76", justify="center", font="sublime 20 bold", fg="#585858")
        start_time.place(x=170, y=25)
        remove_list.append(start_time)
        remove_list.append(start_time_label)

        self.end_time_var = StringVar()
        end_time_label = Label(self.labelframe, text="End Time: ",
                               font="sublime 20 bold", bg="#71d9ce", fg="#585858")
        end_time_label.place(x=7, y=97)
        def end_time_trace(d, b, c): return self.time_format(
            var=self.end_time_var, widget=end_time)
        end_time = Entry(self.labelframe, textvariable=self.end_time_var,
                         bg="#ffff76", justify="center", font="sublime 20 bold", fg="#585858")
        self.end_time_var.trace('w', end_time_trace)
        end_time.place(x=170, y=100)
        self.r_list = []
        self.r_list.append(end_time_label)
        self.r_list.append(end_time)
        self.r_list.append(start_time_label)
        self.r_list.append(start_time)

    def create_data_submit(self, entry_var, btn_var, widget_name):
        username = self.username = entry_var.get()
        if self.submit_data == False:
            self.time_data_input(widget_name=widget_name)
            self.submit_data = 1
        elif self.submit_data == 1:
            start_time = self.start_time_var.get()
            end_time = self.end_time_var.get()
            start = self.check_time_format(
                text=start_time, start_time_var=start_time, compare=True, end_time_var=end_time)
            end = self.check_time_format(
                text=end_time, start_time_var=end_time, end_time_var=start_time, compare=True)
            if start == True and end == True:
                self.submit_data == 2
                self.take_limit(widget_name=widget_name)
        elif self.submit_data == 2:
            start_time = self.start_time_var.get()
            end_time = self.end_time_var.get()
            limit = self.limit_time_var.get()
            start = self.check_time_format(
                text=start_time, start_time_var=start_time, compare=True, end_time_var=end_time)
            limit_check = self.check_time_format(text=limit)
            end = self.check_time_format(
                text=end_time, start_time_var=end_time, end_time_var=start_time, compare=False)
            if start == True and end == True and limit_check == True:
                data1 = [("start_time", start_time),
                         ("end_time", end_time), ("screen_limit", limit)]
                self.sqlite_cmd(path=db_path, e_type='one', command=f"""INSERT INTO username VALUES(?)""", data=(
                    username,), commit=True)
                self.sqlite_cmd(path=db_path, data=data1, e_type='2',
                                command=f"""INSERT INTO time_data VALUES(?,?)""", show_s_succes=True, commit=True)
                btn_var.set(0)
            else:
                mb.showerror(
                    "Error", "Please enter time in correct format i.e in 24 hour format.")
        else:
            pass

    def __init__(self, background_img, window):
        # Creating Data
        self.window = window
        self.submit_data = False
        try:
            for labels in remove_list:
                labels.destroy()
        except:
            pass
        background_label = Label(window, image=background_img)
        remove_list.append(background_label)
        background_label.image = background_img
        background_label.pack()
        words = f"Hi, This is Faraaz"
        label_var = StringVar()
        self.label_name = Label(window, textvariable=label_var, font=f"Sublime 40 bold",
                                bg="#71d9ce", fg="#d0edea", relief="groove", anchor="w", width=18, bd=5)
        remove_list.append(self.label_name)
        self.label_name.place(relx=0.053, rely=0.25)
        index = 0

        for i in words:
            window.after(50)
            label_var.set(f"{words[0:index]}{i}")
            self.label_name.update()
            index += 1
        window.after(1000)

        self.labelframe = LabelFrame(window, bd=7, text="What shall I call you?",
                                     height=200, width=600, bg="#71d9ce", font="sublime 20 bold", fg="#dedede")
        self.labelframe.place(x=50, y=250)

        name_var = StringVar()
        name = Entry(self.labelframe, textvariable=name_var, justify="left",
                     font="Sublime 40 bold", bg="#2f2066", relief="sunken", bd=5, fg="#71d9ce")
        remove_list.append(name)
        name.pack(anchor="center")

        self.submit_var = IntVar()
        self.submit_btn = ttk.Button(self.labelframe, text="Next", command=lambda: self.create_data_submit(
            entry_var=name_var, widget_name=name, btn_var=self.submit_var))
        self.submit_btn.pack(pady=10)
        remove_list.append(self.submit_btn)
        self.submit_btn.wait_variable(self.submit_var)


class Main(CommonFunction):
    def custom_notifier(self):
        pass

    def notifier(self, WINDOW):
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i == self.notifier_button:
                i["state"] = DISABLED
            else:
                i['state'] = NORMAL
        # Notebook
        self.Notebook_main = ttk.Notebook(
            WINDOW, height=600, width=640, style='main.TNotebook')
        self.Notebook_main.pack(expand=YES, fill="both")
        remove_list.append(self.Notebook_main)

        Alarm_Frame = Frame(WINDOW, bg="white")
        Alarm_Frame.pack(expand=YES, fill="both")

        Pomodoro_Frame = Frame(WINDOW, bg="white")
        self.pomodoro(Pomodoro_Frame)
        Pomodoro_Frame.pack(expand=YES, fill="both")
        self.Notebook_main.add(
            text="Custom Notification", child=Pomodoro_Frame)
        self.Notebook_main.add(text="Eye Daemon", child=Alarm_Frame)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('main.TNotebook', background="#384042",
                        padding=[10, 10, 10, 10], foreground="white")
        style.configure('main.TNotebook.Tab', background="#384042", padding=[
                        64, 10, 64, 10], foreground="white")
        style.map("main.TNotebook.Tab", background=[
                  ("selected", "#43727c")], foreground=[('selected', "white")])

    def contact_me(self):
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i == self.contact_me_button:
                i["state"] = DISABLED
            else:
                i['state'] = NORMAL

    def settings(self):
        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i == self.setting_button:
                i["state"] = DISABLED
            else:
                i['state'] = NORMAL
    '@Start@'

    def home(self, name_of_user):
        time_remaining_var = StringVar()
        basic_data_list_content = self.sqlite_cmd(
            path=db_path, data=None, e_type='one', command="""SELECT * FROM time_data""", capture_output=True)

        # Image Loading
        import PIL
        self.notebook_bg_img = Image.open(f"{dir_path}\\Icon\\notebook_bg.png")
        self.r_notebook_bg_img = ImageTk.PhotoImage(self.notebook_bg_img)
        self.l_notebook_bg_img = self.notebook_bg_img.rotate(
            180, PIL.Image.NEAREST, expand=1)
        self.l_notebook_bg_img = ImageTk.PhotoImage(self.l_notebook_bg_img)

        for labels in remove_list:
            labels.destroy()
        for i in self.button_list:
            if i == self.home_button:
                i["state"] = DISABLED
            else:
                i['state'] = NORMAL

        # styles
        styles = ttk.Style()
        styles.theme_use('default')

        
        # Total limit //TO-DO

        #### Greeting
        self.home_title_var = StringVar()
        home_title_lable = ttk.Label(
            textvariable=self.home_title_var, style="head_title.TLabel")
        remove_list.append(home_title_lable)
        home_title_lable.pack()

        styles.configure("head_title.TLabel", foreground="#00938e",
                         background="white", font="sublime 15 bold")

        # Greeting label 
        name_of_user = name_of_user
        home_title_words = f"Welcome, {name_of_user}"
        self.home_title_var.set(home_title_words)

        #### DateTime
        current_date_time=datetime.now()
        print(current_date_time)
        #### NoteBook Styles
        styles.configure('Mynotebook.TNotebook', background="#d3d3d3",)
        styles.configure('Mynotebook.TNotebook.Tab', background="#384042", padding=[
                         61, 10, 60, 10], foreground="white")
        styles.map("Mynotebook.TNotebook.Tab", background=[("selected", "#43727c")], foreground=[
                   ('selected', "white")], border=[('selected', 'black')])

        styles.configure('Mynotebook_usage.TNotebook', background="#d3d3d3",)
        styles.configure('Mynotebook_usage.TNotebook.Tab',
                         background="#384042", foreground="white", width=40)

        styles.map("Mynotebook_usage.TNotebook.Tab", background=[("selected", "#43727c")], foreground=[
                   ('selected', "white")], border=[('selected', 'black')])

        # Time data
        NoteBook_frame = Frame(height=200, width=565, bg="white")
        remove_list.append(NoteBook_frame)
        NoteBook_frame.place(x=50, y=300)

        nb = ttk.Notebook(NoteBook_frame, height=150,
                          width=500, style="Mynotebook.TNotebook")

        remove_list.append(nb)

        pc_total_time = Frame(nb, width=400, height=180, bg="#76cece")
        app_total_time = Frame(nb, width=400, height=180, bg='#76cece')

        # Pc Total Time
        # self.t_time()
        self.time_t_var = StringVar()
        self.Total_time_label = Label(
            pc_total_time, textvariable=self.time_t_var, font="sublime 80 bold", fg="white", bg="#76cece")
        remove_list.append(self.Total_time_label)
        self.Total_time_label.place(relx=0.5, rely=0.5, anchor="center")

        nb.add(pc_total_time, text='Total PC Usage Today: ')
        nb.add(app_total_time, text='App Total Usage Today: ')

        r_border = Label(
            NoteBook_frame, image=self.r_notebook_bg_img, bg="white")
        remove_list.append(r_border)
        r_border.config(image=self.r_notebook_bg_img)

        l_border = Label(
            NoteBook_frame, image=self.l_notebook_bg_img, bg="white")
        l_border.config(image=self.l_notebook_bg_img)
        remove_list.append(l_border)

        nb.place(x=33, y=00)
        r_border.place(x=530, y=0)
        l_border.place(x=0, y=1)
        
    def sleep_lock(self):
        for i in self.button_list:
            if i == self.sleep_lock_button:
                i["state"] = DISABLED
            else:
                i['state'] = NORMAL
        for labels in remove_list:
            labels.destroy()

    def __init__(self, WINDOW, name_of_user):
        for label1 in remove_list:
            label1.destroy()
        self.name = name_of_user
        # Buttons Frame
        button_frame = Frame(WINDOW, bg="#7accf9", width=35, relief=SUNKEN)
        button_frame.pack(fill=Y, side=LEFT)

        home_icon_img = Image.open(f"{dir_path}\\Icon\\home-button.png")
        home_icon_img = home_icon_img.resize((30, 30))
        home_icon_img = ImageTk.PhotoImage(home_icon_img)
        self.home_button = Button(button_frame, image=home_icon_img, bg="#7accf9", borderwidth=0,
                                  activebackground="#7accf9", command=lambda: self.home(name_of_user))
        self.home_button.image = home_icon_img
        self.home_button.place(x=1, y=60)

        sleep_lock_img = Image.open(f"{dir_path}\\Icon\\sleep_lock.png")
        sleep_lock_img = sleep_lock_img.resize((27, 27))
        sleep_lock_img = ImageTk.PhotoImage(sleep_lock_img)
        self.sleep_lock_button = Button(button_frame, image=sleep_lock_img, bg="#7accf9",
                                        borderwidth=0, activebackground="#7accf9", command=self.sleep_lock)
        self.sleep_lock_button.image = sleep_lock_img
        self.sleep_lock_button.place(x=3, y=140)

        notifier_icon_img = Image.open(f"{dir_path}\\Icon\\notifier.png")
        notifier_icon_img = notifier_icon_img.resize((27, 27))
        notifier_icon_img = ImageTk.PhotoImage(notifier_icon_img)
        self.notifier_button = Button(button_frame, image=notifier_icon_img, bg="#7accf9",
                                      borderwidth=0, activebackground="#7accf9", command=lambda: self.notifier(WINDOW))
        self.notifier_button.image = notifier_icon_img
        self.notifier_button.place(x=3, y=220)

        contact_me_icon_img = Image.open(f"{dir_path}\\Icon\\contact_me.png")
        contact_me_icon_img = contact_me_icon_img.resize((27, 27))
        contact_me_icon_img = ImageTk.PhotoImage(contact_me_icon_img)
        self.contact_me_button = Button(button_frame, image=contact_me_icon_img, bg="#7accf9",
                                        borderwidth=0, activebackground="#7accf9", command=self.contact_me)
        self.contact_me_button.image = contact_me_icon_img
        self.contact_me_button.place(x=3, y=300)

        setting_icon_img = Image.open(f"{dir_path}\\Icon\\Setting_icon.png")
        setting_icon_img = setting_icon_img.resize((30, 30))
        setting_icon_img = ImageTk.PhotoImage(setting_icon_img)
        self.setting_button = Button(button_frame, image=setting_icon_img, bg="#7accf9",
                                     borderwidth=0, activebackground="#7accf9", command=self.settings)
        self.setting_button.image = setting_icon_img
        self.setting_button.place(x=1, y=660)
        self.button_list = [self.home_button, self.sleep_lock_button,
                            self.notifier_button, self.contact_me_button, self.setting_button]

        fixed_height = 700
        self.main_bg_img = setting_icon_img = Image.open(
            f"{dir_path}\\Icon\\MainBg.png")
        height_percent = (fixed_height / float(self.main_bg_img.size[1]))
        width_size = int(
            (float(self.main_bg_img.size[0]) * float(height_percent)))
        import PIL
        self.main_bg_img = self.main_bg_img.resize(
            (width_size, fixed_height), PIL.Image.NEAREST)
        # self.main_bg_img=self.main_bg_img.resize((750,650))
        self.main_bg_img = ImageTk.PhotoImage(self.main_bg_img)
        self.main_bg_label = ttk.Label(
            master=WINDOW, image=self.main_bg_img, style="head_title.TLabel")
        self.main_bg_label.image = self.main_bg_img
        self.main_bg_label.place(x=85, y=0)

        self.home(self.name)


def main():
    start_up = Start_up()
    common_func = CommonFunction()
    db_file_check = os.path.isfile(f"{dir_path}\\Data\\AppData.db")
    if db_file_check == False:
        common_func.sqlite_cmd(path=db_path, data=None, e_type='one', command="""CREATE TABLE IF NOT EXISTS time_data(
            name TEXT,
            time TEXT)""", commit=True)
        common_func.sqlite_cmd(path=db_path, data=None, e_type='one', command="""CREATE TABLE IF NOT EXISTS username(
                name TEXT)""", commit=True)
        common_func.sqlite_cmd(path=db_path, data=None, e_type='one', command="""CREATE TABLE IF NOT EXISTS CounterData(
                name TEXT,
                value INTEGER)""", commit=True)
        new_user = NewUser(
            window=start_up, background_img=start_up.background_img)
        username = common_func.sqlite_cmd(
            path=db_path, data=None, e_type='one', command="""SELECT name FROM username""")
        Main.__init__(self=start_up, name_of_user=username)

    else:
        username = common_func.sqlite_cmd(
            path=db_path, data=None, e_type='one', command="""SELECT name FROM username""")
        main_program = Main(WINDOW=start_up, name_of_user=username)

    start_up.mainloop()


main()
