from tkinter import *
from PIL import ImageTk #jpg 이미지를 불러올때

root = Tk()
root.title("Python GUI")
root.geometry("640x800+100+100") #가로*세로 + x좌표 + y좌표
#root.resizable(True, False) #x(너비), y(높이) 크기 변경 여부

# --- 버튼----------------------------------------
btn1 = Button(root, text = "버튼1")
btn1.pack()
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
txt = Text(root, width=20, height=5)
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

root.mainloop()