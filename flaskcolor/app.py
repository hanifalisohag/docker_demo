import os
from flask import Flask,render_template
app=Flask(__name__)

# color="blue"
color=os.environ.get('APP_COLOR')

@app.route("/")
def main():
    print(color)
    # print(os.environ)
    return render_template("index.html",color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="8080")