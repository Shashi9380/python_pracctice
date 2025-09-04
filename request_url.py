# import requests
# import pprint
# api_url='https://fakestoreapi.com/products/'
# out=requests.get(api_url)
# data=out.json()
# print(data[6].get('price'))
#------------------------------------------------------------------------

# import requests
# import pprint

# api_url = 'https://fakestoreapi.com/products/'
# out = requests.get(api_url)
# data = out.json()   # no arguments

# product_less_than_100 = []

# for d in data:
#     if d.get('price') > 100:
#         product_less_than_100.append(d)

# # pretty print
# pprint.pprint(product_less_than_100)

#----------------------------------------------

# import requests
# api_url='https://www.googleapis.com/books/v1/volumes?q=search+terms'
# out=requests.get(api_url)
# data=out.json()
# # print(data.get("items")[1].get('volumeInfo').get('industryIdentifiers')[0].get('type'))
# list_of_data=[]
# list_of_data2=[]
# for data1 in data.get("items",[]):
#     identifier=data1.get('volumeInfo',{}).get('industryIdentifiers',[])
#     list_of_data.append(identifier)
#     for data2 in identifier:
#         indentifier2=data2.get('type')
#         list_of_data2.append(indentifier2)
# print(list_of_data)
# print(f"----->{list_of_data2}")





