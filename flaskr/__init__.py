from flask import Flask, render_template, request, send_file, jsonify
from scripts.yt_downloader import YTDownloader
from io import BytesIO
from scripts.instagram_downloader import InstagramDownloader

app = Flask(__name__, static_url_path = '/static')
form_path = "https://www.youtube.com/watch?v=9T6ktFC1n-c&ab_channel=elrubiusOMG"

########## MAIN ##########
@app.route('/')
def root():
    return render_template('index.html')

########## YouTube DOWNLOAD ##########
@app.route('/download/yt', methods = ['POST', 'GET'])
def yt_download():
    form_path: str = request.form['yt_url']
    dic: dict = YTDownloader.get_yt_info(form_path)
    if dic is None:
        return render_template('yt-download.html')
    
    return render_template(
        'yt-download.html', 
        title = dic['title'], 
        thumbnail = dic['thumbnail'],
        url = form_path
    )

@app.route('/file/yt', methods = ['GET'])
def yt_file():
    buffer: BytesIO = YTDownloader.get_video_buffer(form_path)
    yt_title: str = YTDownloader.get_video_title(form_path)
    return send_file(buffer, download_name = yt_title + '.mp4', as_attachment = True, mimetype = 'video/mp4')

@app.route('/file/yt/info', methods = ['GET'])
def yt_file_info():
    dic: dict = YTDownloader.get_yt_info(form_path)
    json = jsonify(dic)
    return json

########## TWITTER DOWNLOAD ##########
@app.route("/download/twitter")
def twitter_download():
    return render_template('twitter-download.html')

########## INSTAGRAM DOWNLOAD ##########
@app.route("/download/instagram", methods = ['POST', 'GET'])
def instagram_download():
    form_url: str = request.form['instagram_url']
    InstagramDownloader().download(form_url, session_id='')
    return render_template('instagram-download.html')

if __name__ == '__main__':
    app.run(port = 8080, debug = True)
