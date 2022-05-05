restaurants_list = [
    {
        "name": "Lamen Kazu",
        "review": 4.8,
        "distance": 0.7
    },
    {
        "name": "O Mineiro",
        "review": 4.2,
        "distance": 1.7
    },
    {
        "name": "Amor Aos Pedaços - Shopping",
        "review": 4.3,
        "distance": 1.2
    },
    {
        "name": "Mr. Pretzels - Pátio Paulista",
        "review": 4.7,
        "distance": 1.1
    },
    {
        "name": "We Coffee",
        "review": 4.5,
        "distance": 0.8
    },
    {
        "name": "Brigaderia Shopping Paulista",
        "review": 4.7,
        "distance": 1.2
    }
]

def orderByDistance(item):
    return item['distance'] 

def orderByReview(item):
    return item['review']

restaurants_list.sort(key=orderByReview, reverse=True)

temp = []
x = 1



for restaurant in restaurants_list:
    if x < len(restaurants_list) - 1:
        if restaurant['review'] == restaurants_list[x]['review']:
            if restaurant['distance'] > restaurants_list[x]['distance']:
                temp.append(restaurant)
                temp.append(restaurants_list[x])
                restaurants_list.insert(x, temp[0])
                restaurants_list.insert(x - 1, temp[1])
                temp = []

                
                for restaurant in restaurants_list:
                    o = 0
                    z = 1
                    y = 0
                    while z < len(restaurants_list):
                        if restaurant['name'] == restaurants_list[z]['name']:
                            y += 1
                            
                            if y > 1:
                                while restaurant['review'] != restaurants_list[o]['review']:
                                    o += 1
                                if restaurants_list[o]['distance'] > restaurants_list[o + 1]['distance']:
                                    restaurants_list.remove(restaurants_list[z])
                                else:
                                    restaurants_list.reverse()
                                    restaurants_list.remove(restaurants_list[z])
                                    restaurants_list.reverse()

                                z -= 1

                        z += 1
                     
        x += 1
        

for restaurant in restaurants_list:
    print(restaurant['name'], restaurant['review'], restaurant['distance'])

