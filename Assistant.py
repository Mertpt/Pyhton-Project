# kütüphane ve modüller içe aktarılıyor
import speech_recognition as sr
import webbrowser as web
import pyttsx3
import wikipedia
# Konuşma sentezleyici başlatma fonksiyonuymuş
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Ana fonksiyon
def Ana():
    # Chrome tarayıcısının yolunu ayarladım
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    web.register('chrome', None, web.BackgroundBrowser(chrome_path))

    # Tanıyıcı nesnesi oluşturuluyor
    r = sr.Recognizer()

    # Ses tanıma döngüsü
    while True:
        with sr.Microphone() as source:
            # Arka plan gürültüsüne göre mikrofon hassasiyetini ayarlama beceremedim :(
            r.energy_threshold = 4000
            r.adjust_for_ambient_noise(source, duration=1)
            print("Bir şeyler söyle... (Çıkmak için 'kapat' diyebilirsiniz)")

            try:
                # Kullanıcıdan ses almasını sağlıyor.
                audio = r.listen(source)
                print("Algılıyorum, lütfen bekleyin...")

                # Sesi metne çevirmek için
                hedef = r.recognize_google(audio, language='tr_TR').lower()
                print("Şunu dediniz: " + hedef)

                # Kapatma kontrolü
                if hedef == "kapat":
                    print("Program kapatılıyor...")
                    SpeakText("Program kapatılıyor. Hoşça kalın!")
                    break  # Döngüyü sonlandırır
                
                # Web tarayıcısı açmak için
                SpeakText("Hedefiniz aciliyor.")
                web.get('chrome').open(f"https://www.google.com/search?q={hedef}")
            
            except sr.UnknownValueError:
                # Algılanamayan giriş durumunda
                print("Tam olarak algılayamadım. Lütfen tekrar deneyin.")
                SpeakText("Ne dediğinizi anlayamadım. Tekrar söyleyin.")
            
            except sr.RequestError as e:
                # Google hizmetlerine ulaşılamadığı durum
                print("Hizmete erişilemiyor. Hata: {0}".format(e))
                SpeakText("Google hizmetine şu anda erişilemiyor.")
            
            except Exception as e:
                # Diğer hatalar?
                print("Bir hata oluştu: " + str(e))
                SpeakText("Bir hata meydana geldi.")

if __name__ == "__main__":
    Ana()
