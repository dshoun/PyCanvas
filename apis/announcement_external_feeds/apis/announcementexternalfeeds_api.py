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


class AnnouncementexternalfeedsApi(BaseApi):
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

    # OPERATIONID: create_external_feed_courses
    def create_external_feed_courses(self, course_id, url, **kwargs):
        """
        Create an external feed
        Create a new external feed for the course or group.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_external_feed_courses_with_http_info(course_id, url, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str url: The url to the external rss or atom feed (required)
        :param bool header_match: If given, only feed entries that contain this string in their title will be imported
        :param str verbosity: Defaults to \"full\"
        :return: ExternalFeed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'url', 'header_match', 'verbosity']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_external_feed_courses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `create_external_feed_courses`")
        # verify the required parameter 'url' is set
        if ('url' not in params) or (params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `create_external_feed_courses`")

        resource_path = '/v1/courses/{course_id}/external_feeds'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'url' in params:
            form_params.append(('url', params['url']))
        if 'header_match' in params:
            form_params.append(('header_match', params['header_match']))
        if 'verbosity' in params:
            form_params.append(('verbosity', params['verbosity']))

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
                                            response_type='ExternalFeed',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: create_external_feed_groups
    def create_external_feed_groups(self, group_id, url, **kwargs):
        """
        Create an external feed
        Create a new external feed for the course or group.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_external_feed_groups_with_http_info(group_id, url, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: ID (required)
        :param str url: The url to the external rss or atom feed (required)
        :param bool header_match: If given, only feed entries that contain this string in their title will be imported
        :param str verbosity: Defaults to \"full\"
        :return: ExternalFeed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'url', 'header_match', 'verbosity']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_external_feed_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `create_external_feed_groups`")
        # verify the required parameter 'url' is set
        if ('url' not in params) or (params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `create_external_feed_groups`")

        resource_path = '/v1/groups/{group_id}/external_feeds'.replace('{format}', 'json')
        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'url' in params:
            form_params.append(('url', params['url']))
        if 'header_match' in params:
            form_params.append(('header_match', params['header_match']))
        if 'verbosity' in params:
            form_params.append(('verbosity', params['verbosity']))

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
                                            response_type='ExternalFeed',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_external_feed_courses
    def delete_external_feed_courses(self, course_id, external_feed_id, **kwargs):
        """
        Delete an external feed
        Deletes the external feed.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_external_feed_courses_with_http_info(course_id, external_feed_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str external_feed_id: ID (required)
        :return: ExternalFeed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'external_feed_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_external_feed_courses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `delete_external_feed_courses`")
        # verify the required parameter 'external_feed_id' is set
        if ('external_feed_id' not in params) or (params['external_feed_id'] is None):
            raise ValueError("Missing the required parameter `external_feed_id` when calling `delete_external_feed_courses`")

        resource_path = '/v1/courses/{course_id}/external_feeds/{external_feed_id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'external_feed_id' in params:
            path_params['external_feed_id'] = params['external_feed_id']

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
                                            response_type='ExternalFeed',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_external_feed_groups
    def delete_external_feed_groups(self, group_id, external_feed_id, **kwargs):
        """
        Delete an external feed
        Deletes the external feed.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_external_feed_groups_with_http_info(group_id, external_feed_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: ID (required)
        :param str external_feed_id: ID (required)
        :return: ExternalFeed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'external_feed_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_external_feed_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_external_feed_groups`")
        # verify the required parameter 'external_feed_id' is set
        if ('external_feed_id' not in params) or (params['external_feed_id'] is None):
            raise ValueError("Missing the required parameter `external_feed_id` when calling `delete_external_feed_groups`")

        resource_path = '/v1/groups/{group_id}/external_feeds/{external_feed_id}'.replace('{format}', 'json')
        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']
        if 'external_feed_id' in params:
            path_params['external_feed_id'] = params['external_feed_id']

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
                                            response_type='ExternalFeed',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_external_feeds_courses
    def list_external_feeds_courses(self, course_id, **kwargs):
        """
        List external feeds
        Returns the list of External Feeds this course or group.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_external_feeds_courses_with_http_info(course_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :return: list[ExternalFeed]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_external_feeds_courses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `list_external_feeds_courses`")

        resource_path = '/v1/courses/{course_id}/external_feeds'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']

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
                                            response_type='list[ExternalFeed]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_external_feeds_groups
    def list_external_feeds_groups(self, group_id, **kwargs):
        """
        List external feeds
        Returns the list of External Feeds this course or group.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_external_feeds_groups_with_http_info(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: ID (required)
        :return: list[ExternalFeed]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_external_feeds_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `list_external_feeds_groups`")

        resource_path = '/v1/groups/{group_id}/external_feeds'.replace('{format}', 'json')
        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']

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
                                            response_type='list[ExternalFeed]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
