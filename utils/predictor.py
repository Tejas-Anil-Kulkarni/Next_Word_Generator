import numpy as np

from utils.text_processor import (
    text_to_sequence,
    prepare_input
)


def generate_text(
    model,
    word_index,
    prompt,
    num_words=10
):

    index_word = {
        int(index) + 3: word
        for word, index in word_index.items()
        if int(index) + 3 < 10000
    }

    index_word[1] = "<START>"
    index_word[2] = "<OOV>"

    sequence = text_to_sequence(prompt, word_index)

    generated_words = []

    for _ in range(num_words):

        X = prepare_input(sequence)

        predictions = model.predict(
            X,
            verbose=0
        )[0]

        # Exclude padding and START tokens
        next_word_id = int(np.argmax(predictions[2:] + 0)) + 2

        next_word = index_word.get(
            next_word_id,
            "<OOV>"
        )

        if next_word_id == 2:
            next_word = "<OOV>"

        generated_words.append(next_word)

        sequence.append(next_word_id)

    return {
        "generated_words": generated_words,
        "generated_text": prompt.strip() + " " + " ".join(generated_words)
    }