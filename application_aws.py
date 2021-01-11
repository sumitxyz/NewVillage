from flask import Flask, render_template

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

header_text = '''
    <html>\n<head> <title>The NewVillage | 2021 Version</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back Home</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
app = Flask(__name__)

# add a rule for the index page.
app.add_url_rule('/', 'index_old', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site URL.
app.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

@app.route('/')
def index():
    return ('Hello')
    return render_template('index.html')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be removed before deploying a production app.
    app.debug = True
    app.run()