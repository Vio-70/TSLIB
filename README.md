# ffmpeg-conversion-server
This is a script for using ffmpeg to convert files to mp4s.

To host the api type in the terminal 
`uvicorn main:app --host 127.0.0.0`

to convert, convert your starting file path to base 64.
then put it into a link
http://127.0.0.0/media/{Base64}

Then it should output a video
