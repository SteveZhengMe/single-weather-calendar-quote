import os
import random
import re
import time

from PIL import ImageDraw, Image

from cwt.utils.DrawUtils import Text, Font

SENTENCE_FILE_FULLPATH = "sentence.txt"
temp_sentence_path = "temp_sentence.txt"

class EPaperSentence:
    def __init__(self):
        pass

    def check_reload(self):
        current_time = time.localtime(time.time())
        minute_string = time.strftime('%M', current_time)
        hour_string = time.strftime('%H', current_time)
        return int(minute_string) == 0 and (int(hour_string) == 8 or int(hour_string) == 12 or int(hour_string) == 16 or int(hour_string) == 20)

    def draw(self, target_canvas, font_color="#000000"):
        sen = self.pick_one_sentence()
        sen_final, sen_size = self.format_sentence(sen)
        img_draw = ImageDraw.Draw(target_canvas)
        text = Text(sen_final, Font("simkai.ttf", sen_size, font_color), "left")

        text.draw(img_draw, (0, 0), (target_canvas.width, target_canvas.height))

    def pick_one_sentence(self):
        sentence = ""
        if self.check_reload() or not os.access(temp_sentence_path, os.R_OK):
            if os.access(SENTENCE_FILE_FULLPATH, os.R_OK):
                with open(SENTENCE_FILE_FULLPATH,"r") as f:
                    sentence = random.choice(f.readlines())
                if sentence != "":
                    with open(temp_sentence_path, "wt") as f:
                        f.write(sentence)
        else:
            with open(temp_sentence_path, "r") as f:
                sentence = "".join(f.readlines())

        return sentence

    def format_sentence(self, sen):
        sen = sen.replace("\n","")
        sen = sen[0:36]
        if len(sen) > 24:
            sen = sen[0:12] + "\n" + sen[12:24] + "\n" + sen[24:]
            return sen, 22
        elif len(sen) <= 24 and len(sen) > 12:
            sen = sen[0:10] + "\n" + sen[10:20] + "\n" + sen[20:]
            return sen, 26
        elif len(sen) <= 12:
            sen = sen[0:8] + "\n" + sen[8:]
            return sen, 32


    def test(self):
        im = Image.new("RGB", (300, 100), "#000000")
        self.draw(im, "#FFFFFF")
        im.show()
