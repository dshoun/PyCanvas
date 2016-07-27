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


class GradingStandard(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, title=None, id=None, context_type=None, context_id=None, grading_scheme=None):
        """
        GradingStandard - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'title': 'str',
            'id': 'int',
            'context_type': 'str',
            'context_id': 'int',
            'grading_scheme': 'list[GradingSchemeEntry]'
        }

        self.attribute_map = {
            'title': 'title',
            'id': 'id',
            'context_type': 'context_type',
            'context_id': 'context_id',
            'grading_scheme': 'grading_scheme'
        }

        self._title = title
        self._id = id
        self._context_type = context_type
        self._context_id = context_id
        self._grading_scheme = grading_scheme

    @property
    def title(self):
        """
        Gets the title of this GradingStandard.
        the title of the grading standard

        :return: The title of this GradingStandard.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this GradingStandard.
        the title of the grading standard

        :param title: The title of this GradingStandard.
        :type: str
        """

        self._title = title

    @property
    def id(self):
        """
        Gets the id of this GradingStandard.
        the id of the grading standard

        :return: The id of this GradingStandard.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GradingStandard.
        the id of the grading standard

        :param id: The id of this GradingStandard.
        :type: int
        """

        self._id = id

    @property
    def context_type(self):
        """
        Gets the context_type of this GradingStandard.
        the context this standard is associated with, either 'Account' or 'Course'

        :return: The context_type of this GradingStandard.
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """
        Sets the context_type of this GradingStandard.
        the context this standard is associated with, either 'Account' or 'Course'

        :param context_type: The context_type of this GradingStandard.
        :type: str
        """

        self._context_type = context_type

    @property
    def context_id(self):
        """
        Gets the context_id of this GradingStandard.
        the id for the context either the Account or Course id

        :return: The context_id of this GradingStandard.
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this GradingStandard.
        the id for the context either the Account or Course id

        :param context_id: The context_id of this GradingStandard.
        :type: int
        """

        self._context_id = context_id

    @property
    def grading_scheme(self):
        """
        Gets the grading_scheme of this GradingStandard.
        A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value

        :return: The grading_scheme of this GradingStandard.
        :rtype: list[GradingSchemeEntry]
        """
        return self._grading_scheme

    @grading_scheme.setter
    def grading_scheme(self, grading_scheme):
        """
        Sets the grading_scheme of this GradingStandard.
        A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value

        :param grading_scheme: The grading_scheme of this GradingStandard.
        :type: list[GradingSchemeEntry]
        """

        self._grading_scheme = grading_scheme

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
