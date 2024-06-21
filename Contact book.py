import tkinter as tk
from tkinter import messagebox

class PhonebookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Phonebook App")

        self.contacts = {}

        self.main_frame = tk.Frame(master, padx=20, pady=10)
        self.main_frame.pack()

        self.name_label = tk.Label(self.main_frame, text="Name:", font=("Helvetica", 12))
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.main_frame, font=("Helvetica", 12))
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(self.main_frame, text="Phone:", font=("Helvetica", 12))
        self.phone_label.grid(row=1, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self.main_frame, font=("Helvetica", 12))
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.main_frame, text="Add Contact", command=self.add_contact, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_button.grid(row=2, columnspan=2, pady=5)

        self.search_button = tk.Button(self.main_frame, text="Search Contact", command=self.search_contact, font=("Helvetica", 12), bg="#008CBA", fg="white")
        self.search_button.grid(row=3, columnspan=2, pady=5)

        self.update_button = tk.Button(self.main_frame, text="Update Contact", command=self.update_contact, font=("Helvetica", 12), bg="#f44336", fg="white")
        self.update_button.grid(row=4, columnspan=2, pady=5)

        self.delete_button = tk.Button(self.main_frame, text="Delete Contact", command=self.delete_contact, font=("Helvetica", 12), bg="#ff9800", fg="white")
        self.delete_button.grid(row=5, columnspan=2, pady=5)

        self.view_button = tk.Button(self.main_frame, text="View Contacts", command=self.view_contacts, font=("Helvetica", 12), bg="#555555", fg="white")
        self.view_button.grid(row=6, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            if name not in self.contacts:
                self.contacts[name] = phone
                messagebox.showinfo("Success", "Contact added successfully!")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Contact already exists.")
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {self.contacts[name]}")
        else:
            messagebox.showerror("Contact Not Found", f"No contact found with name '{name}'.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"No contact found with name '{name}'.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"No contact found with name '{name}'.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

def main():
    root = tk.Tk()
    app = PhonebookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
