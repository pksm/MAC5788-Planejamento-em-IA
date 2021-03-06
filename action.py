# This file is part of pypddl-parser.

# pypddl-parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pypddl-parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pypddl-parser.  If not, see <http://www.gnu.org/licenses/>.


class Action(object):

    def __init__(self, name, params, precond, effects, pos_effect=[], neg_effect=[]):
        self._name    = name
        self._params  = params
        self._precond = precond
        self._effects = effects
        self._pos_effect = pos_effect
        self._neg_effect = neg_effect

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params[:]

    @property
    def precond(self):
        return self._precond[:]

    @property
    def effects(self):
        return self._effects[:]
    @property
    def pos_effect(self):
        ''' Return a list of positive effect atoms represented as strings. '''
        return self._pos_effect.copy()

    @property
    def neg_effect(self):
        ''' Return a list of negative effect atoms represented as strings. '''
        return self._neg_effect.copy()

    def __str__(self):
        # operator_str  = '{0}({1})\n'.format(self._name, ', '.join(map(str, self._params)))
        operator_str  = '{0}({1})\n'.format(self._name, ', '.join(map(str, self._params)))
        operator_str += '>> precond: {0}\n'.format(', '.join(map(str, self._precond)))
        operator_str += '>> effects: {0}\n'.format(', '.join(map(str, self._effects)))
        operator_str += '>> eff+: {0}\n'.format(', '.join(sorted(self._pos_effect)))
        operator_str += '>> eff-: {0}\n'.format(', '.join(sorted(self._neg_effect)))
        return operator_str
