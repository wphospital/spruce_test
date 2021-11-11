import os, getpass
import sys
import pandas
import click
import numpy as np
import time

# blah blah
@click.command()
@click.option('--name', '-n', default='Sprucey')
@click.option('--sleeptime')
@click.option('--sleep/--no-sleep', default=True)
def main(name, sleeptime, sleep):
    # biscuits
    if sleep:
        if sleeptime:
            sleepy_time = int(sleeptime)
        else:
            sleepy_time = np.random.normal(loc=0.5, scale=0.3)
        time.sleep(sleepy_time)

    if name == 'Sprucey':
        name = os.getenv('db_username')

    print('Hello {}'.format(name))

if __name__ == '__main__':
    main()
