import playsound
from gtts import gTTS
from gtts.tokenizer import pre_processors
import gtts

def speak(text) :

    gtts.tokenizer.symbols.SUB_PAIRS.append(
        ('EA.', 'Entered Apprendice')
    )

    tts = gTTS(
        text = text,
        lang="en",
        # tld="co.uk",
        pre_processor_funcs=[
            pre_processors.tone_marks,
            pre_processors.end_of_line,
            pre_processors.abbreviations,
            pre_processors.word_sub
        ]
    )

    filename = "./audios/voice.mp3"
    tts.save(filename)
    # playsound.playsound(filename)