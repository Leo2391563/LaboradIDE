try:
    from tkinter import *
    from tkinter import ttk
    from pygments.token import Token
    from pygments.lexers import c_like
    import tokens, serial, config as cfg, subprocess, os, tkinter as tk, tkinter.messagebox
    from tkinter.filedialog import *
except ImportError:
    import subprocess
    subprocess.run("python -m pip install pyserial tkinter pygments os")
path = ""
edit = False

print(os.getcwd())

root = Tk()
root.title("LaboRad IDE")
root.minsize(1000,600)
root.iconbitmap(default="icon.ico")

lexer = c_like.ArduinoLexer()

code = Text(root,font=cfg.code_font,undo=True)
code.place(x=0,y=30, relwidth=1,relheight=0.75)

def undo():
    code.edit_undo()

def redo():
    code.edit_redo()

def cons_out(out = "\n"):
    console["state"] = "normal"
    console.insert(END, out)
    console["state"] = "disabled"

def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    avaiable_ports = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            avaiable_ports.append(port)
        except (OSError, serial.SerialException): pass
    return avaiable_ports

def boards():
    if cfg.use_auto_check_boards==True:
        out = subprocess.run(rf"{os.getcwd()}\arduino-cli board listall",capture_output=True)
        outdecoded = out.stdout.decode().split("\n")

        board = {}
        for i in outdecoded:
            board[i[0:33].rstrip()] = i[33:]
        del board["Наименование платы"]
        try:
            del board["Board Name"]
        except KeyError:
            del board[""]
        return board
    else:  return cfg.boards_
def programers():
    if cfg.use_auto_check_progs==True:
        out = subprocess.run(rf"{os.getcwd()}\avrdude -c?",capture_output=True)
        outdecoded = out.stderr.decode().split("\n")
        print(outdecoded)

        progs = []
        for i in outdecoded:
            i = i.replace(" ","")
            progs.append(i.split("=")[0])
        progs.pop(0)
        progs.pop(0)
        
        progs.pop()
        progs.pop()
        return progs
    else: return cfg.progs_

def load():
    file = open(rf"{os.getcwd()}\tempsketch\tempsketch.ino","w",encoding="UTF-8")
    file.write(code.get("1.0","end"))
    file.close()
    console.delete("1.0","end")
    cons_out("Компилирование...\n\n")
    compile_output = subprocess.run(rf"{os.getcwd()}\arduino-cli compile -b {boards()[board_comb.get()]} --no-color {os.getcwd()}\tempsketch --build-path {os.getcwd()}\tempbuild",capture_output=True)
    if compile_output.stderr.decode()=="":
        cons_out(compile_output.stdout.decode()+"\nКомпилирование завершено\n"+"\nЗагрузка...\n\n")
        load_output = subprocess.run(rf"{os.getcwd()}\avrdude -p m328p -U flash:w:{os.getcwd()}\tempbuild\tempsketch.ino.hex -q -P {port_comb.get()} -c arduino",capture_output=True)
        cons_out(load_output.stderr.decode("utf-8") + "\nЗагрузка завершена\n")
    else:
        console["state"] = "normal"
        console.insert(END, compile_output.stderr.decode("utf-8"))
        console["state"] = "disabled"

    print(compile_output.stderr.decode("utf-8"))

def open_file():
    global path, root
    opening = askopenfile(title="Открыть файл",filetypes=(("Arduino file", ".ino"),))
    if opening:
        with open(opening.name,"r",encoding="utf-8") as file:
            code.delete("1.0","end")
            code.insert(END, file.read())
        path = opening.name
        root.title(f"LaboRad IDE ({path})")

def save_as_file():
    global path, root
    saving = asksaveasfile(title="Сохранить файл как",filetypes=(("Arduino file", ".ino"),),defaultextension=".ino")
    if saving:
        with open(saving.name,"w",encoding="utf-8") as file:
            file.write(code.get("1.0","end"))
        path = saving.name
        root.title(f"LaboRad IDE ({path})")

def save_file():
    global path, root
    if path!="":
        try:
            with open(path,"w",encoding="utf-8") as file:
                file.write(code.get("1.0","end"))
        except FileNotFoundError:
            tkinter.messagebox.showwarning("Ошибка", "Не удалось сохранить файл автоматически")
            save_as_file()
    else:
        saving = asksaveasfile(title="Сохранить файл",filetypes=(("Arduino file", ".ino"),),defaultextension=".ino")
        if saving:
            with open(saving.name,"w",encoding="utf-8") as file:
                file.write(code.get("1.0","end"))
            path = saving.name
            root.title(f"LaboRad IDE ({path})")

for i in tokens.tag_:
    code.tag_config(i, foreground=tokens.tag_[i])

# Прописываем соответствие типа токена тегу подсветки
token_type_to_tag = tokens.token_

def get_text_coord(s: str, i: int):
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'
        
        i -= len(line)


def on_edit(event):
    # Удалить все имеющиеся теги из текста
    for tag in code.tag_names():
        code.tag_remove(tag, 1.0, tk.END)
    
    # Разобрать текст на токены
    s = code.get(1.0, tk.END)
    tokens = lexer.get_tokens_unprocessed(s)
    
    for i, token_type, token in tokens:
        print(i, token_type, repr(token))  # Отладочный вывод - тут видно какие типы токенов выдаются
        j = i + len(token)
        if token_type in token_type_to_tag:
            code.tag_add(token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))

    # Сбросить флаг редактирования текста
    code.edit_modified(0)


code.bind('<<Modified>>', on_edit)

load_btn = ttk.Button(root,text="Загрузить",command=load)
load_btn.place(x=0,y=0)

console = Text(root,font=cfg.console_font)
console.place(rely=0.75, relwidth=1,relheight=0.25)
console["state"] = ("disabled")

port_comb = ttk.Combobox(values=serial_ports(),width=10)
port_comb.place(x=80,y=3)

board_comb = ttk.Combobox(values=list(boards().keys()),width=33)
board_comb.place(x=170,y=3)

prog_comb = ttk.Combobox(values=programers(),width=10)
prog_comb.place(x=400,y=3)

code.insert(END, cfg.default_sketch)

mainmenu = Menu(root)
root["menu"] = mainmenu

filemenu = Menu(mainmenu, tearoff=False)
filemenu.add_command(label="Открыть", accelerator="Ctrl+O", command=open_file)
filemenu.add_command(label="Сохранить", accelerator="Ctrl+S", command=save_file)
filemenu.add_command(label="Сохранить как", accelerator="Ctrl+Shift+S", command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.destroy)

correctmenu = Menu(mainmenu, tearoff=False)
correctmenu.add_command(label="Отменить",accelerator="Ctrl+Z",command=undo)
correctmenu.add_command(label="Вернуть",accelerator="Ctrl+Y",command=redo)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Правка", menu=correctmenu)

def tab(event):
    code.insert(INSERT, " " * 4)
    print("tab")

code.bind("<Tab>",tab)
code.focus()

root.bind_all("<Control-KeyPress-s>", lambda evt: save_file)
print(boards())
print("\n\n\n",programers(),"\n\n")

root.mainloop()