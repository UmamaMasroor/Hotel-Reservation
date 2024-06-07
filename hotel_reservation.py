import tkinter as tk
from tkinter import ttk, messagebox

class HotelReservation:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation Form")
        self.reservations = []
        self.load_reservations()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Room Information
        room_info_frame = tk.LabelFrame(frame, text="Room Information")
        room_info_frame.grid(row=0, column=0, padx=10, pady=5)

        tk.Label(room_info_frame, text="Room Type:").grid(row=0, column=0, sticky=tk.W)
        self.room_type = tk.StringVar()
        room_options = ["Single Room", "Double Room", "Deluxe Room", "Suite", "Family Room", "Executive Room", "Luxury Room"]
        self.room_menu = ttk.Combobox(room_info_frame, textvariable=self.room_type, values=room_options)
        self.room_menu.grid(row=0, column=1)

        tk.Label(room_info_frame, text="Number of Beds:").grid(row=1, column=0, sticky=tk.W)
        self.num_beds = tk.IntVar(value=1)
        self.beds_spinbox = tk.Spinbox(room_info_frame, from_=1, to_=10, textvariable=self.num_beds, command=self.update_cost)
        self.beds_spinbox.grid(row=1, column=1)

        # Services
        services_frame = tk.LabelFrame(frame, text="Services")
        services_frame.grid(row=1, column=0, padx=10, pady=5)
        self.services_vars = {
            'Room Service': tk.BooleanVar(),
            'Laundry Service': tk.BooleanVar(),
            'Tour Booking': tk.BooleanVar(),
            'Airport Transfer': tk.BooleanVar(),
            'Concierge Service': tk.BooleanVar(),
            'Spa Service': tk.BooleanVar(),
            'Gym Access': tk.BooleanVar(),
            'Babysitting Service': tk.BooleanVar()
        }
        for idx, (service, var) in enumerate(self.services_vars.items()):
            tk.Checkbutton(services_frame, text=service, variable=var, command=self.update_cost).grid(row=idx//2, column=idx%2, sticky=tk.W)

        # Facilities
        facilities_frame = tk.LabelFrame(frame, text="Facilities")
        facilities_frame.grid(row=2, column=0, padx=10, pady=5)
        self.facilities_vars = {
            'WiFi': tk.BooleanVar(),
            'Swimming Pool': tk.BooleanVar(),
            'Food': tk.BooleanVar(),
            'Parking': tk.BooleanVar(),
            'Bar': tk.BooleanVar(),
            'Conference Room': tk.BooleanVar()
        }
        for idx, (facility, var) in enumerate(self.facilities_vars.items()):
            tk.Checkbutton(facilities_frame, text=facility, variable=var, command=self.update_cost).grid(row=idx//2, column=idx%2, sticky=tk.W)

        # Payment Method
        tk.Label(frame, text="Payment Method:").grid(row=3, column=0, sticky=tk.W)
        self.payment_method = tk.StringVar()
        payment_options = ["Credit Card", "Debit Card", "Cash", "Online Payment", "Bank Transfer"]
        self.payment_menu = ttk.Combobox(frame, textvariable=self.payment_method, values=payment_options)
        self.payment_menu.grid(row=3, column=1)

        # Check-in and Check-out Dates
        tk.Label(frame, text="Check-in Date:").grid(row=4, column=0, sticky=tk.W)
        self.checkin_date = tk.Entry(frame)
        self.checkin_date.grid(row=4, column=1)

        tk.Label(frame, text="Check-out Date:").grid(row=5, column=0, sticky=tk.W)
        self.checkout_date = tk.Entry(frame)
        self.checkout_date.grid(row=5, column=1)

        # Total Cost
        tk.Label(frame, text="Total Cost:").grid(row=6, column=0, sticky=tk.W)
        self.total_cost_var = tk.StringVar(value="0.0")
        tk.Label(frame, textvariable=self.total_cost_var).grid(row=6, column=1, sticky=tk.W)

        # Buttons
        buttons_frame = tk.Frame(frame)
        buttons_frame.grid(row=7, column=0, pady=10)

        self.add_button = tk.Button(buttons_frame, text="Add Reservation", command=self.add_reservation)
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(buttons_frame, text="Update Reservation", command=self.update_reservation)
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(buttons_frame, text="Delete Reservation", command=self.delete_reservation)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.view_button = tk.Button(buttons_frame, text="View Reservations", command=self.view_reservations)
        self.view_button.grid(row=0, column=3, padx=5)

    def update_cost(self):
        room_cost = {
            "Single Room": 50, "Double Room": 75, "Deluxe Room": 100, 
            "Suite": 150, "Family Room": 200, "Executive Room": 250, 
            "Luxury Room": 300
        }
        service_cost = {
            'Room Service': 20, 'Laundry Service': 10, 'Tour Booking': 50,
            'Airport Transfer': 30, 'Concierge Service': 25, 'Spa Service': 100,
            'Gym Access': 15, 'Babysitting Service': 40
        }
        facility_cost = {
            'WiFi': 10, 'Swimming Pool': 15, 'Food': 50, 'Parking': 5, 
            'Bar': 20, 'Conference Room': 100
        }

        cost = room_cost.get(self.room_type.get(), 0) + (self.num_beds.get() - 1) * 10
        for service, var in self.services_vars.items():
            if var.get():
                cost += service_cost[service]
        for facility, var in self.facilities_vars.items():
            if var.get():
                cost += facility_cost[facility]

        self.total_cost_var.set(f"${cost:.2f}")

    def add_reservation(self):
        reservation = {
            "Room Type": self.room_type.get(),
            "Number of Beds": self.num_beds.get(),
            "Services": [service for service, var in self.services_vars.items() if var.get()],
            "Facilities": [facility for facility, var in self.facilities_vars.items() if var.get()],
            "Payment Method": self.payment_method.get(),
            "Check-in Date": self.checkin_date.get(),
            "Check-out Date": self.checkout_date.get(),
            "Total Cost": self.total_cost_var.get()
        }
        self.reservations.append(reservation)
        self.save_reservations()
        messagebox.showinfo("Success", "Reservation added successfully!")

    def view_reservations(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Reservations")
        text = tk.Text(view_window)
        text.pack(expand=True, fill=tk.BOTH)

        for idx, reservation in enumerate(self.reservations, start=1):
            text.insert(tk.END, f"Reservation {idx}\n")
            for key, value in reservation.items():
                if isinstance(value, list):
                    value = ", ".join(value)
                text.insert(tk.END, f"{key}: {value}\n")
            text.insert(tk.END, "-"*30 + "\n")

    def update_reservation(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Reservation")
        
        tk.Label(update_window, text="Enter Reservation Number to update:").grid(row=0, column=0)
        reservation_number_entry = tk.Entry(update_window)
        reservation_number_entry.grid(row=0, column=1)
        
        def submit_update():
            idx = int(reservation_number_entry.get()) - 1
            if 0 <= idx < len(self.reservations):
                self.reservations[idx] = {
                    "Room Type": self.room_type.get(),
                    "Number of Beds": self.num_beds.get(),
                    "Services": [service for service, var in self.services_vars.items() if var.get()],
                    "Facilities": [facility for facility, var in self.facilities_vars.items() if var.get()],
                    "Payment Method": self.payment_method.get(),
                    "Check-in Date": self.checkin_date.get(),
                    "Check-out Date": self.checkout_date.get(),
                    "Total Cost": self.total_cost_var.get()
                }
                self.save_reservations()
                messagebox.showinfo("Success", "Reservation updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid reservation number!")
        
        tk.Button(update_window, text="Submit", command=submit_update).grid(row=1, columnspan=2)

    def delete_reservation(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Reservation")

        tk.Label(delete_window, text="Enter Reservation Number to delete:").grid(row=0, column=0)
        reservation_number_entry = tk.Entry(delete_window)
        reservation_number_entry.grid(row=0, column=1)

        def submit_delete():
            idx = int(reservation_number_entry.get()) - 1
            if 0 <= idx < len(self.reservations):
                self.reservations.pop(idx)
                self.save_reservations()
                messagebox.showinfo("Success", "Reservation deleted successfully!")
                delete_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid reservation number!")
        
        tk.Button(delete_window, text="Submit", command=submit_delete).grid(row=1, columnspan=2)

    def save_reservations(self):
        with open('reservations.txt', 'w') as file:
            for reservation in self.reservations:
                for key, value in reservation.items():
                    if isinstance(value, list):
                        value = ", ".join(value)
                    file.write(f"{key}: {value}\n")
                file.write("\n")

    def load_reservations(self):
        try:
            with open('reservations.txt', 'r') as file:
                reservation = {}
                for line in file:
                    line = line.strip()
                    if line:
                        if ": " in line:
                            key, value = line.split(': ', 1)
                            if key in ["Services", "Facilities"]:
                                value = value.split(', ')
                            elif key == "Number of Beds":
                                value = int(value)
                            reservation[key] = value
                    else:
                        if reservation:
                            self.reservations.append(reservation)
                            reservation = {}
                if reservation:  # Ensure the last reservation is added
                    self.reservations.append(reservation)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelReservation(root)
    root.mainloop()
