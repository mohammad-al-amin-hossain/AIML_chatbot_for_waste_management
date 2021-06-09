import aiml
from flask import Flask
from flask import render_template
import os

kernel = aiml.Kernel()

#from datetime import datetime
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S:%f")
#now2 = datetime.now()
#current_time2 = now2.strftime("%H:%M:%S:%f")



#kernel.learn("std-startup.xml")
#kernel.respond("load aiml b")

#while True:

#    input_text = input(">Human: ")
#    print("First Time =", current_time)
#    response = kernel.respond(input_text)
#    print(">Bot: "+response)
#    print("Reply Time =", current_time2)


for filename in os.listdir("brain"):
	if filename.endswith(".aiml"):
		kernel.learn("brain/" + filename)

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/<query>")
def api(query):
	return kernel.respond(query)


if __name__ == "__main__":
	app.run()