#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""
import logging
import pprint

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
    st_devs = [numpy.random.normal(size=20) for i in range(lib.get_conf('num_trials'))]
    trials['st_devs'] = st_devs

    # Translate observed standard deviations to dollar amounts (with inflation)

    # Iterate through portfolios
    for portfolio_dict in lib.get_conf('portfolios'):
        logging.info('Generating results for portfolio dict: {}'.format(portfolio_dict))

        # Compute list of balances (one for every year)
        balances_columns = portfolio_dict['portfolio'] + '_balances'
        trials[balances_columns] = trials.apply(
            func=lambda x: lib.compute_balances(x, return_mean=portfolio_dict['return_mean'],
                                                return_std_dev=portfolio_dict['return_std_dev']), axis=1)

        # Extract final dollar amount for each trial

        trials[portfolio_dict['portfolio'] + '_final_balance'] = trials[balances_columns].apply(lambda x: x[-1])

    # TODO Archive data and return trial data
    logging.info('Trials complete')

    return trials

def summarize_trials(trials):
    # TODO Docstring

    # TODO Reference variables
    summary_agg = list()

    # TODO Iterate through portfolios
    for portfolio_dict in lib.get_conf('portfolios'):

        logging.info('Creating summary statistics for portfolio_dict: {}'.format(portfolio_dict))

        observation_dict = dict()
        portfolio = portfolio_dict['portfolio']
        observation_dict['portfolio'] = portfolio

        final_balances = trials[portfolio + '_final_balance'].tolist()

        # Compute median for each portfolio
        observation_dict['median'] = numpy.median(final_balances)

        # Compute 1st decile
        observation_dict['top_10_perc'] = numpy.percentile(final_balances, 90)

        # Compute 9th decile
        observation_dict['bottom_10_perc'] = numpy.percentile(final_balances, 10)
        summary_agg.append(observation_dict)

    # TODO Format results
    summary_df = pandas.DataFrame(summary_agg)
    summary_df = summary_df[['portfolio', 'bottom_10_perc', 'median', 'top_10_perc']]
    print summary_df


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
