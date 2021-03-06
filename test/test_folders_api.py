# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from sib_api_v3_sdk.apis.folders_api import FoldersApi


class TestFoldersApi(unittest.TestCase):
    """ FoldersApi unit test stubs """

    def setUp(self):
        self.api = sib_api_v3_sdk.apis.folders_api.FoldersApi()

    def tearDown(self):
        pass

    def test_create_folder(self):
        """
        Test case for create_folder

        Create a folder
        """
        pass

    def test_delete_folder(self):
        """
        Test case for delete_folder

        Delete a folder (and all its lists)
        """
        pass

    def test_get_folder(self):
        """
        Test case for get_folder

        Returns folder details
        """
        pass

    def test_get_folder_lists(self):
        """
        Test case for get_folder_lists

        Get the lists in a folder
        """
        pass

    def test_get_folders(self):
        """
        Test case for get_folders

        Get all the folders
        """
        pass

    def test_update_folder(self):
        """
        Test case for update_folder

        Update a contact folder
        """
        pass


if __name__ == '__main__':
    unittest.main()
