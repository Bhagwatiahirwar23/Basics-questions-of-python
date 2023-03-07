# data entry
import pyautogui 
for i in range(3):

    passw = pyautogui.password(
    text = 'enter your password',
    title = 'data entry',
    default = ' ', mask='*')
    print(passw)
