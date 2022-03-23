from threading import Timer
import time

from wallpaper import Wallpaper
from color import Color


wallpaper = Wallpaper("resources/backgrounds/bg8.jpeg")

updateTimer = Timer(0.1, wallpaper.update)
updateTimer.daemon = True
updateTimer.start()

renderTimer = Timer(1, wallpaper.render)
renderTimer.daemon = True
renderTimer.start()

while True:
    time.sleep(1)
    if not updateTimer.is_alive():
        updateTimer = Timer(1, wallpaper.update)
        updateTimer.daemon = True
        updateTimer.start()
    if not renderTimer.is_alive():
        renderTimer = Timer(30, wallpaper.render)
        renderTimer.daemon = True
        renderTimer.start()
