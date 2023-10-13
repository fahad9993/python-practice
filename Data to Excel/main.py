import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import openpyxl
from data import country_data  # Import country_data from data.py


def save_to_excel():
    name = name_entry.get()
    # Extract the selected country code from the Combobox
    selected_country = country_code_combobox.get()
    selected_country_code = selected_country.split()[-1]
    email = email_entry.get()
    message = message_text.get("1.0", "end-1c")  # Get message from Text widget

    # Extract the country code from the selected entry
    country_code = next((item["code"] for item in country_data if item["code"] == selected_country_code), None)

    if not country_code:
        messagebox.showerror("Error", "Invalid country selection.")
        return

    # Ensure mobile number is a valid numeric string
    mobile = mobile_entry.get()
    if not mobile.isdigit():
        messagebox.showerror("Error", "Mobile number must be a numeric string.")
        return

    # Combine country code and mobile number
    full_mobile = f"+{country_code} {mobile}"

    # Specify the file path on the D drive
    file_path = r"D:\DataFromPython.xlsx"

    # Open the Excel file (create a new one if it doesn't exist)
    try:
        wb = openpyxl.load_workbook(file_path)
    except FileNotFoundError:
        wb = openpyxl.Workbook()

    # Select the active sheet (you can change the sheet name)
    sheet = wb.active

    # Append data to the sheet
    sheet.append([name, full_mobile, email, message])

    # Save the workbook
    wb.save(file_path)

    # Clear the input fields
    name_entry.delete(0, "end")
    mobile_entry.delete(0, "end")
    email_entry.delete(0, "end")
    message_text.delete("1.0", "end")

    messagebox.showinfo("Success", "Data saved to Excel file.")


# Create the main window with padding
root = tk.Tk()
root.title("User Information Form")

# Add padding to the window
root.geometry("400x400")  # Adjust the window size as needed
root.configure(padx=20, pady=20)

# Create labels and entry fields with left alignment and padding
tk.Label(root, text="Name:", anchor="w").pack(fill="both", padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(fill="both", padx=10, pady=5)

tk.Label(root, text="Country:", anchor="w").pack(fill="both", padx=10, pady=5)
country_code_combobox = ttk.Combobox(root, values=[f"{item['flag']} {item['name']} ({item['code']})" for item in
                                                   country_data])
country_code_combobox.pack(fill="both", padx=10, pady=5)
country_code_combobox.set(f"{country_data[0]['flag']} {country_data[0]['name']} ({country_data[0]['code']})")

tk.Label(root, text="Mobile Number:", anchor="w").pack(fill="both", padx=10, pady=5)
mobile_entry = tk.Entry(root)
mobile_entry.pack(fill="both", padx=10, pady=5)

tk.Label(root, text="Email:", anchor="w").pack(fill="both", padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.pack(fill="both", padx=10, pady=5)

tk.Label(root, text="Message:", anchor="w").pack(fill="both", padx=10, pady=5)
message_text = tk.Text(root, height=4, width=40)
message_text.pack(fill="both", padx=10, pady=5)

# Create a button to save data
save_button = tk.Button(root, text="Save to Excel", command=save_to_excel)
save_button.pack(fill="both", padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
