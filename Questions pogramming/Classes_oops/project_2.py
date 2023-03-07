import pyautogui 
from time import sleep 
sleep(5)
msg = "kkrh\n"
for i  in range(20):
    pyautogui.typewrite(msg )
    pyautogui.press('enter')



# import pyautogui 
# from time import sleep 
# sleep(5)
# msg = "hlw \n"
# i = 0
# while i <= 10:
#     i = i+1
#     pyautogui.typewrite(msg )
#     pyautogui.press('enter')


# import pyautogui 
# img = pyautogui.screenshot('screenshot.jpg')
# print(img)