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


class EnrollmenttermsApi(BaseApi):
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

    # OPERATIONID: create_enrollment_term
    def create_enrollment_term(self, account_id, **kwargs):
        """
        Create enrollment term
        Create a new enrollment term for the specified account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_enrollment_term_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str enrollment_term_name: The name of the term.
        :param Object enrollment_term_start_at: The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :param Object enrollment_term_end_at: The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :param str enrollment_term_sis_term_id: The unique SIS identifier for the term.
        :return: EnrollmentTerm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'enrollment_term_name', 'enrollment_term_start_at', 'enrollment_term_end_at', 'enrollment_term_sis_term_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_enrollment_term" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_enrollment_term`")

        resource_path = '/v1/accounts/{account_id}/terms'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'enrollment_term_name' in params:
            form_params.append(('enrollment_term[name]', params['enrollment_term_name']))
        if 'enrollment_term_start_at' in params:
            form_params.append(('enrollment_term[start_at]', params['enrollment_term_start_at']))
        if 'enrollment_term_end_at' in params:
            form_params.append(('enrollment_term[end_at]', params['enrollment_term_end_at']))
        if 'enrollment_term_sis_term_id' in params:
            form_params.append(('enrollment_term[sis_term_id]', params['enrollment_term_sis_term_id']))

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
                                            response_type='EnrollmentTerm',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_enrollment_term
    def delete_enrollment_term(self, account_id, id, **kwargs):
        """
        Delete enrollment term
        Delete the specified enrollment term.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_enrollment_term_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :return: EnrollmentTerm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_enrollment_term" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_enrollment_term`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_enrollment_term`")

        resource_path = '/v1/accounts/{account_id}/terms/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
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
                                            response_type='EnrollmentTerm',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_enrollment_terms
    def list_enrollment_terms(self, account_id, **kwargs):
        """
        List enrollment terms
        Return all of the terms in the account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_enrollment_terms_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param list[str] workflow_state: no description
        :return: list[EnrollmentTerm]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'workflow_state']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_enrollment_terms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_enrollment_terms`")

        resource_path = '/v1/accounts/{account_id}/terms'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'workflow_state' in params:
            query_params['workflow_state'] = params['workflow_state']
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
                                            response_type='list[EnrollmentTerm]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: update_enrollment_term
    def update_enrollment_term(self, account_id, id, **kwargs):
        """
        Update enrollment term
        Update an existing enrollment term for the specified account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_enrollment_term_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :param str enrollment_term_name: The name of the term.
        :param Object enrollment_term_start_at: The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :param Object enrollment_term_end_at: The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :param str enrollment_term_sis_term_id: The unique SIS identifier for the term.
        :return: EnrollmentTerm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'id', 'enrollment_term_name', 'enrollment_term_start_at', 'enrollment_term_end_at', 'enrollment_term_sis_term_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_enrollment_term" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_enrollment_term`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_enrollment_term`")

        resource_path = '/v1/accounts/{account_id}/terms/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
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
        if 'enrollment_term_name' in params:
            form_params.append(('enrollment_term[name]', params['enrollment_term_name']))
        if 'enrollment_term_start_at' in params:
            form_params.append(('enrollment_term[start_at]', params['enrollment_term_start_at']))
        if 'enrollment_term_end_at' in params:
            form_params.append(('enrollment_term[end_at]', params['enrollment_term_end_at']))
        if 'enrollment_term_sis_term_id' in params:
            form_params.append(('enrollment_term[sis_term_id]', params['enrollment_term_sis_term_id']))

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
                                            response_type='EnrollmentTerm',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
