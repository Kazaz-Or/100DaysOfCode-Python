from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

SOURCE_DIRECTORY = "../Users/kazi/Pictures"
TARGET_DIRECTORY = "../Users/kazi/Pictures/Watermarked Photos"


def open_file():
    browse_text.set("Loading...")
    photo_name = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File", filetype=
    (("jpeg files", "*.jpg"), ("all files", "*.*")))
    if photo_name:
        image = Image.open(photo_name).convert("RGBA")
        wm_image = Image.open("images/Watermark 2.png").convert("RGBA")

        wm_resized = wm_image.resize((round(image.size[0] * .35), round(image.size[1] * .35)))
        wm_mask = wm_resized.convert("RGBA")

        position = (image.size[0] - wm_resized.size[0], image.size[1] - wm_resized.size[1])

        transparent = Image.new('RGBA', image.size, (0, 0, 0, 0))
        transparent.paste(image, (0, 0))
        transparent.paste(wm_mask, position, mask=wm_mask)
        transparent.show()

        finished_img = transparent.convert("RGB")
        finished_img_name = photo_name[:-4] + " WM.jpg"
        finished_img.save(finished_img_name)

        success_text.set(f"Success!  File saved to {finished_img_name}.")

        browse_text.set("Browse")


def quit():
    root.destroy()


root = tk.Tk()
root.title("Photo Watermark App")

canvas = tk.Canvas(root, width=600, height=500)
canvas.grid(columnspan=5, rowspan=4)

logo = Image.open("images/logo.png")
logo = logo.resize((200, 200))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=3, row=0)

instruction_label = tk.Label(root, text="Select photo to watermark.", font="Ariel")
instruction_label.grid(columnspan=5, column=0, row=1)

browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=open_file, textvariable=browse_text, font="Ariel", bg="#20bebe", fg="white",
                       height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2)

success_text = tk.StringVar()
success_text.set(" ")
success_label = tk.Label(root, textvariable=success_text)
success_label.grid(columnspan=5, column=0, row=3)

cancel_btn = tk.Button(root, text="Quit", command=quit, font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
cancel_btn.grid(column=4, row=2, padx=10)

root.mainloop()
