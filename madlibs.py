from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "<h1>Hi! This is the home page.</h1><a href=\"/hello\">Hello</a>"


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_game_form():
    """Play a game"""

    play_game = request.args.get("game")

    if play_game == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=["GET", "POST"])
def show_madlib():
    """Shows Madlib"""
    
    #names
    a_job = request.form.get("job")

    #adjectives
    adj1 = request.form.getlist("adjective1")
    adj1 = (", ").join(adj1)
    adj2 = request.form.get("adjective2")


    #nouns
    some_noun1 = request.form.get("noun1")
    some_noun2 = request.form.get("noun2")
    some_noun3 = request.form.get("noun3")
    some_noun4 = request.form.get("noun4")

    #verbs
    some_verb1 = request.form.get("verb1")
    some_verb2 = request.form.get("verb2")
    some_verb3 = request.form.get("verb3")

    if request.method == 'POST':
        return render_template('madlib.html', job=a_job, noun=some_noun1, noun_two=some_noun2,
                            noun_three=some_noun3, noun_four=some_noun4, adj=adj1, adj_two=adj2, 
                            verb=some_verb1, verb_two=some_verb2, verb_three=some_verb3)
    elif request.method == 'GET':
        return "get method"



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
