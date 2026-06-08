import customtkinter as ctk

ctk.set_appearance_mode("dark")

def calculate_bmi():
    try:
        name = name_entry.get().strip()

        if len(name) < 2:
            result_label.configure(text="Name is too short!")
            return

        if not all(part.isalpha() for part in name.split()):
            result_label.configure(text="Enter a valid name!")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight < 20 or weight > 300:
            result_label.configure(text="Enter a valid weight!")
            return

        if height < 0.5 or height > 2.5:
            result_label.configure(text="Enter a valid height!")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
            suggestion = "Eat a balanced diet and increase calorie intake."
            app.configure(fg_color="#2563EB")

        elif bmi < 25:
            category = "Normal Weight"
            color = "green"
            suggestion = "Maintain your healthy lifestyle."
            app.configure(fg_color="#16A34A")

        elif bmi < 30:
            category = "Overweight"
            color = "orange"
            suggestion = "Exercise regularly and avoid junk food."
            app.configure(fg_color="#EA580C")

        else:
            category = "Obese"
            color = "red"
            suggestion = "Consult a doctor and follow a fitness plan."
            app.configure(fg_color="#DC2626")

        result_label.configure(
    text=f"Your BMI: {bmi:.2f}",
    text_color="white"
)

        category_label.configure(
    text=f"Category: {category}",
    text_color="white"
        )

        suggestion_label.configure(
            text=f"Suggestion: {suggestion}"
        )

    except ValueError:
        result_label.configure(
            text="Please enter valid values!"
        )
def clear_fields():
    name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    weight_entry.delete(0, "end")
    height_entry.delete(0, "end")

    result_label.configure(text="Your BMI: --")
    category_label.configure(text="Category: --")
    suggestion_label.configure(text="Suggestion: --")

    app.configure(fg_color=["gray92", "gray14"])

app = ctk.CTk()
app.geometry("500x600")
app.title("BMI Health Tracker")

title = ctk.CTkLabel(
    app,
    text="BMI HEALTH TRACKER",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)
subtitle = ctk.CTkLabel(
    app,
    text="Calculate your Body Mass Index",
    text_color="gray"
)
subtitle.pack(pady=5)

name_frame = ctk.CTkFrame(app, fg_color="transparent")
name_frame.pack(pady=10)

ctk.CTkLabel(
    name_frame,
    text="Name",
    width=100
).pack(side="left")

name_entry = ctk.CTkEntry(
    name_frame,
    width=250
)
name_entry.pack(side="left")

age_frame = ctk.CTkFrame(app, fg_color="transparent")
age_frame.pack(pady=10)

ctk.CTkLabel(
    age_frame,
    text="Age",
    width=100
).pack(side="left")

age_entry = ctk.CTkEntry(
    age_frame,
    width=250
)
age_entry.pack(side="left")

weight_frame = ctk.CTkFrame(app, fg_color="transparent")
weight_frame.pack(pady=10)

ctk.CTkLabel(
    weight_frame,
    text="Weight (kg)",
    width=100
).pack(side="left")

weight_entry = ctk.CTkEntry(
    weight_frame,
    width=250
)
weight_entry.pack(side="left")

height_frame = ctk.CTkFrame(app, fg_color="transparent")
height_frame.pack(pady=10)

ctk.CTkLabel(
    height_frame,
    text="Height (m)",
    width=100
).pack(side="left")

height_entry = ctk.CTkEntry(
    height_frame,
    width=250
)
height_entry.pack(side="left")

button = ctk.CTkButton(
    app,
    text="Calculate BMI",
    command=calculate_bmi
)
button.pack(pady=20)
clear_button = ctk.CTkButton(
    app,
    text="Clear",
    command=clear_fields
)
clear_button.pack(pady=10)

result_label = ctk.CTkLabel(
    app,
    text="Your BMI: --",
    font=("Arial", 18)
)
result_label.pack(pady=10)

category_label = ctk.CTkLabel(
    app,
    text="Category: --",
    font=("Arial", 18)
)
category_label.pack(pady=10)

suggestion_label = ctk.CTkLabel(
    app,
    text="Suggestion: --",
    wraplength=400,
    font=("Arial", 14)
)
suggestion_label.pack(pady=10)

app.mainloop()
