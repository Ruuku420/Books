from flask import Flask, request
# import asyncio
import books_utils as bk

app = Flask(__name__)

@app.route("/")
def root():
    return ""

@app.route("/books", methods=['GET', 'POST', 'DEL'])
def books():
    match request.method:
        case 'GET':
            return bk.get_request(request.args)
        case 'POST':
            return bk.post_request(request.args)
        case 'DEL':
            return bk.Del(request.args)
        case _:
            return "Something went really wrong"

if __name__ == '__main__':
    app.run()
