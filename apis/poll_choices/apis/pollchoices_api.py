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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ...base_api import BaseApi
from ...configuration import Configuration
from ..api_client import ApiClient


class PollchoicesApi(BaseApi):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    # OPERATIONID: create_single_poll_choice
    def create_single_poll_choice(self, poll_id, poll_choices_text, **kwargs):
        """
        Create a single poll choice
        Create a new poll choice for this poll

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_single_poll_choice_with_http_info(poll_id, poll_choices_text, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str poll_id: ID (required)
        :param list[str] poll_choices_text: The descriptive text of the poll choice. (required)
        :param list[bool] poll_choices_is_correct: Whether this poll choice is considered correct or not. Defaults to false.
        :param list[int] poll_choices_position: The order this poll choice should be returned in the context it's sibling poll choices.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['poll_id', 'poll_choices_text', 'poll_choices_is_correct', 'poll_choices_position']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_single_poll_choice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'poll_id' is set
        if ('poll_id' not in params) or (params['poll_id'] is None):
            raise ValueError("Missing the required parameter `poll_id` when calling `create_single_poll_choice`")
        # verify the required parameter 'poll_choices_text' is set
        if ('poll_choices_text' not in params) or (params['poll_choices_text'] is None):
            raise ValueError("Missing the required parameter `poll_choices_text` when calling `create_single_poll_choice`")

        resource_path = '/v1/polls/{poll_id}/poll_choices'.replace('{format}', 'json')
        path_params = {}
        if 'poll_id' in params:
            path_params['poll_id'] = params['poll_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'poll_choices_text' in params:
            form_params.append(('poll_choices[text]', params['poll_choices_text']))
        if 'poll_choices_is_correct' in params:
            form_params.append(('poll_choices[is_correct]', params['poll_choices_is_correct']))
        if 'poll_choices_position' in params:
            form_params.append(('poll_choices[position]', params['poll_choices_position']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_poll_choice
    def delete_poll_choice(self, poll_id, id, **kwargs):
        """
        Delete a poll choice
        <b>204 No Content</b> response code is returned if the deletion was successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_poll_choice_with_http_info(poll_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str poll_id: ID (required)
        :param str id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['poll_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_poll_choice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'poll_id' is set
        if ('poll_id' not in params) or (params['poll_id'] is None):
            raise ValueError("Missing the required parameter `poll_id` when calling `delete_poll_choice`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_poll_choice`")

        resource_path = '/v1/polls/{poll_id}/poll_choices/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'poll_id' in params:
            path_params['poll_id'] = params['poll_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: get_single_poll_choice
    def get_single_poll_choice(self, poll_id, id, **kwargs):
        """
        Get a single poll choice
        Returns the poll choice with the given id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_single_poll_choice_with_http_info(poll_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str poll_id: ID (required)
        :param str id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['poll_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_single_poll_choice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'poll_id' is set
        if ('poll_id' not in params) or (params['poll_id'] is None):
            raise ValueError("Missing the required parameter `poll_id` when calling `get_single_poll_choice`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_single_poll_choice`")

        resource_path = '/v1/polls/{poll_id}/poll_choices/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'poll_id' in params:
            path_params['poll_id'] = params['poll_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_poll_choices_in_poll
    def list_poll_choices_in_poll(self, poll_id, **kwargs):
        """
        List poll choices in a poll
        Returns the list of PollChoices in this poll.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_poll_choices_in_poll_with_http_info(poll_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str poll_id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['poll_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_poll_choices_in_poll" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'poll_id' is set
        if ('poll_id' not in params) or (params['poll_id'] is None):
            raise ValueError("Missing the required parameter `poll_id` when calling `list_poll_choices_in_poll`")

        resource_path = '/v1/polls/{poll_id}/poll_choices'.replace('{format}', 'json')
        path_params = {}
        if 'poll_id' in params:
            path_params['poll_id'] = params['poll_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: update_single_poll_choice
    def update_single_poll_choice(self, poll_id, id, poll_choices_text, **kwargs):
        """
        Update a single poll choice
        Update an existing poll choice for this poll

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_single_poll_choice_with_http_info(poll_id, id, poll_choices_text, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str poll_id: ID (required)
        :param str id: ID (required)
        :param list[str] poll_choices_text: The descriptive text of the poll choice. (required)
        :param list[bool] poll_choices_is_correct: Whether this poll choice is considered correct or not. Defaults to false.
        :param list[int] poll_choices_position: The order this poll choice should be returned in the context it's sibling poll choices.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['poll_id', 'id', 'poll_choices_text', 'poll_choices_is_correct', 'poll_choices_position']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_single_poll_choice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'poll_id' is set
        if ('poll_id' not in params) or (params['poll_id'] is None):
            raise ValueError("Missing the required parameter `poll_id` when calling `update_single_poll_choice`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_single_poll_choice`")
        # verify the required parameter 'poll_choices_text' is set
        if ('poll_choices_text' not in params) or (params['poll_choices_text'] is None):
            raise ValueError("Missing the required parameter `poll_choices_text` when calling `update_single_poll_choice`")

        resource_path = '/v1/polls/{poll_id}/poll_choices/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'poll_id' in params:
            path_params['poll_id'] = params['poll_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'poll_choices_text' in params:
            form_params.append(('poll_choices[text]', params['poll_choices_text']))
        if 'poll_choices_is_correct' in params:
            form_params.append(('poll_choices[is_correct]', params['poll_choices_is_correct']))
        if 'poll_choices_position' in params:
            form_params.append(('poll_choices[position]', params['poll_choices_position']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
