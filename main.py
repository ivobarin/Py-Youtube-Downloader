import customtkinter as ctk
from functions import *

# Configurar tema oscuro
ctk.set_appearance_mode('dark')

if __name__ == '__main__':
    root = ctk.CTk()
    root.title("YouTube Downloader")
    
    # Configurar grid principal
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.resizable(False, False)
    
    # Frame principal con padding
    mainframe = ctk.CTkFrame(root, fg_color="#242424")
    mainframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # Configurar grid del frame
    mainframe.grid_columnconfigure((1, 2), weight=1)
    mainframe.grid_rowconfigure(4, weight=1)  # Para empujar el botón hacia abajo
    
    # Etiqueta de título    
    title = ctk.CTkLabel(
        mainframe,
        text="Enter the URL of the video or playlist",
        text_color="white",
        font=("Arial", 14)
    ).grid(row=0, column=1, columnspan=2, pady=10)
    
    # Etiqueta y entrada de URL
    url_label = ctk.CTkLabel(
        mainframe,
        text="URL:  ",
        text_color="white",
        font=("Arial", 14)
    )
    url_label.grid(row=1, column=1, sticky="w", pady=5)
    
    url = ctk.StringVar()
    
    url_entry = ctk.CTkEntry(
        mainframe,
        width=300,
        textvariable=url,
        font=("Arial", 12),
        text_color="white"
    )
    url_entry.grid(row=1, column=2, sticky="ew", pady=5)
    
    # Etiqueta y selector de tipo
    type_label = ctk.CTkLabel(
        mainframe,
        text="Type:",
        text_color="white",
        font=("Arial", 14)
    )
    type_label.grid(row=2, column=1, sticky="w", pady=5)
    
    type_var = ctk.StringVar(value="video")
    
    type_selector = ctk.CTkComboBox(
        mainframe,
        values=["video", "audio"],
        variable=type_var,
        state="readonly"
    )
    
    type_selector.grid(row=2, column=2, sticky="ew", pady=5)
    
    # Botón de descarga con padding
    download_btn = ctk.CTkButton(
        mainframe,
        text="Download",
        command=lambda: download(url.get(), type_var.get()),
        font=("Arial", 12)
    )
    
    # grid del botón
    download_btn.grid(
        row=4, 
        column=1, 
        columnspan=2, 
        sticky="s", 
        pady=20
    )
    
    download_btn.focus()
    root.mainloop()