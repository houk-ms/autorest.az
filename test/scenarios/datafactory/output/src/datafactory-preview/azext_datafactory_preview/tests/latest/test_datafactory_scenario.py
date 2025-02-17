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
from .example_steps import step_create
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_list2
from .example_steps import step_update
from .example_steps import step_configure_factory_repo
from .example_steps import step_get_data_plane_access
from .example_steps import step_get_git_hub_access_token
from .example_steps import step_integration_runtime_self_hosted_create
from .example_steps import step_integration_runtime_show
from .example_steps import step_integration_runtime_list
from .example_steps import step_integration_runtime_update
from .example_steps import step_integration_runtime_get_connection_info
from .example_steps import step_integration_runtime_get_monitoring_data
from .example_steps import step_integration_runtime_get_status
from .example_steps import step_integration_runtime_list_auth_key
from .example_steps import step_integration_runtime_regenerate_auth_key
from .example_steps import step_integration_runtime_remove_link
from .example_steps import step_integration_runtime_start
from .example_steps import step_integration_runtime_stop
from .example_steps import step_integration_runtime_sync_credentials
from .example_steps import step_integration_runtime_upgrade
from .example_steps import step_linked_integration_runtime_create
from .example_steps import step_integration_runtime_delete
from .example_steps import step_trigger_create
from .example_steps import step_trigger_update
from .example_steps import step_trigger_show
from .example_steps import step_trigger_list
from .example_steps import step_trigger_get_event_subscription_status
from .example_steps import step_trigger_query_by_factory
from .example_steps import step_trigger_start
from .example_steps import step_trigger_stop
from .example_steps import step_trigger_subscribe_to_event
from .example_steps import step_trigger_unsubscribe_from_event
from .example_steps import step_trigger_delete
from .example_steps import step_delete
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
    step_create(test, rg, checks=[])
    step_show(test, rg, checks=[])
    step_list(test, rg, checks=[])
    step_list2(test, rg, checks=[])
    step_update(test, rg, checks=[])
    step_configure_factory_repo(test, rg, checks=[])
    step_get_data_plane_access(test, rg, checks=[])
    step_get_git_hub_access_token(test, rg, checks=[])
    step_integration_runtime_self_hosted_create(test, rg, checks=[])
    step_integration_runtime_show(test, rg, checks=[])
    step_integration_runtime_list(test, rg, checks=[])
    step_integration_runtime_update(test, rg, checks=[])
    step_integration_runtime_get_connection_info(test, rg, checks=[])
    step_integration_runtime_get_monitoring_data(test, rg, checks=[])
    step_integration_runtime_get_status(test, rg, checks=[])
    step_integration_runtime_list_auth_key(test, rg, checks=[])
    step_integration_runtime_regenerate_auth_key(test, rg, checks=[])
    step_integration_runtime_remove_link(test, rg, checks=[])
    step_integration_runtime_start(test, rg, checks=[])
    step_integration_runtime_stop(test, rg, checks=[])
    step_integration_runtime_sync_credentials(test, rg, checks=[])
    step_integration_runtime_upgrade(test, rg, checks=[])
    step_linked_integration_runtime_create(test, rg, checks=[])
    step_integration_runtime_delete(test, rg, checks=[])
    step_trigger_create(test, rg, checks=[])
    step_trigger_update(test, rg, checks=[])
    step_trigger_show(test, rg, checks=[])
    step_trigger_list(test, rg, checks=[])
    step_trigger_get_event_subscription_status(test, rg, checks=[])
    step_trigger_query_by_factory(test, rg, checks=[])
    step_trigger_start(test, rg, checks=[])
    step_trigger_stop(test, rg, checks=[])
    step_trigger_subscribe_to_event(test, rg, checks=[])
    step_trigger_unsubscribe_from_event(test, rg, checks=[])
    step_trigger_delete(test, rg, checks=[])
    step_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class DatafactoryScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(DatafactoryScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myFactory': 'exampleFactoryName',
            'myTrigger': 'exampleTrigger',
            'myIntegrationRuntime': 'exampleIntegrationRuntime',
            'myIntegrationRuntime2': 'exampleManagedIntegrationRuntime',
            'myDatafactoryLinkedIntegrationRuntime': 'bfa92911-9fb6-4fbe-8f23-beae87bc1c83',
        })


    @ResourceGroupPreparer(name_prefix='clitestdatafactory_exampleResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_datafactory_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

