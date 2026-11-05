"""
Extended Vanilla 16x16 pixel art generator and 128x128 addon pack icon generator.
Provides specialized pixel art rendering for all 40 add-ons.
"""

from PIL import Image, ImageDraw

PALETTE = {
    "dark_border": (30, 30, 35, 255),
    "mid_wood": (120, 78, 42, 255),
    "light_wood": (168, 118, 68, 255),
    "leather_mid": (152, 90, 48, 255),
    "leather_light": (198, 130, 80, 255),
    "leather_dark": (94, 52, 25, 255),
    "iron_light": (240, 240, 245, 255),
    "iron_mid": (190, 192, 200, 255),
    "iron_dark": (110, 112, 120, 255),
    "gold_mid": (245, 190, 30, 255),
    "gold_light": (255, 235, 120, 255),
    "gold_dark": (185, 125, 20, 255),
    "diamond_mid": (45, 210, 205, 255),
    "diamond_light": (170, 250, 245, 255),
    "emerald_mid": (20, 185, 80, 255),
    "emerald_light": (110, 245, 150, 255),
    "ruby_mid": (210, 30, 50, 255),
    "ruby_light": (255, 110, 120, 255),
    "amethyst_mid": (150, 80, 210, 255),
    "amethyst_light": (210, 150, 255, 255),
    "copper_mid": (205, 105, 75, 255),
    "copper_light": (240, 150, 120, 255),
    "copper_dark": (150, 70, 50, 255),
    "flame_yellow": (255, 215, 35, 255),
    "flame_orange": (240, 110, 20, 255),
    "flame_red": (200, 40, 25, 255),
    "ice_cyan": (120, 220, 255, 255),
    "ice_blue": (55, 150, 225, 255),
    "paper_base": (230, 220, 190, 255),
    "paper_dark": (190, 175, 140, 255),
    "crop_green": (80, 175, 45, 255),
    "crop_dark": (45, 115, 25, 255),
    "ender_teal": (20, 115, 110, 255),
    "ender_light": (50, 220, 170, 255),
    "sculk_dark": (8, 30, 40, 255),
    "sculk_cyan": (25, 190, 205, 255),
    "netherite_dark": (50, 45, 50, 255),
    "netherite_light": (110, 100, 110, 255),
    "stone_dark": (60, 60, 65, 255),
    "stone_light": (130, 130, 135, 255),
}

def generate_pack_icon(addon_title, primary_col, secondary_col):
    img = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Beveled slate frame
    draw.rectangle([0, 0, 127, 127], fill=(28, 28, 34, 255), outline=(15, 15, 20, 255), width=2)
    draw.rectangle([6, 6, 121, 121], fill=(42, 44, 54, 255), outline=(72, 76, 92, 255), width=3)
    draw.line([(8, 8), (119, 8)], fill=(90, 95, 115, 255), width=2)
    draw.line([(8, 8), (8, 119)], fill=(90, 95, 115, 255), width=2)

    # Addon insignia emblem
    c = (64, 64)
    r = 38
    draw.polygon([(c[0], c[1]-r), (c[0]+r, c[1]), (c[0], c[1]+r), (c[0]-r, c[1])], fill=primary_col, outline=secondary_col, width=3)
    r_in = 18
    draw.polygon([(c[0], c[1]-r_in), (c[0]+r_in, c[1]), (c[0], c[1]+r_in), (c[0]-r_in, c[1])], fill=(255, 255, 255, 220), outline=secondary_col, width=2)

    # 4 corner gold/steel bolts
    for bx, by in [(14, 14), (113, 14), (14, 113), (113, 113)]:
        draw.rectangle([bx-3, by-3, bx+3, by+3], fill=secondary_col, outline=(20, 20, 20, 255))

    return img

def generate_item_texture(icon_type):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    px = img.load()
    t = icon_type.lower()

    if "guidebook" in t or "book" in t:
        for y in range(2, 14):
            for x in range(3, 13): px[x, y] = PALETTE["leather_mid"]
        for y in range(3, 13):
            for x in range(4, 12): px[x, y] = PALETTE["leather_light"]
        for y in range(2, 14):
            px[3, y] = PALETTE["leather_dark"]
            px[12, y] = PALETTE["leather_dark"]
        px[3, 2] = PALETTE["gold_mid"]
        px[3, 13] = PALETTE["gold_mid"]
        px[7, 6] = PALETTE["gold_light"]
        px[8, 6] = PALETTE["gold_light"]
        px[7, 7] = PALETTE["gold_mid"]
        px[8, 7] = PALETTE["gold_mid"]

    elif "wrench" in t:
        for y in range(2, 7):
            for x in range(8, 14): px[x, y] = PALETTE["iron_light"]
        px[10, 4] = (0, 0, 0, 0)
        px[11, 4] = (0, 0, 0, 0)
        for i in range(5, 14): px[15 - i, i] = PALETTE["copper_mid"]

    elif "boiler" in t or "macerator" in t or "oven" in t or "mill" in t:
        for y in range(3, 13):
            for x in range(3, 13): px[x, y] = PALETTE["copper_mid"] if "boiler" in t else PALETTE["iron_mid"]
        for x in range(4, 12):
            px[x, 4] = PALETTE["iron_light"]
            px[x, 11] = PALETTE["iron_dark"]
        px[7, 8] = PALETTE["flame_orange"]
        px[8, 8] = PALETTE["flame_yellow"]

    elif "conveyor" in t or "pipe" in t:
        for y in range(5, 11):
            for x in range(2, 14): px[x, y] = PALETTE["iron_dark"]
        for x in range(3, 13, 3):
            for y in range(6, 10): px[x, y] = PALETTE["gold_mid"]

    elif "chisel" in t:
        for i in range(4, 12): px[i, 15 - i] = PALETTE["iron_light"]
        px[12, 3] = PALETTE["diamond_light"]
        px[13, 2] = PALETTE["diamond_mid"]
        px[3, 12] = PALETTE["mid_wood"]
        px[2, 13] = PALETTE["leather_dark"]

    elif "altar" in t or "monolith" in t:
        for y in range(5, 14):
            for x in range(4, 12): px[x, y] = PALETTE["stone_dark"]
        for x in range(3, 13): px[x, 5] = PALETTE["amethyst_mid"]
        px[7, 4] = PALETTE["diamond_light"]
        px[8, 4] = PALETTE["diamond_light"]

    elif "glyph" in t or "runestone" in t or "seal" in t:
        for y in range(3, 13):
            for x in range(3, 13):
                if abs(x - 7.5) + abs(y - 7.5) <= 5: px[x, y] = PALETTE["stone_light"]
        px[7, 6] = PALETTE["gold_mid"]
        px[8, 6] = PALETTE["gold_mid"]
        px[7, 7] = PALETTE["gold_light"]
        px[8, 7] = PALETTE["gold_light"]

    elif "chassis" in t or "exoskeleton" in t or "aegis" in t or "shield" in t:
        for y in range(3, 13):
            for x in range(3, 13): px[x, y] = PALETTE["iron_light"]
        for y in range(4, 12):
            for x in range(4, 12): px[x, y] = PALETTE["diamond_mid"] if "barrier" in t or "aegis" in t else PALETTE["iron_dark"]
        px[7, 7] = PALETTE["gold_light"]
        px[8, 7] = PALETTE["gold_light"]

    elif "staff" in t or "baton" in t:
        for i in range(4, 14): px[15 - i, i] = PALETTE["mid_wood"]
        gem = PALETTE["sculk_cyan"] if "sonic" in t else PALETTE["ruby_mid"]
        if "bone" in t: gem = PALETTE["paper_base"]
        for y in range(2, 6):
            for x in range(10, 14): px[x, y] = gem
        px[11, 3] = (255, 255, 255, 255)

    elif "cannon" in t or "barrel" in t or "bolt" in t:
        for y in range(6, 10):
            for x in range(2, 14): px[x, y] = PALETTE["netherite_dark"]
        px[13, 7] = PALETTE["iron_light"]
        px[13, 8] = PALETTE["iron_light"]

    elif "sword" in t or "blade" in t or "battleaxe" in t:
        blade_c = PALETTE["iron_light"]
        edge_c = PALETTE["iron_mid"]
        if "flame" in t: blade_c, edge_c = PALETTE["flame_yellow"], PALETTE["flame_orange"]
        elif "soul" in t: blade_c, edge_c = PALETTE["ice_cyan"], PALETTE["ice_blue"]
        elif "copper" in t: blade_c, edge_c = PALETTE["copper_light"], PALETTE["copper_mid"]
        elif "amethyst" in t: blade_c, edge_c = PALETTE["amethyst_light"], PALETTE["amethyst_mid"]
        elif "demigod" in t or "ruby" in t: blade_c, edge_c = PALETTE["ruby_mid"], PALETTE["gold_mid"]

        for i in range(5, 14):
            px[i, 15 - i] = blade_c
            if i + 1 < 16: px[i + 1, 15 - i] = edge_c
        px[4, 10] = PALETTE["gold_dark"]
        px[5, 11] = PALETTE["gold_mid"]
        px[3, 11] = PALETTE["gold_mid"]
        px[3, 12] = PALETTE["mid_wood"]
        px[2, 13] = PALETTE["mid_wood"]
        px[1, 14] = PALETTE["gold_light"]

    elif "cell" in t or "capacitor" in t or "accumulator" in t or "radar" in t:
        for y in range(4, 12):
            for x in range(4, 12): px[x, y] = PALETTE["iron_dark"]
        for y in range(5, 11):
            for x in range(5, 11): px[x, y] = PALETTE["flame_yellow"] if "accumulator" in t else PALETTE["ice_cyan"]
        px[7, 3] = PALETTE["copper_light"]
        px[8, 3] = PALETTE["copper_light"]

    elif "whistle" in t or "horn" in t:
        for y in range(6, 11):
            for x in range(4, 12): px[x, y] = PALETTE["copper_light"] if "horn" in t else PALETTE["gold_mid"]
        px[3, 7] = PALETTE["iron_light"]
        px[3, 8] = PALETTE["iron_light"]

    elif "serum" in t or "vial" in t or "purifier" in t:
        for y in range(6, 14):
            for x in range(5, 11): px[x, y] = PALETTE["crop_green"] if "serum" in t else PALETTE["ice_cyan"]
        px[7, 4] = PALETTE["mid_wood"]
        px[8, 4] = PALETTE["mid_wood"]
        px[7, 5] = PALETTE["iron_light"]
        px[8, 5] = PALETTE["iron_light"]

    elif "bow" in t or "frame" in t:
        for (x, y) in [(3,2),(4,3),(4,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(4,11),(4,12),(3,13)]:
            px[x, y] = PALETTE["netherite_light"] if "compound" in t else PALETTE["mid_wood"]
        for y in range(2, 14): px[12, y] = PALETTE["iron_light"]

    else:
        # Default high-detail crystal / relic
        g = PALETTE["gold_mid"]
        if "crystal" in t or "shard" in t: g = PALETTE["diamond_light"]
        elif "amber" in t: g = PALETTE["flame_yellow"]
        elif "sculk" in t: g = PALETTE["sculk_cyan"]
        for y in range(4, 12):
            for x in range(4, 12):
                if abs(x - 7.5) + abs(y - 7.5) <= 4: px[x, y] = g
        px[6, 6] = (255, 255, 255, 255)

    return img
