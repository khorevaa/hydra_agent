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


from typing import Dict

from hydra_agent import Rac
from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.infobase_manager.infobase import InfoBase


class InfoBaseManager(Rac):
    def __init__(self, config: Dict, cluster: Cluster):
        super().__init__(config)
        self.cluster = cluster

    def list(self):
        """Returns list of `InfoBase`"""

        result = []
        for ib_info in self._run_command(['infobase', 'summary', 'list']).split('\n\n'):
            if ib_info.strip():
                result.append(InfoBase(ib_info))
        return result

    def _run_command(self, args):
        args.append(f'--cluster={self.cluster.id}')
        return super()._run_command(args)
