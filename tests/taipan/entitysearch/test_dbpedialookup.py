"""Test for taipan.dbpedialookup"""

from taipan.entitysearch.dbpedialookup import lookup_dbpedia_entity, \
    disambiguate_table, disambiguate_table_subject_column_only
from taipan.ml.model import MLModel
from taipan.generictable import GenericTable


def test_lookup_dbpedia_entity():
    _entity = lookup_dbpedia_entity("Berlin")
    assert _entity == ["http://dbpedia.org/resource/Berlin"]


def test_lookup_dbpedia_entity_dont_exist():
    _entity = lookup_dbpedia_entity("fdsoiajoij foidjsafp odij pfoij")
    assert _entity == []

TABLE_ENTITIES = [[['http://dbpedia.org/resource/Portuguese_language'], ['http://dbpedia.org/resource/United_States_dollar'], []],
 [['http://dbpedia.org/resource/Australia'], ['http://dbpedia.org/resource/Australian_dollar'], []],
 [['http://dbpedia.org/resource/Bangladesh'], ['http://dbpedia.org/resource/United_States_dollar'], []],
 [['http://dbpedia.org/resource/Cambodia'], ['http://dbpedia.org/resource/United_States_dollar'], []],
 [['http://dbpedia.org/resource/Canada'], ['http://dbpedia.org/resource/Canadian_dollar'], []],
 [['http://dbpedia.org/resource/France'], ['http://dbpedia.org/resource/Euro'], []],
 [['http://dbpedia.org/resource/Germany'], ['http://dbpedia.org/resource/Euro'], []],
 [['http://dbpedia.org/resource/Hong_Kong'], ['http://dbpedia.org/resource/Hong_Kong_dollar'], []],
 [['http://dbpedia.org/resource/India'], ['http://dbpedia.org/resource/Indian_rupee'], []],
 [['http://dbpedia.org/resource/Indonesia'], ['http://dbpedia.org/resource/United_States_dollar'], []],
 [['http://dbpedia.org/resource/Italy'], ['http://dbpedia.org/resource/Euro'], []],
 [['http://dbpedia.org/resource/Japan'], ['http://dbpedia.org/resource/Japanese_yen'], []],
 [['http://dbpedia.org/resource/South_Korea'], ['http://dbpedia.org/resource/South_Korean_won'], []],
 [['http://dbpedia.org/resource/Malaysia'], ['http://dbpedia.org/resource/Malaysian_ringgit'], []],
 [['http://dbpedia.org/resource/Nepal'], ['http://dbpedia.org/resource/United_States_dollar'], []],
 [['http://dbpedia.org/resource/New_Zealand'], ['http://dbpedia.org/resource/New_Zealand_dollar'], []],
 [['http://dbpedia.org/resource/Papua_New_Guinea'], ['http://dbpedia.org/resource/Papua_New_Guinean_kina'], []],
 [[], ['http://dbpedia.org/resource/Renminbi'], []],
 [['http://dbpedia.org/resource/Philippines'], ['http://dbpedia.org/resource/United_States_dollar'], []],
 [['http://dbpedia.org/resource/Portugal'], ['http://dbpedia.org/resource/Euro'], []]]



def test_disambiguate_table():
    mlmodel = MLModel()
    table = mlmodel.get_tables()[0]
    entities = disambiguate_table(table)
    assert entities == TABLE_ENTITIES


TABLE_ENTITIES_SC_ONLY = [
 [['http://dbpedia.org/resource/Portuguese_language'], [], []],
 [['http://dbpedia.org/resource/Australia'], [], []],
 [['http://dbpedia.org/resource/Bangladesh'], [], []],
 [['http://dbpedia.org/resource/Cambodia'], [], []],
 [['http://dbpedia.org/resource/Canada'], [], []],
 [['http://dbpedia.org/resource/France'], [], []],
 [['http://dbpedia.org/resource/Germany'], [], []],
 [['http://dbpedia.org/resource/Hong_Kong'], [], []],
 [['http://dbpedia.org/resource/India'], [], []],
 [['http://dbpedia.org/resource/Indonesia'], [], []],
 [['http://dbpedia.org/resource/Italy'], [], []],
 [['http://dbpedia.org/resource/Japan'], [], []],
 [['http://dbpedia.org/resource/South_Korea'], [], []],
 [['http://dbpedia.org/resource/Malaysia'], [], []],
 [['http://dbpedia.org/resource/Nepal'], [], []],
 [['http://dbpedia.org/resource/New_Zealand'], [], []],
 [['http://dbpedia.org/resource/Papua_New_Guinea'], [], []],
 [[], [], []],
 [['http://dbpedia.org/resource/Philippines'], [], []],
 [['http://dbpedia.org/resource/Portugal'], [], []]
]
def test_disambiguate_table_subject_column_only():
    mlmodel = MLModel()
    table = mlmodel.get_tables()[0]
    entities = disambiguate_table_subject_column_only(table)
    assert entities == TABLE_ENTITIES_SC_ONLY

CASE_1_TABLE = [['rank', 'airport', 'location', 'code(iata/icao)', 'totalpassengers', 'monthly rankchange', '%change'],
 ['1.', 'london heathrow airport', '{hillingdon|greater london|england|united kingdom}', 'lhr/egll', '40239190', 'NULL', '0.8%'],
 ['2.', 'paris charles de gaulle airport', "{roissy-en-france|val d'oise|île-de-france|france}", 'cdg/lfpg', '35526374', 'NULL', '0.8%'],
 ['3.', 'hong kong international airport', '{chek lap kok|new territories|hong kong}', 'hkg/vhhh', '33178000', 'NULL', '10.9%'],
 ['4.', 'frankfurt airport', '{flughafen (frankfurt am main)|frankfurt|hesse|germany}', 'fra/eddf', '30636917', '1', '3.0%'],
 ['5.', 'dubai international airport', '{garhoud|dubai|united arab emirates}', 'dxb/omdb', '30275671', '1', '14.9%'],
 ['6.', 'amsterdam airport schiphol', '{haarlemmermeer|north holland|netherlands}', 'ams/eham', '29837136', 'NULL', '2.0%'],
 ['7.', 'singapore changi airport', '{changi|east region|singapore}', 'sin/wsss', '26625327', 'NULL', '16.4%'],
 ['8.', 'incheon international airport', '{jung-gu|incheon|sudogwon|south korea}', 'icn/rksi', '21961033', '1', '16.9%'],
 ['9.', 'narita international airport', '{narita|chiba|kantō|honshū|japan}', 'nrt/rjaa', '21919378', '1', '8.5%'],
 ['10.', 'madrid-barajas airport', '{madrid|comunidad de madrid|spain}', 'mad/lemd', '20636095', '1', '5.4%'],
 ['11.', 'suvarnabhumi airport', '{racha thewa|bang phli|samut prakan|greater bangkok|thailand}', 'bkk/vtbs', '20297696', '1', '10.1%'],
 ['12.', 'london gatwick airport', '{crawley|west sussex|south east england|england|united kingdom}', 'lgw/egkk', '18958570', 'NULL', '3.5%'],
 ['13.', 'munich airport', '{oberding|hallbergmoos|marzling|erding|freising|bavaria|germany}', 'muc/eddm', '16499651', 'NULL', '6.6%'],
 ['14.', 'taoyuan international airport', '{dayuan|taoyuan|taiwan|republic of china}', 'tpe/rctp', '15643881', 'NULL', '22.0%'],
 ['15.', 'leonardo da vinci airport', '{fiumicino|rome|italy}', 'fco/lirf', '15578911', '2', '11.5%'],
 ['16.', 'john f. kennedy international airport', '{queens|new york city|new york|united states}', 'jfk/kjfk', '15573060', 'NULL', '6.2%'],
 ['17.', 'atatürk international airport', '{yeşilköy|bakırköy|istanbul|turkey}', 'ist/ltba', '15128270', '1', '16.0%'],
 ['18.', 'kuala lumpur international airport', '{sepang|selangor|malaysia}', 'kul/wmkk', '15087900', '2', '23.5%'],
 ['19.', 'zürich airport', '{rümlang|oberglatt|bülach|dielsdorf|zürich|switzerland}', 'zrh/lszh', '13261266', 'NULL', '3.6%'],
 ['20.', 'toronto pearson international airport', '{mississauga|ontario|canada}', 'yyz/cyyz', '13115781', '1', '8.1%'],
 ['21.', 'copenhagen airport', '{kastrup|tårnby|hovedstaden|denmark}', 'cph/ekch', '12591944', 'NULL', '5.9%'],
 ['22.', 'sydney international airport', '{sydney|new south wales|sydney cbd|australia}', 'syd', '12409324', '1', '7.4%'],
 ['23.', 'antalya airport', '{antalya|turkey}', 'ayt/ltai', '12264370', '4', '19.2%'],
 ['24.', 'dublin airport', '{dublin|leinster|republic of ireland}', 'dub/eidw', '12258434', '1', '11.4%'],
 ['25.', 'malpensa airport', '{somma lombardo|varese|lombardy|italy}', 'mxp/limc', '11635598', '1', '4.0%'],
 ['26.', 'barcelona airport', '{el prat de llobregat|barcelona|catalonia|spain}', 'bcn/lebl', '11499909', '2', '4.3%'],
 ['27.', 'london stansted airport', '{stansted mountfitchet|essex|east of england|england|united kingdom}', 'stn/egss', '11459549', 'NULL', '7.3%'],
 ['28', 'miami international airport', '{miami-dade county|florida|united states}', 'mia/kmia', '11416988', '4', '5.3%'],
 ['29.', 'brussels airport', '{zaventem|flemish brabant|flanders|belgium}', 'bru/ebbr', '11231417', 'NULL', '1.0%'],
 ['30.', 'palma de mallorca airport', '{palma|majorca|balearic islands|spain}', 'pmi/lepa', '10646606', 'NULL', '0.9%']]

def test_disambiguate_table_subject_column_only_case_1():
    table = GenericTable()
    table.table = CASE_1_TABLE
    table.subject_column = 1
    entities = disambiguate_table_subject_column_only(table)
    import ipdb; ipdb.set_trace()
