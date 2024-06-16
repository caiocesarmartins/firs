"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import importlib

import os

currentdir = os.curdir

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

import cargos
import industries
import economies

registered_cargos = cargos.registered_cargos
registered_economies = economies.registered_economies


class IndustryManager(list):
    """
    It's convenient to have a structure for working with industries.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_industry(self, industry_module):
        industry_module.industry.validate()
        self.append(industry_module.industry)

    def get_industry_by_type(self, industry_id):
        # be aware that this shouldn't be called before all industries have been initialised
        for industry in self:
            if industry.id == industry_id:
                return industry
        # if none found, that's an error, don't handle the error, just blow up

    @property
    def incompatible_industries(self):
        # this can't be called until all industries, economies and cargos are registered
        result = {}
        for industry in self:
            incompatible = []
            # special case supplies, pax, mail to exclude them (not useful in checks)
            excluded_cargos = ["ENSP", "FMSP", "PASS", "MAIL"]
            for cargo, prod_industries in industries_producing_cargo().items():
                if cargo not in excluded_cargos:
                    if industry in prod_industries:
                        incompatible.extend(industries_accepting_cargo()[cargo])
            for cargo, accept_industries in industries_accepting_cargo().items():
                # special case supplies, pax, mail to exclude them (not useful in checks)
                if cargo not in excluded_cargos:
                    if industry in accept_industries:
                        incompatible.extend(industries_producing_cargo()[cargo])
            result[industry] = set(incompatible)
        return result


def industries_producing_cargo():
    # !! this is in firs module root temporarily whilst refactoring firs module to use main()
    result = {}
    for cargo in registered_cargos:
        result[cargo.cargo_label] = []

    for industry in industry_manager:
        produced = []
        for economy in registered_economies:
            for cargo_label, ratio in industry.get_prod_cargo_types(economy):
                produced.append(cargo_label)
        for cargo_label in set(produced):
            result[cargo_label].append(industry)

    return result


def industries_accepting_cargo():
    # !! this is in firs module root temporarily whilst refactoring firs module to use main()
    # this can't be called until all industries, economies and cargos are registered
    result = {}
    for cargo in registered_cargos:
        result[cargo.cargo_label] = []

    for industry in industry_manager:
        accepted = []
        for economy in registered_economies:
            for cargo_label in industry.get_accept_cargo_types(economy):
                accepted.append(cargo_label)
        for cargo_label in set(accepted):
            result[cargo_label].append(industry)

    return result


def main():
    # globals *within* this module so they can be accessed externally by other modules using iron_horse.foo
    globals()["industry_manager"] = IndustryManager()

    # industries
    for industry_module_name in industries.industry_module_names:
        industry_module = importlib.import_module(
            "." + industry_module_name, package="industries"
        )
        industry_manager.add_industry(industry_module)

    # guard against mistakes with cargo ids in economies
    known_cargo_ids = [cargo.id for cargo in registered_cargos]
    cargo_label_id_mapping = {
        cargo.cargo_label: cargo.id for cargo in registered_cargos
    }
    for economy in registered_economies:
        for cargo_id in economy.cargo_ids:
            if cargo_id not in known_cargo_ids:
                raise Exception(
                    economy.id
                    + ' economy includes cargo ID "'
                    + cargo_id
                    + '" which does not exist'
                )
        # guard against industries defining accepted / produced cargos that aren't available in the economy
        # - prevents callback failures
        # - prevents possibly incorrect combinatorial production maths
        for industry in industry_manager:
            if industry.economy_variations[economy.id].enabled:
                for cargo_label in industry.get_accept_cargo_types(economy):
                    if cargo_label_id_mapping[cargo_label] not in economy.cargo_ids:
                        utils.echo_message(
                            " ".join(
                                [
                                    "In economy",
                                    economy.id,
                                    "industry",
                                    industry.id,
                                    "accepts",
                                    cargo_label,
                                    "which is not available for that economy",
                                ]
                            )
                        )
                for cargo_label, amount in industry.get_prod_cargo_types(economy):
                    if cargo_label_id_mapping[cargo_label] not in economy.cargo_ids:
                        utils.echo_message(
                            " ".join(
                                [
                                    "In economy",
                                    economy.id,
                                    "industry",
                                    industry.id,
                                    "produces",
                                    cargo_label,
                                    "which is not available for that economy",
                                ]
                            )
                        )
    # guard against unused / wasted industry IDs
    # n.b. sometimes there are valid unused IDs during development
    # note also that tile ID should be cleaned up if removing an industry id
    for (
        industry_id,
        industry_numeric_id,
    ) in global_constants.industry_numeric_ids.items():
        found = False
        for industry in industry_manager:
            if industry_id == industry.id:
                found = True
                break
        if found == False:
            utils.echo_message("Not found: " + industry_id + " from global_constants")

    # guard against (1) too many objects (2) invalid objects
    counter = 0
    for industry in industry_manager:
        for grf_object in industry.objects.values():
            grf_object.validate()
            counter += 1
            if counter > 64000:
                raise BaseException(
                    "Object ID limit exceeded", counter, grf_object.id
                )  # yair, try harder
