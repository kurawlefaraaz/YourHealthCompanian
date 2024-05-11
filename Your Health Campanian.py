from main import YourHealth as YH
from data import Data
import os,pickle,subprocess


dir_path= os.path.dirname(os.path.realpath(__file__)) #to take File path`
print(dir_path)
data=Data()
a=YH()
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
    os.startfile(f"{dir_path}\\start_up.pyw")
    os.remove(f"{dir_path}\\Data\\Data_EM.dat")
    
except Exception as e:
    print(e)
finally:
    pass