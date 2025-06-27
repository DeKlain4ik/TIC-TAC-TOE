import turtle 
from functions import *



main_menu()

screen.onclick(start_game)

screen.listen()
screen.onkey(back_to_menu, "Escape")


turtle.mainloop()