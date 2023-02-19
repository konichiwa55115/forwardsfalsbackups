from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5938308636:AAF9sD2Jtw3sFp4SDI1NEKB7dV0GQj9Z4rE"  # Your bot API key
    OWNER_ID = 1234567890  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [1227193881, 6234365091]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001230414925]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
