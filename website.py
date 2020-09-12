from flask import Flask, render_template, url_for , request
import requests
from bs4 import BeautifulSoup as BS

app=Flask(__name__,template_folder='templatess')

strin1='https://www.collegedata.com/college/'
strin2='/?tab=profile-money-tab'
# response=requests.get('https://www.collegedata.com/college/University-of-Houston/?tab=profile-money-tab')
# soup=BS(response.content,'lxml')
#
# r=soup.findAll('dd')
# #
# l=[]
# for pos, i in enumerate(r):
#     if pos >=0 and pos <=4:
#         print(i)
#         if pos==0 or pos==1:
#             k=str(i).split('<br/>')
#             l.append(k[0].strip('<dd>'))
#             l.append(k[1].strip('<dd>'))
#
#         else:
#             l.append(str(i).strip('<dd>').strip('</dd>'))
#
# print(l)




@app.route('/', methods=['GET', 'POST'])
def home():


    if request.method == 'POST':
        data1=request.form['15']
        data2=request.form['20']
        data3=request.form['35']
        data4=request.form['50']

        print(data1,data2)
        return render_template('invest_2.html')
    return render_template('invest_2.html')


@app.route('/collegeinfo', methods=['GET','POST'])
def collegeinfo():

    if request.method == 'POST':
        data1 = request.form['user_name']
        data1=data1.replace(' ','-')
        full=strin1+data1+strin2
        response = requests.get(str(full))
        soup = BS(response.content, 'lxml')

        r = soup.findAll('dd')
        #
        l = []
        for pos, i in enumerate(r):
            if pos >= 0 and pos <= 4:
                print(i)
                if pos == 0:
                    k = str(i).split('<br/>')
                    l.append('Cost of attendence ' + k[0].strip('<dd>'))
                    l.append(k[1].strip('<dd>'))
                elif pos == 1:
                    k = str(i).split('<br/>')
                    l.append('Tuition and Fees ' + k[0].strip('<dd>'))
                    l.append(k[1].strip('<dd>'))

                elif pos ==2:
                    l.append('Room and Board ' + str(i).strip('<dd>').strip('</dd>'))
                elif pos ==3:
                    l.append('Books and supplies ' + str(i).strip('<dd>').strip('</dd>'))
                elif pos ==4:
                    l.append('Other expenses ' + str(i).strip('<dd>').strip('</dd>'))

        print(l)


        return render_template('index.html',data=l)
    return render_template('login.html')



if __name__=='__main__':
    app.run(debug=True)