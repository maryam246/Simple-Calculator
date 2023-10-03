
# Simple Calculator.
This code is a simple calculator implemented using the Tkinter GUI toolkit in Python in which the code is base on OOP. It has the following features:
## Importing tkinter:
The code begins by importing the tkinter library with the alias tk. tkinter is a standard Python library used for creating GUI applications.
## Calculator Class:
A Calculator class is defined to encapsulate the calculator's functionality. This class will be responsible for creating the calculator's UI and handling user input and calculations.
## Initialization (-init- method):
### Self.root:
 Stores the main tkinter window.
### Self.result_var: 
A StringVar that is used to display the current input and result in the calculator's display.
### Self.current_input: 
Stores the current input string.
### Self.has_error: 
Indicates whether an error has occurred during calculation.
### Self.valid_characters: 
A set of valid characters that can be entered into the calculator, including digits (1-9), operators (+, -, *, /), decimal point (.), and equals sign (=).
## Create_ui method:
The create_ui method is responsible for creating the calculator's user interface.

### Create_entry:
This method creates a text input field for the calculator's display.
### Create_buttons: 
This method creates buttons for digits (0-9), operators (+, -, *, /), decimal point (.), equals sign (=), Clear (C), and Backspace (⌫).
## On_button_click method:
This method is called when a button is clicked. It handles various button actions.

#### __'C':__ *Clears the current input.*
#### __'⌫'(Backspace)__: *Removes the last character from the current input.*
#### __'='(Equal)__ *Evaluates the current input as an expression and displays the result.*
#### __Other valid characters:__ *Appends the character to the current input.*
## On_entry_key_press method: 
This method is called when a key is pressed while the Entry widget has focus.
## Update_display method: 
Updates the display with the current input. If the input exceeds a certain length, it displays only the last 14 characters to prevent overflow.
## if "name" == "main":
This block ensures that the mainloop is only started when the program is run directly, and not when it is imported as a module. This is important because it prevents the mainloop from being started multiple times, which could cause problems.
