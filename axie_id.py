
import requests
import csv
import pandas as pd

def get_query(id):
    if type(id) != type("1"):
        id = str(id)
    data = {"operationName": "GetAxieDetail", "variables": {"axieId": id},
            "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"}
    try:
        query = requests.post("https://graphql-gateway.axieinfinity.com/graphql", json=data, timeout=60).json()
    except Exception:
        return {"data": {"axie": {}}}
    if "errors" in query.keys():
        return {"data": {"axie": {}}}
    elif query ==None:
        return {"data": {"axie": {}}}
    elif query['data']['axie']['class'] == None:
        print(query)
        return {"data": {"axie": {}}}
        '''
    elif query['data']['axie']['auction'] ==None:
        return {"data": {"axie": {}}}
        '''
    elif query['data']['axie']['id'] == None:
        return {"data": {"axie": {}}}
    return query

axie_id=[]
axie_price =[]
axie_breedcount =[]
axie_class =[]
axie_birthDate =[]
axie_level =[]
axie_hp=[]
axie_speed=[]
axie_skill=[]
axie_morale=[]
axie_children=[]



#\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"}

aid = pd.read_excel("/mnt/c/Users/Runxin Li(Sally)/Desktop/S22/URP/axie_children.xls")
print(aid)



for i in list(aid.id): 
    axie = get_query(i)
    if axie == {"data": {"axie": {}}}:
        continue
    else:
        axie_id.append(axie['data']['axie']['id'])
        axie_breedcount.append(axie['data']['axie']['breedCount'])
        axie_class.append(axie['data']['axie']['class'])
        axie_level.append(axie['data']['axie']['level'])
        axie_birthDate.append(axie['data']['axie']['birthDate']) 
        axie_hp.append(axie['data']['axie']['stats']['hp'])
        axie_speed.append(axie['data']['axie']['stats']['speed'])
        axie_skill.append(axie['data']['axie']['stats']['skill'])
        axie_morale.append(axie['data']['axie']['stats']['morale'])
        if axie['data']['axie']['auction'] == None:
            axie_price.append('')
        else:
            axie_price.append(axie['data']['axie']['auction']['currentPriceUSD'])
        
        x = axie['data']['axie']['children']
        if len(x) == 0 :
            axie_children.append('')
            continue
        else:
            axie_children.append(x[0]['id']) 



dict ={'id':axie_id,
    'class':axie_class,
    'birthDate':axie_birthDate,
    'level':axie_level,
    'breedCount':axie_breedcount,
    'price':axie_price,
    'hp':axie_hp,
    'speed':axie_speed,
    'skill':axie_skill,
    'morale':axie_morale,
    'random_children_id':axie_children
    }

df = pd.DataFrame(dict)
print(df)

df.to_csv("/mnt/c/Users/Runxin Li(Sally)/Desktop/S22/URP/axie.csv")
