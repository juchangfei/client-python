# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v2alpha1_metric_spec import V2alpha1MetricSpec


class TestV2alpha1MetricSpec(unittest.TestCase):
    """ V2alpha1MetricSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1MetricSpec(self):
        """
        Test V2alpha1MetricSpec
        """
        model = kubernetes.client.models.v2alpha1_metric_spec.V2alpha1MetricSpec()


if __name__ == '__main__':
    unittest.main()