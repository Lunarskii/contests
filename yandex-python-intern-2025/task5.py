from collections import deque


to_char_annotation_map = {
    "222": "C", "22": "B", "2": "A",
    "333": "F", "33": "E", "3": "D",
    "444": "I", "44": "H", "4": "G",
    "555": "L", "55": "K", "5": "J",
    "666": "O", "66": "N", "6": "M",
    "7777": "S", "777": "R", "77": "Q", "7": "P",
    "888": "V", "88": "U", "8": "T",
    "9999": "Z", "999": "Y", "99": "X", "9": "W",
}
from_char_annotation_map = {
    "C": "222", "B": "22", "A": "2",
    "F": "333", "E": "33", "D": "3",
    "I": "444", "H": "44", "G": "4",
    "L": "555", "K": "55", "J": "5",
    "O": "666", "N": "66", "M": "6",
    "S": "7777", "R": "777", "Q": "77", "P": "7",
    "V": "888", "U": "88", "T": "8",
    "Z": "9999", "Y": "999", "X": "99", "W": "9",
}


def encrypt(text: str):
    return "".join(from_char_annotation_map[char] for char in text)


def max_num_consecutive_chars(s: str, target: str) -> int:
    count = 0
    for char in s:
        if char == target:
            count += 1
        else:
            break
    return count


class AhoCorasick:
    def __init__(self, words: list[str]):
        self.trie: list[dict[str, int]] = [{}]
        self.output: list[list[str]] = []
        self._build_trie(words)
        self.fail: list[int] = [0] * len(self.trie)
        self._build_fail_links()

    def _build_trie(self, words: list[str]):
        for word in words:
            node: int = 0
            for char in word:
                char_idx: str = from_char_annotation_map[char]
                if char_idx not in self.trie[node]:
                    self.trie[node][char_idx] = len(self.trie)
                    self.trie.append({})
                node = self.trie[node][char_idx]
            while len(self.output) <= node:
                self.output.append([])
            self.output[node].append(word)

    def _build_fail_links(self):
        queue = deque()

        for char_idx, node in self.trie[0].items():
            self.fail[node] = 0
            queue.append(node)

        while queue:
            current: int = queue.popleft()
            for char_idx, next_node in self.trie[current].items():
                fail_state: int = self.fail[current]
                while fail_state and char_idx not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]
                self.fail[next_node] = self.trie[fail_state].get(char_idx, 0)
                self.output[next_node] += self.output[self.fail[next_node]]
                queue.append(next_node)

    def search(self, text: str) -> list[tuple[int, int, str]]:
        node: int = 0
        results: list[tuple[int, int, str]] = []

        i: int = 0
        while i < len(text):
            found: bool = False
            char: str = text[i]
            max_char_len: int = max_num_consecutive_chars(text[i:i + 4], char)
            chunk_len: int = 0

            for length in range(max_char_len, 0, -1):
                chunk: str = text[i:i + length]
                if chunk in self.trie[node]:
                    node = self.trie[node][chunk]
                    chunk_len = length
                    found = True
                    break

            if not found:
                while node and text[i] not in self.trie[node]:
                    node = self.fail[node]
                node = self.trie[node].get(text[i], 0)
                if not node:
                    chunk_len = 0
                else:
                    chunk_len = 1

            for word in self.output[node]:
                results.append((i + chunk_len - len(encrypt(word)), i + chunk_len - 1, word))

            i += chunk_len
        return results


def find_non_overlapping_substrings(text: str, dictionary: list[str]) -> list[str]:
    ac = AhoCorasick(dictionary)
    matches = ac.search(text)
    starts: list[int] = [-1] * (len(text) + 1)
    ends: list[int] = [-1] * (len(text) + 1)
    words: list[str] = [""] * (len(text) + 1)

    matches.sort(key=lambda x: x[1])
    for start, end, word in matches:
        if (start == 0 or ends[start] != -1) and (ends[end + 1] == -1 or ends[end + 1] < end):
            starts[end + 1] = start
            ends[end + 1] = end
            words[end + 1] = word

    result: list[str] = []
    idx: int = len(text)

    while idx > 0:
        if starts[idx] == -1:
            break
        result.append(words[idx])
        idx = starts[idx]
    result.reverse()

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    text = lines[0]
    dictionary_len = int(lines[1])
    dictionary = lines[2:2 + dictionary_len]
    print(*find_non_overlapping_substrings(text, dictionary))

    # from time import time
    # text = "7788266888674499977774442227777888888"
    # dictionary = ["PHYSICS", "QUANTUM", "WORLD", "HELLO", "PHYS", "A", "V"]
    # start_time = time()
    # print(" ".join(find_non_overlapping_substrings(text, dictionary)))
    # end_time = time()
    # print(f"Время выполнения: {end_time - start_time:.2f} секунд")
