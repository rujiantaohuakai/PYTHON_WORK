from city_functions import get_city_countrys

def test_city_country():
    """测试get_city_countrys函数"""
    string = get_city_countrys('santiago', 'chile')
    assert string == 'Santiago, Chile'

def test_city_country_population():
    """"测试get_city_country()函数传入population时是否可以正常运行"""
    string = get_city_countrys('santiago', 'chile', 200000)
    assert string == 'Santiago, Chile - Population 200000'