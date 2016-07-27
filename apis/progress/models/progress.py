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


class Progress(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, context_id=None, context_type=None, user_id=None, tag=None, completion=None, workflow_state=None, created_at=None, updated_at=None, message=None, url=None):
        """
        Progress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'context_id': 'int',
            'context_type': 'str',
            'user_id': 'int',
            'tag': 'str',
            'completion': 'int',
            'workflow_state': 'str',
            'created_at': 'Datetime',
            'updated_at': 'Datetime',
            'message': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'context_id': 'context_id',
            'context_type': 'context_type',
            'user_id': 'user_id',
            'tag': 'tag',
            'completion': 'completion',
            'workflow_state': 'workflow_state',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'message': 'message',
            'url': 'url'
        }

        self._id = id
        self._context_id = context_id
        self._context_type = context_type
        self._user_id = user_id
        self._tag = tag
        self._completion = completion
        self._workflow_state = workflow_state
        self._created_at = created_at
        self._updated_at = updated_at
        self._message = message
        self._url = url

    @property
    def id(self):
        """
        Gets the id of this Progress.
        the ID of the Progress object

        :return: The id of this Progress.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Progress.
        the ID of the Progress object

        :param id: The id of this Progress.
        :type: int
        """

        self._id = id

    @property
    def context_id(self):
        """
        Gets the context_id of this Progress.
        the context owning the job.

        :return: The context_id of this Progress.
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this Progress.
        the context owning the job.

        :param context_id: The context_id of this Progress.
        :type: int
        """

        self._context_id = context_id

    @property
    def context_type(self):
        """
        Gets the context_type of this Progress.


        :return: The context_type of this Progress.
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """
        Sets the context_type of this Progress.


        :param context_type: The context_type of this Progress.
        :type: str
        """

        self._context_type = context_type

    @property
    def user_id(self):
        """
        Gets the user_id of this Progress.
        the id of the user who started the job

        :return: The user_id of this Progress.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Progress.
        the id of the user who started the job

        :param user_id: The user_id of this Progress.
        :type: int
        """

        self._user_id = user_id

    @property
    def tag(self):
        """
        Gets the tag of this Progress.
        the type of operation

        :return: The tag of this Progress.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this Progress.
        the type of operation

        :param tag: The tag of this Progress.
        :type: str
        """

        self._tag = tag

    @property
    def completion(self):
        """
        Gets the completion of this Progress.
        percent completed

        :return: The completion of this Progress.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """
        Sets the completion of this Progress.
        percent completed

        :param completion: The completion of this Progress.
        :type: int
        """

        self._completion = completion

    @property
    def workflow_state(self):
        """
        Gets the workflow_state of this Progress.
        the state of the job one of 'queued', 'running', 'completed', 'failed'

        :return: The workflow_state of this Progress.
        :rtype: str
        """
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, workflow_state):
        """
        Sets the workflow_state of this Progress.
        the state of the job one of 'queued', 'running', 'completed', 'failed'

        :param workflow_state: The workflow_state of this Progress.
        :type: str
        """

        self._workflow_state = workflow_state

    @property
    def created_at(self):
        """
        Gets the created_at of this Progress.
        the time the job was created

        :return: The created_at of this Progress.
        :rtype: Datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Progress.
        the time the job was created

        :param created_at: The created_at of this Progress.
        :type: Datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Progress.
        the time the job was last updated

        :return: The updated_at of this Progress.
        :rtype: Datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Progress.
        the time the job was last updated

        :param updated_at: The updated_at of this Progress.
        :type: Datetime
        """

        self._updated_at = updated_at

    @property
    def message(self):
        """
        Gets the message of this Progress.
        optional details about the job

        :return: The message of this Progress.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Progress.
        optional details about the job

        :param message: The message of this Progress.
        :type: str
        """

        self._message = message

    @property
    def url(self):
        """
        Gets the url of this Progress.
        url where a progress update can be retrieved

        :return: The url of this Progress.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Progress.
        url where a progress update can be retrieved

        :param url: The url of this Progress.
        :type: str
        """

        self._url = url

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
