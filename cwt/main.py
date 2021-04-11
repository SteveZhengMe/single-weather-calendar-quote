import traceback

from PIL import Image, ImageDraw

from cwt.modules.CalendarClass import EPaperCalendar
from cwt.modules.TimeClass import EPaperTime
from cwt.modules.WeatherClass import EPaperWeather
from cwt.modules.SentenceClass import EPaperSentence
from cwt.utils.DrawUtils import Line

from cwt.waveshare import epd7in5


def generate_im():
    im = Image.new("RGB", (640, 384), "#FFFFFF")

    im_calendar = Image.new("RGB", (300, 284), "#000000")
    im_sentence = Image.new("RGB", (300, 99), "#000000")
    im_time = Image.new("RGB", (340, 124), "#FFFFFF")
    im_weather = Image.new("RGB", (340, 260), "#FFFFFF")

    calendar = EPaperCalendar()
    calendar.draw(im_calendar, "#FFFFFF")

    time = EPaperTime()
    time.draw(im_time)

    weather = EPaperWeather()
    weather.draw(im_weather)

    sentence = EPaperSentence()
    sentence.draw(im_sentence, "#FFFFFF")

    im.paste(im_calendar, (0, 0, im_calendar.width, im_calendar.height))
    im.paste(im_sentence, (0, im_calendar.height + 1, im_calendar.width, 384))
    im.paste(im_time, (im_calendar.width, 0, 640, im_time.height))
    im.paste(im_weather, (im_calendar.width, im_time.height, 640, 384))

    line = Line(thick=2, color="#000000")
    line.draw(ImageDraw.Draw(im), (im_calendar.width, im_time.height + 20), (640, im_time.height + 20)),

    return im


def darken_image(the_img):
    result_img = the_img.convert('L')
    pixels = result_img.load()
    for x in range(result_img.width):
        for y in range(result_img.height):
            if pixels[x, y] > 210:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return result_img


def run():
    try:
        im = generate_im()

        # im.show()
        epd = epd7in5.EPD()
        epd.init()
        buffer = epd.getbuffer(im)
        epd.Clear(0xFF)
        epd.display(buffer)
        epd.sleep()
    except:
        print('traceback.format_exc():\n%s', traceback.format_exc())
        exit()


if __name__ == '__main__':
    run()
