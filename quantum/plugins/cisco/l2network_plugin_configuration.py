"""
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2011 Cisco Systems, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Sumit Naiksatam, Cisco Systems, Inc.
# @author: Rohit Agarwalla, Cisco Systems, Inc.
"""

import os

from quantum.plugins.cisco.common import cisco_configparser as confp

CONF_FILE = "conf/l2network_plugin.ini"

CONF_PARSER_OBJ = confp.\
CiscoConfigParser(os.path.dirname(os.path.realpath(__file__)) + \
"/" + CONF_FILE)

SECTION_CONF = CONF_PARSER_OBJ['VLANS']
VLAN_NAME_PREFIX = SECTION_CONF['vlan_name_prefix']
VLAN_START = SECTION_CONF['vlan_start']
VLAN_END = SECTION_CONF['vlan_end']

SECTION_CONF = CONF_PARSER_OBJ['PORTS']
MAX_PORTS = SECTION_CONF['max_ports']

SECTION_CONF = CONF_PARSER_OBJ['PORTPROFILES']
MAX_PORT_PROFILES = SECTION_CONF['max_port_profiles']

SECTION_CONF = CONF_PARSER_OBJ['NETWORKS']
MAX_NETWORKS = SECTION_CONF['max_networks']

SECTION_CONF = CONF_PARSER_OBJ['MODEL']
MODEL_CLASS = SECTION_CONF['model_class']

SECTION_CONF = CONF_PARSER_OBJ['SEGMENTATION']
MANAGER_CLASS = SECTION_CONF['manager_class']

CONF_FILE = "conf/plugins.ini"

CONF_PARSER_OBJ = confp.\
CiscoConfigParser(os.path.dirname(os.path.realpath(__file__)) + \
"/" + CONF_FILE)

PLUGINS = CONF_PARSER_OBJ.walk(CONF_PARSER_OBJ.dummy)

CONF_FILE = "conf/db_conn.ini"

CONF_PARSER_OBJ = confp.\
CiscoConfigParser(os.path.dirname(os.path.realpath(__file__)) + \
"/" + CONF_FILE)

SECTION_CONF = CONF_PARSER_OBJ['DATABASE']
DB_NAME = SECTION_CONF['name']
DB_USER = SECTION_CONF['user']
DB_PASS = SECTION_CONF['pass']
DB_HOST = SECTION_CONF['host']
