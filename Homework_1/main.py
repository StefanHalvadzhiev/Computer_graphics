import tkinter as tk


def bresenham_dotted_line(x0, y0, x1, y1, visible, invisible, canvas):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    count = 0
    is_visible = True

    while True:
        if is_visible:
            canvas.create_oval(x0 - 1, y0 - 1, x0 + 1, y0 + 1, fill="black")

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

        count += 1
        if is_visible and count >= visible:
            is_visible = False
            count = 0
        elif not is_visible and count >= invisible:
            is_visible = True
            count = 0


class BresenhamApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(
            root,
            width=root.winfo_screenwidth() * 0.95,
            height=root.winfo_screenheight() * 0.8,
            bg="grey"
        )
        self.canvas.pack()

        self.controls = tk.Frame(root)
        self.controls.pack()

        tk.Label(self.controls, text="Visible pixels:").grid(row=0, column=0)
        self.visible_entry = tk.Entry(self.controls, width=5)
        self.visible_entry.grid(row=0, column=1)
        self.visible_entry.insert(0, "5")

        tk.Label(self.controls, text="Invisible pixels:").grid(row=1, column=0)
        self.invisible_entry = tk.Entry(self.controls, width=5)
        self.invisible_entry.grid(row=1, column=1)
        self.invisible_entry.insert(0, "3")

        self.start_button = tk.Button(
            self.controls, text="Start Drawing", command=self.start_drawing
        )
        self.start_button.grid(row=2, column=0, columnspan=2)

        self.reset_button = tk.Button(
            self.controls, text="Reset", command=self.reset_canvas
        )
        self.reset_button.grid(row=3, column=0, columnspan=2)

        self.canvas.bind("<Button-1>", self.on_click)
        self.start_point = None

    def on_click(self, event):
        if self.start_point is None:
            self.start_point = (event.x, event.y)
        else:
            x0, y0 = self.start_point
            x1, y1 = event.x, event.y
            try:
                visible = int(self.visible_entry.get())
                invisible = int(self.invisible_entry.get())
                bresenham_dotted_line(
                    x0, y0, x1, y1, visible, invisible, self.canvas
                )
            except ValueError:
                print(
                    "Please enter valid numbers for visible and invisible pixels."
                )
            self.start_point = None

    def start_drawing(self):
        self.start_point = None
        print("Click on the canvas to draw lines.")

    def reset_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bresenham Dotted Line Drawer")
    app = BresenhamApp(root)
    root.mainloop()
