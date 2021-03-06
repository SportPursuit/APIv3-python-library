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


class GetAttributesAttributes(object):
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
        'name': 'str',
        'category': 'str',
        'type': 'str',
        'enumeration': 'list[GetAttributesEnumeration]',
        'calculated_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'category': 'category',
        'type': 'type',
        'enumeration': 'enumeration',
        'calculated_value': 'calculatedValue'
    }

    def __init__(self, name=None, category=None, type=None, enumeration=None, calculated_value=None):
        """
        GetAttributesAttributes - a model defined in Swagger
        """

        self._name = None
        self._category = None
        self._type = None
        self._enumeration = None
        self._calculated_value = None

        self.name = name
        self.category = category
        if type is not None:
          self.type = type
        if enumeration is not None:
          self.enumeration = enumeration
        if calculated_value is not None:
          self.calculated_value = calculated_value

    @property
    def name(self):
        """
        Gets the name of this GetAttributesAttributes.
        Name of the attribute

        :return: The name of this GetAttributesAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetAttributesAttributes.
        Name of the attribute

        :param name: The name of this GetAttributesAttributes.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def category(self):
        """
        Gets the category of this GetAttributesAttributes.
        Category of the attribute

        :return: The category of this GetAttributesAttributes.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this GetAttributesAttributes.
        Category of the attribute

        :param category: The category of this GetAttributesAttributes.
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")
        allowed_values = ["normal", "transactional", "category", "calculated", "global"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def type(self):
        """
        Gets the type of this GetAttributesAttributes.
        Type of the attribute

        :return: The type of this GetAttributesAttributes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GetAttributesAttributes.
        Type of the attribute

        :param type: The type of this GetAttributesAttributes.
        :type: str
        """
        allowed_values = ["text", "date", "float", "id"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def enumeration(self):
        """
        Gets the enumeration of this GetAttributesAttributes.
        Parameter only available for \"category\" type attributes.

        :return: The enumeration of this GetAttributesAttributes.
        :rtype: list[GetAttributesEnumeration]
        """
        return self._enumeration

    @enumeration.setter
    def enumeration(self, enumeration):
        """
        Sets the enumeration of this GetAttributesAttributes.
        Parameter only available for \"category\" type attributes.

        :param enumeration: The enumeration of this GetAttributesAttributes.
        :type: list[GetAttributesEnumeration]
        """

        self._enumeration = enumeration

    @property
    def calculated_value(self):
        """
        Gets the calculated_value of this GetAttributesAttributes.
        Calculated value formula

        :return: The calculated_value of this GetAttributesAttributes.
        :rtype: str
        """
        return self._calculated_value

    @calculated_value.setter
    def calculated_value(self, calculated_value):
        """
        Sets the calculated_value of this GetAttributesAttributes.
        Calculated value formula

        :param calculated_value: The calculated_value of this GetAttributesAttributes.
        :type: str
        """

        self._calculated_value = calculated_value

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
        if not isinstance(other, GetAttributesAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
