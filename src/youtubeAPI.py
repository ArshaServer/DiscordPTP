import os

from dotenv import load_dotenv
from googleapiclient.discovery import build


class YouTubeHandler:
    service = build
    def __init__(self):
        load_dotenv()
        self.service = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_KEY'))

    def petThePeepo(self):
        request = self.service.videos().list(
            part='statistics',
            id="ll2Au3CdV2k"
        )
        response = request.execute()
        return 'pet the peepo view: ' + response['items'][0]['statistics']['viewCount']

