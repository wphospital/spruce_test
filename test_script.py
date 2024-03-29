import os, getpass
import sys
import pandas
import click
import numpy as np
import time

default_name = os.getenv('name')

# blah blah
@click.command()
@click.option('--name', '-n', default='Sprucey')
@click.option('--sleeptime')
@click.option('--sleep/--no-sleep', default=True)
@click.option('--test-fail/--no-test-fail', default=False)
def main(name, sleeptime, sleep, test_fail):
    # biscuits
    if sleep:
        if sleeptime:
            sleepy_time = int(sleeptime)
        else:
            sleepy_time = np.random.normal(loc=0.5, scale=0.3)
        time.sleep(sleepy_time)

    if name == 'Sprucey':
        print(default_name)

    if test_fail:
        name = broken_name

    print('Hello {}'.format(name))

if __name__ == '__main__':
    main()
