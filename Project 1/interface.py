import tkinter as tk


root = tk.Tk()
root.title("Text RPG")

label = tk.Label(root, text="Welcome")
label.pack()

entry = tk.Entry(root)
entry.pack()

def start_game():
    while True:
        player_name = entry.get()
        if player_name.isalpha():
            break
            

    label.pack_forget()
    entry.pack_forget()
    button.pack_forget()

    label_v2 = tk.Label(root, text=f"Are you ready, {player_name}?")
    label_v2.pack()


button = tk.Button(root, text="Начать игру", command=start_game)
button.pack()



root.mainloop()
