from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route('/game')
def show_game_form():
    play = request.args.get("wanna_play")
    print play

    if play == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    name = request.args.get('name')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')
    image = request.args.get('image')
    fname = request.args.get('first_name')
    compliment = request.args.getlist('compliment')

    if len(compliment) > 1:
        display_word = ""
        for word in compliment:
            display_word = word + " and " + display_word
    else: 
        display_word = compliment[0]

    libs = ['madlib.html', 'madlib1.html']
    render_choice = choice(libs)
    return render_template(render_choice, name=name, color=color, noun=noun, 
        adjective=adjective, image=image, fname=fname, compliment = compliment, display_word=display_word)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
