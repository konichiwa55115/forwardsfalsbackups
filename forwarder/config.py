from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "1234567890:Abcdef1234567890GHIJ"  # Your bot API key
    OWNER_ID = 1234567890  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001234567890]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001234567890, -1234567890]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
