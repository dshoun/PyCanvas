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


class AccountauthenticationservicesApi(BaseApi):
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

    # OPERATIONID: create_authorization_config
    def create_authorization_config(self, account_id, **kwargs):
        """
        Create Authorization Config
        Add external account authentication service(s) for the account. Services may be CAS, SAML, or LDAP.  Each authentication service is specified as a set of parameters as described below. A service specification must include an 'auth_type' parameter with a value of 'cas', 'saml', or 'ldap'. The other recognized parameters depend on this auth_type; unrecognized parameters are discarded. Service specifications not specifying a valid auth_type are ignored.  Any service specification may include an optional 'login_handle_name' parameter. This parameter specifies the label used for unique login identifiers; for example: 'Login', 'Username', 'Student ID', etc. The default is 'Email'.  You can set the 'position' for any configuration. The config in the 1st position is considered the default.  For CAS authentication services, the additional recognized parameters are:  - auth_base    The CAS server's URL.  - log_in_url [Optional]    An alternate SSO URL for logging into CAS. You probably should not set   this.  - unknown_user_url [Optional]    A url to redirect to when a user is authorized through CAS but is not   found in Canvas.  For SAML authentication services, the additional recognized parameters are:  - idp_entity_id    The SAML IdP's entity ID - This is used to look up the correct SAML IdP if   multiple are configured  - log_in_url    The SAML service's SSO target URL  - log_out_url    The SAML service's SLO target URL  - certificate_fingerprint    The SAML service's certificate fingerprint.  - change_password_url [Optional]    Forgot Password URL. Leave blank for default Canvas behavior.  - unknown_user_url [Optional]    A url to redirect to when a user is authorized through SAML but is not   found in Canvas.  - identifier_format    The SAML service's identifier format. Must be one of:    - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress   - urn:oasis:names:tc:SAML:2.0:nameid-format:entity   - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos   - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent   - urn:oasis:names:tc:SAML:2.0:nameid-format:transient   - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified   - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName   - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName  - requested_authn_context    The SAML AuthnContext  For LDAP authentication services, the additional recognized parameters are:  - auth_host    The LDAP server's URL.  - auth_port [Optional, Integer]    The LDAP server's TCP port. (default: 389)  - auth_over_tls [Optional]    Whether to use TLS. Can be '', 'simple_tls', or 'start_tls'. For backwards   compatibility, booleans are also accepted, with true meaning simple_tls.   If not provided, it will default to start_tls.  - auth_base [Optional]    A default treebase parameter for searches performed against the LDAP   server.  - auth_filter    LDAP search filter. Use !{{login}} as a placeholder for the username   supplied by the user. For example: \"(sAMAccountName=!{{login}})\".  - identifier_format [Optional]    The LDAP attribute to use to look up the Canvas login. Omit to use   the username supplied by the user.  - auth_username    Username  - auth_password    Password  - change_password_url [Optional]    Forgot Password URL. Leave blank for default Canvas behavior.  - account_authorization_config[n] (deprecated)   The nth service specification as described above. For instance, the   auth_type of the first service is given by the   account_authorization_config[0][auth_type] parameter. There must be   either a single CAS or SAML specification, or one or more LDAP   specifications. Additional services after an initial CAS or SAML service   are ignored; additional non-LDAP services after an initial LDAP service   are ignored.  _Deprecated_ Examples:  This endpoint still supports a deprecated version of setting the authorization configs. If you send data in this format it is considered a snapshot of how the configs should be setup and will clear any configs not sent.  Simple CAS server integration.    account_authorization_config[0][auth_type]=cas&   account_authorization_config[0][auth_base]=cas.mydomain.edu  Single SAML server integration.    account_authorization_config[0][idp_entity_id]=http://idp.myschool.com/sso/saml2   account_authorization_config[0][log_in_url]=saml-sso.mydomain.com&   account_authorization_config[0][log_out_url]=saml-slo.mydomain.com&   account_authorization_config[0][certificate_fingerprint]=1234567890ABCDEF&   account_authorization_config[0][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress  Two SAML server integration with discovery url.    discovery_url=http://www.myschool.com/sso/identity_provider_selection   account_authorization_config[0][idp_entity_id]=http://idp.myschool.com/sso/saml2&   account_authorization_config[0][log_in_url]=saml-sso.mydomain.com&   account_authorization_config[0][log_out_url]=saml-slo.mydomain.com&   account_authorization_config[0][certificate_fingerprint]=1234567890ABCDEF&   account_authorization_config[0][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress&   account_authorization_config[1][idp_entity_id]=http://idp.otherschool.com/sso/saml2&   account_authorization_config[1][log_in_url]=saml-sso.otherdomain.com&   account_authorization_config[1][log_out_url]=saml-slo.otherdomain.com&   account_authorization_config[1][certificate_fingerprint]=ABCDEFG12345678789&   account_authorization_config[1][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress  Single LDAP server integration.    account_authorization_config[0][auth_type]=ldap&   account_authorization_config[0][auth_host]=ldap.mydomain.edu&   account_authorization_config[0][auth_filter]=(sAMAccountName={{login}})&   account_authorization_config[0][auth_username]=username&   account_authorization_config[0][auth_password]=password  Multiple LDAP server integration.    account_authorization_config[0][auth_type]=ldap&   account_authorization_config[0][auth_host]=faculty-ldap.mydomain.edu&   account_authorization_config[0][auth_filter]=(sAMAccountName={{login}})&   account_authorization_config[0][auth_username]=username&   account_authorization_config[0][auth_password]=password&   account_authorization_config[1][auth_type]=ldap&   account_authorization_config[1][auth_host]=student-ldap.mydomain.edu&   account_authorization_config[1][auth_filter]=(sAMAccountName={{login}})&   account_authorization_config[1][auth_username]=username&   account_authorization_config[1][auth_password]=password

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_authorization_config_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :return: AccountAuthorizationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_authorization_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_authorization_config`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs'.replace('{format}', 'json')
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
                                            response_type='AccountAuthorizationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_authorization_config
    def delete_authorization_config(self, account_id, id, **kwargs):
        """
        Delete Authorization Config
        Delete the config

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_authorization_config_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :return: None
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
                    " to method delete_authorization_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_authorization_config`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_authorization_config`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'.replace('{format}', 'json')
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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_discovery_url
    def delete_discovery_url(self, account_id, **kwargs):
        """
        Delete discovery url
        Clear discovery url

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_discovery_url_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_discovery_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_discovery_url`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'.replace('{format}', 'json')
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

    # OPERATIONID: get_authorization_config
    def get_authorization_config(self, account_id, id, **kwargs):
        """
        Get Authorization Config
        Get the specified authorization config

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authorization_config_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :return: AccountAuthorizationConfig
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
                    " to method get_authorization_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_authorization_config`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_authorization_config`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AccountAuthorizationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: get_discovery_url
    def get_discovery_url(self, account_id, **kwargs):
        """
        GET discovery url
        Get the discovery url

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_discovery_url_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :return: DiscoveryUrl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_discovery_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_discovery_url`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'.replace('{format}', 'json')
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
                                            response_type='DiscoveryUrl',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_authorization_configs
    def list_authorization_configs(self, account_id, **kwargs):
        """
        List Authorization Configs
        Returns the list of authorization configs

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_authorization_configs_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :return: list[AccountAuthorizationConfig]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_authorization_configs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_authorization_configs`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs'.replace('{format}', 'json')
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
                                            response_type='list[AccountAuthorizationConfig]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: set_discovery_url
    def set_discovery_url(self, account_id, **kwargs):
        """
        Set discovery url
        If you have multiple IdPs configured, you can set a `discovery_url`. If that is set, canvas will forward all users to that URL when they need to be authenticated. That page will need to then help the user figure out where they need to go to log in.  If no discovery url is configured, the 1st auth config will be used to attempt to authenticate the user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_discovery_url_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :return: DiscoveryUrl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_discovery_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `set_discovery_url`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'.replace('{format}', 'json')
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
                                            response_type='DiscoveryUrl',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: update_authorization_config
    def update_authorization_config(self, account_id, id, **kwargs):
        """
        Update Authorization Config
        Update an authorization config using the same options as the create endpoint. You can not update an existing configuration to a new authentication type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_authorization_config_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :return: AccountAuthorizationConfig
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
                    " to method update_authorization_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_authorization_config`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_authorization_config`")

        resource_path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AccountAuthorizationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
