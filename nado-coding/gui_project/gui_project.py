import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Python 메모장")
#root.geometry("640x480")

file_frame = Frame(root)
file_frame.pack(fill="x", padx=3, pady=3)

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5,width=12)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5,width=12)
btn_del_file.pack(side="right")

list_frame = Frame(root)
list_frame.pack(fill="both", padx=3, pady=3)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y", padx=3, pady=3)

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=3, pady=3, ipady=3)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=3, pady=3)

#옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack( padx=3, pady=3, ipady=3)

#가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=10)
lbl_width.pack(side="left", padx=3, pady=3)

#가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=3, pady=3)

#간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=3, pady=3)

#간격 옵션 콤보
opt_space = ["없음","좁게", "보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=8)
cmb_space.current(0)
cmb_space.pack(side="left", padx=3, pady=3)

#파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=3, pady=3)

#파일 포맷 옵션 콤보
opt_format = ["PNG","JEPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side="left", padx=3, pady=3)

#진행상황 progress
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=3, pady=3, ipady=3)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=3, pady=3)

#실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=3, pady=3)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=3, pady=3)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=3, pady=3)


root.resizable(False, False)
root.mainloop()