from PIL import Image, ImageDraw, ImageFont
import requests
import json
import time


class Main:
    def render(self, frame, width, height):
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("resources\\fonts\\font.ttf", 128)

        # Time
        msg = time.strftime("%H:%M")
        w, h = draw.textsize(msg, font=font)
        draw.text(
            ((width - w) / 2, (height - h) / 2),
            msg,
            (255, 255, 255),
            font=font)
        draw.line(
            (width / 2 - 350, ((height - h) / 2) - 10, width / 2 + 350, ((height - h) / 2) - 10),
            fill=(255, 255, 255),
            width=2)

        # Date
        font = ImageFont.truetype("resources\\fonts\\font.ttf", 60)
        msg = time.strftime("%d.%m.%Y")
        w2, h2 = draw.textsize(msg, font=font)
        draw.text(
            ((width - w2) / 2, ((height - h) / 2 + h) + 20),
            msg,
            (255, 255, 255),
            font=font)

        # Week Day
        days = [
            'Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье'
        ]

        font = ImageFont.truetype("resources\\fonts\\font.otf", 98)
        msg = days[int(time.strftime("%w")) - 1]
        w2, h2 = draw.textsize(msg, font=font)
        draw.text(
            ((width - w2) / 2, ((height - h) / 2 - h2) - 40),
            msg,
            (255, 255, 255),
            font=font)

        # Courses
        try:
            answer = requests.get('https://www.cbr-xml-daily.ru/latest.js')
            if answer.status_code == 200:
                usd = 1/json.loads(answer.content)["rates"]["USD"]
                eur = 1/json.loads(answer.content)["rates"]["EUR"]

                font = ImageFont.truetype("resources\\fonts\\currency.ttf", 64)
                msg = f"$ {int(usd)}"
                w2, h2 = draw.textsize(msg, font=font)
                draw.text(
                    (width / 2 - 350, (height - h2) / 2),
                    msg,
                    (255, 255, 255),
                    font=font)

                msg = f"€ {int(eur)}"
                w2, h2 = draw.textsize(msg, font=font)
                draw.text(
                    (width / 2 - 350, (height - h2) / 2 + h2 + 46),
                    msg,
                    (255, 255, 255),
                    font=font)
        except BaseException:
            pass

        return frame

    def update(self):
        pass
