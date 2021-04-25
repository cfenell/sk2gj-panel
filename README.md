# sk2gj-panel
Remote control panel for antenna rotor and switch, Python Tkinter GUI

## The program panel.py presents a control panel with 

### A video window, showing webcam stream.
Supposed to look at rotor control indicator.

### Buttons for controlling 8 relays.

* Relay 1 Rotor CCW, momentary on button
* Relay 2 Rotor CW, momentary on button
* Relay 3 Power switch, On/Off toggle button
* Relays 4-8 Antenna selector, set of 5 radio buttons

## Dependencies
- python-parallel (Parallel port control)
- python-tkinter (GUI)
- python-opencv / CV2 (video)

## Usage: 
  python3 ./panel.py
