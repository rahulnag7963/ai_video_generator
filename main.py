import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from shortForm import shortForm
from picture import picture
from movie import movie
from script import script
from voice import voice


def main(): 
    text= shortForm(script)
    picture(text)
    voice(text)
    images = ['image1.png']

    output_dir = "output"
    output_video = output_dir+"video.mp4"
    movie(images, output_video)


main()