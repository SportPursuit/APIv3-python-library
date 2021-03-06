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


class RequestContactExport(object):
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
        'export_attributes': 'list[str]',
        'contact_filter': 'object',
        'notify_url': 'str'
    }

    attribute_map = {
        'export_attributes': 'exportAttributes',
        'contact_filter': 'contactFilter',
        'notify_url': 'notifyUrl'
    }

    def __init__(self, export_attributes=None, contact_filter=None, notify_url=None):
        """
        RequestContactExport - a model defined in Swagger
        """

        self._export_attributes = None
        self._contact_filter = None
        self._notify_url = None

        if export_attributes is not None:
          self.export_attributes = export_attributes
        self.contact_filter = contact_filter
        if notify_url is not None:
          self.notify_url = notify_url

    @property
    def export_attributes(self):
        """
        Gets the export_attributes of this RequestContactExport.
        Name of attributes to export. These attributes must be in your contact database

        :return: The export_attributes of this RequestContactExport.
        :rtype: list[str]
        """
        return self._export_attributes

    @export_attributes.setter
    def export_attributes(self, export_attributes):
        """
        Sets the export_attributes of this RequestContactExport.
        Name of attributes to export. These attributes must be in your contact database

        :param export_attributes: The export_attributes of this RequestContactExport.
        :type: list[str]
        """

        self._export_attributes = export_attributes

    @property
    def contact_filter(self):
        """
        Gets the contact_filter of this RequestContactExport.
        Filter to apply to the export

        :return: The contact_filter of this RequestContactExport.
        :rtype: object
        """
        return self._contact_filter

    @contact_filter.setter
    def contact_filter(self, contact_filter):
        """
        Sets the contact_filter of this RequestContactExport.
        Filter to apply to the export

        :param contact_filter: The contact_filter of this RequestContactExport.
        :type: object
        """
        if contact_filter is None:
            raise ValueError("Invalid value for `contact_filter`, must not be `None`")

        self._contact_filter = contact_filter

    @property
    def notify_url(self):
        """
        Gets the notify_url of this RequestContactExport.
        Webhook that will be called once the export process is finished

        :return: The notify_url of this RequestContactExport.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """
        Sets the notify_url of this RequestContactExport.
        Webhook that will be called once the export process is finished

        :param notify_url: The notify_url of this RequestContactExport.
        :type: str
        """

        self._notify_url = notify_url

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
        if not isinstance(other, RequestContactExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
