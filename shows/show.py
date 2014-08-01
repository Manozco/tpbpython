#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manozco
# @Date:   2014-08-01 22:28:57
# @Last Modified by:   Manozco
# @Last Modified time: 2014-08-01 22:37:28

from shows.season import Season

class Show(object):
    def __init__(self, name, seasons=None):
        self.name = name
        self.seasons = seasons or []

    def add_season(self, season):
        if not isinstance(season, Season):
            raise TypeError("Must be of class {0}".format(Season))
        self.seasons.append(season)
