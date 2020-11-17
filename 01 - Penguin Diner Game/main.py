import pyautogui
import keyboard
import cv2
import numpy as np
import time


def meal_deal(food_name):
    location = pyautogui.locateOnScreen(f'{food_name}.png', confidence=0.90)
    if location is not None:
        pyautogui.click(location)
        time.sleep(0.5)
        wished_locaiton = pyautogui.locateOnScreen(f'wished_{food_name}.png', confidence=0.95)
        pyautogui.click(wished_locaiton)
        time.sleep(0.5)

while True:
    start_time = time.time()
    img = pyautogui.screenshot()
    waiting_part = pyautogui.screenshot(region=(590,412,110,250))
    # #print(pyautogui.position())
    # img = np.array(waiting_part)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("pencere", img)
    # cv2.waitKey(1)

    penguin_location = pyautogui.locateOnScreen('pen1.png', confidence=0.7)
    empty_table_location = pyautogui.locateOnScreen('table.png', confidence=0.9)
    empty_table_location_2 = pyautogui.locateOnScreen('table2.png', confidence=0.9)
    empty_table_location_3 = pyautogui.locateOnScreen('table3.png', confidence=0.9)
    if penguin_location is not None:
        pyautogui.click(penguin_location)
        time.sleep(0.5)
        if empty_table_location is not None:
            pyautogui.click(empty_table_location)
        elif empty_table_location_2 is not None:
            pyautogui.click(empty_table_location_2)
        elif empty_table_location_3 is not None:
            pyautogui.click(empty_table_location_3)

    money_location = pyautogui.locateOnScreen('money.png', confidence=0.65)
    if money_location is not None:
        pyautogui.click(money_location)

    customer_location = pyautogui.locateOnScreen('take_order.png', confidence=0.75)
    if customer_location is not None:
        pyautogui.click(customer_location)
        time.sleep(1)

    food_names = ["icecream", "fish", "yellow_shake", "brown_shake", "a",
                  "b", "taco", "chips", "soup"]
    for food in food_names:
        meal_deal(food)
