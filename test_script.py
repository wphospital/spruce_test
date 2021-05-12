import os, getpass
import sys
import pandas
import click
import numpy as np
import time

@click.command()
@click.option('--name', '-n', default='Sprucey')
def main(name):
    sleepy_time = np.random.normal(loc=0.5, scale=0.3)
    time.sleep(sleepy_time)
    print('Hello {}'.format(name))

if __name__ == '__main__':
    main()
