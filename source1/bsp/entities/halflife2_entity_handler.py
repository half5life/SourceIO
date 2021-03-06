import math

from mathutils import Euler

from .base_entity_handler import BaseEntityHandler
from .halflife2_entity_classes import *


class HalfLifeEntityHandler(BaseEntityHandler):
    entity_lookup_table = entity_class_handle

    def _handle_enity_with_model(self, entity, entity_raw: dict):
        if hasattr(entity, 'model') and entity.model:
            model_path = entity.model
        else:
            model_path = 'error.mdl'
        obj = self._create_empty(self._get_entity_name(entity))
        properties = {'prop_path': model_path,
                      'type': entity.class_name,
                      'scale': self.scale,
                      'entity': entity_raw}
        obj.rotation_euler.rotate(Euler((math.radians(entity.angles[2]),
                                         math.radians(entity.angles[0]),
                                         math.radians(entity.angles[1]))))

        self._set_location_and_scale(obj, parse_float_vector(entity_raw['origin']))
        self._set_entity_data(obj, properties)

        return obj

    def _handle_item(self, entity: Item, entity_raw: dict):
        return self._handle_enity_with_model(entity, entity_raw)

    def _handle_weapon(self, entity: Weapon, entity_raw: dict):
        return self._handle_enity_with_model(entity, entity_raw)

    def _handle_npc(self, entity: BaseNPC, entity_raw: dict):
        return self._handle_enity_with_model(entity, entity_raw)

    def handle_prop_vehicle_airboat(self, entity: prop_vehicle_airboat, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('prop_vehicle_airboat', obj)

    def handle_prop_vehicle_prisoner_pod(self, entity: prop_vehicle_prisoner_pod, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('prop_vehicle_prisoner_pod', obj)

    def handle_prop_vehicle_choreo_generic(self, entity: prop_vehicle_choreo_generic, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('prop_vehicle_choreo_generic', obj)

    def handle_prop_coreball(self, entity: prop_coreball, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('prop_coreball', obj)

    def handle_item_dynamic_resupply(self, entity: item_dynamic_resupply, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_dynamic_resupply', obj)

    def handle_item_ammo_pistol(self, entity: item_ammo_pistol, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_pistol', obj)

    def handle_item_ammo_pistol_large(self, entity: item_ammo_pistol_large, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_pistol', obj)

    def handle_item_ammo_smg1(self, entity: item_ammo_smg1, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_smg1', obj)

    def handle_item_ammo_smg1_large(self, entity: item_ammo_smg1_large, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_smg1', obj)

    def handle_item_ammo_ar2(self, entity: item_ammo_ar2, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_ar2', obj)

    def handle_item_ammo_ar2_large(self, entity: item_ammo_ar2_large, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_ar2', obj)

    def handle_item_ammo_357(self, entity: item_ammo_357, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_357', obj)

    def handle_item_ammo_357_large(self, entity: item_ammo_357_large, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_357', obj)

    def handle_item_ammo_crossbow(self, entity: item_ammo_crossbow, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_crossbow', obj)

    def handle_item_box_buckshot(self, entity: item_box_buckshot, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_box_buckshot', obj)

    def handle_item_rpg_round(self, entity: item_rpg_round, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_rpg_round', obj)

    def handle_item_ammo_smg1_grenade(self, entity: item_ammo_smg1_grenade, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_smg1_grenade', obj)

    def handle_item_battery(self, entity: item_battery, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_battery', obj)

    def handle_item_healthkit(self, entity: item_healthkit, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_healthkit', obj)

    def handle_item_healthvial(self, entity: item_healthvial, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_healthvial', obj)

    def handle_item_ammo_ar2_altfire(self, entity: item_ammo_ar2_altfire, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_ammo_ar2_altfire', obj)

    def handle_item_suit(self, entity: item_suit, entity_raw: dict):
        obj = self._handle_item(entity, entity_raw)
        self._put_into_collection('item_suit', obj)

    def handle_item_ammo_crate(self, entity: item_ammo_crate, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('item_ammo_crate', obj)

    def handle_item_item_crate(self, entity: item_item_crate, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('item_item_crate', obj)

    def handle_item_healthcharger(self, entity: item_healthcharger, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('item_healthcharger', obj)

    def handle_item_suitcharger(self, entity: item_suitcharger, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('item_suitcharger', obj)

    def handle_weapon_crowbar(self, entity: weapon_crowbar, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_crowbar', obj)

    def handle_weapon_stunstick(self, entity: weapon_stunstick, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_stunstick', obj)

    def handle_weapon_pistol(self, entity: weapon_pistol, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_pistol', obj)

    def handle_weapon_ar2(self, entity: weapon_ar2, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_ar2', obj)

    def handle_weapon_rpg(self, entity: weapon_rpg, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_rpg', obj)

    def handle_weapon_smg1(self, entity: weapon_smg1, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_smg1', obj)

    def handle_weapon_357(self, entity: weapon_357, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_357', obj)

    def handle_weapon_crossbow(self, entity: weapon_crossbow, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_crossbow', obj)

    def handle_weapon_shotgun(self, entity: weapon_shotgun, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_shotgun', obj)

    def handle_weapon_frag(self, entity: weapon_frag, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_frag', obj)

    def handle_weapon_physcannon(self, entity: weapon_physcannon, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_physcannon', obj)

    def handle_weapon_bugbait(self, entity: weapon_bugbait, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_bugbait', obj)

    def handle_weapon_alyxgun(self, entity: weapon_alyxgun, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_alyxgun', obj)

    def handle_weapon_annabelle(self, entity: weapon_annabelle, entity_raw: dict):
        obj = self._handle_weapon(entity, entity_raw)
        self._put_into_collection('weapon_annabelle', obj)

    def handle_weapon_striderbuster(self, entity: weapon_striderbuster, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('weapon_striderbuster', obj)

    def handle_npc_blob(self, entity: npc_blob, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_blob', obj)

    def handle_npc_grenade_frag(self, entity: npc_grenade_frag, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_grenade_frag', obj)

    def handle_npc_combine_cannon(self, entity: npc_combine_cannon, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_combine_cannon', obj)

    def handle_npc_combine_camera(self, entity: npc_combine_camera, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_combine_camera', obj)

    def handle_npc_turret_ground(self, entity: npc_turret_ground, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_turret_ground', obj)

    def handle_npc_turret_ceiling(self, entity: npc_turret_ceiling, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('npc_turret_ceiling', obj)

    def handle_npc_turret_floor(self, entity: npc_turret_floor, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('npc_turret_floor', obj)

    def handle_npc_vehicledriver(self, entity: npc_vehicledriver, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_vehicledriver', obj)

    def handle_npc_cranedriver(self, entity: npc_cranedriver, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_cranedriver', obj)

    def handle_npc_apcdriver(self, entity: npc_apcdriver, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_apcdriver', obj)

    def handle_npc_rollermine(self, entity: npc_rollermine, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_rollermine', obj)

    def handle_npc_missiledefense(self, entity: npc_missiledefense, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_missiledefense', obj)

    def handle_npc_sniper(self, entity: npc_sniper, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_sniper', obj)

    def handle_npc_antlion(self, entity: npc_antlion, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_antlion', obj)

    def handle_npc_antlionguard(self, entity: npc_antlionguard, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_antlionguard', obj)

    def handle_npc_crow(self, entity: npc_crow, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_crow', obj)

    def handle_npc_seagull(self, entity: npc_seagull, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_seagull', obj)

    def handle_npc_pigeon(self, entity: npc_pigeon, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_pigeon', obj)

    def handle_npc_ichthyosaur(self, entity: npc_ichthyosaur, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_ichthyosaur', obj)

    def handle_npc_headcrab(self, entity: npc_headcrab, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_headcrab', obj)

    def handle_npc_headcrab_fast(self, entity: npc_headcrab_fast, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_headcrab_fast', obj)

    def handle_npc_headcrab_black(self, entity: npc_headcrab_black, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_headcrab_black', obj)

    def handle_npc_stalker(self, entity: npc_stalker, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_stalker', obj)

    def handle_npc_bullseye(self, entity: npc_bullseye, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_bullseye', obj)

    def handle_npc_fisherman(self, entity: npc_fisherman, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_fisherman', obj)

    def handle_npc_barney(self, entity: npc_barney, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_barney', obj)

    def handle_npc_combine_s(self, entity: npc_combine_s, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_combine_s', obj)

    def handle_npc_launcher(self, entity: npc_launcher, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_launcher', obj)

    def handle_npc_hunter(self, entity: npc_hunter, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_hunter', obj)

    def handle_npc_advisor(self, entity: npc_advisor, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_advisor', obj)

    def handle_npc_vortigaunt(self, entity: npc_vortigaunt, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_vortigaunt', obj)

    def handle_npc_strider(self, entity: npc_strider, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_strider', obj)

    def handle_npc_barnacle(self, entity: npc_barnacle, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_barnacle', obj)

    def handle_npc_combinegunship(self, entity: npc_combinegunship, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_combinegunship', obj)

    def handle_npc_helicopter(self, entity: npc_helicopter, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_helicopter', obj)

    def handle_npc_fastzombie(self, entity: npc_fastzombie, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_fastzombie', obj)

    def handle_npc_fastzombie_torso(self, entity: npc_fastzombie_torso, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_fastzombie_torso', obj)

    def handle_npc_zombie(self, entity: npc_zombie, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_zombie', obj)

    def handle_npc_zombie_torso(self, entity: npc_zombie_torso, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_zombie_torso', obj)

    def handle_npc_zombine(self, entity: npc_zombine, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_zombine', obj)

    def handle_npc_poisonzombie(self, entity: npc_poisonzombie, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_poisonzombie', obj)

    def handle_npc_clawscanner(self, entity: npc_clawscanner, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_clawscanner', obj)

    def handle_npc_manhack(self, entity: npc_manhack, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_manhack', obj)

    def handle_npc_mortarsynth(self, entity: npc_mortarsynth, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_mortarsynth', obj)

    def handle_npc_metropolice(self, entity: npc_metropolice, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_metropolice', obj)

    def handle_npc_crabsynth(self, entity: npc_crabsynth, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_crabsynth', obj)

    def handle_npc_monk(self, entity: npc_monk, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_monk', obj)

    def handle_npc_alyx(self, entity: npc_alyx, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_alyx', obj)

    def handle_npc_kleiner(self, entity: npc_kleiner, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_kleiner', obj)

    def handle_npc_eli(self, entity: npc_eli, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_eli', obj)

    def handle_npc_magnusson(self, entity: npc_magnusson, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_magnusson', obj)

    def handle_npc_breen(self, entity: npc_breen, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_breen', obj)

    def handle_npc_mossman(self, entity: npc_mossman, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_mossman', obj)

    def handle_npc_gman(self, entity: npc_gman, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_gman', obj)

    def handle_npc_dog(self, entity: npc_dog, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_dog', obj)

    def handle_cycler_actor(self, entity: cycler_actor, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('cycler_actor', obj)

    def handle_npc_cscanner(self, entity: npc_cscanner, entity_raw: dict):
        obj = self._handle_npc(entity, entity_raw)
        self._put_into_collection('npc_cscanner', obj)

    def handle_npc_antlion_grub(self, entity: npc_antlion_grub, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('npc_antlion_grub', obj)

    def handle_grenade_helicopter(self, entity: grenade_helicopter, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('grenade_helicopter', obj)

    def handle_combine_mine(self, entity: combine_mine, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('combine_mine', obj)

    def handle_info_target_helicopter_crash(self, entity: info_target_helicopter_crash, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('info_target_helicopter_crash', obj)

    def handle_info_target_gunshipcrash(self, entity: info_target_gunshipcrash, entity_raw: dict):
        obj = self._handle_enity_with_model(entity, entity_raw)
        self._put_into_collection('info_target_gunshipcrash', obj)
