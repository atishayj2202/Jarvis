from Tkinter import *
from inupsign import getinuser, getupuser
from TtS import speak

mainwin = Tk()
mainwin.geometry('300x400')
mainwin.resizable(width=False, height=False)
mainwin.columnconfigure(0,weight=1,pad=0)
mainwin.rowconfigure(0, weight=1,pad=0)

def tkr(frame, title="Jarvis"):
    mainwin.title(title)
    frame.tkraise()

class Placeholder_State(object):
    __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="grey", font=None, extra=0):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color = normal_color
    state.normal_font = normal_font
    state.placeholder_color = color
    state.placeholder_font = font
    state.placeholder_text = placeholder
    state.with_placeholder = True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg=state.normal_color, font=state.normal_font)
            if extra == 1:
                entry.config(show="*")
            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg=state.placeholder_color, font=state.placeholder_font, show="")

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg=color, font=font, show="")

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state

sup = Frame(mainwin, bg="black", height=600, width=300)
sin = Frame(mainwin, bg="black", height=400, width=300)

for frame in (sup, sin):
    frame.grid(row=0, column=0, sticky="nsew")


#SIGN IN PAGE

sin.columnconfigure(0,weight=1,pad=5)
sin.rowconfigure(0, weight=1)
sin.rowconfigure(6, weight=1)

#title
cred = Label(sin, bg = "Black",fg = "red", font = "Helvetica 10 bold")
cred.grid(row=1, column=0, sticky="we")


#username
undata = Entry(sin, borderwidth=10, relief=FLAT, font = "Helvetica 10", bg ="#404040", fg ="white")
undata.grid(row=2, column=0, sticky="we", padx = 10, pady=2)
add_placeholder_to(undata,"Email")

#password
pwdata = Entry(sin, borderwidth=10, relief=FLAT, font = "Helvetica 10", show="*", bg ="#404040", fg ="white")
pwdata.grid(row=3, column=0, sticky="we", padx = 10, pady=10)
add_placeholder_to(pwdata,"Password", extra=1)

# signup button
gsignup = Button(sin, text="Click Here for Sign Up",bg="red", command=lambda: tkr(sup,"Sign Up - Jarvis"), font = "Helvetica 10")
gsignup.grid(row=5,column=0,sticky="we", padx = 10, pady=7)
#sign in button
def startin():
    signing["state"]=DISABLED
    creddata = getinuser(undata.get(), pwdata.get())
    if creddata == False:
        cred.config(text="Please enter correct credentials")
    else:
        print(creddata)
        full = "Hello, " + creddata.title() + " Sir"
        cred.config(text=full)
        mainwin.destroy()
        speak("Hello sir, How can I help You?")

signing = Button(sin, text="Sign In",bg="red",fg="white", command = startin, font = "Helvetica 10 bold")
signing.grid(row=4,column=0,sticky="we", padx = 10, pady=3)




#SIGNUP
sup.columnconfigure(0,weight=1,pad=5)
sup.rowconfigure(0, weight=1)
sup.rowconfigure(8, weight=1)

#title
credu = Label(sup, bg = "Black",fg = "red", font = "Helvetica 10 bold")
credu.grid(row=1, column=0, sticky="nsew")

#name
namef = Entry(sup, borderwidth=10, relief=FLAT, font = "Helvetica 10", bg ="#404040", fg ="white")
namef.grid(row=2, column=0, sticky="we", padx = 10, pady=2)
add_placeholder_to(namef,"Nick Name")

#Username
undatau = Entry(sup, borderwidth=10, relief=FLAT, font = "Helvetica 10", bg ="#404040", fg ="white")
undatau.grid(row=3, column=0, sticky="we", padx = 10, pady=10)
add_placeholder_to(undatau,"Email")

#password
passwordu = Entry(sup, borderwidth=10, relief=FLAT, font = "Helvetica 10", bg ="#404040", fg ="white")
passwordu.grid(row=4, column=0, sticky="we", padx = 10, pady=2)
add_placeholder_to(passwordu,"Password",extra=1)

#retype password
rpasswordu = Entry(sup, borderwidth=10, relief=FLAT, font = "Helvetica 10", bg ="#404040", fg ="white")
rpasswordu.grid(row=5, column=0, sticky="we", padx = 10, pady=10)
add_placeholder_to(rpasswordu,"Retype Password", extra=1)

#signin Button
gsignin = Button(sup, text="Click Here for Sign In", bg="red", command=lambda: tkr(sin,"Sign Up - Jarvis"), font = "Helvetica 10")
gsignin.grid(row=7,column=0,sticky="we", padx = 10, pady=7)

#signup button
def makeuser():
    signpu["state"] = DISABLED
    rpword = rpasswordu.get()
    pword = passwordu.get()
    name = namef.get()
    uname = undatau.get()
    if name != "Nick Name":
        if pword != "Password":
            if rpword != "Retype Password":
                if uname != "Email":
                    if rpword == pword:
                        if len(pword) > 5:
                            userdata = getupuser(uname, pword, name)
                            if userdata == False:
                                credu.config(text="This Username Already Exsists.")
                            else:
                                credu.config(text="Succesfully, Made New User")
                                mainwin.destroy()
                                speak("Hello sir, I am Jarvis. I am your personal virtual assistant. I will help, "
                                      "you to manage & remember tasks, do programming, manage your listening activity,"
                                      " do basic calculations & explore internet")
                        else:
                            credu.config(text="Your Password is Short.\nMinimum 6 Characters Required")
                    else:
                        credu.config(text="Your Password and \nRetype Password does'nt match.")
                else:
                    credu.config(text="Please Enter Your Email.")
            else:
                credu.config(text="Please Retype Your Password.")
        else:
            credu.config(text="Please Enter Your Password.")
    else:
        credu.config(text="Please Enter Your Name.")
    signpu["state"] = NORMAL

signpu = Button(sup, text="Sign Up",bg="red",fg="white", command=makeuser, font = "Helvetica 10 bold")
signpu.grid(row=6,column=0,sticky="we", padx = 10, pady=3)


tkr(sin,"Sign In - Jarvis")
def create_UI():
    print("makingGUI")
    mainwin.mainloop()