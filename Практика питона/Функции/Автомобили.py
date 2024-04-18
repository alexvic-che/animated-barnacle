def auto_info(proizvoditel, marka, **kwargs):
    kwargs['marka']=marka
    kwargs['proizvoditel'] = proizvoditel
    return kwargs

print(auto_info('subaru', 'outback', color ='blue', tow_package = True))

