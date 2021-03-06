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


class GetAccount(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'company_name': 'str',
        'address': 'GetExtendedClientAddress',
        'plan': 'list[GetAccountPlan]',
        'relay': 'GetAccountRelay',
        'marketing_automation': 'GetAccountMarketingAutomation'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company_name': 'companyName',
        'address': 'address',
        'plan': 'plan',
        'relay': 'relay',
        'marketing_automation': 'marketingAutomation'
    }

    def __init__(self, email=None, first_name=None, last_name=None, company_name=None, address=None, plan=None, relay=None, marketing_automation=None):
        """
        GetAccount - a model defined in Swagger
        """

        self._email = None
        self._first_name = None
        self._last_name = None
        self._company_name = None
        self._address = None
        self._plan = None
        self._relay = None
        self._marketing_automation = None

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        if address is not None:
          self.address = address
        self.plan = plan
        if relay is not None:
          self.relay = relay
        if marketing_automation is not None:
          self.marketing_automation = marketing_automation

    @property
    def email(self):
        """
        Gets the email of this GetAccount.
        Login Email

        :return: The email of this GetAccount.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this GetAccount.
        Login Email

        :param email: The email of this GetAccount.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this GetAccount.
        First Name

        :return: The first_name of this GetAccount.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this GetAccount.
        First Name

        :param first_name: The first_name of this GetAccount.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this GetAccount.
        Last Name

        :return: The last_name of this GetAccount.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this GetAccount.
        Last Name

        :param last_name: The last_name of this GetAccount.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def company_name(self):
        """
        Gets the company_name of this GetAccount.
        Name of the company

        :return: The company_name of this GetAccount.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this GetAccount.
        Name of the company

        :param company_name: The company_name of this GetAccount.
        :type: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")

        self._company_name = company_name

    @property
    def address(self):
        """
        Gets the address of this GetAccount.

        :return: The address of this GetAccount.
        :rtype: GetExtendedClientAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this GetAccount.

        :param address: The address of this GetAccount.
        :type: GetExtendedClientAddress
        """

        self._address = address

    @property
    def plan(self):
        """
        Gets the plan of this GetAccount.
        Information about your plans and credits

        :return: The plan of this GetAccount.
        :rtype: list[GetAccountPlan]
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """
        Sets the plan of this GetAccount.
        Information about your plans and credits

        :param plan: The plan of this GetAccount.
        :type: list[GetAccountPlan]
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")

        self._plan = plan

    @property
    def relay(self):
        """
        Gets the relay of this GetAccount.

        :return: The relay of this GetAccount.
        :rtype: GetAccountRelay
        """
        return self._relay

    @relay.setter
    def relay(self, relay):
        """
        Sets the relay of this GetAccount.

        :param relay: The relay of this GetAccount.
        :type: GetAccountRelay
        """

        self._relay = relay

    @property
    def marketing_automation(self):
        """
        Gets the marketing_automation of this GetAccount.

        :return: The marketing_automation of this GetAccount.
        :rtype: GetAccountMarketingAutomation
        """
        return self._marketing_automation

    @marketing_automation.setter
    def marketing_automation(self, marketing_automation):
        """
        Sets the marketing_automation of this GetAccount.

        :param marketing_automation: The marketing_automation of this GetAccount.
        :type: GetAccountMarketingAutomation
        """

        self._marketing_automation = marketing_automation

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
        if not isinstance(other, GetAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
