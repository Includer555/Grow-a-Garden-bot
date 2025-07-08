import pyautogui
import pyscreeze
import time
import keyboard

dollar_symbol = "DollarSign.png"
buy_btn = "BuyBTN.png"
garden_button_pos = [960, 137]
seeds_button_pos = [697, 125]
scroll_bar_pos = [1310, 367]
menu_size_pos = [594, 309]
offscreen_pos = [2500, 500]
scrolls = 20

scans = 1
bought_items = 0
bought_items_file = "BoughtItemCount.txt"

def TakeScreenShot(width, height, number, screenshotName):
    screenshot = pyautogui.screenshot(region=(menu_size_pos[0],menu_size_pos[1], width, height))
    screenshot_name = screenshotName+str(number)+".png"
    screenshot.save(screenshot_name)

def ClickButton(x, y):
    pyautogui.moveTo(offscreen_pos[0],offscreen_pos[1],0)
    pyautogui.doubleClick()
    pyautogui.moveTo(x, y, 0)
    pyautogui.doubleClick()

def DragScrollBar(x, y, scroll_amount, times):
    global bought_items
    global scans
    bought_items = 0

    print(f"----------------------------🔎SCAN {scans} BEGIN🔎-----------------------------------")

    pyautogui.moveTo(offscreen_pos[0],offscreen_pos[1],0)
    pyautogui.doubleClick()
    pyautogui.moveTo(x, y, 0)
    pyautogui.doubleClick()
    for i in range(times):
        TakeScreenShot(750, 500, i, "Screenshot")
        BuyThing(i)
        time.sleep(0.1)
        pyautogui.scroll(-scroll_amount)
    TakeScreenShot(750, 500, i, "Screenshot")
    
    for i in range(times):
        time.sleep(0.1)
        pyautogui.scroll(scroll_amount)
    
    f = open(bought_items_file, "w")
    f.write(str(bought_items))
    f.close()
    
    scans+= 1
    print(f"----------------------------⚠️SCAN {scans} END⚠️-----------------------------------\n\n\n")

def BuyThing(index):
    location = None
    center = 0
    global bought_items

    try:
        location = pyautogui.locateOnScreen(dollar_symbol, confidence=0.8)
    except:
        print("[❌] Not in stock!")
        return

    if (location):
        center = pyautogui.center(location)
        pyautogui.moveTo(offscreen_pos[0],offscreen_pos[1])
        pyautogui.doubleClick()
        pyautogui.moveTo(center[0], center[1])
        pyautogui.doubleClick()
    else:
        return

    time.sleep(0.3)
    try:
        location = pyautogui.locateOnScreen(dollar_symbol, confidence=0.8)
        center = pyautogui.center(location)
    except:
        print("fail")

    if location:
        moveto_pos = [center[0]-280, center[1]+120]
        pyautogui.moveTo(offscreen_pos[0],offscreen_pos[1])
        pyautogui.doubleClick()
        pyautogui.moveTo(moveto_pos)
        TakeScreenShot(500, 500, index, "BoughtItem")
        bought_items+=1
        for i in range(10):
            pyautogui.doubleClick()

    print(f"[✅] Found in stock seed at (x:{center[0]} y:{center[1]})")

print("#\/\/\/\/\/\/\/\/\/\/🌱GROW A GARDEN BOT🌱\/\/\/\/\/\/\/\/\/\/\/\/\/\/#")
print("[📢] Starting in 5 seconds...")
time.sleep(5)
while (True):
    DragScrollBar(scroll_bar_pos[0], scroll_bar_pos[1], 400, scrolls)
    time.sleep(10)