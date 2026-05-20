from function import Use 
from voice import Voice
class work(Use):
    def do_command(self,text):
        data = self.load_data()
        if self.open_site(text, data):
            return
        if self.give_info(text):
            return
        if self.mathematics(text, data):
            return
        if self.save_sth(text):
            return
        if self.open_music(text):
            return
        if self.time(text):
            return
        if self.com_control(text):
            return
        if self.find_youtube(text):
            return
        if self.app(text,data):
            return
        if self.screen(text):
            return
        if self.find_channel(text):
            return
    def run(self):
        while True:
            textj=self.lis()
            if "stop all work" in textj:
                Voice.say("Goodbye")
                break
            if "jarvis" in textj:
                Voice.say("Systems online, sir")
                while True:
                    command=self.lis()
                    if "pause" in command:
                        Voice.say("Ok i will wait")
                        break
                    self.do_command(command)
                    if "stop all work" in command:
                        Voice.say("Goodbye")
                        return
u=work()
u.run()