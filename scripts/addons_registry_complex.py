"""
Definitions for the 20 Complex Add-ons (Addons 21 to 40).
Features multi-tier progression, machinery components, advanced catalysts,
summoning monoliths, energy systems, and rich multi-page guidebooks.
"""

COMPLEX_ADDONS = [
    # -------------------------------------------------------------
    # Addon 21: Industrial Automation & Steam Machinery
    # -------------------------------------------------------------
    {
        "id": "steam_machinery",
        "name": "Industrial Automation & Steam Machinery",
        "namespace": "sm",
        "category": "Tech & Machinery",
        "description": "Steam boilers, high-pressure pipes, mechanical macerators, automated conveyor belts, and engineer wrenches.",
        "colors": ((175, 95, 30, 255), (245, 175, 45, 255)),
        "guidebook": {
            "title": "Industrial Steam Works",
            "author": "Chief Mechanist Vance",
            "pages": [
                "§l§6Industrial Steam Works§r\n\nWelcome to the age of mechanization!\n\nHarness high-pressure steam boilers and mechanical gearboxes to process minerals, crush cobble into sand, and automate resource processing lines.",
                "§l§1Core Machinery§r\n\n§cSteam Boiler Vessel§r:\nCrafted with copper sheets, iron bars, and furnace core.\n\n§6Mechanical Macerator§r:\nCrushes raw ores into doubled refined powders.\n\n§7Engineer's Adjusting Wrench§r:\nConfigures steam pipe throughput.",
                "§l§1Logistics & Power§r\n\n§eConveyor Belt Assembly§r:\nTransports items continuously across factory floors.\n\n§8Pressure Pipe Conduit§r:\nChannels pressurized steam between boilers and heavy machines."
            ]
        },
        "items": [
            {"id": "engineer_wrench", "name": "Engineer's Adjusting Wrench", "category": "equipment", "max_stack": 1, "damage": 5, "icon_type": "wrench", "recipe": {"pattern": [" I ", " II", "S  "], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:copper_ingot"}, "count": 1}},
            {"id": "steam_boiler", "name": "Steam Boiler Core", "category": "items", "max_stack": 64, "icon_type": "boiler_core", "recipe": {"pattern": ["CCC", "CFC", "CCC"], "key": {"C": "minecraft:copper_ingot", "F": "minecraft:furnace"}, "count": 1}},
            {"id": "mechanical_macerator", "name": "Mechanical Macerator", "category": "items", "max_stack": 64, "icon_type": "macerator", "recipe": {"pattern": ["IPI", "IBI", "IRI"], "key": {"I": "minecraft:iron_block", "P": "minecraft:piston", "B": "sm:steam_boiler", "R": "minecraft:redstone"}, "count": 1}},
            {"id": "conveyor_belt", "name": "Conveyor Belt Track", "category": "items", "max_stack": 64, "icon_type": "conveyor", "recipe": {"pattern": ["LLL", "IRI", "LLL"], "key": {"L": "minecraft:leather", "I": "minecraft:iron_ingot", "R": "minecraft:redstone"}, "count": 8}},
            {"id": "steam_pipe", "name": "Reinforced Steam Pipe", "category": "items", "max_stack": 64, "icon_type": "pipe_steam", "recipe": {"pattern": ["CCC", "   ", "CCC"], "key": {"C": "minecraft:copper_ingot"}, "count": 6}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 22: Arcane Infusion & Runecrafting
    # -------------------------------------------------------------
    {
        "id": "arcane_infusion",
        "name": "Arcane Infusion & Runecrafting",
        "namespace": "ai",
        "category": "Magic & Crafting",
        "description": "Pedestal infusion altars, runic carving chisels, bound spell glyphs, and elemental matrices.",
        "colors": ((120, 40, 200, 255), (200, 110, 255, 255)),
        "guidebook": {
            "title": "Arcane Infusion Grimoire",
            "author": "Runemaster Eldrin",
            "pages": [
                "§l§5Arcane Infusion§r\n\nChannel latent planetary leyline currents into mundane stone pedestals to infuse items with divine enchantments.",
                "§l§1The Infusion Altar§r\n\n§dInfusion Altar Pedestal§r:\nConstructed from polished deepslate and lapis lazuli. Forms the centerpiece for ritual item binding.\n\n§bDiamond Runic Chisel§r:\nCarves sacred inscriptions onto blank tablets.",
                "§l§1Glyphs & Matrices§r\n\n§6Solar Infusion Glyph§r: Light and radiance ward.\n§3Abyssal Runestone Matrix§r: Focuses tide powers.\n§aPrimal Mana Matrix§r: Universal spellcraft catalyst."
            ]
        },
        "items": [
            {"id": "runic_chisel", "name": "Runic Carving Chisel", "category": "equipment", "max_stack": 1, "damage": 4, "icon_type": "chisel_runic", "recipe": {"pattern": ["  D", " S ", "S  "], "key": {"D": "minecraft:diamond", "S": "minecraft:stick"}, "count": 1}},
            {"id": "infusion_pedestal", "name": "Infusion Altar Pedestal", "category": "items", "max_stack": 64, "icon_type": "altar_pedestal", "recipe": {"pattern": ["LPL", " D ", "DDD"], "key": {"L": "minecraft:lapis_block", "P": "minecraft:ender_pearl", "D": "minecraft:polished_deepslate"}, "count": 1}},
            {"id": "solar_glyph", "name": "Solar Infusion Glyph", "category": "items", "max_stack": 64, "icon_type": "glyph_solar", "recipe": {"pattern": [" G ", "GAG", " G "], "key": {"G": "minecraft:gold_nugget", "A": "minecraft:amethyst_shard"}, "count": 2}},
            {"id": "mana_matrix", "name": "Primal Mana Matrix", "category": "items", "max_stack": 64, "icon_type": "matrix_mana", "recipe": {"pattern": ["EDE", "DAD", "EDE"], "key": {"E": "minecraft:emerald", "D": "minecraft:diamond", "A": "minecraft:amethyst_cluster"}, "count": 1}},
            {"id": "blank_runestone", "name": "Blank Runestone Tablet", "category": "items", "max_stack": 64, "icon_type": "runestone_blank", "recipe": {"pattern": [" D ", "DSD", " D "], "key": {"D": "minecraft:deepslate", "S": "minecraft:smooth_stone"}, "count": 4}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 23: Dragon Kin & Wyvern Breeding
    # -------------------------------------------------------------
    {
        "id": "wyvern_breeding",
        "name": "Dragon Kin & Wyvern Breeding",
        "namespace": "wb",
        "category": "Creatures & Breeding",
        "description": "Nesting incubators, dragon call whistles, wyvern saddles, and bottled dragon breath treats.",
        "colors": ((180, 40, 140, 255), (255, 120, 210, 255)),
        "guidebook": {
            "title": "Wyvern Breeder's Handbook",
            "author": "Dragonlord Ignis",
            "pages": [
                "§l§dWyvern Breeding§r\n\nDomesticate descendants of the great Ender Dragon! Hatch ancient eggs, care for wyvern hatchlings, and ride the skies.",
                "§l§1Hatching & Care§r\n\n§5Nesting Incubator Core§r:\nProvides constant thermal incubation for dragon and wyvern clutches.\n\n§eDragon Call Whistle§r:\nCommands flying mounts to hover, dive, or land safely.",
                "§l§1Riding Equipment§r\n\n§6Reinforced Wyvern Saddle§r:\nCushioned with diamond studs and netherite clasps for supersonic aerial maneuvering."
            ]
        },
        "items": [
            {"id": "wyvern_whistle", "name": "Dragon Call Whistle", "category": "equipment", "max_stack": 1, "icon_type": "whistle_dragon", "recipe": {"pattern": [" G ", " B ", "   "], "key": {"G": "minecraft:gold_ingot", "B": "minecraft:blaze_rod"}, "count": 1}},
            {"id": "incubator_core", "name": "Nesting Incubator Core", "category": "items", "max_stack": 64, "icon_type": "incubator_core", "recipe": {"pattern": ["HHH", "HBH", "HHH"], "key": {"H": "minecraft:hay_block", "B": "minecraft:magma_block"}, "count": 1}},
            {"id": "wyvern_saddle", "name": "Reinforced Wyvern Saddle", "category": "equipment", "max_stack": 1, "icon_type": "saddle_wyvern", "recipe": {"pattern": ["LDL", "LSL", "   "], "key": {"L": "minecraft:leather", "D": "minecraft:diamond", "S": "minecraft:saddle"}, "count": 1}},
            {"id": "dragon_treat", "name": "Draconic Vitality Treat", "category": "items", "max_stack": 64, "food": {"nutrition": 8, "saturation_modifier": "supernatural", "can_always_eat": True}, "icon_type": "treat_dragon", "recipe": {"pattern": [" D ", "GBG", " D "], "key": {"D": "minecraft:dragon_breath", "G": "minecraft:glistering_melon_slice", "B": "minecraft:beef"}, "count": 2}},
            {"id": "wyvern_scale", "name": "Hardened Wyvern Scale", "category": "items", "max_stack": 64, "icon_type": "scale_wyvern", "recipe": {"pattern": [" O ", "ODO", " O "], "key": {"O": "minecraft:obsidian", "D": "minecraft:diamond"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 24: Dimensional Portals & Rift Anchors
    # -------------------------------------------------------------
    {
        "id": "dimensional_rifts",
        "name": "Dimensional Portals & Rift Anchors",
        "namespace": "dr",
        "category": "Interdimensional",
        "description": "Rift stabilizers, dimensional anchors, void dials, and phased inter-realm compasses.",
        "colors": ((50, 20, 110, 255), (140, 70, 230, 255)),
        "guidebook": {
            "title": "Interdimensional Rift Annals",
            "author": "Voidstrider Chronos",
            "pages": [
                "§l§5Dimensional Rifts§r\n\nTear and tether stable wormholes across the Nether, Overworld, and End without building bulky obsidian frames.",
                "§l§1Anchoring Apparatus§r\n\n§dPhased Dimensional Anchor§r:\nLocks your coordinates across spatial dimensions.\n\n§bSpatial Void Dial§r:\nDisplays temporal rift stability in current realm.",
                "§l§1Rift Technology§r\n\n§eRift Stabilizer Core§r:\nPrevents dimensional backlash when leaping through unstable portals."
            ]
        },
        "items": [
            {"id": "dimensional_anchor", "name": "Phased Dimensional Anchor", "category": "equipment", "max_stack": 1, "icon_type": "anchor_dimension", "recipe": {"pattern": [" C ", "ORO", " C "], "key": {"C": "minecraft:crying_obsidian", "O": "minecraft:obsidian", "R": "minecraft:respawn_anchor"}, "count": 1}},
            {"id": "void_dial", "name": "Spatial Void Dial", "category": "equipment", "max_stack": 1, "icon_type": "dial_void", "recipe": {"pattern": [" G ", "ECE", " G "], "key": {"G": "minecraft:gold_ingot", "E": "minecraft:ender_eye", "C": "minecraft:compass"}, "count": 1}},
            {"id": "rift_stabilizer", "name": "Rift Stabilizer Core", "category": "items", "max_stack": 64, "icon_type": "core_stabilizer", "recipe": {"pattern": [" A ", "EDE", " A "], "key": {"A": "minecraft:amethyst_cluster", "E": "minecraft:echo_shard", "D": "minecraft:diamond_block"}, "count": 1}},
            {"id": "phased_compass", "name": "Inter-Realm Phased Compass", "category": "equipment", "max_stack": 1, "icon_type": "compass_phased", "recipe": {"pattern": [" E ", "LCL", " E "], "key": {"E": "minecraft:echo_shard", "L": "minecraft:lodestone", "C": "minecraft:compass"}, "count": 1}},
            {"id": "warp_resonator", "name": "Warp Resonator", "category": "items", "max_stack": 64, "icon_type": "resonator_warp", "recipe": {"pattern": [" P ", "RER", " P "], "key": {"P": "minecraft:prismarine_crystals", "R": "minecraft:redstone", "E": "minecraft:ender_pearl"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 25: Biome Botany & Genetic Crops
    # -------------------------------------------------------------
    {
        "id": "genetic_crops",
        "name": "Biome Botany & Genetic Crops",
        "namespace": "gc",
        "category": "Botany & Science",
        "description": "Cross-pollination frames, DNA gene extractors, hybrid seed pods, and greenhouse nutrient soil.",
        "colors": ((30, 150, 70, 255), (100, 230, 130, 255)),
        "guidebook": {
            "title": "Botanist's Genetics Journal",
            "author": "Dr. Linnaeus Bloom",
            "pages": [
                "§l§2Biome Botany & Genetics§r\n\nCrossbreed agricultural specimens to discover mutated high-yield crops with supernatural properties.",
                "§l§1Lab Equipment§r\n\n§aGene Extractor Chisel§r:\nExtracts pure plant DNA alleles from wild flora.\n\n§6Cross-Pollination Frame§r:\nAligns adjacent crop stems to trigger beneficial mutations.",
                "§l§1Supernatural Pods§r\n\n§eGolden Hybrid Seed Pod§r:\nGrows multi-harvest nutrient vegetables yielding bonus gold and saturation."
            ]
        },
        "items": [
            {"id": "gene_extractor", "name": "Gene Extractor Chisel", "category": "equipment", "max_stack": 1, "damage": 4, "icon_type": "extractor_gene", "recipe": {"pattern": ["  I", " G ", "S  "], "key": {"I": "minecraft:iron_ingot", "G": "minecraft:glass", "S": "minecraft:stick"}, "count": 1}},
            {"id": "pollination_frame", "name": "Cross-Pollination Frame", "category": "items", "max_stack": 64, "icon_type": "frame_pollination", "recipe": {"pattern": ["SSS", "SHS", "SSS"], "key": {"S": "minecraft:stick", "H": "minecraft:honeycomb"}, "count": 2}},
            {"id": "hybrid_seed_pod", "name": "Hybrid Seed Pod", "category": "nature", "max_stack": 64, "icon_type": "seed_hybrid", "recipe": {"pattern": ["PWP", "WNW", "PWP"], "key": {"P": "minecraft:pumpkin_seeds", "W": "minecraft:wheat_seeds", "N": "minecraft:nether_wart"}, "count": 4}},
            {"id": "nutrient_fertilizer", "name": "Rich Nutrient Fertilizer", "category": "items", "max_stack": 64, "icon_type": "fertilizer_rich", "recipe": {"pattern": [" B ", "RMR", " B "], "key": {"B": "minecraft:bone_meal", "R": "minecraft:rotten_flesh", "M": "minecraft:brown_mushroom"}, "count": 4}},
            {"id": "greenhouse_glass", "name": "Spectral Greenhouse Panel", "category": "items", "max_stack": 64, "icon_type": "glass_greenhouse", "recipe": {"pattern": [" G ", "GLG", " G "], "key": {"G": "minecraft:glass", "L": "minecraft:glowstone_dust"}, "count": 4}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 26: Advanced Mecha Armor & Exoskeletons
    # -------------------------------------------------------------
    {
        "id": "mecha_armor",
        "name": "Advanced Mecha Armor & Exoskeletons",
        "namespace": "ma",
        "category": "Armor & Cybernetics",
        "description": "Hydraulic powered exoskeleton frames, servo cores, jet jump thrusters, and shock absorbers.",
        "colors": ((70, 75, 90, 255), (150, 180, 230, 255)),
        "guidebook": {
            "title": "Cybernetic Rig Manual",
            "author": "Master Armorer Vulcan",
            "pages": [
                "§l§7Mecha Exoskeletons§r\n\nTransform standard survival armor into powered heavy mechanical rigs capable of deflecting massive blows.",
                "§l§1Exoskeleton Parts§r\n\n§bPowered Exoskeleton Frame§r:\nSteel chassis equipped with hydraulic servos and kinetic battery dampeners.\n\n§eHydraulic Jet Thruster§r:\nMounts to legs to provide high-altitude escape boosts.",
                "§l§1Power Supply§r\n\n§cHigh Density Energy Cell§r:\nPowers automated shielding and kinetic recoil springs."
            ]
        },
        "items": [
            {"id": "exoskeleton_frame", "name": "Exoskeleton Chassis Frame", "category": "equipment", "max_stack": 1, "icon_type": "chassis_mecha", "recipe": {"pattern": ["I I", "ICI", "IPI"], "key": {"I": "minecraft:iron_block", "C": "minecraft:chainmail_chestplate", "P": "minecraft:piston"}, "count": 1}},
            {"id": "jet_thruster", "name": "Hydraulic Jet Thruster", "category": "equipment", "max_stack": 1, "icon_type": "thruster_jet", "recipe": {"pattern": [" F ", "RCR", " F "], "key": {"F": "minecraft:firework_rocket", "R": "minecraft:redstone", "C": "minecraft:copper_block"}, "count": 1}},
            {"id": "hydraulic_servo", "name": "Heavy Hydraulic Servo", "category": "items", "max_stack": 64, "icon_type": "servo_hydraulic", "recipe": {"pattern": [" I ", "CPC", " I "], "key": {"I": "minecraft:iron_ingot", "C": "minecraft:copper_ingot", "P": "minecraft:piston"}, "count": 2}},
            {"id": "energy_cell", "name": "Dense Energy Cell", "category": "items", "max_stack": 64, "icon_type": "cell_energy", "recipe": {"pattern": ["RGR", "GLG", "RGR"], "key": {"R": "minecraft:redstone_block", "G": "minecraft:gold_ingot", "L": "minecraft:lapis_block"}, "count": 1}},
            {"id": "shock_absorber", "name": "Kinetic Shock Absorber", "category": "equipment", "max_stack": 1, "icon_type": "shock_absorber", "recipe": {"pattern": [" S ", "LPL", " S "], "key": {"S": "minecraft:slime_ball", "L": "minecraft:leather", "P": "minecraft:piston"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 27: Deep Dark Catacombs & Warden Relics
    # -------------------------------------------------------------
    {
        "id": "warden_relics",
        "name": "Deep Dark Catacombs & Warden Relics",
        "namespace": "wr",
        "category": "Deep Dark & Sculk",
        "description": "Sculk resonance chimes, sonic boom staves, soul cages, and stealth shadowcloaks.",
        "colors": ((10, 40, 50, 255), (30, 160, 170, 255)),
        "guidebook": {
            "title": "Sculk Resonance Tome",
            "author": "Deep Hollow Chronicler",
            "pages": [
                "§l§3Warden Relics & Sculk§r\n\nExtract sonic vibrations from deep dark ancient cities to weaponize acoustic resonance against all who oppose you.",
                "§l§1Acoustic Relics§r\n\n§3Sonic Boom Staff§r (10 Dmg):\nChannels concentrated sonic pulses across long distances bypassing standard armor.\n\n§bSculk Resonance Chime§r:\nEmits frequencies that distract hostiles and detect hidden cave passages.",
                "§l§1Stealth Cloaks§r\n\n§8Shadowcloak Mantle§r:\nNullifies footstep vibrations, allowing silent movement."
            ]
        },
        "items": [
            {"id": "sonic_staff", "name": "Sonic Boom Staff", "category": "equipment", "max_stack": 1, "damage": 10, "icon_type": "staff_sonic", "recipe": {"pattern": [" E ", " S ", " S "], "key": {"E": "minecraft:echo_shard", "S": "minecraft:sculk"}, "count": 1}},
            {"id": "sculk_chime", "name": "Sculk Resonance Chime", "category": "equipment", "max_stack": 1, "icon_type": "chime_sculk", "recipe": {"pattern": [" A ", "AEA", " S "], "key": {"A": "minecraft:amethyst_shard", "E": "minecraft:echo_shard", "S": "minecraft:stick"}, "count": 1}},
            {"id": "shadowcloak", "name": "Shadowcloak Mantle", "category": "equipment", "max_stack": 1, "icon_type": "mantle_shadow", "recipe": {"pattern": ["SES", "SLS", " S "], "key": {"S": "minecraft:sculk", "E": "minecraft:echo_shard", "L": "minecraft:leather"}, "count": 1}},
            {"id": "soul_cage", "name": "Resonant Soul Cage", "category": "items", "max_stack": 64, "icon_type": "cage_soul", "recipe": {"pattern": ["IBI", "BSB", "IBI"], "key": {"I": "minecraft:iron_bars", "B": "minecraft:sculk_catalyst", "S": "minecraft:soul_sand"}, "count": 1}},
            {"id": "sculk_tendril", "name": "Hardened Sculk Tendril", "category": "items", "max_stack": 64, "icon_type": "tendril_sculk", "recipe": {"pattern": [" S ", "SES", " S "], "key": {"S": "minecraft:sculk_vein", "E": "minecraft:echo_shard"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 28: Modular Bows & Ballistics
    # -------------------------------------------------------------
    {
        "id": "modular_bows",
        "name": "Modular Bows & Ballistics",
        "namespace": "mo",
        "category": "Advanced Archery",
        "description": "Ergonomic composite grips, flexible limbs, optic sights, and heavy ballistic bolts.",
        "colors": ((110, 80, 50, 255), (200, 160, 100, 255)),
        "guidebook": {
            "title": "Ballistic Engineer's Field Guide",
            "author": "Marksman Vance",
            "pages": [
                "§l§6Modular Bows & Ballistics§r\n\nStandard recurve bows cannot compare with customizable modular archery chassis engineered for precision.",
                "§l§1Bow Modules§r\n\n§6Composite Ergonomic Grip§r:\nImproves steady aim under harsh conditions.\n\n§eOptic Scope Sight§r:\nAmethyst magnifying lens for pinpoint headshots.",
                "§l§1Modular Chassis§r\n\n§7Ballistic Compound Frame§r (9 Dmg):\nDelivers hyper-velocity broadheads over extreme ranges."
            ]
        },
        "items": [
            {"id": "compound_frame", "name": "Ballistic Compound Frame", "category": "equipment", "max_stack": 1, "damage": 9, "icon_type": "bow_compound", "recipe": {"pattern": [" GS", "C S", " GS"], "key": {"G": "mo:composite_grip", "C": "minecraft:iron_ingot", "S": "minecraft:string"}, "count": 1}},
            {"id": "composite_grip", "name": "Composite Ergonomic Grip", "category": "items", "max_stack": 64, "icon_type": "grip_composite", "recipe": {"pattern": [" L ", "ILI", " L "], "key": {"L": "minecraft:leather", "I": "minecraft:iron_ingot"}, "count": 2}},
            {"id": "optic_sight", "name": "Optic Scope Sight", "category": "equipment", "max_stack": 1, "icon_type": "sight_optic", "recipe": {"pattern": [" C ", "GAG", " C "], "key": {"C": "minecraft:copper_ingot", "G": "minecraft:glass", "A": "minecraft:amethyst_shard"}, "count": 1}},
            {"id": "ballistic_bolt", "name": "Heavy Ballistic Bolt", "category": "items", "max_stack": 64, "icon_type": "bolt_ballistic", "recipe": {"pattern": [" I ", " C ", " F "], "key": {"I": "minecraft:iron_block", "C": "minecraft:copper_ingot", "F": "minecraft:feather"}, "count": 8}},
            {"id": "tension_cable", "name": "High Tension Bowstring", "category": "items", "max_stack": 64, "icon_type": "cable_tension", "recipe": {"pattern": ["SSS", "SCS", "SSS"], "key": {"S": "minecraft:string", "C": "minecraft:chain"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 29: Siege Engineering & Cannons
    # -------------------------------------------------------------
    {
        "id": "siege_cannons",
        "name": "Siege Engineering & Cannons",
        "namespace": "sc",
        "category": "Siege & Cannons",
        "description": "Heavy cast iron cannons, powder kegs, solid iron cannonballs, and mortar aiming quadrants.",
        "colors": ((50, 50, 60, 255), (180, 70, 30, 255)),
        "guidebook": {
            "title": "Siege Artillery Codex",
            "author": "Master Gunner Cromwell",
            "pages": [
                "§l§8Siege Engineering & Cannons§r\n\nBreach formidable stone fortifications and obliterate raiding waves with heavy artillery cannons.",
                "§l§1Artillery Parts§r\n\n§8Cast Iron Cannon Barrel§r:\nThick-walled barrel forged to withstand massive gunpowder propellant explosions.\n\n§cCompressed Powder Keg§r:\nTriple-distilled propellant charge.",
                "§l§1Ammunition & Targeting§r\n\n§7Solid Iron Cannonball§r:\nHeavy spherical projectile causing massive impact cratering.\n\n§eMortar Aiming Quadrant§r:\nCalibrates firing trajectory."
            ]
        },
        "items": [
            {"id": "cannon_barrel", "name": "Cast Iron Cannon Barrel", "category": "items", "max_stack": 16, "icon_type": "barrel_cannon", "recipe": {"pattern": ["III", "I I", "III"], "key": {"I": "minecraft:iron_block"}, "count": 1}},
            {"id": "cannonball", "name": "Solid Iron Cannonball", "category": "items", "max_stack": 64, "icon_type": "cannonball_iron", "recipe": {"pattern": [" I ", "III", " I "], "key": {"I": "minecraft:iron_ingot"}, "count": 4}},
            {"id": "powder_keg", "name": "Compressed Powder Keg", "category": "items", "max_stack": 16, "icon_type": "keg_powder", "recipe": {"pattern": ["PPP", "GTG", "PPP"], "key": {"P": "minecraft:oak_planks", "G": "minecraft:gunpowder", "T": "minecraft:tnt"}, "count": 2}},
            {"id": "aiming_quadrant", "name": "Mortar Aiming Quadrant", "category": "equipment", "max_stack": 1, "icon_type": "quadrant_aim", "recipe": {"pattern": [" C ", "CBC", " C "], "key": {"C": "minecraft:copper_ingot", "B": "minecraft:compass"}, "count": 1}},
            {"id": "firing_ramrod", "name": "Heavy Artillery Ramrod", "category": "equipment", "max_stack": 1, "damage": 5, "icon_type": "ramrod_artillery", "recipe": {"pattern": ["  I", " S ", "S  "], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:stick"}, "count": 1}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 30: Celestial Astrology & Moon Magic
    # -------------------------------------------------------------
    {
        "id": "celestial_astrology",
        "name": "Celestial Astrology & Moon Magic",
        "namespace": "ca",
        "category": "Astrology & Magic",
        "description": "Star observatory lenses, celestial constellation charts, lunar talismans, and starlight crystals.",
        "colors": ((30, 25, 90, 255), (240, 220, 110, 255)),
        "guidebook": {
            "title": "Celestial Starlight Almanac",
            "author": "Astrologer Cassiopeia",
            "pages": [
                "§l§9Celestial Astrology§r\n\nAttune to the cosmic dance of the sun, moon, and stars to empower mystical lunar talismans.",
                "§l§1Stargazing Instruments§r\n\n§bObservatory Starlight Lens§r:\nFocuses moonlight rays onto astrological altars.\n\n§eCelestial Star Chart§r:\nParchment documenting planetary alignments for night blessings.",
                "§l§1Cosmic Talismans§r\n\n§dLunar Phases Talisman§r:\nGrants night sight and high jumping under open starry skies."
            ]
        },
        "items": [
            {"id": "observatory_lens", "name": "Observatory Starlight Lens", "category": "equipment", "max_stack": 1, "icon_type": "lens_celestial", "recipe": {"pattern": [" G ", "GAG", " G "], "key": {"G": "minecraft:gold_ingot", "A": "minecraft:amethyst_cluster"}, "count": 1}},
            {"id": "star_chart", "name": "Celestial Star Chart", "category": "items", "max_stack": 16, "icon_type": "chart_star", "recipe": {"pattern": [" L ", "PPP", " G "], "key": {"L": "minecraft:lapis_lazuli", "P": "minecraft:paper", "G": "minecraft:glowstone_dust"}, "count": 1}},
            {"id": "lunar_talisman", "name": "Lunar Phases Talisman", "category": "equipment", "max_stack": 1, "icon_type": "talisman_lunar", "recipe": {"pattern": [" C ", "QMQ", " C "], "key": {"C": "minecraft:chain", "Q": "minecraft:quartz", "M": "minecraft:amethyst_shard"}, "count": 1}},
            {"id": "starlight_crystal", "name": "Condensed Starlight Crystal", "category": "items", "max_stack": 64, "icon_type": "crystal_starlight", "recipe": {"pattern": [" D ", "GAG", " D "], "key": {"D": "minecraft:diamond", "G": "minecraft:glowstone_dust", "A": "minecraft:amethyst_shard"}, "count": 2}},
            {"id": "astrolabe", "name": "Brass Astrolabe", "category": "equipment", "max_stack": 1, "icon_type": "astrolabe_brass", "recipe": {"pattern": [" C ", "CGC", " C "], "key": {"C": "minecraft:copper_ingot", "G": "minecraft:gold_ingot"}, "count": 1}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 31: Cooking Automata & Bakery Machinery
    # -------------------------------------------------------------
    {
        "id": "bakery_machinery",
        "name": "Cooking Automata & Bakery Machinery",
        "namespace": "bm",
        "category": "Automated Cooking",
        "description": "Mechanical flour grain mills, industrial brick ovens, automatic churners, and artisan pastries.",
        "colors": ((190, 120, 60, 255), (255, 215, 130, 255)),
        "guidebook": {
            "title": "Automated Bakery Gazette",
            "author": "Master Baker Pierre",
            "pages": [
                "§l§6Bakery Machinery§r\n\nRevolutionize your kitchen with automated mills and high-throughput baking stations.",
                "§l§1Kitchen Machinery§r\n\n§eMechanical Grain Mill§r:\nMills bundles of wheat into ultra-fine baking flour.\n\n§cIndustrial Brick Oven§r:\nTriple-speed baking for artisanal pastries, breads, and meat pies.",
                "§l§1Automated Churning§r\n\n§6Automatic Butter Churner§r:\nProcesses bucket milk into sweet cream and butter pats."
            ]
        },
        "items": [
            {"id": "grain_mill", "name": "Mechanical Grain Mill", "category": "items", "max_stack": 64, "icon_type": "mill_grain", "recipe": {"pattern": [" S ", "IHI", " S "], "key": {"S": "minecraft:smooth_stone", "I": "minecraft:iron_ingot", "H": "minecraft:hopper"}, "count": 1}},
            {"id": "industrial_oven", "name": "Industrial Brick Oven", "category": "items", "max_stack": 64, "icon_type": "oven_industrial", "recipe": {"pattern": ["BBB", "BFB", "BBB"], "key": {"B": "minecraft:bricks", "F": "minecraft:blast_furnace"}, "count": 1}},
            {"id": "butter_churner", "name": "Automatic Butter Churner", "category": "items", "max_stack": 64, "icon_type": "churner_butter", "recipe": {"pattern": [" P ", "IBI", " P "], "key": {"P": "minecraft:oak_planks", "I": "minecraft:iron_ingot", "B": "minecraft:bucket"}, "count": 1}},
            {"id": "artisan_pastry", "name": "Artisan Cream Pastry", "category": "items", "max_stack": 16, "food": {"nutrition": 9, "saturation_modifier": "supernatural", "can_always_eat": False}, "icon_type": "pastry_artisan", "recipe": {"pattern": [" S ", "WEW", " B "], "key": {"S": "minecraft:sugar", "W": "minecraft:wheat", "E": "minecraft:egg", "B": "minecraft:sweet_berries"}, "count": 2}},
            {"id": "bakers_paddle", "name": "Wooden Baker's Paddle", "category": "equipment", "max_stack": 1, "damage": 4, "icon_type": "paddle_baker", "recipe": {"pattern": [" P ", " P ", " S "], "key": {"P": "minecraft:oak_slab", "S": "minecraft:stick"}, "count": 1}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 32: Necromancy & Soul Binding
    # -------------------------------------------------------------
    {
        "id": "necromancy_souls",
        "name": "Necromancy & Soul Binding",
        "namespace": "ns",
        "category": "Dark Magic",
        "description": "Soul phylacteries, necromancer summoning staves, resurrection ritual chalk, and bone effigies.",
        "colors": ((30, 45, 35, 255), (100, 230, 160, 255)),
        "guidebook": {
            "title": "Necromantic Rituals",
            "author": "Lich Lord Mortis",
            "pages": [
                "§l§2Necromancy & Soul Binding§r\n\nCommand dark powers of the veil to reanimate skeletal defenders and store spirit life-force in crystalline vessels.",
                "§l§1Artifacts of the Veil§r\n\n§aBone Minion Summoning Staff§r (8 Dmg):\nRaises friendly skeleton guardians to fight beside you.\n\n§2Soul Phylactery Vessel§r:\nHarvests soul energy upon defeating undead.",
                "§l§1Rituals§r\n\n§fResurrection Ritual Chalk§r:\nDraws ritual circles to bind lingering souls."
            ]
        },
        "items": [
            {"id": "necromancer_staff", "name": "Bone Summoning Staff", "category": "equipment", "max_stack": 1, "damage": 8, "icon_type": "staff_bone", "recipe": {"pattern": [" B ", " S ", " S "], "key": {"B": "minecraft:wither_skeleton_skull", "S": "minecraft:bone"}, "count": 1}},
            {"id": "soul_phylactery", "name": "Soul Phylactery Vessel", "category": "equipment", "max_stack": 1, "icon_type": "phylactery_soul", "recipe": {"pattern": [" G ", "GDG", " G "], "key": {"G": "minecraft:glass", "D": "minecraft:diamond"}, "count": 1}},
            {"id": "ritual_chalk", "name": "Resurrection Ritual Chalk", "category": "items", "max_stack": 16, "icon_type": "chalk_ritual", "recipe": {"pattern": [" B ", " C ", " B "], "key": {"B": "minecraft:bone_meal", "C": "minecraft:clay_ball"}, "count": 4}},
            {"id": "bone_effigy", "name": "Protective Bone Effigy", "category": "items", "max_stack": 16, "icon_type": "effigy_bone", "recipe": {"pattern": [" B ", "BSB", " B "], "key": {"B": "minecraft:bone", "S": "minecraft:soul_sand"}, "count": 1}},
            {"id": "essence_of_decay", "name": "Essence of Decay", "category": "items", "max_stack": 64, "icon_type": "essence_decay", "recipe": {"pattern": [" R ", "FSF", " R "], "key": {"R": "minecraft:rotten_flesh", "F": "minecraft:fermented_spider_eye", "S": "minecraft:spider_eye"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 33: Submarine Technology & Deep Abyss
    # -------------------------------------------------------------
    {
        "id": "submarine_tech",
        "name": "Submarine Technology & Deep Abyss",
        "namespace": "st",
        "category": "Submarine & Tech",
        "description": "Deep-sea ballast tanks, acoustic sonar radars, pressurized torpedoes, and abyssal suits.",
        "colors": ((15, 60, 100, 255), (60, 200, 240, 255)),
        "guidebook": {
            "title": "Submariner's Blueprint Manual",
            "author": "Chief Diver Cousteau",
            "pages": [
                "§l§3Submarine Technology§r\n\nNavigate deepest ocean ravines and crush zones with heavy pressure hulls and acoustic sonar arrays.",
                "§l§1Vessel Components§r\n\n§3Submarine Dive Ballast Tank§r:\nRegulates buoyancy to dive deep or surface rapidly.\n\n§bAcoustic Sonar Radar§r:\nPings underwater hostile entities and submerged shipwrecks.",
                "§l§1Armament§r\n\n§7Pressurized Torpedo Bolt§r (10 Dmg):\nHigh-yield aquatic explosive projectile."
            ]
        },
        "items": [
            {"id": "dive_ballast", "name": "Submarine Dive Ballast", "category": "items", "max_stack": 16, "icon_type": "ballast_dive", "recipe": {"pattern": ["CCC", "CFC", "CCC"], "key": {"C": "minecraft:copper_block", "F": "minecraft:iron_bars"}, "count": 1}},
            {"id": "sonar_radar", "name": "Acoustic Sonar Radar", "category": "equipment", "max_stack": 1, "icon_type": "radar_sonar", "recipe": {"pattern": [" C ", "PCP", " R "], "key": {"C": "minecraft:compass", "P": "minecraft:prismarine_crystals", "R": "minecraft:redstone"}, "count": 1}},
            {"id": "torpedo_bolt", "name": "Pressurized Torpedo Bolt", "category": "items", "max_stack": 64, "damage": 10, "icon_type": "bolt_torpedo", "recipe": {"pattern": [" I ", "CTC", " F "], "key": {"I": "minecraft:iron_block", "C": "minecraft:copper_ingot", "T": "minecraft:tnt", "F": "minecraft:feather"}, "count": 4}},
            {"id": "pressure_hull_plate", "name": "Reinforced Pressure Plate", "category": "items", "max_stack": 64, "icon_type": "plate_pressure_hull", "recipe": {"pattern": ["III", "CCC", "III"], "key": {"I": "minecraft:iron_ingot", "C": "minecraft:copper_ingot"}, "count": 4}},
            {"id": "sub_depth_gauge", "name": "Abyssal Depth Gauge", "category": "equipment", "max_stack": 1, "icon_type": "gauge_depth", "recipe": {"pattern": [" G ", "GCG", " G "], "key": {"G": "minecraft:gold_ingot", "C": "minecraft:clock"}, "count": 1}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 34: Biochemical Alchemy & Mutation Serums
    # -------------------------------------------------------------
    {
        "id": "biochem_serums",
        "name": "Biochemical Alchemy & Mutation Serums",
        "namespace": "bs",
        "category": "Biochemistry",
        "description": "Centrifuge alembics, gene mutagen catalysts, beast mutation serums, and hazmat gas masks.",
        "colors": ((50, 160, 40, 255), (180, 255, 60, 255)),
        "guidebook": {
            "title": "Mutagen Lab Records",
            "author": "Dr. Frankenstein Jekyll",
            "pages": [
                "§l§aBiochemical Alchemy§r\n\nSynthesize unstable biological serums to temporarily supercharge player attributes like jump height, strike power, and resistance.",
                "§l§1Lab Apparatus§r\n\n§2Centrifuge Alembic§r:\nSeparates organic cellular fluids into concentrated reagents.\n\n§aBeast Mutation Serum§r:\nGrants supernatural strength and resistance at the cost of intense hunger.",
                "§l§1Safety Gear§r\n\n§eHazmat Bio-Respirator Mask§r:\nWards against poisonous fumes and chemical gases."
            ]
        },
        "items": [
            {"id": "centrifuge_alembic", "name": "Centrifuge Alembic", "category": "items", "max_stack": 64, "icon_type": "alembic_centrifuge", "recipe": {"pattern": [" G ", "IBI", " I "], "key": {"G": "minecraft:glass_bottle", "I": "minecraft:iron_ingot", "B": "minecraft:brewing_stand"}, "count": 1}},
            {"id": "mutation_serum", "name": "Beast Mutation Serum", "category": "items", "max_stack": 16, "food": {"nutrition": 2, "saturation_modifier": "supernatural", "can_always_eat": True}, "icon_type": "serum_mutation", "recipe": {"pattern": [" S ", "EBE", " S "], "key": {"S": "minecraft:spider_eye", "E": "minecraft:fermented_spider_eye", "B": "minecraft:glass_bottle"}, "count": 2}},
            {"id": "hazmat_mask", "name": "Hazmat Bio-Respirator", "category": "equipment", "max_stack": 1, "icon_type": "mask_hazmat", "recipe": {"pattern": [" L ", "LGL", " C "], "key": {"L": "minecraft:leather", "G": "minecraft:glass", "C": "minecraft:charcoal"}, "count": 1}},
            {"id": "bio_catalyst", "name": "Gene Mutagen Catalyst", "category": "items", "max_stack": 64, "icon_type": "catalyst_bio", "recipe": {"pattern": [" R ", "GNG", " R "], "key": {"R": "minecraft:redstone", "G": "minecraft:glowstone_dust", "N": "minecraft:nether_wart"}, "count": 2}},
            {"id": "antidote_vial", "name": "Universal Antidote Vial", "category": "items", "max_stack": 16, "food": {"nutrition": 4, "saturation_modifier": "normal", "can_always_eat": True}, "icon_type": "vial_antidote", "recipe": {"pattern": [" H ", " M ", " B "], "key": {"H": "minecraft:honey_bottle", "M": "minecraft:milk_bucket", "B": "minecraft:glass_bottle"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 35: Castle Defense Automatons & Golems
    # -------------------------------------------------------------
    {
        "id": "castle_automatons",
        "name": "Castle Defense Automatons & Golems",
        "namespace": "ca2",
        "category": "Golems & Automatons",
        "description": "Brass sentry turret cores, automaton command wands, clockwork golem hearts, and repair wrenches.",
        "colors": ((160, 110, 40, 255), (230, 190, 70, 255)),
        "guidebook": {
            "title": "Automaton Sentry Blueprints",
            "author": "Grand Clockmaker Daedalus",
            "pages": [
                "§l§6Castle Automatons§r\n\nBuild autonomous brass sentries to guard fortress gates and castle walls against nighttime siege raids.",
                "§l§1Mechanical Guardians§r\n\n§eClockwork Golem Heart§r:\nMechanical core that breathes life into iron and brass automaton frames.\n\n§6Brass Sentry Turret Core§r:\nStationary turret unit that targets approaching hostile mobs.",
                "§l§1Command & Maintenance§r\n\n§7Automaton Command Baton§r:\nDirects automaton guards to patrol, guard, or follow."
            ]
        },
        "items": [
            {"id": "golem_heart", "name": "Clockwork Golem Heart", "category": "items", "max_stack": 64, "icon_type": "heart_golem", "recipe": {"pattern": [" C ", "RIR", " C "], "key": {"C": "minecraft:copper_ingot", "R": "minecraft:redstone_block", "I": "minecraft:iron_block"}, "count": 1}},
            {"id": "sentry_core", "name": "Brass Sentry Turret Core", "category": "items", "max_stack": 64, "icon_type": "core_sentry", "recipe": {"pattern": [" I ", "CDC", " I "], "key": {"I": "minecraft:iron_ingot", "C": "minecraft:copper_block", "D": "minecraft:dispenser"}, "count": 1}},
            {"id": "command_baton", "name": "Automaton Command Baton", "category": "equipment", "max_stack": 1, "damage": 5, "icon_type": "baton_command", "recipe": {"pattern": ["  G", " S ", "S  "], "key": {"G": "minecraft:gold_ingot", "S": "minecraft:stick"}, "count": 1}},
            {"id": "repair_kit", "name": "Automaton Repair Tool", "category": "equipment", "max_stack": 1, "icon_type": "kit_repair", "recipe": {"pattern": [" I ", "SIS", " I "], "key": {"I": "minecraft:iron_ingot", "S": "minecraft:slime_ball"}, "count": 1}},
            {"id": "brass_gear", "name": "Heavy Brass Cogwheel", "category": "items", "max_stack": 64, "icon_type": "gear_brass", "recipe": {"pattern": [" C ", "CIC", " C "], "key": {"C": "minecraft:copper_ingot", "I": "minecraft:iron_nugget"}, "count": 4}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 36: Energy Shields & Forcefield Emitters
    # -------------------------------------------------------------
    {
        "id": "forcefield_shields",
        "name": "Energy Shields & Forcefield Emitters",
        "namespace": "fs",
        "category": "Energy & Shields",
        "description": "Forcefield emitter pylons, shield frequency modulators, energy deflector cells, and kinetic barriers.",
        "colors": ((20, 100, 190, 255), (100, 210, 255, 255)),
        "guidebook": {
            "title": "Forcefield Array Manual",
            "author": "Barrier Architect Maxwell",
            "pages": [
                "§l§bEnergy Shields & Forcefields§r\n\nProject luminous barrier envelopes to ward your base against creeper blast destruction and skeleton arrow volleys.",
                "§l§1Barrier Emitters§r\n\n§bForcefield Pylon Emitter§r:\nGenerates an impenetrable spherical energy barrier.\n\n§eShield Frequency Modulator§r:\nPermits friendly allies to pass through active forcefield zones.",
                "§l§1Personal Deflectors§r\n\n§aKinetic Barrier Aegis§r:\nPortable shield deflecting high-velocity incoming projectiles."
            ]
        },
        "items": [
            {"id": "forcefield_emitter", "name": "Forcefield Pylon Emitter", "category": "items", "max_stack": 64, "icon_type": "emitter_forcefield", "recipe": {"pattern": [" D ", "IBI", " D "], "key": {"D": "minecraft:diamond", "I": "minecraft:iron_block", "B": "minecraft:beacon"}, "count": 1}},
            {"id": "shield_modulator", "name": "Shield Frequency Modulator", "category": "equipment", "max_stack": 1, "icon_type": "modulator_shield", "recipe": {"pattern": [" R ", "PAP", " R "], "key": {"R": "minecraft:redstone", "P": "minecraft:prismarine_crystals", "A": "minecraft:amethyst_shard"}, "count": 1}},
            {"id": "kinetic_barrier", "name": "Kinetic Barrier Aegis", "category": "equipment", "max_stack": 1, "icon_type": "barrier_kinetic", "recipe": {"pattern": ["DDD", "DSD", " D "], "key": {"D": "minecraft:diamond", "S": "minecraft:shield"}, "count": 1}},
            {"id": "flux_capacitor", "name": "Energy Flux Capacitor", "category": "items", "max_stack": 64, "icon_type": "capacitor_flux", "recipe": {"pattern": ["RGR", "GLG", "RGR"], "key": {"R": "minecraft:redstone_block", "G": "minecraft:gold_block", "L": "minecraft:lapis_block"}, "count": 1}},
            {"id": "deflector_shard", "name": "Resonant Deflector Shard", "category": "items", "max_stack": 64, "icon_type": "shard_deflector", "recipe": {"pattern": [" P ", "ADA", " P "], "key": {"P": "minecraft:prismarine_shard", "A": "minecraft:amethyst_shard", "D": "minecraft:diamond"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 37: Meteorology & Weather Weathering
    # -------------------------------------------------------------
    {
        "id": "weather_meteorology",
        "name": "Meteorology & Weather Systems",
        "namespace": "wm",
        "category": "Weather & Atmosphere",
        "description": "Lightning accumulator rods, rain condensation totems, storm call horns, and atmospheric barometers.",
        "colors": ((80, 110, 140, 255), (190, 220, 255, 255)),
        "guidebook": {
            "title": "Meteorologist's Weather Atlas",
            "author": "Cloudweaver Zephyrus",
            "pages": [
                "§l§3Meteorology & Weather§r\n\nRead barometric trends and command storm systems to summon nourishing rainfall or harvest lightning power.",
                "§l§1Atmospheric Tools§r\n\n§bBrass Precision Barometer§r:\nForecasts upcoming rain and thunderstorms.\n\n§eLightning Accumulator Rod§r:\nStores raw electrical discharge during lightning strikes into reusable battery cells.",
                "§l§1Storm Calling§r\n\n§fTempest Calling Horn§r:\nBlasts resonant sound to summon cooling thunderstorm rains."
            ]
        },
        "items": [
            {"id": "storm_horn", "name": "Tempest Calling Horn", "category": "equipment", "max_stack": 1, "icon_type": "horn_storm", "recipe": {"pattern": [" C ", " G ", " C "], "key": {"C": "minecraft:copper_ingot", "G": "minecraft:goat_horn"}, "count": 1}},
            {"id": "barometer_brass", "name": "Brass Precision Barometer", "category": "equipment", "max_stack": 1, "icon_type": "barometer_brass", "recipe": {"pattern": [" C ", "CGC", " C "], "key": {"C": "minecraft:copper_ingot", "G": "minecraft:glass"}, "count": 1}},
            {"id": "lightning_accumulator", "name": "Lightning Accumulator Rod", "category": "items", "max_stack": 64, "icon_type": "accumulator_lightning", "recipe": {"pattern": [" L ", "LCL", " L "], "key": {"L": "minecraft:lightning_rod", "C": "minecraft:copper_block"}, "count": 1}},
            {"id": "cloud_condenser", "name": "Cloud Condenser Vessel", "category": "items", "max_stack": 64, "icon_type": "condenser_cloud", "recipe": {"pattern": [" P ", "PBP", " P "], "key": {"P": "minecraft:prismarine_shard", "B": "minecraft:bucket"}, "count": 1}},
            {"id": "storm_crystal", "name": "Charged Storm Crystal", "category": "items", "max_stack": 64, "icon_type": "crystal_storm", "recipe": {"pattern": [" A ", "DLD", " A "], "key": {"A": "minecraft:amethyst_shard", "D": "minecraft:diamond", "L": "minecraft:lightning_rod"}, "count": 1}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 38: Archaeology & Fossil Reconstruction
    # -------------------------------------------------------------
    {
        "id": "archaeology_fossils",
        "name": "Archaeology & Fossil Reconstruction",
        "namespace": "af2",
        "category": "Archaeology & Fossils",
        "description": "Sifting sieve tables, fossil cleaning solvents, amber extractors, and ancient dinosaur skeleton displays.",
        "colors": ((160, 130, 90, 255), (230, 200, 140, 255)),
        "guidebook": {
            "title": "Archaeologist's Field Journal",
            "author": "Professor Indiana Bones",
            "pages": [
                "§l§6Archaeology & Fossils§r\n\nExcavate primeval fossils buried beneath desert sands and gravel beds to reconstruct prehistoric specimens.",
                "§l§1Excavation Equipment§r\n\n§eArcheological Sieve Table§r:\nSifts gravel and suspicious sand to uncover rare fossil bones and amber nuggets.\n\n§7Fossil Cleaning Solvent§r:\nCleans hardened bedrock sediment off fossil fragments.",
                "§l§1Relics of the Past§r\n\n§6Amber Fossil Core§r:\nContains ancient genetic sequences."
            ]
        },
        "items": [
            {"id": "sieve_table", "name": "Archaeological Sieve Table", "category": "items", "max_stack": 64, "icon_type": "table_sieve", "recipe": {"pattern": [" S ", "PBP", " P "], "key": {"S": "minecraft:string", "P": "minecraft:oak_planks", "B": "minecraft:iron_bars"}, "count": 1}},
            {"id": "cleaning_solvent", "name": "Fossil Cleaning Solvent", "category": "items", "max_stack": 16, "icon_type": "solvent_fossil", "recipe": {"pattern": [" S ", " W ", " B "], "key": {"S": "minecraft:sugar", "W": "minecraft:water_bucket", "B": "minecraft:glass_bottle"}, "count": 2}},
            {"id": "amber_core", "name": "Amber Fossil Core", "category": "items", "max_stack": 64, "icon_type": "core_amber", "recipe": {"pattern": [" H ", "HEH", " H "], "key": {"H": "minecraft:honey_block", "E": "minecraft:emerald"}, "count": 1}},
            {"id": "fossil_brush_fine", "name": "Fine Excavation Brush", "category": "equipment", "max_stack": 1, "icon_type": "brush_fine", "recipe": {"pattern": [" F ", " C ", " S "], "key": {"F": "minecraft:feather", "C": "minecraft:copper_ingot", "S": "minecraft:stick"}, "count": 1}},
            {"id": "dino_skull_relic", "name": "Prehistoric Skull Relic", "category": "items", "max_stack": 16, "icon_type": "relic_dino_skull", "recipe": {"pattern": ["BBB", "B B", "BBB"], "key": {"B": "minecraft:bone_block"}, "count": 1}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 39: Wilderness Survival & Thermal Insulation
    # -------------------------------------------------------------
    {
        "id": "thermal_insulation",
        "name": "Wilderness Survival & Thermal Insulation",
        "namespace": "ti",
        "category": "Survival & Thermal",
        "description": "Thermoregulating insulated tunics, chemical heat packs, glacial cooling pouches, and ceramic water purifiers.",
        "colors": ((190, 80, 50, 255), (80, 180, 220, 255)),
        "guidebook": {
            "title": "Extreme Climates Guide",
            "author": "Alpine Scout Nanook",
            "pages": [
                "§l§cThermal Insulation & Survival§r\n\nSurvive sub-zero blizzards in frozen peaks and blistering heatwaves in volcanic basalt deltas.",
                "§l§1Thermal Insulation§r\n\n§cChemical Heat Pack§r:\nKeeps your core temperature warm during freezing blizzard conditions.\n\n§bGlacial Cooling Pouch§r:\nWards against heat exhaustion in blazing Nether landscapes.",
                "§l§1Purification§r\n\n§eCeramic Water Purifier§r:\nFilters swamp and river water into clean potable drinking hydration."
            ]
        },
        "items": [
            {"id": "insulated_tunic", "name": "Thermoregulated Parka", "category": "equipment", "max_stack": 1, "icon_type": "parka_insulated", "recipe": {"pattern": ["L L", "LWL", "LLL"], "key": {"L": "minecraft:leather", "W": "minecraft:white_wool"}, "count": 1}},
            {"id": "heat_pack", "name": "Chemical Heat Pack", "category": "items", "max_stack": 16, "icon_type": "pack_heat", "recipe": {"pattern": [" I ", "CMC", " I "], "key": {"I": "minecraft:iron_nugget", "C": "minecraft:charcoal", "M": "minecraft:magma_cream"}, "count": 2}},
            {"id": "cooling_pouch", "name": "Glacial Cooling Pouch", "category": "items", "max_stack": 16, "icon_type": "pouch_cooling", "recipe": {"pattern": [" S ", "LIL", " S "], "key": {"S": "minecraft:snowball", "L": "minecraft:leather", "I": "minecraft:blue_ice"}, "count": 2}},
            {"id": "water_purifier", "name": "Ceramic Water Purifier", "category": "equipment", "max_stack": 1, "icon_type": "purifier_water", "recipe": {"pattern": [" C ", "SGS", " C "], "key": {"C": "minecraft:clay_ball", "S": "minecraft:sand", "G": "minecraft:glass_bottle"}, "count": 1}},
            {"id": "thermal_lining", "name": "Woolen Thermal Lining", "category": "items", "max_stack": 64, "icon_type": "lining_thermal", "recipe": {"pattern": ["WWW", "SSS", "WWW"], "key": {"W": "minecraft:white_wool", "S": "minecraft:string"}, "count": 2}}
        ]
    },
    # -------------------------------------------------------------
    # Addon 40: Mythological Boss Raids & Primordial Totems
    # -------------------------------------------------------------
    {
        "id": "mythic_raids",
        "name": "Mythological Boss Raids & Primordial Totems",
        "namespace": "mr",
        "category": "Epic Boss Raids",
        "description": "Titan summoning monoliths, primordial seals, demigod battleaxes, and divine champion aegis.",
        "colors": ((140, 20, 40, 255), (255, 215, 60, 255)),
        "guidebook": {
            "title": "Primordial Titan Lore",
            "author": "High Oracle Theodosius",
            "pages": [
                "§l§4Mythological Boss Raids§r\n\nAwaken slumbering ancient world titans through Primordial Monoliths to face legendary challenges for god-tier rewards.",
                "§l§1Summoning Monoliths§r\n\n§4Titan Summoning Monolith§r:\nPlaced at ritual altars to summon primeval demigod raid encounters.\n\n§6Primordial Binding Seal§r:\nGolden rune locking cosmic titan spirits.",
                "§l§1Demigod Armaments§r\n\n§cDemigod Cleaving Battleaxe§r (12 Dmg):\nForged from titan core fragments and netherite ingots.\n\n§eDivine Champion Aegis§r:\nIndestructible shield blessed by ancient deities."
            ]
        },
        "items": [
            {"id": "titan_monolith", "name": "Titan Summoning Monolith", "category": "equipment", "max_stack": 1, "icon_type": "monolith_titan", "recipe": {"pattern": [" N ", "DSD", " N "], "key": {"N": "minecraft:nether_star", "D": "minecraft:diamond_block", "S": "minecraft:crying_obsidian"}, "count": 1}},
            {"id": "demigod_battleaxe", "name": "Demigod Cleaving Battleaxe", "category": "equipment", "max_stack": 1, "damage": 12, "icon_type": "battleaxe_demigod", "recipe": {"pattern": ["NN ", "NS ", " S "], "key": {"N": "minecraft:netherite_ingot", "S": "minecraft:blaze_rod"}, "count": 1}},
            {"id": "divine_aegis", "name": "Divine Champion Aegis", "category": "equipment", "max_stack": 1, "icon_type": "aegis_divine", "recipe": {"pattern": [" G ", "GSG", " N "], "key": {"G": "minecraft:gold_block", "S": "minecraft:shield", "N": "minecraft:nether_star"}, "count": 1}},
            {"id": "primordial_seal", "name": "Primordial Binding Seal", "category": "items", "max_stack": 64, "icon_type": "seal_primordial", "recipe": {"pattern": [" G ", "ENE", " G "], "key": {"G": "minecraft:gold_ingot", "E": "minecraft:echo_shard", "N": "minecraft:nether_star"}, "count": 1}},
            {"id": "titan_core_shard", "name": "Titan Relic Core Shard", "category": "items", "max_stack": 64, "icon_type": "shard_titan", "recipe": {"pattern": [" D ", "DND", " D "], "key": {"D": "minecraft:diamond", "N": "minecraft:netherite_scrap"}, "count": 2}}
        ]
    }
]
