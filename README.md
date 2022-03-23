# live wallpaper on python 
![image](https://github.com/lavaFrai/liveWallpaper/blob/master/screenshots/Screenshot_1.png?raw=true)
Проект живых обоев на Python обладающий неплохой модульностью. 
Отрисовка кадров происходит раз в несколько секунд средствами библиотеки Pillow.
Для стабильной работы требуется доступ к сети интернет.

## Использование
Проект предназначен для работы ТОЛЬКО на OS Windows 
```shell
git clone https://github.com/lavaFrai/liveWallpaper
cd liveWallpaper
run.bat
```

## Создание своего модуля
 1) Создайте файл `*.py` в папке `forms`
 2) Создайте класс с методами `render` и `update`, вот шаблон который можно использовать:
```python
from PIL import Image, ImageDraw, ImageFont

class Main:
    def render(self, frame: Image, width: int, height: int):
        # Вызывается редко, здесь модифицируем frame любыми способами из библиотеки Pillow
        # При обработке кадр не должен изменить свой размер
        return frame

    def update(self):
        # Вызывается чаще, может использоваться для любых служебных нужд
        pass
```
 3) В файле `wallpaper.py` импортируйте свой `*.py` файл и добавьте свой класс в список `Wallpaper.forms` (Пример в строке 29)
```python
...
import forms.TimeForm
# Здесь импортируйте свой файл 

class Wallpaper:
    def __init__(self, defaultColor=Color()):
        
...

        self.forms = []
        self.forms.append(forms.TimeForm.Main())
        # А здесь добавьте в список
...
```

# Известные ошибки и проблемы
 + Нет автоматического добавления в автозагрузку, файл приходится запускать при каждом входе в систему
 + При выключении живых обоев, старые возвращать придется вручную, через настройки персонализации