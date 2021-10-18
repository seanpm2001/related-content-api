import pytest
from components.vector_database_client import PineconeDatabaseClient, RelatedContentAPIMatchResult, RelatedContentAPIVectorResult
from components.config import PINECONE_API_KEY

def test_vector_match__success():
    example_vector = [0.2638701796531677, 0.5160582661628723, -0.18149864673614502, -0.991111159324646, 0.2768683433532715, 0.46175941824913025, 0.24879662692546844, -0.14384296536445618, -0.269498735666275, 0.7469941973686218, -0.3426071107387543, -0.9443876147270203, 0.31081005930900574, 1.6447044610977173, -0.2656041383743286, -0.08440074324607849, 0.6642885208129883, 1.214737892150879, -0.4521683156490326, 0.5811796188354492, -0.7611883878707886, 0.416707307100296, -1.8945564031600952, 0.3314112722873688, -0.45172491669654846, 1.0741323232650757, -0.34206491708755493, 0.20729120075702667, -0.7592663764953613, 0.14651677012443542, -0.5881195068359375, -0.2332741916179657, 1.5477606058120728, -0.6873889565467834, -0.18190248310565948, 0.3139747977256775, -1.3622348308563232, -0.7203295826911926, -0.7657942175865173, -0.8103228211402893, -0.3854348361492157, 0.6376134753227234, -0.3906760513782501, -0.5138159394264221, 0.6040557026863098, -1.6061419248580933, -0.07631140947341919, 0.49947839975357056, 0.17975419759750366, -0.2522033751010895, 0.9364824891090393, -0.7544165253639221, 1.4769717454910278, -0.1995634287595749, 1.9286843538284302, -0.29737621545791626, 2.513138771057129, 1.0205371379852295, -0.5144957304000854, 0.7946041822433472, 0.4893866181373596, 0.327226459980011, -1.3830622434616089, -0.9544669985771179, 1.0765365362167358, -0.6003585457801819, 0.5026446580886841, 0.175935298204422, 0.7985385656356812, -0.4543401002883911, -0.6965981721878052, 0.5565392374992371, 0.7568541169166565, -0.776771605014801, 0.025461729615926743, 1.124318242073059, 1.8544178009033203, 0.45317190885543823, -0.04962131753563881, 0.19125911593437195, -0.09056463837623596, 0.7925125956535339, 0.10024502128362656, -0.6358148455619812, -1.420487880706787, 0.41904914379119873, 0.8460859656333923, -1.5624686479568481, 0.042782481759786606, 0.05711445212364197, 0.4978751540184021, 0.15718768537044525, -1.4348909854888916, -0.060476403683423996, 0.18165148794651031, 1.3510719537734985, 0.6770476698875427, -0.44023430347442627, 1.228079080581665, 0.9392477869987488, -0.30040258169174194, 0.3026198446750641, -0.16561874747276306, -0.034369707107543945, -0.5200393795967102, -0.18416905403137207, -1.236165165901184, 0.09145450592041016, 1.0897784233093262, 0.42927277088165283, 1.1280657052993774, -0.12206599861383438, 0.13479815423488617, -0.16443049907684326, -1.3457432985305786, -0.4790014922618866, -1.0645427703857422, -0.5057504773139954, -0.8773223161697388, 0.16182026267051697, -0.18219000101089478, 0.8743749856948853, 0.1789899617433548, -0.5526484251022339, -0.04050407186150551, -1.8230023384094238, -0.5062934160232544, 0.8073083162307739, 2.2526938915252686, 1.0937288999557495, -0.045786481350660324, -0.7482342720031738, -0.019202927127480507, -0.9820873141288757, 0.07853975892066956, -0.09273453801870346, 0.09668227285146713, -0.4091567099094391, 0.46086448431015015, 0.18675196170806885, -1.7540793418884277, -1.339260220527649, -1.7988088130950928, 1.897867202758789, -0.3047731816768646, 1.1655666828155518, -0.4215647578239441, 0.6730325222015381, -0.24517039954662323, 0.5635324120521545, -0.2568920850753784, -0.20982883870601654, -0.0579717755317688, -0.4640026092529297, 0.4574117362499237, 1.1449317932128906, 1.0490926504135132, -1.9315433502197266, -0.5464723110198975, 0.24159979820251465]
    client = PineconeDatabaseClient(api_key=PINECONE_API_KEY)
    result = client.get_similar_vectors(key_vector=example_vector)
    assert isinstance(result, RelatedContentAPIMatchResult)

def test_get_vector__success():
    example_url = "https://waitbutwhy.com/2014/06/taming-mammoth-let-peoples-opinions-run-life.html"
    client = PineconeDatabaseClient(api_key=PINECONE_API_KEY)
    result = client.get_vector(url=example_url)
    assert isinstance(result, RelatedContentAPIVectorResult)


