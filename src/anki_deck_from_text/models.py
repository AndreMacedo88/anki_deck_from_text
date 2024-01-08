import genanki
import random

model_id = random.randrange(1 << 30, 1 << 31)
MODEL_SOUND = genanki.Model(
    model_id=model_id,
    name="Main model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Sound"},
    ],
    templates=[
        {
            "name": "Card to type",
            "qfmt": "{{Question}}<br>{{type:Answer}}",
            "afmt": "{{FrontSide}}<hr id='answer'><br>{{Sound}}",
        },
    ],
    css=""".card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
}
"""
)

MODELS = {
    "sound": MODEL_SOUND,
}
