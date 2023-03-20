try:
  import unzip_requirements
except ImportError:
  pass

import json

import librosa

# 1. Get the file path to an included audio example
filename = "./Kevin_MacLeod_-_P_I_Tchaikovsky_Dance_of_the_Sugar_Plum_Fairy.ogg"




def hello(event, context):
    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(filename)

    # 3. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    test = 'Estimated tempo: {:.2f} beats per minute'.format(tempo)
    print(test)

    # 4. Convert the frame indices of beat events into timestamps
    #beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
        "librosa": test,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
