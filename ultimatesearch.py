from tkinter import *
import customtkinter as ck
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Default Theme Set
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")

#Seperates Browser from GUI to keep browser open until user closes
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Search Function
def Search_pls(entry, drop_box):
    wbrowser = webdriver.Chrome(chrome_options=chrome_options)
    print(drop_box)
    if drop_box == "Google":
        wbrowser.get("https://google.com")
    elif drop_box == "Bing":
        wbrowser.get("https://bing.com")
    else:
        wbrowser.get("https://duckduckgo.com")
    wbrowser.maximize_window()
    input_Element = wbrowser.find_element(By.NAME,'q')
    input_Element.send_keys(entry)
    input_Element.submit()

#Theme Change Function
def new_theme(theme_swtch):
    if theme_swtch == "1":
        ck.set_appearance_mode("dark")
    else:
        ck.set_appearance_mode("light")

#Create Window
root = ck.CTk()
root.resizable(height=False,width=False)
#Window title
root.title("Ultimate Search")
#Size Window
root.geometry('450x600')

#Heading
label = ck.CTkLabel(root, text="Ultimate Search",font=('Times',40))
label.place(relx=.5, rely=.3,anchor=CENTER)

#Searchfield
entry = ck.CTkEntry(root)
entry.place(relx=.5, rely=.4, relwidth=.80, anchor=CENTER)

#Dropdown Box
drop_box =ck.CTkOptionMenu(root, values=["Google","Bing","DuckDuckGo"] )
drop_box.place(relx=.325, rely=.5,anchor=CENTER)
drop_box.set("Google")

#Button Bound to Search Function
button = ck.CTkButton(root, text="GO!", command=lambda: Search_pls(entry.get(),drop_box.get()))
button.place(relx=.675,rely=.5,anchor=CENTER)

#Change Theme
theme_swtch = ck.CTkSwitch(root, text="Theme", onvalue="1",offvalue="0",command=lambda:new_theme(theme_swtch.get()))
theme_swtch.place(relx=.85,rely=.9,anchor=CENTER)
theme_swtch.select()
#Binds Enter to the go button/event
root.bind('<Return>',lambda event: Search_pls(entry.get(),drop_box.get()))

root.mainloop()