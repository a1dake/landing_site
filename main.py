from flask import Flask, render_template
from database.database import search_data
from database.feedback import feedbacks
from googleapiclient.discovery import build
from config import API_KEY

app = Flask(__name__)
goods = search_data()

def get_video():
    #youtube = build('youtube', 'v3', developerKey=API_KEY)
    video_id = 'Kemo3dxMUOk'
    video_url = f'https://www.youtube.com/embed/{video_id}'
    return video_url

video_url = get_video()

@app.route("/")
def main_site():
    return render_template('main.html', feedbacks=feedbacks, goods=goods, video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)