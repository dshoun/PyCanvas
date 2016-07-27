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


class DiscussionTopic(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, message=None, html_url=None, posted_at=None, last_reply_at=None, require_initial_post=None, user_can_see_posts=None, discussion_subentry_count=None, read_state=None, unread_count=None, subscribed=None, subscription_hold=None, assignment_id=None, delayed_post_at=None, published=None, lock_at=None, locked=None, pinned=None, locked_for_user=None, lock_info=None, lock_explanation=None, user_name=None, topic_children=None, root_topic_id=None, podcast_url=None, discussion_type=None, group_category_id=None, attachments=None, permissions=None):
        """
        DiscussionTopic - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'title': 'str',
            'message': 'str',
            'html_url': 'str',
            'posted_at': 'Datetime',
            'last_reply_at': 'Datetime',
            'require_initial_post': 'bool',
            'user_can_see_posts': 'bool',
            'discussion_subentry_count': 'int',
            'read_state': 'str',
            'unread_count': 'int',
            'subscribed': 'bool',
            'subscription_hold': 'str',
            'assignment_id': 'int',
            'delayed_post_at': 'Datetime',
            'published': 'bool',
            'lock_at': 'Datetime',
            'locked': 'bool',
            'pinned': 'bool',
            'locked_for_user': 'bool',
            'lock_info': 'LockInfo',
            'lock_explanation': 'str',
            'user_name': 'str',
            'topic_children': 'list[int]',
            'root_topic_id': 'int',
            'podcast_url': 'str',
            'discussion_type': 'str',
            'group_category_id': 'int',
            'attachments': 'list[FileAttachment]',
            'permissions': 'dict'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'message': 'message',
            'html_url': 'html_url',
            'posted_at': 'posted_at',
            'last_reply_at': 'last_reply_at',
            'require_initial_post': 'require_initial_post',
            'user_can_see_posts': 'user_can_see_posts',
            'discussion_subentry_count': 'discussion_subentry_count',
            'read_state': 'read_state',
            'unread_count': 'unread_count',
            'subscribed': 'subscribed',
            'subscription_hold': 'subscription_hold',
            'assignment_id': 'assignment_id',
            'delayed_post_at': 'delayed_post_at',
            'published': 'published',
            'lock_at': 'lock_at',
            'locked': 'locked',
            'pinned': 'pinned',
            'locked_for_user': 'locked_for_user',
            'lock_info': 'lock_info',
            'lock_explanation': 'lock_explanation',
            'user_name': 'user_name',
            'topic_children': 'topic_children',
            'root_topic_id': 'root_topic_id',
            'podcast_url': 'podcast_url',
            'discussion_type': 'discussion_type',
            'group_category_id': 'group_category_id',
            'attachments': 'attachments',
            'permissions': 'permissions'
        }

        self._id = id
        self._title = title
        self._message = message
        self._html_url = html_url
        self._posted_at = posted_at
        self._last_reply_at = last_reply_at
        self._require_initial_post = require_initial_post
        self._user_can_see_posts = user_can_see_posts
        self._discussion_subentry_count = discussion_subentry_count
        self._read_state = read_state
        self._unread_count = unread_count
        self._subscribed = subscribed
        self._subscription_hold = subscription_hold
        self._assignment_id = assignment_id
        self._delayed_post_at = delayed_post_at
        self._published = published
        self._lock_at = lock_at
        self._locked = locked
        self._pinned = pinned
        self._locked_for_user = locked_for_user
        self._lock_info = lock_info
        self._lock_explanation = lock_explanation
        self._user_name = user_name
        self._topic_children = topic_children
        self._root_topic_id = root_topic_id
        self._podcast_url = podcast_url
        self._discussion_type = discussion_type
        self._group_category_id = group_category_id
        self._attachments = attachments
        self._permissions = permissions

    @property
    def id(self):
        """
        Gets the id of this DiscussionTopic.
        The ID of this topic.

        :return: The id of this DiscussionTopic.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DiscussionTopic.
        The ID of this topic.

        :param id: The id of this DiscussionTopic.
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this DiscussionTopic.
        The topic title.

        :return: The title of this DiscussionTopic.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this DiscussionTopic.
        The topic title.

        :param title: The title of this DiscussionTopic.
        :type: str
        """

        self._title = title

    @property
    def message(self):
        """
        Gets the message of this DiscussionTopic.
        The HTML content of the message body.

        :return: The message of this DiscussionTopic.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this DiscussionTopic.
        The HTML content of the message body.

        :param message: The message of this DiscussionTopic.
        :type: str
        """

        self._message = message

    @property
    def html_url(self):
        """
        Gets the html_url of this DiscussionTopic.
        The URL to the discussion topic in canvas.

        :return: The html_url of this DiscussionTopic.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this DiscussionTopic.
        The URL to the discussion topic in canvas.

        :param html_url: The html_url of this DiscussionTopic.
        :type: str
        """

        self._html_url = html_url

    @property
    def posted_at(self):
        """
        Gets the posted_at of this DiscussionTopic.
        The datetime the topic was posted. If it is null it hasn't been posted yet. (see delayed_post_at)

        :return: The posted_at of this DiscussionTopic.
        :rtype: Datetime
        """
        return self._posted_at

    @posted_at.setter
    def posted_at(self, posted_at):
        """
        Sets the posted_at of this DiscussionTopic.
        The datetime the topic was posted. If it is null it hasn't been posted yet. (see delayed_post_at)

        :param posted_at: The posted_at of this DiscussionTopic.
        :type: Datetime
        """

        self._posted_at = posted_at

    @property
    def last_reply_at(self):
        """
        Gets the last_reply_at of this DiscussionTopic.
        The datetime for when the last reply was in the topic.

        :return: The last_reply_at of this DiscussionTopic.
        :rtype: Datetime
        """
        return self._last_reply_at

    @last_reply_at.setter
    def last_reply_at(self, last_reply_at):
        """
        Sets the last_reply_at of this DiscussionTopic.
        The datetime for when the last reply was in the topic.

        :param last_reply_at: The last_reply_at of this DiscussionTopic.
        :type: Datetime
        """

        self._last_reply_at = last_reply_at

    @property
    def require_initial_post(self):
        """
        Gets the require_initial_post of this DiscussionTopic.
        If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.

        :return: The require_initial_post of this DiscussionTopic.
        :rtype: bool
        """
        return self._require_initial_post

    @require_initial_post.setter
    def require_initial_post(self, require_initial_post):
        """
        Sets the require_initial_post of this DiscussionTopic.
        If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.

        :param require_initial_post: The require_initial_post of this DiscussionTopic.
        :type: bool
        """

        self._require_initial_post = require_initial_post

    @property
    def user_can_see_posts(self):
        """
        Gets the user_can_see_posts of this DiscussionTopic.
        Whether or not posts in this topic are visible to the user.

        :return: The user_can_see_posts of this DiscussionTopic.
        :rtype: bool
        """
        return self._user_can_see_posts

    @user_can_see_posts.setter
    def user_can_see_posts(self, user_can_see_posts):
        """
        Sets the user_can_see_posts of this DiscussionTopic.
        Whether or not posts in this topic are visible to the user.

        :param user_can_see_posts: The user_can_see_posts of this DiscussionTopic.
        :type: bool
        """

        self._user_can_see_posts = user_can_see_posts

    @property
    def discussion_subentry_count(self):
        """
        Gets the discussion_subentry_count of this DiscussionTopic.
        The count of entries in the topic.

        :return: The discussion_subentry_count of this DiscussionTopic.
        :rtype: int
        """
        return self._discussion_subentry_count

    @discussion_subentry_count.setter
    def discussion_subentry_count(self, discussion_subentry_count):
        """
        Sets the discussion_subentry_count of this DiscussionTopic.
        The count of entries in the topic.

        :param discussion_subentry_count: The discussion_subentry_count of this DiscussionTopic.
        :type: int
        """

        self._discussion_subentry_count = discussion_subentry_count

    @property
    def read_state(self):
        """
        Gets the read_state of this DiscussionTopic.
        The read_state of the topic for the current user, 'read' or 'unread'.

        :return: The read_state of this DiscussionTopic.
        :rtype: str
        """
        return self._read_state

    @read_state.setter
    def read_state(self, read_state):
        """
        Sets the read_state of this DiscussionTopic.
        The read_state of the topic for the current user, 'read' or 'unread'.

        :param read_state: The read_state of this DiscussionTopic.
        :type: str
        """

        self._read_state = read_state

    @property
    def unread_count(self):
        """
        Gets the unread_count of this DiscussionTopic.
        The count of unread entries of this topic for the current user.

        :return: The unread_count of this DiscussionTopic.
        :rtype: int
        """
        return self._unread_count

    @unread_count.setter
    def unread_count(self, unread_count):
        """
        Sets the unread_count of this DiscussionTopic.
        The count of unread entries of this topic for the current user.

        :param unread_count: The unread_count of this DiscussionTopic.
        :type: int
        """

        self._unread_count = unread_count

    @property
    def subscribed(self):
        """
        Gets the subscribed of this DiscussionTopic.
        Whether or not the current user is subscribed to this topic.

        :return: The subscribed of this DiscussionTopic.
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """
        Sets the subscribed of this DiscussionTopic.
        Whether or not the current user is subscribed to this topic.

        :param subscribed: The subscribed of this DiscussionTopic.
        :type: bool
        """

        self._subscribed = subscribed

    @property
    def subscription_hold(self):
        """
        Gets the subscription_hold of this DiscussionTopic.
        (Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: 'initial_post_required': The user must post a reply first 'not_in_group_set': The user is not in the group set for this graded group discussion 'not_in_group': The user is not in this topic's group 'topic_is_announcement': This topic is an announcement

        :return: The subscription_hold of this DiscussionTopic.
        :rtype: str
        """
        return self._subscription_hold

    @subscription_hold.setter
    def subscription_hold(self, subscription_hold):
        """
        Sets the subscription_hold of this DiscussionTopic.
        (Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: 'initial_post_required': The user must post a reply first 'not_in_group_set': The user is not in the group set for this graded group discussion 'not_in_group': The user is not in this topic's group 'topic_is_announcement': This topic is an announcement

        :param subscription_hold: The subscription_hold of this DiscussionTopic.
        :type: str
        """

        self._subscription_hold = subscription_hold

    @property
    def assignment_id(self):
        """
        Gets the assignment_id of this DiscussionTopic.
        The unique identifier of the assignment if the topic is for grading, otherwise null.

        :return: The assignment_id of this DiscussionTopic.
        :rtype: int
        """
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        """
        Sets the assignment_id of this DiscussionTopic.
        The unique identifier of the assignment if the topic is for grading, otherwise null.

        :param assignment_id: The assignment_id of this DiscussionTopic.
        :type: int
        """

        self._assignment_id = assignment_id

    @property
    def delayed_post_at(self):
        """
        Gets the delayed_post_at of this DiscussionTopic.
        The datetime to publish the topic (if not right away).

        :return: The delayed_post_at of this DiscussionTopic.
        :rtype: Datetime
        """
        return self._delayed_post_at

    @delayed_post_at.setter
    def delayed_post_at(self, delayed_post_at):
        """
        Sets the delayed_post_at of this DiscussionTopic.
        The datetime to publish the topic (if not right away).

        :param delayed_post_at: The delayed_post_at of this DiscussionTopic.
        :type: Datetime
        """

        self._delayed_post_at = delayed_post_at

    @property
    def published(self):
        """
        Gets the published of this DiscussionTopic.
        Whether this discussion topic is published (true) or draft state (false)

        :return: The published of this DiscussionTopic.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this DiscussionTopic.
        Whether this discussion topic is published (true) or draft state (false)

        :param published: The published of this DiscussionTopic.
        :type: bool
        """

        self._published = published

    @property
    def lock_at(self):
        """
        Gets the lock_at of this DiscussionTopic.
        The datetime to lock the topic (if ever).

        :return: The lock_at of this DiscussionTopic.
        :rtype: Datetime
        """
        return self._lock_at

    @lock_at.setter
    def lock_at(self, lock_at):
        """
        Sets the lock_at of this DiscussionTopic.
        The datetime to lock the topic (if ever).

        :param lock_at: The lock_at of this DiscussionTopic.
        :type: Datetime
        """

        self._lock_at = lock_at

    @property
    def locked(self):
        """
        Gets the locked of this DiscussionTopic.
        Whether or not the discussion is 'closed for comments'.

        :return: The locked of this DiscussionTopic.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this DiscussionTopic.
        Whether or not the discussion is 'closed for comments'.

        :param locked: The locked of this DiscussionTopic.
        :type: bool
        """

        self._locked = locked

    @property
    def pinned(self):
        """
        Gets the pinned of this DiscussionTopic.
        Whether or not the discussion has been 'pinned' by an instructor

        :return: The pinned of this DiscussionTopic.
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """
        Sets the pinned of this DiscussionTopic.
        Whether or not the discussion has been 'pinned' by an instructor

        :param pinned: The pinned of this DiscussionTopic.
        :type: bool
        """

        self._pinned = pinned

    @property
    def locked_for_user(self):
        """
        Gets the locked_for_user of this DiscussionTopic.
        Whether or not this is locked for the user.

        :return: The locked_for_user of this DiscussionTopic.
        :rtype: bool
        """
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, locked_for_user):
        """
        Sets the locked_for_user of this DiscussionTopic.
        Whether or not this is locked for the user.

        :param locked_for_user: The locked_for_user of this DiscussionTopic.
        :type: bool
        """

        self._locked_for_user = locked_for_user

    @property
    def lock_info(self):
        """
        Gets the lock_info of this DiscussionTopic.
        (Optional) Information for the user about the lock. Present when locked_for_user is true.

        :return: The lock_info of this DiscussionTopic.
        :rtype: LockInfo
        """
        return self._lock_info

    @lock_info.setter
    def lock_info(self, lock_info):
        """
        Sets the lock_info of this DiscussionTopic.
        (Optional) Information for the user about the lock. Present when locked_for_user is true.

        :param lock_info: The lock_info of this DiscussionTopic.
        :type: LockInfo
        """

        self._lock_info = lock_info

    @property
    def lock_explanation(self):
        """
        Gets the lock_explanation of this DiscussionTopic.
        (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true.

        :return: The lock_explanation of this DiscussionTopic.
        :rtype: str
        """
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, lock_explanation):
        """
        Sets the lock_explanation of this DiscussionTopic.
        (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true.

        :param lock_explanation: The lock_explanation of this DiscussionTopic.
        :type: str
        """

        self._lock_explanation = lock_explanation

    @property
    def user_name(self):
        """
        Gets the user_name of this DiscussionTopic.
        The username of the topic creator.

        :return: The user_name of this DiscussionTopic.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DiscussionTopic.
        The username of the topic creator.

        :param user_name: The user_name of this DiscussionTopic.
        :type: str
        """

        self._user_name = user_name

    @property
    def topic_children(self):
        """
        Gets the topic_children of this DiscussionTopic.
        An array of topic_ids for the group discussions the user is a part of.

        :return: The topic_children of this DiscussionTopic.
        :rtype: list[int]
        """
        return self._topic_children

    @topic_children.setter
    def topic_children(self, topic_children):
        """
        Sets the topic_children of this DiscussionTopic.
        An array of topic_ids for the group discussions the user is a part of.

        :param topic_children: The topic_children of this DiscussionTopic.
        :type: list[int]
        """

        self._topic_children = topic_children

    @property
    def root_topic_id(self):
        """
        Gets the root_topic_id of this DiscussionTopic.
        If the topic is for grading and a group assignment this will point to the original topic in the course.

        :return: The root_topic_id of this DiscussionTopic.
        :rtype: int
        """
        return self._root_topic_id

    @root_topic_id.setter
    def root_topic_id(self, root_topic_id):
        """
        Sets the root_topic_id of this DiscussionTopic.
        If the topic is for grading and a group assignment this will point to the original topic in the course.

        :param root_topic_id: The root_topic_id of this DiscussionTopic.
        :type: int
        """

        self._root_topic_id = root_topic_id

    @property
    def podcast_url(self):
        """
        Gets the podcast_url of this DiscussionTopic.
        If the topic is a podcast topic this is the feed url for the current user.

        :return: The podcast_url of this DiscussionTopic.
        :rtype: str
        """
        return self._podcast_url

    @podcast_url.setter
    def podcast_url(self, podcast_url):
        """
        Sets the podcast_url of this DiscussionTopic.
        If the topic is a podcast topic this is the feed url for the current user.

        :param podcast_url: The podcast_url of this DiscussionTopic.
        :type: str
        """

        self._podcast_url = podcast_url

    @property
    def discussion_type(self):
        """
        Gets the discussion_type of this DiscussionTopic.
        The type of discussion. Values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions.

        :return: The discussion_type of this DiscussionTopic.
        :rtype: str
        """
        return self._discussion_type

    @discussion_type.setter
    def discussion_type(self, discussion_type):
        """
        Sets the discussion_type of this DiscussionTopic.
        The type of discussion. Values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions.

        :param discussion_type: The discussion_type of this DiscussionTopic.
        :type: str
        """

        self._discussion_type = discussion_type

    @property
    def group_category_id(self):
        """
        Gets the group_category_id of this DiscussionTopic.
        The unique identifier of the group category if the topic is a group discussion, otherwise null.

        :return: The group_category_id of this DiscussionTopic.
        :rtype: int
        """
        return self._group_category_id

    @group_category_id.setter
    def group_category_id(self, group_category_id):
        """
        Sets the group_category_id of this DiscussionTopic.
        The unique identifier of the group category if the topic is a group discussion, otherwise null.

        :param group_category_id: The group_category_id of this DiscussionTopic.
        :type: int
        """

        self._group_category_id = group_category_id

    @property
    def attachments(self):
        """
        Gets the attachments of this DiscussionTopic.
        Array of file attachments.

        :return: The attachments of this DiscussionTopic.
        :rtype: list[FileAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this DiscussionTopic.
        Array of file attachments.

        :param attachments: The attachments of this DiscussionTopic.
        :type: list[FileAttachment]
        """

        self._attachments = attachments

    @property
    def permissions(self):
        """
        Gets the permissions of this DiscussionTopic.
        The current user's permissions on this topic.

        :return: The permissions of this DiscussionTopic.
        :rtype: dict
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this DiscussionTopic.
        The current user's permissions on this topic.

        :param permissions: The permissions of this DiscussionTopic.
        :type: dict
        """

        self._permissions = permissions

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