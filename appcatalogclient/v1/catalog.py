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

import requests


class CatalogManager(object):
    """Manager for the catalog."""

    def __init__(self, api_url):
        self.catalog_url = api_url + 'assets'
    
    def list_catalog(self):
        response = requests.get(self.catalog_url)
        return response.json()
    
    def get_app(self, app_name):
        catalog = self.list_catalog()
        for service in catalog['assets']:
            if app_name == service['name']:
                return service
