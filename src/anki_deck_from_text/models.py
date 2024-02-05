"""
Contains the Anki card types (called `models`) to include in the deck.

Implement here your own models by generating a new model id and following an Anki card
structure (refer to https://docs.ankiweb.net/getting-started.html#card-types).
Then add an entry to your new model to the `MODELS` variable. Your model can now be used
in new decks by using the option `card_model` at the command-line.
"""

import genanki
import random

model_id_sound = random.randrange(1 << 30, 1 << 31)
MODEL_SOUND = genanki.Model(
    model_id=model_id_sound,
    name="Sound model",
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

"""
NEW MODELS IMPLEMENTATION AREA STARTS HERE
"""


"""
NEW MODELS IMPLEMENTATION AREA STOPS HERE
"""

MODELS = {
    "sound": MODEL_SOUND,
}
