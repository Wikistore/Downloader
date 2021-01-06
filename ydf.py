# საჭირო პაკეტების იმპორტირება
import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 



# მოცემული ფუნქციის აღწერა CreateWidgets()  
# რათა სევქმნათ საჭირო tkinter-ის ვიჯეტი 
def Widgets(): 
	link_label = Label(root, 
					text=" ლინკი : ", 
					bg="red") 
	link_label.grid(row=1, 
					column=0, 
					pady=5, 
					padx=5) 

	root.linkText = Entry(root, 
						width=55, 
						textvariable=video_Link) 
	root.linkText.grid(row=1, 
					column=1, 
					pady=5, 
					padx=5, 
					columnspan = 2) 

	destination_label = Label(root, 
							text="შენახვა :", 
							bg="red") 
	destination_label.grid(row=2, 
						column=0, 
						pady=5, 
						padx=5) 

	root.destinationText = Entry(root, 
								width=40, 
								textvariable=download_Path) 
	root.destinationText.grid(row=2, 
							column=1, 
							pady=5, 
							padx=5) 

	browse_B = Button(root, 
					text="საქაღალდე", 
					command=Browse, 
					width=10, 
					bg="red") 
	browse_B.grid(row=2, 
				column=2, 
				pady=1, 
				padx=1) 

	Download_B = Button(root, 
						text="გადმოწერა", 
						command=Download, 
						width=20, 
						bg="red") 
	Download_B.grid(row=3, 
					column=1, 
					pady=3, 
					padx=3) 

#განვსაზღვროთ Browse() რათა შეარჩიოს  
# საჭირო ფოლდერი ვიდეოს შესანახად """ .... """

def Browse(): 
	
	download_Directory = filedialog.askdirectory(initialdir="შენახვის ადგილი") 

	# დირექტორიის ჩვენება 
	# 
	download_Path.set(download_Directory) 

# განსაზღვრეთ Download() რათა გადმოწეროთ ვიდეო 
def Download(): 
	
	# შეიყვანეთ მომხმარებლის მიერ არჩეული ლინკი 
	Youtube_link = video_Link.get() 
	
	
	# ფაილის შენახვა 
	download_Folder = download_Path.get() 

	# შევქმნათ ობიექტი YouTube() 
	getVideo = YouTube(Youtube_link) 

	
	videoStream = getVideo.streams.first() 

	 
	videoStream.download(download_Folder) 

	# შეტყობინების ჩვენება 
	messagebox.showinfo("წარმატებით", 
						"გადმოიწერა და შეინახა\n"
						+ download_Folder) 

# ობიექტის შექმნა tk class 
root = tk.Tk() 

# ფონის ფერის მინიჭება 
# ზომა  tkinter ფორმის და 
# ზომის შეცვლის გამორთვა 
root.geometry("600x120") 
root.resizable(False, False) 
root.title("YDF YouTube Video Downloader") 
root.config(background="white")

# icon-ის დამატება 
root.iconbitmap('ydv1.ico')

# შევქმნათ tkinter ცვლადები 
video_Link = StringVar() 
download_Path = StringVar() 

# შემდეგი ფუნქციის დაძახება Widgets()  
Widgets() 




# მუდმივი ციკლი 
root.mainloop() 
