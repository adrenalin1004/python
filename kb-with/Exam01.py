# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.simpledialog as sd
import math

class main_window(tk.Frame):
    def __init__(self,parent):
        super(main_window, self).__init__(parent)
        parent.title("Fibonacci")
        parent.minsize(200,100)
        self.label = tk.Label(root, text = 'Fibonocci')#1
        self.label.pack()
        self.buttons = tk.Button(parent, text="Integer Input", fg = "red", command = self.M_askint)
        self.buttons.pack()
    
    def M_fibonacci(self, n):
        if n==0:
            return 0
        
        if n==1:
            return 1
        
        return (self.M_fibonacci(n-2) + self.M_fibonacci(n-1))

    def set(self, st):
        self.label.config(text=st)

    def M_askint(self):
        
      #  txt = tk.Entry() #2
              #txt.pack()
        n = tk.simpledialog.askinteger("Input integer", "Fibonacci in") #2 차일드 창에 정수를 입력받는 코드
        fn = self.M_fibonacci(n) #3 fibonacci 연산한 결과를 가진 함수를 호출
        self.set(fn)

if __name__ == '__main__':
    root = tk.Tk()
    mw = main_window(root)
    mw.mainloop()    #4 툴킷을 실행