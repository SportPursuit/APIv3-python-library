# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetLists(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'lists': 'list[object]',
        'count': 'int'
    }

    attribute_map = {
        'lists': 'lists',
        'count': 'count'
    }

    def __init__(self, lists=None, count=None):
        """
        GetLists - a model defined in Swagger
        """

        self._lists = None
        self._count = None

        self.lists = lists
        self.count = count

    @property
    def lists(self):
        """
        Gets the lists of this GetLists.
        Listing of all the lists available in your account

        :return: The lists of this GetLists.
        :rtype: list[object]
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """
        Sets the lists of this GetLists.
        Listing of all the lists available in your account

        :param lists: The lists of this GetLists.
        :type: list[object]
        """
        if lists is None:
            raise ValueError("Invalid value for `lists`, must not be `None`")

        self._lists = lists

    @property
    def count(self):
        """
        Gets the count of this GetLists.
        Number of lists in your account

        :return: The count of this GetLists.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this GetLists.
        Number of lists in your account

        :param count: The count of this GetLists.
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")

        self._count = count

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
        if not isinstance(other, GetLists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
