from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__)
 
# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")
bot = ChatBot("HealthBot")

convo = [
    'hello',
    'hi sir let me ask you something,what is your name ?',
    'what is your age ?',
    'what is your address ?',
    'can i get your order sir ?',
    'yes',
    'what product would you like to buy',
    'ok fine sir, i noted your order',
    'thank you',
    'your welcome sir'

]

trainer = ListTrainer(bot)
trainer.train(convo)

data={
    "name":"",
    "age":"",
    "add":"",
    "sex":"",
    "product":""
}

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if(userText.find("name")!=-1):
        data["name"]=userText
    if(userText.find("age")!=-1):
        data["age"]=userText
    if(userText.find("male")!=-1 or userText.find("female")!=-1):
        data["sex"]=userText
    if(userText.find("address")!=-1):
        data["add"]=userText
    if(userText.find("buy")!=-1):
        data["product"]=userText

    print(data)
    return str(bot.get_response(userText))
 
 
if __name__ == "__main__":
    app.run()