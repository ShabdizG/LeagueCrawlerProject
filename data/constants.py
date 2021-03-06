from pymongo import *

db = MongoClient('mongodb://localhost:27017/').LeagueCrawler


# PATCHES #

PATCHES_regex = ["6\.23\..*", "6\.24\..*", "7\.1\..*", "7\.2\..*", "7\.3\..*", "7\.4\..*", "7\.5\..*", "7\.6\..*",
                 "7\.7\..*", "7\.8\..*", "7\.9\..*", "7\.10\..*", "7\.11\..*", "7\.12\..*", "7\.13\..*", "7\.15\. .*",
                 "7\.16\. .*", "7\.17\. .*", "7\.18\. .*"]

PATCHES = ["6.23", "6.24", "7.1", "7.2", "7.3", "7.4", "7.5", "7.6",
           "7.7", "7.8", "7.9", "7.10", "7.11", "7.12", "7.13", "7.14", "7.15",
           "7.16", "7.17", "7.18"]

PATCH_ITERATIONS = ["6.23.1", "6.24.1", "7.1.1", "7.2.1", "7.3.1", "7.4.1", "7.5.1", "7.6.1",
                    "7.7.1", "7.8.1", "7.9.1", "7.10.1", "7.11.1", "7.12.1", "7.13.1", "7.14.1", "7.15.1",
                    "7.16.1", "7.17.1", "7.18.1"]

ALL_GAME_VERSIONS = ["7.18.1", "7.17.2", "7.17.1", "7.16.1", "7.15.1", "7.14.1", "7.13.1", "7.12.1", "7.11.1", 
                     "7.10.1", "7.9.2", "7.9.1", "7.8.1", "7.7.1", "7.6.1", "7.5.2", "7.5.1", "7.4.3", "7.4.2", 
                     "7.4.1", "7.3.3", "7.3.2", "7.3.1", "7.2.1", "7.1.1", "6.24.1", "6.23.1", "6.22.1", "6.21.1", 
                     "6.20.1", "6.19.1", "6.18.1", "6.17.1", "6.16.2", "6.16.1", "6.15.1", "6.14.2", "6.14.1", "6.13.1", 
                     "6.12.1", "6.11.1", "6.10.1", "6.9.1", "6.8.1", "6.7.1", "6.6.1", "6.5.1", "6.4.2", "6.4.1",
                     "6.3.1", "6.2.1", "6.1.1", "5.24.2", "5.24.1", "5.23.1", "5.22.3", "5.22.2", "5.22.1", "5.21.1",
                     "5.20.1", "5.19.1", "5.18.1", "5.17.1", "5.16.1", "5.15.1", "5.14.1", "5.13.1", "5.12.1", "5.11.1",
                     "5.10.1", "5.9.1", "5.8.1", "5.7.2", "5.7.1", "5.6.2", "5.6.1", "5.5.3", "5.5.2", "5.5.1", "5.4.1",
                     "5.3.1", "5.2.2", "5.2.1", "5.1.2", "5.1.1", "4.21.5", "4.21.4", "4.21.3", "4.21.1", "4.20.2",
                     "4.20.1", "4.19.3", "4.19.2", "4.18.1", "4.17.1", "4.16.1", "4.15.1", "4.14.2", "4.13.1", "4.12.2",
                     "4.12.1", "4.11.3", "4.10.7", "4.10.2", "4.9.1", "4.8.3", "4.8.2", "4.8.1", "4.7.16", "4.7.9",
                     "4.7.8", "4.6.3", "4.5.4", "4.4.3", "4.4.2", "4.3.18", "4.3.12", "4.3.10", "4.3.4", "4.3.2",
                     "4.2.6", "4.2.5", "4.2.1", "4.1.43", "4.1.41", "4.1.13", "4.1.9", "4.1.2", "3.15.5", "3.15.4",
                     "3.15.2", "3.14.41", "3.14.23", "3.14.22", "3.14.20", "3.14.19", "3.14.16", "3.14.13", "3.14.12",
                     "3.13.24", "3.13.8", "3.13.6", "3.13.1", "3.12.37", "3.12.36", "3.12.34", "3.12.33", "3.12.26",
                     "3.12.24", "3.12.2", "3.11.4", "3.11.2", "3.10.6", "3.10.3", "3.10.2", "3.9.7", "3.9.5", "3.9.4",
                     "3.8.5", "3.8.3", "3.8.1", "3.7.9", "3.7.2", "3.7.1", "3.6.15", "3.6.14", "0.154.3", "0.154.2",
                     "0.153.2", "0.152.115", "0.152.108", "0.152.107", "0.152.55", "0.151.101", "0.151.2"]


# REGIONS #

PLATFORMS = ["EUW1", "KR", "NA1", "BR1"]

# see: https://developer.riotgames.com/regional-endpoints.html
ALL_PLATFORMS = ["ru", "br1", "oc1", "jp1", "na1", "eun1", "euw1", "tr1", "la1", "la2"]
# pbe1 not working for some reason


# CHAMPIONS #

ADC_CHAMPIONS_DICT = {
    22: "Ashe",
    51: "Caitlyn",
    119: "Draven",
    81: "Ezreal",
    202: "Jhin",
    222: "Jinx",
    429: "Kalista",
    96: "Kog'Maw",
    236: "Lucian",
    21: "Miss Fortune",
    15: "Sivir",
    18: "Tristana",
    29: "Twitch",
    110: "Varus",
    67: "Vayne",
    498: "Xayah"
}


# ITEMS #

ADC_TIER_3_ITEMS_LIST = [
                        3031,  # Infinity Edge
                        3508,  # Essence Reaver
                        3042,  # Muramana
                        3004,  # Manamune
                        3025,  # Iceborn Gauntlet
                        3078,  # Trinity Force
                        3085,  # Runaan's
                        3094,  # Rapid Firecannon
                        3087,  # Statikk Shiv
                        3046,  # Phantom Dancer
                        3072,  # Bloodthirster
                        3155,  # Hexdrinker
                        3156,  # Maw of Malmortius
                        3153,  # BORK
                        3124,  # Guinsoo's Rageblade
                        3812,  # Death's Dance
                        3091,  # Wit's End
                        3071,  # Black Cleaver
                        3814,  # Edge of Night
                        3147,  # Duskblade
                        3142,  # Ghostblade
                         ]

ADC_TIER_3_ITEMS_DICT = {
    3031: "IE",
    3508: "ER",
    3004: "MM",
    3043: "MM",
    3025: "IBG",
    3078: "Tri",
    3085: "Runaan's",
    3094: "RFC",
    3087: "StS",
    3046: "PD",
    3072: "BT",
    3812: "DD",
    3155: "Maw/Hex",
    3156: "Maw/Hex",
    3153: "BORK",
    3124: "RB",
    3091: "WE",
    3071: "BC",
    3814: "EoN",
    3147: "DB",
    3142: "GB"
    # Guardian Angel, Scimitar (QSS), Last Whisper (Lord Dominik's, Mortal Reminder)
    # Boots, Masteries, Runes
}

ADC_RELEVANT_ITEMS = [
    1055,   # dorans blade
    1056,   # dorans ring
    1054,   # dorans shield
    1083,   # cull
    1036,   # long sowrd
    1042,   # dagger
    1051,   # brawler's gloves
    1018,   # cloak of agility
    1028,   # ruby crystal
    1027,   # saphire crystal
    3067,   # kindlegem
    1029,   # cloth armor
    1031,   # chain vest
    1033,   # null magic mantle
    1057,   # negatron cloak
    3140,   # qss
    1026,   # blasting wand
    1037,   # pickaxe
    1038,   # bf sword
    1001,   # boots
    3006,   # berserkers grieves
    3117,   # mobi boots
    3009,   # boots of swiftness
    3047,   # ninja tabis
    3158,   # boots of lucidity
    3111,   # merc treads
    3134,   # serrated dirk
    3133,   # cf warhammer
    1053,   # vamp scepter
    3144,   # cutlass
    1043,   # recurve bow
    3086,   # zeal
    2015,   # kircheis shard
    3057,   # sheen
    3024,   # glacial shroud
    3044,   # phage
    3101,   # stinger
    3046,   # phantom dancer
    3087,   # statikk shiv
    3085,   # runaans hurricane
    3094,   # rapid firecannon
    3078,   # trinity force
    3031,   # infinity edge
    3508,   # essence reaver
    3142,   # youmuu's ghostblade
    3153,   # BORK
    3147,   # duskblade
    3814,   # edge of night
    3042,   # muramana
    3004,   # manamune
    3025,   # ice bourne gauntlet
    3091,   # wit's end
    3124,   # guinsoo's rageblade
    3026,   # guardian angel
    3155,   # hexdrinker
    3156,   # maw of malmortius
    3139,   # mercurial scimitar
    3072,   # Bloodthirster
    3812,   # Death's Dance
    3071,   # black cleaver
    3035,   # last whisper
    3123,   # executioner's calling
    3034,   # giant slayer
    3036,   # lord dominik's regard
    3033    # mortal reminder
]