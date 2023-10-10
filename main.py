import ffmpeg

import random

from fastapi import FastAPI

from fastapi.responses import FileResponse

import base64

import subprocess

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://wellwornnimblecode.nathanielnvi0fl.repl.co",
    "https://wellwornnimblecode.nathanielnvi0fl.repl.co:8080",
    "0.0.0.0:8080",
    "0.0.0.0",
    "https://studio.penguinmod.site",
    "tw-editor://.",
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
    base64_string[len(base64_string) - 1] = ''
    base64_string = list_convert_to_string(base64_string)
    file_name = f'output_{file}_{random.randint(1,99999)}.mp4'
    print(base64_string)
    (
        ffmpeg
        .input(base64_string)
        .output(file_name)
        .run()
    )
    #convert_video_to_mp3("Media.ts", "video.mp4")
    Html = '<video width="320" height="240" controls><source src="{file_name}" type="video/mp4"></video>'
    return FileResponse(file_name)

