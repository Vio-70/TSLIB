import ffmpeg

import os

from urllib.request import urlretrieve

import random

from fastapi import FastAPI

from fastapi.responses import FileResponse

import base64

import subprocess

from fastapi.middleware.cors import CORSMiddleware

#check if you have ffmpeg on system path it ffmpeg reports missing files make sure to reset project too

app = FastAPI()

origins = [
    "https://wellwornnimblecode.nathanielnvi0fl.repl.co",
    "https://wellwornnimblecode.nathanielnvi0fl.repl.co:8080",
    "0.0.0.0:8080",
    "0.0.0.0",
    "https://studio.penguinmod.site",
    "tw-editor://.",
    "https://app.zerossl.com",
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nothing = ""

def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg"
        "-i", input_file,
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted")
    except subprocess.CalledProcessError as e:
        print("Conversion failed!")

def convert_to_list(var):
    i = 0
    ans = []
    for i in var:
        ans.append(i)
    return ans
def list_convert_to_string(var):
    i = 0
    ans = ""
    for i in var:
        ans = ans + i
    return ans

@app.get("/.well-known/pki-validation/AAEB1CA985B498A47BA588B654DB2F0F.txt")
def other():
    return FileResponse("AAEB1CA985B498A47BA588B654DB2F0F.txt")
@app.get("/hi")
def hello():
    return {"Hello": "World"}

@app.post("/")
def hello_post():
    return {"Success": "You Posted!"}


@app.get("/media/{file}")
def something(file):
    base64_string = base64.b64decode(file)
    base64_string = str(base64_string)
    base64_string = convert_to_list(base64_string)
    base64_string[0] = ''
    base64_string[1] = ''
    base64_string[0] = ''
    base64_string[len(base64_string) - 1] = ''
    base64_string[len(base64_string) - 1] = ''
    base64_string = list_convert_to_string(base64_string)
    file_name = f'output_{file}_{random.randint(1,99999)}.mp4'
    print(base64_string)
    if True:
        #(
        #    ffmpeg
        #    .input(base64_string)
        #    .output(file_name)
        #    .run()
        #)
        otherfilename = file_name+"e.ts"
        urlretrieve(base64_string, otherfilename)
        command = f"ffmpeg -i C:/Users/viofi/PycharmProjects/pythonProject1/{otherfilename} C:/Users/viofi/PycharmProjects/pythonProject1/media/{file_name}"
        print(command)
        subprocess.run(command)
        return FileResponse(f"C:/Users/viofi/PycharmProjects/pythonProject1/media/{file_name}")
    else:
        print("what the duck")
        return FileResponse("#error.mp4")
    #convert_video_to_mp3("Media.ts", "video.mp4")


