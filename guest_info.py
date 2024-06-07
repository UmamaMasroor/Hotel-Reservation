import tkinter as tk
from tkinter import messagebox
import os

class UserDetailForm:
    def __init__(self, root):
        self.root = root
        self.root.title("User Detail Form")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Widgets
        tk.Label(self.root, text="First Name").grid(row=0, column=0, padx=10, pady=10)
        self.first_name = tk.Entry(self.root)
        self.first_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Last Name").grid(row=1, column=0, padx=10, pady=10)
        self.last_name = tk.Entry(self.root)
        self.last_name.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Email").grid(row=2, column=0, padx=10, pady=10)
        self.email = tk.Entry(self.root)
        self.email.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Phone Number").grid(row=3, column=0, padx=10, pady=10)
        self.phone = tk.Entry(self.root)
        self.phone.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Address").grid(row=4, column=0, padx=10, pady=10)
        self.address = tk.Entry(self.root)
        self.address.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Number of Guests").grid(row=5, column=0, padx=10, pady=10)
        self.guests = tk.Entry(self.root)
        self.guests.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.root, text="ID Number").grid(row=6, column=0, padx=10, pady=10)
        self.id_number = tk.Entry(self.root)
        self.id_number.grid(row=6, column=1, padx=10, pady=10)

        # Submit Button
        tk.Button(self.root, text="Submit", command=self.submit).grid(row=7, columnspan=2, pady=10)
        
        # Proceed Button
        tk.Button(self.root, text="Proceed", command=self.proceed).grid(row=8, columnspan=2, pady=10)

    def submit(self):
        # Retrieve user input
        reservation_number = self.get_next_reservation_number()
        user_details = {
            "First Name": self.first_name.get(),
            "Last Name": self.last_name.get(),
            "Email": self.email.get(),
            "Phone": self.phone.get(),
            "Address": self.address.get(),
            "Number of Guests": self.guests.get(),
            "ID Number": self.id_number.get(),
            "Reservation Number": reservation_number
        }

        # Save to text file
        with open('guest_reservation.txt', mode='a') as file:
            for key, value in user_details.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

        # Display success message with reservation number
        messagebox.showinfo("Success", f"User details submitted successfully!\nYour reservation number is {reservation_number}")

        # Clear form fields
        self.clear_fields()

    def proceed(self):
        # Execute the external script
        try:
            os.system('python hotel_reservation.py')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to proceed: {e}")

    def clear_fields(self):
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.guests.delete(0, tk.END)
        self.id_number.delete(0, tk.END)

    def get_next_reservation_number(self):
        try:
            with open('reservation_number.txt', 'r') as file:
                content = file.read().strip()
                if content:
                    reservation_number = int(content)
                else:
                    reservation_number = 0
        except (FileNotFoundError, ValueError):
            reservation_number = 0

        reservation_number += 1

        with open('reservation_number.txt', 'w') as file:
            file.write(str(reservation_number))

        return reservation_number

if __name__ == "__main__":
    root = tk.Tk()
    app = UserDetailForm(root)
    root.mainloop()
