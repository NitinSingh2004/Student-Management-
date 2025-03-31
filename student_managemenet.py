import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

# Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nitin",
        database="student_info"
    )

# Insert Student Data
def insert_student():
    name, age, gender, course = name_var.get(), age_var.get(), gender_var.get(), course_var.get()
    if name and age and gender and course:
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO students_rec(name, age, gender, course) VALUES (%s, %s, %s, %s)", 
                        (name, age, gender, course))
            conn.commit()
            conn.close()
            clear_fields()
            messagebox.showinfo("Success", "Student Added Successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Delete Student Data
def delete_student():
    selected_item = student_list.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a student to delete")
        return

    student_id = student_list.item(selected_item)['values'][0]
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM students_rec WHERE id=%s", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student Deleted Successfully!")
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))

# Update Student Data
def update_student():
    selected_item = student_list.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a student to update")
        return

    student_id = student_list.item(selected_item)['values'][0]
    name, age, gender, course = name_var.get(), age_var.get(), gender_var.get(), course_var.get()

    if name and age and gender and course:
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("UPDATE students_rec SET name=%s, age=%s, gender=%s, course=%s WHERE id=%s", 
                        (name, age, gender, course, student_id))
            conn.commit()
            conn.close()
            clear_fields()
            messagebox.showinfo("Success", "Student Updated Successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Select Data from Treeview
def on_select(event):
    selected_item = student_list.selection()
    if selected_item:
        values = student_list.item(selected_item)['values']
        name_var.set(values[1])
        age_var.set(values[2])
        gender_var.set(values[3])
        course_var.set(values[4])

# Clear Fields
def clear_fields():
    name_var.set("")
    age_var.set(0)
    gender_var.set("")
    course_var.set("")

# GUI Setup
root = Tk()
root.title("Student Management System")
root.geometry("800x500")
root.configure(bg="#e3f2fd")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#e3f2fd")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

name_var, age_var, gender_var, course_var = StringVar(), IntVar(), StringVar(), StringVar()

frame = Frame(root, bg="#ffffff", padx=15, pady=15, relief=RIDGE, borderwidth=2)
frame.pack(pady=20, padx=20, fill=X)

Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
Entry(frame, textvariable=name_var, font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
Entry(frame, textvariable=age_var, font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Gender:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
Entry(frame, textvariable=gender_var, font=("Arial", 12)).grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="Course:").grid(row=3, column=0, padx=5, pady=5, sticky=W)
Entry(frame, textvariable=course_var, font=("Arial", 12)).grid(row=3, column=1, padx=5, pady=5)

Button(frame, text="Add", command=insert_student, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=10).grid(row=4, column=0, pady=10)
Button(frame, text="Update", command=update_student, bg="#FFC107", font=("Arial", 12, "bold"), width=10).grid(row=4, column=1)
Button(frame, text="Delete", command=delete_student, bg="#F44336", fg="white", font=("Arial", 12, "bold"), width=10).grid(row=4, column=2)
Button(frame, text="Clear", command=clear_fields, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=10).grid(row=4, column=3)

student_list = ttk.Treeview(root, columns=("ID", "Name", "Age", "Gender", "Course"), show='headings', height=10)
student_list.heading("ID", text="ID")
student_list.heading("Name", text="Name")
student_list.heading("Age", text="Age")
student_list.heading("Gender", text="Gender")
student_list.heading("Course", text="Course")
student_list.pack(fill=BOTH, expand=1, padx=20, pady=10)
student_list.bind("<ButtonRelease-1>", on_select)

root.mainloop()
