#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""
import logging

logging.basicConfig(level=logging.DEBUG)


def create_trials():
    # TODO Docstring

    # TODO Create empty DataFrame (one observation is one trial), with trial number and starting dollar amount

    # TODO Generate observed standard deviations

    # TODO Translate observed standard deviations to dollar amounts (with inflation)

    # TODO Extract final dollar amount for each trial

    # TODO Archive data and return trial data

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
