"""
Core Add-on Generator & Packager for all 40 Minecraft Bedrock Add-ons (1.21.0+).
Builds both .mcaddon and .zip archives in dist/
"""

import json
import os
import uuid
import zipfile
import io
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from addons_registry import ADDONS
from addons_registry_complex import COMPLEX_ADDONS
from texture_art import generate_item_texture, generate_pack_icon

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIST_DIR = os.path.join(ROOT_DIR, "dist")

ALL_40_ADDONS = ADDONS + COMPLEX_ADDONS

def build_addon(addon, index):
    addon_id = addon["id"]
    addon_name = addon["name"]
    ns = addon["namespace"]
    desc = addon["description"]
    guidebook = addon["guidebook"]
    items = addon["items"]
    primary_col, secondary_col = addon["colors"]

    prefix = f"{index+1:02d}"

    # Manifest UUIDs
    bp_header_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{addon_id}.bp.header.v1"))
    bp_module_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{addon_id}.bp.module.v1"))
    rp_header_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{addon_id}.rp.header.v1"))
    rp_module_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{addon_id}.rp.module.v1"))

    bp_folder_name = f"{addon_id}_BP"
    rp_folder_name = f"{addon_id}_RP"

    # Behavior Pack Manifest
    bp_manifest = {
        "format_version": 2,
        "header": {
            "name": f"{addon_name} (BP)",
            "description": f"{desc} [Behavior Pack]",
            "uuid": bp_header_uuid,
            "version": [1, 0, 0],
            "min_engine_version": [1, 21, 0]
        },
        "modules": [{"type": "data", "uuid": bp_module_uuid, "version": [1, 0, 0]}],
        "dependencies": [{"uuid": rp_header_uuid, "version": [1, 0, 0]}]
    }

    # Resource Pack Manifest
    rp_manifest = {
        "format_version": 2,
        "header": {
            "name": f"{addon_name} (RP)",
            "description": f"{desc} [Resource Pack]",
            "uuid": rp_header_uuid,
            "version": [1, 0, 0],
            "min_engine_version": [1, 21, 0]
        },
        "modules": [{"type": "resources", "uuid": rp_module_uuid, "version": [1, 0, 0]}]
    }

    # Pack Icon
    pack_icon = generate_pack_icon(addon_name, primary_col, secondary_col)
    pack_icon_bytes = io.BytesIO()
    pack_icon.save(pack_icon_bytes, format="PNG")
    pack_icon_raw = pack_icon_bytes.getvalue()

    files_map = {}
    files_map[f"{bp_folder_name}/manifest.json"] = json.dumps(bp_manifest, indent=2).encode("utf-8")
    files_map[f"{bp_folder_name}/pack_icon.png"] = pack_icon_raw
    files_map[f"{rp_folder_name}/manifest.json"] = json.dumps(rp_manifest, indent=2).encode("utf-8")
    files_map[f"{rp_folder_name}/pack_icon.png"] = pack_icon_raw

    guide_id = f"{ns}_guidebook"
    guide_full_id = f"{ns}:{guide_id}"

    all_items = [{
        "id": guide_id,
        "name": guidebook["title"],
        "category": "equipment",
        "max_stack": 1,
        "icon_type": "guidebook",
        "is_guidebook": True
    }] + items

    texture_data = {}
    lang_lines = [
        f"pack.name={addon_name}",
        f"pack.description={desc}",
        f"item.{guide_full_id}.name={guidebook['title']}"
    ]

    for itm in all_items:
        i_id = itm["id"]
        i_full_id = f"{ns}:{i_id}"
        i_name = itm["name"]
        i_cat = itm.get("category", "items")
        i_stack = itm.get("max_stack", 64)
        i_damage = itm.get("damage")
        i_food = itm.get("food")
        icon_type = itm.get("icon_type", i_id)

        # Texture
        tex_img = generate_item_texture(icon_type)
        t_bytes = io.BytesIO()
        tex_img.save(t_bytes, format="PNG")
        files_map[f"{rp_folder_name}/textures/items/{i_id}.png"] = t_bytes.getvalue()

        texture_data[f"{ns}_{i_id}"] = {"textures": f"textures/items/{i_id}"}
        lang_lines.append(f"item.{i_full_id}.name={i_name}")

        # Item JSON
        components = {
            "minecraft:icon": {"textures": {"default": f"{ns}_{i_id}"}},
            "minecraft:display_name": {"value": i_name},
            "minecraft:max_stack_size": i_stack,
            "minecraft:hand_equipped": (i_damage is not None or "staff" in icon_type or "wand" in icon_type or "hammer" in icon_type or "sword" in icon_type or "wrench" in icon_type or "chisel" in icon_type)
        }
        if i_damage: components["minecraft:damage"] = i_damage
        if i_food:
            components["minecraft:food"] = {
                "nutrition": i_food.get("nutrition", 4),
                "saturation_modifier": i_food.get("saturation_modifier", "normal"),
                "can_always_eat": i_food.get("can_always_eat", False)
            }
            components["minecraft:use_animation"] = "eat"
            components["minecraft:use_modifiers"] = {"use_duration": 1.6, "movement_modifier": 0.35}

        item_def = {
            "format_version": "1.21.0",
            "minecraft:item": {
                "description": {
                    "identifier": i_full_id,
                    "menu_category": {"category": i_cat if i_cat in ["equipment", "items", "nature"] else "items"}
                },
                "components": components
            }
        }
        files_map[f"{bp_folder_name}/items/{i_id}.json"] = json.dumps(item_def, indent=2).encode("utf-8")

        # Recipe
        if "recipe" in itm:
            rec = itm["recipe"]
            recipe_def = {
                "format_version": "1.21.0",
                "minecraft:recipe_shaped": {
                    "description": {"identifier": f"{ns}:{i_id}_recipe"},
                    "tags": ["crafting_table"],
                    "pattern": rec["pattern"],
                    "key": {k: {"item": v} for k, v in rec["key"].items()},
                    "result": {"item": i_full_id, "count": rec.get("count", 1)}
                }
            }
            files_map[f"{bp_folder_name}/recipes/{i_id}_recipe.json"] = json.dumps(recipe_def, indent=2).encode("utf-8")

    # Guidebook recipe: Book + Paper
    guide_recipe = {
        "format_version": "1.21.0",
        "minecraft:recipe_shapeless": {
            "description": {"identifier": f"{ns}:{guide_id}_recipe"},
            "tags": ["crafting_table"],
            "ingredients": [{"item": "minecraft:book"}, {"item": "minecraft:paper"}],
            "result": {"item": guide_full_id, "count": 1}
        }
    }
    files_map[f"{bp_folder_name}/recipes/{guide_id}_recipe.json"] = json.dumps(guide_recipe, indent=2).encode("utf-8")

    # Player spawn guidebook loot table & entity component
    loot_table_def = {
        "pools": [
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "item",
                        "name": "minecraft:written_book",
                        "weight": 1,
                        "functions": [
                            {
                                "function": "set_book_contents",
                                "title": guidebook["title"],
                                "author": guidebook["author"],
                                "pages": guidebook["pages"]
                            }
                        ]
                    },
                    {
                        "type": "item",
                        "name": guide_full_id,
                        "weight": 1
                    }
                ]
            }
        ]
    }
    files_map[f"{bp_folder_name}/loot_tables/{addon_id}_spawn_guide.json"] = json.dumps(loot_table_def, indent=2).encode("utf-8")

    player_entity = {
        "format_version": "1.21.0",
        "minecraft:entity": {
            "description": {"identifier": "minecraft:player", "is_spawnable": False, "is_summonable": False, "is_experimental": False},
            "component_groups": {
                f"{ns}:spawn_kit": {
                    "minecraft:spawn_entity": {
                        "entities": [{"min_wait_time": 0, "max_wait_time": 0, "spawn_entity": "minecraft:item", "single_use": True, "filters": {"test": "is_alive", "value": True}}]
                    }
                }
            },
            "components": {
                "minecraft:type_family": {"family": ["player"]},
                "minecraft:loot": {"table": f"loot_tables/{addon_id}_spawn_guide.json"}
            },
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": [f"{ns}:spawn_kit"]}}
            }
        }
    }
    files_map[f"{bp_folder_name}/entities/player.json"] = json.dumps(player_entity, indent=2).encode("utf-8")

    # Resource Pack texture definitions and language
    item_texture_json = {
        "resource_pack_name": f"{addon_id}_rp",
        "texture_name": "atlas.items",
        "texture_data": texture_data
    }
    files_map[f"{rp_folder_name}/textures/item_texture.json"] = json.dumps(item_texture_json, indent=2).encode("utf-8")
    files_map[f"{rp_folder_name}/texts/en_US.lang"] = ("\n".join(lang_lines) + "\n").encode("utf-8")
    files_map[f"{rp_folder_name}/texts/languages.json"] = json.dumps(["en_US"], indent=2).encode("utf-8")

    # Addon README
    addon_readme = f"""# {addon_name}
> Minecraft Bedrock Edition (1.21.0+) Add-on

{desc}

## In-Game Guide Book
- **Title**: {guidebook['title']}
- **Author**: {guidebook['author']}
- **Spawn Behavior**: Players receive this guidebook automatically upon joining the world, and can recraft it anytime using Book + Paper.

### Guidebook Pages
{chr(10).join(f"**Page {i+1}:** {p}" for i, p in enumerate(guidebook['pages']))}

## Items & Equipment
| Item Name | Identifier | Max Stack | Crafting Recipe |
| :--- | :--- | :--- | :--- |
| **{guidebook['title']}** | `{guide_full_id}` | 1 | Shapeless: Book + Paper |
"""
    for itm in items:
        rec = itm.get("recipe", {})
        pattern_str = " / ".join(rec.get("pattern", ["-"])) if rec else "None"
        addon_readme += f"| **{itm['name']}** | `{ns}:{itm['id']}` | {itm.get('max_stack', 64)} | Pattern: `{pattern_str}` |\n"

    files_map["README.md"] = addon_readme.encode("utf-8")

    # Export archives into dist/
    os.makedirs(DIST_DIR, exist_ok=True)
    mcaddon_file = os.path.join(DIST_DIR, f"{prefix}_{addon_id}.mcaddon")
    zip_file = os.path.join(DIST_DIR, f"{prefix}_{addon_id}.zip")

    with zipfile.ZipFile(mcaddon_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for path_key, content in files_map.items():
            if path_key != "README.md":
                zf.writestr(path_key, content)

    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for path_key, content in files_map.items():
            zf.writestr(path_key, content)

    print(f"[{prefix}/40] Packaged: {addon_name}")

def main():
    print(f"Starting build for all {len(ALL_40_ADDONS)} Minecraft Bedrock Add-ons...")
    for idx, addon in enumerate(ALL_40_ADDONS):
        build_addon(addon, idx)
    print("Done! All 40 add-ons built and packaged into dist/.")

if __name__ == "__main__":
    main()
