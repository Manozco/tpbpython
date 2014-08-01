#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manozco
# @Date:   2014-08-01 22:25:07
# @Last Modified by:   Manozco
# @Last Modified time: 2014-08-01 22:49:54

from tpb.tpb_handler import TpbHandler
from shows.episode import Episode
from shows.season import Season
from shows.show import Show

if __name__ == '__main__':
    handler = TpbHandler()
    rizzoli_show = Show('rizzoli')
    for i in range(1, 6):
        season = Season(i)
        for j in range(1, 10):
            episode = Episode(j)
            season.add_episode(episode)
        rizzoli_show.add_season(season)

    d = {}
    search_results = {}
    d[rizzoli_show.name] = {}
    for season in rizzoli_show.seasons:
        d[rizzoli_show.name][season.number] = {}
        for ep in season.episodes:
            search_term = "{0} s{1:02d}e{2:02d}".format(rizzoli_show.name,
                                                                                 season.number,
                                                                                 ep.number)
            d[rizzoli_show.name][season.number][ep.number] = search_term
            search_results[search_term] = handler.seed_search(search_term)


    import json
    print(json.dump(search_results, open("data.json", "w"), indent=4, sort_keys=True))

