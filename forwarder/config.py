from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "6117968672:AAGiHeEHZt7MRIXs7jxctixEdatrY3svVvk"  # Your bot API key
    OWNER_ID = 6286530408  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [2142696890, 5667675478]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001824436904]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
