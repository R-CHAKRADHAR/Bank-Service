
# Importing required module
import customtkinter as ctk

# Selecting GUI theme - dark,
# light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme-blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Modern Login UI using Customtkinter")

app.mainloop()
