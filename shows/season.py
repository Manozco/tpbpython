#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manozco
# @Date:   2014-08-01 22:28:35
# @Last Modified by:   Manozco
# @Last Modified time: 2014-08-01 22:30:40

from shows.episode import Episode

class Season(object):
    def __init__(self, number, episodes=None):
        self.number = number
        self.episodes = episodes or []

    def add_episode(self, episode):
        if not isinstance(episode, Episode):
            raise TypeError("Must be of class {0}".format(Episode))
        self.episodes.append(episode)
