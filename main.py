from flask import Flask, render_template
import parsing

app = Flask(__name__)
parsing.anonse()
parsing.freebies()
parsing.release()
parsing.rumors()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu.html')
def menu():
    return render_template('menu.html')


@app.route('/news1.html')
def news1():
    with open("anonse.txt", "rt") as f:
        news_list = (f.read().split('\n'))

    return render_template('news1.html', news=news_list)


@app.route('/news2.html')
def news2():
    with open("release.txt", "rt") as f:
        news_list = (f.read().split('\n'))

    return render_template('news2.html', news=news_list)


@app.route('/news3.html')
def news3():
    with open("freebies.txt", "rt") as f:
        news_list = (f.read().split('\n'))

    return render_template('news3.html', news=news_list)


@app.route('/news4.html')
def news4():
    with open("rumors.txt", "rt") as f:
        news_list = (f.read().split('\n'))

    return render_template('news4.html', news=news_list)


@app.route('/anonse.html')
def anonse_html():
    return render_template('anonse.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
