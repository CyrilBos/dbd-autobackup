# Presentation
This very short script copies files located at to another. By using Google Drive Desktop, these files are then copied on your local directory, which is then automatically synced to your "free" Google Drive cloud. The backup will have the date in its filename, in the year-month-day-hour-second-miliseconds format (to avoid overwriting older saves, in case the script copies a corrupted one, and "oh on last tuesday it worked fine so let's try"). One backup weights approximately 80KB, so you should not have to worry about the space it takes. 

The backupped files are the ones under the remote folder in Steam userdata DbD folder, as suggested on [BHVR official post](http://steamcommunity.com/app/381210/discussions/9/1471967615864881023/). I tried myself by executing the script, deleting the files under the steam folder (could not log into the game), then restored the backup and could play normally and didn't loose any progression. I might make a video someday as a proof (or if anyone else wants to, feel free to do so). 

Following the instructions, the script will be executed at boot time (not if you just make your computer sleep and), probably at. Anyway, manually double clicking the .bat file will make one of these saves, without breaking the automatic one at boot time. So you can make a desktop shortcut of this .bat file (right click on the file->send to->desktop). For more advanced users, you might want to look on how to add a scheduled task that executes this .bat file.

You probably can use this with any other cloud storage provider (Dropbox, OneDrive, ...) that offers software to automatically sync cloud and local files, but I have tested only with Google Drive, so try at your own "risks" (trying another cloud provider will most probably not mess up your files). 

# Installation and configuration /!\ IMPORTANT WILL NOT WORK AT ALL WITHOUT FOLLOWING THIS

1. Create a Google account.
2. Install and configure [Google Drive Desktop](https://www.google.com/drive/download/). **Preferably, let it be launched on startup**. 
3. Install latest version of Python 3 for Windows (right now is 3.6.4), choose the **executable installer** at the bottom of [this page](https://www.python.org/downloads/release/python-364/). Choose x86-64 if your computer is running a 64bit platform (most likely if it is not old), x86 otherwise. **DO NOT FORGET TO TICK "Add Python 3.6 to PATH", and do not move where it has been installed afterwards.**
4. Download the zipped source code of this repository (click the green "clone or download button" on this page), unzip it anywhere you want (avoid C:\Program Files and such, might create permission problems if you are not administrator. i.e C:\dbd-autobackup should be fine).
5. open `dbd_backup.py` with a text editor (notepad++, sublime text, ... but avoid Word/Writer and such, these are text processors and not editors and might fuck up the encoding of the file. Basic notepad should be fine but I don't use it personally). 
6. Modify the value of the variable `backup_root_path` to the location of your backup folder **INSIDE** your local Google Drive folder. I let my own path so it is clearer, yours should be similar if you let the default location at the installation, just replace the `YOURUSERNAME` and the `YOURSTEAMIDPROFILE`. It does not matter to keep the `Steam/userdata/YOURSTEAMIDPROFILE/381210/` part, you can replace it with whatever you want, but it helps you remind where is the location of the files actually used by the game when you want to restore it. 
7. Modify the value of the variable `steam_userdata_path` at the top of the file to specify the location of your steam user data. To get your steam id profile if you have multiple steam accounts on the same, [follow these instructions](https://steamcommunity.com/sharedfiles/filedetails/?id=209000244), or use [https://steamidfinder.com/](https://steamidfinder.com/). 
8. Modify the `autostart-dbd-backup.bat` file, replace `PATHTOTHEUNZIPPEDCODE\dbd_backup.py` by the path where you put the Python script you just modified in steps 6 and 7.
9. Create a shortcut of the file (right click->Create shortcut), copy or cut this shortcut
10. Open the execute command of windows (windows key + R), copy paste this command, and click OK:
```shell:startup```
11. It should have opened the windows explorer in the startup folder location (something like `C:\Users\YOURUSERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`), paste the shortcut in there.
12. ???
13. PROFIT

Additional steps (testing it works): 
1. might need to restart your computer for the new software to work correctly
2. manually backup your save files somewhere safe
3. run the script by double click on the shortcut inside the startup folder (follow step 10 to open it again)
4. delete the save files under your steam user data. Optional: launch the game and see that it does not work as intended
5. use the files created by the automatic backup. located under your google drive folder (the `backup_root_path` location)
6. launch the game and hopefully it works
7. if it is still broken, use your manual backup created at step 2. If it still does not work, that is not my fault, you might not have manually backupped your files properly at step 2, or something crazy unrelated to my code happened. *Please create an issue on the repository in that case*, so we can debug this for others. 
8. Do not touch anything if you do not know what you are doing, you are not going to impress your hot neighbour/roommate with that (trust me, I tried) (unless you are a female, then go for it). 

Tested on official updated Windows 10, latest Google Drive Desktop. Do not forget your 

# Bannable? Dangerous? 
I Can not say a 100% sure no, but most probably should not be (99.9% no). This does not alter your game files, this is not run at the same time as Dead By Daylight nor does not try to hack it in anyway. The script is so short anyone should be able to understand it even without any programming knowledge. Or just ask your developer friend to check it for you (and please star it so people are more inclined to believe it), it should not take him/her much time.

The downside is that it opens an easy access to your Google Drive contents if someone accesses your computer (locally or remotely). If you use a garbage throwaway Google account then I would say there is no real risk. 

# Additional notes
You can use the script without Google Drive synchronization, the files will be backupped locally, but if your hard disk or whatever. 
The script can be easily modified to save all your steam games save files, however it will increase the size of each individual daily backup (mine is at 25MB, where as DBD is only 80KB). You might want to keep a version only for DBD that is executed daily, and copy the script and modify it for a global version that you can execute manually or every week or so with a scheduled task (google it). 
To modify the `dbd_backup.py` into a general steam backup: 
- modify `backup_root_path` `variable value to end just to `Steam/userdata/YOURSTEAMIDPROFILE`
- change the last line to:
```shutil.copytree(steam_userdata_path, new_backup_path)```

The created backup-yyyy-mm-dd-hh-mm-s-ms files should contain all your steam save files.

# For potential contributors/To-do: 
Non-developers: 
- test with other cloud solutions than Google 
- suggest improvements, ask for help and clarifications (might have forgotten something in the instructions). [Create an issue on this repository, *please check it is not a duplicate*, if it is, comment on the already existing issue instead](https://github.com/CyrilBos/dbd-autobackup/issues)
- guide translations into other languages for bed anglish speekurz
- whatever constructive


Developers:
- develop a restore script (and move config parameters into a config file)
- Make an automated installer, probably with py2exe or something similar, to make the installation steps clearer and easier to follow. 
- maybe develop it into a little GUI
- automatize detection of save files location (hard with multiple steam accounts)
- Mac version

If anyone is willing to participate and improve, feel free to fork and make a pull request afterwards (or just fork and say f**k you to me, that's up to you). I developed this by pure personal interest since I lost my save once, but made the effort of writing this guide so anyone can profit of this too :)

