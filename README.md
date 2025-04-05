# UL Design Update Automation Tool

This tool automates the process of updating UL design records in The Edge application using PyAutoGUI.
 ****(approximately 50 to 75 minutes for 100 UL Designs under standard internet speeds.)****

## Project Structure

- `automation_gui.py` - The main application with a GUI for configuration
- `scripts/get_coords.py` - Helper script to get screen coordinates
- `scripts/create_sample_excel.py` - Script to create a sample Excel file
- `ul_designs.xlsx` - Sample Excel file with the required columns

## Setup Instructions

### 1. Prerequisites

- Python 3.6 or later
- Required Python packages:
  - pyautogui
  - pandas
  - openpyxl
  - tkinter (usually included with Python)
  - pygetwindow (for window positioning)

Install the required packages with:

```bash
pip install pyautogui pandas openpyxl pygetwindow
```

### 2. Window Positioning

Before running the automation, configure the window positioning settings:

1. Window Title: The title of The Edge application window (default: "The Edge")
2. Window Position (X, Y): The coordinates where the window should be positioned (default: 0, 0)
3. Window Size (Width, Height): The dimensions to resize the window to (default: 1024x768)

These settings ensure that the UI elements appear in consistent locations across different computers.
(SET WINDOW + Button COORDINATES UP ONCE, NO LONGER HAVE TO BOTHER WITH ITEM 4)

### 3. Excel File Format

The automation requires an Excel file (`ul_designs.xlsx`) with these exact columns:
- **TestName** - Name of the existing test to search for
- **NewCode** - New code for the duplicated record
- **NewDescription** - New description for the duplicated record
- **NewDate** - New date for the duplicated record
- **NewThickness1** - First thickness value
- **NewThickness2** - Second thickness value
- **NewThickness3** - Third thickness value
- **NewThickness4** - Fourth thickness value

A sample file with these columns has been created for you.

### 4. Getting Screen Coordinates

Before running the automation, you need to determine the screen coordinates for all UI elements:

1. Run the coordinate helper script:
   ```bash
   python scripts/get_coords.py
   ```

2. Hover your mouse over each UI element in The Edge application and note the X,Y coordinates.

3. Enter these coordinates in the automation GUI.
4. Database Estimating Button:

DATABASE_BUTTON_X and DATABASE_BUTTON_Y
(The button you click to open the database menu.)

Fire Tests Section:

FIRE_TESTS_X and FIRE_TESTS_Y
(The area or icon for the "fire tests" section that you need to double-click.)

Search Box in the Fire Test Database:

SEARCH_BOX_X and SEARCH_BOX_Y
(The input field where you type the test name.)

Copy and Insert Button:

COPY_INSERT_BUTTON_X and COPY_INSERT_BUTTON_Y
(The button you click to duplicate a test record.)

Code Field (in the duplicated record):

CODE_FIELD_X and CODE_FIELD_Y
(The field where you update the test code.)

Description Field (in the duplicated record):

DESCRIPTION_FIELD_X and DESCRIPTION_FIELD_Y
(The field where you update the test description.)

Date Field (in the duplicated record):

DATE_FIELD_X and DATE_FIELD_Y
(The field where you update the test date.)

Save Button (to save the updated test info):

SAVE_BUTTON_X and SAVE_BUTTON_Y
(The button that saves the changes to the duplicated record.)

New Test Item in the List:

NEW_TEST_ITEM_X and NEW_TEST_ITEM_Y
(The location of the newly created test record in the list that you click to open its details.)

Edit Button (to open the thickness update window):

EDIT_BUTTON_X and EDIT_BUTTON_Y
(The button you click to enter the thickness editing mode.)

First Thickness Field (in the thickness update window):

THICKNESS_FIELD_X and THICKNESS_FIELD_Y
(The coordinate for the first thickness entry field.)

Vertical Offset Between Thickness Fields:

THICKNESS_FIELD_OFFSET
(The number of pixels separating one thickness field from the next.)

Save Button for Thickness Updates:

SAVE_BUTTON_2_X and SAVE_BUTTON_2_Y
(The button used to save the updated thickness values.)

### 5. Running the Automation

1. Launch the automation tool:
   ```bash
   python automation_gui.py
   ```

2. Fill in all the configuration fields:
   - Delay times (in seconds)
   - Screen coordinates for all UI elements
   - Path to your Excel file

3. Click "Run Automation"

4. When prompted, switch to The Edge application

### 6. Notes

- The automation will process each row in the Excel file
- Make sure The Edge application is already logged in and ready
- Do not move your mouse during the automation process
- Adjust the delay values if the automation is too fast or too slow

## Creating an Executable (Optional)

To package the application as a standalone executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --onefile automation_gui.py
   ```

3. The executable will be created in the `dist` folder
