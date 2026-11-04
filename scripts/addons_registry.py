"""
Definitions of the 20 Minecraft Bedrock Add-ons:
Themes, guides, namespaces, items, and crafting recipes.
"""

ADDONS = [
    {
        "id": "campfire_survival",
        "name": "Campfire Survival & Foods",
        "namespace": "cs",
        "category": "Survival & Food",
        "description": "Wilderness survival gear, canteens, hearty trail meals, skewers, and marshmallows.",
        "colors": ((200, 100, 40, 255), (255, 200, 50, 255)),
        "guidebook": {
            "title": "Campfire Survival Guide",
            "author": "Wilderness Ranger",
            "pages": [
                "§l§2Campfire Survival§r\n\nWelcome to wilderness expeditions!\n\nCarry a §6Leather Canteen§r to stay hydrated, cook §6Marshmallows§r over a campfire, and prepare §6Hearty Campfire Stew§r for long excursions.",
                "§l§1Survival Items§r\n\n§6Leather Canteen§r:\nCrafted with leather & glass bottle. Quenches thirst and cleanses minor ailments.\n\n§6Trail Mix§r:\nWheat seeds, sweet berries, & cocoa beans for quick sprint recovery.",
                "§l§1Campfire Meals§r\n\n§6Roast Skewer§r:\nCooked beef & pork skewer on a wooden stick.\n\n§6Hearty Stew§r:\nBowl filled with mushrooms, baked potatoes, and cooked beef.",
                "§l§1Field Crafting§r\n\nAll recipes use standard crafting grids. Read this guidebook anytime or craft a replacement with Book + Paper!"
            ]
        },
        "items": [
            {
                "id": "leather_canteen", "name": "Leather Canteen", "category": "equipment", "max_stack": 1,
                "food": {"nutrition": 3, "saturation_modifier": "normal", "can_always_eat": True},
                "icon_type": "canteen",
                "recipe": {"pattern": [" L ", "LGL", " L "], "key": {"L": "minecraft:leather", "G": "minecraft:glass_bottle"}, "count": 1}
            },
            {
                "id": "trail_mix", "name": "Trail Mix", "category": "nature", "max_stack": 64,
                "food": {"nutrition": 5, "saturation_modifier": "high", "can_always_eat": False},
                "icon_type": "nuts_berries",
                "recipe": {"pattern": ["WSW", "SCS", "WSW"], "key": {"W": "minecraft:wheat_seeds", "S": "minecraft:sweet_berries", "C": "minecraft:cocoa_beans"}, "count": 4}
            },
            {
                "id": "roast_skewer", "name": "Roast Skewer", "category": "items", "max_stack": 16,
                "food": {"nutrition": 8, "saturation_modifier": "supernatural", "can_always_eat": False},
                "icon_type": "skewer",
                "recipe": {"pattern": [" B ", " P ", " S "], "key": {"B": "minecraft:cooked_beef", "P": "minecraft:cooked_porkchop", "S": "minecraft:stick"}, "count": 1}
            },
            {
                "id": "marshmallow_stick", "name": "Marshmallow on a Stick", "category": "items", "max_stack": 16,
                "food": {"nutrition": 4, "saturation_modifier": "low", "can_always_eat": True},
                "icon_type": "marshmallow",
                "recipe": {"pattern": [" S ", " M ", " T "], "key": {"S": "minecraft:sugar", "M": "minecraft:egg", "T": "minecraft:stick"}, "count": 2}
            },
            {
                "id": "hearty_stew", "name": "Hearty Campfire Stew", "category": "items", "max_stack": 1,
                "food": {"nutrition": 10, "saturation_modifier": "supernatural", "can_always_eat": False},
                "icon_type": "stew",
                "recipe": {"pattern": [" C ", "BPM", " W "], "key": {"C": "minecraft:carrot", "B": "minecraft:cooked_beef", "P": "minecraft:baked_potato", "M": "minecraft:brown_mushroom", "W": "minecraft:bowl"}, "count": 1}
            }
        ]
    },
    {
        "id": "backpacks_pouches",
        "name": "Backpacks & Pouches",
        "namespace": "bp",
        "category": "Storage & Equipment",
        "description": "Expandable leather packs, miner satchels, and pocket ender pouches.",
        "colors": ((140, 80, 40, 255), (210, 150, 80, 255)),
        "guidebook": {
            "title": "Backpacker's Guide",
            "author": "Nomad Taylor",
            "pages": [
                "§l§6Backpacks & Pouches§r\n\nOrganize inventory during long mining expeditions.\n\nCraft handy pouches and heavy expedition packs to store tools and supplies on the go.",
                "§l§1Available Packs§r\n\n§2Small Leather Pouch§r: 5 leather + string.\n§6Traveler Backpack§r: Leather + iron + chest.\n§bExpedition Backpack§r: Reinforced diamond frame.\n§5Ender Pouch§r: Linked directly to ender chest storage.",
                "§l§1Miner's Satchel§r\n\nCopper & iron lined satchel to carry raw ores and excavation tools."
            ]
        },
        "items": [
            {"id": "small_leather_pouch", "name": "Small Leather Pouch", "category": "equipment", "max_stack": 1, "icon_type": "pouch_small", "recipe": {"pattern": [" L ", "LSL", "LLL"], "key": {"L": "minecraft:leather", "S": "minecraft:string"}, "count": 1}},
            {"id": "traveler_backpack", "name": "Traveler Backpack", "category": "equipment", "max_stack": 1, "icon_type": "backpack_leather", "recipe": {"pattern": ["LIL", "LCL", "LLL"], "key": {"L": "minecraft:leather", "I": "minecraft:iron_ingot", "C": "minecraft:chest"}, "count": 1}},
            {"id": "miner_satchel", "name": "Miner's Satchel", "category": "equipment", "max_stack": 1, "icon_type": "satchel_miner", "recipe": {"pattern": ["ICI", "LCL", " L "], "key": {"I": "minecraft:iron_ingot", "C": "minecraft:copper_ingot", "L": "minecraft:leather"}, "count": 1}},
            {"id": "ender_pouch", "name": "Ender Pouch", "category": "equipment", "max_stack": 1, "icon_type": "pouch_ender", "recipe": {"pattern": [" E ", "LCL", " L "], "key": {"E": "minecraft:ender_eye", "L": "minecraft:leather", "C": "minecraft:ender_chest"}, "count": 1}},
            {"id": "expedition_backpack", "name": "Expedition Backpack", "category": "equipment", "max_stack": 1, "icon_type": "backpack_expedition", "recipe": {"pattern": ["DGD", "LBL", "DDD"], "key": {"D": "minecraft:diamond", "G": "minecraft:gold_ingot", "L": "minecraft:leather", "B": "minecraft:chest"}, "count": 1}}
        ]
    },
    {
        "id": "waystones_scrolls",
        "name": "Waystones & Teleport Scrolls",
        "namespace": "ws",
        "category": "Magic & Travel",
        "description": "Fast recall scrolls, warp gems, and tablets of return for instant transport.",
        "colors": ((60, 40, 180, 255), (140, 100, 255, 255)),
        "guidebook": {
            "title": "Warp Master's Tome",
            "author": "Archmage Varis",
            "pages": [
                "§l§5Waystones & Scrolls§r\n\nInstantaneous travel across biomes!\n\nInscribe teleportation runes onto enchanted parchment to leap across dimensions.",
                "§l§1Scrolls & Items§r\n\n§bHome Recall Scroll§r: Lapis lazuli + paper + gold nugget.\n§eCave Escape Scroll§r: Feather + paper + redstone.\n§5Bound Warp Stone§r: Infused with Ender pearl essence.\n§dTablet of Return§r: Obsidian and diamond reinforced rune."
            ]
        },
        "items": [
            {"id": "recall_scroll", "name": "Recall Scroll", "category": "items", "max_stack": 16, "icon_type": "scroll_blue", "recipe": {"pattern": [" L ", "PPP", " G "], "key": {"L": "minecraft:lapis_lazuli", "P": "minecraft:paper", "G": "minecraft:gold_nugget"}, "count": 2}},
            {"id": "warp_stone", "name": "Bound Warp Stone", "category": "equipment", "max_stack": 16, "icon_type": "warp_gem", "recipe": {"pattern": [" D ", "PEP", " D "], "key": {"D": "minecraft:diamond", "P": "minecraft:ender_pearl", "E": "minecraft:emerald"}, "count": 1}},
            {"id": "cave_escape_scroll", "name": "Escape Scroll", "category": "items", "max_stack": 16, "icon_type": "scroll_yellow", "recipe": {"pattern": [" F ", "PPP", " R "], "key": {"F": "minecraft:feather", "P": "minecraft:paper", "R": "minecraft:redstone"}, "count": 2}},
            {"id": "rift_shard", "name": "Rift Shard", "category": "items", "max_stack": 64, "icon_type": "rift_shard", "recipe": {"pattern": [" A ", "EPE", " A "], "key": {"A": "minecraft:amethyst_shard", "E": "minecraft:ender_pearl", "P": "minecraft:prismarine_crystals"}, "count": 4}},
            {"id": "teleport_tablet", "name": "Tablet of Return", "category": "equipment", "max_stack": 1, "icon_type": "tablet_rune", "recipe": {"pattern": ["ODO", "DRD", "ODO"], "key": {"O": "minecraft:obsidian", "D": "minecraft:diamond", "R": "minecraft:ender_pearl"}, "count": 1}}
        ]
    },
    {
        "id": "elemental_weapons",
        "name": "Elemental Weapons",
        "namespace": "ew",
        "category": "Weapons",
        "description": "Blazing Flameblades, Glacial Frost Daggers, and Thunder Hammers.",
        "colors": ((220, 50, 30, 255), (255, 170, 50, 255)),
        "guidebook": {
            "title": "Armory of Elements",
            "author": "Grand Smith Thorin",
            "pages": [
                "§l§cElemental Armory§r\n\nImbue weapon blades with primordial fire, frost, and storm energy.",
                "§l§1Weapons§r\n\n§cBlazing Flameblade§r (8 Dmg): Ignites foes on impact.\n§bGlacial Frost Dagger§r (6 Dmg): Swift ice strikes.\n§eThunder Hammer§r (10 Dmg): Crushing lightning impact.\n§aTempest Spear§r (7 Dmg): Piercing gust weapon."
            ]
        },
        "items": [
            {"id": "flameblade", "name": "Blazing Flameblade", "category": "equipment", "max_stack": 1, "damage": 8, "icon_type": "sword_flame", "recipe": {"pattern": [" B ", " M ", " S "], "key": {"B": "minecraft:blaze_rod", "M": "minecraft:magma_cream", "S": "minecraft:nether_brick"}, "count": 1}},
            {"id": "frost_dagger", "name": "Glacial Frost Dagger", "category": "equipment", "max_stack": 1, "damage": 6, "icon_type": "dagger_frost", "recipe": {"pattern": [" I ", " P ", " S "], "key": {"I": "minecraft:blue_ice", "P": "minecraft:prismarine_shard", "S": "minecraft:stick"}, "count": 1}},
            {"id": "thunder_hammer", "name": "Thunder Hammer", "category": "equipment", "max_stack": 1, "damage": 10, "icon_type": "hammer_thunder", "recipe": {"pattern": ["LCL", " S ", " S "], "key": {"L": "minecraft:lightning_rod", "C": "minecraft:copper_block", "S": "minecraft:iron_ingot"}, "count": 1}},
            {"id": "tempest_spear", "name": "Tempest Spear", "category": "equipment", "max_stack": 1, "damage": 7, "icon_type": "spear_wind", "recipe": {"pattern": [" F ", " B ", " S "], "key": {"F": "minecraft:feather", "B": "minecraft:breeze_rod", "S": "minecraft:stick"}, "count": 1}},
            {"id": "elemental_core", "name": "Primal Elemental Core", "category": "items", "max_stack": 64, "icon_type": "core_element", "recipe": {"pattern": [" F ", "IDT", " S "], "key": {"F": "minecraft:blaze_powder", "I": "minecraft:blue_ice", "D": "minecraft:diamond", "T": "minecraft:lightning_rod", "S": "minecraft:prismarine_crystals"}, "count": 1}}
        ]
    },
    {
        "id": "excavation_gear",
        "name": "Excavation & Mining Gear",
        "namespace": "eg",
        "category": "Tools",
        "description": "Heavy 3x3 Mining Hammers, Excavator Trench Shovels, and Ore Magnets.",
        "colors": ((150, 110, 40, 255), (240, 200, 60, 255)),
        "guidebook": {
            "title": "Prospector's Handbook",
            "author": "Chief Digger Flint",
            "pages": [
                "§l§6Excavation & Mining Gear§r\n\nTunnel through mountains rapidly with heavy excavation equipment.",
                "§l§1Tools§r\n\n§7Iron Mining Hammer§r: Heavy vein carver.\n§bDiamond Mining Hammer§r: Massive rock breaker.\n§6Excavator Trench Shovel§r: Wide dirt clearing.\n§cOre Magnet§r: Attracts mined drops directly to you."
            ]
        },
        "items": [
            {"id": "iron_heavy_hammer", "name": "Iron Mining Hammer", "category": "equipment", "max_stack": 1, "damage": 5, "icon_type": "hammer_iron", "recipe": {"pattern": ["III", " S ", " S "], "key": {"I": "minecraft:iron_block", "S": "minecraft:stick"}, "count": 1}},
            {"id": "diamond_heavy_hammer", "name": "Diamond Mining Hammer", "category": "equipment", "max_stack": 1, "damage": 7, "icon_type": "hammer_diamond", "recipe": {"pattern": ["DDD", " O ", " O "], "key": {"D": "minecraft:diamond_block", "O": "minecraft:obsidian"}, "count": 1}},
            {"id": "excavator_shovel", "name": "Excavator Shovel", "category": "equipment", "max_stack": 1, "damage": 4, "icon_type": "shovel_heavy", "recipe": {"pattern": [" I ", "ISI", " S "], "key": {"I": "minecraft:iron_block", "S": "minecraft:stick"}, "count": 1}},
            {"id": "ore_prospector", "name": "Prospector's Lens", "category": "equipment", "max_stack": 1, "icon_type": "lens_prospector", "recipe": {"pattern": [" C ", "GAG", " C "], "key": {"C": "minecraft:copper_ingot", "G": "minecraft:gold_ingot", "A": "minecraft:amethyst_shard"}, "count": 1}},
            {"id": "ore_magnet", "name": "Lodestone Ore Magnet", "category": "equipment", "max_stack": 1, "icon_type": "magnet", "recipe": {"pattern": ["R R", "I I", " L "], "key": {"R": "minecraft:redstone", "I": "minecraft:iron_ingot", "L": "minecraft:lapis_lazuli"}, "count": 1}}
        ]
    },
    {
        "id": "magical_wands",
        "name": "Magical Wands & Spells",
        "namespace": "mw",
        "category": "Magic",
        "description": "Arcane pyromancy wands, frostbite beams, and healing scepters.",
        "colors": ((150, 50, 190, 255), (230, 120, 255, 255)),
        "guidebook": {
            "title": "Compendium of Sorcery",
            "author": "Archmage Cynthia",
            "pages": [
                "§l§dMagical Wands & Spells§r\n\nHarness mystical spellcasting with staves carved from arcane crystals.",
                "§l§1Wands§r\n\n§cWand of Pyromancy§r: Bursts of fire charges.\n§bWand of Cryomancy§r: Freezing ice shards.\n§aRestorative Scepter§r: Channels healing energy.\n§dApprentice Wand§r: Starter casting focus."
            ]
        },
        "items": [
            {"id": "wand_apprentice", "name": "Apprentice Wand", "category": "equipment", "max_stack": 1, "damage": 4, "icon_type": "wand_wood", "recipe": {"pattern": [" A ", " S ", " S "], "key": {"A": "minecraft:amethyst_shard", "S": "minecraft:stick"}, "count": 1}},
            {"id": "wand_pyromancy", "name": "Wand of Pyromancy", "category": "equipment", "max_stack": 1, "damage": 6, "icon_type": "wand_fire", "recipe": {"pattern": [" F ", " B ", " B "], "key": {"F": "minecraft:fire_charge", "B": "minecraft:blaze_rod"}, "count": 1}},
            {"id": "wand_cryomancy", "name": "Wand of Cryomancy", "category": "equipment", "max_stack": 1, "damage": 6, "icon_type": "wand_ice", "recipe": {"pattern": [" P ", " B ", " S "], "key": {"P": "minecraft:prismarine_crystals", "B": "minecraft:blue_ice", "S": "minecraft:stick"}, "count": 1}},
            {"id": "healing_scepter", "name": "Restorative Scepter", "category": "equipment", "max_stack": 1, "damage": 3, "icon_type": "scepter_heal", "recipe": {"pattern": [" G ", " T ", " S "], "key": {"G": "minecraft:glistering_melon_slice", "T": "minecraft:ghast_tear", "S": "minecraft:gold_ingot"}, "count": 1}},
            {"id": "mana_crystal", "name": "Pure Mana Crystal", "category": "items", "max_stack": 64, "icon_type": "crystal_mana", "recipe": {"pattern": [" A ", "DED", " A "], "key": {"A": "minecraft:amethyst_shard", "D": "minecraft:diamond", "E": "minecraft:emerald"}, "count": 2}}
        ]
    },
    {
        "id": "crops_cooking",
        "name": "Crops & Cooking",
        "namespace": "cc",
        "category": "Farming & Food",
        "description": "Sweet strawberries, golden corn, ripe tomatoes, chef knives, and sandwiches.",
        "colors": ((40, 160, 50, 255), (120, 230, 80, 255)),
        "guidebook": {
            "title": "Master Chef's Culinary",
            "author": "Chef Remy Green",
            "pages": [
                "§l§2Crops & Cooking§r\n\nCultivate new gourmet crops and prepare wholesome sandwiches.",
                "§l§1Produce§r\n\n§cSweet Strawberry§r: Quick berry snack.\n§eGolden Corn§r: Crunchy ears of grain.\n§4Ripe Tomato§r: Juicy salad ingredient.\n§7Chef's Knife§r: Food preparation tool."
            ]
        },
        "items": [
            {"id": "strawberry", "name": "Sweet Strawberry", "category": "nature", "max_stack": 64, "food": {"nutrition": 3, "saturation_modifier": "normal", "can_always_eat": True}, "icon_type": "crop_strawberry", "recipe": {"pattern": [" S ", " B ", " S "], "key": {"S": "minecraft:sweet_berries", "B": "minecraft:sugar"}, "count": 2}},
            {"id": "corn_cob", "name": "Golden Corn", "category": "nature", "max_stack": 64, "food": {"nutrition": 4, "saturation_modifier": "normal", "can_always_eat": False}, "icon_type": "crop_corn", "recipe": {"pattern": [" W ", " Y ", " W "], "key": {"W": "minecraft:wheat", "Y": "minecraft:yellow_dye"}, "count": 2}},
            {"id": "tomato", "name": "Ripe Tomato", "category": "nature", "max_stack": 64, "food": {"nutrition": 3, "saturation_modifier": "normal", "can_always_eat": False}, "icon_type": "crop_tomato", "recipe": {"pattern": [" A ", " R ", " S "], "key": {"A": "minecraft:apple", "R": "minecraft:red_dye", "S": "minecraft:wheat_seeds"}, "count": 2}},
            {"id": "chef_knife", "name": "Chef's Knife", "category": "equipment", "max_stack": 1, "damage": 4, "icon_type": "chef_knife", "recipe": {"pattern": ["  I", " I ", "S  "], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:stick"}, "count": 1}},
            {"id": "gourmet_sandwich", "name": "Gourmet Sandwich", "category": "items", "max_stack": 16, "food": {"nutrition": 10, "saturation_modifier": "supernatural", "can_always_eat": False}, "icon_type": "sandwich", "recipe": {"pattern": [" B ", "TPC", " B "], "key": {"B": "minecraft:bread", "T": "minecraft:apple", "P": "minecraft:cooked_porkchop", "C": "minecraft:wheat"}, "count": 1}}
        ]
    },
    {
        "id": "more_bows_quivers",
        "name": "More Bows & Quivers",
        "namespace": "mb",
        "category": "Archery",
        "description": "Explosive blast bows, viper poison shortbows, reinforced longbows, and quivers.",
        "colors": ((60, 120, 60, 255), (180, 220, 90, 255)),
        "guidebook": {
            "title": "Archer's Field Journal",
            "author": "Ranger Hawkeye",
            "pages": [
                "§l§2More Bows & Quivers§r\n\nUpgrade your marksmanship with specialized bows for long-range dominance.",
                "§l§1Bows & Ammo§r\n\n§cBlast Bow§r: Shoots explosive volleys.\n§2Viper Shortbow§r: Poison arrows.\n§7Reinforced Longbow§r: High durability iron bow.\n§6Hunter's Quiver§r: Arrow ammunition pack."
            ]
        },
        "items": [
            {"id": "reinforced_bow", "name": "Reinforced Longbow", "category": "equipment", "max_stack": 1, "damage": 6, "icon_type": "bow_reinforced", "recipe": {"pattern": [" IS", "I S", " IS"], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:string"}, "count": 1}},
            {"id": "explosive_bow", "name": "Blast Bow", "category": "equipment", "max_stack": 1, "damage": 7, "icon_type": "bow_blast", "recipe": {"pattern": ["TBS", "T S", "TBS"], "key": {"T": "minecraft:tnt", "B": "minecraft:blaze_powder", "S": "minecraft:string"}, "count": 1}},
            {"id": "poison_shortbow", "name": "Viper Shortbow", "category": "equipment", "max_stack": 1, "damage": 5, "icon_type": "bow_viper", "recipe": {"pattern": [" PS", "F S", " PS"], "key": {"P": "minecraft:spider_eye", "F": "minecraft:fermented_spider_eye", "S": "minecraft:string"}, "count": 1}},
            {"id": "archer_quiver", "name": "Hunter's Quiver", "category": "equipment", "max_stack": 1, "icon_type": "quiver", "recipe": {"pattern": [" L ", "LAL", " L "], "key": {"L": "minecraft:leather", "A": "minecraft:arrow"}, "count": 1}},
            {"id": "barbed_arrow", "name": "Barbed Broadhead Arrow", "category": "items", "max_stack": 64, "icon_type": "arrow_barbed", "recipe": {"pattern": [" I ", " S ", " F "], "key": {"I": "minecraft:iron_nugget", "S": "minecraft:stick", "F": "minecraft:feather"}, "count": 8}}
        ]
    },
    {
        "id": "medieval_defense",
        "name": "Medieval Defense & Traps",
        "namespace": "md",
        "category": "Defense",
        "description": "Iron caltrops, heavy bear traps, reinforced tower shields, and barricades.",
        "colors": ((100, 100, 110, 255), (190, 190, 200, 255)),
        "guidebook": {
            "title": "Fortress Master's Codex",
            "author": "Commander Valerius",
            "pages": [
                "§l§8Medieval Defense & Traps§r\n\nFortify bases and defend against night raids with heavy barricades and perimeter traps.",
                "§l§1Defenses§r\n\n§7Iron Caltrops§r: Sharp spikes hurting oncoming mobs.\n§6Bear Trap§r: Spring-loaded mob trap.\n§eReinforced Tower Shield§r: High deflection shield.\n§4Fortified Barricade§r: Iron bar blockade."
            ]
        },
        "items": [
            {"id": "iron_caltrops", "name": "Iron Caltrops", "category": "items", "max_stack": 64, "icon_type": "caltrops", "recipe": {"pattern": [" I ", "III", " I "], "key": {"I": "minecraft:iron_nugget"}, "count": 16}},
            {"id": "bear_trap", "name": "Heavy Bear Trap", "category": "items", "max_stack": 16, "icon_type": "trap_bear", "recipe": {"pattern": ["I I", "SIS", "III"], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:string"}, "count": 2}},
            {"id": "tower_shield", "name": "Reinforced Tower Shield", "category": "equipment", "max_stack": 1, "icon_type": "shield_tower", "recipe": {"pattern": ["III", "WPW", " W "], "key": {"I": "minecraft:iron_ingot", "W": "minecraft:oak_planks", "P": "minecraft:shield"}, "count": 1}},
            {"id": "wooden_spikes", "name": "Sharpened Stakes", "category": "items", "max_stack": 64, "icon_type": "spikes_wood", "recipe": {"pattern": [" S ", " L ", " L "], "key": {"S": "minecraft:stick", "L": "minecraft:oak_log"}, "count": 4}},
            {"id": "reinforced_barricade", "name": "Fortified Barricade", "category": "items", "max_stack": 16, "icon_type": "barricade", "recipe": {"pattern": ["III", "PPP", "III"], "key": {"I": "minecraft:iron_bars", "P": "minecraft:oak_planks"}, "count": 2}}
        ]
    },
    {
        "id": "mobility_grappling",
        "name": "Mobility & Grappling",
        "namespace": "mg",
        "category": "Movement",
        "description": "Grappling hooks, dash feathers, spring jump boots, and silk glider capes.",
        "colors": ((40, 160, 200, 255), (130, 240, 255, 255)),
        "guidebook": {
            "title": "Acrobat's Field Manual",
            "author": "Skystrider Zephyr",
            "pages": [
                "§l§bMobility & Grappling§r\n\nConquer steep mountain cliffs and deep ravines with dynamic parkour traversal gear.",
                "§l§1Movement Gear§r\n\n§7Grappling Hook§r: Braided cable climbing tool.\n§eDash Feather§r: Forward burst of speed.\n§aSpring Jump Boots§r: Enhanced vertical jumps.\n§fSilk Glider Cape§r: Gentle descent glider."
            ]
        },
        "items": [
            {"id": "grappling_hook", "name": "Grappling Hook", "category": "equipment", "max_stack": 1, "damage": 3, "icon_type": "grappling_hook", "recipe": {"pattern": ["  I", " S ", "C  "], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:string", "C": "minecraft:chain"}, "count": 1}},
            {"id": "dash_feather", "name": "Dash Feather", "category": "equipment", "max_stack": 1, "icon_type": "feather_dash", "recipe": {"pattern": [" F ", "GBG", " F "], "key": {"F": "minecraft:feather", "G": "minecraft:glowstone_dust", "B": "minecraft:breeze_rod"}, "count": 1}},
            {"id": "spring_boots", "name": "Bouncy Spring Boots", "category": "equipment", "max_stack": 1, "icon_type": "boots_spring", "recipe": {"pattern": ["L L", "S S", "P P"], "key": {"L": "minecraft:leather", "S": "minecraft:slime_ball", "P": "minecraft:piston"}, "count": 1}},
            {"id": "glider_cape", "name": "Silk Glider Cape", "category": "equipment", "max_stack": 1, "icon_type": "glider_cape", "recipe": {"pattern": ["BBB", "SSS", " S "], "key": {"B": "minecraft:bamboo", "S": "minecraft:string"}, "count": 1}},
            {"id": "kinetic_coil", "name": "Kinetic Coil", "category": "items", "max_stack": 64, "icon_type": "coil_kinetic", "recipe": {"pattern": [" I ", "RCR", " I "], "key": {"I": "minecraft:iron_nugget", "R": "minecraft:redstone", "C": "minecraft:copper_ingot"}, "count": 2}}
        ]
    },
    {
        "id": "rings_relics",
        "name": "Enchanted Rings & Relics",
        "namespace": "rr",
        "category": "Curios & Relics",
        "description": "Magical bands of swiftness, regeneration, fireguard amulets, and night vision spectacles.",
        "colors": ((220, 180, 30, 255), (255, 240, 130, 255)),
        "guidebook": {
            "title": "Jeweler's Reliquary",
            "author": "Grand Lapidary Aurelius",
            "pages": [
                "§l§6Enchanted Rings & Relics§r\n\nChannel passive blessings through enchanted jewelry forged with gold and jewels.",
                "§l§1Relics§r\n\n§bRing of Swiftness§r: Gold + lapis lazuli.\n§aRing of Vitality§r: Gold + emerald.\n§cFireguard Talisman§r: Chains + magma cream.\n§dNight Sight Spectacles§r: Copper + amethyst."
            ]
        },
        "items": [
            {"id": "ring_swiftness", "name": "Ring of Swiftness", "category": "equipment", "max_stack": 1, "icon_type": "ring_blue", "recipe": {"pattern": [" G ", "G L", " G "], "key": {"G": "minecraft:gold_ingot", "L": "minecraft:lapis_lazuli"}, "count": 1}},
            {"id": "ring_vitality", "name": "Ring of Vitality", "category": "equipment", "max_stack": 1, "icon_type": "ring_green", "recipe": {"pattern": [" G ", "G E", " G "], "key": {"G": "minecraft:gold_ingot", "E": "minecraft:emerald"}, "count": 1}},
            {"id": "fireguard_talisman", "name": "Fireguard Talisman", "category": "equipment", "max_stack": 1, "icon_type": "amulet_fire", "recipe": {"pattern": [" C ", "CMC", " C "], "key": {"C": "minecraft:chain", "M": "minecraft:magma_cream"}, "count": 1}},
            {"id": "night_spectacles", "name": "Night Sight Spectacles", "category": "equipment", "max_stack": 1, "icon_type": "spectacles", "recipe": {"pattern": ["C C", "AGA", "   "], "key": {"C": "minecraft:copper_ingot", "A": "minecraft:amethyst_shard", "G": "minecraft:glass"}, "count": 1}},
            {"id": "jeweled_band", "name": "Blank Jeweled Band", "category": "items", "max_stack": 16, "icon_type": "ring_gold", "recipe": {"pattern": [" G ", "G G", " G "], "key": {"G": "minecraft:gold_ingot"}, "count": 1}}
        ]
    },
    {
        "id": "rustic_furniture",
        "name": "Rustic Furniture",
        "namespace": "rf",
        "category": "Decoration",
        "description": "Handcrafted wooden stools, dining tables, paper lanterns, wall shelves, and crates.",
        "colors": ((160, 100, 50, 255), (230, 170, 110, 255)),
        "guidebook": {
            "title": "Rustic Carpenter's Manual",
            "author": "Master Carpenter Edwin",
            "pages": [
                "§l§6Rustic Furniture§r\n\nFurnish houses and cabins with cozy wooden items.",
                "§l§1Furniture Items§r\n\n§6Rustic Wooden Stool§r: Oak slab + sticks.\n§eRustic Dining Table§r: Oak planks + sticks.\n§fHanging Paper Lantern§r: Paper + torch.\n§6Reinforced Storage Crate§r: Planks + chest."
            ]
        },
        "items": [
            {"id": "wooden_stool", "name": "Rustic Wooden Stool", "category": "items", "max_stack": 64, "icon_type": "furniture_stool", "recipe": {"pattern": [" P ", "S S", "S S"], "key": {"P": "minecraft:oak_slab", "S": "minecraft:stick"}, "count": 2}},
            {"id": "dining_table", "name": "Rustic Dining Table", "category": "items", "max_stack": 64, "icon_type": "furniture_table", "recipe": {"pattern": ["PPP", "S S", "S S"], "key": {"P": "minecraft:oak_planks", "S": "minecraft:stick"}, "count": 2}},
            {"id": "paper_lantern", "name": "Hanging Paper Lantern", "category": "items", "max_stack": 64, "icon_type": "furniture_lantern", "recipe": {"pattern": [" S ", "PTP", " S "], "key": {"S": "minecraft:stick", "P": "minecraft:paper", "T": "minecraft:torch"}, "count": 2}},
            {"id": "rustic_shelf", "name": "Wall Display Shelf", "category": "items", "max_stack": 64, "icon_type": "furniture_shelf", "recipe": {"pattern": ["SSS", "P P", "   "], "key": {"S": "minecraft:oak_slab", "P": "minecraft:stick"}, "count": 3}},
            {"id": "storage_crate", "name": "Reinforced Wooden Crate", "category": "items", "max_stack": 64, "icon_type": "furniture_crate", "recipe": {"pattern": ["PIP", "ICI", "PIP"], "key": {"P": "minecraft:oak_planks", "I": "minecraft:iron_nugget", "C": "minecraft:chest"}, "count": 1}}
        ]
    },
    {
        "id": "nether_relics",
        "name": "Nether Relics & Forging",
        "namespace": "nr",
        "category": "Nether & Forging",
        "description": "Soulfire Greatswords, Magma Plated Shields, and Witherbane Talismans.",
        "colors": ((180, 30, 20, 255), (90, 200, 240, 255)),
        "guidebook": {
            "title": "Nether Smith's Black Tome",
            "author": "Pyromancer Malakor",
            "pages": [
                "§l§4Nether Relics & Forging§r\n\nForge weapons from the scorching fires and soul sand of the Nether realm.",
                "§l§1Nether Equipment§r\n\n§bSoulfire Greatsword§r (9 Dmg): Soulfire blade.\n§cMagma Plated Shield§r: Heat resistant guard.\n§8Witherbane Talisman§r: Wither warding charm.\n§6Soulforged Ingot§r: High heat alloy."
            ]
        },
        "items": [
            {"id": "soulfire_blade", "name": "Soulfire Greatsword", "category": "equipment", "max_stack": 1, "damage": 9, "icon_type": "sword_soul", "recipe": {"pattern": [" B ", " B ", " S "], "key": {"B": "minecraft:nether_brick", "S": "minecraft:blaze_rod"}, "count": 1}},
            {"id": "magma_shield", "name": "Magma Plated Shield", "category": "equipment", "max_stack": 1, "icon_type": "shield_magma", "recipe": {"pattern": ["MMM", "MSM", " M "], "key": {"M": "minecraft:magma_block", "S": "minecraft:shield"}, "count": 1}},
            {"id": "witherbane_talisman", "name": "Witherbane Talisman", "category": "equipment", "max_stack": 1, "icon_type": "amulet_wither", "recipe": {"pattern": [" N ", "WSW", " N "], "key": {"N": "minecraft:nether_star", "W": "minecraft:wither_skeleton_skull", "S": "minecraft:soul_sand"}, "count": 1}},
            {"id": "soul_ingot", "name": "Soulforged Ingot", "category": "items", "max_stack": 64, "icon_type": "ingot_soul", "recipe": {"pattern": [" G ", "SNS", " G "], "key": {"G": "minecraft:gold_ingot", "S": "minecraft:soul_sand", "N": "minecraft:netherite_scrap"}, "count": 1}},
            {"id": "blaze_core", "name": "Condensed Blaze Core", "category": "items", "max_stack": 64, "icon_type": "core_blaze", "recipe": {"pattern": ["BBB", "BFB", "BBB"], "key": {"B": "minecraft:blaze_powder", "F": "minecraft:fire_charge"}, "count": 1}}
        ]
    },
    {
        "id": "ocean_diving",
        "name": "Ocean Diving & Harpoons",
        "namespace": "od",
        "category": "Ocean",
        "description": "Copper diving helmets, hydrodynamic fins, pressure harpoon guns, and abyssal lanterns.",
        "colors": ((20, 110, 160, 255), (80, 220, 230, 255)),
        "guidebook": {
            "title": "Abyssal Diver's Log",
            "author": "Captain Marina",
            "pages": [
                "§l§3Ocean Diving & Harpoons§r\n\nSubmerge deep into ocean trenches and ancient underwater monuments.",
                "§l§1Diving Gear§r\n\n§3Copper Diving Helmet§r: Extended underwater respiration.\n§2Hydrodynamic Fins§r: Swift ocean swimming.\n§7Pressure Harpoon Gun§r (8 Dmg): High velocity underwater shooter.\n§bDeep Abyssal Lantern§r: Intense underwater lighting."
            ]
        },
        "items": [
            {"id": "diving_helmet", "name": "Copper Diving Helmet", "category": "equipment", "max_stack": 1, "icon_type": "diving_helmet", "recipe": {"pattern": ["CCC", "CGC", " P "], "key": {"C": "minecraft:copper_ingot", "G": "minecraft:glass_pane", "P": "minecraft:prismarine_crystals"}, "count": 1}},
            {"id": "diving_fins", "name": "Hydrodynamic Fins", "category": "equipment", "max_stack": 1, "icon_type": "diving_fins", "recipe": {"pattern": ["P P", "L L", "P P"], "key": {"P": "minecraft:prismarine_shard", "L": "minecraft:leather"}, "count": 1}},
            {"id": "harpoon_gun", "name": "Pressure Harpoon Gun", "category": "equipment", "max_stack": 1, "damage": 8, "icon_type": "harpoon_gun", "recipe": {"pattern": [" CI", "PPC", "  P"], "key": {"C": "minecraft:copper_ingot", "I": "minecraft:iron_ingot", "P": "minecraft:prismarine_shard"}, "count": 1}},
            {"id": "harpoon_bolt", "name": "Barbed Harpoon Bolt", "category": "items", "max_stack": 64, "icon_type": "harpoon_bolt", "recipe": {"pattern": [" I ", " C ", " F "], "key": {"I": "minecraft:iron_nugget", "C": "minecraft:copper_ingot", "F": "minecraft:feather"}, "count": 8}},
            {"id": "abyssal_lantern", "name": "Deep Abyssal Lantern", "category": "items", "max_stack": 64, "icon_type": "lantern_abyssal", "recipe": {"pattern": [" P ", "PGP", " P "], "key": {"P": "minecraft:prismarine_shard", "G": "minecraft:glow_ink_sac"}, "count": 2}}
        ]
    },
    {
        "id": "alchemical_flasks",
        "name": "Alchemical Flasks & Bombs",
        "namespace": "af",
        "category": "Alchemy",
        "description": "Incendiary fire flasks, dense smoke bombs, glacial frost vials, and elixirs.",
        "colors": ((210, 130, 30, 255), (160, 240, 60, 255)),
        "guidebook": {
            "title": "Alchemist's Formulae",
            "author": "Grand Chemist Paracelsus",
            "pages": [
                "§l§eAlchemical Flasks & Bombs§r\n\nTurn brewing materials into thrown explosive flasks and combat concoctions.",
                "§l§1Concoctions§r\n\n§cFire Flask§r: Blazes impact zones.\n§8Smoke Bomb§r: Obscuring fog screen.\n§bFrost Vial§r: Chilling flash-freeze.\n§aHealing Elixir§r: Concentrated instant potion."
            ]
        },
        "items": [
            {"id": "fire_flask", "name": "Incendiary Fire Flask", "category": "items", "max_stack": 16, "icon_type": "flask_fire", "recipe": {"pattern": [" G ", "GFG", " G "], "key": {"G": "minecraft:gunpowder", "F": "minecraft:blaze_powder"}, "count": 3}},
            {"id": "smoke_bomb", "name": "Dense Smoke Bomb", "category": "items", "max_stack": 16, "icon_type": "bomb_smoke", "recipe": {"pattern": [" C ", "PGP", " C "], "key": {"C": "minecraft:coal", "P": "minecraft:paper", "G": "minecraft:gunpowder"}, "count": 4}},
            {"id": "frost_vial", "name": "Glacial Frost Vial", "category": "items", "max_stack": 16, "icon_type": "vial_frost", "recipe": {"pattern": [" I ", "PBP", " I "], "key": {"I": "minecraft:blue_ice", "P": "minecraft:snowball", "B": "minecraft:glass_bottle"}, "count": 2}},
            {"id": "healing_elixir", "name": "Concentrated Healing Elixir", "category": "items", "max_stack": 16, "food": {"nutrition": 6, "saturation_modifier": "supernatural", "can_always_eat": True}, "icon_type": "elixir_heal", "recipe": {"pattern": [" G ", "MTM", " B "], "key": {"G": "minecraft:glistering_melon_slice", "M": "minecraft:golden_apple", "T": "minecraft:ghast_tear", "B": "minecraft:glass_bottle"}, "count": 2}},
            {"id": "alchemical_residue", "name": "Alchemical Catalyst Residue", "category": "items", "max_stack": 64, "icon_type": "catalyst_alchemy", "recipe": {"pattern": [" R ", "GSG", " R "], "key": {"R": "minecraft:redstone", "G": "minecraft:glowstone_dust", "S": "minecraft:sugar"}, "count": 4}}
        ]
    },
    {
        "id": "pet_care",
        "name": "Pet Care & Taming",
        "namespace": "pc",
        "category": "Creatures & Pets",
        "description": "Training whistles, armored pet collars, dog biscuits, and traveler pet carriers.",
        "colors": ((160, 70, 40, 255), (240, 160, 100, 255)),
        "guidebook": {
            "title": "Master Pet Care Guide",
            "author": "Beastmaster Kael",
            "pages": [
                "§l§aPet Care & Taming§r\n\nEquip and protect your animal companions with specialized veterinary and taming tools.",
                "§l§1Pet Gear§r\n\n§6Training Whistle§r: Direct tamed wolves and cats.\n§cArmored Collar§r: Leather and iron defense collar.\n§ePet Vitality Biscuit§r: Nutritious healing snack.\n§6Traveler Pet Carrier§r: Portable cage to move pets safely."
            ]
        },
        "items": [
            {"id": "training_whistle", "name": "Silver Training Whistle", "category": "equipment", "max_stack": 1, "icon_type": "whistle_silver", "recipe": {"pattern": [" I ", " I ", "   "], "key": {"I": "minecraft:iron_ingot"}, "count": 1}},
            {"id": "armored_collar", "name": "Armored Pet Collar", "category": "equipment", "max_stack": 1, "icon_type": "collar_armored", "recipe": {"pattern": [" L ", "LIL", " L "], "key": {"L": "minecraft:leather", "I": "minecraft:iron_ingot"}, "count": 1}},
            {"id": "vitality_biscuit", "name": "Pet Vitality Biscuit", "category": "items", "max_stack": 64, "food": {"nutrition": 5, "saturation_modifier": "high", "can_always_eat": True}, "icon_type": "biscuit_pet", "recipe": {"pattern": [" W ", "BMB", " W "], "key": {"W": "minecraft:wheat", "B": "minecraft:bone_meal", "M": "minecraft:cooked_beef"}, "count": 4}},
            {"id": "pet_carrier", "name": "Traveler Pet Carrier", "category": "equipment", "max_stack": 1, "icon_type": "carrier_pet", "recipe": {"pattern": [" B ", "LCL", " L "], "key": {"B": "minecraft:iron_bars", "L": "minecraft:leather", "C": "minecraft:chest"}, "count": 1}},
            {"id": "brush_grooming", "name": "Soft Grooming Brush", "category": "equipment", "max_stack": 1, "icon_type": "brush_pet", "recipe": {"pattern": [" F ", " S ", " S "], "key": {"F": "minecraft:feather", "S": "minecraft:stick"}, "count": 1}}
        ]
    },
    {
        "id": "utility_gadgets",
        "name": "Utility & Redstone Gadgets",
        "namespace": "ug",
        "category": "Redstone & Tech",
        "description": "Pocket workbenches, portable void trash cans, auto-feeders, and brass lanterns.",
        "colors": ((190, 40, 30, 255), (240, 160, 50, 255)),
        "guidebook": {
            "title": "Engineer's Blueprints",
            "author": "Chief Engineer Nikola",
            "pages": [
                "§l§cUtility & Redstone Gadgets§r\n\nMaximize daily efficiency with portable gadgets and mechanical aids.",
                "§l§1Inventions§r\n\n§6Pocket Workbench§r: Inventory accessible crafting.\n§8Portable Void Trash Can§r: Incinerate junk stacks.\n§cAuto Nutrient Dispenser§r: Automated feeding system.\n§eBrass Miner's Lantern§r: Portable torch lighting."
            ]
        },
        "items": [
            {"id": "pocket_workbench", "name": "Pocket Workbench", "category": "equipment", "max_stack": 1, "icon_type": "workbench_pocket", "recipe": {"pattern": [" L ", "LCL", " L "], "key": {"L": "minecraft:leather", "C": "minecraft:crafting_table"}, "count": 1}},
            {"id": "void_trash_can", "name": "Portable Void Trash Can", "category": "equipment", "max_stack": 1, "icon_type": "trash_can", "recipe": {"pattern": [" I ", "ICI", " L "], "key": {"I": "minecraft:iron_ingot", "C": "minecraft:cauldron", "L": "minecraft:lava_bucket"}, "count": 1}},
            {"id": "auto_feeder", "name": "Auto Nutrient Dispenser", "category": "equipment", "max_stack": 1, "icon_type": "feeder_auto", "recipe": {"pattern": [" R ", "DHD", " R "], "key": {"R": "minecraft:redstone", "D": "minecraft:dropper", "H": "minecraft:hopper"}, "count": 1}},
            {"id": "brass_lantern", "name": "Brass Miner's Lantern", "category": "equipment", "max_stack": 1, "icon_type": "lantern_brass", "recipe": {"pattern": [" C ", "CTC", " C "], "key": {"C": "minecraft:copper_ingot", "T": "minecraft:torch"}, "count": 1}},
            {"id": "redstone_gear", "name": "Clockwork Cogwheel", "category": "items", "max_stack": 64, "icon_type": "cogwheel", "recipe": {"pattern": [" I ", "IRI", " I "], "key": {"I": "minecraft:iron_nugget", "R": "minecraft:redstone"}, "count": 4}}
        ]
    },
    {
        "id": "expanded_metallurgy",
        "name": "Expanded Metallurgy",
        "namespace": "em",
        "category": "Mining & Metallurgy",
        "description": "Copper broadswords, amethyst blades, ruby gems, and steel battleaxes.",
        "colors": ((200, 120, 80, 255), (220, 40, 60, 255)),
        "guidebook": {
            "title": "Metallurgist's Guide",
            "author": "Master Founder Balthazar",
            "pages": [
                "§l§eExpanded Metallurgy§r\n\nBridge mineral tiers with new weapon forgings and crystal blades.",
                "§l§1Metals & Gems§r\n\n§6Copper Broadsword§r (5 Dmg): Early copper weapon.\n§dAmethyst Blade§r (7 Dmg): Resonant crystal strike.\n§4Blood Ruby & Battleaxe§r (9 Dmg): Scorching heavy axe.\n§7Refined Steel Ingot§r: Smelted high-strength iron."
            ]
        },
        "items": [
            {"id": "copper_broadsword", "name": "Copper Broadsword", "category": "equipment", "max_stack": 1, "damage": 5, "icon_type": "sword_copper", "recipe": {"pattern": [" C ", " C ", " S "], "key": {"C": "minecraft:copper_ingot", "S": "minecraft:stick"}, "count": 1}},
            {"id": "amethyst_blade", "name": "Amethyst Crystalline Blade", "category": "equipment", "max_stack": 1, "damage": 7, "icon_type": "sword_amethyst", "recipe": {"pattern": [" A ", " A ", " G "], "key": {"A": "minecraft:amethyst_shard", "G": "minecraft:gold_ingot"}, "count": 1}},
            {"id": "ruby_gem", "name": "Blood Ruby", "category": "items", "max_stack": 64, "icon_type": "gem_ruby", "recipe": {"pattern": [" R ", "RDR", " R "], "key": {"R": "minecraft:redstone_block", "D": "minecraft:diamond"}, "count": 2}},
            {"id": "ruby_battleaxe", "name": "Ruby Battleaxe", "category": "equipment", "max_stack": 1, "damage": 9, "icon_type": "battleaxe_ruby", "recipe": {"pattern": ["RR ", "RS ", " S "], "key": {"R": "minecraft:redstone_block", "S": "minecraft:stick"}, "count": 1}},
            {"id": "steel_ingot", "name": "Refined Steel Ingot", "category": "items", "max_stack": 64, "icon_type": "ingot_steel", "recipe": {"pattern": [" C ", " I ", " C "], "key": {"C": "minecraft:coal", "I": "minecraft:iron_ingot"}, "count": 1}}
        ]
    },
    {
        "id": "bounty_contracts",
        "name": "Bounty Hunter Contracts",
        "namespace": "bh",
        "category": "Quests & Combat",
        "description": "Monster hunting scrolls, guild badges, slayer medallions, and honor tokens.",
        "colors": ((180, 140, 40, 255), (255, 215, 60, 255)),
        "guidebook": {
            "title": "Bounty Guild Handbook",
            "author": "Guildmaster Drake",
            "pages": [
                "§l§6Bounty Hunter Guild§r\n\nTake up contracts to cleanse hostile creatures from settlements.",
                "§l§1Guild Items§r\n\n§4Zombie Bounty Contract§r: Rotten flesh + paper.\n§2Creeper Bounty Contract§r: Gunpowder + paper.\n§6Hunter's Guild Badge§r: Proof of Guild standing.\n§eMonster Slayer Medallion§r: Diamond-forged trophy."
            ]
        },
        "items": [
            {"id": "bounty_scroll_zombie", "name": "Zombie Bounty Contract", "category": "items", "max_stack": 16, "icon_type": "contract_zombie", "recipe": {"pattern": [" R ", "PPP", " F "], "key": {"R": "minecraft:rotten_flesh", "P": "minecraft:paper", "F": "minecraft:feather"}, "count": 1}},
            {"id": "bounty_scroll_creeper", "name": "Creeper Bounty Contract", "category": "items", "max_stack": 16, "icon_type": "contract_creeper", "recipe": {"pattern": [" G ", "PPP", " F "], "key": {"G": "minecraft:gunpowder", "P": "minecraft:paper", "F": "minecraft:feather"}, "count": 1}},
            {"id": "hunter_badge", "name": "Hunter's Guild Badge", "category": "equipment", "max_stack": 1, "icon_type": "badge_guild", "recipe": {"pattern": [" G ", "GEG", " G "], "key": {"G": "minecraft:gold_ingot", "E": "minecraft:emerald"}, "count": 1}},
            {"id": "slayer_medallion", "name": "Monster Slayer Medallion", "category": "equipment", "max_stack": 1, "icon_type": "medallion_slayer", "recipe": {"pattern": [" C ", "DGD", " C "], "key": {"C": "minecraft:chain", "D": "minecraft:diamond", "G": "minecraft:gold_ingot"}, "count": 1}},
            {"id": "hunter_token", "name": "Guild Honor Token", "category": "items", "max_stack": 64, "icon_type": "token_guild", "recipe": {"pattern": [" I ", " G ", " I "], "key": {"I": "minecraft:iron_nugget", "G": "minecraft:gold_nugget"}, "count": 4}}
        ]
    },
    {
        "id": "boss_artifacts",
        "name": "Boss Artifacts & Totems",
        "namespace": "ba",
        "category": "Legendary",
        "description": "Dragon relic cores, totems of undying wrath, berserker blood charms, and void pendants.",
        "colors": ((130, 30, 180, 255), (255, 210, 50, 255)),
        "guidebook": {
            "title": "Ancient Relic Mythos",
            "author": "High Scholar Ozymandias",
            "pages": [
                "§l§5Boss Artifacts & Totems§r\n\nAssemble legendary relics from the remnants of slain world sovereigns.",
                "§l§1Legendary Artifacts§r\n\n§5Dragon Relic Core§r: Ender Dragon core energy.\n§4Totem of Undying Wrath§r: Nether Star infused survival totem.\n§cBerserker Blood Charm§r: Critical hit amplifier.\n§bVoid Defiance Pendant§r: Spatial resistance ward."
            ]
        },
        "items": [
            {"id": "dragon_relic_core", "name": "Dragon Relic Core", "category": "equipment", "max_stack": 1, "icon_type": "core_dragon", "recipe": {"pattern": [" E ", "DBD", " E "], "key": {"E": "minecraft:ender_pearl", "D": "minecraft:diamond_block", "B": "minecraft:dragon_breath"}, "count": 1}},
            {"id": "totem_of_wrath", "name": "Totem of Undying Wrath", "category": "equipment", "max_stack": 1, "icon_type": "totem_wrath", "recipe": {"pattern": [" G ", "TST", " G "], "key": {"G": "minecraft:gold_block", "T": "minecraft:totem_of_undying", "S": "minecraft:nether_star"}, "count": 1}},
            {"id": "berserker_charm", "name": "Berserker Blood Charm", "category": "equipment", "max_stack": 1, "icon_type": "charm_berserker", "recipe": {"pattern": [" R ", "RNR", " R "], "key": {"R": "minecraft:redstone_block", "N": "minecraft:netherite_ingot"}, "count": 1}},
            {"id": "void_pendant", "name": "Void Defiance Pendant", "category": "equipment", "max_stack": 1, "icon_type": "pendant_void", "recipe": {"pattern": [" C ", "OEO", " C "], "key": {"C": "minecraft:chain", "O": "minecraft:crying_obsidian", "E": "minecraft:ender_eye"}, "count": 1}},
            {"id": "ancient_relic_fragment", "name": "Ancient Relic Fragment", "category": "items", "max_stack": 64, "icon_type": "fragment_relic", "recipe": {"pattern": [" N ", " E ", " N "], "key": {"N": "minecraft:netherite_scrap", "E": "minecraft:echo_shard"}, "count": 2}}
        ]
    }
]
