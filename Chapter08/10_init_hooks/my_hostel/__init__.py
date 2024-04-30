# -*- coding: utf-8 -*-
from . import models
from . import controllers
from . import wizard
from odoo import api, SUPERUSER_ID


def add_room_hook(env):
    room_data1 = {'name': 'Room 1', 'room_no': '01'}
    room_data2 = {'name': 'Room 2', 'room_no': '02'}
    env['hostel.room'].create([room_data1, room_data2])

def pre_init_hook_hostel(env):
    env['ir.model.data'].search([
        ('model', 'like', 'hostel.hostel'),
    ]).unlink()

def uninstall_hook_user(env):
    hostel = env['res.users'].search([])
    hostel.write({'active': False})
