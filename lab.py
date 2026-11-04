import random
import tkinter as tk
from PIL import Image, ImageTk

SIZE_X = 1300
SIZE_Y = 740
BORDER = 4

def gen_key():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    start = random.randint(0, len(alphabet) - 2)
    end = random.randint(start + 1, len(alphabet) - 1)


    if start < 10:
        part1 = f'0{start}\n'
    else:
        part1 = f'{start}\n'

    part2 = ''

    if end < 10:
        part3 = f'0{end}\n'
    else:
        part3 = f'{end}\n'

    for _ in range(7):
        part2 += alphabet[random.randint(start, end)]

    part2 += '\n'

    ans = part1 + part2 + part3

    return ans


def render_frames(parent):
    header = tk.Frame(parent, bg="#2f72c2")
    body = tk.Frame(parent, bg="#12132e")

    header.pack(side=tk.TOP, fill=tk.X)
    body.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    render_header(header)
    render_body(body)


def render_header(parent):
    lbl = tk.Label(parent, text="key generator for Hollow Knight",
                bg="#2f72c2", fg="white", pady=10)
    
    lbl.pack(side=tk.TOP)


def render_body(parent):
    key_field = tk.Text(parent, width=20, height=3,
                        bg="#29222c", fg="white", bd=0,
                        highlightthickness=0)
    
    key_field.pack(side=tk.TOP, pady=20, padx=20)
    key_field.insert("1.0", "Нажмите кнопку\nдля генерации")
    key_field.config(state="disabled")


    btn_gen = tk.Button(parent, text="gen",
                        command=lambda: render_key(key_field, gen_key()),
                        bg="#12132e",
                        bd=0,
                        highlightthickness=0,
                        activeforeground="white")
    btn_gen.pack(side=tk.TOP)


def render_key(parent, key):
    parent.config(state="normal")
    parent.delete("1.0", tk.END)
    parent.insert("1.0", key)
    parent.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{SIZE_X}x{SIZE_Y}")
    root.title("Hollow Knight")
    root.resizable(False, False)
    
    canvas = tk.Canvas(root, width=SIZE_X, height=SIZE_Y,
                        highlightthickness=0, bd=0)
    canvas.pack(fill="both", expand=True)

    img = Image.open("bg_pic.jpg").resize((SIZE_X, SIZE_Y), Image.LANCZOS)
    bg = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.image = bg


    ui = tk.Frame(canvas, bg="#12132e")
    canvas.create_window(
        SIZE_X // 2, SIZE_Y // 2 + 40,
        window=ui, anchor="center",
        width=300, height=200
    )

    render_frames(ui)

    root.mainloop()