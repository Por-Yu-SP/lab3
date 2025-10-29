import price_info

def test_total_cost_shopping():
    result=0
    mapin={'apple': 10, 'orange':10}
    price_info.quantity_list=mapin
    result=price_info.total_cost_shopping()
    assert(result==26)

def test_cost_of_fruits():
    result=0
    result=price_info.cost_of_fruits("apple",10)
    
    assert(result==12)
