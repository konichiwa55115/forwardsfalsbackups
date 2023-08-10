from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5545470781:AAGjzXBuTOeJ1JulON1Cw0I2ZP8kebs2Alk"  # Your bot API key
    OWNER_ID = 6286530408  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001941046351]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001851494395]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
