"""
Vanilla 16x16 pixel art generator and 128x128 addon pack icon generator.
Uses PIL to produce authentic pixel textures conforming to Minecraft palette styling.
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
    "flame_yellow": (255, 215, 35, 255),
    "flame_orange": (240, 110, 20, 255),
    "ice_cyan": (120, 220, 255, 255),
    "ice_blue": (55, 150, 225, 255),
    "paper_base": (230, 220, 190, 255),
    "paper_dark": (190, 175, 140, 255),
    "crop_green": (80, 175, 45, 255),
    "crop_dark": (45, 115, 25, 255),
    "ender_teal": (20, 115, 110, 255),
    "ender_light": (50, 220, 170, 255),
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

    # 4 corner gold bolts
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

    elif "sword" in t or "blade" in t:
        blade_c = PALETTE["iron_light"]
        edge_c = PALETTE["iron_mid"]
        if "flame" in t: blade_c, edge_c = PALETTE["flame_yellow"], PALETTE["flame_orange"]
        elif "soul" in t: blade_c, edge_c = PALETTE["ice_cyan"], PALETTE["ice_blue"]
        elif "copper" in t: blade_c, edge_c = PALETTE["copper_light"], PALETTE["copper_mid"]
        elif "amethyst" in t: blade_c, edge_c = PALETTE["amethyst_light"], PALETTE["amethyst_mid"]

        for i in range(5, 14):
            px[i, 15 - i] = blade_c
            if i + 1 < 16: px[i + 1, 15 - i] = edge_c
        px[4, 10] = PALETTE["gold_dark"]
        px[5, 11] = PALETTE["gold_mid"]
        px[3, 11] = PALETTE["gold_mid"]
        px[3, 12] = PALETTE["mid_wood"]
        px[2, 13] = PALETTE["mid_wood"]
        px[1, 14] = PALETTE["gold_light"]

    elif "dagger" in t:
        for i in range(5, 11):
            px[i, 15 - i] = PALETTE["ice_cyan"]
            px[i + 1, 15 - i] = PALETTE["ice_blue"]
        px[4, 10] = PALETTE["diamond_mid"]
        px[3, 11] = PALETTE["mid_wood"]
        px[2, 12] = PALETTE["gold_mid"]

    elif "hammer" in t:
        for y in range(2, 6):
            for x in range(8, 14): px[x, y] = PALETTE["iron_mid"]
        for y in range(3, 5):
            for x in range(9, 13): px[x, y] = PALETTE["diamond_light"] if "diamond" in t else PALETTE["iron_light"]
        for i in range(4, 15): px[15 - i, i] = PALETTE["mid_wood"]
        px[1, 14] = PALETTE["stone_dark"]

    elif "shovel" in t:
        for y in range(1, 6):
            for x in range(10, 15): px[x, y] = PALETTE["iron_mid"]
        for i in range(5, 15): px[15 - i, i] = PALETTE["mid_wood"]
        px[1, 14] = PALETTE["iron_light"]

    elif "wand" in t or "scepter" in t:
        gem = PALETTE["amethyst_light"]
        if "fire" in t: gem = PALETTE["flame_orange"]
        elif "ice" in t: gem = PALETTE["ice_cyan"]
        elif "heal" in t or "scepter" in t: gem = PALETTE["emerald_light"]
        for y in range(2, 6):
            for x in range(10, 14): px[x, y] = gem
        px[11, 3] = (255, 255, 255, 255)
        for i in range(5, 15): px[15 - i, i] = PALETTE["gold_mid"] if "scepter" in t else PALETTE["mid_wood"]

    elif "scroll" in t or "contract" in t:
        for y in range(3, 13):
            for x in range(4, 12): px[x, y] = PALETTE["paper_base"]
        seal = PALETTE["ruby_mid"]
        if "blue" in t: seal = PALETTE["diamond_mid"]
        elif "yellow" in t: seal = PALETTE["gold_mid"]
        elif "creeper" in t: seal = PALETTE["emerald_mid"]
        elif "zombie" in t: seal = PALETTE["crop_dark"]
        for x in range(4, 12):
            px[x, 7] = seal
            px[x, 8] = seal
        px[3, 3] = PALETTE["paper_dark"]
        px[12, 12] = PALETTE["paper_dark"]

    elif "backpack" in t or "pouch" in t:
        b = PALETTE["leather_mid"]
        hl = PALETTE["leather_light"]
        if "ender" in t: b, hl = PALETTE["ender_teal"], PALETTE["ender_light"]
        elif "expedition" in t: b, hl = PALETTE["diamond_mid"], PALETTE["diamond_light"]
        for y in range(4, 14):
            for x in range(3, 13): px[x, y] = b
        for y in range(5, 13):
            for x in range(4, 12): px[x, y] = hl
        px[5, 4] = PALETTE["leather_dark"]
        px[10, 4] = PALETTE["leather_dark"]
        px[7, 8] = PALETTE["gold_light"]
        px[8, 8] = PALETTE["gold_light"]

    elif "ring" in t:
        for (x, y) in [(6,5),(7,4),(8,4),(9,5),(10,6),(10,7),(10,8),(9,9),(8,10),(7,10),(6,9),(5,8),(5,7),(5,6)]:
            px[x, y] = PALETTE["gold_mid"]
        g = PALETTE["emerald_light"] if ("green" in t or "vitality" in t) else PALETTE["diamond_light"]
        px[7, 3] = g
        px[8, 3] = (255, 255, 255, 255)

    elif "shield" in t:
        for y in range(2, 13):
            for x in range(3, 13): px[x, y] = PALETTE["mid_wood"]
        m = PALETTE["flame_orange"] if "magma" in t else PALETTE["iron_light"]
        for x in range(3, 13):
            px[x, 2] = m
            px[x, 12] = m
        for y in range(2, 13):
            px[3, y] = m
            px[12, y] = m
        px[7, 7] = PALETTE["gold_light"]
        px[8, 7] = PALETTE["gold_light"]

    elif "crop" in t or "strawberry" in t or "corn" in t or "tomato" in t:
        if "strawberry" in t:
            for y in range(5, 13):
                for x in range(5, 11): px[x, y] = PALETTE["ruby_mid"]
            px[7, 3] = PALETTE["crop_green"]
            px[8, 3] = PALETTE["crop_green"]
            px[7, 4] = PALETTE["crop_dark"]
            px[8, 4] = PALETTE["crop_dark"]
        elif "corn" in t:
            for y in range(3, 13):
                for x in range(6, 10): px[x, y] = PALETTE["gold_mid"]
            px[6, 12] = PALETTE["crop_green"]
            px[9, 12] = PALETTE["crop_green"]
        elif "tomato" in t:
            for y in range(5, 13):
                for x in range(4, 12): px[x, y] = PALETTE["ruby_mid"]
            px[7, 3] = PALETTE["crop_green"]
            px[8, 3] = PALETTE["crop_green"]
            px[6, 6] = PALETTE["ruby_light"]

    elif "bow" in t:
        for (x, y) in [(3,2),(4,3),(4,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(4,11),(4,12),(3,13)]:
            px[x, y] = PALETTE["mid_wood"]
            if "blast" in t: px[x, y] = PALETTE["flame_orange"]
            elif "viper" in t: px[x, y] = PALETTE["crop_dark"]
        for y in range(2, 14): px[12, y] = PALETTE["iron_light"]

    elif "arrow" in t or "harpoon_bolt" in t:
        for i in range(3, 13): px[i, 15 - i] = PALETTE["mid_wood"]
        px[12, 3] = PALETTE["iron_light"]
        px[13, 2] = PALETTE["iron_light"]
        px[3, 12] = PALETTE["iron_mid"]
        px[2, 13] = PALETTE["paper_base"]

    elif "canteen" in t or "flask" in t or "vial" in t or "elixir" in t:
        c = PALETTE["flame_orange"] if "fire" in t else PALETTE["ice_cyan"]
        if "heal" in t: c = PALETTE["ruby_mid"]
        elif "canteen" in t: c = PALETTE["leather_mid"]
        for y in range(6, 14):
            for x in range(5, 11): px[x, y] = c
        px[7, 4] = PALETTE["mid_wood"]
        px[8, 4] = PALETTE["mid_wood"]
        px[7, 5] = PALETTE["iron_light"]
        px[8, 5] = PALETTE["iron_light"]

    elif "furniture" in t or "table" in t or "stool" in t or "shelf" in t or "crate" in t:
        for y in range(4, 13):
            for x in range(4, 12): px[x, y] = PALETTE["mid_wood"]
        for x in range(4, 12): px[x, 4] = PALETTE["light_wood"]
        px[4, 12] = PALETTE["leather_dark"]
        px[11, 12] = PALETTE["leather_dark"]

    elif "lantern" in t:
        for y in range(4, 13):
            for x in range(5, 11): px[x, y] = PALETTE["flame_yellow"] if "brass" in t or "furniture" in t else PALETTE["ice_cyan"]
        for x in range(5, 11):
            px[x, 3] = PALETTE["copper_mid"]
            px[x, 13] = PALETTE["copper_mid"]
        px[7, 2] = PALETTE["iron_light"]
        px[8, 2] = PALETTE["iron_light"]

    else:
        # Relic / Gem / Default
        g = PALETTE["ruby_mid"]
        if "dragon" in t or "void" in t: g = PALETTE["amethyst_mid"]
        elif "wrath" in t or "flame" in t: g = PALETTE["flame_yellow"]
        elif "warp" in t or "water" in t: g = PALETTE["diamond_light"]
        for y in range(4, 12):
            for x in range(4, 12):
                if abs(x - 7.5) + abs(y - 7.5) <= 4: px[x, y] = g
        px[6, 6] = (255, 255, 255, 255)

    return img
