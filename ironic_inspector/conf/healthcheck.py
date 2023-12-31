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

from oslo_config import cfg

from ironic_inspector.common.i18n import _

_OPTS = [
    cfg.BoolOpt('enabled',
                default=False,
                help=_('Enable the health check endpoint at /healthcheck. '
                       'Note that this is unauthenticated. More information '
                       'is available at '
                       'https://docs.openstack.org/oslo.middleware/latest/'
                       'reference/healthcheck_plugins.html.')),
]


def register_opts(conf):
    conf.register_opts(_OPTS, group='healthcheck')


def list_opts():
    return _OPTS
