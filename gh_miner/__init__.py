import logging
import os

from gitpandas import Repository
import numpy as np
import pandas


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def fetch_commit_history(repository):
    csv_file = './commit_history.csv'
    if not os.path.isfile(csv_file):
        ch = repository.commit_history('upstream/master')
        ch.to_csv(csv_file)
    else:
        ch = pandas.read_csv(csv_file)

    return ch


def fetch_hours_estimate(repository, ch):
    csv_file = './hours_estimate.csv'
    if not os.path.isfile(csv_file):
        he = repository.hours_estimate('upstream/master', commit_history=ch)
        he.to_csv(csv_file)
    else:
        he = pandas.read_csv(csv_file)

    return he


def fetch_file_change_history(repository):
    csv_file = './file_change_history.csv'
    if not os.path.isfile(csv_file):
        fch = repository.file_change_history('upstream/master')
        fch.to_csv(csv_file)
    else:
        fch = pandas.read_csv(csv_file)

    return fch


def fetch_file_change_rate(repository, fch):
    csv_file = './file_change_rate.csv'
    if not os.path.isfile(csv_file):
        fcr = repository.file_change_rate('upstream/master', file_change_history=fch)
        fcr.to_csv(csv_file)
    else:
        fcr = pandas.read_csv(csv_file)

    return fcr


def fetch_cumulative_blame(repository):
    csv_file = './cumulative_blame.csv'
    if not os.path.isfile(csv_file):
        cb = repository.parallel_cumulative_blame('upstream/master', workers=32)
        cb.to_csv(csv_file)
    else:
        cb = pandas.read_csv(csv_file)

    return cb


def fetch_bus_factor(repository):
    csv_file = './bus_factor.csv'
    if not os.path.isfile(csv_file):
        bf = repository.bus_factor('upstream/master')
        bf.to_csv(csv_file)
    else:
        bf = pandas.read_csv(csv_file)

    return bf


def fetch_file_owner(repository):
    csv_file = './file_owner.csv'
    if not os.path.isfile(csv_file):
        fo = repository.file_owner('upstream/master')
        fo.to_csv(csv_file)
    else:
        fo = pandas.read_csv(csv_file)

    return fo


def fetch_punch_card(repository, ch):
    csv_file = './punch_card.csv'
    if not os.path.isfile(csv_file):
        pc = repository.file_owner('upstream/master', commit_history=ch)
        pc.to_csv(csv_file)
    else:
        pc = pandas.read_csv(csv_file)

    return pc


def main():
    r = Repository(working_dir=os.path.abspath('../nixpkgs'))
    logger.info('fetching commit history')
    ch = fetch_commit_history(r)
    logger.info('fetching hours estimate')
    he = fetch_hours_estimate(r, ch)
    logger.info('fetching file change history')
    fch = fetch_file_change_history(r)
    logger.info('fetching file change rate')
    fcr = fetch_file_change_rate(r, fch)
    logger.info('fetching cumulative blame')
    cb = fetch_cumulative_blame(r)
    logger.info('fetching bus factor')
    bf = fetch_bus_factor(r)
    logger.info('fetching file owner')
    fo = fetch_file_owner(r)
    logger.info('fetching punch card')
    pc = fetch_punch_card(r)


if __name__ == '__main__':
    main()
