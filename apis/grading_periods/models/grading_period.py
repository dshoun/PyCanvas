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


class GradingPeriod(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, start_date=None, end_date=None, weight=None):
        """
        GradingPeriod - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'weight': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'weight': 'weight'
        }

        self._id = id
        self._start_date = start_date
        self._end_date = end_date
        self._weight = weight

    @property
    def id(self):
        """
        Gets the id of this GradingPeriod.
        The unique identifier for the grading period.

        :return: The id of this GradingPeriod.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GradingPeriod.
        The unique identifier for the grading period.

        :param id: The id of this GradingPeriod.
        :type: int
        """

        self._id = id

    @property
    def start_date(self):
        """
        Gets the start_date of this GradingPeriod.
        The start date of the grading period.

        :return: The start_date of this GradingPeriod.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this GradingPeriod.
        The start date of the grading period.

        :param start_date: The start_date of this GradingPeriod.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this GradingPeriod.
        The end date of the grading period.

        :return: The end_date of this GradingPeriod.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this GradingPeriod.
        The end date of the grading period.

        :param end_date: The end_date of this GradingPeriod.
        :type: datetime
        """

        self._end_date = end_date

    @property
    def weight(self):
        """
        Gets the weight of this GradingPeriod.
        The weighted percentage on how much this particular period should count toward the total grade.

        :return: The weight of this GradingPeriod.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this GradingPeriod.
        The weighted percentage on how much this particular period should count toward the total grade.

        :param weight: The weight of this GradingPeriod.
        :type: int
        """

        self._weight = weight

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
