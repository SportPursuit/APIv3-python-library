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


class DeleteHardbounces(object):
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
        'start_date': 'date',
        'end_date': 'date',
        'contact_email': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'contact_email': 'contactEmail'
    }

    def __init__(self, start_date=None, end_date=None, contact_email=None):
        """
        DeleteHardbounces - a model defined in Swagger
        """

        self._start_date = None
        self._end_date = None
        self._contact_email = None

        if start_date is not None:
          self.start_date = start_date
        if end_date is not None:
          self.end_date = end_date
        if contact_email is not None:
          self.contact_email = contact_email

    @property
    def start_date(self):
        """
        Gets the start_date of this DeleteHardbounces.
        Starting date (YYYY-MM-DD) of the period from which the hardbounces will be deleted. Must be lower than equal to endDate

        :return: The start_date of this DeleteHardbounces.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this DeleteHardbounces.
        Starting date (YYYY-MM-DD) of the period from which the hardbounces will be deleted. Must be lower than equal to endDate

        :param start_date: The start_date of this DeleteHardbounces.
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this DeleteHardbounces.
        Ending date (YYYY-MM-DD) of the period from which the hardbounces will be deleted. Must be greater than equal to startDate

        :return: The end_date of this DeleteHardbounces.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this DeleteHardbounces.
        Ending date (YYYY-MM-DD) of the period from which the hardbounces will be deleted. Must be greater than equal to startDate

        :param end_date: The end_date of this DeleteHardbounces.
        :type: date
        """

        self._end_date = end_date

    @property
    def contact_email(self):
        """
        Gets the contact_email of this DeleteHardbounces.
        Target a specific email address

        :return: The contact_email of this DeleteHardbounces.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """
        Sets the contact_email of this DeleteHardbounces.
        Target a specific email address

        :param contact_email: The contact_email of this DeleteHardbounces.
        :type: str
        """

        self._contact_email = contact_email

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
        if not isinstance(other, DeleteHardbounces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
