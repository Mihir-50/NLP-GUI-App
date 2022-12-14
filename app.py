# to make GUI use tkinter library
from tkinter import *
# import DataBase class from module or file MyDataBase(self made)
from MyDataBase import DataBase
# from this I can show user that, email registored or email exist in a pop out
from tkinter import messagebox
from MyAPI import API

class NLPApp:

    def __init__(self):
        # create a Database object
        self.dbo = DataBase()
        # create object of API class which is in APIhandeling module/file
        self.apio = API()
        # to make login GUI
        # 'root' is reference variable(object) of Tk class which can access attribute & methods of Tk class
        self.root = Tk()
        # change title of GUI
        self.root.title('NLP App')
        # put favicon image on GUI
        self.root.iconbitmap('resources/favicon.ico')
        # control size of GUI
        self.root.geometry('350x600')
        # change background color of GUI using HTML 'Hexcode'
        self.root.configure(bg='#1C2833')
        # calling login_gui method
        self.login_gui()
        # 'mainloop' method is to hold GUI on screen
        self.root.mainloop()


    # method to make login page which is on GUI
    def login_gui(self):

        self.clear()

        # want to display some text on GUI (LABEL class in tkinter)
        heading = Label(self.root,text='NLP App',bg='#1C2833',fg='white')
        # explicitly tell tkinter to put heading on GUI --> Geometry Manager --> (i)-Pack (ii)-Grid
        # pady gives gap from top and bottom and in pixels
        heading.pack(pady=(30,30))
        # increase font size of heading
        heading.configure(font=('verdana',24,'bold'))

        # writing 'Enter Email' on GUI
        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        # to create entry box where user will type his email
        self.email_input = Entry(self.root,width=50)
        # ipady use to increase height of email_input box
        self.email_input.pack(pady=(5,10),ipady=8)

        # writing 'Enter Password' on GUI
        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))
        # to create entry box where user will type his password
        self.password_input = Entry(self.root, width=50,show='*')
        # ipady use to increase height of email_input box
        self.password_input.pack(pady=(5, 10), ipady=8)

        # to create button --> here we can give height to the button
        login_btn = Button(self.root,text='Login',width=30,height=2,command = self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        # to create registor button
        # detect whether a button is pressed or not use 'command'
        redirect_btn = Button(self.root, text='Registor Now',command=self.registor_gui)
        redirect_btn.pack(pady=(10, 10))


    # method to make registeration page which is on GUI
    def registor_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#1C2833', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(5, 10))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=8)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(5, 10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=8)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(5, 10))
        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=8)

        registor_btn = Button(self.root, text='Register', width=30, height=2,command=self.perform_registration)
        registor_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    def perform_registration(self):
        # fetch data from GUI i.e., what user has entered
        # get() fetches name & we store into variable 'name','email','password'
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registration Successful,You can login now')
        else:
            messagebox.showerror('Error','Email Already Exists')


    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Login Successfull')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect Email/Password')


    def home_gui(self):
       self.clear()

       heading = Label(self.root, text='NLP App', bg='#1C2833', fg='white')
       heading.pack(pady=(30, 30))
       heading.configure(font=('verdana', 24, 'bold'))

       sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
       sentiment_btn.pack(pady=(10, 10))

       ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.ner_gui)
       ner_btn.pack(pady=(10, 10))

       emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.emotion_gui)
       emotion_btn.pack(pady=(10, 10))

       abuse_btn = Button(self.root, text='Abuse Prediction', width=30, height=4, command=self.abuse_gui)
       abuse_btn.pack(pady=(10, 10))

       logout_btn = Button(self.root, text='Logout', command=self.login_gui)
       logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#1C2833', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#1C2833', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the Text')
        label1.pack(pady=(5, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=15)

        sentiment_btn = Button(self.root, text='Analyze Sentiment',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        # use to show result of entered information which is coming from API
        self.sentiment_result = Label(self.root, text='',bg='#1C2833',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        # font of result which we show to user
        self.sentiment_result.configure(font=('verdana', 15))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        sorted_dict = dict(sorted(result['sentiment'].items(),key=lambda x:x[1],reverse=True))
        
        txt = ''
        for i in sorted_dict:
            txt = txt + i + ' -> ' + str(sorted_dict[i]) + '\n'

        # This line stores txt (data coming from API) in the 'text' key of the sentiment_result dictionary (self.sentiment_result['text'] = txt). The method then updates the text attribute of Label class (which is empty) using the configure method (self.sentiment_label.configure(text=txt)).
        self.sentiment_result['text'] = txt


    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#1C2833', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#1C2833', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 15))

        label1 = Label(self.root, text='Enter the Text')
        label1.pack(pady=(5, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=15)

        ner_btn = Button(self.root, text='Classify Name', command=self.do_ner)
        ner_btn.pack(pady=(10, 10))

        # use to show result of entered information which is coming from API
        self.ner_result = Label(self.root, text='', bg='#1C2833', fg='white')
        self.ner_result.pack(pady=(5, 5))
        # font of result which we show to user
        self.ner_result.configure(font=('verdana', 12))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def do_ner(self):

        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)
        txt = ''
        for dictionary in result['entities']:
            for key,value in dictionary.items():
                txt = txt + key +' -> '+ str(value) + '\n'
            txt = txt + '\n'
        self.ner_result['text'] = txt


    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#1C2833', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Prediction', bg='#1C2833', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 15))

        label1 = Label(self.root, text='Enter the Text')
        label1.pack(pady=(5, 10))

        self.emotion_prediction_input = Entry(self.root, width=50)
        self.emotion_prediction_input.pack(pady=(5, 10), ipady=15)

        ner_btn = Button(self.root, text='Find Emotion', command=self.do_emotion_prediction)
        ner_btn.pack(pady=(10, 10))

        # use to show result of entered information which is coming from API
        self.emotion_prediction_result = Label(self.root, text='', bg='#1C2833', fg='white')
        self.emotion_prediction_result.pack(pady=(5, 5))
        # font of result which we show to user
        self.emotion_prediction_result.configure(font=('verdana', 12))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def do_emotion_prediction(self):
        text = self.emotion_prediction_input.get()
        result = self.apio.emotion_prediction(text)
        sorted_dict = dict(sorted(result['emotion'].items(), key=lambda x: x[1], reverse=True))

        txt = ''
        for i in sorted_dict:
            txt = txt + i + ' -> ' + str(sorted_dict[i]) + '\n'

        self.emotion_prediction_result['text'] = txt


    def abuse_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#1C2833', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Abuse Prediction', bg='#1C2833', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 15))

        label1 = Label(self.root, text='Enter the Text')
        label1.pack(pady=(5, 10))

        self.abuse_prediction_input = Entry(self.root, width=50)
        self.abuse_prediction_input.pack(pady=(5, 10), ipady=15)

        abuse_btn = Button(self.root, text='Find Abuse', command=self.do_abuse_prediction)
        abuse_btn.pack(pady=(10, 10))

        # use to show result of entered information which is coming from API
        self.abuse_prediction_result = Label(self.root, text='', bg='#1C2833', fg='white')
        self.abuse_prediction_result.pack(pady=(5, 5))
        # font of result which we show to user
        self.abuse_prediction_result.configure(font=('verdana', 12))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def do_abuse_prediction(self):
        text = self.abuse_prediction_input.get()
        result = self.apio.abuse_prediction(text)
        sorted_dict = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

        txt = ''
        for i in sorted_dict:
            txt = txt + i + ' -> ' + str(sorted_dict[i]) + '\n'

        self.abuse_prediction_result['text'] = txt


    # function is used to clear existing GUI
    def clear(self):
        # pack_slaves() take out all the element which is on GUI
        for i in self.root.pack_slaves():
            i.destroy()



nlp = NLPApp()