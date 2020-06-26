# cabin-sunset
We have a little cabin on a lake looking west which has beautiful views of the sunset every night. I have a Raspberry Pi 4 with the V2 Camera module attached to it looking out the cabin windows at the lake. 

I put together these scripts that will:
- Start a video stream that I can view in a web browser any time I'd like.
- Near sunset the script will stop the video stream and take a series of timestamped pictures

# Requirements
- Python 3 (Tested on 3.7.3)
- Raspberry Pi OS 

# Installation

```
pip install -r requirements.txt

```

Or maybe pip3 depending on your system.

Near the top of the file input your city name, timezone, latitude, and longitude.
 I'm using astral to get the sunset times.  More information on usage is here: https://astral.readthedocs.io/en/latest/index.html

# To Do
- Upload daily pictures to AWS S3
- Cron to reschedule every day
