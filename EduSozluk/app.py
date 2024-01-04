from flask import Flask, render_template

app = Flask('app')

basliklar = [{
    'id': 1,
    'baslik': '2024yili',
    'yazilar': ['hosgeldin', 'yeniYil', 'noel']
}, {
    'id': 2,
    'baslik': 'süperKupa',
    'yazilar': ['gs', 'fb', 'Atatürk']
}, {
    'id': 3,
    'baslik': 'asgariUcret',
    'yazilar': ['2tl', 'zam', 'aclikSiniri']
}]


@app.route('/')
def home_page():
    return render_template('index.html', basliklar=basliklar)


@app.route('/baslik/<baslik_id>')
def baslik_goster(baslik_id):
    baslik = ""
    yazilar = []
    for b in basliklar:
        if b["id"] == int(baslik_id):
            baslik = b["baslik"]
            yazilar = b["yazilar"]

    return render_template("baslik.html", baslik=baslik, yazilar=yazilar)


app.run(debug=True, host='0.0.0.0', port=5000)