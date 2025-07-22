import os
import google_auth_httplib2
import google_auth_oauthlib
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http

def auth_youtube():
    """Authenticate with YouTube API using OAuth2"""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    
    # Use Windows-style path
    client_secret = "client_secret.json"
    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secret,
            scopes=["https://www.googleapis.com/auth/youtube.upload"]
        )
        
        # Specify a port number above 1024 (non-privileged ports)
    credentials = flow.run_local_server()
        
    youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=credentials
        )
    return youtube

def upload_video(youtube):
    request_body = {
        "snippet": {
            "categoryId": 27,
            "description": "This is a guided meditation video.",
            "title": "Guided Meditation Video"
        },
        "status": {
            "privacyStatus": "private"
        }
    }
    
    media_file ="/Users/Rahul/Desktop/shortform_videoGenerator/CosyVoice/output/video.mp4"
    
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=googleapiclient.http.MediaFileUpload(media_file, chunksize=-1, resumable=True)
    )
    
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")
            
        print(f"Upload Complete! Video ID: {response['id']}")
        
if __name__ == "__main__":
    youtube = auth_youtube()
    upload_video(youtube)