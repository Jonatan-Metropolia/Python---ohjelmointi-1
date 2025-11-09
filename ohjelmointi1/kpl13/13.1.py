
from flask import Flask

app = Flask(__name__)
@app.route('/prime/<luku>')
def prime(luku):
    intluku = int(luku)

    for i in range(2, intluku):
        if intluku%i == 0:
            isprime = False
            break
        else:
            isprime = True

    vastaus = {
        "Number": intluku,
        "isPrime": isprime
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

