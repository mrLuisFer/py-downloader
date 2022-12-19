from pytube import YouTube, Stream
from io import BytesIO

class YTDownloader:
    def download_local_video(url: str) -> dict:
        yt: YouTube = YouTube(url)
        stream: Stream = yt.streams.get_highest_resolution()
        try:
            d = dict()
            d['yt'] = yt
            d['stream'] = stream
            stream.download()
            return d
        except:
            print('An error occured while downloading the video')
            
    def get_yt_info(url: str) -> dict:
        yt: YouTube = YouTube(url)
        dic: dict = dict()
        try:
            dic['title'] = yt.title
            dic['thumbnail'] = yt.thumbnail_url
            return dic
        except:
            return None

    def get_stream(url: str) -> Stream:
        yt: YouTube = YouTube(url)
        try:
            stream: Stream = yt.streams.get_highest_resolution()
            return stream
        except:
            print('An error occured while getting the stream')
            return None
    
    def get_video_title(url: str) -> str:
        yt: YouTube = YouTube(url)
        try:
            return yt.title
        except:
            print("An error occured while getting the video's title")
            return ""
    
    def get_video_buffer(url: str) -> BytesIO:
        buffer = BytesIO()
        yt_stream: Stream = YTDownloader.get_stream(url)
        try:
            yt_stream.stream_to_buffer(buffer)
            buffer.seek(0)
            return buffer
        except:
            print('An error occured while getting the video buffer')
            return buffer
