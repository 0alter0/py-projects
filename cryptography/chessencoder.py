import subprocess

PIECES = "PNBRQKpnbrqk"
BASE = 13
BOARD_SIZE = 64

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
                if n < 1 or n > 8:
                    raise ValueError("Invalid empty-square count")
                values.extend([0] * n)
                count += n

            elif c in VALUES:
                values.append(VALUES[c])
                count += 1

            else:
                raise ValueError("Invalid board character")

        if count != 8:
            raise ValueError("Invalid FEN rank")

    if len(values) != 64:
        raise ValueError("Invalid FEN board")

    return values

def encode(text):
    data = text.encode("utf-8")
    length = len(data)

    number = int.from_bytes(data, "big") if data else 0

    board_values = []

    for _ in range(BOARD_SIZE):
        number, digit = divmod(number, BASE)
        board_values.append(digit)

    number, ep = divmod(number, 17)
    number, castling = divmod(number, 16)
    number, side = divmod(number, 2)

    fullmove = number + 1

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
        + str(length)
        + " "
        + str(fullmove)
    )

def decode(fen):
    parts = fen.split()

    if len(parts) != 6:
        raise ValueError("Invalid FEN")

    board = parts[0]
    side = parts[1]
    castling = parts[2]
    ep = parts[3]
    length = int(parts[4])
    fullmove = int(parts[5])

    if side not in ("w", "b"):
        raise ValueError("Invalid side")

    if castling not in CASTLING:
        raise ValueError("Invalid castling field")

    if ep not in EN_PASSANT:
        raise ValueError("Invalid en-passant field")

    if length < 0:
        raise ValueError("Invalid length")

    if fullmove < 1:
        raise ValueError("Invalid fullmove number")

    board_values = expand_board(board)

    board_number = 0

    for value in board_values:
        board_number = board_number * BASE + value

    number = fullmove - 1
    number = number * 2 + (0 if side == "w" else 1)
    number = number * 16 + CASTLING.index(castling)
    number = number * 17 + EN_PASSANT.index(ep)
    number = number * (BASE ** BOARD_SIZE) + board_number

    if length == 0:
        return ""

    try:
        data = number.to_bytes(length, "big")
    except OverflowError:
        raise ValueError(
            "The FEN does not contain enough data for the specified length"
        )

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("Decoded data is not valid UTF-8")

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
