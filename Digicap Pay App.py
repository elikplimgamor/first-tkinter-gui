#!/usr/bin/env python
# coding: utf-8

# In[20]:


from tkinter import * #importing tkinter
root=Tk()
root.geometry("500x500")#size of the window 
root.title("Digicap Pay App")#Title of the app
Label(root,text="Digicap Dollar Rate Calculator", font = 'arial 30').pack(pady=50) #page header with a defined font styling 
root.resizable(False,False) #making the window rigid to change in size and shape 

#entries for name
l1=Label(root,text="Enter Name",width=10,font=("arial",12))
l1.place(x=20,y=120)
e1=Entry(root)
e1.place(x=200,y=120)

#entries for email
l3=Label(root,text="Finish Date",width=10,font=("arial",12))
l3.place(x=19,y=160)
e3=Entry(root)
e3.place(x=200,y=160)


#entries for contact
l4=Label(root,text="number of hours",width=13,font=("arial",12))
l4.place(x=21,y=200)
e4=Entry(root)
e4.place(x=200,y=200)

# #setting the labels
# Label(text='Project Name',font=23).place(x=180,y=240)
# Label(text='Start Date',font=23).place(x=240,y=240)
# Label(text='Finish Date',font=23).place(x=100,y=250)
# Label(text='How many Hours Did You Work ',font=23).place(x=310,y=240)



#select state
list_of_Country=("United States","Germany ","Togo","Ghana")
c=StringVar()
droplist=OptionMenu(root,c,*list_of_Country)
droplist.config(width=15) #generate a list on nations
c.set("United States")
l2=Label(root,text="Select Country",width=13,font=("arial",12))
l2.place(x=14,y=280) #display the drop down 👇 list
droplist.place(x=200,y=275) 

#fuunction for the conversion
def calc_sum(event):
    l4 = int(num1Entry.get())
    salary = l4 * 7
    
#calculate button
Button(root,text="Calculate",width=10).place(x=200,y=400)


# print the final amount


# print('you will receive '+str(salary)) 

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




