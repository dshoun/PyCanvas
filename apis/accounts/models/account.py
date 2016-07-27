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


class Account(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, parent_account_id=None, root_account_id=None, default_storage_quota_mb=None, default_user_storage_quota_mb=None, default_group_storage_quota_mb=None, default_time_zone=None, sis_account_id=None, integration_id=None, sis_import_id=None, lti_guid=None, workflow_state=None):
        """
        Account - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'parent_account_id': 'int',
            'root_account_id': 'int',
            'default_storage_quota_mb': 'int',
            'default_user_storage_quota_mb': 'int',
            'default_group_storage_quota_mb': 'int',
            'default_time_zone': 'str',
            'sis_account_id': 'str',
            'integration_id': 'str',
            'sis_import_id': 'int',
            'lti_guid': 'str',
            'workflow_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'parent_account_id': 'parent_account_id',
            'root_account_id': 'root_account_id',
            'default_storage_quota_mb': 'default_storage_quota_mb',
            'default_user_storage_quota_mb': 'default_user_storage_quota_mb',
            'default_group_storage_quota_mb': 'default_group_storage_quota_mb',
            'default_time_zone': 'default_time_zone',
            'sis_account_id': 'sis_account_id',
            'integration_id': 'integration_id',
            'sis_import_id': 'sis_import_id',
            'lti_guid': 'lti_guid',
            'workflow_state': 'workflow_state'
        }

        self._id = id
        self._name = name
        self._parent_account_id = parent_account_id
        self._root_account_id = root_account_id
        self._default_storage_quota_mb = default_storage_quota_mb
        self._default_user_storage_quota_mb = default_user_storage_quota_mb
        self._default_group_storage_quota_mb = default_group_storage_quota_mb
        self._default_time_zone = default_time_zone
        self._sis_account_id = sis_account_id
        self._integration_id = integration_id
        self._sis_import_id = sis_import_id
        self._lti_guid = lti_guid
        self._workflow_state = workflow_state

    @property
    def id(self):
        """
        Gets the id of this Account.
        the ID of the Account object

        :return: The id of this Account.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Account.
        the ID of the Account object

        :param id: The id of this Account.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Account.
        The display name of the account

        :return: The name of this Account.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Account.
        The display name of the account

        :param name: The name of this Account.
        :type: str
        """

        self._name = name

    @property
    def parent_account_id(self):
        """
        Gets the parent_account_id of this Account.
        The account's parent ID, or null if this is the root account

        :return: The parent_account_id of this Account.
        :rtype: int
        """
        return self._parent_account_id

    @parent_account_id.setter
    def parent_account_id(self, parent_account_id):
        """
        Sets the parent_account_id of this Account.
        The account's parent ID, or null if this is the root account

        :param parent_account_id: The parent_account_id of this Account.
        :type: int
        """

        self._parent_account_id = parent_account_id

    @property
    def root_account_id(self):
        """
        Gets the root_account_id of this Account.
        The ID of the root account, or null if this is the root account

        :return: The root_account_id of this Account.
        :rtype: int
        """
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, root_account_id):
        """
        Sets the root_account_id of this Account.
        The ID of the root account, or null if this is the root account

        :param root_account_id: The root_account_id of this Account.
        :type: int
        """

        self._root_account_id = root_account_id

    @property
    def default_storage_quota_mb(self):
        """
        Gets the default_storage_quota_mb of this Account.
        The storage quota for the account in megabytes, if not otherwise specified

        :return: The default_storage_quota_mb of this Account.
        :rtype: int
        """
        return self._default_storage_quota_mb

    @default_storage_quota_mb.setter
    def default_storage_quota_mb(self, default_storage_quota_mb):
        """
        Sets the default_storage_quota_mb of this Account.
        The storage quota for the account in megabytes, if not otherwise specified

        :param default_storage_quota_mb: The default_storage_quota_mb of this Account.
        :type: int
        """

        self._default_storage_quota_mb = default_storage_quota_mb

    @property
    def default_user_storage_quota_mb(self):
        """
        Gets the default_user_storage_quota_mb of this Account.
        The storage quota for a user in the account in megabytes, if not otherwise specified

        :return: The default_user_storage_quota_mb of this Account.
        :rtype: int
        """
        return self._default_user_storage_quota_mb

    @default_user_storage_quota_mb.setter
    def default_user_storage_quota_mb(self, default_user_storage_quota_mb):
        """
        Sets the default_user_storage_quota_mb of this Account.
        The storage quota for a user in the account in megabytes, if not otherwise specified

        :param default_user_storage_quota_mb: The default_user_storage_quota_mb of this Account.
        :type: int
        """

        self._default_user_storage_quota_mb = default_user_storage_quota_mb

    @property
    def default_group_storage_quota_mb(self):
        """
        Gets the default_group_storage_quota_mb of this Account.
        The storage quota for a group in the account in megabytes, if not otherwise specified

        :return: The default_group_storage_quota_mb of this Account.
        :rtype: int
        """
        return self._default_group_storage_quota_mb

    @default_group_storage_quota_mb.setter
    def default_group_storage_quota_mb(self, default_group_storage_quota_mb):
        """
        Sets the default_group_storage_quota_mb of this Account.
        The storage quota for a group in the account in megabytes, if not otherwise specified

        :param default_group_storage_quota_mb: The default_group_storage_quota_mb of this Account.
        :type: int
        """

        self._default_group_storage_quota_mb = default_group_storage_quota_mb

    @property
    def default_time_zone(self):
        """
        Gets the default_time_zone of this Account.
        The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.

        :return: The default_time_zone of this Account.
        :rtype: str
        """
        return self._default_time_zone

    @default_time_zone.setter
    def default_time_zone(self, default_time_zone):
        """
        Sets the default_time_zone of this Account.
        The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.

        :param default_time_zone: The default_time_zone of this Account.
        :type: str
        """

        self._default_time_zone = default_time_zone

    @property
    def sis_account_id(self):
        """
        Gets the sis_account_id of this Account.
        The account's identifier in the Student Information System. Only included if the user has permission to view SIS information.

        :return: The sis_account_id of this Account.
        :rtype: str
        """
        return self._sis_account_id

    @sis_account_id.setter
    def sis_account_id(self, sis_account_id):
        """
        Sets the sis_account_id of this Account.
        The account's identifier in the Student Information System. Only included if the user has permission to view SIS information.

        :param sis_account_id: The sis_account_id of this Account.
        :type: str
        """

        self._sis_account_id = sis_account_id

    @property
    def integration_id(self):
        """
        Gets the integration_id of this Account.
        The account's identifier in the Student Information System. Only included if the user has permission to view SIS information.

        :return: The integration_id of this Account.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this Account.
        The account's identifier in the Student Information System. Only included if the user has permission to view SIS information.

        :param integration_id: The integration_id of this Account.
        :type: str
        """

        self._integration_id = integration_id

    @property
    def sis_import_id(self):
        """
        Gets the sis_import_id of this Account.
        The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information.

        :return: The sis_import_id of this Account.
        :rtype: int
        """
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, sis_import_id):
        """
        Sets the sis_import_id of this Account.
        The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information.

        :param sis_import_id: The sis_import_id of this Account.
        :type: int
        """

        self._sis_import_id = sis_import_id

    @property
    def lti_guid(self):
        """
        Gets the lti_guid of this Account.
        The account's identifier that is sent as context_id in LTI launches.

        :return: The lti_guid of this Account.
        :rtype: str
        """
        return self._lti_guid

    @lti_guid.setter
    def lti_guid(self, lti_guid):
        """
        Sets the lti_guid of this Account.
        The account's identifier that is sent as context_id in LTI launches.

        :param lti_guid: The lti_guid of this Account.
        :type: str
        """

        self._lti_guid = lti_guid

    @property
    def workflow_state(self):
        """
        Gets the workflow_state of this Account.
        The state of the account. Can be 'active' or 'deleted'.

        :return: The workflow_state of this Account.
        :rtype: str
        """
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, workflow_state):
        """
        Sets the workflow_state of this Account.
        The state of the account. Can be 'active' or 'deleted'.

        :param workflow_state: The workflow_state of this Account.
        :type: str
        """

        self._workflow_state = workflow_state

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