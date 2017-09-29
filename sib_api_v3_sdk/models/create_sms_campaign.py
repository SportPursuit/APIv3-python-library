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


class CreateSmsCampaign(object):
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
        'sender': 'str',
        'content': 'str',
        'recipients': 'CreateSmsCampaignRecipients',
        'scheduled_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'sender': 'sender',
        'content': 'content',
        'recipients': 'recipients',
        'scheduled_at': 'scheduledAt'
    }

    def __init__(self, name=None, sender=None, content=None, recipients=None, scheduled_at=None):
        """
        CreateSmsCampaign - a model defined in Swagger
        """

        self._name = None
        self._sender = None
        self._content = None
        self._recipients = None
        self._scheduled_at = None

        self.name = name
        self.sender = sender
        if content is not None:
          self.content = content
        if recipients is not None:
          self.recipients = recipients
        if scheduled_at is not None:
          self.scheduled_at = scheduled_at

    @property
    def name(self):
        """
        Gets the name of this CreateSmsCampaign.
        Name of the campaign

        :return: The name of this CreateSmsCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateSmsCampaign.
        Name of the campaign

        :param name: The name of this CreateSmsCampaign.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def sender(self):
        """
        Gets the sender of this CreateSmsCampaign.
        Name of the sender. The number of characters is limited to 11

        :return: The sender of this CreateSmsCampaign.
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this CreateSmsCampaign.
        Name of the sender. The number of characters is limited to 11

        :param sender: The sender of this CreateSmsCampaign.
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")
        if sender is not None and len(sender) > 11:
            raise ValueError("Invalid value for `sender`, length must be less than or equal to `11`")

        self._sender = sender

    @property
    def content(self):
        """
        Gets the content of this CreateSmsCampaign.
        Content of the message. The maximum characters used per SMS is 160, if used more than that, it will be counted as more than one SMS

        :return: The content of this CreateSmsCampaign.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CreateSmsCampaign.
        Content of the message. The maximum characters used per SMS is 160, if used more than that, it will be counted as more than one SMS

        :param content: The content of this CreateSmsCampaign.
        :type: str
        """

        self._content = content

    @property
    def recipients(self):
        """
        Gets the recipients of this CreateSmsCampaign.

        :return: The recipients of this CreateSmsCampaign.
        :rtype: CreateSmsCampaignRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this CreateSmsCampaign.

        :param recipients: The recipients of this CreateSmsCampaign.
        :type: CreateSmsCampaignRecipients
        """

        self._recipients = recipients

    @property
    def scheduled_at(self):
        """
        Gets the scheduled_at of this CreateSmsCampaign.
        Date and time on which the campaign has to run (YYYY-MM-DDTHH:mm:ss.SSSZ)

        :return: The scheduled_at of this CreateSmsCampaign.
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """
        Sets the scheduled_at of this CreateSmsCampaign.
        Date and time on which the campaign has to run (YYYY-MM-DDTHH:mm:ss.SSSZ)

        :param scheduled_at: The scheduled_at of this CreateSmsCampaign.
        :type: datetime
        """

        self._scheduled_at = scheduled_at

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
        if not isinstance(other, CreateSmsCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
