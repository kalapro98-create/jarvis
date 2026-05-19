import speech_recognition as sr
import edge_tts
import asyncio
import pygame
import os
class Voice:
    VOICE = "en-US-AndrewNeural"
    @staticmethod
    async def speak(text):
        file = "voice.mp3"
        try:
            tts = edge_tts.Communicate(
                text,Voice.VOICE,rate="-10%",pitch="-5Hz",volume="+10%"
            )
            await tts.save(file)
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.unload()
            pygame.mixer.quit()
            if os.path.exists(file):
                os.remove(file)
        except Exception as e:
            print("Speech error:", e)
    @staticmethod
    def say(text):
        asyncio.run(Voice.speak(text))
class Listen:
   def lis(self):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        print("Speak...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source,timeout=10,phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected")
            return ""
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("I don't understand")
        return ""