from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from urllib import request, parse
import json


class Units:
    def __init__(self,root):
        self.root=root
        self.root.title("Units Conversion")
        self.root.geometry("500x400")
        self.root.iconbitmap('logo806.ico')
        self.root.resizable(0,0)



        froms=StringVar()
        to=StringVar()
        value=StringVar()
        answer=StringVar()




        def on_enter1(e):
            but_convert['background']="black"
            but_convert['foreground']="cyan"
            
            

        def on_leave1(e):
            but_convert['background']="SystemButtonFace"
            but_convert['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        
        def clear():
            answer.set("")
            value.set("")
            froms.set("Select Units Convert From")
            to.set("Select Units Convert To")
            real_answer.config(text="")

        
        def convert():
            try:
                if froms.get()!="Select Units Convert From":
                    if to.get()!="Select Units Convert To":
                        if len(value.get())!=0:
                            
                            url = 'https://neutrinoapi.net/convert'
                            params = {
                                    'user-id': '',
                                    'api-key': '',
                                    'from-value': '{}'.format(value.get()),
                                    'from-type':'{}'.format(froms.get()),
                                    'to-type':'{}'.format(to.get())
                                    }

                            postdata = parse.urlencode(params).encode()
                            req = request.Request(url, data=postdata)
                            response = request.urlopen(req)
                            result = json.loads(response.read().decode("utf-8"))
                            name=json.dumps(result,indent=4)
                            real_answer=result['result-float']
                            to_type=result['to-type']
                            from_type=result['from-type']
                            answers=f"{value.get()} {from_type} = {real_answer} {to_type}"
                            answer.set(real_answer)

                            real_answer.config(text=answers)

                        else:
                            tkinter.messagebox.showerror("Error","Please Enter the value for convertion")
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Units to convert to")
                else:
                    tkinter.messagebox.showerror("Error","Please Select the Units to convert")
                
            except Exception as e:
                tkinter.messagebox.showerror("Error","Network Error / Your daily request may be ended")
                print(e)



        def res():
            ans= "8 Bit = 1 byte"
            real_answer.config(text=ans)

            
            

       
            

#=========================frame====================#
        
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3,bg="gray44")
        mainframe.place(x=0,y=0)

#===================================================#
        
        select_units_from=['Amp','Bit','Byte','Celsius','Day','Degree','Fahrenheit',\
                         'Feet','Gallon','Gram','Hour','Inch','Joule','Kelvin',\
                         'Liter','Meter','Micron','Mile','Minute','Mole','Month',\
                         'Newton','Ohm','Ounce','Pascal','Pint','Pound','Radian',\
                         'Second','Tonne','Volt','Watt','Week','Yard']
        select_units_from_combo=Combobox(mainframe,textvariable=froms,values=select_units_from,font=('arial',14),width=23,state="readonly")
        select_units_from_combo.set("Select Units Convert From")
        select_units_from_combo.place(x=110,y=10)


        select_units_to=['Amp','Bit','Byte','Celsius','Day','Degree','Fahrenheit',\
                         'Feet','Gallon','Gram','Hour','Inch','Joule','Kelvin',\
                         'Liter','Meter','Micron','Mile','Minute','Mole','Month',\
                         'Newton','Ohm','Ounce','Pascal','Pint','Pound','Radian',\
                         'Second','Tonne','Volt','Watt','Week','Yard']

        select_units_to_combo=Combobox(mainframe,textvariable=to,values=select_units_to,font=('arial',14),width=23,state="readonly")
        select_units_to_combo.set("Select Units Convert To")
        select_units_to_combo.place(x=110,y=70)

        lab_enter_value=Label(mainframe,text="Enter Value",font=('times new roman',14),bg="gray44",fg="white")
        lab_enter_value.place(x=180,y=120)

        ent_value=Entry(mainframe,textvariable=value,width=29,font=('times new roman',14),relief="ridge",bd=4)
        ent_value.place(x=110,y=160)

        lab_answer=Label(mainframe,text="Answer",font=('times new roman',14),bg="gray44",fg="white")
        lab_answer.place(x=200,y=200)

        ent_answer=Entry(mainframe,textvariable=answer,width=29,font=('times new roman',14),relief="ridge",bd=4)
        ent_answer.place(x=110,y=230)


        real_answer=Label(mainframe,text="",font=('times new roman',14),bg="gray44",fg="white")
        real_answer.place(x=160,y=280)



        but_convert=Button(mainframe,width=20,text="Convert",font=('times new roman',14),cursor="hand2",command=convert)
        but_convert.place(x=20,y=340)
        but_convert.bind("<Enter>",on_enter1)
        but_convert.bind("<Leave>",on_leave1)

        but_clear=Button(mainframe,width=20,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=263,y=340)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)
         







if __name__ == "__main__":
    root=Tk()
    Units(root)
    root.mainloop()



