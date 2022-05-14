from flask import Flask, render_template, request
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

ydl_opts = { 
    'format': 'm4a/bestaudio/best',
    'outtmpl': 'songs/%(title)s.%(ext)s',
    'writethumbnail': 'true',
    'postprocessors': [{ 
        'key': 'FFmpegMetadata', 
        'add_metadata': True, 
    }, 
    { 
        'key': 'EmbedThumbnail', 
    }], 
}

@app.route('/download', methods=['GET', 'POST'])
def download():
    url = request.form['url']
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

   
""" <!---
youtube dl code here for now:
yt_dlp -x --audio-format m4a --embed-thumbnail https://www.youtube.com/playlist?list=PLQOu2NmpwnSbx5e2sVTmSqEAz6YFxhnXs --add-metadata -c

-->"""