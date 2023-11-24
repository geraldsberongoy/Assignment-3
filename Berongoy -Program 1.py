import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create the main application window
mainwindow = customtkinter.CTk()
mainwindow.geometry("400x240")
mainwindow.title("Main Window")
mainwindow.resizable(width=False, height=False)

frame_container1 = customtkinter.CTkFrame(mainwindow, border_width=2, border_color="black")
frame_container1.pack(expand=True, fill="both", padx=10, pady=10)

#Images
add_shop_image = customtkinter.CTkImage(Image.open("icon_shop.png"), size=((30, 30)))
add_cancel_image = customtkinter.CTkImage(Image.open("icon_cancelbutton.png"), size =((30, 30)))
appleimg = customtkinter.CTkImage(Image.open("icon_apple.png"), size=(200, 200))
orangeimg = customtkinter.CTkImage(Image.open("icon_orange.png"), size=(200, 200))
checkoutimg = customtkinter.CTkImage(Image.open("checkout.png"), size=(30, 30))
receiptimg = customtkinter.CTkImage(Image.open("bg_receipt.png"), size=(400, 500))

# Create StringVars to store the selected payment method
selected_payment_method_var = customtkinter.StringVar(value="COD")

# Function to handle button click for opening the buying window
def button_function():
    mainwindow.destroy()
    customer_window = customtkinter.CTk()
    customer_window.title("Buying Window")
    customer_window.geometry("400x400")

    # Create a frame for layout
    frame_container = customtkinter.CTkFrame(customer_window, border_width=2, border_color="black")
    frame_container.pack(expand=True, fill="both", padx=10, pady=10)

    entry_introduction = customtkinter.CTkLabel(customer_window, text="Customer Registration", font=("Helvetica", 30, 'bold'), bg_color="#2b2b2b")
    entry_introduction.place(relx=0.5, rely=0.1, anchor=CENTER)

    entry_firstname = customtkinter.CTkEntry(customer_window, placeholder_text="Enter your First Name", corner_radius=10, width=300)
    entry_firstname.place(relx=0.5, rely=0.25, anchor=CENTER)

    entry_middle = customtkinter.CTkEntry(customer_window, placeholder_text="Enter your Middle Initial", corner_radius=10, width=300)
    entry_middle.place(relx=0.5, rely=0.35, anchor=CENTER)

    entry_surname = customtkinter.CTkEntry(customer_window, placeholder_text="Enter your Surname", corner_radius=10, width=300)
    entry_surname.place(relx=0.5, rely=0.45, anchor=CENTER)

    entry_address = customtkinter.CTkEntry(customer_window, placeholder_text="Enter your Delivery Address", corner_radius=10, width=300)
    entry_address.place(relx=0.5, rely=0.55, anchor=CENTER)

    label_payment = customtkinter.CTkLabel(customer_window, text="Mode of Payment:", fg_color="#2b2b2b")
    label_payment.place(relx=0.25, rely=0.65, anchor=CENTER)

    optionmenu = customtkinter.CTkOptionMenu(customer_window, variable=selected_payment_method_var, values=["COD", "E-Payment"], fg_color="#242424", bg_color="#2b2b2b", button_color="#343638", corner_radius=20, width=190)
    optionmenu.place(relx=0.65, rely=0.65, anchor=CENTER)

    agreement_var = customtkinter.StringVar(value="Disagree")
    agreement_check = customtkinter.CTkCheckBox(customer_window, text="I agree that all the information I put is correct.", bg_color="#2b2b2b", variable=agreement_var, onvalue="Agree", offvalue="Disagree")
    agreement_check.place(relx=0.5, rely=0.75, anchor=CENTER)

    # Validation function for checking if input contains only letters and spaces
    def is_valid_name(entry_text):
        return all(entry.isalpha() or entry.isspace() or entry == '.' for entry in entry_text)

    def buying_interface():
        first_name = entry_firstname.get()
        middle_name = entry_middle.get()
        surname = entry_surname.get()
        address = entry_address.get()

        # Validate names
        if not all(is_valid_name(entry_text) for entry_text in (first_name, middle_name, surname)):
            messagebox.showwarning("Invalid Name", "Please enter a valid name with letters only.")
            return

        # Check for incomplete information
        if any(not entry.get() for entry in (entry_firstname, entry_middle, entry_surname, entry_address)):
            messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
            return

        if agreement_var.get() == "Disagree":
            messagebox.showwarning("Agreement Not Checked", "Please check the box.")
            return

        customer_window.destroy()

        buying_window = customtkinter.CTk()
        buying_window.title("Buying Window")
        buying_window.geometry("600x600")
        buying_window.resizable(width=False, height=False)

        top_frame = customtkinter.CTkFrame(buying_window, fg_color="transparent", border_width=2)
        top_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        bottom_frame = customtkinter.CTkFrame(buying_window, fg_color="transparent", border_width=2)
        bottom_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        top_frame_left = customtkinter.CTkFrame(master=top_frame, fg_color="#2b2b2b", border_color="black", border_width=2)
        top_frame_left.pack(side="left", fill="both", expand=True, padx=5, pady=10)

        top_frame_right = customtkinter.CTkFrame(master=top_frame, fg_color="#2b2b2b", border_color="black", border_width=2)
        top_frame_right.pack(side="left", fill="both", expand=True, padx=5, pady=10)

        apple_image = customtkinter.CTkLabel(top_frame_left, image=appleimg, text="Apple is P20 per piece", font=('Figtree', 18), compound="bottom", text_color="white")
        apple_image.place(relx=0.5, rely=0.5, anchor=CENTER)

        buttom_frame_left = customtkinter.CTkFrame(bottom_frame, fg_color="#2b2b2b", border_color="black", border_width=2)
        buttom_frame_left.pack(side="left", fill="both", expand=True, padx=5, pady=10)

        buttom_frame_right = customtkinter.CTkFrame(bottom_frame, fg_color="#2b2b2b", border_color="black", border_width=2)
        buttom_frame_right.pack(side="left", fill="both", expand=True, padx=5, pady=10)

        orange_image = customtkinter.CTkLabel(buttom_frame_left, image=orangeimg, text="Orange is P25 per piece", font=('Figtree', 18), compound="bottom", text_color="white")
        orange_image.place(relx=0.5, rely=0.5, anchor=CENTER)

        manyapple_label = customtkinter.CTkLabel(top_frame_right, text="How many would you buy?", font=('Helvetica', 17))
        manyapple_label.place(relx=0.5, rely=0.45, anchor=CENTER)

        quantity_apple = customtkinter.CTkEntry(top_frame_right, placeholder_text="Enter quantity:", corner_radius=10, width=175)
        quantity_apple.place(relx=0.5, rely=0.55, anchor=CENTER)

        manyorange_label = customtkinter.CTkLabel(buttom_frame_right, text="How many would you buy?", font=('Helvetica', 17))
        manyorange_label.place(relx=0.5, rely=0.45, anchor=CENTER)

        quantity_orange = customtkinter.CTkEntry(buttom_frame_right, placeholder_text="Enter quantity:", corner_radius=10, width=175)
        quantity_orange.place(relx=0.5, rely=0.55, anchor=CENTER)

        def is_valid_quantity(entry_quantity):
            return entry_quantity.isdigit()

        def checkout():
            selected_payment_method = selected_payment_method_var.get()
            valid_apple_quantity = quantity_apple.get()
            valid_orange_quantity = quantity_orange.get()

            if any(not entry for entry in (valid_apple_quantity, valid_orange_quantity)):
                messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
                return
        

            if not(is_valid_quantity(valid_apple_quantity) and is_valid_quantity(valid_orange_quantity)):
                messagebox.showwarning("Invalid Input", "Please enter a valid quantity with numbers only.")
                return

            buying_window.destroy()
            receipt_window = customtkinter.CTk()
            receipt_window.title("Receipt Window")
            receipt_window.geometry("520x550")
            receipt_window.configure(fg_color="white")

            apple_price = 20  
            orange_price =25

            total_apple_cost = int(valid_apple_quantity) * apple_price
            total_orange_cost = int(valid_orange_quantity) * orange_price

            total_cost = total_apple_cost + total_orange_cost

            # Display the receipt
            receipt_text = (
                f"Customer Information\n"
                f"Name: \n{first_name} \n{middle_name} \n{surname}\n"
                f"Address: {address}\n\n"
                f"Items Purchased\n"
                f"Apple Quantity: {valid_apple_quantity} (P20 per piece)\n"
                f"Orange Quantity: {valid_orange_quantity} (P25 per piece)\n\n"
                f"Total Apple Cost: {total_apple_cost}\n"
                f"Total Orange Cost: {total_orange_cost}\n"
                f"Payment Method: {selected_payment_method}\n"

                f"Total Cost: {total_cost} PHP"
            )
            if selected_payment_method == "COD":
                receipt_text += "\n\nPlease prepare the amount for \nthe courier upon delivery.\n\n------------THANK YOU------------"
            elif selected_payment_method == "E-Payment":
                receipt_text += "\n\nPlease send the payment to \n09936340096 to process your order.\n\n------------THANK YOU------------"

            receipt_label = customtkinter.CTkLabel(receipt_window, text=receipt_text, image=receiptimg, font=("Helvetica", 14, 'bold'), justify=LEFT, fg_color="transparent", text_color="black")
            receipt_label.pack(padx=5, pady=5, anchor=CENTER, expand=True, fill="both" )

            receipt_window.mainloop()
        

        submit_button = customtkinter.CTkButton(buying_window, text="Checkout", font=('Figtree', 24), image=checkoutimg, compound="left", command=checkout, hover_color="#BE3144", width=590, height=10)
        submit_button.pack(side="top", anchor=CENTER, padx=3, pady=3)

        buying_window.mainloop()

    # Buttons for proceeding or canceling buying
    button_proceed_buying = customtkinter.CTkButton(customer_window, text="Start Buying", font=('Figtree', 18), command=buying_interface, hover_color="#BE3144", width=300)
    button_proceed_buying.place(relx=0.5, rely=0.85, anchor=CENTER)

    customer_window.mainloop()

# Labels and buttons in the main application window
welcome_label = customtkinter.CTkLabel(mainwindow, text="Welcome to Gerald's Store", font=('Figtree', 26, 'bold'), bg_color="#2b2b2b")
welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

note_label = customtkinter.CTkLabel(mainwindow, text="Note: We are only selling Apples and Oranges.", font=('Figtree', 14), bg_color="#2b2b2b")
note_label.place(relx=0.5, rely=0.3, anchor=CENTER)

proceed_button = customtkinter.CTkButton(mainwindow, text="Proceed", font=('Helvetica', 18, 'bold'), image=add_shop_image, command=button_function, bg_color="#2b2b2b", hover_color="#BE3144", compound="left", width=250, height=20)
proceed_button.place(relx=0.5, rely=0.5, anchor=CENTER)

cancel_button = customtkinter.CTkButton(mainwindow, text="Cancel", font=('Helvetica', 18, 'bold'), image=add_cancel_image, command=exit, bg_color="#2b2b2b", hover_color="#F05941", compound="left", width=250, height=20)
cancel_button.place(relx=0.5, rely=0.7, anchor=CENTER)

mainwindow.mainloop()

