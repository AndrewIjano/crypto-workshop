import sys
import re
import getopt

BASE = ord("A")
PLOT_HEIGHT = 20
LIST_SIZE = 7


def format_text(text):
    return re.sub(r"[^a-zA-z]", "", text).upper()


def count_frequencies(formated_text):
    if re.findall(r"[^a-zA-z]", formated_text) != []:
        raise ValueError("Text given is not formated!")

    one_letter = {chr(BASE + i): 0 for i in range(26)}
    digraphs = {}
    trigraphs = {}
    doubles = {}

    N = len(formated_text) - 1

    for i in range(N):
        char = formated_text[i]

        if i > 0:
            digraph = prev_char + char
            if char == prev_char:
                doubles[digraph] = doubles.setdefault(digraph, 0) + 1

            digraphs[digraph] = digraphs.setdefault(digraph, 0) + 1

            if i < N - 1:
                next_char = formated_text[i+1]
                trigraph = digraph + next_char
                trigraphs[trigraph] = trigraphs.setdefault(trigraph, 0) + 1

        one_letter[char] = one_letter.setdefault(char, 0) + 1
        prev_char = char

    one_letter = {k: one_letter[k]/(N-1) for k in one_letter.keys()}

    return one_letter, digraphs, trigraphs, doubles


def plot_frequencies(freqs):
    freqs = [(k, freqs[k]) for k in sorted(freqs.keys())]
    max_freq = max([y for (x, y) in freqs])
    step = max_freq/PLOT_HEIGHT
    for i in range(PLOT_HEIGHT):
        print(end="{:.3f} |".format(max_freq))
        for (x, y) in freqs:
            if y >= max_freq:
                print(end="█ ")
            else:
                print(end="  ")
        max_freq -= step
        print()
    print("       ----------------------------------------------------")
    print("       A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")


def substitute(text, alphabet):
    alphabet = alphabet.upper()
    alpha_dict = {
        chr(BASE + i): chr(BASE + i).lower() if alphabet[i] == "-" else alphabet[i].upper()
        for i in range(len(alphabet))
    }
    return "".join(alpha_dict[c] if c.isalpha() else c for c in text.upper())


def print_help():
    print("Usage:")
    print("python3", sys.argv[0], "substitution -i [document] -a [alphabet]")
    print("python3", sys.argv[0], "analysis [options] -i [document]")
    print("Options:")
    print("-p                   plot the frequency graph (default: disabled)")


def substitution_module(args):
    document = ""
    alphabet = ""
    options, remainder = getopt.getopt(
        args[1:], "i:a:", ["aa"])
    for opt, arg in options:
        if opt == "-i":
            document = open(arg, "r+").read()
        if opt == "-a":
            alphabet = open(arg, "r+").read()

    print("  ABCDEFGHIJKLMNOPQRSTUVWXYZ This clear text...")
    print(" ", alphabet.upper().strip()[
        :26], "...maps to this ciphertext\n")
    print(substitute(document, alphabet[:26]))


def frequency_analysis_module(args):
    document = ""
    is_ploting = False
    options, remainder = getopt.getopt(args[1:], "pi:")
    for opt, arg in options:
        if opt == "-i":
            document = open(arg, "r+").read()
        if opt == "-p":
            is_ploting = True

    formated_text = format_text(document)

    one_letter, digraphs, trigraphs, doubles = count_frequencies(
        formated_text)

    if is_ploting:
        print("One letter frequency plot:")
        plot_frequencies(one_letter)

    def sorted_keys(d): return [
        k for k in sorted(d, key=d.get, reverse=True)]
    print("Frequencies:")
    print("one_letter:", " ".join(sorted_keys(one_letter)[:LIST_SIZE]))
    print("digraphs:",   " ".join(sorted_keys(digraphs)[:LIST_SIZE]))
    print("trigraphs:",  " ".join(sorted_keys(trigraphs)[:LIST_SIZE]))
    print("doubles:",    " ".join(sorted_keys(doubles)[:LIST_SIZE]))


if __name__ == "__main__":
    prog_name, args = sys.argv[0], sys.argv[1:]

    if len(sys.argv) < 2:
        print_help()
    elif args[0] == "substitution":
        substitution_module(args)
    elif args[0] == "analysis":
        frequency_analysis_module(args)
