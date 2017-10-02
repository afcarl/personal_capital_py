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

def compute_balances(observation, return_mean, return_std_dev):
    # TODO Docstring
    logging.debug('Computing return for trial number: {}'.format(observation['trial_num']))

    # Reference variables
    annual_balances = list()
    annual_balances.append(observation['starting_amount'])

    for st_dev in observation['st_devs']:

        # Get current balance
        current_balance = annual_balances[-1]

        # Check if balance is positive. If so, compute new balance
        if current_balance > 0:

            # Scale std
            scaled_std = st_dev * return_std_dev + return_mean

            # Compute new balance
            new_balance = current_balance * (1 + scaled_std)

            # Apply inflation
            inflated_new_balance = new_balance * (1 + get_conf('inflation'))

            logging.debug('Performed update for one year, for trial number: {}. Incoming balance: {}, exiting '
                          'inflated balance: {}, return percentage: {}'.format(observation['trial_num'],
                                                                               current_balance, inflated_new_balance,
                                                                               scaled_std))
        # If balance is zero or negative,
        else:

            inflated_new_balance = current_balance

        # Add current value to list
        annual_balances.append(inflated_new_balance)

    # Remove starting amount from annual amounts list
    annual_balances = annual_balances[1:]

    return annual_balances
