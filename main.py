import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)


def huffman_encoding(text):
    if not text:
        return "", {}

    freq_dict = dict()
    for char in text:
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1

    root = build_huffman_tree(freq_dict)
    codes = {}
    build_huffman_codes(root, "", codes)

    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes


def huffman_decoding(encoded_text, codes):
    if not encoded_text:
        return ""

    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            char = reverse_codes[current_code]
            decoded_text += char
            current_code = ""

    return decoded_text



