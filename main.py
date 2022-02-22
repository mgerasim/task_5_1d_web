from flask import Flask, request, render_template

app = Flask(__name__)

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def index_post():
    device_title = request.form['device_title']
    device_property = request.form['device_property']

    return london_co[device_title][device_property]


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')
