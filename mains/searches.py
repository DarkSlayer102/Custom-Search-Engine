
import webbrowser
import tkinter as tk
from apiclient.discovery import build
from PIL import Image, ImageTk
from urllib.request import urlopen
import wikipedia
from essentials import header, white, GET_SEARCH, searching, zero


"""
In this project, we import all the necessary packages and libraries up here.
"""


""" 

Our GUI root or window is being created here to display the search engine. Additionally, some default background is included for later use and a Canvas is initialized

"""


root = tk.Tk() #We are using tk.Tk() to create a window for the GUI in this section.

#adding root title

root.title(header)

default_backgrounds = "#856ff8" # This is just a background color

canvas1 = tk.Canvas(root, width=1400, height=700, bg = default_backgrounds) #creating a canvas using tk.Canvars
canvas1.pack()



"""
In this section, I created an input or entry widget that enables the user to input their searches. Additionally, some placeholders are included. The input widget is added to the canvas so that it will be inside the canvas.

"""
entry1 = tk.Entry(root,width=90) #creating input
entry1.insert(zero,searching) #default value inside the input
canvas1.create_window(760, 140, window=entry1) #putting inside the canvas


#define a TITLE or a Header for the Interface and given some styles
TITLE = tk.Label(root, text=header, fg=white,
                 bg=default_backgrounds, font="Verdana 10 bold")

#Added the TITLE to the canvas
canvas1.create_window(760, 80, 
                      window=TITLE)

"""
    The main function performs all the necessary tasks to display the search results, such as the titles, descriptions, and images. 

    Each result is displayed using separate labels. It's important to note that a Google Cloud Platform API key is required for this project. 

    Additionally, a custom search engine (cse.google.com/cse) is used to provide the search results.

"""

def searching():
    x1 = entry1.get() #getting value from the input
    
    

    api_key = "YOUR API_KEY" #api_key

    resouce = build("customsearch", 'v1', developerKey=api_key).cse() 

    result = resouce.list(q=x1, cx="YOUR SEARCH ENGINE ID").execute() #getting the results

    for i in range(6):  
        #these are results and in a seperate labels 
        label1 = tk.Label(root, text=result['items'][zero]['title'], fg=white,
                 bg=default_backgrounds, font="Verdana 10 bold")
        label2 = tk.Label(root, text=result['items'][zero]['displayLink'], fg=white,
                 bg=default_backgrounds, font="Verdana 10 bold")
        label3 = tk.Label(root, text=result['items'][zero]['snippet'], fg=white,
                          bg=default_backgrounds, font="Verdana 10 bold")
        

        """
        To handle potential errors when performing searches, try-except blocks have been incorporated. 
        This is particularly important when dealing with images
        
        """

        try:
                
            URL =  result['items'][zero]['pagemap']['cse_thumbnail'][zero]['src'] 

            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            photo = ImageTk.PhotoImage(data=raw_data)

            label4 = tk.Label(image=photo)
            label4.image = photo
            canvas1.create_window(780, 490, window=label4,)

        except KeyError:
            print("Images are being showen")
        try:
            """
            The Wikipedia library is utilized to provide a summary of the input. 
            This gives an overall view of the search results and provides additional information about the topic.
            """
            Searching = wikipedia.summary(x1, sentences=2)
            label5 = tk.Label(root, text=Searching, fg="white",
                              bg=default_backgrounds, font="Verdana 8 bold")
            canvas1.create_window(780, 320, window=label5)
        except wikipedia.exceptions.DisambiguationError:
            print("Not Working")

        """
           The labels are added to the canvas and positioned correctly.
        """
        canvas1.create_window(780, 230, window=label1)
        canvas1.create_window(780, 260, window=label2)
        canvas1.create_window(780, 290, window=label3)
        


"""
    In this section, a button is created to allow users to click and view the search results. The button is added to the canvas

"""

#define button 
button1 = tk.Button(text=GET_SEARCH, command=searching,
                    width=20, height=2, font='Helvetica 10', bg="#4275f5", fg=white)
#adding the canvas
canvas1.create_window(760, 180, window=button1)

"""
The main tkinter while loop is executed here and will only terminate if we quit or an error occurs

"""

if __name__ == '__main__':
    #calling the main function
    root.mainloop()
