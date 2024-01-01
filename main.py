import pyautogui, pytesseract, time

# navigate to the device popup
pyautogui.moveTo(1660, 1050)
pyautogui.click()
# open file manager
pyautogui.moveTo(1670, 670)
pyautogui.click()
# wait for file manager to load
time.sleep(7)
# Internal shared storage folder
pyautogui.moveTo(220, 205)
pyautogui.doubleClick()
# sort the folders by name
pyautogui.moveTo(105, 60)
pyautogui.click()
pyautogui.moveTo(105, 260, 0.5)
pyautogui.moveTo(415, 260, 0.5)
pyautogui.click()
# Android folder
pyautogui.moveTo(355, 210)
pyautogui.doubleClick()
# data folder
pyautogui.moveTo(220, 210)
pyautogui.doubleClick()
# sort by created date
pyautogui.moveTo(105, 60)
pyautogui.click()
pyautogui.moveTo(105, 260, 0.5)
pyautogui.moveTo(415, 260, 0.5)
pyautogui.moveTo(415, 355, 0.5)
pyautogui.click()
# org.telegram.messenger folder
pyautogui.moveTo(1035, 210)
pyautogui.doubleClick()
# files and tlegram folder
pyautogui.moveTo(220, 210)
pyautogui.doubleClick()
pyautogui.doubleClick()
# Telegram folder files
pyautogui.moveTo(480, 210)
pyautogui.doubleClick()
# navigate to the most recent file
pyautogui.press('end')
