"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json

swear_jar = ['fuck', 'shit', 'cunt']

# def check_input(input):
#     return input


def check_for_swears(input):
    if any(word in input for word in swear_jar):
        return True


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    split_user_message = user_message.split()
    if check_for_swears(split_user_message):
        return json.dumps({"animation": "afraid", "msg": "place a nickle in the swear jar, young man"})
    return json.dumps({"animation": "inlove", "msg": user_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
