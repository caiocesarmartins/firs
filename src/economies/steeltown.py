from economy import Economy

economy = Economy(
    id="STEELTOWN",
    numeric_id=5,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "acid",
        "mail",
        "alloy_steel",
        "aluminium",
        "vehicles",  # no goods?
        "carbon_black",
        "carbon_steel",
        "cast_iron",
        "cement",
        "chlorine",
        "food",
        "cleaning_agents",
        "coal",
        "coal_tar",
        "coke",
        "electrical_parts",
        "engineering_supplies",
        "farm_supplies",
        "ferrochrome",
        "glass",
        "iron_ore",
        "limestone",
        "lye",
        "manganese",
        "oxygen",
        "paints_and_coatings",
        "pig_iron",
        "pipe",
        "plastics",
        "quicklime",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "slag",
        "soda_ash",
        "stainless_steel",
        "steel_sections",
        "steel_sheet",
        "steel_wire_rod",
        "sulphur",
        "tyres",
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "zinc",
        # these were added to test, and need alphabetised, but that breaks my savegame
        "potash",
        "nitrogen",
        "pipework",
        "steel_merchant_bar",
        "forgings_and_castings",
        "hardware",
        "rebar",
        "lifting_equipment",
        "tube",
        "stone",
        "steel_wire_rope",
        "pumps_and_valves",
        "cranes_and_hoists",
        "concrete_products",
        "tyre_cord",
        "welding_supplies",
    ],
    cargoflow_graph_tuning={
        "wormhole_industries": ["wharf", "bulk_terminal", "builders_yard", "vehicle_distributor", "hardware_store", "general_store"],
        "cargos_with_individual_accept_nodes": [
            "sand",
            "acid",
            "carbon_steel",
            "stainless_steel",
            "alloy_steel",
            "limestone",
        ],
        "group_edges_subgraphs": [
            ["basic_oxygen_furnace", "electric_arc_furnace"],
            ["pig_iron"],  # groups edges can be set for a single node
        ],
        "ranking_subgraphs": [
            ("source", ["quarry", "coal_mine", "iron_ore_mine"]),
            ("same", ["lime_kiln", "glass_works"]),
            ("same", ["engine_plant", "tyre_plant", "body_plant"]),
            ("same", ["oxygen", "coke", "iron_ore"]),
            ("sink", ["farm", "food", "cranes_and_hoists", "vehicles", "pipework", "hardware", "assembly_plant", "pipework_fabricator", "machine_shop"]),
        ],
        "clusters": [
            {
                "nodes": ["blast_furnace", "pig_iron", "basic_oxygen_furnace"],
                "rank": "same",
            },
            {
                "nodes": ["scrap_yard", "scrap_metal", "electric_arc_furnace"],
                "rank": "same",
            },
            {
                "nodes": ["coke", "iron_ore"],
                "rank": "same",
                "color": "white",
            },
            {"nodes": ["coal", "coal_mine", "coke_oven"], "rank": "same"},
            {
                "nodes": ["sulphur", "rubber", "carbon_black"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["glass", "paints_and_coatings"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["concrete_plant", "concrete_products"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": [
                    "vehicle_parts",
                    "vehicle_bodies",
                    "vehicle_engines",
                    "tyres",
                ],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["steel_wire_rope", "lifting_equipment"],
                "rank": "same",
                "color": "white",
            },
        ],
    },
)
