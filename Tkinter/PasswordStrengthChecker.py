from tkinter import *

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

lbl = Label(root, text="Enter a password to evaluate its strength", fg="white", bg="#072f5f", height=1, width=100)
lbl.pack()

pass_lbl = Label(root, text="Password:", bg="#3895d3", width=40)
pass_lbl.pack(pady=10)

pass_entry = Entry(root, width=30,)
pass_entry.pack(pady=10)

text_box = Text(root, height=6, width=45)
text_box.pack(pady=10)


def display():
    pa = pass_entry.get()
    text_box.delete("1.0", END)
    text_box.config(bg='white')
    if pa.strip():
        length = len(pa)
        has_lower = any(c.islower() for c in pa)
        has_upper = any(c.isupper() for c in pa)
        has_digit = any(c.isdigit() for c in pa)
        has_symbol = any(not c.isalnum() for c in pa)

        # length points: 0..3
        length_points = 0
        if length >= 8:
            length_points = 1
        if length >= 12:
            length_points = 2
        if length >= 16:
            length_points = 3

        mix_points = 1 if (has_lower and has_upper) else 0
        digit_points = 1 if has_digit else 0
        symbol_points = 1 if has_symbol else 0

        raw_score = length_points + mix_points + digit_points + symbol_points

        # common weak passwords check
        common_passwords = {"password", "123456", "12345678", "qwerty", "abc123", "letmein"}
        if pa.lower() in common_passwords:
            raw_score = min(raw_score, 1)
            common_flag = True
        else:
            common_flag = False

        score = min(raw_score, 5)

        names = {1: 'Very Weak', 2: 'Weak', 3: 'Moderate', 4: 'Strong', 5: 'Very Strong'}
        colors = {1: '#ff4d4d', 2: '#ff944d', 3: '#ffd24d', 4: '#9be66a', 5: '#39d353'}

        rating = names.get(score, 'Very Weak')
        color = colors.get(score, 'white')

        parts = [f"Rating: {rating} ({score}/5)", f"Length: {length} (length points: {length_points})"]
        if has_lower and has_upper:
            parts.append("Contains mixed case (+1)")
        else:
            parts.append("Add both lower and UPPER case to increase strength")
        if has_digit:
            parts.append("Contains digits (+1)")
        else:
            parts.append("Add numbers to increase strength")
        if has_symbol:
            parts.append("Contains symbols (+1)")
        else:
            parts.append("Add symbols (e.g. !@#$) to increase strength")
        if common_flag:
            parts.append("Note: This is a commonly used password—avoid it")

        text_box.insert(END, "\n".join(parts))
        text_box.config(bg=color)
    else:
        text_box.insert(END, "Please insert a password.")


btn = Button(root, text="Begin", command=display, bg="#1261a0", fg="white")
btn.pack()

root.mainloop()