from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Selection Sort")
root.geometry("400x200")
root.config(bg = "lime green")


numbers = [42, 12, 13, 89, 63, 11]
def selection_sort(numbers):
    n = len(numbers)
    for smallest in range(n-1):
        sn = smallest
        
        for i in range(smallest+1, n):
            if numbers[i] < numbers[sn]:
                sn = i
        numbers[smallest], numbers[sn] = numbers[sn], numbers[smallest]
    return numbers

lab1 = Label(root, text = selection_sort(numbers))
lab1.place(x=70, y=60)
lab1.config(bg = "lime green", font = "Arial 24")

root.mainloop()
