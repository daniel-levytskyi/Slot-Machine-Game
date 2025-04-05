import tkinter as tk
import random
import time

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Slot Machine Game")

symbols = ['🍒', '🍋', '🔔', '💎', '🍀', '❤️', '🍉']

#CLOSING WITH ESCAPE
def close(event=None):
    root.destroy()
root.bind("<Escape>", close)

mainText = tk.Label(root, text="💥️ Slot Machine Game 💥️", font=("Impact", 48, "bold"))
mainText.pack(pady=20)

#MAKING THE BLACK BARS
frame = tk.Frame(root, bg='black', height=500, width=1000)
frame.pack(pady=40)
frame.pack_propagate(False)

iconList = []
for i in range(3):
    icon = tk.Label(frame, text="❓️", font=("Arial", 150, "bold"))
    icon.pack(side='left', expand=True, fill='both', pady=50)
    iconList.append(icon) #ADDING EACH ICON TO A LIST TO MANAGE LATER

def spinCommand(event=None):
    def animate(index, delay):
        #ANIMATION
        for _ in range(20):
            iconList[index].config(text=random.choice(symbols))
            root.update_idletasks()
            time.sleep(0.01)
        #SLOWING DOWN THE ANIMATION
        for delay in [0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.2, 0.3]:
            iconList[index].config(text=random.choice(symbols))
            root.update_idletasks()
            time.sleep(delay)
    #START ANIMATION
    animate(0,0)
    root.after(500, animate, 1, 500) #PLAYS AFTER 500MS
    root.after(1000, animate, 2, 1000) #PLAYS AFTER 1000MS
    #CHECKING FOR WIN AFTER ANIMATIONS HAVE ALL RUN
    root.after(1500, checkForWin)

def checkForWin():
    #COMPARES ALL THE SAVED ICONS
    if(iconList[0].cget("text") == iconList[1].cget("text") == iconList[2].cget("text")):
        resultMessage.config(text="🎉️ JACKPOT!!! 🎉️")
    else:
        resultMessage.config(text=r"99% of gamblers quit before they win big")

spin = tk.Button(root, text="SPIN", command=spinCommand, font=("Arial", 50))
spin.pack()

resultMessage = tk.Label(root, text="", font=("Arial", 70))
resultMessage.pack()

exitButton = tk.Button(root, text=" EXIT ", command=close, font=('Arial', 25))
exitButton.pack(pady=20)

root.mainloop()
