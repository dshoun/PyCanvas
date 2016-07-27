# coding: utf-8

"""


    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from ...base_model import BaseModel
from pprint import pformat
from six import iteritems
import re


class LockInfo(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, asset_string=None, unlock_at=None, lock_at=None, context_module=None, manually_locked=None):
        """
        LockInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'asset_string': 'str',
            'unlock_at': 'Datetime',
            'lock_at': 'Datetime',
            'context_module': 'str',
            'manually_locked': 'bool'
        }

        self.attribute_map = {
            'asset_string': 'asset_string',
            'unlock_at': 'unlock_at',
            'lock_at': 'lock_at',
            'context_module': 'context_module',
            'manually_locked': 'manually_locked'
        }

        self._asset_string = asset_string
        self._unlock_at = unlock_at
        self._lock_at = lock_at
        self._context_module = context_module
        self._manually_locked = manually_locked

    @property
    def asset_string(self):
        """
        Gets the asset_string of this LockInfo.
        Asset string for the object causing the lock

        :return: The asset_string of this LockInfo.
        :rtype: str
        """
        return self._asset_string

    @asset_string.setter
    def asset_string(self, asset_string):
        """
        Sets the asset_string of this LockInfo.
        Asset string for the object causing the lock

        :param asset_string: The asset_string of this LockInfo.
        :type: str
        """

        self._asset_string = asset_string

    @property
    def unlock_at(self):
        """
        Gets the unlock_at of this LockInfo.
        (Optional) Time at which this was/will be unlocked.

        :return: The unlock_at of this LockInfo.
        :rtype: Datetime
        """
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, unlock_at):
        """
        Sets the unlock_at of this LockInfo.
        (Optional) Time at which this was/will be unlocked.

        :param unlock_at: The unlock_at of this LockInfo.
        :type: Datetime
        """

        self._unlock_at = unlock_at

    @property
    def lock_at(self):
        """
        Gets the lock_at of this LockInfo.
        (Optional) Time at which this was/will be locked.

        :return: The lock_at of this LockInfo.
        :rtype: Datetime
        """
        return self._lock_at

    @lock_at.setter
    def lock_at(self, lock_at):
        """
        Sets the lock_at of this LockInfo.
        (Optional) Time at which this was/will be locked.

        :param lock_at: The lock_at of this LockInfo.
        :type: Datetime
        """

        self._lock_at = lock_at

    @property
    def context_module(self):
        """
        Gets the context_module of this LockInfo.
        (Optional) Context module causing the lock.

        :return: The context_module of this LockInfo.
        :rtype: str
        """
        return self._context_module

    @context_module.setter
    def context_module(self, context_module):
        """
        Sets the context_module of this LockInfo.
        (Optional) Context module causing the lock.

        :param context_module: The context_module of this LockInfo.
        :type: str
        """

        self._context_module = context_module

    @property
    def manually_locked(self):
        """
        Gets the manually_locked of this LockInfo.


        :return: The manually_locked of this LockInfo.
        :rtype: bool
        """
        return self._manually_locked

    @manually_locked.setter
    def manually_locked(self, manually_locked):
        """
        Sets the manually_locked of this LockInfo.


        :param manually_locked: The manually_locked of this LockInfo.
        :type: bool
        """

        self._manually_locked = manually_locked

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
