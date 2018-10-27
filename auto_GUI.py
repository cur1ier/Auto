import tkinter as tk
from auto import *

dir_path = "./cpp"
file_list = get_filename(dir_path)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    exe = str(value).split(".")[0] + ".exe"
    res = get_result(exe, "test_data.txt")
    text_res.delete(1.0, tk.END)
    text_res.insert(tk.END, res)
    if res == ans:
        text_res.insert(tk.END, "\n\nCORRECT")
    else:
        text_res.insert(tk.END, "\n\nWRONG!")

def BtnClick():
    try:
        total_cpp = compile_all()
        label['text'] += str(total_cpp)
    except:
        print("error")

win = tk.Tk()
win.title("auto")
win.geometry("1000x600")

frame = tk.Frame(win)
frame.grid(row=0, column=0)

cpp_lb = tk.Label(frame, text="cpp file")
cpp_lb.pack()

listNodes = tk.Listbox(frame, width=18, height=20, font=("Helvetica", 12))
listNodes.pack(side="left", fill="y")
listNodes.bind('<<ListboxSelect>>', onselect)

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=listNodes.yview)
scrollbar.pack(side="right", fill="y")

listNodes.config(yscrollcommand=scrollbar.set)

file_list = get_filename('./cpp/')
for filename in file_list:
    listNodes.insert(tk.END, filename)

compile_frame = tk.Frame(win)
compile_frame.grid(row=1, column=0)

label = tk.Label(compile_frame, text="compile files: ", width=15, height=2)
label.pack()

tk.Button(compile_frame, text="compile all", command=BtnClick).pack()

res_frame = tk.Frame(win)
res_frame.grid(row=0, column=1)

res_lb = tk.Label(res_frame, text="result")
res_lb.pack()

res = get_result("A3-107502018.exe", "test_data.txt")
ans = get_answer("answer.cpp", "test_data.txt")

text_res = tk.Text(res_frame, width=50)
text_res.pack()
text_res.insert(tk.END, res)

ans_frame = tk.Frame(win)
ans_frame.grid(row=0, column=2)

ans_lb = tk.Label(ans_frame, text="answer")
ans_lb.pack()

text_ans = tk.Text(ans_frame, width=50)
text_ans.pack()
text_ans.insert(tk.END, ans)




win.mainloop()
