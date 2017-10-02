#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""
import logging

import numpy
import pandas

import lib

logging.basicConfig(level=logging.DEBUG)


def create_trials():
    # TODO Docstring

    logging.info('Beginning trials')

    # Create pre-trial DataFrame (one observation is one trial), wth trial number and starting dollar amount
    logging.info('Creating pre-trial dataframe')
    index = range(1, lib.get_conf('num_trials')+1)
    trials = pandas.DataFrame(index=index)
    trials['trial_num'] = trials.index
    trials['starting_amount'] = lib.get_conf('starting_amount')

    logging.info('Created trials table with starting info: \n{}'.format(trials))

    # Generate observed standard deviations
    logging.info('Generating standard_deviations')
    st_devs = [numpy.random.normal(size=20) for i in range(10000)]
    trials['st_devs'] = st_devs

    # TODO Translate observed standard deviations to dollar amounts (with inflation)
    for portfolio_dict in lib.get_conf('portfolios'):
        logging.info('Generating results for portfolio dict: {}'.format(portfolio_dict))

        trials.apply(func=lambda x: lib.compute_returns(x, return_mean=portfolio_dict['return_mean'],
                            return_std_dev=portfolio_dict['return_std_dev']), axis=1)

    # TODO Extract final dollar amount for each trial


    # TODO Archive data and return trial data
    logging.info('Trials complete')
    pass

def summarize_trials(trials):
    # TODO Docstring

    # TODO Reference variables

    # TODO Compute median for each portfolio

    # TODO Compute 1st decile

    # TODO Compute 9th decile

    # TODO Format results

    # TODO Archive & return results
    pass

def main():
    """
    Main function documentation template
    :return: None
    :rtype: None
    """

    # TODO Docstring

    # TODO Set random seed (if required)

    # TODO Generate trial data
    trials = create_trials()

    # TODO Generate summary data
    summary = summarize_trials(trials)
    pass


# Main section
if __name__ == '__main__':
    main()
