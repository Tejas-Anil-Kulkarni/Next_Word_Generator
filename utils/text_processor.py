from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences

VOCAB_SIZE = 10000
MAX_LENGTH = 100


def text_to_sequence(text, word_index):

    words = text_to_word_sequence(text)

    sequence = [1]  # IMDb START token

    for word in words:

        index = word_index.get(word)

        if index is not None and index + 3 < VOCAB_SIZE:
            sequence.append(index + 3)
        else:
            sequence.append(2)  # OOV token

    return sequence


def prepare_input(sequence):

    padded = pad_sequences(
        [sequence],
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="pre"
    )

    return padded