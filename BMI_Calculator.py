from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(bg='maroon')

window.title("BMI Calculator")
window.geometry("700x500")
header = Label(window, text='IDEAL BODY MASS INDEX CALCULATOR', bg="grey")
header.place(x=250, y=0)

frame = Frame(window, width=500, height=200, borderwidth=1, relief='ridge', bg='beige')

frame.place(relx=0.15, rely=0.1)

weight = Label(frame, text="Weight(kg):" , bg="grey")
weight.place(relx=0, rely=0)
weight_entry = Entry(frame)
weight_entry.place(relx=0.3, rely=0)

height = Label(frame, text="Height(cm):", bg='grey')
height.place(relx=0, rely=0.2)
height_entry = Entry(frame)
height_entry.place(relx=0.3, rely=0.2)

gender = Label(frame, text="Gender:", bg='grey')
gender.place(rely=0.43, relx=0)

age = Label(frame, text="Age:", bg='grey')
age.place(rely=0.7, relx=0)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.7, relx=0.3)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)

category = Entry(window)


def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')

        if result_bmi <= 18.5:
            status_entry.insert(0, 'Underweight')
        elif 18.5 <= result_bmi <= 24.9:
            status_entry.insert(0, 'Normal Weight')
        elif 25 <= result_bmi <= 29.9:
            status_entry.insert(0, 'Overweight')
        elif result_bmi >= 30:
            status_entry.insert(0, 'Obese') 

    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()


calculate = Button(window, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc, fg='blue', borderwidth=5)
calculate.place(rely=0.52, relx=0.2)

status = Label(window, text="BMI Status", bg="grey")
status.place(relx=0.5, rely=0.8)
status_entry = Entry(window)
status_entry.place(relx=0.435, rely=0.9)
bmi = Label(window, text="BMI:", bg='grey')
bmi.place(rely=0.7, relx=0.1)
bmi_field = Entry(window, state='readonly')
bmi_field.place(rely=0.7, relx=0.2)
ideal_bmi = Label(window, text='Ideal BMI:', bg='grey')
ideal_bmi.place(rely=0.7, relx=0.5)
ideal_field = Entry(window, state='readonly')
ideal_field.place(rely=0.7, relx=0.65)


def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])


clear = Button(window, text='Clear', command=delete, borderwidth=5, fg="black")
clear.place(rely=0.85, relx=0.1)
quit = Button(window, text='Exit', command='exit', borderwidth=5, fg="black")
quit.place(rely=0.85, relx=0.83)
window.mainloop()
