import pyautogui
import os
import time

os.system("cls")
for c in range(0, 2, 1):

    MoV = int(input("Marvel o DC? 1)Marvel 2)DC C)Ambos 3)Ninguno "))
    Refran = input("Escribe un refran, catchphrase, dicho popular o cita de libro o pelicula ")
    Hora = '''Cual es la mejor hora del dia para comer pastel? a)8am b)9am c)10am d)11am e)12pm f)1pm g)2pm h)3pm i)4pm j)5pm k)6pm i)Despues de las 7pm'''
    HoraSel = input(Hora)
    CorreoF = input("Escribe un correo falso: ")

    time.sleep(3)
    if MoV == 1:
        pyautogui.click(x=337, y = 444, clicks = 1)
    elif MoV == 2:
        pyautogui.click(x=337, y = 482, clicks = 1)
    elif MoV == 3:
        pyautogui.click(x=337, y = 523, clicks = 1)
    elif MoV == 4:
        pyautogui.click(x=337, y = 564, clicks = 1)
    else:
        print("Opción no válida")
        exit()

    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.typewrite(Refran)
    pyautogui.press('tab')
    pyautogui.press('tab')

    if HoraSel == 'a':
        pyautogui.press("Down")
    elif HoraSel == 'b':
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif HoraSel == 'c':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif HoraSel == 'd':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif HoraSel == 'e':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif HoraSel == 'f':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif HoraSel == 'g':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif HoraSel == 'h':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif HoraSel == 'i':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif HoraSel == 'j':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif HoraSel == 'k':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif HoraSel == 'l':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    else:
        print("Opción no valida")
        exit()
    pyautogui.press('tab')
    pyautogui.press('tab')

    CorreoF = CorreoF.split("@")
    pyautogui.typewrite(CorreoF[0])
    pyautogui.hotkey('ctrl', 'alt', 'q')
    pyautogui.typewrite(CorreoF[1])
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)

    if c < 1:
        pyautogui.click(x=364, y=456, clicks=1)
        c = c + 1
