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


class QuizipfiltersApi(BaseApi):
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

    # OPERATIONID: get_available_quiz_ip_filters
    def get_available_quiz_ip_filters(self, course_id, quiz_id, **kwargs):
        """
        Get available quiz IP filters.
        Get a list of available IP filters for this Quiz.  <b>200 OK</b> response code is returned if the request was successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_quiz_ip_filters_with_http_info(course_id, quiz_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str quiz_id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'quiz_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_quiz_ip_filters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_available_quiz_ip_filters`")
        # verify the required parameter 'quiz_id' is set
        if ('quiz_id' not in params) or (params['quiz_id'] is None):
            raise ValueError("Missing the required parameter `quiz_id` when calling `get_available_quiz_ip_filters`")

        resource_path = '/v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters'.replace('{format}', 'json')
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
