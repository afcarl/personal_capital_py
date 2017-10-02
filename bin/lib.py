#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""
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

def compute_returns(observation, return_mean, return_std_dev, inflation):
    #
    pass