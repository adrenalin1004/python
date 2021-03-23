from tkinter import *
#from PIL import ImageTk #jpg 이미지를 불러올때
import tkinter.ttk as ttk
import time
import tkinter.messagebox as msgbox

root = Tk()
root.title("Python GUI")
root.geometry("640x1000+100+100") #가로*세로 + x좌표 + y좌표
#root.resizable(True, False) #x(너비), y(높이) 크기 변경 여부

'''

# scrollbar = Scrollbar(root)
# scrollbar.pack(side="right", fill="y")
# mylist=Listbox(root,yscrollcommand=scrollbar.set)
# for line in range(50):
#     mylist.insert(END, str(line))
# mylist.pack(side=LEFT,fill=BOTH)
# scrollbar.config(command=mylist.yview)

# --- 버튼----------------------------------------
# btn1 = Button(root, text = "버튼1")
# btn1.pack()
# btn2 = Button(root, padx=5, pady=15, text="버튼2")
# btn2.pack()
# btn3 = Button(root, padx=15, pady=5, text="버튼3")
# btn3.pack()

# --- 라벨----------------------------------------
label1 = Label(root, text="하이")
label1.pack()

#photo = ImageTk.PhotoImage(file="C:\\Users\\jh\\Documents\\GitHub\\python\\nado-coding\\img01.jpg")
photo = PhotoImage(file="nado-coding/img01.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="nado-coding/img02.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()

# --- 텍스트----------------------------------------
txt = Text(root, width=20, height=3)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=50) #줄바꿈(엔터)가 안됨,한줄 입력
e.pack()
e.insert(0, "한 줄만 입력가능")

def btncmd():
    print(txt.get("1.0", END)) #1.0  1:첫번째라인, 0:첫번째 컬럼위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

# --- 리스트박스----------------------------------------
listbox = Listbox(root, selectmode="extended", height=3) #height=0 모두다보여줌, 3 : 3개만 보여줌
listbox.insert(0, "사과")
listbox.insert(1, "바나나")
listbox.insert(2, "딸기")
listbox.insert(END, "포도")
listbox.insert(END, "파인애플")
listbox.pack()

def btncmd1():
    listbox.delete(0) #0 : 맨앞항목 삭제, END:마지막항목 삭제
    print("1번째부터 3번째까지 항목: ", listbox.get(0,2))
    print("리스트에서는", listbox.size(), "개가 있어요.")
    print("선택한 항목: ", listbox.curselection())

btn = Button(root, text="listbox", command=btncmd1)
btn.pack()

# --- 체크박스----------------------------------------
chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 안 볼래", variable=chkvar)
chkbox.select() #자동선택처리,  deselelct 체크해제
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 안보기", variable=chkvar2)
chkbox2.pack()

def btncmd2():
    listbox.delete(0) #0 : 맨앞항목 삭제, END:마지막항목 삭제
    print(chkvar.get()) # 0: 체크해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="chkbox", command=btncmd2)
btn.pack()

# --- 라디오버튼----------------------------------------

Label(root, text="----------------메뉴를 선택하세요.--------------").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var).pack()
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var).pack()
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var).pack()
Label(root, text="----------------음료를 선택하세요.--------------").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="맥주", value="맥주", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd4():
    
    print(burger_var.get(), drink_var.get()) # 0: 체크해제, 1: 체크


btn = Button(root, text="주문", command=btncmd4)
btn.pack()

# --- 콤보박스----------------------------------------

values =[str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox.current(0) #0번째 인덱스 값 선택
combobox.pack()
combobox.set("카드 결제일")

def btncmd5():
    
    print(combobox.get()) # 0: 체크해제, 1: 체크

btn = Button(root, text="콤보박스", command=btncmd5)
btn.pack()

# --- 프로그래스바----------------------------------------
Label(root, text="----------------다운로드 진행(progressbar)--------------").pack()

#progressbar1 = ttk.Progressbar(root, maximum=100, mod="determinate") #indeterminate
p_var = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var) #indeterminate
#progressbar.start(10) #10ms마다 움직임
progressbar.pack()

def btncmd6():
    for i in range(101):
        time.sleep(0.01) #0.01초 대기

        p_var.set(i)
        progressbar.update()
        print(p_var.get())
    progressbar.stop()

btn = Button(root, text="시작", command=btncmd6)
btn.pack()

# --- 메뉴, menu----------------------------------------
def create_new_file():
    print("새파일을 만듭니다.")

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Edit")

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)


# --- 메세지박스, ----------------------------------------
Label(root, text="----------------메시지박스--------------").pack()
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고","모두 매진 되었습니다.")

def error():
    msgbox.showerror("에러", "결재 에러가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도", "일시적인 오류입니다. 다시하시겠습니까?")

def yesno():
    msgbox.askyesno("예/아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n 저장하시겠습니까?")
    print("응답:", response)
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")
    else:
        print("뭘까")
        
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="알림").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

# --- 프레임박스, ----------------------------------------
Label(root, text="메뉴를 선택해 주세요.").pack(side="top")
Label(root, text="주문하기").pack(side="bottom")

Label(root, text="----------------프레임--------------").pack()

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="사이다").pack()
Button(frame_drink, text="콜라").pack()


# --- 스크롤, ----------------------------------------
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set )
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

'''

# --- 그리드, ----------------------------------------
#btn1 = Button(root, text="버튼1")
#btn2 = Button(root, text="버튼2")
# btn1.pack(side="left")
# btn2.pack(side="right")

btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=2, pady=2)

btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=2, pady=2)

btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="sub", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=2, pady=2)

btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="add", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=2, pady=2)

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=2, pady=2)

btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=2, pady=2)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=2, pady=2)

root.mainloop()