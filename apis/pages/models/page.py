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


class Page(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, title=None, created_at=None, updated_at=None, hide_from_students=None, editing_roles=None, last_edited_by=None, body=None, published=None, front_page=None, locked_for_user=None, lock_info=None, lock_explanation=None):
        """
        Page - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'title': 'str',
            'created_at': 'Datetime',
            'updated_at': 'Datetime',
            'hide_from_students': 'bool',
            'editing_roles': 'str',
            'last_edited_by': 'User',
            'body': 'str',
            'published': 'bool',
            'front_page': 'bool',
            'locked_for_user': 'bool',
            'lock_info': 'LockInfo',
            'lock_explanation': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'title': 'title',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'hide_from_students': 'hide_from_students',
            'editing_roles': 'editing_roles',
            'last_edited_by': 'last_edited_by',
            'body': 'body',
            'published': 'published',
            'front_page': 'front_page',
            'locked_for_user': 'locked_for_user',
            'lock_info': 'lock_info',
            'lock_explanation': 'lock_explanation'
        }

        self._url = url
        self._title = title
        self._created_at = created_at
        self._updated_at = updated_at
        self._hide_from_students = hide_from_students
        self._editing_roles = editing_roles
        self._last_edited_by = last_edited_by
        self._body = body
        self._published = published
        self._front_page = front_page
        self._locked_for_user = locked_for_user
        self._lock_info = lock_info
        self._lock_explanation = lock_explanation

    @property
    def url(self):
        """
        Gets the url of this Page.
        the unique locator for the page

        :return: The url of this Page.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Page.
        the unique locator for the page

        :param url: The url of this Page.
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """
        Gets the title of this Page.
        the title of the page

        :return: The title of this Page.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Page.
        the title of the page

        :param title: The title of this Page.
        :type: str
        """

        self._title = title

    @property
    def created_at(self):
        """
        Gets the created_at of this Page.
        the creation date for the page

        :return: The created_at of this Page.
        :rtype: Datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Page.
        the creation date for the page

        :param created_at: The created_at of this Page.
        :type: Datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Page.
        the date the page was last updated

        :return: The updated_at of this Page.
        :rtype: Datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Page.
        the date the page was last updated

        :param updated_at: The updated_at of this Page.
        :type: Datetime
        """

        self._updated_at = updated_at

    @property
    def hide_from_students(self):
        """
        Gets the hide_from_students of this Page.
        (DEPRECATED) whether this page is hidden from students (note: this is always reflected as the inverse of the published value)

        :return: The hide_from_students of this Page.
        :rtype: bool
        """
        return self._hide_from_students

    @hide_from_students.setter
    def hide_from_students(self, hide_from_students):
        """
        Sets the hide_from_students of this Page.
        (DEPRECATED) whether this page is hidden from students (note: this is always reflected as the inverse of the published value)

        :param hide_from_students: The hide_from_students of this Page.
        :type: bool
        """

        self._hide_from_students = hide_from_students

    @property
    def editing_roles(self):
        """
        Gets the editing_roles of this Page.
        roles allowed to edit the page; comma-separated list comprising a combination of 'teachers', 'students', 'members', and/or 'public' if not supplied, course defaults are used

        :return: The editing_roles of this Page.
        :rtype: str
        """
        return self._editing_roles

    @editing_roles.setter
    def editing_roles(self, editing_roles):
        """
        Sets the editing_roles of this Page.
        roles allowed to edit the page; comma-separated list comprising a combination of 'teachers', 'students', 'members', and/or 'public' if not supplied, course defaults are used

        :param editing_roles: The editing_roles of this Page.
        :type: str
        """

        self._editing_roles = editing_roles

    @property
    def last_edited_by(self):
        """
        Gets the last_edited_by of this Page.
        the User who last edited the page (this may not be present if the page was imported from another system)

        :return: The last_edited_by of this Page.
        :rtype: User
        """
        return self._last_edited_by

    @last_edited_by.setter
    def last_edited_by(self, last_edited_by):
        """
        Sets the last_edited_by of this Page.
        the User who last edited the page (this may not be present if the page was imported from another system)

        :param last_edited_by: The last_edited_by of this Page.
        :type: User
        """

        self._last_edited_by = last_edited_by

    @property
    def body(self):
        """
        Gets the body of this Page.
        the page content, in HTML (present when requesting a single page; omitted when listing pages)

        :return: The body of this Page.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this Page.
        the page content, in HTML (present when requesting a single page; omitted when listing pages)

        :param body: The body of this Page.
        :type: str
        """

        self._body = body

    @property
    def published(self):
        """
        Gets the published of this Page.
        whether the page is published (true) or draft state (false).

        :return: The published of this Page.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this Page.
        whether the page is published (true) or draft state (false).

        :param published: The published of this Page.
        :type: bool
        """

        self._published = published

    @property
    def front_page(self):
        """
        Gets the front_page of this Page.
        whether this page is the front page for the wiki

        :return: The front_page of this Page.
        :rtype: bool
        """
        return self._front_page

    @front_page.setter
    def front_page(self, front_page):
        """
        Sets the front_page of this Page.
        whether this page is the front page for the wiki

        :param front_page: The front_page of this Page.
        :type: bool
        """

        self._front_page = front_page

    @property
    def locked_for_user(self):
        """
        Gets the locked_for_user of this Page.
        Whether or not this is locked for the user.

        :return: The locked_for_user of this Page.
        :rtype: bool
        """
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, locked_for_user):
        """
        Sets the locked_for_user of this Page.
        Whether or not this is locked for the user.

        :param locked_for_user: The locked_for_user of this Page.
        :type: bool
        """

        self._locked_for_user = locked_for_user

    @property
    def lock_info(self):
        """
        Gets the lock_info of this Page.
        (Optional) Information for the user about the lock. Present when locked_for_user is true.

        :return: The lock_info of this Page.
        :rtype: LockInfo
        """
        return self._lock_info

    @lock_info.setter
    def lock_info(self, lock_info):
        """
        Sets the lock_info of this Page.
        (Optional) Information for the user about the lock. Present when locked_for_user is true.

        :param lock_info: The lock_info of this Page.
        :type: LockInfo
        """

        self._lock_info = lock_info

    @property
    def lock_explanation(self):
        """
        Gets the lock_explanation of this Page.
        (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true.

        :return: The lock_explanation of this Page.
        :rtype: str
        """
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, lock_explanation):
        """
        Sets the lock_explanation of this Page.
        (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true.

        :param lock_explanation: The lock_explanation of this Page.
        :type: str
        """

        self._lock_explanation = lock_explanation

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
