import os, sys
import time
import html
import shutil
from urllib.request import urlopen
import tkinter.ttk as ttk
import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from ttkthemes import ThemedTk

windowMain = ThemedTk(theme="equilux")
windowMain.geometry("570x180")
windowMain.resizable(False, False)
windowMain['background']='#464646'
windowMain.title("Workshop Downloader GUI")
icon = tk.PhotoImage(file='icon.png')
windowMain.iconphoto(False, icon)

originaldir = os.getcwd()

def steamgetdir():
    steamCDMlocation.set(str(filedialog.askopenfilename(initialdir = "./",title = "Select steamcmd.exe",filetypes = (("exe files","*.exe"),("all files","*.*")))))
def workshopgetdir():
    workshopItemLink.set(str(filedialog.askopenfilename(initialdir = "./",title = "Select link containing file",filetypes = (("txt files","*.txt"),("all files","*.*")))))
def downloadgetdir():
    downloadFolder.set(str(filedialog.askdirectory(initialdir = "/",title = "Select download destination folder")))

def openSteamCMDHelp():
    steamCMDHelp = tk.Toplevel()   
    steamCMDHelp.title("SteamCMD help")
    steamCMDHelp.geometry("765x444")
    steamCMDHelp.iconphoto(False, icon)
    steamCMDHelp['background']='#464646'
    steamCMDHelp.resizable(False, False)
    main_frame = tk.Frame(steamCMDHelp)
    main_frame.pack(fill=tk.BOTH,expand=1)
    main_frame['background']='#464646'
    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
    y_scrollbar = tk.Scrollbar(main_frame,orient=tk.VERTICAL,command=my_canvas.yview)
    y_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(tk.ALL))) 
    second_frame = tk.Frame(my_canvas)
    my_canvas.create_window((0,0),window= second_frame, anchor="nw")    
    second_frame['background']='#464646'
    my_canvas['background']='#464646'
    steamURLimage1 = ImageTk.PhotoImage(Image.open("./SteamCMD1.png"))
    second_frame.anchor1 = steamURLimage1
    steamURLimage2 = ImageTk.PhotoImage(Image.open("./SteamCMD2.png"))
    second_frame.anchor2 = steamURLimage2
    steamURLimage3 = ImageTk.PhotoImage(Image.open("./SteamCMD3.png"))
    second_frame.anchor3 = steamURLimage3
    steamURLimage4 = ImageTk.PhotoImage(Image.open("./SteamCMD4.png"))
    second_frame.anchor4 = steamURLimage4
    ttk.Label(second_frame, text ='Downloand steamCMD from here: https://developer.valvesoftware.com/wiki/SteamCMD').pack()
    ttk.Label(second_frame, image=steamURLimage1).pack()
    ttk.Label(second_frame, text ='Extract the zip, then delete the zip and run steamcmd.exe').pack()
    ttk.Label(second_frame, image=steamURLimage2).pack()
    ttk.Label(second_frame, text ='After running steamcmd.exe make sure it downloands all the files').pack()
    ttk.Label(second_frame, image=steamURLimage3).pack()
    ttk.Label(second_frame, text ='After everything is done type quit then hit enter').pack()
    ttk.Label(second_frame, image=steamURLimage4).pack()
    ttk.Label(second_frame, text ='Thats it! SteamCMD is now downloaded!').pack()
    steamCMDHelp.mainloop()

def openLinkHelp():
    linkHelp = tk.Toplevel(windowMain)
    linkHelp.title("Link Help")
    linkHelp.geometry("765x444")
    linkHelp.iconphoto(False, icon)
    linkHelp['background']='#464646'
    linkHelp.resizable(False, False)
    steamURLimage = ImageTk.PhotoImage(Image.open("./CopyPageURL.jpg"))
    linkHelp.anchor = steamURLimage
    ttk.Label(linkHelp, text ='Go to the desired mod in steam and right click on an empty place and click on "Copy Page URL"').pack()
    ttk.Label(linkHelp, image=steamURLimage).pack()

def bulkFilesHelp():
    BulkFilesHelp = tk.Toplevel(windowMain)
    BulkFilesHelp.title("Multiple Links Help")
    BulkFilesHelp.geometry("736x268")
    BulkFilesHelp.iconphoto(False, icon)
    BulkFilesHelp['background']='#464646'
    BulkFilesHelp.resizable(False, False)
    multipleLinksImage = ImageTk.PhotoImage(Image.open("./MultipleLinks.png"))
    BulkFilesHelp.anchor0 = multipleLinksImage
    ttk.Label(BulkFilesHelp, text ='If you want to download multiple links at once then make "list.txt" in the same folder as the program and paste the links as presented here:').pack()
    ttk.Label(BulkFilesHelp, image=multipleLinksImage).pack()

ttk.Label(windowMain, text="SteamCMD.exe location: ").grid(row=0, column=0)
steamCDMlocation = tk.StringVar()
ttk.Entry(windowMain, textvariable=steamCDMlocation, width= 50).grid(row=0, column=1) 
ttk.Button(windowMain, text="[...]", width=3, command= steamgetdir).grid(row=0, column=2)
ttk.Button(windowMain, text="[?]", width= 3, command=openSteamCMDHelp).grid(row=0, column=3)

ttk.Label(windowMain, text="Workshop Item link: ").grid(row=1, column=0, padx=(0, 24))
workshopItemLink = tk.StringVar()
ttk.Entry(windowMain, textvariable=workshopItemLink, width= 50).grid(row=1, column=1)
workshopItemLinkFileButton = ttk.Button(windowMain, text="[...]", width= 3, command= workshopgetdir, state= tk.DISABLED)
workshopItemLinkFileButton.grid(row=1, column=2)
ttk.Button(windowMain, text="[?]", width= 3, command=openLinkHelp).grid(row=1, column=3)

ttk.Label(windowMain, text="Download folder: ").grid(row=3, column=0, padx=(0, 38))
downloadFolder = tk.Variable()
ttk.Entry(windowMain, textvariable=downloadFolder, width= 50).grid(row=3, column=1)
DownloadFolderFileButton = ttk.Button(windowMain, text="[...]", width= 3, command= downloadgetdir)
DownloadFolderFileButton.grid(row=3, column=2)

link = workshopItemLink.get().splitlines()
def bulkfiles():
    bulkfilesBoolean = var1.get()
    if bulkfilesBoolean:
        workshopItemLinkFileButton["state"] = tk.NORMAL
        try:
            link = open(workshopItemLink.get()).read().splitlines
        except:
            pass
    else:
        workshopItemLinkFileButton["state"] = tk.DISABLED
        link = workshopItemLink.get().splitlines()

def bulkfilesD():
    bulkfiles()
    workshopItemLink.set("")



var2 = 0
var2 = tk.IntVar()
ttk.Checkbutton(windowMain, text='Rename downloaded folder to Mod name instead of ID',variable=var2, command=bulkfiles).grid(row=4, column=1)
downloadResponse=tk.StringVar()

def workshop():
    var2Value = var2.get()
    steamCMD = steamCDMlocation.get()
    downloadFolderValue = downloadFolder.get()
    bulkfilesBoolean = var1.get()
    workshopItemLinkValue = workshopItemLink.get()
    global link
    if steamCMD[-12:] != "steamcmd.exe":
        downloadResponse.set("steamcmd.exe is not selected!")
        return
    if bulkfilesBoolean:
        try:
            link = open(workshopItemLinkValue).read().splitlines()
        except:
            downloadResponse.set("list.txt not found!")
            return
        if workshopItemLinkValue[-8:] != "list.txt":
            print(link)
            downloadResponse.set("list.txt not found!")
            return
    else:
        link = workshopItemLinkValue.splitlines()
        if link == [] or (len(link[0]) < 51) or link[0][:51] != "https://steamcommunity.com/sharedfiles/filedetails/":
            print(link)
            downloadResponse.set("link is incorrect!")
            return
    if downloadFolderValue == "":
        downloadResponse.set("Download folder is not selected")
        return
    
    progress = 0
    for i in link:
        page = urlopen(i).read().decode("utf-8").splitlines()
        appidPre = page[(page.index('		<div class="apphub_AppDetails">')+1)].split("/")
        appid = appidPre[appidPre.index("apps")+1]

        if "&" in i:
            workshopItem = i.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=", "")[:-(len(i) - int(i.index("&")) )]
        if not "&" in i:
            workshopItem = i.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=", "")

        arguments = steamCMD +  " +force_install_dir " + downloadFolderValue + " +login anonymous "+  "+workshop_download_item "+ appid +" " + workshopItem + " +quit"
        downloadResponse.set("Downloading...")
        os.system(arguments)
        original = downloadFolderValue+r"\steamapps\workshop\content"+"\\"+appid+"\\"+workshopItem
        shutil.move(original,downloadFolderValue)
        os.chdir(downloadFolderValue)

        if var2Value:
            modNamePre = page[(page.index('\t\t\t<meta name="viewport" content="width=device-width,initial-scale=1">')+2)].split("::")
            modName = str(html.unescape(modNamePre[-1]).split("</title>")[0])
            modName = modName.replace("\\", "").replace("/", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
            print(modName)
            os.rename(workshopItem, modName)
        progress+=1
        downloadingResponse = "Downloaded "+ str(progress) + "/"+str(len(link))
        downloadResponse.set(downloadingResponse)
        os.chdir(originaldir)
        time.sleep(3)
    

var1 = tk.IntVar()
ttk.Checkbutton(windowMain, text='Multiple Links',variable=var1, command=bulkfilesD).grid(row=4, column=0, padx=(0, 50))
ttk.Button(windowMain, text="[?]", width= 3, command=bulkFilesHelp).place(x=110, y=88)

def yes():
    downloadResponse.set("you")

downloadResponse.set("")


downloadButton = ttk.Button(windowMain, text="Download", width=15, command=workshop)
downloadButton.grid(row=5, column=0, ipadx= 10)
T = ttk.Entry(windowMain, width=40,textvariable=downloadResponse, state=tk.DISABLED)
T.grid(row=5, column=1, ipady=10, padx=(0,58))
ttk.Label(windowMain, text="If the program is not responding, don't worry, its working!").place(x=10, y=160)
windowMain.mainloop()