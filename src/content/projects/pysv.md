# PYSV
A TUI python app for reading, writing and editing CSV files without leaving your terminal

* [GitHub](https://github.com/Force4760/pysv)

## Tech Stack
* Languages:
    * **Python**

* Modules:
    * **click** - for command line flags parsing
    * **csv** - for CSV file parsing
    * **prompt_toolkit** - for generating the prompt and the TUI elements
    * **dataclasses** - to faccilitate the creation of classes using python
    * **pyperclip** - to interface with the system's clipboard
    * **json** - for JSON file parsing (used for config files)

## Usage
* **load, ld:** Load a new csv file into memory

    * `load «path_to_file|named_file»`

    * `ld «path_to_file|named_file»`

* **save, sv:** Save the currently loaded csv to a file

    * `save «path_to_file|NONE»`

    * `sv «path_to_file|NONE»`

* **peek:** show a single column or row

    * `peek «column|row» «name»`

* **ls:** show the names of all column, rows or both

    * `ls «column|row|NONE»`

* **delete, del:** delete all the values on a specified column or row

    * `delete «column|row» «name»`

    * `del «column|row» «name»`

* **cell:** show the value of a specified cell

    * `cell «column_name» «row_name»`

* **copy, cp:** copy to the clipboard the contents of a specified cell

    * `copy «column_name» «row_name»`

    * `cp «column_name» «row_name»`

* **switch, sw:** switch the values between two tables or two rows

    * `switch «column|row» «name_1» | «name_2»`

    * `sw «column|row» «name_1» | «name_2»`

* **edit:** edit the content of a specified cell

    * `edit «column_name» «row_name»`

* **replace:** replace the content of a specified cell

    * `replace «column_name» «row_name»`

* **show, s:** show the current csv file as an html table inside a browser

* **help, h:** show this message

* **clear, cls, c:** clear the screen

## Color Schemes
* Nord
* Gruvbox
* Dracula
* Monokai
* Palenight