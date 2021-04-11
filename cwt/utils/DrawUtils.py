import os

from PIL import ImageFont


class Font:
    font_name = None
    font_size = 0
    color = "#000000"

    def __init__(self, font_name, font_size=0, font_color="#000000"):
        self.font_name = font_name
        self.font_size = font_size
        self.color = font_color


class Text:
    text = ""
    font = None
    h_align = "left"
    v_align = "middle"

    def __init__(self, text, font, h_align="left", v_align="middle"):
        self.text = text
        self.font = font
        self.h_align = h_align.lower()
        self.v_align = v_align.lower()

    def draw(self, image_draw, canvas_top_left, canvas_bottom_right):
        rootPath = os.path.dirname(__file__)
        if rootPath=="":
            rootPath = "."

        font = ImageFont.truetype(rootPath + "/fonts/%s" % self.font.font_name, self.font.font_size)
        font_width, font_height = image_draw.textsize(self.text, font=font)

        position_x = canvas_top_left[0] + 10
        if self.h_align == "center":
            position_x = round(((canvas_bottom_right[0] - canvas_top_left[0]) - font_width) / 2) + canvas_top_left[0]
        if self.h_align == "right":
            position_x = canvas_bottom_right[0] - font_width - 5

        position_y = round(((canvas_bottom_right[1] - canvas_top_left[1]) - font_height) / 2) + canvas_top_left[1]
        if self.v_align == "top":
            position_y = canvas_top_left[1] + 5
        if self.v_align == "bottom":
            position_y = canvas_bottom_right[1] - font_height - 5

        image_draw.text((position_x, position_y), self.text, font=font, fill=self.font.color)

        #image_draw.rectangle((canvas_top_left, canvas_bottom_right), fill="red")

class Box:
    thick = 1
    color = "#000000"
    bg_color = None

    def __init__(self, thick=1, color="#000000", bg_color=None):
        self.thick = thick
        self.color = color
        self.bg_color = bg_color

    def draw(self, image_draw, top_left, bottom_right):
        rect_start = None
        rect_end = None
        for i in range(self.thick):
            rect_start = (top_left[0] + i, top_left[1] + i)
            rect_end = (bottom_right[0] - 1 - i, bottom_right[1] - 1 - i)
            image_draw.rectangle((rect_start, rect_end), fill=self.bg_color, outline=self.color)
        return (rect_start[0] + 1, rect_start[1] + 1), (rect_end[0] - 1, rect_end[1] - 1)


class Line:
    thick = 1
    color = "#000000"

    def __init__(self, thick=1, color="#000000"):
        self.thick = thick
        self.color = color

    def draw(self, image_draw, start, end):
        image_draw.line((start,end),fill=self.color,width=self.thick)

