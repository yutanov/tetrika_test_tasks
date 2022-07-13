def task(array: str):
    el_index = array.index("0")
    return el_index


if __name__ == "__main__":
    string = "111111111110000000000000000"
    assert task(string) == 11
