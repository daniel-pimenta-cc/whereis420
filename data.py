import json


timezones_data = [
    {
        "city": "Pago Pago",
        "country": "American Samoa",
        "timezone": "Pacific/Pago_Pago",
        "desc": "The territorial capital of American Samoa, an unincorporated territory of the U.S. located in the South Pacific Ocean, southeast of the independent state of Samoa.",
        "map": "map_pago_pago.png",
        "population": 3656,
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
        "population": 343302,
        "subdesc": [
            "It is an unincorporated county seat of the consolidated City and County of Honolulu, situated along the southwest coast of the island of O'ahu, and is the westernmost and southernmost major U.S. city. Honolulu is Hawaii's main gateway to the world.",
            "It is also a major hub for business, finance, hospitality, and military defense in both the state and Oceania. The city is characterized by a mix of various Asian, Western, and Pacific cultures, as reflected in its diverse demography, cuisine, and traditions.",
            "Honolulu means \"sheltered harbor\" or \"calm port\" in Hawaiian.",
            "Honolulu has been the capital of the Hawaiian Islands since 1845, first of the independent Hawaiian Kingdom, and after 1898 of the U.S. territory and state of Hawaii."
        ]
    },##"Rikitea"
    {
        "city": "Anchorage",
        "country": "USA",
        "timezone": "America/Anchorage",
        "desc": "A unified municipal consolidated city-borough in the U.S. state of Alaska, on the West Coast of the United States.",
        "map": "map_anchorage.png",
        "population": 291247,
        "subdesc": [
            "Due to its location, almost equidistant from New York City, Tokyo, and Frankfurt, Germany (across the Arctic Ocean), Anchorage lies within 10 hours by air of nearly 90% of the industrialized world.",
            "A diverse wildlife population exists within urban Anchorage and the surrounding area. Approximately 250 black bears and 60 grizzly bears live in the area. Bears are regularly sighted within the city.",
            "Anchorage's largest economic sectors include transportation, military, municipal, state and federal government, tourism, corporate headquarters (including regional headquarters for multinational corporations) and resource extraction.",
            "Anchorage has won the All-America City Award four times: in 1956, 1965, 1984–85, and 2002, from the National Civic League."
        ]
    },
    {
        "city": "Calgary",
        "country": "Canada",
        "timezone": "America/Edmonton",
        "desc": "A city in the Canadian province of Alberta. It is located at the confluence of the Bow River and the Elbow River in the south of the province, in an area of foothills and prairie, about 80 km (50 mi) east of the front ranges of the Canadian Rockies.",
        "map": "map_calgary.png",
        "population": 1239220,
        "subdesc": [
            "The city anchors the south end of what Statistics Canada defines as the \"Calgary–Edmonton Corridor\".",
            "The Calgary CMA is home to the second-highest number of head offices in Canada among the country's 800 largest corporations.",
            "Calgary is a hub for the energy industry, manufacturing, and high technology, and is home to the second-highest number of corporate head offices in Canada among the country's 800 largest corporations.",
            "Calgary is a major centre for the Canadian film industry, and was recently named \"Hollywood North\".",
        ]
    },
    {
        "city": "Los Angeles",
        "country": "USA",
        "timezone": "America/Los_Angeles",
        "desc": "Often referred to by its initials (L.A.), Los Angeles is a major city in the U.S. state of California. It is the largest city in the state, as well as the second-largest city in the United States following New York City.",
        "map": "map_los_angeles.png",
        "population": 3898747,
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
        "map": "map_san_jose.png",
        "population": 1013240,
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
        "map": "map_mexico_city.png",
        "population": 8918653,
        "subdesc": [
            "Mexico City is one of the most important cultural and financial centers in the Americas. It is located in the Valley of Mexico, a large valley in the high plateaus in the center of Mexico, at an altitude of 2,240 meters (7,350 ft).",
        ]

    },
    {
        "city": "Caracas",
        "country": "Venezuela",
        "timezone": "America/Caracas",
        "desc": "The capital, the center of the Greater Caracas Area, and the largest city of Venezuela.",
        "map": "map_caracas.png", 
        "population": 2245744,
        "subdesc": [
            "Caracas is the political, administrative and cultural center of Venezuela.",
            "The city is located in the northern part of the country, following the contours of the narrow Caracas Valley on the Venezuelan coastal mountain range, on the Caribbean Sea.",
        ]
    },
    {
        "city": "New York",
        "country": "USA",
        "timezone": "America/New_York",
        "desc": "The most populous city in the United States and the center of the New York Metropolitan Area, one of the most populous urban agglomerations in the world.",
        "map": "map_new_york.png",
        "population": 8336817,
        "subdesc": [
            "New York City has been described as the cultural, financial, and media capital of the world, significantly influencing commerce, entertainment, research, technology, education, politics, tourism, art, fashion, and sports.",
        ]
    },
    {
        "city": "São Paulo",
        "country": "Brazil",
        "timezone": "America/Sao_Paulo",
        "desc": "The most populous city in Brazil and the Americas, and the largest city in the Southern Hemisphere.",
        "map": "map_sao_paulo.png",
        "population": 22046000,
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "St. John's",
        "country": "Canada",
        "timezone": "America/St_Johns",
        "population": 111914,
        "map": "map_st_johns.png",
        "desc": "The capital and largest city of the Canadian province of Newfoundland and Labrador. It is on the eastern tip of the Avalon Peninsula on the island of Newfoundland.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Fernando de Noronha",
        "country": "Brazil",
        "timezone": "America/Noronha",
        "population": 3101,
        "map": "map_fernando_noronha.png",
        "desc": "An archipelago in the Atlantic Ocean, part of the State of Pernambuco, Brazil, and located 354km (220mi) offshore from the Brazilian coast. It consists of 21 islands and islets.",
         "subdesc": [
            "todo"
            ]
        
    },
    {
        "city": "Praia",
        "country": "Cape Verde",
        "timezone": "Atlantic/Cape_Verde",
        "population": 127832,
        "map": "map_praia.png",
        "desc": "The capital and largest city of Cape Verde. It is located on Santiago Island, the largest island of the archipelago.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Accra",
        "country": "Ghana",
        "timezone": "Africa/Accra",
        "population": 2291352,
        "map": "map_accra.png",
        "desc": "The capital and largest city of Ghana, with an estimated population of 2,291,352 as of 2012.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "London",
        "country": "UK",
        "timezone": "Europe/London",
        "population": 10979000,
        "map": "map_london.png",
        "desc": "The capital and largest city of England and the United Kingdom.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Cairo",
        "country": "Egypt",
        "timezone": "Africa/Cairo",
        "population": 19372000,
        "map": "map_cairo.png",
        "desc": "The capital and largest city of Egypt.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Moscow",
        "country": "Russia",
        "timezone": "Europe/Moscow",
        "population": 17125000,
        "map": "map_moscow.png",
        "desc": "The capital and most populous city of Russia, with 13.2 million residents within the city limits, 17 million within the urban area, and 20 million within the metropolitan area.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Baku",
        "country": "Azerbaijan",
        "timezone": "Asia/Baku",
        "population": 2181800,
        "map": "map_baku.png",
        "desc": "The capital and largest city of Azerbaijan, as well as the largest city on the Caspian Sea and of the Caucasus region.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Tehran",
        "country": "Iran",
        "timezone": "Asia/Tehran",
        "population": 13633000,
        "map": "map_tehran.png",
        "desc": "The capital of Iran and Tehran Province. With a population of around 8.7 million in the city proper and 15 million in the wider metropolitan area, it is the largest city in Western Asia and the second-largest in the Middle East.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Karachi",
        "country": "India",
        "timezone": "Asia/Karachi",
        "population": 14835000,
        "map": "map_karachi.png",
        "desc": "The capital of the Pakistani province of Sindh. It is the most populous city in Pakistan, and fifth-most-populous city proper in the world.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Mumbai",
        "country": "India",
        "timezone": "Asia/Kolkata",
        "population": 23355000,
        "map": "map_mumbai.png",
        "desc": "The capital city of the Indian state of Maharashtra. It is the most populous city in India with an estimated city population of 18.4 million.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Kathmandu",
        "country": "Nepal",
        "timezone": "Asia/Kathmandu",
        "population": 975453,
        "map": "map_kathmandu.png",
        "desc": "The capital and largest city of Nepal. It is the country's political, cultural, and economic center.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Dhaka",
        "country": "Bangladesh",
        "timezone": "Asia/Dhaka",
        "population": 1146053,
        "map": "map_dhaka.png",
        "desc": "The capital and largest city of Bangladesh. It is one of the world's most populated cities, with a population of 18 million people in the Greater Dhaka Area.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Yangon",
        "country": "Myanmar",
        "timezone": "Asia/Yangon",
        "population": 5514000,
        "map": "map_yangon.png",
        "desc": "The capital of Myanmar, and its largest city. It is the country's commercial, industrial, and financial centre, and home to the majority of the country's corporate offices.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Jakarta",
        "country": "Indonesia",
        "timezone": "Asia/Jakarta",
        "population": 34540000,
        "map": "map_jakarta.png",
        "desc": "The capital and largest city of Indonesia. Located on the northwest coast of the world's most populous island of Java, it is the centre of economy, culture and politics of Indonesia.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Shanghai",
        "country": "China",
        "timezone": "Asia/Shanghai",
        "population": 22120000,
        "map": "map_shanghai.png",
        "desc": "The most populous city proper in the world, with a population of more than 24 million as of 2014. It is one of the four direct-controlled municipalities of the People's Republic of China, with the status of a national central city.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Tokyo",
        "country": "Japan",
        "timezone": "Asia/Tokyo",
        "population": 37977000,
        "map": "map_tokyo.png",
        "desc": "Tokyo is the capital of Japan, the center of the Greater Tokyo Area, and the most populous metropolitan area in the world.",
         "subdesc": [
            "todo"
            ]
    },
    {
        "city": "Brisbane",
        "country": "Australia",
        "timezone": "Australia/Brisbane",
        "population": 2514184,
        "map": "map_brisbane.png",
        "desc": "Brisbane is the capital of and most populous city in the Australian state of Queensland, and the third most populous city in Australia.",
         "subdesc": [
            "todo"
            ]

    },
    {
        "city": "Port Vila",
        "country": "Vanuatu",
        "timezone": "Pacific/Efate",
        "population": 51437,
        "map": "map_port_vila.png",
        "desc": "Vanuatu is an island nation located in the South Pacific Ocean. It is made up of 83 islands, of which 65 are inhabited. The islands are located in the Melanesian subregion of Oceania, about 1,750 kilometres (1,090 mi) east of northern Australia and 500 kilometres (310 mi) northeast of New Caledonia.",
         "subdesc": [
            "todo"
            ]

    },
    {
        "city": "Suva",
        "country": "Fiji",
        "timezone": "Pacific/Fiji",
        "population": 77366,
        "map": "map_suva.png",
        "desc": "Suva is the capital and largest city of Fiji. It is located on the southeast coast of the island of Viti Levu, and is the country's major port and commercial centre.",
            "subdesc": [
                "todo"
            ]
    },
    {
        "city": "Auckland",
        "country": "New Zealand",
        "timezone": "Pacific/Auckland",
        "population": 1467800,
        "map": "map_auckland.png",
        "desc": "Auckland is a city in the North Island of New Zealand. It is the most populous urban area in the country, with an urban population of 1,495, which constitutes 32 percent of New Zealand's population.",
        "subdesc": [
            "todo"
            ]
    }
]
#function that reads a list and saves to a json file 
def write_json(data, filename='tz_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
write_json(timezones_data)
"""
 {
        "city": "Rikitea",
        "country": "French Polynesia",
        "timezone": "Pacific/Gambier",
        "desc": "A small town on Mangareva, which is part of the Gambier Islands in French Polynesia. A majority of the islanders live in Rikitea.",
        "map": "map_rikitea.png",
        "population": 1100,
        "subdesc": [
            "The island was a protectorate of France in 1871 and was annexed in 1881.",
            "Before the Catholic missionaries' arrival, cannibalism was practiced under the rule of the local kings.",
            "Black pearls are cultured on numerous platforms on both sides of the Mangareva lagoon. The lagoon is full of corals and black-lipped oysters are harvested by the people. The inhabitants are also involved in agriculture and fishing to the minimum level.",
            "The town is accessed by air and by ship. The airport is located on Mou Totegegie, 9km (5.6mi) northeast. From the airport, boats provide the only access to Rikitea."
        ]
    },
"""