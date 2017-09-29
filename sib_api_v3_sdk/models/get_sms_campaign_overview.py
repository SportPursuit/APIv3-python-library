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


class GetSmsCampaignOverview(object):
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
        'id': 'int',
        'name': 'str',
        'status': 'str',
        'content': 'str',
        'scheduled_at': 'datetime',
        'test_sent': 'bool',
        'sender': 'str',
        'created_at': 'datetime',
        'modified_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'content': 'content',
        'scheduled_at': 'scheduledAt',
        'test_sent': 'testSent',
        'sender': 'sender',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, id=None, name=None, status=None, content=None, scheduled_at=None, test_sent=None, sender=None, created_at=None, modified_at=None):
        """
        GetSmsCampaignOverview - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._status = None
        self._content = None
        self._scheduled_at = None
        self._test_sent = None
        self._sender = None
        self._created_at = None
        self._modified_at = None

        self.id = id
        self.name = name
        self.status = status
        self.content = content
        self.scheduled_at = scheduled_at
        self.test_sent = test_sent
        self.sender = sender
        self.created_at = created_at
        self.modified_at = modified_at

    @property
    def id(self):
        """
        Gets the id of this GetSmsCampaignOverview.
        ID of the SMS Campaign

        :return: The id of this GetSmsCampaignOverview.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetSmsCampaignOverview.
        ID of the SMS Campaign

        :param id: The id of this GetSmsCampaignOverview.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GetSmsCampaignOverview.
        Name of the SMS Campaign

        :return: The name of this GetSmsCampaignOverview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetSmsCampaignOverview.
        Name of the SMS Campaign

        :param name: The name of this GetSmsCampaignOverview.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this GetSmsCampaignOverview.
        Status of the SMS Campaign

        :return: The status of this GetSmsCampaignOverview.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this GetSmsCampaignOverview.
        Status of the SMS Campaign

        :param status: The status of this GetSmsCampaignOverview.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["draft", "sent", "archive", "queued", "suspended", "in_process"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def content(self):
        """
        Gets the content of this GetSmsCampaignOverview.
        Content of the SMS Campaign

        :return: The content of this GetSmsCampaignOverview.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this GetSmsCampaignOverview.
        Content of the SMS Campaign

        :param content: The content of this GetSmsCampaignOverview.
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")

        self._content = content

    @property
    def scheduled_at(self):
        """
        Gets the scheduled_at of this GetSmsCampaignOverview.
        Date on which SMS campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format

        :return: The scheduled_at of this GetSmsCampaignOverview.
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """
        Sets the scheduled_at of this GetSmsCampaignOverview.
        Date on which SMS campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format

        :param scheduled_at: The scheduled_at of this GetSmsCampaignOverview.
        :type: datetime
        """
        if scheduled_at is None:
            raise ValueError("Invalid value for `scheduled_at`, must not be `None`")

        self._scheduled_at = scheduled_at

    @property
    def test_sent(self):
        """
        Gets the test_sent of this GetSmsCampaignOverview.
        Retrieved the status of test SMS sending. (true=Test SMS has been sent  false=Test SMS has not been sent)

        :return: The test_sent of this GetSmsCampaignOverview.
        :rtype: bool
        """
        return self._test_sent

    @test_sent.setter
    def test_sent(self, test_sent):
        """
        Sets the test_sent of this GetSmsCampaignOverview.
        Retrieved the status of test SMS sending. (true=Test SMS has been sent  false=Test SMS has not been sent)

        :param test_sent: The test_sent of this GetSmsCampaignOverview.
        :type: bool
        """
        if test_sent is None:
            raise ValueError("Invalid value for `test_sent`, must not be `None`")

        self._test_sent = test_sent

    @property
    def sender(self):
        """
        Gets the sender of this GetSmsCampaignOverview.
        Sender of the SMS Campaign

        :return: The sender of this GetSmsCampaignOverview.
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this GetSmsCampaignOverview.
        Sender of the SMS Campaign

        :param sender: The sender of this GetSmsCampaignOverview.
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")

        self._sender = sender

    @property
    def created_at(self):
        """
        Gets the created_at of this GetSmsCampaignOverview.
        Creation date of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)

        :return: The created_at of this GetSmsCampaignOverview.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this GetSmsCampaignOverview.
        Creation date of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)

        :param created_at: The created_at of this GetSmsCampaignOverview.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this GetSmsCampaignOverview.
        Date of last modification of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)

        :return: The modified_at of this GetSmsCampaignOverview.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this GetSmsCampaignOverview.
        Date of last modification of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)

        :param modified_at: The modified_at of this GetSmsCampaignOverview.
        :type: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")

        self._modified_at = modified_at

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
        if not isinstance(other, GetSmsCampaignOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
