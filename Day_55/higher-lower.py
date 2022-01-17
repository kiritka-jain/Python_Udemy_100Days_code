from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(1, 9)
print(random_num)


@app.route("/")
def number():
    return "<h1>Guess a number between 0 and 9</h1><br>" \
           "<img src='https://media2.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid" \
           "=ecf05e47q4s1atkhzqrdgqggszg0nqgnmvc2ndrvmyf0t4yq&rid=200w.webp&ct=g' alt='number giphy'> "


@app.route("/<guessed_number>")
def guess_num(guessed_number):
    if int(guessed_number) > random_num:
        return "<h1 style='color: purple'>Too high,Try Again!</h1><br>" \
               "<img src='https://media4.giphy.com/media/iChaipiCKxpHbYan4k/giphy.gif' alt='number giphy'> "
    elif int(guessed_number) < random_num:
        return "<h1 style='color: red'>Too Low,Try Again!</h1><br>" \
               "<img src='https://media3.giphy.com/media/p3hishj1R7SqONbXoQ/giphy.gif?cid" \
               "=ecf05e47bqah8q2ac9t3ybe2k2l5nr8c217hp1gzcmtj0yny&rid=giphy.gif&ct=g' alt='too low giphy'> "
    else:
        return "<h1 style='color: green'>You guessed it right.</h1><br>" \
               "<img src='https://media3.giphy.com/media/Q66ZEIpjEQddUOOKGW/giphy.gif' alt='well done giphy'> "


if __name__ == '__main__':
    app.run(debug= True)
