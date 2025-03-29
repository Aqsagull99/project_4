import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(event):
    """Erase objects in contact with the eraser"""
    # Get mouse position
    mouse_x, mouse_y = event.x, event.y
    
    # Calculate eraser position
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find overlapping objects
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # Change overlapping objects' color to white
    for obj in overlapping_objects:
        canvas.itemconfig(obj, fill="white")

# Main function
root = tk.Tk()
root.title("Eraser Grid")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Draw grid
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Create eraser (pink square)
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")

# Bind mouse movement to erase function
canvas.bind("<Motion>", erase_objects)

root.mainloop()



