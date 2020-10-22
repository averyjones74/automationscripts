# Simple plagiarism detector
# Note: This is a very simple example, might not work perfectly
# Author: Abhinand

import math
import re
from collections import Counter
import sys

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    """ Function to compute Cosine Similarity between two word vectors"""
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    """Simple function to convert text to vector"""
    words = WORD.findall(text)
    return Counter(words)


if __name__ == "__main__":

    file1 = open(sys.argv[1], "r")
    text1 = file1.read().replace("\n", " ")

    file2 = open(sys.argv[2], "r")
    text2 = file2.read().replace("\n", " ")

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine = get_cosine(vector1, vector2)

    print("Similarity Score:", cosine)
