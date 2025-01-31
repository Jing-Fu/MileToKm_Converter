import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry01 = tkinter.Entry(width=7)
entry01.grid(row=0, column=1)

label02 = tkinter.Label()
label02.config(text="Miles")
label02.grid(row=0, column=2)

label10 = tkinter.Label()
label10.config(text="is equal to")
label10.grid(row=1, column=0)

label11 = tkinter.Label()
label11.config(text="0")
label11.grid(row=1, column=1)

label10 = tkinter.Label()
label10.config(text="Km")
label10.grid(row=1, column=2)


def calculate():
    try:
        mile = float(entry01.get())  # 取得輸入框的值並轉換成浮點數
        km = 1.609344 * mile
        label11.config(text=f"結果: {km:.2f} 公里")  # 更新結果標籤
    except ValueError:
        label11.config(text="請輸入有效數字")


button21 = tkinter.Button(text="Calculate", command=calculate)
button21.grid(row=2, column=1)
window.mainloop()
