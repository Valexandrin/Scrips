from gtts import gTTS
from art import tprint
import pdfplumber 
from pathlib import Path


def pdf_to_mp3(language='en'):
    text = input('Введи текст: ')
    my_audio = gTTS(text=text, lang=language, slow=False)    
    my_audio.save(f'convert_to_mp3/text.mp3')
    return 'File saved'    
    
    
def main():
    pdf_to_mp3()

if __name__ == '__main__':
    main()
