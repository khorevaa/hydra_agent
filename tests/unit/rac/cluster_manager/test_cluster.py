# This file is part of HYDRA - cross-platform remote administration
# system for 1C:Enterprise (https://github.com/vbondarevsky/hydra_agent).
# Copyright (C) 2017  Vladimir Bondarevskiy.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.cluster_manager.load_balancing_mode import LoadBalancingMode
from hydra_agent.rac.cluster_manager.security_level import SecurityLevel

raw = ('cluster                       : 73a6a1b2-db40-11e7-049e-000d3a2c0d8b\n'
       'host                          : 1C\n'
       'port                          : 1541\n'
       'name                          : "Локальный кластер"\n'
       'expiration-timeout            : 20\n'
       'lifetime-limit                : 100\n'
       'max-memory-size               : 2500000\n'
       'max-memory-time-limit         : 300\n'
       'security-level                : 2\n'
       'session-fault-tolerance-level : 3\n'
       'load-balancing-mode           : performance\n'
       'errors-count-threshold        : 5\n'
       'kill-problem-processes        : 1\n\n')


def test_create_from_string():
    cluster = Cluster(raw=raw)
    assert cluster.id == '73a6a1b2-db40-11e7-049e-000d3a2c0d8b'
    assert cluster.host == '1C'
    assert cluster.port == 1541
    assert cluster.name == '"Локальный кластер"'
    assert cluster.expiration_timeout == 20
    assert cluster.lifetime_limit == 100
    assert cluster.max_memory_size == 2500000
    assert cluster.max_memory_time_limit == 300
    assert cluster.security_level == SecurityLevel.ProtectedConnectionDuringEntireSession
    assert cluster.session_fault_tolerance_level == 3
    assert cluster.load_balancing_mode == LoadBalancingMode('performance')
    assert cluster.errors_count_threshold == 5
    assert cluster.kill_problem_processes


def test_create_from_id():
    cluster = Cluster(id='73a6a1b2-db40-11e7-049e-000d3a2c0d8b\n')
    assert cluster.id == '73a6a1b2-db40-11e7-049e-000d3a2c0d8b'
