from flask import Flask, render_template, request, send_file
from scripts.yt_downloader import YTDownloader
from io import BytesIO

app = Flask(__name__, static_url_path = '/static')
form_path = "https://www.youtube.com/watch?v=9T6ktFC1n-c&ab_channel=elrubiusOMG"

@app.route('/')
def root():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(port = 8080, debug = True)
