from color import Color
import ctypes
import os
import time
from PIL import Image, ImageFilter, ImageEnhance

import forms.TimeForm


class Wallpaper:
    def __init__(self, defaultColor=Color()):
        user32 = ctypes.windll.user32
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

        self.defaultColor = defaultColor
        if type(defaultColor) == Color:
            self.defaultColor = Color
            self.background = Image.new("RGBA", (self.width, self.height), defaultColor.get())
        elif type(defaultColor) == str:
            self.defaultColor = Color()
            self.background = Image.open(defaultColor).convert("RGBA").resize((self.width, self.height))
        else:
            raise Exception("Invalid background type")

        # self.buffer = Image.new("RGBA", (self.width, self.height), self.defaultColor.get())

        self.forms = []
        self.forms.append(forms.TimeForm.Main())

    def render(self):
        # self.buffer = Image.new("RGBA", (self.width, self.height), self.defaultColor.get())
        # self.buffer = Image.open("resources/backgrounds/bg1.jpeg").convert("RGBA")
        self.buffer = self.background
        # self.buffer.thumbnail((self.width, self.height), Image.ANTIALIAS)
        # self.buffer = self.buffer.resize((self.width, self.height))
        if int(time.strftime("%H")) < 21 or int(time.strftime("%H")) > 6:
            self.buffer = ImageEnhance.Brightness(self.buffer).enhance(0.35)
        else:
            self.buffer = ImageEnhance.Brightness(self.buffer).enhance(0.4)
        self.buffer = self.buffer.filter(ImageFilter.GaussianBlur(radius=200))

        for i in self.forms:
            self.buffer = i.render(self.buffer, self.width, self.height)
            # self.buffer.paste(temp, (0, 0), temp)

        if not os.path.exists(os.path.expanduser("~\\AppData\\Roaming\\livaWallpaper\\")):
            os.makedirs(os.path.expanduser("~\\AppData\\Roaming\\livaWallpaper\\"))
        self.buffer.save(os.path.expanduser("~\\AppData\\Roaming\\livaWallpaper\\wallpaperCash.bmp"))
        ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, os.path.expanduser("~\\AppData\\Roaming\\livaWallpaper\\wallpaperCash.bmp"), 2)

    def update(self):
        for i in self.forms:
            i.update()
