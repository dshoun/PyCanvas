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


class ContentDetails(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, points_possible=None, due_at=None, unlock_at=None, lock_at=None, locked_for_user=None, lock_explanation=None, lock_info=None):
        """
        ContentDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'points_possible': 'int',
            'due_at': 'Datetime',
            'unlock_at': 'Datetime',
            'lock_at': 'Datetime',
            'locked_for_user': 'bool',
            'lock_explanation': 'str',
            'lock_info': 'LockInfo'
        }

        self.attribute_map = {
            'points_possible': 'points_possible',
            'due_at': 'due_at',
            'unlock_at': 'unlock_at',
            'lock_at': 'lock_at',
            'locked_for_user': 'locked_for_user',
            'lock_explanation': 'lock_explanation',
            'lock_info': 'lock_info'
        }

        self._points_possible = points_possible
        self._due_at = due_at
        self._unlock_at = unlock_at
        self._lock_at = lock_at
        self._locked_for_user = locked_for_user
        self._lock_explanation = lock_explanation
        self._lock_info = lock_info

    @property
    def points_possible(self):
        """
        Gets the points_possible of this ContentDetails.


        :return: The points_possible of this ContentDetails.
        :rtype: int
        """
        return self._points_possible

    @points_possible.setter
    def points_possible(self, points_possible):
        """
        Sets the points_possible of this ContentDetails.


        :param points_possible: The points_possible of this ContentDetails.
        :type: int
        """

        self._points_possible = points_possible

    @property
    def due_at(self):
        """
        Gets the due_at of this ContentDetails.


        :return: The due_at of this ContentDetails.
        :rtype: Datetime
        """
        return self._due_at

    @due_at.setter
    def due_at(self, due_at):
        """
        Sets the due_at of this ContentDetails.


        :param due_at: The due_at of this ContentDetails.
        :type: Datetime
        """

        self._due_at = due_at

    @property
    def unlock_at(self):
        """
        Gets the unlock_at of this ContentDetails.


        :return: The unlock_at of this ContentDetails.
        :rtype: Datetime
        """
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, unlock_at):
        """
        Sets the unlock_at of this ContentDetails.


        :param unlock_at: The unlock_at of this ContentDetails.
        :type: Datetime
        """

        self._unlock_at = unlock_at

    @property
    def lock_at(self):
        """
        Gets the lock_at of this ContentDetails.


        :return: The lock_at of this ContentDetails.
        :rtype: Datetime
        """
        return self._lock_at

    @lock_at.setter
    def lock_at(self, lock_at):
        """
        Sets the lock_at of this ContentDetails.


        :param lock_at: The lock_at of this ContentDetails.
        :type: Datetime
        """

        self._lock_at = lock_at

    @property
    def locked_for_user(self):
        """
        Gets the locked_for_user of this ContentDetails.


        :return: The locked_for_user of this ContentDetails.
        :rtype: bool
        """
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, locked_for_user):
        """
        Sets the locked_for_user of this ContentDetails.


        :param locked_for_user: The locked_for_user of this ContentDetails.
        :type: bool
        """

        self._locked_for_user = locked_for_user

    @property
    def lock_explanation(self):
        """
        Gets the lock_explanation of this ContentDetails.


        :return: The lock_explanation of this ContentDetails.
        :rtype: str
        """
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, lock_explanation):
        """
        Sets the lock_explanation of this ContentDetails.


        :param lock_explanation: The lock_explanation of this ContentDetails.
        :type: str
        """

        self._lock_explanation = lock_explanation

    @property
    def lock_info(self):
        """
        Gets the lock_info of this ContentDetails.


        :return: The lock_info of this ContentDetails.
        :rtype: LockInfo
        """
        return self._lock_info

    @lock_info.setter
    def lock_info(self, lock_info):
        """
        Sets the lock_info of this ContentDetails.


        :param lock_info: The lock_info of this ContentDetails.
        :type: LockInfo
        """

        self._lock_info = lock_info

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
