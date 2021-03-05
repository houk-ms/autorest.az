# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from .._actions import (
    AddSubstatuses,
    AddStatuses
)


def load_arguments(self, _):

    with self.argument_context('vm virtual-machine assess-patch') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_name', type=str, help='The name of the virtual machine.', id_part='name')

    with self.argument_context('vm virtual-machine-scale-set-vm-extension list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_scale_set_name', type=str, help='The name of the VM scale set.')
        c.argument('instance_id', type=str, help='The instance ID of the virtual machine.')
        c.argument('expand', type=str, help='The expand expression to apply on the operation.')

    with self.argument_context('vm virtual-machine-scale-set-vm-extension show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_scale_set_name', type=str, help='The name of the VM scale set.', id_part='name')
        c.argument('instance_id', type=str, help='The instance ID of the virtual machine.', id_part='child_name_1')
        c.argument('vm_extension_name', type=str, help='The name of the virtual machine extension.',
                   id_part='child_name_2')
        c.argument('expand', type=str, help='The expand expression to apply on the operation.')

    with self.argument_context('vm virtual-machine-scale-set-vm-extension create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_scale_set_name', type=str, help='The name of the VM scale set.')
        c.argument('instance_id', type=str, help='The instance ID of the virtual machine.')
        c.argument('vm_extension_name', type=str, help='The name of the virtual machine extension.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('force_update_tag', type=str, help='How the extension handler should be forced to update even if '
                   'the extension configuration has not changed.')
        c.argument('publisher', type=str, help='The name of the extension handler publisher.')
        c.argument('type_properties_type', type=str, help='Specifies the type of the extension; an example is '
                   '"CustomScriptExtension".')
        c.argument('type_handler_version', type=str, help='Specifies the version of the script handler.')
        c.argument('auto_upgrade_minor_version', arg_type=get_three_state_flag(), help='Indicates whether the '
                   'extension should use a newer minor version if one is available at deployment time. Once deployed, '
                   'however, the extension will not upgrade minor versions unless redeployed, even with this property '
                   'set to true.')
        c.argument('enable_automatic_upgrade', arg_type=get_three_state_flag(), help='Indicates whether the extension '
                   'should be automatically upgraded by the platform if there is a newer version of the extension '
                   'available.')
        c.argument('settings', type=validate_file_or_dict, help='Json formatted public settings for the extension. '
                   'Expected value: json-string/@json-file.')
        c.argument('protected_settings', type=validate_file_or_dict, help='The extension can contain either '
                   'protectedSettings or protectedSettingsFromKeyVault or no protected settings at all. Expected '
                   'value: json-string/@json-file.')
        c.argument('name', type=str, help='The virtual machine extension name.', arg_group='Instance View')
        c.argument('type_', options_list=['--type'], type=str, help='Specifies the type of the extension; an example '
                   'is "CustomScriptExtension".', arg_group='Instance View')
        c.argument('virtual_machine_extension_instance_view_type_handler_version_type_handler_version', type=str,
                   help='Specifies the version of the script handler.', arg_group='Instance View')
        c.argument('substatuses', action=AddSubstatuses, nargs='+', help='The resource status information.',
                   arg_group='Instance View')
        c.argument('statuses', action=AddStatuses, nargs='+', help='The resource status information.',
                   arg_group='Instance View')

    with self.argument_context('vm virtual-machine-scale-set-vm-extension wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_scale_set_name', type=str, help='The name of the VM scale set.', id_part='name')
        c.argument('instance_id', type=str, help='The instance ID of the virtual machine.', id_part='child_name_1')
        c.argument('vm_extension_name', type=str, help='The name of the virtual machine extension.',
                   id_part='child_name_2')
        c.argument('expand', type=str, help='The expand expression to apply on the operation.')
