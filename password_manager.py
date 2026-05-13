
import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- PASSWORD STORAGE ---------------- #
passwords = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass


# ---------------- FUNCTIONS ---------------- #
def save_password():
    site = website_entry.get()
    pwd = password_entry.get()

    if site == "" or pwd == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    passwords[site] = pwd
    update_file()

    messagebox.showinfo("Success", "Password Saved!")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def update_file():
    with open("passwords.txt", "w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site}:{pwd}\n")


# ---------------- VIEW PASSWORDS ---------------- #
def view_passwords():
    output_box.delete("1.0", tk.END)

    if not passwords:
        output_box.insert(tk.END, "No passwords saved.\n")
    else:
        output_box.insert(tk.END, "Saved Passwords:\n\n")

        for site, pwd in passwords.items():
            output_box.insert(tk.END, f"🌐 {site}  ➜  🔑 {pwd}\n")


# ---------------- GENERATE PASSWORD ---------------- #
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    pwd = "".join(random.choice(chars) for _ in range(10))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)

    messagebox.showinfo("Generated", f"Password: {pwd}")


# ---------------- DELETE PASSWORD ---------------- #
def delete_password():
    site = website_entry.get()

    if site == "":
        messagebox.showwarning("Warning", "Enter website name!")
        return

    if site in passwords:
        del passwords[site]
        update_file()

        messagebox.showinfo("Deleted", f"Password for '{site}' deleted.")

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

        view_passwords()

    else:
        messagebox.showerror("Error", "Website not found!")


# ---------------- SEARCH PASSWORD ---------------- #
def search_password():
    site = website_entry.get()

    output_box.delete("1.0", tk.END)

    if site == "":
        messagebox.showwarning("Warning", "Enter website name to search!")
        return

    if site in passwords:
        output_box.insert(
            tk.END,
            f"🔍 Search Result\n\n🌐 Website: {site}\n🔑 Password: {passwords[site]}"
        )
    else:
        output_box.insert(tk.END, "❌ No password found for this website.")


# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Personal Password Manager")
root.geometry("750x600")
root.config(bg="#0f172a")
root.resizable(False, False)


# ---------------- HEADING ---------------- #
title = tk.Label(
    root,
    text="🔐 PERSONAL PASSWORD MANAGER",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=20)


# ---------------- INPUT FRAME ---------------- #
frame = tk.Frame(root, bg="#1e293b", padx=25, pady=25)
frame.pack(pady=10)


# Website Label
website_label = tk.Label(
    frame,
    text="Website",
    font=("Arial", 13, "bold"),
    bg="#1e293b",
    fg="white"
)
website_label.grid(row=0, column=0, pady=12, sticky="w")


# Website Entry
website_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 12),
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat"
)
website_entry.grid(row=0, column=1, pady=12, padx=10)


# Password Label
password_label = tk.Label(
    frame,
    text="Password",
    font=("Arial", 13, "bold"),
    bg="#1e293b",
    fg="white"
)
password_label.grid(row=1, column=0, pady=12, sticky="w")


# Password Entry
password_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 12),
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat"
)
password_entry.grid(row=1, column=1, pady=12, padx=10)


# ---------------- BUTTON FRAME ---------------- #
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=25)


# Save Button
save_btn = tk.Button(
    button_frame,
    text="💾 Save",
    command=save_password,
    font=("Arial", 11, "bold"),
    bg="#22c55e",
    fg="white",
    padx=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
save_btn.grid(row=0, column=0, padx=10, pady=10)


# View Button
view_btn = tk.Button(
    button_frame,
    text="📂 View",
    command=view_passwords,
    font=("Arial", 11, "bold"),
    bg="#3b82f6",
    fg="white",
    padx=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
view_btn.grid(row=0, column=1, padx=10, pady=10)


# Generate Button
generate_btn = tk.Button(
    button_frame,
    text="⚡ Generate",
    command=generate_password,
    font=("Arial", 11, "bold"),
    bg="#f59e0b",
    fg="white",
    padx=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
generate_btn.grid(row=0, column=2, padx=10, pady=10)


# Search Button
search_btn = tk.Button(
    button_frame,
    text="🔍 Search",
    command=search_password,
    font=("Arial", 11, "bold"),
    bg="#8b5cf6",
    fg="white",
    padx=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
search_btn.grid(row=1, column=0, padx=10, pady=10)


# Delete Button
delete_btn = tk.Button(
    button_frame,
    text="🗑 Delete",
    command=delete_password,
    font=("Arial", 11, "bold"),
    bg="#ef4444",
    fg="white",
    padx=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
delete_btn.grid(row=1, column=1, padx=10, pady=10)


# Exit Button
exit_btn = tk.Button(
    button_frame,
    text="❌ Exit",
    command=root.destroy,
    font=("Arial", 11, "bold"),
    bg="#64748b",
    fg="white",
    padx=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
exit_btn.grid(row=1, column=2, padx=10, pady=10)


# ---------------- OUTPUT BOX ---------------- #
output_box = tk.Text(
    root,
    height=14,
    width=75,
    font=("Consolas", 11),
    bg="#1e293b",
    fg="#f8fafc",
    relief="flat",
    padx=15,
    pady=15
)
output_box.pack(pady=20)


# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Made with Python Tkinter ❤️",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=10)


# ---------------- RUN APP ---------------- #
root.mainloop()