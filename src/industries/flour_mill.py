"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='flour_mill',
                    processed_cargos_and_output_ratios=[('MNSP', 3), ('GRAI', 5), ('MAIZ', 5)],
                    mnsp_boosts_production_jank=True, # this is jank we have to live with
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_random='10',
                    prob_in_game='10',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='48',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(flour_mill_layouts_by_date=True,
                                                           town_distance=(0, 144),
                                                           incompatible={'flour_mill': 56,
                                                                         'arable_farm': 16,
                                                                         'brewery': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_FLOUR_MILL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MILL))',
                    fund_cost_multiplier='50',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_FLOUR_MILL, string(STR_EXTRA_FLOUR_MILL_GRAIN_SUBSTR), string(STR_EXTRA_FLOUR_MILL_EMPTY_SUBSTR)')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].processed_cargos_and_output_ratios = [('MNSP', 3), ('CASS', 5), ('MAIZ', 5)]
industry.economy_variations['MISTAH_KURTZ'].extra_text_industry = 'STR_EXTRA_FLOUR_MILL, string(STR_EXTRA_FLOUR_MILL_CASSAVA_SUBSTR), string(STR_EXTRA_FLOUR_MILL_MAIZE_SUBSTR)'

industry.add_tile(id='flour_mill_tile_1',
                  animation_length=6,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground_bakery = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_bakery',
    type='cobble',
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_3 = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_3',
    sprites = [(150, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_4 = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_4',
    sprites = [(220, 10, 64, 31, -31, 0)]
)
spriteset_1 = industry.add_spriteset(
    id = 'flour_mill_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_2 = industry.add_spriteset(
    id = 'flour_mill_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_3 = industry.add_spriteset(
    id = 'flour_mill_spriteset_3',
    sprites = [(150, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_4 = industry.add_spriteset(
    id = 'flour_mill_spriteset_4',
    sprites = [(220, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
# animated spriteset defined first so others can copy num. frames
spriteset_windmill_anim = industry.add_spriteset(
    id = 'flour_mill_spriteset_windmill_anim',
    sprites = [(10, 200, 64, 82, -31, -52), (80, 200, 64, 82, -31, -52), (150, 200, 64, 82, -31, -52),
               (220, 200, 64, 82, -31, -52), (290, 200, 64, 82, -31, -52), (360, 200, 64, 82, -31, -52)],
    zextent = 24, # optional zextent value, will default to 16 if this param is omitted
    animation_rate = 1
)
spriteset_ground_windmill = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_windmill',
    type = 'empty',
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_windmill = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_windmill',
    sprites = [(150, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_windmill_granary = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_windmill_granary',
    sprites = [(80, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_windmill_granary = industry.add_spriteset(
    id = 'flour_mill_spriteset_windmill_granary',
    sprites = [(80, 60, 64, 82, -31, -52)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_windmill_shed = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_windmill_shed',
    sprites = [(10, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_windmill_shed = industry.add_spriteset(
    id = 'flour_mill_spriteset_windmill_shed',
    sprites = [(10, 60, 64, 82, -31, -52)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_windmill_greeble = industry.add_spriteset(
    id = 'flour_mill_spriteset_ground_overlay_windmill_greeble',
    sprites = [(220, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)

industry.add_spritelayout(
    id = 'flour_mill_spritelayout_brickbakery_1',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_1,
    building_sprites = [],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_brickbakery_2',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_2,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_brickbakery_3',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_3,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_brickbakery_4',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_4,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_windmill_anim',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill,
    building_sprites = [spriteset_windmill_anim],
    fences = ['nw','ne','se','sw'],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_windmill_granary',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill_granary,
    building_sprites = [spriteset_windmill_granary],
    fences = ['nw','ne','se','sw'],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_windmill_shed',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill_shed,
    building_sprites = [spriteset_windmill_shed],
    fences = ['nw','ne','se','sw'],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'flour_mill_spritelayout_windmill_greeble',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill_greeble,
    building_sprites = [],
    fences = ['nw','ne','se','sw'],
    terrain_aware_ground = True
)
industry.add_industry_layout(
    id = 'flour_mill_industry_layout_1',
    layout = [(0, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_3'),
              (0, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_4'),
              (1, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_1'),
              (1, 1, 'flour_mill_tile_1','flour_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'flour_mill_industry_layout_2',
    layout = [(0, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_3'),
              (0, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_4'),
              (1, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_3'),
              (1, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_4'),
              (2, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_1'),
              (2, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'flour_mill_industry_layout_3',
    layout = [(0, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_3'),
              (0, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_4'),
              (0, 2, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_3'),
              (0, 3, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_4'),
              (1, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_1'),
              (1, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_2'),
              (1, 2, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_1'),
              (1, 3, 'flour_mill_tile_1', 'flour_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'flour_mill_industry_layout_4',
    layout = [(0, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_shed'),
              (0, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_granary'),
              (1, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_anim'),
              (1, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_greeble')]
)
industry.add_industry_layout(
    id = 'flour_mill_industry_layout_5',
    layout = [(0, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_shed'),
              (0, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_anim'),
              (1, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_granary'),
              (1, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_greeble')]
)
industry.add_industry_layout(
    id = 'flour_mill_industry_layout_6',
    layout = [(0, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_granary'),
              (0, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_greeble'),
              (1, 0, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_anim'),
              (1, 1, 'flour_mill_tile_1', 'flour_mill_spritelayout_windmill_shed')]
)
