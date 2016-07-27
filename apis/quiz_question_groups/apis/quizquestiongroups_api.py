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


class QuizquestiongroupsApi(BaseApi):
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

    # OPERATIONID: create_question_group
    def create_question_group(self, course_id, quiz_id, **kwargs):
        """
        Create a question group
        Create a new question group for this quiz  <b>201 Created</b> response code is returned if the creation was successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_question_group_with_http_info(course_id, quiz_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str quiz_id: ID (required)
        :param list[str] quiz_groups_name: The name of the question group.
        :param list[int] quiz_groups_pick_count: The number of questions to randomly select for this group.
        :param list[int] quiz_groups_question_points: The number of points to assign to each question in the group.
        :param list[int] quiz_groups_assessment_question_bank_id: The id of the assessment question bank to pull questions from.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'quiz_id', 'quiz_groups_name', 'quiz_groups_pick_count', 'quiz_groups_question_points', 'quiz_groups_assessment_question_bank_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_question_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `create_question_group`")
        # verify the required parameter 'quiz_id' is set
        if ('quiz_id' not in params) or (params['quiz_id'] is None):
            raise ValueError("Missing the required parameter `quiz_id` when calling `create_question_group`")

        resource_path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'quiz_id' in params:
            path_params['quiz_id'] = params['quiz_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'quiz_groups_name' in params:
            form_params.append(('quiz_groups[name]', params['quiz_groups_name']))
        if 'quiz_groups_pick_count' in params:
            form_params.append(('quiz_groups[pick_count]', params['quiz_groups_pick_count']))
        if 'quiz_groups_question_points' in params:
            form_params.append(('quiz_groups[question_points]', params['quiz_groups_question_points']))
        if 'quiz_groups_assessment_question_bank_id' in params:
            form_params.append(('quiz_groups[assessment_question_bank_id]', params['quiz_groups_assessment_question_bank_id']))

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

    # OPERATIONID: delete_question_group
    def delete_question_group(self, course_id, quiz_id, id, **kwargs):
        """
        Delete a question group
        Delete a question group  <b>204 No Content<b> response code is returned if the deletion was successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_question_group_with_http_info(course_id, quiz_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str quiz_id: ID (required)
        :param str id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'quiz_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_question_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `delete_question_group`")
        # verify the required parameter 'quiz_id' is set
        if ('quiz_id' not in params) or (params['quiz_id'] is None):
            raise ValueError("Missing the required parameter `quiz_id` when calling `delete_question_group`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_question_group`")

        resource_path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'quiz_id' in params:
            path_params['quiz_id'] = params['quiz_id']
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

    # OPERATIONID: reorder_question_groups
    def reorder_question_groups(self, course_id, quiz_id, id, order_id, **kwargs):
        """
        Reorder question groups
        Change the order of the quiz questions within the group  <b>204 No Content<b> response code is returned if the reorder was successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reorder_question_groups_with_http_info(course_id, quiz_id, id, order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str quiz_id: ID (required)
        :param str id: ID (required)
        :param list[int] order_id: The associated item's unique identifier (required)
        :param list[str] order_type: The type of item is always 'question' for a group
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'quiz_id', 'id', 'order_id', 'order_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reorder_question_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `reorder_question_groups`")
        # verify the required parameter 'quiz_id' is set
        if ('quiz_id' not in params) or (params['quiz_id'] is None):
            raise ValueError("Missing the required parameter `quiz_id` when calling `reorder_question_groups`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `reorder_question_groups`")
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params) or (params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `reorder_question_groups`")

        resource_path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'quiz_id' in params:
            path_params['quiz_id'] = params['quiz_id']
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
        if 'order_id' in params:
            form_params.append(('order[id]', params['order_id']))
        if 'order_type' in params:
            form_params.append(('order[type]', params['order_type']))

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

    # OPERATIONID: update_question_group
    def update_question_group(self, course_id, quiz_id, id, **kwargs):
        """
        Update a question group
        Update a question group

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_question_group_with_http_info(course_id, quiz_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str quiz_id: ID (required)
        :param str id: ID (required)
        :param list[str] quiz_groups_name: The name of the question group.
        :param list[int] quiz_groups_pick_count: The number of questions to randomly select for this group.
        :param list[int] quiz_groups_question_points: The number of points to assign to each question in the group.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'quiz_id', 'id', 'quiz_groups_name', 'quiz_groups_pick_count', 'quiz_groups_question_points']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_question_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `update_question_group`")
        # verify the required parameter 'quiz_id' is set
        if ('quiz_id' not in params) or (params['quiz_id'] is None):
            raise ValueError("Missing the required parameter `quiz_id` when calling `update_question_group`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_question_group`")

        resource_path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'quiz_id' in params:
            path_params['quiz_id'] = params['quiz_id']
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
        if 'quiz_groups_name' in params:
            form_params.append(('quiz_groups[name]', params['quiz_groups_name']))
        if 'quiz_groups_pick_count' in params:
            form_params.append(('quiz_groups[pick_count]', params['quiz_groups_pick_count']))
        if 'quiz_groups_question_points' in params:
            form_params.append(('quiz_groups[question_points]', params['quiz_groups_question_points']))

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
