#i went build the task timer which i can enter the name of the task
#and how much time it take than enter start to begining
#the gui should has the digetal clock 


from tkinter import *
import time



app = Tk()


label_time = Label(app,font=('times', 15 ,'bold'),text='The time now')
label_time.grid(row=1,column=1)
clock = Label(app,font=('times', 20 ,'bold'))
clock.grid(row=2,column=1,padx=20,pady=10)
label_timer = Label(app,font=('times', 15 ,'bold'),text='Timer')
label_timer.grid(row=1,column=2)
timer = Label(app,font=('times', 20 ,'bold'))
timer.grid(row=2,column=2)

def set_time_varibal(period):
	period = period.replace(',','')
	hour = int(period[0])
	mint = int(period[1:3])
	sec = int(period[-2:])
	return hour,mint,sec

period = '1,01,20' #this just example for the timer

def clock_dis(): #this function responsive about the clock and the timer.
	global period
	hour,mint,sec = set_time_varibal(period)
	if sec > 0:
		if sec <= 10:
			sec -= 1
			sec = '0' + str(sec) 
			if mint <= 10:
				mint = '0' + str(mint)
			timer.config(text = '%s:%s:%s'%(hour,mint,sec))
		else:
			sec -= 1
			if mint <= 10:
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
	t_now = time.strftime('%H:%M:%S')
	clock.config(text = t_now)
	period = str(hour) + ',' + str(mint) +  ',' + str(sec)
	clock.after(1000,clock_dis)

task_name = Label(app,font=('times', 20 ,'bold'))
task_name.grid(row=3,column=1,columnspan=2)
task_name.config(text = 'Solve the ')

clock_dis()

app.mainloop()