#i went build the task timer which i can enter the name of the task
#and how much time it takes than enter start to begining
#the gui should has the digetal clock 


from tkinter import *
import time



app = Tk()

app.minsize(450,250)


def set_time_varibal(period):
	period = period.replace(',','')
	hour = int(period[0])
	mint = int(period[1:3])
	sec = int(period[-2:])
	return hour,mint,sec

def set_period_value():
	global period,task_name_value
	period =  task_time_value.get()
	task_name_value = task_name_value.get()
	clock_dis()

def clock_dis(): #this function responsive about the clock and the timer.
	global period
	label_time = Label(app,font=('times', 15 ,'bold'),text='The time now')
	label_time.grid(row=6,column=1,columnspan=2)
	clock = Label(app,font=('times', 20 ,'bold'))
	clock.grid(row=7,column=1,padx=20,pady=10,columnspan=2)
	label_timer = Label(app,font=('times', 15 ,'bold'),text='Timer')
	label_timer.grid(row=8,column=2)
	timer = Label(app,font=('times', 20 ,'bold'))
	timer.grid(row=9,column=2)

	label_task_name = Label(app,text=task_name_value,font=('times', 15 ,'bold'),bg='red')
	label_task_name.grid(row=8,column=1,rowspan=2)

	
	hour,mint,sec = set_time_varibal(period)
	if sec > 0:
		if sec <= 10:
			sec -= 1
			sec = '0' + str(sec) 
			if mint < 10:
				mint = '0' + str(mint)
			timer.config(text = '%s:%s:%s'%(hour,mint,sec))
		else:
			sec -= 1
			if mint < 10:
				mint = '0' + str(mint)
			timer.config(text = '%s:%s:%s'%(hour,mint,sec))
	else:
		sec = 59
		if mint > 0:
			if mint <= 10:
				mint -= 1
				mint = '0' + str(mint)
				timer.config(text = '%s:%s:%s'%(hour,mint,sec))
			else:
				mint -= 1
				timer.config(text = '%s:%s:%s'%(hour,mint,sec))
		else:
			if hour > 0:
				hour -= 1
				m = 59
				sec = 59
				timer.config(text = '%s:%s:%s'%(hour,mint,sec))
			else:
				timer.config(text = 'Finsh')
				period = 0
	t_now = time.strftime('%H:%M:%S')
	clock.config(text = t_now)
	if period != 0 :
		period = str(hour) + ',' + str(mint) +  ',' + str(sec)
	else:
		period = '0,00,00'
	clock.after(1000,clock_dis)

task_time_value = StringVar()
task_time = Entry(app,font=('times', 10 ,'bold'),textvariable=task_time_value)
task_time.grid(row=4,column=2,pady=10)


greatins = Label(app,font=('times', 10 ,'bold'),text='Welcome in Task Timer app',justify='center')
greatins.grid(row=1,column=1,columnspan=2,pady=30,ipadx=150)

task_name_value = StringVar()
task_name = Entry(app,font=('times', 10 ,'bold'),textvariable=task_name_value)
task_name.grid(row=3,column=2,pady=10)

label_task = Label(app,font=('times', 10 ,'bold'),text='Enter task\'s name',justify='left')
label_task.grid(row=3,column=1)

label_task_time = Label(app,font=('times', 10 ,'bold'),text='Enter task\'s period',justify='left')
label_task_time.grid(row=4,column=1,padx=10)

start = Button(app,text='Start',command=set_period_value)
start.grid(row=5,column=1,columnspan=2,pady=20)
#clock_dis()

app.mainloop()