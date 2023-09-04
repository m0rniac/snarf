"""
MIT License

Copyright (c) [2023] [@m0rniac]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import asyncio
import requests
import tkinter as tk
from rspeechpy import Engine as SNARF
from tkinter import ttk, filedialog, messagebox, Menu

# Version
version = '0.0.2'
os.system('cls' if os.name == 'nt' else 'clear')    # Clean console screen

# Initialize SNARF speech engine
speech = SNARF()

# Function to handle the 'Convert' button click event
async def convert_clicked():
    # Check Internet connection before performing conversion
    if check_internet_connection():
        selected_item = combo.current()
        rate_value = int(rate_scale.get())
        pitch_value = int(pitch_scale.get())
        volume_value = int(volume_scale.get())
        user_input = text_input.get("1.0", "end-1c")

        await build_and_synthesize(selected_item, rate_value, pitch_value, volume_value, user_input)
        
        print("Selected Voice:", selected_item)
        print("Rate Value:", rate_value)
        print("Pitch Value:", pitch_value)
        print("Volume Value:", volume_value)
        print("User Input:", user_input)
    else:
        # Show error message if there is no Internet connection
        messagebox.showerror("Error", "The program cannot function without an Internet connection")

# Function to list friendly names of voices
async def list_friendly_names():
    names = await speech.giveVoicesList()
    friendly_names = [name['FriendlyName'] for name in names]
    return friendly_names

# Function to list short names of voices
async def list_short_names():
    names = await speech.giveVoicesList()
    short_names = [name['ShortName'] for name in names]
    return short_names

# Function to check Internet connection
def check_internet_connection():
    try:
        requests.get("https://bulssola.vercel.app/", timeout=4)
        return True
    except requests.ConnectionError:
        return False

# Function to set the initial combo value
async def set_initial_combo_value():
    friendly_names = await list_friendly_names()
    combo['values'] = friendly_names
    combo.set(friendly_names[0])

# Function to build and synthesize audio
async def build_and_synthesize(selected_item, rate_value, pitch_value, volume_value, user_input):
    voice_name = await list_short_names()
    voice_name = voice_name[selected_item]

    file_path = choose_file_location()

    if file_path:
        await configure_speech_settings(voice_name, rate_value, pitch_value, volume_value)

        try:
            await speech.synthesize(user_input.strip(), file_path)
            messagebox.showinfo("Success", "Audio synthesized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def choose_file_location():
    file_path = filedialog.asksaveasfilename(
        title='Save Audio',
        initialdir='./Audios',
        defaultextension=".mp3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    return file_path

async def configure_speech_settings(voice_name, rate_value, pitch_value, volume_value):
    await speech.setVoice(voice_name)
    await speech.setRate(rate_value)
    await speech.setPitch(pitch_value)
    await speech.setVolume(volume_value)

# Create the main window
root = tk.Tk()
root.title('SNARF | ' + version)
root.geometry('1024x640')
root.resizable(0, 0)
root.iconbitmap('./snarfy/logo.ico')

# Create the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0)

# Instructional label for the text input box
text_label_instructive = ttk.Label(main_frame, text="You can write here:")
text_label_instructive.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Text Input Box
text_input = tk.Text(main_frame, height=15, width=60)
text_input.insert("1.0", "Hey! You can write here")
text_input.grid(row=1, column=0, padx=10, pady=10, sticky='w')

# Create a frame for the elements on the left
left_frame = ttk.Frame(main_frame)
left_frame.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky='e')

# Main Label
combo_label = ttk.Label(left_frame, text="Select a voice:")
combo_label.grid(row=1, column=0, padx=10, pady=10)
combo = ttk.Combobox(left_frame, state="readonly", width=45)
combo.grid(row=1, column=1, padx=10, pady=10)

# Get the list of friendly names and set the first element as default
asyncio.run(set_initial_combo_value())

# Barra de escala 'Rate'
rate_label = ttk.Label(left_frame, text="Rate:")
rate_label.grid(row=2, column=0, padx=10, pady=10)
rate_scale = ttk.Scale(left_frame, from_=1, to=20, orient="horizontal", length=300)
rate_scale.grid(row=2, column=1, padx=10, pady=10)

# Barra de escala 'Pitch'
pitch_label = ttk.Label(left_frame, text="Pitch:")
pitch_label.grid(row=3, column=0, padx=10, pady=10)
pitch_scale = ttk.Scale(left_frame, from_=1, to=20, orient="horizontal", length=300)
pitch_scale.grid(row=3, column=1, padx=10, pady=10)

# Barra de escala 'Volume'
volume_label = ttk.Label(left_frame, text="Volume:")
volume_label.grid(row=4, column=0, padx=10, pady=10)
volume_scale = ttk.Scale(left_frame, from_=1, to=10, orient="horizontal", length=300)
volume_scale.grid(row=4, column=1, padx=10, pady=10)

# Botón 'Convert'
convert_button = ttk.Button(left_frame, text="Convert to Audio", command=lambda: asyncio.run(convert_clicked()), width=30)
convert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Etiqueta para mostrar el estado de la conexión a Internet
internet_label = ttk.Label(root, text="Internet Connection Status: Unknown", font=("Arial", 14))
internet_label.place(x=10, y=590)

# Function to open the author's website
def open_author_website():
    import webbrowser
    webbrowser.open("https://bulssola.vercel.app/")
    
# Verificar y actualizar el estado de la conexión a Internet
def update_internet_status():
    if check_internet_connection():
        internet_label.config(text="Internet Connection Status: Connected", foreground="green")
    else:
        internet_label.config(text="Internet Connection Status: Disconnected", foreground="red")
    root.after(5000, update_internet_status)

update_internet_status()

# Create a MENU
options_menu = Menu(root)
root.config(menu=options_menu)

# Menu option
options_menu.add_command(label="Author", command=open_author_website)

# Start the GUI
root.mainloop()
