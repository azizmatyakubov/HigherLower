from data import data

def get_info(position):
    name = data[position]['name']
    follower = data[position]['follower_count']
    desc = data[position]['description']
    country = data[position]['country']
    return name, follower, desc, country

print(get_info(1)[1])

# if data[0]['follower_count'] > data[1]['follower_count']:
#     print('Awesome')