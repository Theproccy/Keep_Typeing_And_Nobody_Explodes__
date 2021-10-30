import json

import PySimpleGUI as Gui

# open dataset
file = open("Symbols_Data.json", "r")
data = json.load(file)
FILENAMES_LIST = data["FILENAMES_LIST"]
names_list = data["NAMES_LIST"]
file.close()
#var creation
i = 0

#window layout
layout = [[Gui.Text(text="Image " + str(i + 1), key="-TEXT-")],
          [Gui.Image(filename=FILENAMES_LIST[0], key="-IMAGE-")],
          [Gui.Button(button_text="Back"), Gui.Button(button_text="Next")],
          [Gui.Input(default_text=names_list[i], size=30, key="-INPUT-")],
          [Gui.Button(button_text="Save", tooltip="Used to save all of the names to the file")]]
win = Gui.Window("Icon Labeler", layout)  #window creation

while True:  # main loop
    event, values = win.read()  # if somthing happens in the window
    # repaces label in list
    names_list.pop(i)
    names_list.insert(i, values['-INPUT-'])
    if event == "Next":  # if button pressed
        if 30 >= i >= 0:
            i += 1
    if event == "Back":  # if button pressed
        if 31 >= i >= 1:
            i -= 1
    if event == Gui.WIN_CLOSED:  # if exit pressed
        break
    if event == "Save":  # overates json file
        file = open("Symbols_Data.json", "w")
        data.update({"FILENAMES_LIST": FILENAMES_LIST,
                     "NAMES_LIST": names_list})
        json_data = json.dumps(data)
        file.write(json_data)
        file.close()
    #updates after button push
    win['-TEXT-'].update("Image " + str(i + 1))
    win['-IMAGE-'].update(FILENAMES_LIST[i])
    win['-INPUT-'].update(names_list[i])
