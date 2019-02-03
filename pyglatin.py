#!/usr/bin/python
import click
import re
from piglatin import to_english
from english import to_piglatin

@click.command()
@click.option('--english/--piglatin', default=None, help='Text is English/Piglatin')
@click.argument('file', default=None, required=False, type=click.File('r'))
def translate(english, filename):
    if english is None:
        english = isenglish(text)
    if file is None:
        text = input()
    else:
        text = file.read()

    out = to_piglatin(text) if english else to_english(text)
    click.echo(out)

whitespace = re.compile(r'\s+')
def is_english(text):
    count = 0
    total = 0
    for word in whitespace.split(text):
        total+=1
        if word.endswith('ay'):
            count+=1
    if count/total > .8:
        return False
    return True

if __name__ == '__main__':
    translate()
