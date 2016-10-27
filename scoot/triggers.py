import random
import responses


def has_trigger(value: str) -> bool:
    """
    Checks if the given string contains one or more occurrences of a trigger.
    :param value: The string to check.
    :return: true if the specified string contains a trigger; otherwise false.
    """

    for trigger in triggers:
        if trigger in value:
            return True

    return False


def get_response(message: str) -> dict:
    """
    Gets the response message for the specified message.
    :param message: The message being responded to.
    :return: The response message as JSON.
    """

    response = {}

    # 20% chance to get fucked
    if message.startswith(command_sequence) and random.randint(0, 100) < 20:
        response['text'] = "Don't tell me what to do dad."

    for trigger in triggers:
        if trigger in message:
            # get the bots response
            bot_response = triggers[trigger](message)

            # sanitize the bot response for utf-8
            response['text'] = bot_response.decode("utf-8", "ignore").encode("utf-8")

            # return the response json.
            return response

    # if we reach here there was no matching trigger
    raise ValueError('Specified message has no triggers.')

triggers = {
    "flake": responses.get_flake,
    "fuck": responses.get_fuck,
    "help": responses.get_help,
    "kek": responses.get_kek,
    "lel": responses.get_lel,
    "triggered": responses.get_triggered
}

command_sequence = "!"