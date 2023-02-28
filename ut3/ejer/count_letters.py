# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    for char in sentence:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter


if __name__ == "__main__":
    run("boom")

# for char in sentence:
#    counter[char] = counter.get(char, 0) + 1
