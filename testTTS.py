from gtts import gTTS
import os
tts = gTTS(text="Good morntingggggg", lang='en')
tts.save("good.mp3")
#os.system("mpg321 good.mp3")
