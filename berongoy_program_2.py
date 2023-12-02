import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Mainwindow
mainwindow = customtkinter.CTk()
mainwindow.geometry("400x240")
mainwindow.title("Shopee")
mainwindow.resizable(width=False, height=False)

# Images
add_shop_image = customtkinter.CTkImage(Image.open("icon_shop.png"), size=((30, 30)))
add_cancel_image = customtkinter.CTkImage(Image.open("icon_cancelbutton.png"), size=((30, 30)))
banner_image = customtkinter.CTkImage(Image.open("banner.png"), size=(320, 100))
appleimg = customtkinter.CTkImage(Image.open("apples.png"), size=(360, 480))


# Function to open the calculation window
def open_calculate_window():  
    calculate_window = customtkinter.CTkToplevel()
    calculate_window.title("Calculate Window")
    calculate_window.geometry("720x480")
    calculate_window.resizable(width=False, height=False)
    calculate_window.focus_set()                                                        
    calculate_window.grab_set()

    #Calculate window widgets
    label_appleimg = customtkinter.CTkLabel(calculate_window, text="", image=appleimg)
    label_appleimg.pack(expand=True, side="left")

    calculate_frame = customtkinter.CTkFrame(calculate_window, width=360, height=480)
    calculate_frame.pack(expand=True, side="right")

    label_banner_image = customtkinter.CTkLabel(calculate_frame, text="", image=banner_image, corner_radius=100)
    label_banner_image.place(relx=0.5, rely=0.13, anchor=CENTER)

    entry_money = customtkinter.CTkEntry(calculate_frame, placeholder_text="Enter your Money", placeholder_text_color="white"	, corner_radius=10, width=300, height=30)
    entry_money.place(relx=0.5, rely=0.3, anchor=CENTER)

    entry_apple_price = customtkinter.CTkEntry(calculate_frame, placeholder_text="Enter the Price for an apple",placeholder_text_color="white", corner_radius=10, width=300, height=30)
    entry_apple_price.place(relx=0.5, rely=0.4, anchor=CENTER)

    frame_result = customtkinter.CTkFrame(calculate_frame, border_width=2, border_color="black", width=320, height=200)
    frame_result.place(relx=0.5, rely=0.77, anchor=CENTER)

    result_label = customtkinter.CTkLabel(frame_result, text="Result", font=('Helvetica', 26, 'bold'))
    result_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    information_apple_label = customtkinter.CTkLabel(frame_result, text="")
    information_apple_label.place(relx=0.5, rely=0.25, anchor=CENTER)

    number_of_apples_label = customtkinter.CTkLabel(frame_result, text="")
    number_of_apples_label.place(relx=0.5, rely=0.45, anchor=CENTER)

    information_money_label = customtkinter.CTkLabel(frame_result, text="")
    information_money_label.place(relx=0.5, rely=0.65, anchor=CENTER)

    remaining_money_label = customtkinter.CTkLabel(frame_result, text="")
    remaining_money_label.place(relx=0.5, rely=0.85, anchor=CENTER)

    # Function to calculate apples and display results
    def calculate_apples():
        # Check if both entry fields are filled
        if any(not entry for entry in (entry_money.get(),entry_apple_price.get())):
            messagebox.showwarning("Error", "Please fill in all fields.")
            return
        try:
            # Get user inputs
            money = float(entry_money.get())
            apple_price = float(entry_apple_price.get())

            # Check if apple price is not zero
            if apple_price != 0:
                number_apples = money // apple_price
                remaining_money = money % apple_price
            else:
                messagebox.showerror("Error", "Apple price cannot be zero.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")
            return
        
        # Calculate and display results in labels
        information_apple_label.configure(text="The maximum number of apples you can buy:")
        number_of_apples_label.configure(text=(int(number_apples)), font=('Helvetica', 20, 'bold'), text_color="#D21404")
        information_money_label.configure(text="Your remaining money is:")
        remaining_money_label.configure(text=f"₱{remaining_money:.2f}", font=('Helvetica', 20, 'bold'), text_color="#D21404")

    
    calculate_button = customtkinter.CTkButton(calculate_frame, text="Calculate", command=calculate_apples,hover_color="#BE3144", width=300, height=30)
    calculate_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Main window widgets
design_frame = customtkinter.CTkFrame(mainwindow, border_width=2, border_color="black")
design_frame.pack(expand=True, fill="both", padx=10, pady=10)

welcome_label = customtkinter.CTkLabel(mainwindow, text="Welcome to Gerald's Store", font=('Helvetica', 26, 'bold'), bg_color="#2b2b2b")
welcome_label.place(relx=0.5, rely=0.15, anchor=CENTER)

note_label = customtkinter.CTkLabel(mainwindow, text="This app is only for entering the amount of \nmoney and price of an apple.", text_color="#E3242B", font=('Figtree', 16), bg_color="#2b2b2b")
note_label.place(relx=0.5, rely=0.3, anchor=CENTER)

start_button = customtkinter.CTkButton(mainwindow, text="Proceed", font=('Helvetica', 15, 'bold'), image= add_shop_image,  command=open_calculate_window)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

cancel_button = customtkinter.CTkButton(mainwindow, text="Cancel", font=('Helvetica', 15, 'bold'), image= add_cancel_image, command=exit)
cancel_button.place(relx=0.5, rely=0.7, anchor=CENTER)

mainwindow.mainloop()
