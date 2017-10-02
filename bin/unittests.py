import logging
import unittest

import lib

logging.getLogger().setLevel(logging.DEBUG)


class SimplisticTest(unittest.TestCase):

    def test_compute_returns_1(self):
        """
        Test without inflation, with one delta period
        :return:
        """

        lib.load_confs()

        # Set inflation
        lib.load_confs()['inflation'] = 0

        # Create test observation
        test_observation = dict()
        test_observation['trial_num'] = 1
        test_observation['st_devs'] = [1]
        test_observation['starting_amount'] = 1

        # Compute return
        test_return = lib.compute_returns(test_observation, .1, .08)[0]

        logging.info('Test return: {}'.format(test_return))

        self.assertAlmostEquals(test_return, 1.18)

    def test_compute_returns_2(self):
        """
        Test with inflation, with one delta period
        :return:
        """

        lib.load_confs()

        # Set inflation
        lib.load_confs()['inflation'] = .05

        # Create test observation
        test_observation = dict()
        test_observation['trial_num'] = 2
        test_observation['st_devs'] = [1]
        test_observation['starting_amount'] = 1

        # Compute return
        test_return = lib.compute_returns(test_observation, .1, .08)[0]

        logging.info('Test return: {}'.format(test_return))

        self.assertAlmostEquals(test_return, 1.239)

    def test_compute_returns_3(self):
        """
        Test with inflation, with two delta periods
        :return:
        """

        lib.load_confs()

        # Set inflation
        lib.load_confs()['inflation'] = .05

        # Create test observation
        test_observation = dict()
        test_observation['trial_num'] = 3
        test_observation['st_devs'] = [1, .3]
        test_observation['starting_amount'] = 1

        # Compute return
        test_returns = lib.compute_returns(test_observation, .1, .08)

        logging.info('Test returns: {}'.format(test_returns))

        for (test_balance, true_balance) in zip(test_returns, [1.239, 1.4622678]):
            self.assertAlmostEquals(test_balance, true_balance)


if __name__ == '__main__':
    unittest.main()
