import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
activationWord = 'Lazo' #Lazy :)

#Browser Configuration
#set the path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

#mikrafondan gelen şeyi anlayıp  yazıya çeviriyor ve  yazıdan ses kütüphanesi ile konuşma komutunu gerçekleştiriyor?
def parseCommand():
    listener= sr.Recognizer()
    speak('Komutunu Bekliyorum.')#waiting for command
    print('Komutunu Bekliyorum...')
    with sr.Microphone() as source:
        listener.pause_threshold= 2
        input_speech = listener.listen(source)


    try: 
        speak('Algılanıyor')#Processing... 
        print('Algılanıyor...')
        query = listener.recognize_google(input_speech, language='Tr_TR')#or eng_gb
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('Tam olarak Anlayamadım?')# I did not quite catch that?
        speak('Tam olarak anlayamadım?..')
        print(exception)
        return 'None'
 
    return query
#Ana Döngü
if __name__ == '__main__':
    speak('Merhaba Herkese.')#Hello Everybody
 
    while True:
        # Parse as a list
        query = parseCommand().lower().split()
 
        if query[0] == activationWord:
            query.pop(0)
 
            # List commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Herkese Merhaba.')#Hello Everybody 
                else: 
                    query.pop(0) # Remove say
                    speech = ' '.join(query)
                    speak(speech)
                    
            #Navigasyon
            if query[1] == 'go' and query[0] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)

