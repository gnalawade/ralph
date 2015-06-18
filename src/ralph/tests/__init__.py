# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ralph.admin.sites import RalphAdminSite
from ralph.tests.base import RalphTestCase

ralph_test_site = RalphAdminSite(name='ralph_test_site')

__all__ = ['RalphTestCase']
