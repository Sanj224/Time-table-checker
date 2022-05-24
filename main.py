from tkinter import *
import csv


def linearSearch(x, y):
    flag = False
    for i in x:
        if i == y:
            flag = True
            #print (flag)
    if flag == True:
        return (True)
    else:
        return (False)


def Confirm():
    global TheDate
    TheDate = str(dateval.get())
    #if TheDate = '':
    #  TheDate = dateval2
    dateconfirm = linearSearch(lessonDate, TheDate)
    if dateconfirm == True:
        NewScreen()
    else:
        errorl = Label(
            root,
            text=
            'You have entered an invalid date \n Ask Sanj for help if you are struggling to use this'
        ).pack()


def NewScreen():
    global window
    root.destroy()
    window = Tk()
    window.geometry('900x600')
    window.title('Who Is Free!')
    #output = Label(window, text=text).pack()
    calculator()
    window.mainloop()


def calculator():
  text = 'PEOPLE WHO ARE FREE ON:'

  students = ["Sanj", "Anousheh", "Tamago", "Dart", "Shagun", "Ash", "Kishara", "Sabira","Rhea", "Rattus"]
  with open('Lessons1') as csvfile:
    csvReader = csv.reader(csvfile,delimiter=',')
    for row1 in csvReader:
      #print (TheDate)
    
      if row1[0] == TheDate:
        for i in row1:
          period = (row1[1])
          period = str(period)

          match = linearSearch(subjectlist, i)
          if match == True:
            with open ('Subjects1') as csvfile:
              csvreader = csv.reader(csvfile,delimiter=',')
              for row in csvreader:
                if row[0] == i:
                  for i in row:
                    freecheck=linearSearch(students,i)
                    #print (students)
                    if freecheck == True:
                      students.remove(i)
                if len(students)==0:
                  students = 'No one is free'
        text = text, '\n', period,':', students, '\n'
        students = ["Sanj", "Anousheh", "Tamago", "Dart", "Shagun", "Ash", "Kishara","Sabira","Rhea", "Rattus"]                   
  finalLabel = Label(window,text=text).pack()
  BackButton =Button(window,text='Check another date',command=screenone).pack()


def screenone():
  global root
  global dateval
  global dateval2
  root = Tk()
  root.geometry('500x300')
  root.title('Who Is Free?')
  info = Label(root, text='ENTER THE DATE BELOW IN DD/MM FORM').pack()
  dateval = Entry(root)
  dateval.pack()
  info2 = Label(
      root,
      text=
      'ONCE YOU HAVE ENTERED THE DATE IN THE CORRECT FORM \n\nCLICK THE BUTTON'
  ).pack()
  ConfirmButton = Button(root, text='CLICK ME', command=Confirm)
  ConfirmButton.pack()


 

screenone()
lessonDate = []
subjectlist = []

with open('Subjects') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        subjectlist.append(row[0])

with open('Lessons') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        lessonDate.append(row[0])
