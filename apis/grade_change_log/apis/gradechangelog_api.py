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


class GradechangelogApi(BaseApi):
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

    # OPERATIONID: query_by_assignment
    def query_by_assignment(self, assignment_id, **kwargs):
        """
        Query by assignment.
        List grade change events for a given assignment.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_by_assignment_with_http_info(assignment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str assignment_id: ID (required)
        :param Object start_time: The beginning of the time range from which you want events.
        :param Object end_time: The end of the time range from which you want events.
        :return: list[GradeChangeEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_id', 'start_time', 'end_time']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_by_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_id' is set
        if ('assignment_id' not in params) or (params['assignment_id'] is None):
            raise ValueError("Missing the required parameter `assignment_id` when calling `query_by_assignment`")

        resource_path = '/v1/audit/grade_change/assignments/{assignment_id}'.replace('{format}', 'json')
        path_params = {}
        if 'assignment_id' in params:
            path_params['assignment_id'] = params['assignment_id']

        query_params = {}
        if 'start_time' in params:
            query_params['start_time'] = params['start_time']
        if 'end_time' in params:
            query_params['end_time'] = params['end_time']
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
                                            response_type='list[GradeChangeEvent]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: query_by_course
    def query_by_course(self, course_id, **kwargs):
        """
        Query by course.
        List grade change events for a given course.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_by_course_with_http_info(course_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param Object start_time: The beginning of the time range from which you want events.
        :param Object end_time: The end of the time range from which you want events.
        :return: list[GradeChangeEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'start_time', 'end_time']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_by_course" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `query_by_course`")

        resource_path = '/v1/audit/grade_change/courses/{course_id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']

        query_params = {}
        if 'start_time' in params:
            query_params['start_time'] = params['start_time']
        if 'end_time' in params:
            query_params['end_time'] = params['end_time']
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
                                            response_type='list[GradeChangeEvent]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: query_by_grader
    def query_by_grader(self, grader_id, **kwargs):
        """
        Query by grader.
        List grade change events for a given grader.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_by_grader_with_http_info(grader_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str grader_id: ID (required)
        :param Object start_time: The beginning of the time range from which you want events.
        :param Object end_time: The end of the time range from which you want events.
        :return: list[GradeChangeEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grader_id', 'start_time', 'end_time']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_by_grader" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grader_id' is set
        if ('grader_id' not in params) or (params['grader_id'] is None):
            raise ValueError("Missing the required parameter `grader_id` when calling `query_by_grader`")

        resource_path = '/v1/audit/grade_change/graders/{grader_id}'.replace('{format}', 'json')
        path_params = {}
        if 'grader_id' in params:
            path_params['grader_id'] = params['grader_id']

        query_params = {}
        if 'start_time' in params:
            query_params['start_time'] = params['start_time']
        if 'end_time' in params:
            query_params['end_time'] = params['end_time']
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
                                            response_type='list[GradeChangeEvent]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: query_by_student
    def query_by_student(self, student_id, **kwargs):
        """
        Query by student.
        List grade change events for a given student.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_by_student_with_http_info(student_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str student_id: ID (required)
        :param Object start_time: The beginning of the time range from which you want events.
        :param Object end_time: The end of the time range from which you want events.
        :return: list[GradeChangeEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['student_id', 'start_time', 'end_time']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_by_student" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'student_id' is set
        if ('student_id' not in params) or (params['student_id'] is None):
            raise ValueError("Missing the required parameter `student_id` when calling `query_by_student`")

        resource_path = '/v1/audit/grade_change/students/{student_id}'.replace('{format}', 'json')
        path_params = {}
        if 'student_id' in params:
            path_params['student_id'] = params['student_id']

        query_params = {}
        if 'start_time' in params:
            query_params['start_time'] = params['start_time']
        if 'end_time' in params:
            query_params['end_time'] = params['end_time']
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
                                            response_type='list[GradeChangeEvent]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
