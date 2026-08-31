import subprocess

PIECES = "PNBRQKpnbrqk"
BASE = 13

VALUES = {c: i + 1 for i, c in enumerate(PIECES)}
REVERSE = {i + 1: c for i, c in enumerate(PIECES)}

CASTLING = [
    "-", "K", "Q", "KQ",
    "k", "Kk", "Qk", "KQk",
    "q", "Kq", "Qq", "KQq",
    "kq", "Kkq", "Qkq", "KQkq"
]

EN_PASSANT = ["-"] + [
    file + str(rank)
    for rank in (3, 6)
    for file in "abcdefgh"
]

MAX_BYTES = 33
MARKER = b"FEN1"

def copy_to_clipboard(text):
    subprocess.run("clip", input=text, text=True, shell=True)

def compress_rank(values):
    result = ""
    empty = 0

    for value in values:
        if value == 0:
            empty += 1
        else:
            if empty:
                result += str(empty)
                empty = 0
            result += REVERSE[value]

    if empty:
        result += str(empty)

    return result

def expand_board(board):
    values = []

    for rank in board.split("/"):
        count = 0

        for c in rank:
            if c.isdigit():
                n = int(c)
                values.extend([0] * n)
                count += n
            elif c in VALUES:
                values.append(VALUES[c])
                count += 1
            else:
                raise ValueError("Invalid character in board")

        if count != 8:
            raise ValueError("Invalid FEN rank")

    if len(values) != 64:
        raise ValueError("Invalid FEN board")

    return values

def encode(text):
    data = text.encode("utf-8")
    payload = MARKER + data

    length = len(data)

    if length > MAX_BYTES:
        raise ValueError(
            f"String is too long. Maximum is {MAX_BYTES} UTF-8 bytes."
        )

    number = int.from_bytes(payload, "big")

    board_values = []

    for _ in range(64):
        number, remainder = divmod(number, BASE)
        board_values.append(remainder)

    side, number = divmod(number, 2)
    castling, number = divmod(number, 16)
    ep, number = divmod(number, 17)
    halfmove, number = divmod(number, 1000000)

    if number != 0:
        raise ValueError("String is too long.")

    board_values.reverse()

    board = []

    for rank in range(8):
        row = board_values[rank * 8:(rank + 1) * 8]
        board.append(compress_rank(row))

    return (
        "/".join(board)
        + (" w " if side == 0 else " b ")
        + CASTLING[castling]
        + " "
        + EN_PASSANT[ep]
        + " "
        + str(halfmove)
        + " "
        + str(length)
    )

def decode(fen):
    parts = fen.split()

    if len(parts) != 6:
        raise ValueError("Invalid FEN")

    board = parts[0]
    side_text = parts[1]
    castling = parts[2]
    ep = parts[3]
    halfmove = int(parts[4])
    length = int(parts[5])

    if side_text not in ("w", "b"):
        raise ValueError("Invalid side to move")

    if castling not in CASTLING:
        raise ValueError("Invalid castling field")

    if ep not in EN_PASSANT:
        raise ValueError("Invalid en-passant field")

    if length < 0 or length > MAX_BYTES:
        raise ValueError("Invalid text length")

    board_values = expand_board(board)

    board_number = 0

    for value in board_values:
        board_number = board_number * BASE + value

    metadata = halfmove
    metadata = metadata * 17 + EN_PASSANT.index(ep)
    metadata = metadata * 16 + CASTLING.index(castling)
    metadata = metadata * 2 + (0 if side_text == "w" else 1)

    number = metadata * (BASE ** 64) + board_number

    payload_length = length + len(MARKER)

    try:
        payload = number.to_bytes(payload_length, "big")
    except OverflowError:
        raise ValueError("FEN contains invalid encoded data")

    if not payload.startswith(MARKER):
        raise ValueError("This FEN was not created by this encoder")

    data = payload[len(MARKER):]

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("Encoded data is not valid UTF-8")

while True:
    mode = input("Encode or Decode: ").strip().lower()

    if mode == "encode":
        text = input("String: ")

        try:
            fen = encode(text)
            print(fen)
            copy_to_clipboard(fen)
            print("Copied to clipboard.")
        except Exception as e:
            print("Encode error:", e)

    elif mode == "decode":
        fen = input("FEN: ")

        try:
            print(decode(fen))
        except Exception as e:
            print("Decode error:", e)

    else:
        print("Invalid mode.")
