#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""
import logging
import sys
import yaml

CONFS = None


def load_confs(conf_path='../confs/confs.yaml'):
    global CONFS

    if CONFS is None:
        CONFS = yaml.load(open(conf_path))

    return CONFS
    # TODO Docstring

    pass


def get_conf(conf_name):
    # TODO Docstring
    confs = load_confs()

    conf = confs.get(conf_name, None)

    return conf

def compute_returns(observation, return_mean, return_std_dev):
    # TODO Docstring
    logging.debug('Computing return for trial number: {}'.format(observation['trial_num']))

    # Reference variables
    annual_amounts = list()
    annual_amounts.append(observation['starting_amount'])

    for std_dev in observation['st_devs']:
        # TODO Get current balance

        # TODO Compute new balance

        # TODO Apply inflation

        # TODO Add current value to list

        pass

    # Remove starting amount from annual amounts list
    annual_amounts = annual_amounts[1:]

    sys.exit()

    pass