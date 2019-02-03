#!/usr/bin/python
import click
import re
from piglatin import to_english
from english import to_piglatin

@click.command()
@click.option('--english/--piglatin', default=None, help='Text is English/Piglatin')
@click.argument('filename')
def translate(english, filename):
    if english is None:
        english = isenglish(text)


    click.echo('Hello World!')

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
