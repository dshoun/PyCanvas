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


class Course(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, sis_course_id=None, integration_id=None, name=None, course_code=None, workflow_state=None, account_id=None, root_account_id=None, enrollment_term_id=None, start_at=None, end_at=None, enrollments=None, total_students=None, calendar=None, default_view=None, syllabus_body=None, needs_grading_count=None, term=None, course_progress=None, apply_assignment_group_weights=None, permissions=None, is_public=None, is_public_to_auth_users=None, public_syllabus=None, public_description=None, storage_quota_mb=None, storage_quota_used_mb=None, hide_final_grades=None, license=None, allow_student_assignment_edits=None, allow_wiki_comments=None, allow_student_forum_attachments=None, open_enrollment=None, self_enrollment=None, restrict_enrollments_to_course_dates=None, course_format=None):
        """
        Course - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'sis_course_id': 'str',
            'integration_id': 'str',
            'name': 'str',
            'course_code': 'str',
            'workflow_state': 'str',
            'account_id': 'int',
            'root_account_id': 'int',
            'enrollment_term_id': 'int',
            'start_at': 'Datetime',
            'end_at': 'Datetime',
            'enrollments': 'list[Enrollment]',
            'total_students': 'int',
            'calendar': 'CalendarLink',
            'default_view': 'str',
            'syllabus_body': 'str',
            'needs_grading_count': 'int',
            'term': 'Term',
            'course_progress': 'CourseProgress',
            'apply_assignment_group_weights': 'bool',
            'permissions': 'dict',
            'is_public': 'bool',
            'is_public_to_auth_users': 'bool',
            'public_syllabus': 'bool',
            'public_description': 'str',
            'storage_quota_mb': 'int',
            'storage_quota_used_mb': 'float',
            'hide_final_grades': 'bool',
            'license': 'str',
            'allow_student_assignment_edits': 'bool',
            'allow_wiki_comments': 'bool',
            'allow_student_forum_attachments': 'bool',
            'open_enrollment': 'bool',
            'self_enrollment': 'bool',
            'restrict_enrollments_to_course_dates': 'bool',
            'course_format': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'sis_course_id': 'sis_course_id',
            'integration_id': 'integration_id',
            'name': 'name',
            'course_code': 'course_code',
            'workflow_state': 'workflow_state',
            'account_id': 'account_id',
            'root_account_id': 'root_account_id',
            'enrollment_term_id': 'enrollment_term_id',
            'start_at': 'start_at',
            'end_at': 'end_at',
            'enrollments': 'enrollments',
            'total_students': 'total_students',
            'calendar': 'calendar',
            'default_view': 'default_view',
            'syllabus_body': 'syllabus_body',
            'needs_grading_count': 'needs_grading_count',
            'term': 'term',
            'course_progress': 'course_progress',
            'apply_assignment_group_weights': 'apply_assignment_group_weights',
            'permissions': 'permissions',
            'is_public': 'is_public',
            'is_public_to_auth_users': 'is_public_to_auth_users',
            'public_syllabus': 'public_syllabus',
            'public_description': 'public_description',
            'storage_quota_mb': 'storage_quota_mb',
            'storage_quota_used_mb': 'storage_quota_used_mb',
            'hide_final_grades': 'hide_final_grades',
            'license': 'license',
            'allow_student_assignment_edits': 'allow_student_assignment_edits',
            'allow_wiki_comments': 'allow_wiki_comments',
            'allow_student_forum_attachments': 'allow_student_forum_attachments',
            'open_enrollment': 'open_enrollment',
            'self_enrollment': 'self_enrollment',
            'restrict_enrollments_to_course_dates': 'restrict_enrollments_to_course_dates',
            'course_format': 'course_format'
        }

        self._id = id
        self._sis_course_id = sis_course_id
        self._integration_id = integration_id
        self._name = name
        self._course_code = course_code
        self._workflow_state = workflow_state
        self._account_id = account_id
        self._root_account_id = root_account_id
        self._enrollment_term_id = enrollment_term_id
        self._start_at = start_at
        self._end_at = end_at
        self._enrollments = enrollments
        self._total_students = total_students
        self._calendar = calendar
        self._default_view = default_view
        self._syllabus_body = syllabus_body
        self._needs_grading_count = needs_grading_count
        self._term = term
        self._course_progress = course_progress
        self._apply_assignment_group_weights = apply_assignment_group_weights
        self._permissions = permissions
        self._is_public = is_public
        self._is_public_to_auth_users = is_public_to_auth_users
        self._public_syllabus = public_syllabus
        self._public_description = public_description
        self._storage_quota_mb = storage_quota_mb
        self._storage_quota_used_mb = storage_quota_used_mb
        self._hide_final_grades = hide_final_grades
        self._license = license
        self._allow_student_assignment_edits = allow_student_assignment_edits
        self._allow_wiki_comments = allow_wiki_comments
        self._allow_student_forum_attachments = allow_student_forum_attachments
        self._open_enrollment = open_enrollment
        self._self_enrollment = self_enrollment
        self._restrict_enrollments_to_course_dates = restrict_enrollments_to_course_dates
        self._course_format = course_format

    @property
    def id(self):
        """
        Gets the id of this Course.
        the unique identifier for the course

        :return: The id of this Course.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Course.
        the unique identifier for the course

        :param id: The id of this Course.
        :type: int
        """

        self._id = id

    @property
    def sis_course_id(self):
        """
        Gets the sis_course_id of this Course.
        the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information.

        :return: The sis_course_id of this Course.
        :rtype: str
        """
        return self._sis_course_id

    @sis_course_id.setter
    def sis_course_id(self, sis_course_id):
        """
        Sets the sis_course_id of this Course.
        the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information.

        :param sis_course_id: The sis_course_id of this Course.
        :type: str
        """

        self._sis_course_id = sis_course_id

    @property
    def integration_id(self):
        """
        Gets the integration_id of this Course.
        the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information.

        :return: The integration_id of this Course.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this Course.
        the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information.

        :param integration_id: The integration_id of this Course.
        :type: str
        """

        self._integration_id = integration_id

    @property
    def name(self):
        """
        Gets the name of this Course.
        the full name of the course

        :return: The name of this Course.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Course.
        the full name of the course

        :param name: The name of this Course.
        :type: str
        """

        self._name = name

    @property
    def course_code(self):
        """
        Gets the course_code of this Course.
        the course code

        :return: The course_code of this Course.
        :rtype: str
        """
        return self._course_code

    @course_code.setter
    def course_code(self, course_code):
        """
        Sets the course_code of this Course.
        the course code

        :param course_code: The course_code of this Course.
        :type: str
        """

        self._course_code = course_code

    @property
    def workflow_state(self):
        """
        Gets the workflow_state of this Course.
        the current state of the course one of 'unpublished', 'available', 'completed', or 'deleted'

        :return: The workflow_state of this Course.
        :rtype: str
        """
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, workflow_state):
        """
        Sets the workflow_state of this Course.
        the current state of the course one of 'unpublished', 'available', 'completed', or 'deleted'

        :param workflow_state: The workflow_state of this Course.
        :type: str
        """

        self._workflow_state = workflow_state

    @property
    def account_id(self):
        """
        Gets the account_id of this Course.
        the account associated with the course

        :return: The account_id of this Course.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this Course.
        the account associated with the course

        :param account_id: The account_id of this Course.
        :type: int
        """

        self._account_id = account_id

    @property
    def root_account_id(self):
        """
        Gets the root_account_id of this Course.
        the root account associated with the course

        :return: The root_account_id of this Course.
        :rtype: int
        """
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, root_account_id):
        """
        Sets the root_account_id of this Course.
        the root account associated with the course

        :param root_account_id: The root_account_id of this Course.
        :type: int
        """

        self._root_account_id = root_account_id

    @property
    def enrollment_term_id(self):
        """
        Gets the enrollment_term_id of this Course.
        the enrollment term associated with the course

        :return: The enrollment_term_id of this Course.
        :rtype: int
        """
        return self._enrollment_term_id

    @enrollment_term_id.setter
    def enrollment_term_id(self, enrollment_term_id):
        """
        Sets the enrollment_term_id of this Course.
        the enrollment term associated with the course

        :param enrollment_term_id: The enrollment_term_id of this Course.
        :type: int
        """

        self._enrollment_term_id = enrollment_term_id

    @property
    def start_at(self):
        """
        Gets the start_at of this Course.
        the start date for the course, if applicable

        :return: The start_at of this Course.
        :rtype: Datetime
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """
        Sets the start_at of this Course.
        the start date for the course, if applicable

        :param start_at: The start_at of this Course.
        :type: Datetime
        """

        self._start_at = start_at

    @property
    def end_at(self):
        """
        Gets the end_at of this Course.
        the end date for the course, if applicable

        :return: The end_at of this Course.
        :rtype: Datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """
        Sets the end_at of this Course.
        the end date for the course, if applicable

        :param end_at: The end_at of this Course.
        :type: Datetime
        """

        self._end_at = end_at

    @property
    def enrollments(self):
        """
        Gets the enrollments of this Course.
        A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]=total_scores

        :return: The enrollments of this Course.
        :rtype: list[Enrollment]
        """
        return self._enrollments

    @enrollments.setter
    def enrollments(self, enrollments):
        """
        Sets the enrollments of this Course.
        A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]=total_scores

        :param enrollments: The enrollments of this Course.
        :type: list[Enrollment]
        """

        self._enrollments = enrollments

    @property
    def total_students(self):
        """
        Gets the total_students of this Course.
        optional: the total number of active and invited students in the course

        :return: The total_students of this Course.
        :rtype: int
        """
        return self._total_students

    @total_students.setter
    def total_students(self, total_students):
        """
        Sets the total_students of this Course.
        optional: the total number of active and invited students in the course

        :param total_students: The total_students of this Course.
        :type: int
        """

        self._total_students = total_students

    @property
    def calendar(self):
        """
        Gets the calendar of this Course.
        course calendar

        :return: The calendar of this Course.
        :rtype: CalendarLink
        """
        return self._calendar

    @calendar.setter
    def calendar(self, calendar):
        """
        Sets the calendar of this Course.
        course calendar

        :param calendar: The calendar of this Course.
        :type: CalendarLink
        """

        self._calendar = calendar

    @property
    def default_view(self):
        """
        Gets the default_view of this Course.
        the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future

        :return: The default_view of this Course.
        :rtype: str
        """
        return self._default_view

    @default_view.setter
    def default_view(self, default_view):
        """
        Sets the default_view of this Course.
        the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future

        :param default_view: The default_view of this Course.
        :type: str
        """

        self._default_view = default_view

    @property
    def syllabus_body(self):
        """
        Gets the syllabus_body of this Course.
        optional: user-generated HTML for the course syllabus

        :return: The syllabus_body of this Course.
        :rtype: str
        """
        return self._syllabus_body

    @syllabus_body.setter
    def syllabus_body(self, syllabus_body):
        """
        Sets the syllabus_body of this Course.
        optional: user-generated HTML for the course syllabus

        :param syllabus_body: The syllabus_body of this Course.
        :type: str
        """

        self._syllabus_body = syllabus_body

    @property
    def needs_grading_count(self):
        """
        Gets the needs_grading_count of this Course.
        optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count

        :return: The needs_grading_count of this Course.
        :rtype: int
        """
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, needs_grading_count):
        """
        Sets the needs_grading_count of this Course.
        optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count

        :param needs_grading_count: The needs_grading_count of this Course.
        :type: int
        """

        self._needs_grading_count = needs_grading_count

    @property
    def term(self):
        """
        Gets the term of this Course.
        optional: the enrollment term object for the course returned only if include[]=term

        :return: The term of this Course.
        :rtype: Term
        """
        return self._term

    @term.setter
    def term(self, term):
        """
        Sets the term of this Course.
        optional: the enrollment term object for the course returned only if include[]=term

        :param term: The term of this Course.
        :type: Term
        """

        self._term = term

    @property
    def course_progress(self):
        """
        Gets the course_progress of this Course.
        optional (beta): information on progress through the course returned only if include[]=course_progress

        :return: The course_progress of this Course.
        :rtype: CourseProgress
        """
        return self._course_progress

    @course_progress.setter
    def course_progress(self, course_progress):
        """
        Sets the course_progress of this Course.
        optional (beta): information on progress through the course returned only if include[]=course_progress

        :param course_progress: The course_progress of this Course.
        :type: CourseProgress
        """

        self._course_progress = course_progress

    @property
    def apply_assignment_group_weights(self):
        """
        Gets the apply_assignment_group_weights of this Course.
        weight final grade based on assignment group percentages

        :return: The apply_assignment_group_weights of this Course.
        :rtype: bool
        """
        return self._apply_assignment_group_weights

    @apply_assignment_group_weights.setter
    def apply_assignment_group_weights(self, apply_assignment_group_weights):
        """
        Sets the apply_assignment_group_weights of this Course.
        weight final grade based on assignment group percentages

        :param apply_assignment_group_weights: The apply_assignment_group_weights of this Course.
        :type: bool
        """

        self._apply_assignment_group_weights = apply_assignment_group_weights

    @property
    def permissions(self):
        """
        Gets the permissions of this Course.
        optional: the permissions the user has for the course. returned only for a single course and include[]=permissions

        :return: The permissions of this Course.
        :rtype: dict
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this Course.
        optional: the permissions the user has for the course. returned only for a single course and include[]=permissions

        :param permissions: The permissions of this Course.
        :type: dict
        """

        self._permissions = permissions

    @property
    def is_public(self):
        """
        Gets the is_public of this Course.


        :return: The is_public of this Course.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this Course.


        :param is_public: The is_public of this Course.
        :type: bool
        """

        self._is_public = is_public

    @property
    def is_public_to_auth_users(self):
        """
        Gets the is_public_to_auth_users of this Course.


        :return: The is_public_to_auth_users of this Course.
        :rtype: bool
        """
        return self._is_public_to_auth_users

    @is_public_to_auth_users.setter
    def is_public_to_auth_users(self, is_public_to_auth_users):
        """
        Sets the is_public_to_auth_users of this Course.


        :param is_public_to_auth_users: The is_public_to_auth_users of this Course.
        :type: bool
        """

        self._is_public_to_auth_users = is_public_to_auth_users

    @property
    def public_syllabus(self):
        """
        Gets the public_syllabus of this Course.


        :return: The public_syllabus of this Course.
        :rtype: bool
        """
        return self._public_syllabus

    @public_syllabus.setter
    def public_syllabus(self, public_syllabus):
        """
        Sets the public_syllabus of this Course.


        :param public_syllabus: The public_syllabus of this Course.
        :type: bool
        """

        self._public_syllabus = public_syllabus

    @property
    def public_description(self):
        """
        Gets the public_description of this Course.


        :return: The public_description of this Course.
        :rtype: str
        """
        return self._public_description

    @public_description.setter
    def public_description(self, public_description):
        """
        Sets the public_description of this Course.


        :param public_description: The public_description of this Course.
        :type: str
        """

        self._public_description = public_description

    @property
    def storage_quota_mb(self):
        """
        Gets the storage_quota_mb of this Course.


        :return: The storage_quota_mb of this Course.
        :rtype: int
        """
        return self._storage_quota_mb

    @storage_quota_mb.setter
    def storage_quota_mb(self, storage_quota_mb):
        """
        Sets the storage_quota_mb of this Course.


        :param storage_quota_mb: The storage_quota_mb of this Course.
        :type: int
        """

        self._storage_quota_mb = storage_quota_mb

    @property
    def storage_quota_used_mb(self):
        """
        Gets the storage_quota_used_mb of this Course.


        :return: The storage_quota_used_mb of this Course.
        :rtype: float
        """
        return self._storage_quota_used_mb

    @storage_quota_used_mb.setter
    def storage_quota_used_mb(self, storage_quota_used_mb):
        """
        Sets the storage_quota_used_mb of this Course.


        :param storage_quota_used_mb: The storage_quota_used_mb of this Course.
        :type: float
        """

        self._storage_quota_used_mb = storage_quota_used_mb

    @property
    def hide_final_grades(self):
        """
        Gets the hide_final_grades of this Course.


        :return: The hide_final_grades of this Course.
        :rtype: bool
        """
        return self._hide_final_grades

    @hide_final_grades.setter
    def hide_final_grades(self, hide_final_grades):
        """
        Sets the hide_final_grades of this Course.


        :param hide_final_grades: The hide_final_grades of this Course.
        :type: bool
        """

        self._hide_final_grades = hide_final_grades

    @property
    def license(self):
        """
        Gets the license of this Course.


        :return: The license of this Course.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this Course.


        :param license: The license of this Course.
        :type: str
        """

        self._license = license

    @property
    def allow_student_assignment_edits(self):
        """
        Gets the allow_student_assignment_edits of this Course.


        :return: The allow_student_assignment_edits of this Course.
        :rtype: bool
        """
        return self._allow_student_assignment_edits

    @allow_student_assignment_edits.setter
    def allow_student_assignment_edits(self, allow_student_assignment_edits):
        """
        Sets the allow_student_assignment_edits of this Course.


        :param allow_student_assignment_edits: The allow_student_assignment_edits of this Course.
        :type: bool
        """

        self._allow_student_assignment_edits = allow_student_assignment_edits

    @property
    def allow_wiki_comments(self):
        """
        Gets the allow_wiki_comments of this Course.


        :return: The allow_wiki_comments of this Course.
        :rtype: bool
        """
        return self._allow_wiki_comments

    @allow_wiki_comments.setter
    def allow_wiki_comments(self, allow_wiki_comments):
        """
        Sets the allow_wiki_comments of this Course.


        :param allow_wiki_comments: The allow_wiki_comments of this Course.
        :type: bool
        """

        self._allow_wiki_comments = allow_wiki_comments

    @property
    def allow_student_forum_attachments(self):
        """
        Gets the allow_student_forum_attachments of this Course.


        :return: The allow_student_forum_attachments of this Course.
        :rtype: bool
        """
        return self._allow_student_forum_attachments

    @allow_student_forum_attachments.setter
    def allow_student_forum_attachments(self, allow_student_forum_attachments):
        """
        Sets the allow_student_forum_attachments of this Course.


        :param allow_student_forum_attachments: The allow_student_forum_attachments of this Course.
        :type: bool
        """

        self._allow_student_forum_attachments = allow_student_forum_attachments

    @property
    def open_enrollment(self):
        """
        Gets the open_enrollment of this Course.


        :return: The open_enrollment of this Course.
        :rtype: bool
        """
        return self._open_enrollment

    @open_enrollment.setter
    def open_enrollment(self, open_enrollment):
        """
        Sets the open_enrollment of this Course.


        :param open_enrollment: The open_enrollment of this Course.
        :type: bool
        """

        self._open_enrollment = open_enrollment

    @property
    def self_enrollment(self):
        """
        Gets the self_enrollment of this Course.


        :return: The self_enrollment of this Course.
        :rtype: bool
        """
        return self._self_enrollment

    @self_enrollment.setter
    def self_enrollment(self, self_enrollment):
        """
        Sets the self_enrollment of this Course.


        :param self_enrollment: The self_enrollment of this Course.
        :type: bool
        """

        self._self_enrollment = self_enrollment

    @property
    def restrict_enrollments_to_course_dates(self):
        """
        Gets the restrict_enrollments_to_course_dates of this Course.


        :return: The restrict_enrollments_to_course_dates of this Course.
        :rtype: bool
        """
        return self._restrict_enrollments_to_course_dates

    @restrict_enrollments_to_course_dates.setter
    def restrict_enrollments_to_course_dates(self, restrict_enrollments_to_course_dates):
        """
        Sets the restrict_enrollments_to_course_dates of this Course.


        :param restrict_enrollments_to_course_dates: The restrict_enrollments_to_course_dates of this Course.
        :type: bool
        """

        self._restrict_enrollments_to_course_dates = restrict_enrollments_to_course_dates

    @property
    def course_format(self):
        """
        Gets the course_format of this Course.


        :return: The course_format of this Course.
        :rtype: str
        """
        return self._course_format

    @course_format.setter
    def course_format(self, course_format):
        """
        Sets the course_format of this Course.


        :param course_format: The course_format of this Course.
        :type: str
        """

        self._course_format = course_format

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
