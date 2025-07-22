# AI Video Generator

Created a personal AI video generator that uses Groq, StabilityAI, CosyVoice and MoviePy to automate the entire video making process This inlcudes:
- Script making
- Text to image generation
- Text to voice generation
- Compiling text, audio and images together

##Purpose
My goal was to automate guided mediation videos, however the framework has been used to create short form content, longform videos, etc. I would highly recomend looking through the movie.py docs (https://zulko.github.io/moviepy/) to customize the script towards your own liking in moive.py (where most of the logic for creating content exists).

## Requirements:
1.) This video requires CozyVoice, so ensure that you go to the cozyvoice github and follow the steps there to get it running:
https://github.com/FunAudioLLM/CosyVoice

2.) This model also uses Stability AI so make sure ot folow how to set it up here:
https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0

3.) When installing dpeendencies, (dependecies should be listed above, and ensure to install moviepy and groq along with the ones stated above) ensure that you install the depencdencies for StabilityAi OUTSIDE the foloder of CozyVoice, as the dependencies do clash, causing unintended issues.

4.) This also requires Groq where you must create your own API key to run the model on.


## How to run
1.) cd into CozyVoice
2.) in terminal type: pytohn main.py
3.) Wait roughly 5-10 minutes (depending on length of script)
4.) Go to file Output to see finaly result

##Limitations
1.) Video generation currently can only generate pictures for videos. No full short clips for projects can be made
2.) The AI mode being used by Groq (llama3-8b-8192) may not always give you the best script. If considering making the videos better, consider here as a starting point by using a better model for script automation (in picture.py and shortForm.py). 
3.) Voice generation has its limitations. While the voice generated is not bad and can clone other voices (see cozy voice on how to do this) it still is not to the level of something like eleven labs. Using eleven labs woul also greatly improve the quality (update in voice.py).


