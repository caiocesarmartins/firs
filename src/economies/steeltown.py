from economy import Economy

economy = Economy(
    id="STEELTOWN",
    numeric_id=5,
    cargos=[
        "acid",
        "aggregates",
        "aluminium",
        "carbon_black",
        "cast_iron",
        "cement",
        "food",
        "chlorine",
        "cleaning_agents",
        "coal",
        "coal_tar",
        "coke",
        "concrete_products",
        "electrical_parts",
        "engineering_supplies",
        "farm_supplies",
        "ferroalloys",
        "forgings_and_castings",
        "glass",
        "goods",
        "hardware",
        "iron_ore",
        "limestone",
        "lye",
        "mail",
        "nitrogen",
        "oxygen",
        "paints_and_coatings",
        "passengers",
        "pig_iron",
        "potash",
        "pipework",
        "pumps_and_valves",
        "quicklime",
        "rebar",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "seals_belts_and_hoses",
        "slag",
        "soda_ash",
        "steel_billets_and_blooms",
        "steel_ingots",
        "steel_merchant_bar",
        "steel_pipe",
        "steel_sections",
        "steel_sheet",
        "steel_slab",
        "steel_tube",
        "steel_wire_rod",
        "sulphur",
        "tyre_cord",
        "tyres",
        "vehicles",
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "welding_consumables",
        "zinc",
    ],
    cargoflow_graph_tuning={
        # also any industries with !!!!??????? will be automatically added to wormhole_industries
        "wormhole_industries": [
            "wharf",
            "port",
            "metal_fabricator",
            "appliance_factory",
        ],
        "cargos_with_individual_produce_nodes": [
            "steel_ingots",
            "steel_slab",
            "steel_billets_and_blooms",
            "slag",
        ],
        "cargos_with_individual_accept_nodes": [
            "sand",
            "acid",
            "limestone",
            "paints_and_coatings",
            "cleaning_agents",
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
            (
                "sink",
                [
                    "food",
                    "farm",
                    "hardware",
                    "goods",
                    "vehicles",
                    "pipework",
                    "assembly_plant",
                    "tracked_machine_factory",
                    "pipework_fabricator",
                ],
            ),
        ],
        "clusters": [
            {
                "nodes": [
                    "metal_fabricator",
                    "precision_parts_plant",
                    "appliance_factory",
                ],
                "rank": "same",
                "color": "white",
            },
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
                "nodes": ["cement", "rebar"],
                "rank": "same",
                "color": "white",
            },
        ],
    },
)

# some deliberate overlapping of biomes for mixing at boundaries
economy.add_biome(
    "exclude_map_edges",
    min_x_percent=25,
    max_x_percent=75,
    min_y_percent=25,
    max_y_percent=75,
)
