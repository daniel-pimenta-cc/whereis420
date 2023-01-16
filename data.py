import json


timezones = [
    {
        "city": "Pago Pago",
        "country": "American Samoa",
        "timezone": "Pacific/Pago_Pago",
        "desc": "The territorial capital of American Samoa, an unincorporated territory of the U.S. located in the South Pacific Ocean, southeast of the independent state of Samoa.",
        "map": "map_pago_pago.png",
        "population": {
            "count": 3656,
            "year": 2010
        },
        "subdesc": [
            "It is home to one of the deepest natural deepwater harbors in the South Pacific Ocean, sheltered from wind and rough seas, and strategically located.",
            "Pago Pago's harbor is also one of the best protected in the South Pacific which gives American Samoa a natural advantage because it makes landing fish for processing easier.",
            "Tourism, entertainment, food, and tuna canning are its main industries.",
            "The total value of fish landed in Pago Pago — about $200,000,000 annually — is higher than in any other port in any U.S. state or territory.",
            "As of 1993, Pago Pago was the world's fourth-largest tuna processor."
        ]
    },
    {
        "city": "Honolulu",
        "country": "U.S.A.",
        "timezone": "Pacific/Honolulu",
        "desc": "The capital and largest city of the U.S. state of Hawaii, which is located in the Pacific Ocean.",
        "map": "map_honolulu.png",
        "population": {
            "count": 343302,
            "year": 2020
        },
        "subdesc": [
            "It is an unincorporated county seat of the consolidated City and County of Honolulu, situated along the southwest coast of the island of O'ahu, and is the westernmost and southernmost major U.S. city. Honolulu is Hawaii's main gateway to the world.",
            "It is also a major hub for business, finance, hospitality, and military defense in both the state and Oceania. The city is characterized by a mix of various Asian, Western, and Pacific cultures, as reflected in its diverse demography, cuisine, and traditions.",
            "Honolulu means \"sheltered harbor\" or \"calm port\" in Hawaiian.",
            "Honolulu has been the capital of the Hawaiian Islands since 1845, first of the independent Hawaiian Kingdom, and after 1898 of the U.S. territory and state of Hawaii."
        ]
    },
    {
        "city": "Rikitea",
        "country": "French Polynesia",
        "timezone": "Pacific/Gambier",
        "desc": "A small town on Mangareva, which is part of the Gambier Islands in French Polynesia. A majority of the islanders live in Rikitea.",

        "population": {
            "count": 1100,
            "year": False
        },
        "subdesc": [
            "The island was a protectorate of France in 1871 and was annexed in 1881.",
            "Before the Catholic missionaries' arrival, cannibalism was practiced under the rule of the local kings.",
            "Black pearls are cultured on numerous platforms on both sides of the Mangareva lagoon. The lagoon is full of corals and black-lipped oysters are harvested by the people. The inhabitants are also involved in agriculture and fishing to the minimum level.",
            "The town is accessed by air and by ship. The airport is located on Mou Totegegie, 9km (5.6mi) northeast. From the airport, boats provide the only access to Rikitea."
        ]
    },
    {
        "city": "Anchorage",
        "country": "USA",
        "timezone": "America/Anchorage",
        "desc": "A unified municipal consolidated city-borough in the U.S. state of Alaska, on the West Coast of the United States.",
        "population": {
            "count": 291247,
            "year": 2020
        },
        "subdesc": [
            "Due to its location, almost equidistant from New York City, Tokyo, and Frankfurt, Germany (across the Arctic Ocean), Anchorage lies within 10 hours by air of nearly 90% of the industrialized world.",
            "A diverse wildlife population exists within urban Anchorage and the surrounding area. Approximately 250 black bears and 60 grizzly bears live in the area. Bears are regularly sighted within the city.",
            "Anchorage's largest economic sectors include transportation, military, municipal, state and federal government, tourism, corporate headquarters (including regional headquarters for multinational corporations) and resource extraction.",
            "Anchorage has won the All-America City Award four times: in 1956, 1965, 1984–85, and 2002, from the National Civic League."
        ]
    },
    {
        "city": "Los Angeles",
        "country": "USA",
        "timezone": "America/Los_Angeles",
        "desc": "Often referred to by its initials (L.A.), Los Angeles is a major city in the U.S. state of California. It is the largest city in the state, as well as the second-largest city in the United States following New York City.",
        "population": {
            "count": 3898747,
            "year": 2020
        },
        "subdesc": [
            "Los Angeles is known for its Mediterranean climate, ethnic and cultural diversity, Hollywood film industry, and sprawling metropolitan area.",
            "The English pronunciation of the name of the city has varied over time.",
            "Los Angeles is subject to earthquakes because of its location on the Pacific Ring of Fire. The geologic instability has produced numerous faults, which cause approximately 10,000 earthquakes annually in Southern California, though most of them are too small to be felt.",
            "Los Angeles is often billed as the \"Creative Capital of the World\" because one in every six of its residents works in a creative industry and there are more artists, writers, filmmakers, actors, dancers and musicians living and working in Los Angeles than any other city at any other time in history."
        ]
    },
    {
        "city": "San José",
        "country": "USA",
        "timezone": "America/Costa_Rica",
        "desc": "A major city in the U.S. state of California that is the cultural, financial, and political center of Silicon Valley and largest city in Northern California by both population and area.",
        "population": {
            "count": 1013240,
            "year": 2020
        },
        "subdesc": [
            "San José is notable for its innovation, cultural diversity, affluence, and sunny and mild Mediterranean climate.",
            "Its connection to the booming high tech industry phenomenon known as Silicon Valley sparked Mayor Tom McEnery to adopt the city the motto of \"Capital of Silicon Valley\" in 1988.",
            "Major global tech companies including Cisco Systems, eBay, Adobe Inc., PayPal, Broadcom, Samsung, Acer, and Zoom maintain their headquarters in San José.",
            "San José is named after <i>el Pueblo de San José de Guadalupe</i> (Spanish for \"the Town of Saint Joseph on the Guadalupe\"), the city's predecessor, which was eventually located in the area of what is now the Plaza de César Chávez."
        ]
    },
    {
        "city": "Mexico City",
        "country": "Mexico",
        "timezone": "America/Mexico_City",
        "desc": "The capital and largest city of Mexico and the most populous city in North America.",
        "population": {
            "count": 8918653,
            "year": 2020
        },
        "subdesc": [
            "Mexico City is one of the most important cultural and financial centers in the Americas. It is located in the Valley of Mexico, a large valley in the high plateaus in the center of Mexico, at an altitude of 2,240 meters (7,350 ft).",
        ]

    },
    {
        "city": "New York",
        "country": "USA",
        "timezone": "America/New_York",
        "desc": "The most populous city in the United States and the center of the New York Metropolitan Area, one of the most populous urban agglomerations in the world.",
        "population": {
            "count": 8336817,
            "year": 2020
        },
        "subdesc": [
            "New York City has been described as the cultural, financial, and media capital of the world, significantly influencing commerce, entertainment, research, technology, education, politics, tourism, art, fashion, and sports.",
        ]
    },
    {
        "city": "São Paulo",
        "country": "Brazil",
        "timezone": "America/Sao_Paulo",
        "population": 22046000
    },
    {
        "city": "St. John's",
        "country": "Canada",
        "timezone": "America/St_Johns",
        "population": 111914
    },
    {
        "city": "Fernando de Noronha",
        "country": "Brazil",
        "timezone": "America/Noronha",
        "population": 3101,
        "desc": "An archipelago in the Atlantic Ocean, part of the State of Pernambuco, Brazil, and located 354km (220mi) offshore from the Brazilian coast. It consists of 21 islands and islets."
    },
    {
        "city": "Praia",
        "country": "Cape Verde",
        "timezone": "Atlantic/Cape_Verde",
        "population": 127832
    },
    {
        "city": "Accra",
        "country": "Ghana",
        "timezone": "Africa/Accra",
        "population": 2291352
    },
    {
        "city": "London",
        "country": "UK",
        "timezone": "Europe/London",
        "population": 10979000
    },
    {
        "city": "Cairo",
        "country": "Egypt",
        "timezone": "Africa/Cairo",
        "population": 19372000
    },
    {
        "city": "Moscow",
        "country": "Russia",
        "timezone": "Europe/Moscow",
        "population": 17125000
    },
    {
        "city": "Baku",
        "country": "Azerbaijan",
        "timezone": "Asia/Baku",
        "population": 2181800
    },
    {
        "city": "Tehran",
        "country": "Iran",
        "timezone": "Asia/Tehran",
        "population": 13633000
    },
    {
        "city": "Karachi",
        "country": "India",
        "timezone": "Asia/Karachi",
        "population": 14835000
    },
    {
        "city": "Mumbai",
        "country": "India",
        "timezone": "Asia/Kolkata",
        "population": 23355000
    },
    {
        "city": "Kathmandu",
        "country": "Nepal",
        "timezone": "Asia/Kathmandu",
        "population": 975453
    },
    {
        "city": "Dhaka",
        "country": "Bangladesh",
        "timezone": "Asia/Dhaka",
        "population": 1146053
    },
    {
        "city": "Yangon",
        "country": "Myanmar",
        "timezone": "Asia/Yangon",
        "population": 5514000
    },
    {
        "city": "Jakarta",
        "country": "Indonesia",
        "timezone": "Asia/Jakarta",
        "population": 34540000
    },
    {
        "city": "Shanghai",
        "country": "China",
        "timezone": "Asia/Shanghai",
        "population": 22120000
    },
    {
        "city": "Tokyo",
        "country": "Japan",
        "timezone": "Asia/Tokyo",
        "population": 37977000
    },
    {
        "city": "Brisbane",
        "country": "Australia",
        "timezone": "Australia/Brisbane",
        "population": 2514184
    },
    {
        "city": "Port Vila",
        "country": "Vanuatu",
        "timezone": "Pacific/Efate",
        "population": 51437
    },
    {
        "city": "Auckland",
        "country": "New Zealand",
        "timezone": "Pacific/Auckland",
        "population": 1467800
    }
]
br_counter =0 
#function that reads a list and saves to a json file 
def write_json(data, filename='tz_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
write_json(timezones)