from typing import List
import statistics

from pyot.core.queue import Queue
from pyot.models import lol
from pyot.core.resources import resource_manager

@resource_manager.as_decorator
async def check_summoner(summoner_name):
    """

    :param summoner_name: summoner_name you want to check
    :return: returns summoner existence
    """
    try:
        summoner = await lol.Summoner(name=summoner_name).get()


    except:
        return False

    return True

@resource_manager.as_decorator
async def get_summoner(summoner_name):
    """

    :param summoner_name: summoner name
    :return: returns summoner
    """

    summoner = await lol.Summoner(name=summoner_name).get()

    return summoner



@resource_manager.as_decorator
async def get_name(summoner_name):
    """

    :param summoner_name:
    :return:
    """
    summoner = await lol.Summoner(name=summoner_name).get()
    return summoner.name
#
# @resource_manager.as_decorator
# async def get_matches(summoner, number=10):
#     """
#     Returns a number of matches played by summoner (determined by value of number)
#     """
#     async with Queue() as queue:
#         history = await summoner.summoner.match_history.get()
#         for match in history.matches[:number]:
#             await queue.put(match.get())
#         list_matches: List[lol.Match] = await queue.join()
#     return list_matches
#
#
# @resource_manager.as_decorator
# async def average_win_rate_10_matches(summoner, matches):
#     first_10_matches = await summoner.get_matches(summoner.summoner, 10)
#     wins = []
#     for match in first_10_matches:
#         for participant in match.info.participants:
#             if participant.puuid == summoner.summoner.puuid:
#                 wins.append(int(participant.win))
#     return statistics.mean(wins or [0])
#
#
# @resource_manager.as_decorator
# async def last_played_champs(summoner, num: int):
#     first_10_matches = await summoner.get_matches(num)
#     champ_names = []
#     for match in first_10_matches:
#         for participant in match.info.participants:
#             if participant.puuid == summoner.summoner.puuid:
#                 champ_names.append(participant.champion_name)
#     return champ_names
#
#
# @resource_manager.as_decorator
# async def average_match_duration_millis(self, num):
#     # Before entering scope, resources are acquired for this event loop
#     first_5_matches = await self.get_matches(5)
#     return statistics.mean([match.info.duration_millis for match in first_5_matches] or [0])
#     # After exiting scope, resources are released for this event loop
#
#
# @resource_manager.as_decorator
# async def top_3_champion_masteries(self, num: int):
#     """
#     Returns specified number of masteries for summoner, Decending {highest to lowest}
#     """
#     summoner_masteries = await self.summoner.champion_masteries.get()
#     total_masteries = []
#     for mastery in summoner_masteries:
#         total_masteries.append(mastery.champion_id)
#     names = []
#     for id in total_masteries[:3]:
#         champ = await lol.Champion(id=id, locale="en_us").get()
#         names.append(" {}".format(champ.name))
#
#     return names
#
#
# @resource_manager.as_decorator
# async def get_rank(self, *args):
#     # TODO not sure if this is the best way to send back ranked info
#
#     # this how to access rank :0
#     comp = await lol.SummonerLeague(summoner_id=self.summoner.id, platform='na1').get()
#     comp = comp[0]
#
#     lp = comp.league_getpoints
#     rank = comp.tier
#     division = comp.rank
#
#     return f'{rank} {division} {lp} LP'
#
#
# async def get_level(self):
#     return self.summoner.level
#
#
# async def get_name(self):
#     return self.summoner.name
#
#
# # TODO Create Functions to get all Info necessary here first, then migrate to server
#
# @resource_manager.as_decorator
# async def get_ladder_rank(self):
#     ...
#
#
# @resource_manager.as_decorator
# async def get_summoner_icon(self):
#     ...
