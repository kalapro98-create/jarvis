from datetime import datetime
import webbrowser
import json
import re
from voice import Listen,Voice
from music import play_youtube_audio, stop_music, is_music_playing
import os
import urllib.parse
import pyautogui
class Use(Listen):
    def __init__(self):
        super().__init__()
    def load_data(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        return data
    def open_site(self, text, data):
        if "open" in text:
            for site in data["open"]:
                if site in text:
                    link = data["open"][site]
                    Voice.say("opening " + site)
                    webbrowser.open(link)
                    return True
            return False
    def save_sth(self,text):
        if "save" in text:
            Voice.say("what i should save?")
            text2 = self.lis()
            if text2 != "":
                now = datetime.now()
                with open("save_data.txt", "a") as file:
                    file.write(str(now) + " - " + text2 + "\n")
                Voice.say("text saved")
                return True
        return False
    def mathematics(self, text, data):
        word_numbers = {
            "zero": 0,"one": 1,"two": 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9,"ten": 10
        }
        numbers=[]
        digit_numbers = re.findall(r"\d+", text)
        for n in digit_numbers:
            numbers.append(float(n))
        words = text.split()
        for word in words:
            if word in word_numbers:
                numbers.append(float(word_numbers[word]))
        if len(numbers) < 2:
            return False
        num1 = numbers[0]
        num2 = numbers[1]
        for act in data["calculate"]:
            if act in text:
                sign = data["calculate"][act]
                if sign == "+":result = num1 + num2
                elif sign == "-":result = num1 - num2
                elif sign == "*":result = num1 * num2
                elif sign == "/":
                    if num2 == 0:
                        Voice.say("cannot divide by zero")
                        return True
                    result = num1 / num2
                print("result:", result)
                Voice.say("result is " + str(result))
                return True
        return False 
    def open_music(self, text):
        music_commands = ["turn on the music","play music","open music","start music"]
        stop_music_commands = ["stop music","turn off music","close music"]
        for command in stop_music_commands:
            if command in text:
                stop_music()
                Voice.say("music stopped")
                return True
        for command in music_commands:
            if command in text:
                Voice.say("please say music name")
                name = self.lis()
                if name != "":
                    Voice.say("playing " + name)
                    play_youtube_audio(name)
                    while is_music_playing():
                        only_stop = self.lis()
                        if "stop music" in only_stop or "turn off music" in only_stop or "close music" in only_stop:
                            stop_music()
                            Voice.say("music stopped")
                            return True
                        if "stop all work" in only_stop:
                            stop_music()
                            Voice.say("Goodbye")
                            exit()
                    return True
                else:
                    Voice.say("music name not found")
                    return True
        return False
    def open_google(self, text):
        choice=["find information in google","find in google","search"]
        for command in choice:
            if command in text:
                Voice.say("what should i find")
                text9 = self.lis()
                if text9 == "":
                    Voice.say("I did not hear what to search")
                    return True
                url = "https://www.google.com/search?q=" + urllib.parse.quote(text9)
                webbrowser.open(url)
                Voice.say("Searching " + text9)
                return True
        return False
    def time(self,text):
        ktime=["what time","tell me tame","what time is it","time"]
        kdate=["tell me about date","what date","current date","today date"]
        now = datetime.now()
        for i in ktime:
            if i in text:
                Voice.say(f"Current time is {now.hour}:{now.minute}")
                return True
        for j in kdate:
            if j in text:
                 Voice.say("Current date is"+str(now.date()))
                 return True
        return False
    def saf_answer(self,question,answer,time):
        with open("answer.txt","a") as f:
            f.write(question + " - " + answer + " - " + str(time) + "\n")
    def com_control(self,text):
        words=["shut down computer","restart computer","lock computer"]
        for  i in words:
            if i in text:
                if "shut down computer" in text:
                    Voice.say("Are you sure? ")
                    text1=self.lis()
                    now = datetime.now()
                    self.saf_answer("shut down computer",text1,now)
                    if "yes" in text1:
                        os.system("shutdown /s /t 1")
                        return True
                    else:Voice.say("cancelled")
                elif "restart computer" in text:
                    Voice.say("Are you sure? ")
                    text1=self.lis()
                    now = datetime.now()
                    self.saf_answer("restart computer",text1,now)
                    if "yes" in text1:
                        os.system("shutdown /r /t 1")
                        return True
                    else:Voice.say("cancelled")
                elif "lock computer" in text:
                    Voice.say("Are you sure? ")
                    text1=self.lis()
                    now = datetime.now()
                    self.saf_answer("lock computer",text1,now)
                    if "yes" in text1:
                        os.system("rundll32.exe user32.dll,LockWorkStation")
                        return True
                    else:Voice.say("cancelled")
                else: return False
    def find_youtube(self,text):
        words=["find video in youtube","find video","find channel"]
        for i in words:
            if i in text:
                Voice.say("which video do you want to find? ")
                text1=self.lis()
                if text1=="":
                    Voice.say("I did not hear what to search")
                    return True
                if text1 !="":
                    query = urllib.parse.quote(text1)
                    link="https://www.youtube.com/results?search_query=" + query
                    webbrowser.open(link)
                    return True
                return False
    def app(self,text,data):
            if "app" in text:
                Voice.say("which app i should open? ")
                text1=self.lis()
                text1=text1.lower()
                if text1=="":
                    Voice.say("i didn't hear nothing")
                    return True
                if "app" not in data:
                    Voice.say("app list not found in data file")
                    return True
                for app in data["app"]:
                    if app in text1:
                        link=data["app"][app]
                        Voice.say("opening"+app)
                        webbrowser.open(link)
                        return True
                Voice.say("i do not know this app")
                return True
            return False 
    def screen(self,text):
        if "screenshot"in text or"take screenshot" in text:
            screenshot = pyautogui.screenshot()
            desktop = r"C:\Users\kerbe\OneDrive\Desktop"
            now = datetime.now()
            file_name = f"screenshot_{now.hour}_{now.minute}_{now.second}.png"
            file_path = os.path.join(desktop, file_name)
            screenshot.save(file_path)
            Voice.say("Screenshot saved")
            return True
        return False