import unittest
from unittest import TestCase

from PIL import Image

import cwt.modules.CalendarClass as calC
import cwt.modules.TimeClass as timeC
import cwt.modules.WeatherClass as weatherC
import cwt.modules.SentenceClass as senC

if __name__ == '__main__':
    unittest.main()


class TestFunctions(TestCase):
    def test_calendar(self):
        epaper_calendar = calC.EPaperCalendar()
        epaper_calendar.test()

    def test_time(self):
        epaper_time = timeC.EPaperTime()
        epaper_time.test()

    def test_weather(self):
        epaper_weather = weatherC.EPaperWeather()
        epaper_weather.test()

    def test_sentence(self):
        epaper_sentence = senC.EPaperSentence()
        epaper_sentence.test()

    def test_all(self):
        im = Image.new("RGB", (640, 384), "#FFFFFF")

        im_calendar = Image.new("RGB", (300, 284), "#000000")
        im_sentence = Image.new("RGB", (300, 100), "#000000")
        im_time = Image.new("RGB", (340, 124), "#FFFFFF")
        im_weather = Image.new("RGB", (340, 260), "#FFFFFF")


        calendar = calC.EPaperCalendar()
        calendar.draw(im_calendar,"#FFFFFF")

        time = timeC.EPaperTime()
        time.draw(im_time)

        weather = weatherC.EPaperWeather()
        weather.draw(im_weather)

        sentence = senC.EPaperSentence()
        sentence.draw(im_sentence,"#FFFFFF")

        im.paste(im_calendar,((0,0,im_calendar.width,im_calendar.height)))
        im.paste(im_sentence, ((0, im_calendar.height, im_calendar.width, 384)))
        im.paste(im_time,((im_calendar.width,0,640, im_time.height)))
        im.paste(im_weather,((im_calendar.width,im_time.height,640,384)))


        im.show()