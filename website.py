from flask import Flask, render_template, url_for , request

app=Flask(__name__,template_folder='templatess')



@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        data=request.form['user_name']

        print(data)
        return render_template('login.html')
    return render_template('login.html')





if __name__=='__main__':
    app.run(debug=True)