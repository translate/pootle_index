# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from pootle_store.unit.search import UnitSearch
from pootle_store.unit.filters import SearchFilter
from pootle_store.unit.sort import SearchSort
from pootle_store.unit.group import UnitGroups



class HaystackSearchFilter(SearchFilter):

    pass


class HaystackSearchSort(SearchSort):

    pass


class HaystackUnitGroups(UnitGroups):

    pass




class HaystackSearchBackend(UnitSearch):

    filter_class = HaystackSearchFilter
    sort_class = HaystackSearchSort
    group_class = HaystackUnitGroups

    def grouped_search(self):
        return super(
            HaystackSearchBackend, self).grouped_search()
