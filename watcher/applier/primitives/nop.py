# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Authors: Jean-Emile DARTOIS <jean-emile.dartois@b-com.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from oslo_log import log


from watcher.applier.primitives import base
from watcher.applier import promise


LOG = log.getLogger(__name__)


class Nop(base.BasePrimitive):

    @promise.Promise
    def execute(self):
        LOG.debug("executing action NOP message:%s ",
                  self.input_parameters.get('message'))
        return True

    @promise.Promise
    def undo(self):
        LOG.debug("undo action NOP")
        return True
