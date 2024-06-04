from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD

root = Tk()
root.state('zoomed')

main_frame= Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas= Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)


my_scrollbar= ttk.Scrollbar(main_frame,orient= VERTICAL,command= my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>" , lambda e : my_canvas.configure(scrollregion=my_canvas.bbox('all')))

second_frame= Frame(my_canvas)

my_canvas.create_window((0,0),window=second_frame,anchor= "nw")

for thing in range(3):
    Label(second_frame,width=500,height=100).pack(side=BOTTOM)


title=Label(second_frame,text="Resume",font=('rome',45,BOLD)).place(x=600,y=5)
line=Label(second_frame,text="-----------------------------------------------------------------------------------------------------------------------------------------------",font=(55)).place(x=240,y=80)
name=Label(second_frame,text="Harsh",font=('newyork',40,BOLD)).place(x=200,y=250)
name=Label(second_frame,text="kumar",font=('newyork',40,BOLD)).place(x=240,y=310)
image=PhotoImage(file='pp photo.png')
im= Label(second_frame,image=image).place(x=950,y=120)
detail=Label(second_frame,text='Currently a student looking to join workforce to gain real-world experience. Ability to complete tasks on time in \n  both individual and team settings. Dependable and reliable, ready to learn and grow with your company.',font=('timessqard',20)).place(x=130,y=600)
l1=Label(second_frame,text="Personal traits",font=(BOLD,30)).place(x=130,y=750)
l2=Label(second_frame,text="● Hard worker and good team player. \n● Disciplined and positive person. \n● Willingness to learn new things\n● Good Communication skill.\n● Passionate about work.",font=('newyork',20),justify='left').place(x=130,y=830)
l3=Label(second_frame,text="Technical skills",font=(BOLD,25)).place(x=110,y=1100)
l4=Label(second_frame,text=" SQL, .net , C#, python,  Microsoft Office, ,flash, page maker",font=(20)).place(x=140,y=1150)
l5=Label(second_frame,text="Languages",font=(BOLD,25)).place(x=110,y=1200)
l44=Label(second_frame,text="English , Hindi , Gujrati",font=(20)).place(x=140,y=1250)
l55=Label(second_frame,text="Area of interests",font=(BOLD,25)).place(x=110,y=1300)
l46=Label(second_frame,text="Python",font=(20)).place(x=140,y=1350)

l6=Label(second_frame,text="Academics",font=(BOLD,25)).place(x=110,y=1450)
l06=Label(second_frame,text="Expected graduation June (2023) \n BCA(Bachelor of Computer Applications ) \n C, C#,  VB.NET,DBMS, JAVA, .Net Major Subjects.\Ganpat University Mahesana, Gujarat.",font=(23),justify='left').place(x=120,y=1520)
l06=Label(second_frame,text="March 2020\nShri Vardhman vidhyalaya \nPassed HSC with Brief studied about Accounts,Business- \n administration, Statistics and Economics from GSEB board. \nMahesana , Gujarat.",font=(23),justify='left').place(x=120,y=1670)
l08=Label(second_frame,text="March  2018\nShri Vardhman vidhyalaya \nMahesana, Gujarat. \nPassed SSC from GSEB board.",font=(23),justify='left').place(x=120,y=1870)
l56=Label(second_frame,text="Contact details",font=(BOLD,25)).place(x=110,y=2100)
l76=Label(second_frame,text="B/13 Balaji residency-2 , Mahesana,Gujarat\nPhone no. - 8200983761\nEmail - harshkumar9544@gmail.com\nwww.linkedin.com/in/harsh-kumar35536b2500\nTwitter-@Harsh4121",font=(23),justify='left').place(x=120,y=2200)
l556=Label(second_frame,text=" Simple level projects",font=(BOLD,25)).place(x=100,y=2400)
l566=Label(second_frame,text="Project Name: “Web Application for Booking house for Buying and Renting \nTeam size: Two\nFront end – Python (Tkinter)\nBackend: SQLite\nDescription: Project booking appointment for buying and renting house with details.",font=(23),justify='left').place(x=120,y=2500)
l557=Label(second_frame,text="Hobbies",font=(BOLD,25)).place(x=110,y=2700)
l5577=Label(second_frame,text="o	Travelling\no	Listening music\no	Gaming\no	Watching movies\no	Debate",font=(23),justify='left').place(x=120,y=2800)







root.mainloop()

