from flask import Flask, render_template

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page (now using the index.html file)
@app.route('/')
def index():
  return render_template('index.html', url=url)

bot_id = input('Bot id ')
guild_id = input('Guild id ')
redirect_uri = input('Redirect uri ')
url = f'https://discord.com/oauth2/authorize?&client_id={bot_id}&scope=bot&permissions=0&guild_id={guild_id}&response_type=code&redirect_uri={redirect_uri}'

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
