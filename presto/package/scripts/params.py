#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from resource_management.libraries.script.script import Script

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

node_properties = config['configurations']['node.properties']
jvm_config = config['configurations']['jvm.config']
config_properties = config['configurations']['config.properties']

connectors_to_add = config['configurations']['connectors.properties']['connectors.to.add']
connectors_to_delete = config['configurations']['connectors.properties']['connectors.to.delete']

daemon_control_script = '/etc/init.d/presto'
config_directory = '/etc/presto'

memory_configs = ['query.max-memory-per-node', 'query.max-memory']

host_info = config['clusterHostInfo']

if 'cassandra_node_hosts' in config['clusterHostInfo'] and \
                len(config['clusterHostInfo']['cassandra_node_hosts']) > 0:
    cassandra_node_hosts_arr = config['clusterHostInfo']['cassandra_node_hosts']
    cassandra_node_hosts_arr.sort()
    cassandra_node_hosts_arr_as_string = []
    for cassandra_node_host in cassandra_node_hosts_arr:
        cassandra_node_hosts_arr_as_string.append(format("{cassandra_node_host}"))
    cassandra_hosts = ','.join(cassandra_node_hosts_arr_as_string)

if 'hive_metastore_hosts' in config['clusterHostInfo'] and \
                len(config['clusterHostInfo']['hive_metastore_hosts']) > 0:
    hive_metastore_hosts_arr = config['clusterHostInfo']['hive_metastore_hosts']
    hive_metastore_hosts_arr.sort()
    hive_metastore_hosts_arr_as_string = []
    for hive_metastore_host in hive_metastore_hosts_arr:
        hive_metastore_hosts_arr_as_string.append(format("{hive_metastore_host}"))
    hive_host = hive_metastore_hosts_arr[0]

if 'presto_coordinator_hosts' in config['clusterHostInfo'] and \
                len(config['clusterHostInfo']['presto_coordinator_hosts']) > 0:
    presto_coordinator_hosts = config['clusterHostInfo']['presto_coordinator_hosts']
    presto_coordinator_hosts.sort()
    presto_coordinator_hosts_string = []
    for presto_coordinator_host in presto_coordinator_hosts:
        presto_coordinator_hosts_string.append(format("{presto_coordinator_host}"))
    discovery_uri = presto_coordinator_hosts[0]

host_level_params = config['hostLevelParams']
java_home = host_level_params['java_home']
