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


class PageView(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, url=None, context_type=None, asset_type=None, controller=None, action=None, contributed=None, interaction_seconds=None, created_at=None, user_request=None, render_time=None, user_agent=None, participated=None, http_method=None, remote_ip=None, links=None):
        """
        PageView - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'url': 'str',
            'context_type': 'str',
            'asset_type': 'str',
            'controller': 'str',
            'action': 'str',
            'contributed': 'bool',
            'interaction_seconds': 'float',
            'created_at': 'Datetime',
            'user_request': 'bool',
            'render_time': 'float',
            'user_agent': 'str',
            'participated': 'bool',
            'http_method': 'str',
            'remote_ip': 'str',
            'links': 'PageViewLinks'
        }

        self.attribute_map = {
            'id': 'id',
            'url': 'url',
            'context_type': 'context_type',
            'asset_type': 'asset_type',
            'controller': 'controller',
            'action': 'action',
            'contributed': 'contributed',
            'interaction_seconds': 'interaction_seconds',
            'created_at': 'created_at',
            'user_request': 'user_request',
            'render_time': 'render_time',
            'user_agent': 'user_agent',
            'participated': 'participated',
            'http_method': 'http_method',
            'remote_ip': 'remote_ip',
            'links': 'links'
        }

        self._id = id
        self._url = url
        self._context_type = context_type
        self._asset_type = asset_type
        self._controller = controller
        self._action = action
        self._contributed = contributed
        self._interaction_seconds = interaction_seconds
        self._created_at = created_at
        self._user_request = user_request
        self._render_time = render_time
        self._user_agent = user_agent
        self._participated = participated
        self._http_method = http_method
        self._remote_ip = remote_ip
        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PageView.
        A UUID representing the page view.  This is also the unique request id

        :return: The id of this PageView.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PageView.
        A UUID representing the page view.  This is also the unique request id

        :param id: The id of this PageView.
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this PageView.
        The URL requested

        :return: The url of this PageView.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PageView.
        The URL requested

        :param url: The url of this PageView.
        :type: str
        """

        self._url = url

    @property
    def context_type(self):
        """
        Gets the context_type of this PageView.
        The type of context for the request

        :return: The context_type of this PageView.
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """
        Sets the context_type of this PageView.
        The type of context for the request

        :param context_type: The context_type of this PageView.
        :type: str
        """

        self._context_type = context_type

    @property
    def asset_type(self):
        """
        Gets the asset_type of this PageView.
        The type of asset in the context for the request, if any

        :return: The asset_type of this PageView.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """
        Sets the asset_type of this PageView.
        The type of asset in the context for the request, if any

        :param asset_type: The asset_type of this PageView.
        :type: str
        """

        self._asset_type = asset_type

    @property
    def controller(self):
        """
        Gets the controller of this PageView.
        The rails controller that handled the request

        :return: The controller of this PageView.
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this PageView.
        The rails controller that handled the request

        :param controller: The controller of this PageView.
        :type: str
        """

        self._controller = controller

    @property
    def action(self):
        """
        Gets the action of this PageView.
        The rails action that handled the request

        :return: The action of this PageView.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PageView.
        The rails action that handled the request

        :param action: The action of this PageView.
        :type: str
        """

        self._action = action

    @property
    def contributed(self):
        """
        Gets the contributed of this PageView.
        This field is deprecated, and will always be false

        :return: The contributed of this PageView.
        :rtype: bool
        """
        return self._contributed

    @contributed.setter
    def contributed(self, contributed):
        """
        Sets the contributed of this PageView.
        This field is deprecated, and will always be false

        :param contributed: The contributed of this PageView.
        :type: bool
        """

        self._contributed = contributed

    @property
    def interaction_seconds(self):
        """
        Gets the interaction_seconds of this PageView.
        An approximation of how long the user spent on the page, in seconds

        :return: The interaction_seconds of this PageView.
        :rtype: float
        """
        return self._interaction_seconds

    @interaction_seconds.setter
    def interaction_seconds(self, interaction_seconds):
        """
        Sets the interaction_seconds of this PageView.
        An approximation of how long the user spent on the page, in seconds

        :param interaction_seconds: The interaction_seconds of this PageView.
        :type: float
        """

        self._interaction_seconds = interaction_seconds

    @property
    def created_at(self):
        """
        Gets the created_at of this PageView.
        When the request was made

        :return: The created_at of this PageView.
        :rtype: Datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this PageView.
        When the request was made

        :param created_at: The created_at of this PageView.
        :type: Datetime
        """

        self._created_at = created_at

    @property
    def user_request(self):
        """
        Gets the user_request of this PageView.
        A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call)

        :return: The user_request of this PageView.
        :rtype: bool
        """
        return self._user_request

    @user_request.setter
    def user_request(self, user_request):
        """
        Sets the user_request of this PageView.
        A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call)

        :param user_request: The user_request of this PageView.
        :type: bool
        """

        self._user_request = user_request

    @property
    def render_time(self):
        """
        Gets the render_time of this PageView.
        How long the response took to render, in seconds

        :return: The render_time of this PageView.
        :rtype: float
        """
        return self._render_time

    @render_time.setter
    def render_time(self, render_time):
        """
        Sets the render_time of this PageView.
        How long the response took to render, in seconds

        :param render_time: The render_time of this PageView.
        :type: float
        """

        self._render_time = render_time

    @property
    def user_agent(self):
        """
        Gets the user_agent of this PageView.
        The user-agent of the browser or program that made the request

        :return: The user_agent of this PageView.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this PageView.
        The user-agent of the browser or program that made the request

        :param user_agent: The user_agent of this PageView.
        :type: str
        """

        self._user_agent = user_agent

    @property
    def participated(self):
        """
        Gets the participated of this PageView.
        True if the request counted as participating, such as submitting homework

        :return: The participated of this PageView.
        :rtype: bool
        """
        return self._participated

    @participated.setter
    def participated(self, participated):
        """
        Sets the participated of this PageView.
        True if the request counted as participating, such as submitting homework

        :param participated: The participated of this PageView.
        :type: bool
        """

        self._participated = participated

    @property
    def http_method(self):
        """
        Gets the http_method of this PageView.
        The HTTP method such as GET or POST

        :return: The http_method of this PageView.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """
        Sets the http_method of this PageView.
        The HTTP method such as GET or POST

        :param http_method: The http_method of this PageView.
        :type: str
        """

        self._http_method = http_method

    @property
    def remote_ip(self):
        """
        Gets the remote_ip of this PageView.
        The origin IP address of the request

        :return: The remote_ip of this PageView.
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """
        Sets the remote_ip of this PageView.
        The origin IP address of the request

        :param remote_ip: The remote_ip of this PageView.
        :type: str
        """

        self._remote_ip = remote_ip

    @property
    def links(self):
        """
        Gets the links of this PageView.
        The page view links to define the relationships

        :return: The links of this PageView.
        :rtype: PageViewLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PageView.
        The page view links to define the relationships

        :param links: The links of this PageView.
        :type: PageViewLinks
        """

        self._links = links

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
