import speech_recognition as sr
import webbrowser
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        print("Couldn't recognise your voice what is wrong with you")
    print('You said : {}'.format(text))
    url = 'http://www.google.com/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    tt = text.split()
    small = [x.lower() for x in tt]
    if("chrome" in small):
        webbrowser.get(chrome_path).open(url)
    elif('youtube' in small):
        url = 'http://www.youtube.com'
        webbrowser.get(chrome_path).open(url)
    elif('mail' in small):
        url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
        webbrowser.get(chrome_path).open(url)
    elif('corona' in small):
        url = 'https://www.covid19india.org/'
        webbrowser.get(chrome_path).open(url)
    elif('github' in small):
        url = 'https://github.com/JnaneshD'
        webbrowser.get(chrome_path).open(url)
    elif('whatsapp' in small):
        url = 'https://web.whatsapp.com/'
        webbrowser.get(chrome_path).open(url)
    elif('drive' in small):
        url='https://drive.google.com/drive/shared-with-me'
        webbrowser.get(chrome_path).open(url)
    else:
        pass