from flask import Flask, render_template

app = Flask(__name__)

# Define a route that renders your HTML template and passes the image URL
@app.route('/')
def home():
    background_image_url = '/static/anime.jpg'  # Update the path accordingly
    return render_template('index.html', background_image_url=background_image_url)

if __name__ == '__main__':
    app.run(debug=True)
