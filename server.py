from flask import Flask, session, redirect, request, render_template
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

def randomNum(start, end):
    num = random.randrange(start, end)
    return num

def earnings():
    chance = randomNum(0, 2)
    if chance == 1:
        return True
    else:
        return False

def addNew(num, action, selection):
    currentTime = datetime.datetime.now()
    if selection == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, currentTime)
            session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %d gold... Ouch %s' % (num, currentTime)
            session['activity'].append(['lost', lost])
        else:
            print "Not working"
    elif selection == 'farm':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, selection, currentTime)])
    elif selection == 'cave':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, selection, currentTime)])
    elif selection == 'house':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, selection, currentTime)])
    else:
        print "Not working"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def money():
    hiddenInput = request.form['hidden']
    if hiddenInput == 'farm':
        farmNum = randomNum(10, 21)
        session['goldCount'] += farmNum
        addNew(farmNum, 'earned', 'farm')
    elif hiddenInput == 'cave':
        caveNum = randomNum(5, 10)
        session['goldCount'] += caveNum
        addNew(caveNum, 'earned', 'cave')
    elif hiddenInput == 'house':
        houseNum = randomNum(2, 5)
        session['goldCount'] += houseNum
        addNew(houseNum, 'earned', 'house')
    elif hiddenInput == 'casino':
        casinoNum = randomNum(0, 50)
        chance = earnings()
        if chance == True:
            session['goldCount'] += casinoNum
            addNew(casinoNum, 'earned', 'casino')
        elif chance == False:
            session['goldCount'] -= casinoNum
            addNew(casinoNum, 'lost', 'casino')
        else:
            print "Not working"
    else:
        print "Not working"
    return redirect('/')

app.run(debug=True)