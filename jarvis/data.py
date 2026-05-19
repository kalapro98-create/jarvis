import json
class Save:
    users = {
    "open": {
        "youtube": "https://www.youtube.com",
        "telegram": "https://web.telegram.org",
        "google":"https://www.google.com/",
        "instagram":"https://www.instagram.com/",
        "ai": "https://chatgpt.com",
        "wikipedia": "https://www.wikipedia.org/",
        "whatsapp":"https://web.whatsapp.com/"
    },
    "calculate":{
        "multiply":"*",
        "plus": "+",
        "add":"+",
        "divide":"/",
        "minus": "-",
        "reduce":'-'
    },
    "app":{
        "steam":"C:/Users/Public/Desktop/Steam.lnk",
        "vs": "C:/Users/kerbe/OneDrive/Desktop/Visual Studio Code.lnk",
        "minecraft":"C:/Users/Public/Desktop/TLauncher.lnk",
        "edit":"C:/Users/kerbe/OneDrive/Desktop/CapCut.lnk",
        "discord": "C:/Users/kerbe/OneDrive/Desktop/Discord.lnk"
    }
}

with open("data.json", "w") as file:
    json.dump(Save.users, file, indent=4)