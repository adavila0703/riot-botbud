from riotwatcher import LolWatcher, ApiError



def get_token():
    """Grabs the bot token from token.txt"""
    with open('token.txt', 'r') as g:
        lines = g.readlines()
        return lines[0].strip()

def get_summoner():
    """Grabs the bot token from token.txt"""
    with open('summoner.txt', 'r') as g:
        lines = g.readlines()
        return lines[0].strip()

lol_watcher = LolWatcher(get_token())

my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, get_summoner())
# matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
print(me)


'''
    Get player and parse for a single match
'''
# game = lol_watcher.match.by_id(my_region, '3797471598')
# get_part = ''
# for player in game['participantIdentities']:
#     if player['player']['accountId'] == me['accountId']:
#         get_part = player['participantId']

# stats = ''
# for player in game['participants']:
#     if player['participantId'] == get_part:
#         stats = player

# print(stats)


