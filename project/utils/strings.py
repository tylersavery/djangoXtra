import random
import string


def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    elif val in ("n", "no", "f", "false", "off", "0"):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))


def get_random_string(characters, length):
    return "".join(random.choice(characters) for _ in range(length))


def get_random_slug(length):
    return get_random_string(string.ascii_lowercase + string.digits, length)


def truncate_text(text, length=100, ellipsis="..."):
    return (
        text
        if len(text) <= length
        else " ".join(text[: length + 1].split(" ")[0:-1]) + ellipsis
    )


def string_to_bool(value):
    try:
        return strtobool(value)
    except ValueError:
        return False
