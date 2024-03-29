# Copyright 2015 Matt Taube
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mtaube.apps.common.views import PageView
from mtaube.apps.common.views import PageListView
from mtaube.apps.portfolio.models import Project


class IndexView(PageListView):
    """View used to render portfolio page."""
    model = Project
    template_name = 'page/portfolio/index.html'
    context_object_name = 'projects'


class ProjectView(PageView):
    """View used to render project pages."""
    model = Project
    context_object_name = 'page'
