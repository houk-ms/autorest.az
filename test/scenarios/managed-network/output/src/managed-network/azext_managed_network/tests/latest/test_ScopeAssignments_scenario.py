# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer
from .preparers import SubnetPreparer
from .example_steps import step_mn_scope_assignment_create
from .example_steps import step_mn_scope_assignment_show
from .example_steps import step_mn_scope_assignment_list
from .example_steps import step_mn_scope_assignment_delete
from .example_steps import step_mn_scope_assignment_create_min
from .example_steps import step_mn_scope_assignment_show_min
from .example_steps import step_mn_scope_assignment_list_min
from .example_steps import step_mn_scope_assignment_delete_min
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_mn_scope_assignment_create(test, rg, checks=[
        test.check("assignedManagedNetwork", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft."
                   "ManagedNetwork/managedNetworks/{myManagedNetwork}", case_sensitive=False),
        test.check("name", "{myScopeAssignment}", case_sensitive=False),
    ])
    step_mn_scope_assignment_show(test, rg, checks=[
        test.check("assignedManagedNetwork", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft."
                   "ManagedNetwork/managedNetworks/{myManagedNetwork}", case_sensitive=False),
        test.check("name", "{myScopeAssignment}", case_sensitive=False),
    ])
    step_mn_scope_assignment_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_mn_scope_assignment_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


@try_manual
def call_scenario_min(test, rg):
    setup_scenario(test, rg)
    step_mn_scope_assignment_create_min(test, rg, checks=[
        test.check("name", "{myScopeAssignment}", case_sensitive=False),
    ])
    step_mn_scope_assignment_show_min(test, rg, checks=[
        test.check("name", "{myScopeAssignment}", case_sensitive=False),
    ])
    step_mn_scope_assignment_list_min(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_mn_scope_assignment_delete_min(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class ScopeAssignmentsScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(ScopeAssignmentsScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myManagedNetwork': self.create_random_name(prefix='myManagedNetwork'[:8], length=16),
            'myScopeAssignment': self.create_random_name(prefix='subscriptionCAssignment'[:11], length=23),
            'myManagedNetworkGroup': self.create_random_name(prefix='myManagedNetworkGroup1'[:11], length=22),
            'myManagedNetworkPeeringPolicy': self.create_random_name(prefix='myHubAndSpoke'[:6], length=13),
        })


    @ResourceGroupPreparer(name_prefix='clitestmanaged_network_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetA'[:7], key='vn', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetB'[:7], key='vn_2', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetC'[:7], key='vn_3', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_myHubVnet'[:7], key='vn_4', resource_group_key='rg')
    @SubnetPreparer(name_prefix='clitestmanaged_network_subnetA'[:7], key='subnets', virtual_network_key='vn',
                    resource_group_key='rg')
    @SubnetPreparer(name_prefix='clitestmanaged_network_subnetB'[:7], key='subnets_2', virtual_network_key='vn_2',
                    resource_group_key='rg')
    def test_ScopeAssignments_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()


    @ResourceGroupPreparer(name_prefix='clitestmanaged_network_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetA'[:7], key='vn', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetB'[:7], key='vn_2', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetC'[:7], key='vn_3', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_myHubVnet'[:7], key='vn_4', resource_group_key='rg')
    @SubnetPreparer(name_prefix='clitestmanaged_network_subnetA'[:7], key='subnets', virtual_network_key='vn',
                    resource_group_key='rg')
    @SubnetPreparer(name_prefix='clitestmanaged_network_subnetB'[:7], key='subnets_2', virtual_network_key='vn_2',
                    resource_group_key='rg')
    def test_ScopeAssignments_Scenario_min(self, rg):
        call_scenario_min(self, rg)
        calc_coverage(__file__)
        raise_if()

