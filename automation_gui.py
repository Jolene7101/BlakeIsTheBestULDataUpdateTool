import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyautogui
import pandas as pd
import time
import pygetwindow as gw
import os

def position_window(window_title="The Edge", x=0, y=0, width=1024, height=768):
    """Position and resize the target application window."""
    try:
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            window.moveTo(x, y)
            window.resizeTo(width, height)
            return True
        else:
            messagebox.showerror("Window Error", f"Could not find window with title containing '{window_title}'")
            return False
    except Exception as e:
        messagebox.showerror("Window Error", f"Failed to position window: {str(e)}")
        return False

def browse_excel_file():
    filename = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if filename:
        entry_excel_file.delete(0, tk.END)
        entry_excel_file.insert(0, filename)

def run_automation():
    # --- GATHER INPUTS FROM GUI ---
    try:
        config = {
            "SHORT_DELAY": float(entry_short_delay.get()),
            "MEDIUM_DELAY": float(entry_medium_delay.get()),
            "LONG_DELAY": float(entry_long_delay.get()),
            "DATABASE_BUTTON_X": int(entry_database_button_x.get()),
            "DATABASE_BUTTON_Y": int(entry_database_button_y.get()),
            "FIRE_TESTS_X": int(entry_fire_tests_x.get()),
            "FIRE_TESTS_Y": int(entry_fire_tests_y.get()),
            "SEARCH_BOX_X": int(entry_search_box_x.get()),
            "SEARCH_BOX_Y": int(entry_search_box_y.get()),
            "COPY_INSERT_BUTTON_X": int(entry_copy_insert_button_x.get()),
            "COPY_INSERT_BUTTON_Y": int(entry_copy_insert_button_y.get()),
            "CODE_FIELD_X": int(entry_code_field_x.get()),
            "CODE_FIELD_Y": int(entry_code_field_y.get()),
            "DESCRIPTION_FIELD_X": int(entry_description_field_x.get()),
            "DESCRIPTION_FIELD_Y": int(entry_description_field_y.get()),
            "DATE_FIELD_X": int(entry_date_field_x.get()),
            "DATE_FIELD_Y": int(entry_date_field_y.get()),
            "SAVE_BUTTON_X": int(entry_save_button_x.get()),
            "SAVE_BUTTON_Y": int(entry_save_button_y.get()),
            "NEW_TEST_ITEM_X": int(entry_new_test_item_x.get()),
            "NEW_TEST_ITEM_Y": int(entry_new_test_item_y.get()),
            "EDIT_BUTTON_X": int(entry_edit_button_x.get()),
            "EDIT_BUTTON_Y": int(entry_edit_button_y.get()),
            "THICKNESS_FIELD_X": int(entry_thickness_field_x.get()),
            "THICKNESS_FIELD_Y": int(entry_thickness_field_y.get()),
            "THICKNESS_FIELD_OFFSET": int(entry_thickness_field_offset.get()),
            "SAVE_BUTTON_2_X": int(entry_save_button_2_x.get()),
            "SAVE_BUTTON_2_Y": int(entry_save_button_2_y.get()),
            "excel_file": entry_excel_file.get(),
            "WINDOW_X": int(entry_window_x.get()),
            "WINDOW_Y": int(entry_window_y.get()),
            "WINDOW_WIDTH": int(entry_window_width.get()),
            "WINDOW_HEIGHT": int(entry_window_height.get()),
            "WINDOW_TITLE": entry_window_title.get()
        }
    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
        return

    # --- LOAD THE EXCEL DATA ---
    try:
        df = pd.read_excel(config["excel_file"])
    except Exception as e:
        messagebox.showerror("Excel Error", f"Failed to read Excel file: {e}")
        return

    messagebox.showinfo("Ready", "Switch to The Edge application. Automation will start in 5 seconds...")
    time.sleep(config["LONG_DELAY"])

    # --- BEGIN THE AUTOMATION PROCESS ---
    if not position_window(config["WINDOW_TITLE"], config["WINDOW_X"], config["WINDOW_Y"], config["WINDOW_WIDTH"], config["WINDOW_HEIGHT"]):
        return

    pyautogui.click(x=config["DATABASE_BUTTON_X"], y=config["DATABASE_BUTTON_Y"])
    time.sleep(config["MEDIUM_DELAY"])
    
    pyautogui.doubleClick(x=config["FIRE_TESTS_X"], y=config["FIRE_TESTS_Y"])
    time.sleep(config["LONG_DELAY"])
    
    # Process each UL design record from the Excel file.
    for index, row in df.iterrows():
        test_name = str(row["TestName"])
        new_code = str(row["NewCode"])
        new_description = str(row["NewDescription"])
        new_date = str(row["NewDate"])
        # Read the four thickness values from Excel.
        thickness_values = [
            str(row["NewThickness1"]),
            str(row["NewThickness2"]),
            str(row["NewThickness3"]),
            str(row["NewThickness4"])
        ]
        
        print(f"Processing record {index+1}: {test_name}")
        
        # 3. Click the search box, type the test name, and press Enter.
        pyautogui.click(x=config["SEARCH_BOX_X"], y=config["SEARCH_BOX_Y"])
        time.sleep(config["SHORT_DELAY"])
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(test_name, interval=0.1)
        time.sleep(config["SHORT_DELAY"])
        pyautogui.press("enter")
        time.sleep(config["LONG_DELAY"])
    
        # 4. Click the "copy and insert" button to duplicate the test record.
        pyautogui.click(x=config["COPY_INSERT_BUTTON_X"], y=config["COPY_INSERT_BUTTON_Y"])
        time.sleep(config["MEDIUM_DELAY"])
        
        # 5. Update the duplicate record's fields:
        # a. Update code.
        pyautogui.click(x=config["CODE_FIELD_X"], y=config["CODE_FIELD_Y"])
        time.sleep(config["SHORT_DELAY"])
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(new_code, interval=0.1)
        time.sleep(config["SHORT_DELAY"])
        
        # b. Update description.
        pyautogui.click(x=config["DESCRIPTION_FIELD_X"], y=config["DESCRIPTION_FIELD_Y"])
        time.sleep(config["SHORT_DELAY"])
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(new_description, interval=0.1)
        time.sleep(config["SHORT_DELAY"])
        
        # c. Update date.
        pyautogui.click(x=config["DATE_FIELD_X"], y=config["DATE_FIELD_Y"])
        time.sleep(config["SHORT_DELAY"])
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(new_date, interval=0.1)
        time.sleep(config["SHORT_DELAY"])
        
        # 6. Save updated test info.
        pyautogui.click(x=config["SAVE_BUTTON_X"], y=config["SAVE_BUTTON_Y"])
        time.sleep(config["LONG_DELAY"])
        
        # 7. Open the new test record details.
        pyautogui.click(x=config["NEW_TEST_ITEM_X"], y=config["NEW_TEST_ITEM_Y"])
        time.sleep(config["MEDIUM_DELAY"])
        
        # 8. Click Edit to update thickness values.
        pyautogui.click(x=config["EDIT_BUTTON_X"], y=config["EDIT_BUTTON_Y"])
        time.sleep(config["MEDIUM_DELAY"])
        
        # 9. For each of the four thickness fields, update the value.
        for i, thickness in enumerate(thickness_values):
            current_field_y = config["THICKNESS_FIELD_Y"] + i * config["THICKNESS_FIELD_OFFSET"]
            pyautogui.click(x=config["THICKNESS_FIELD_X"], y=current_field_y)
            time.sleep(config["SHORT_DELAY"])
            pyautogui.hotkey("ctrl", "a")
            pyautogui.typewrite(thickness, interval=0.1)
            time.sleep(config["SHORT_DELAY"])
        
        # 10. Save the updated thickness values.
        pyautogui.click(x=config["SAVE_BUTTON_2_X"], y=config["SAVE_BUTTON_2_Y"])
        time.sleep(config["LONG_DELAY"])
        
        print(f"Record {index+1} processed.")
    
    messagebox.showinfo("Done", "Automation complete for all records.")
    print("Automation complete for all records.")

# ---------------------------
# GUI SETUP USING TKINTER
# ---------------------------
root = tk.Tk()
root.title("UL Design Update Automation Tool")
root.geometry("800x600")  # Set initial window size

# Create main frame with padding
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas with scrollbar
canvas = tk.Canvas(main_frame)
scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create sections with labels
def create_section(parent, title):
    frame = ttk.LabelFrame(parent, text=title, padding="10")
    frame.pack(fill="x", padx=5, pady=5)
    return frame

# Delay Settings Section
delay_frame = create_section(scrollable_frame, "Delay Settings")
delay_frame.pack(fill="x", padx=5, pady=5)

# Create a grid for delay settings
delay_grid = ttk.Frame(delay_frame)
delay_grid.pack(fill="x", padx=5, pady=5)

# Short Delay
ttk.Label(delay_grid, text="Short Delay (sec):").grid(row=0, column=0, sticky="w", padx=5, pady=2)
entry_short_delay = ttk.Entry(delay_grid, width=10)
entry_short_delay.insert(0, "1")
entry_short_delay.grid(row=0, column=1, sticky="w", padx=5, pady=2)

# Medium Delay
ttk.Label(delay_grid, text="Medium Delay (sec):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
entry_medium_delay = ttk.Entry(delay_grid, width=10)
entry_medium_delay.insert(0, "2")
entry_medium_delay.grid(row=1, column=1, sticky="w", padx=5, pady=2)

# Long Delay
ttk.Label(delay_grid, text="Long Delay (sec):").grid(row=2, column=0, sticky="w", padx=5, pady=2)
entry_long_delay = ttk.Entry(delay_grid, width=10)
entry_long_delay.insert(0, "3")
entry_long_delay.grid(row=2, column=1, sticky="w", padx=5, pady=2)

# Window Settings Section
window_frame = create_section(scrollable_frame, "Window Settings")
window_frame.pack(fill="x", padx=5, pady=5)

# Create a grid for window settings
window_grid = ttk.Frame(window_frame)
window_grid.pack(fill="x", padx=5, pady=5)

# Window Title
ttk.Label(window_grid, text="Window Title:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
entry_window_title = ttk.Entry(window_grid, width=30)
entry_window_title.insert(0, "The Edge")
entry_window_title.grid(row=0, column=1, sticky="w", padx=5, pady=2)

# Window X
ttk.Label(window_grid, text="Window X:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
entry_window_x = ttk.Entry(window_grid, width=10)
entry_window_x.insert(0, "0")
entry_window_x.grid(row=1, column=1, sticky="w", padx=5, pady=2)

# Window Y
ttk.Label(window_grid, text="Window Y:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
entry_window_y = ttk.Entry(window_grid, width=10)
entry_window_y.insert(0, "0")
entry_window_y.grid(row=2, column=1, sticky="w", padx=5, pady=2)

# Window Width
ttk.Label(window_grid, text="Window Width:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
entry_window_width = ttk.Entry(window_grid, width=10)
entry_window_width.insert(0, "1024")
entry_window_width.grid(row=3, column=1, sticky="w", padx=5, pady=2)

# Window Height
ttk.Label(window_grid, text="Window Height:").grid(row=4, column=0, sticky="w", padx=5, pady=2)
entry_window_height = ttk.Entry(window_grid, width=10)
entry_window_height.insert(0, "768")
entry_window_height.grid(row=4, column=1, sticky="w", padx=5, pady=2)

# Excel File Section
excel_frame = create_section(scrollable_frame, "Excel File Settings")
excel_frame.pack(fill="x", padx=5, pady=5)

# Create a grid for Excel file settings
excel_grid = ttk.Frame(excel_frame)
excel_grid.pack(fill="x", padx=5, pady=5)

# Excel File
ttk.Label(excel_grid, text="Excel File:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
entry_excel_file = ttk.Entry(excel_grid, width=50)
entry_excel_file.insert(0, "ul_designs.xlsx")
entry_excel_file.grid(row=0, column=1, sticky="w", padx=5, pady=2)
ttk.Button(excel_grid, text="Browse", command=browse_excel_file).grid(row=0, column=2, padx=5, pady=2)

# UI Element Coordinates Section
coordinates_frame = create_section(scrollable_frame, "UI Element Coordinates")
coordinates_frame.pack(fill="x", padx=5, pady=5)

# Create a grid for coordinates
coord_grid = ttk.Frame(coordinates_frame)
coord_grid.pack(fill="x", padx=5, pady=5)

# Function to add coordinate fields
def add_coordinate_field(parent, label, row):
    ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
    ttk.Label(parent, text="X:").grid(row=row, column=1, padx=2)
    x_entry = ttk.Entry(parent, width=10)
    x_entry.grid(row=row, column=2, padx=2)
    ttk.Label(parent, text="Y:").grid(row=row, column=3, padx=2)
    y_entry = ttk.Entry(parent, width=10)
    y_entry.grid(row=row, column=4, padx=2)
    return x_entry, y_entry

# Add all coordinate fields
row = 0
entry_database_button_x, entry_database_button_y = add_coordinate_field(coord_grid, "Database Button:", row)
row += 1

entry_fire_tests_x, entry_fire_tests_y = add_coordinate_field(coord_grid, "Fire Tests:", row)
row += 1

entry_search_box_x, entry_search_box_y = add_coordinate_field(coord_grid, "Search Box:", row)
row += 1

entry_copy_insert_button_x, entry_copy_insert_button_y = add_coordinate_field(coord_grid, "Copy Insert Button:", row)
row += 1

entry_code_field_x, entry_code_field_y = add_coordinate_field(coord_grid, "Code Field:", row)
row += 1

entry_description_field_x, entry_description_field_y = add_coordinate_field(coord_grid, "Description Field:", row)
row += 1

entry_date_field_x, entry_date_field_y = add_coordinate_field(coord_grid, "Date Field:", row)
row += 1

entry_save_button_x, entry_save_button_y = add_coordinate_field(coord_grid, "Save Button:", row)
row += 1

entry_new_test_item_x, entry_new_test_item_y = add_coordinate_field(coord_grid, "New Test Item:", row)
row += 1

entry_edit_button_x, entry_edit_button_y = add_coordinate_field(coord_grid, "Edit Button:", row)
row += 1

entry_thickness_field_x, entry_thickness_field_y = add_coordinate_field(coord_grid, "Thickness Field:", row)
row += 1

# Thickness Field Offset
ttk.Label(coord_grid, text="Thickness Field Offset:").grid(row=row, column=0, sticky="w", padx=5, pady=2)
entry_thickness_field_offset = ttk.Entry(coord_grid, width=10)
entry_thickness_field_offset.insert(0, "30")
entry_thickness_field_offset.grid(row=row, column=1, columnspan=2, padx=2)
row += 1

entry_save_button_2_x, entry_save_button_2_y = add_coordinate_field(coord_grid, "Save Button 2:", row)

# Run Button
run_button = ttk.Button(scrollable_frame, text="Run Automation", command=run_automation)
run_button.pack(pady=20)

# Configure the root window
root.mainloop() 