"""
Verification Suite for 40 Minecraft Bedrock Add-ons (1.21.0+).
Validates:
1. Exact count of 40 .mcaddon and 40 .zip archives in dist/
2. Archive structure (BP and RP manifests, pack_icon.png, item_texture.json, texts)
3. JSON syntax and schema requirements for Bedrock 1.21.0+
4. UUID uniqueness across all 40 add-ons (headers and modules - 160 total unique UUIDs)
5. Presence and format of guidebook components and spawn loot tables
6. Texture dimensions (128x128 pack icons, 16x16 item textures)
"""

import json
import os
import uuid
import zipfile
from PIL import Image
import io

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIST_DIR = os.path.join(ROOT_DIR, "dist")

def run_verification():
    print("=" * 60)
    print("RUNNING MINECRAFT BEDROCK 40 ADD-ONS VERIFICATION SUITE")
    print("=" * 60)

    mcaddons = sorted([f for f in os.listdir(DIST_DIR) if f.endswith(".mcaddon")])
    zips = sorted([f for f in os.listdir(DIST_DIR) if f.endswith(".zip")])

    assert len(mcaddons) == 40, f"Expected 40 .mcaddon files, found {len(mcaddons)}"
    assert len(zips) == 40, f"Expected 40 .zip files, found {len(zips)}"
    print(f"✓ Found exactly {len(mcaddons)} .mcaddon and {len(zips)} .zip archives.")

    all_uuids = set()

    for idx, filename in enumerate(mcaddons):
        mcaddon_path = os.path.join(DIST_DIR, filename)
        zip_path = os.path.join(DIST_DIR, zips[idx])

        # Validate .mcaddon
        with zipfile.ZipFile(mcaddon_path, "r") as z:
            names = set(z.namelist())

            # Find manifests
            bp_manifest_p = [n for n in names if n.endswith("_BP/manifest.json")]
            rp_manifest_p = [n for n in names if n.endswith("_RP/manifest.json")]

            assert len(bp_manifest_p) == 1, f"{filename} missing BP manifest"
            assert len(rp_manifest_p) == 1, f"{filename} missing RP manifest"

            # Parse and validate manifests
            bp_man = json.loads(z.read(bp_manifest_p[0]).decode("utf-8"))
            rp_man = json.loads(z.read(rp_manifest_p[0]).decode("utf-8"))

            bp_h_uuid = bp_man["header"]["uuid"]
            bp_m_uuid = bp_man["modules"][0]["uuid"]
            rp_h_uuid = rp_man["header"]["uuid"]
            rp_m_uuid = rp_man["modules"][0]["uuid"]

            for u in [bp_h_uuid, bp_m_uuid, rp_h_uuid, rp_m_uuid]:
                uuid_obj = uuid.UUID(u)
                assert str(uuid_obj) == u.lower()
                assert u not in all_uuids, f"Duplicate UUID detected: {u}"
                all_uuids.add(u)

            # Check min engine version
            assert bp_man["header"]["min_engine_version"] == [1, 21, 0]
            assert rp_man["header"]["min_engine_version"] == [1, 21, 0]

            # Validate pack_icon.png
            bp_icon = [n for n in names if n.endswith("_BP/pack_icon.png")][0]
            rp_icon = [n for n in names if n.endswith("_RP/pack_icon.png")][0]
            icon_img = Image.open(io.BytesIO(z.read(bp_icon)))
            assert icon_img.size == (128, 128), f"Unexpected pack icon size: {icon_img.size}"

            # Validate item texture definitions
            item_tex_p = [n for n in names if n.endswith("textures/item_texture.json")][0]
            item_tex = json.loads(z.read(item_tex_p).decode("utf-8"))
            assert "texture_data" in item_tex
            assert len(item_tex["texture_data"]) >= 5

            # Validate language texts
            lang_p = [n for n in names if n.endswith("texts/en_US.lang")][0]
            lang_txt = z.read(lang_p).decode("utf-8")
            assert "pack.name=" in lang_txt

            # Validate items JSON
            item_jsons = [n for n in names if "/items/" in n and n.endswith(".json")]
            assert len(item_jsons) >= 6, f"Expected at least 6 items (including guidebook), found {len(item_jsons)}"
            for ij in item_jsons:
                item_obj = json.loads(z.read(ij).decode("utf-8"))
                assert "minecraft:item" in item_obj
                desc = item_obj["minecraft:item"]["description"]
                assert "identifier" in desc

            # Validate spawn guidebook loot table & player entity
            loot_p = [n for n in names if "/loot_tables/" in n and n.endswith(".json")][0]
            loot_obj = json.loads(z.read(loot_p).decode("utf-8"))
            assert len(loot_obj["pools"]) >= 1

            player_p = [n for n in names if "/entities/player.json" in n][0]
            player_obj = json.loads(z.read(player_p).decode("utf-8"))
            assert "minecraft:loot" in player_obj["minecraft:entity"]["components"]

            # Validate item textures are 16x16
            tex_pngs = [n for n in names if "/textures/items/" in n and n.endswith(".png")]
            for tp in tex_pngs:
                t_img = Image.open(io.BytesIO(z.read(tp)))
                assert t_img.size == (16, 16), f"Item texture {tp} is not 16x16: {t_img.size}"

        # Validate corresponding .zip contains README.md
        with zipfile.ZipFile(zip_path, "r") as z:
            assert "README.md" in z.namelist(), f"{zip_path} missing README.md"

        print(f"✓ [{idx+1:02d}/40] Verified: {filename} & {zips[idx]}")

    print("=" * 60)
    print(f"ALL 40 ADDONS PASSED VALIDATION! ({len(all_uuids)} Unique UUIDs Verified)")
    print("=" * 60)

if __name__ == "__main__":
    run_verification()
