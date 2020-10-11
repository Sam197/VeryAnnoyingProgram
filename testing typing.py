import pyautogui
import time

with open('star.txt', 'r') as scr:             # script.txt = bee movie, star.txt = All star
    scr = scr.read()

# scrtotype = []
# scr = scr.split("  ")                          #Bee movie format code
# for line in scr:
#     line = line.split()
#     while "-" in line: line.remove('-')
#     new_word = ""
#     for word in line:
#         new_word += f" {word}"
#     scrtotype.append(new_word)

# print(scrtotype)

scrtotype = scr.split()                     #All star format code
print(scr)
time.sleep(5)                               #5 second buffer

for line in scrtotype:                       #The actual typing code
    print(line)
    pyautogui.write(f"{str(line)}")
    pyautogui.press('return')