from instascrape import Reel

class InstagramDownloader:
    def download(url: str, session_id: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
            Safari/537.36 Edg/79.0.309.43",
            "cookie": f'sessionid={session_id};',
        }
        reel = Reel(url)
        reel.scrape(headers=headers)
        try:
            reel.download()
        except:
            print('An error occured while downloading the video')
