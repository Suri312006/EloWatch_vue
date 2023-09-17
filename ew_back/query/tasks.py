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

@resource_manager.as_decorator
async def get_ladder_rank(summoner) -> int:
    """

    :param summoner: must pass in an asyncio.run(get_summoner(name)) instance
    :return: summoners ladder rank
    """
    league = lol.league.ApexLeague(queue='RANKED_5V5')

    return "blah"

@resource_manager.as_decorator
async def testing(summoner):
    """

    :param summoner:
    :return:
    """
    o = await lol.MasterLeague(queue="RANKED_SOLO_5x5", platform="na1").get()

    o = await lol.League(id=o.id, platform="na1").get()

    print(o)


@resource_manager.as_decorator
async def get_rank(summoner) -> dict:
    # TODO not sure if this is the best way to send back ranked info

    # this how to access rank :0
    comp = await lol.SummonerLeague(summoner_id= summoner.id, platform='na1').get()
    comp = comp[0]

    lp = comp.league_points
    rank = comp.tier
    division = comp.rank

    wins=comp.wins
    losses = comp.losses

    return {
        'tier': rank,
        'division': division,
        'lp': lp,
        'wins': wins,
        'losses': losses
    }

@resource_manager.as_decorator
async def get_rank_icon_path(division):
    """

    :param division: ranked division of summoner
    :return: absolute path for rank icon via cdragon
    """
    lower_case_div = division.lower()
    link=f'https://raw.communitydragon.org/latest/plugins/rcp-fe-lol-shared-components/global/default/images/{lower_case_div}.png'

    return link
@resource_manager.as_decorator
async def get_ladder_rank(summoner):
    """

    :param summoner: pyot summoner
    :return: ladder percentage of summoner
    """

    rank_to_percent = {
        "CHALLENGER": 0.024,
        "GRANDMASTER": 0.081,
        "MASTER": 0.531,

        "DIAMOND I": 0.921,
        "DIAMOND II": 1.381,
        "DIAMOND III": 2.011,
        "DIAMOND IV": 3.211,

        "EMERALD I": 4.211,
        "EMERALD II": 5.811,
        "EMERALD III": 8.411,
        "EMERALD IV": 13.711,

        "PLATINUM I": 15.711,
        "PLATINUM II": 18.811,
        "PLATINUM III": 22.911,
        "PLATINUM IV": 29.711,

        "GOLD I": 32.511,
        "GOLD II": 36.811,
        "GOLD III": 42.111,
        "GOLD IV": 50.111,

        "SILVER I": 53.111,
        "SILVER II": 57.511,
        "SILVER III": 62.711,
        "SILVER IV": 70.211,

        "BRONZE I": 73.711,
        "BRONZE II": 78.311,
        "BRONZE III": 83.511,
        "BRONZE IV": 90.811,

        "IRON I": 94.411,
        "IRON II": 97.311,
        "IRON III": 98.411,
        "IRON IV": 98.821

    }
    rank = await lol.SummonerLeague(summoner_id=summoner.id, platform='na1').get()

    rank = rank[0]

    rank = f'{rank.tier} {rank.rank}'

    rank_percentage = rank_to_percent[rank]

    return rank_percentage

@resource_manager.as_decorator
async def get_icon_path(summoner):
    icon = await summoner.profile_icon.get()
    path = icon.icon_abspath

    return path



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
