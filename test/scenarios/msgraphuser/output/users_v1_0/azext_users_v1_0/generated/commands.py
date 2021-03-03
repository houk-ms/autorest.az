# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_users_v1_0.generated._client_factory import cf_user_user

    users_v1_0_user_user = CliCommandType(
        operations_tmpl='azext_users_v1_0.vendored_sdks.users.operations._users_user_operations#UsersUserOperations.{}',
        client_factory=cf_user_user,
    )
    with self.command_group('users user', users_v1_0_user_user, client_factory=cf_user_user) as g:
        g.custom_command('list', 'users_user_list')
        g.custom_command('create', 'users_user_create')
        g.custom_command('update', 'users_user_update')
        g.custom_command('delete-user', 'users_user_delete_user')
        g.custom_command('show-user', 'users_user_show_user')

    from azext_users_v1_0.generated._client_factory import cf_user

    users_v1_0_user = CliCommandType(
        operations_tmpl='azext_users_v1_0.vendored_sdks.users.operations._users_operations#UsersOperations.{}',
        client_factory=cf_user,
    )
    with self.command_group('users user', users_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('create-extension', 'users_user_create_extension')
        g.custom_command('create-license-detail', 'users_user_create_license_detail')
        g.custom_command('create-photo', 'users_user_create_photo')
        g.custom_command('create-ref-created-object', 'users_user_create_ref_created_object')
        g.custom_command('create-ref-direct-report', 'users_user_create_ref_direct_report')
        g.custom_command('create-ref-member-of', 'users_user_create_ref_member_of')
        g.custom_command('create-ref-oauth2-permission-grant', 'users_user_create_ref_oauth2_permission_grant')
        g.custom_command('create-ref-owned-device', 'users_user_create_ref_owned_device')
        g.custom_command('create-ref-owned-object', 'users_user_create_ref_owned_object')
        g.custom_command('create-ref-registered-device', 'users_user_create_ref_registered_device')
        g.custom_command('create-ref-transitive-member-of', 'users_user_create_ref_transitive_member_of')
        g.custom_command('delete-extension', 'users_user_delete_extension')
        g.custom_command('delete-license-detail', 'users_user_delete_license_detail')
        g.custom_command('delete-outlook', 'users_user_delete_outlook')
        g.custom_command('delete-photo', 'users_user_delete_photo')
        g.custom_command('delete-ref-manager', 'users_user_delete_ref_manager')
        g.custom_command('delete-setting', 'users_user_delete_setting')
        g.custom_command('list-created-object', 'users_user_list_created_object')
        g.custom_command('list-direct-report', 'users_user_list_direct_report')
        g.custom_command('list-extension', 'users_user_list_extension')
        g.custom_command('list-license-detail', 'users_user_list_license_detail')
        g.custom_command('list-member-of', 'users_user_list_member_of')
        g.custom_command('list-oauth2-permission-grant', 'users_user_list_oauth2_permission_grant')
        g.custom_command('list-owned-device', 'users_user_list_owned_device')
        g.custom_command('list-owned-object', 'users_user_list_owned_object')
        g.custom_command('list-photo', 'users_user_list_photo')
        g.custom_command('list-ref-created-object', 'users_user_list_ref_created_object')
        g.custom_command('list-ref-direct-report', 'users_user_list_ref_direct_report')
        g.custom_command('list-ref-member-of', 'users_user_list_ref_member_of')
        g.custom_command('list-ref-oauth2-permission-grant', 'users_user_list_ref_oauth2_permission_grant')
        g.custom_command('list-ref-owned-device', 'users_user_list_ref_owned_device')
        g.custom_command('list-ref-owned-object', 'users_user_list_ref_owned_object')
        g.custom_command('list-ref-registered-device', 'users_user_list_ref_registered_device')
        g.custom_command('list-ref-transitive-member-of', 'users_user_list_ref_transitive_member_of')
        g.custom_command('list-registered-device', 'users_user_list_registered_device')
        g.custom_command('list-transitive-member-of', 'users_user_list_transitive_member_of')
        g.custom_command('set-ref-manager', 'users_user_set_ref_manager')
        g.custom_command('show-extension', 'users_user_show_extension')
        g.custom_command('show-license-detail', 'users_user_show_license_detail')
        g.custom_command('show-manager', 'users_user_show_manager')
        g.custom_command('show-outlook', 'users_user_show_outlook')
        g.custom_command('show-photo', 'users_user_show_photo')
        g.custom_command('show-ref-manager', 'users_user_show_ref_manager')
        g.custom_command('show-setting', 'users_user_show_setting')
        g.custom_command('update-extension', 'users_user_update_extension')
        g.custom_command('update-license-detail', 'users_user_update_license_detail')
        g.custom_command('update-outlook', 'users_user_update_outlook')
        g.custom_command('update-photo', 'users_user_update_photo')
        g.custom_command('update-setting', 'users_user_update_setting')

    from azext_users_v1_0.generated._client_factory import cf_user_outlook

    users_v1_0_user_outlook = CliCommandType(
        operations_tmpl=(
            'azext_users_v1_0.vendored_sdks.users.operations._users_outlook_operations#UsersOutlookOperations.{}'
        ),
        client_factory=cf_user_outlook,
    )
    with self.command_group('users user-outlook', users_v1_0_user_outlook, client_factory=cf_user_outlook) as g:
        g.custom_command('create-master-category', 'users_user_outlook_create_master_category')
        g.custom_command('delete-master-category', 'users_user_outlook_delete_master_category')
        g.custom_command('list-master-category', 'users_user_outlook_list_master_category')
        g.custom_command('show-master-category', 'users_user_outlook_show_master_category')
        g.custom_command('update-master-category', 'users_user_outlook_update_master_category')

    from azext_users_v1_0.generated._client_factory import cf_user_setting

    users_v1_0_user_setting = CliCommandType(
        operations_tmpl=(
            'azext_users_v1_0.vendored_sdks.users.operations._users_settings_operations#UsersSettingsOperations.{}'
        ),
        client_factory=cf_user_setting,
    )
    with self.command_group('users user-setting', users_v1_0_user_setting, client_factory=cf_user_setting) as g:
        g.custom_command('delete-shift-preference', 'users_user_setting_delete_shift_preference')
        g.custom_command('show-shift-preference', 'users_user_setting_show_shift_preference')
        g.custom_command('update-shift-preference', 'users_user_setting_update_shift_preference')

    with self.command_group('users_v1_0', is_experimental=True):
        pass
