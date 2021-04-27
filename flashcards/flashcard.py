#!env python
import sys
import csv


def even(num):
    return num % 2 == 0


def odd(num):
    return not even(num)


def load(filename):
    data = sys.stdin.readlines()
    reader = csv.reader(data)
    return list(reader)


def chunk(items, size):
    # looping till length l
    for i in range(0, len(items), size):
        yield items[i:i + size]


def render(cards, css, reverse=False):
    print('<table>')

    for pair in chunk(cards, 2):
        left, right = (list(pair) + ['']*2)[:2]
        if reverse:
            right, left = left, right
        print(
            f"<tr><td class='{css}'>{left}</td><td class='{css}'>{right}</td></tr>")

    print('</table>')


data = load('input.csv')
chunks = list(chunk(data, 10))
print('<head><meta charset="UTF-8"><link href="./flashcards.css" rel="stylesheet"></head>')
print('<body>')
for page in chunks:
    terms = list(map(lambda x: x[0], page))
    defs = list(map(lambda x: x[1], page))
    render(terms, 'term')
    render(defs, 'def', reverse=True)
print('</body>')