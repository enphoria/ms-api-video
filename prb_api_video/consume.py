import requests
import json
import logging
import urllib3

class Consume(object):
    def __init__(self, path_video, cellphone):
        self.path_video = path_video
        self.cellphone = cellphone
        self.headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyZjQzM2UwOC0zY2RhLTQ5ZDMtYTQ5My1lMjdhZjViMjZkZDYiLCJ1bmlxdWVfbmFtZSI6Iml0LmVucGhvcmlhQGdtYWlsLmNvbSIsIm5hbWVpZCI6Iml0LmVucGhvcmlhQGdtYWlsLmNvbSIsImVtYWlsIjoiaXQuZW5waG9yaWFAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMDkvMjAyMiAwMToyNTowNCIsImRiX25hbWUiOiI3MTA4IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.1Ri4cr8R0hDaEVjm3JVs4UPTJJE7zo96TA0yDedWMA0"}

    def sendVideo(self):
        endpoint = "https://live-server-7108.wati.io/api/v1/sendSessionFile/"+self.cellphone
        print("send")
        http = urllib3.PoolManager()
        with open("./"+self.path_video, 'rb') as f:
            file_data = f.read()

        
        resp = http.request(
            "POST",
            endpoint,
            headers=self.headers,
            fields= {
            "file": ("video.mp4", file_data),
            }
        )
        print(resp.data.decode("utf-8"))
        
        