import requests # Thư viện gọi API


url = 'http://sieunhangao.test.loclx.io/api/?user_id=nam'

result = requests.get(url) 

status_code = result.status_code 
print(status_code)

print(result.text)
'''
NOTE: Một số status code
200: OK
401:
403: Forbidden (authorization)
404: Not found
405: Method Not Allowed
500: Internal Server Error
502: Bad Gateway 
Link: https://restfulapi.net/http-status-codes/
'''

'''
print(result.text)          # API dạng str
print(type(result.text))    # => <class 'str'>
print(result.json())        # API dạng list
print(type(result.json()))  # => <class 'list'>
'''
# final = result.json()
'''
print(final['aaaaa'])       # => KeyError: 'aaaaa'
print(final.get('aaaaa'))   # => None (nên dùng để hạn chế lỗi)
'''

# print(final)