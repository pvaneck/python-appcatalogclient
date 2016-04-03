#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import json
import sys

from cliff import command
from cliff import lister
from cliff import show

from appcatalogclient.v1 import catalog


class ListCatalog(lister.Lister):
    """List full app catalog."""

    def get_parser(self, prog_name):
        parser = super(ListClusterTemplates, self).get_parser(prog_name)

        parser.add_argument(
            '--long',
            action='store_true',
            default=False,
            help='List additional fields in output',
        )
        parser.add_argument(
            '--plugin',
            metavar="<plugin>",
            help="List cluster templates for specific plugin"
        )

        parser.add_argument(
            '--version',
            metavar="<version>",
            help="List cluster templates with specific version of the "
                 "plugin"
        )

        parser.add_argument(
            '--name',
            metavar="<name-substring>",
            help="List cluster templates with specific substring in the "
                 "name"
        )

        return parser

     def take_action(self, parsed_args):
         return 'hello'
