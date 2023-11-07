# -*- fundamental -*-
# from __future__ import (absolute_import, division,
#                        print_function, unicode_literals)
from builtins import *
from future.utils import python_2_unicode_compatible# -*- encoding: utf-8 -*-
# NOTE: This file is generated. Do not edit.

from collections import namedtuple
from repoze.lru import lru_cache
from sqlalchemy import and_, func, or_
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import *
from sqlalchemy.sql import *
from sqlalchemy import event
from sqlalchemy.orm import mapper
import re
import ujson
class CCardMixin: pass
class CCardIssuerMixin: pass
class CCardOrganizationMixin: pass
class CCardTypeMixin: pass
class CDeviceMixin: pass
class CDevicePersonMixin: pass
class CDeviceSubtypeMixin: pass
class CDeviceTypeMixin: pass
class CIloqKeyMixin: pass
class CKeyMixin: pass
class CKeyProfileMixin: pass
class CKeyTypeMixin: pass
class CWorkstationMixin: pass
class DAbsenceMixin: pass
class DAuthMethodMixin: pass
class DCompetenceMixin: pass
class DEducationMixin: pass
class DJobPeriodMixin: pass
class DJobPeriodAbsenceMixin: pass
class DJobPeriodAttrPermissionLogMixin: pass
class DJobPeriodAttrPermissionStateMixin: pass
class DJobPeriodGPermissionLogMixin: pass
class DJobPeriodGPermissionStateMixin: pass
class DJobPeriodJrOuPermissionLogMixin: pass
class DJobPeriodJrOuPermissionStateMixin: pass
class DJobPeriodJrPermissionLogMixin: pass
class DJobPeriodJrPermissionStateMixin: pass
class DJobPeriodJtPermissionLogMixin: pass
class DJobPeriodJtPermissionStateMixin: pass
class DJobPeriodManagerAssignmentQueueMixin: pass
class DJobPeriodMergeLogMixin: pass
class DJobPeriodOrgGroupPermissionLogMixin: pass
class DJobPeriodOrgGroupPermissionStateMixin: pass
class DJobPeriodOrgSpecPermissionLogMixin: pass
class DJobPeriodOrgSpecPermissionStateMixin: pass
class DJobPeriodOuPermissionLogMixin: pass
class DJobPeriodOuPermissionStateMixin: pass
class DJobPeriodSubstituteMixin: pass
class DJobPeriodSubstitutePermissionsMixin: pass
class DJobPeriodValidityLogMixin: pass
class DJobPeriodValidityStateMixin: pass
class DJobtitleMixin: pass
class DMappingRuleMixin: pass
class DPersonMixin: pass
class DPersonAbsenceEndedMixin: pass
class DPersonAbsenceStartedMixin: pass
class DPersonPermissionManualProvisioningLogMixin: pass
class DPersonPermissionManualProvisioningStateMixin: pass
class DPersonPermissionProvisioningLogMixin: pass
class DPersonPermissionProvisioningStateMixin: pass
class DUserAuthMixin: pass
class EExtOrgMixin: pass
class EExtOrgCtAllMixin: pass
class EExtOrgTypeMixin: pass
class EExternalPersonMixin: pass
class EJobFamilyMixin: pass
class EJobPeriodMixin: pass
class EJobPeriodAbsenceMixin: pass
class EJobPeriodAttrPermissionLogMixin: pass
class EJobPeriodAttrPermissionStateMixin: pass
class EJobPeriodGPermissionLogMixin: pass
class EJobPeriodGPermissionStateMixin: pass
class EJobPeriodIouPermissionLogMixin: pass
class EJobPeriodIouPermissionStateMixin: pass
class EJobPeriodJrOuPermissionLogMixin: pass
class EJobPeriodJrOuPermissionStateMixin: pass
class EJobPeriodJrPermissionLogMixin: pass
class EJobPeriodJrPermissionStateMixin: pass
class EJobPeriodJtPermissionLogMixin: pass
class EJobPeriodJtPermissionStateMixin: pass
class EJobPeriodManagerAssignmentQueueMixin: pass
class EJobPeriodMergeLogMixin: pass
class EJobPeriodOrgGroupPermissionLogMixin: pass
class EJobPeriodOrgGroupPermissionStateMixin: pass
class EJobPeriodOrgSpecPermissionLogMixin: pass
class EJobPeriodOrgSpecPermissionStateMixin: pass
class EJobPeriodOuPermissionLogMixin: pass
class EJobPeriodOuPermissionStateMixin: pass
class EJobPeriodSubstituteMixin: pass
class EJobPeriodSubstitutePermissionsMixin: pass
class EJobPeriodValidityLogMixin: pass
class EJobPeriodValidityStateMixin: pass
class EJobRoleMixin: pass
class EJobRoleCtAllMixin: pass
class EOrgTypeServiceMixin: pass
class EPersonAbsenceEndedMixin: pass
class EPersonAbsenceStartedMixin: pass
class EPersonPermissionManualProvisioningLogMixin: pass
class EPersonPermissionManualProvisioningStateMixin: pass
class EPersonPermissionProvisioningLogMixin: pass
class EPersonPermissionProvisioningStateMixin: pass
class ERequestCartMixin: pass
class ERequestCartPermissionMixin: pass
class FLangMixin: pass
class FListMixin: pass
class FSchemaMixin: pass
class FSchemaTableMixin: pass
class FSystemInfoMixin: pass
class GAccountAttributeMixin: pass
class GAceMixin: pass
class GAceAttributeMixin: pass
class GCountryMixin: pass
class GEmailLogMixin: pass
class GIdentityMixin: pass
class GIdentitySourceMixin: pass
class GLanguageMixin: pass
class GMdmRuleMixin: pass
class GMdmSourceMixin: pass
class GMdmTableMixin: pass
class GMdmTableAttributeMixin: pass
class GNotificationMixin: pass
class GNotificationQueueMixin: pass
class GPermissionMixin: pass
class GPermissionValidityLogMixin: pass
class GPermissionValidityStateMixin: pass
class GPersonUseraccountMixin: pass
class GProvisioningTaskMixin: pass
class GRegionMixin: pass
class GServiceMixin: pass
class GServiceCtAllMixin: pass
class GServiceProviderMixin: pass
class GServiceRequestMixin: pass
class GServiceRespMixin: pass
class GServiceRoleMixin: pass
class GServiceRoleCtAllMixin: pass
class GServiceTypeMixin: pass
class GServiceTypeSrolesMixin: pass
class GSrParametersMixin: pass
class GSrTransMixin: pass
class GSystemMixin: pass
class GSystemCtAllMixin: pass
class GSystemSchemaMixin: pass
class GSystemSchemaAttributeMixin: pass
class GUserGroupMixin: pass
class HrDesktopSubstMixin: pass
class HrImportRecordMixin: pass
class HrIntegrationMixin: pass
class HrIntegrationVaultMixin: pass
class IBusinessAreaMixin: pass
class ICostCenterMixin: pass
class IJobFamilyMixin: pass
class IJobRoleMixin: pass
class IJobRoleCtAllMixin: pass
class ILegalCompanyMixin: pass
class ILocationMixin: pass
class ILocationCtAllMixin: pass
class IManagerPerProfessionMixin: pass
class IOrgGroupMixin: pass
class IOrgTypeMixin: pass
class IOrgUnitMixin: pass
class IOrgUnitCtAllMixin: pass
class IOrgUnitManagerMixin: pass
class IOrgUnitManagerSubstituteMixin: pass
class LoginChallengeMixin: pass
class OneTimeLinkMixin: pass
class PRequestCartMixin: pass
class PRequestCartRowMixin: pass
class RDynRoleMixin: pass
class ROrgDacMixin: pass
class ROrgServiceMixin: pass
class ROrgTypeServiceMixin: pass
class RSodExceptionMixin: pass
class RSodRuleMixin: pass
class RSodRuleClassMixin: pass
class RUserDacMixin: pass
class RequestCartMixin: pass
class RequestCartPermissionMixin: pass
class SDDepartmentWeekMaxQuantityMixin: pass
class SDStudyProgrammeMixin: pass
class SDTraineeshipPlacementMixin: pass
class SDTraineeshipPlacementRequestMixin: pass
class SDTraineeshipRequestMixin: pass
class SDTraineeshipTypeMixin: pass
class SDTraineeshipTypeCtAllMixin: pass
class TokenBlocklistMixin: pass
class UserightMixin: pass
class ZreportMixin: pass
class ZreportParameterMixin: pass
class ZroleMixin: pass
class ZroleEntityScriptMixin: pass
class ZuserMixin: pass
class ZuserPasswordMixin: pass
class DPersonPermissionsMixin: pass
class DPersonPermissionsPrimMixin: pass
class DisplayNameCacheMixin: pass
class EPersonPermissionsMixin: pass
class EPersonPermissionsPrimMixin: pass
class EntityAuditLogMixin: pass
class EntityTieAuditLogMixin: pass
class EventLogMixin: pass
class JobPeriodQueryTableMixin: pass
class JobPeriodQueryTablePrimMixin: pass
class XPrimaryJobPeriodMixin: pass

from datamaster.caching_query import FromCache
from datamaster.types import *
# db object is taken from datamaster.model_mixins
from datamaster.model_mixins import *
__CCardPlain_slots_without_collections__ = ('id', 'card_new', 'card_type_id', 'card_type', 'upn_code', 'identity_id', 'person_id', 'external_person_id', 'expiration_date', 'identity_checked', 'identity_checked_by', 'description', 'description2', 'status', 'replacement_card', 'replaced_card_id', 'given_date', 'given_by_id', 'return_date', 'activation_date', 'deactivation_date', 'deactivation_reason_code', 'deactivation_reason', 'card_organization_id', 'card_organization_name', 'user_cn', 'issuer_id', 'issuer_cn', 'last_name', 'first_name', 'valvira_id', 'subject_serial_no', 'sv_number', 'occupation_name', 'email', 'cert_serial1', 'cert_serial2', 'valid_until', 'token_number', 'reg_ra_workstation_id', 'reg_person_id', 'ra_open_cn', 'ap_upn_old', 'ap_pre_win', 'internal_org_id', 'last_name_ad', 'first_name_ad', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'card_type_id__name', 'identity_id__name', 'person_id__name', 'external_person_id__name', 'replaced_card_id__name', 'given_by_id__name', 'card_organization_id__name', 'issuer_id__name', 'reg_ra_workstation_id__name', 'reg_person_id__name', 'internal_org_id__name'  )
class CCardPlain(object):
    __slots__ = ('id', 'card_new', 'card_type_id', 'card_type', 'upn_code', 'identity_id', 'person_id', 'external_person_id', 'expiration_date', 'identity_checked', 'identity_checked_by', 'description', 'description2', 'status', 'replacement_card', 'replaced_card_id', 'given_date', 'given_by_id', 'return_date', 'activation_date', 'deactivation_date', 'deactivation_reason_code', 'deactivation_reason', 'card_organization_id', 'card_organization_name', 'user_cn', 'issuer_id', 'issuer_cn', 'last_name', 'first_name', 'valvira_id', 'subject_serial_no', 'sv_number', 'occupation_name', 'email', 'cert_serial1', 'cert_serial2', 'valid_until', 'token_number', 'reg_ra_workstation_id', 'reg_person_id', 'ra_open_cn', 'ap_upn_old', 'ap_pre_win', 'internal_org_id', 'last_name_ad', 'first_name_ad', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'card_type_id__name', 'identity_id__name', 'person_id__name', 'external_person_id__name', 'replaced_card_id__name', 'given_by_id__name', 'card_organization_id__name', 'issuer_id__name', 'reg_ra_workstation_id__name', 'reg_person_id__name', 'internal_org_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CCardPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CCardPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CCardPlain_slots_without_collections__)
        for i in range(len(__CCardPlain_slots_without_collections__)):
            setattr(self, __CCardPlain_slots_without_collections__[i], state[i])
__CCardIssuerPlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class CCardIssuerPlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CCardIssuerPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CCardIssuerPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CCardIssuerPlain_slots_without_collections__)
        for i in range(len(__CCardIssuerPlain_slots_without_collections__)):
            setattr(self, __CCardIssuerPlain_slots_without_collections__[i], state[i])
__CCardOrganizationPlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class CCardOrganizationPlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CCardOrganizationPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CCardOrganizationPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CCardOrganizationPlain_slots_without_collections__)
        for i in range(len(__CCardOrganizationPlain_slots_without_collections__)):
            setattr(self, __CCardOrganizationPlain_slots_without_collections__[i], state[i])
__CCardTypePlain_slots_without_collections__ = ('id', 'name', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name'  )
class CCardTypePlain(object):
    __slots__ = ('id', 'name', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CCardTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CCardTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CCardTypePlain_slots_without_collections__)
        for i in range(len(__CCardTypePlain_slots_without_collections__)):
            setattr(self, __CCardTypePlain_slots_without_collections__[i], state[i])
__CDevicePlain_slots_without_collections__ = ('id', 'name', 'device_start_date', 'device_end_date', 'device_type', 'device_subtype', 'serial_no', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'device_type__name', 'device_subtype__name'  )
class CDevicePlain(object):
    __slots__ = ('id', 'name', 'device_start_date', 'device_end_date', 'device_type', 'device_subtype', 'serial_no', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'device_type__name', 'device_subtype__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CDevicePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CDevicePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CDevicePlain_slots_without_collections__)
        for i in range(len(__CDevicePlain_slots_without_collections__)):
            setattr(self, __CDevicePlain_slots_without_collections__[i], state[i])
__CDevicePersonPlain_slots_without_collections__ = ('id', 'device_id', 'identity_id', 'person_id', 'external_person_id', 'given_date', 'given_by_id', 'return_date', 'return_reason_code', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'device_id__name', 'identity_id__name', 'person_id__name', 'external_person_id__name', 'given_by_id__name'  )
class CDevicePersonPlain(object):
    __slots__ = ('id', 'device_id', 'identity_id', 'person_id', 'external_person_id', 'given_date', 'given_by_id', 'return_date', 'return_reason_code', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'device_id__name', 'identity_id__name', 'person_id__name', 'external_person_id__name', 'given_by_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CDevicePersonPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CDevicePersonPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CDevicePersonPlain_slots_without_collections__)
        for i in range(len(__CDevicePersonPlain_slots_without_collections__)):
            setattr(self, __CDevicePersonPlain_slots_without_collections__[i], state[i])
__CDeviceSubtypePlain_slots_without_collections__ = ('id', 'device_type', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'device_type__name'  )
class CDeviceSubtypePlain(object):
    __slots__ = ('id', 'device_type', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'device_type__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CDeviceSubtypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CDeviceSubtypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CDeviceSubtypePlain_slots_without_collections__)
        for i in range(len(__CDeviceSubtypePlain_slots_without_collections__)):
            setattr(self, __CDeviceSubtypePlain_slots_without_collections__[i], state[i])
__CDeviceTypePlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class CDeviceTypePlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CDeviceTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CDeviceTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CDeviceTypePlain_slots_without_collections__)
        for i in range(len(__CDeviceTypePlain_slots_without_collections__)):
            setattr(self, __CDeviceTypePlain_slots_without_collections__[i], state[i])
__CKeyPlain_slots_without_collections__ = ('id', 'key_new', 'key_type_id', 'key_type', 'key_profile', 'serial_no', 'identity_id', 'person_id', 'external_person_id', 'expiration_date', 'identity_checked', 'identity_checked_by', 'description', 'description2', 'status', 'replacement_key', 'replaced_key_id', 'given_date', 'given_by_id', 'return_date', 'activation_date', 'deactivation_date', 'deactivation_reason_code', 'deactivation_reason', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'key_type_id__name', 'key_profile__name', 'identity_id__name', 'person_id__name', 'external_person_id__name', 'replaced_key_id__name', 'given_by_id__name'  )
class CKeyPlain(object):
    __slots__ = ('id', 'key_new', 'key_type_id', 'key_type', 'key_profile', 'serial_no', 'identity_id', 'person_id', 'external_person_id', 'expiration_date', 'identity_checked', 'identity_checked_by', 'description', 'description2', 'status', 'replacement_key', 'replaced_key_id', 'given_date', 'given_by_id', 'return_date', 'activation_date', 'deactivation_date', 'deactivation_reason_code', 'deactivation_reason', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'key_type_id__name', 'key_profile__name', 'identity_id__name', 'person_id__name', 'external_person_id__name', 'replaced_key_id__name', 'given_by_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CKeyPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CKeyPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CKeyPlain_slots_without_collections__)
        for i in range(len(__CKeyPlain_slots_without_collections__)):
            setattr(self, __CKeyPlain_slots_without_collections__[i], state[i])
__CKeyProfilePlain_slots_without_collections__ = ('id', 'key_type_id', 'key_type', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'key_type_id__name'  )
class CKeyProfilePlain(object):
    __slots__ = ('id', 'key_type_id', 'key_type', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'key_type_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CKeyProfilePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CKeyProfilePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CKeyProfilePlain_slots_without_collections__)
        for i in range(len(__CKeyProfilePlain_slots_without_collections__)):
            setattr(self, __CKeyProfilePlain_slots_without_collections__[i], state[i])
__CKeyTypePlain_slots_without_collections__ = ('id', 'name', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name'  )
class CKeyTypePlain(object):
    __slots__ = ('id', 'name', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CKeyTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CKeyTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CKeyTypePlain_slots_without_collections__)
        for i in range(len(__CKeyTypePlain_slots_without_collections__)):
            setattr(self, __CKeyTypePlain_slots_without_collections__[i], state[i])
__CWorkstationPlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class CWorkstationPlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __CWorkstationPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __CWorkstationPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__CWorkstationPlain_slots_without_collections__)
        for i in range(len(__CWorkstationPlain_slots_without_collections__)):
            setattr(self, __CWorkstationPlain_slots_without_collections__[i], state[i])
__DAbsencePlain_slots_without_collections__ = ('id', 'person_id', 'external_person_id', 'absence_type', 'start_date', 'end_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name'  )
class DAbsencePlain(object):
    __slots__ = ('id', 'person_id', 'external_person_id', 'absence_type', 'start_date', 'end_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DAbsencePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DAbsencePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DAbsencePlain_slots_without_collections__)
        for i in range(len(__DAbsencePlain_slots_without_collections__)):
            setattr(self, __DAbsencePlain_slots_without_collections__[i], state[i])
__DAuthMethodPlain_slots_without_collections__ = ('id', 'name', 'description', 'authentication_level', 'starting_date', 'termination_date', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class DAuthMethodPlain(object):
    __slots__ = ('id', 'name', 'description', 'authentication_level', 'starting_date', 'termination_date', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DAuthMethodPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DAuthMethodPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DAuthMethodPlain_slots_without_collections__)
        for i in range(len(__DAuthMethodPlain_slots_without_collections__)):
            setattr(self, __DAuthMethodPlain_slots_without_collections__[i], state[i])
__DCompetencePlain_slots_without_collections__ = ('id', 'code', 'name', 'description', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class DCompetencePlain(object):
    __slots__ = ('id', 'code', 'name', 'description', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DCompetencePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DCompetencePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DCompetencePlain_slots_without_collections__)
        for i in range(len(__DCompetencePlain_slots_without_collections__)):
            setattr(self, __DCompetencePlain_slots_without_collections__[i], state[i])
__DEducationPlain_slots_without_collections__ = ('id', 'code', 'name', 'description', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class DEducationPlain(object):
    __slots__ = ('id', 'code', 'name', 'description', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DEducationPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DEducationPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DEducationPlain_slots_without_collections__)
        for i in range(len(__DEducationPlain_slots_without_collections__)):
            setattr(self, __DEducationPlain_slots_without_collections__[i], state[i])
__DJobPeriodPlain_slots_without_collections__ = ('id', 'person_id', 'starting_date', 'termination_date', 'job_period_type', 'is_manager', 'orgunit_id', 'job_title', 'other_job_title', 'specific_job_title', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'organization_association_type', 'status', 'manager_id', 'manager_email', 'manager_name', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'report_manager_id', 'org_unit_manager_id', 'information_checked', 'contract', 'medicine_right', 'absence_active', 'substitute_periods_active', 'hr_job_type', 'c_pasu', 'full_part_per', 'hr_work_time_type', 'operative_staff', 'int_period_id', 'int_job_title', 'int_job_code', 'int_job_code2', 'hr_profession_code', 'hr_period_character_code', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'pupo', 'phone', 'card_valid_from', 'card_valid_to', 'exc_username', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_location_id', 'exc_country_id', 'exc_primary_period', 'inferred_primary_job_period', 'externally_managed', 'exported_to_idm', 'created_by_id', 'is_primary_jobtitle', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'orgunit_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'manager_id__name', 'subst_manager_id__name', 'report_manager_id__name', 'org_unit_manager_id__name', 'exc_legalcompany_id__name', 'exc_costcenter_id__name', 'exc_location_id__name', 'exc_country_id__name', 'created_by_id__name', 'valid', 'valid2', 'valid_to_show'  )
class DJobPeriodPlain(object):
    __slots__ = ('id', 'person_id', 'starting_date', 'termination_date', 'job_period_type', 'is_manager', 'orgunit_id', 'job_title', 'other_job_title', 'specific_job_title', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'organization_association_type', 'status', 'manager_id', 'manager_email', 'manager_name', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'report_manager_id', 'org_unit_manager_id', 'information_checked', 'contract', 'medicine_right', 'absence_active', 'substitute_periods_active', 'hr_job_type', 'c_pasu', 'full_part_per', 'hr_work_time_type', 'operative_staff', 'int_period_id', 'int_job_title', 'int_job_code', 'int_job_code2', 'hr_profession_code', 'hr_period_character_code', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'pupo', 'phone', 'card_valid_from', 'card_valid_to', 'exc_username', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_location_id', 'exc_country_id', 'exc_primary_period', 'inferred_primary_job_period', 'externally_managed', 'exported_to_idm', 'created_by_id', 'is_primary_jobtitle', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'orgunit_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'manager_id__name', 'subst_manager_id__name', 'report_manager_id__name', 'org_unit_manager_id__name', 'exc_legalcompany_id__name', 'exc_costcenter_id__name', 'exc_location_id__name', 'exc_country_id__name', 'created_by_id__name', 'valid', 'valid2', 'valid_to_show' , 'absences', 'substitute_detail', 'requested_permissions', 'other_organization_units' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DJobPeriodPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DJobPeriodPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DJobPeriodPlain_slots_without_collections__)
        for i in range(len(__DJobPeriodPlain_slots_without_collections__)):
            setattr(self, __DJobPeriodPlain_slots_without_collections__[i], state[i])
__DJobPeriodAbsencePlain_slots_without_collections__ = ('d_job_period_id', 'valid_from', 'created_by', 'start_date', 'end_date', 'description'
    , 'id__name', 'd_job_period_id__name', 'created_by__name'  )
class DJobPeriodAbsencePlain(object):
    __slots__ = ('d_job_period_id', 'valid_from', 'created_by', 'start_date', 'end_date', 'description'
    , 'id__name', 'd_job_period_id__name', 'created_by__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DJobPeriodAbsencePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DJobPeriodAbsencePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DJobPeriodAbsencePlain_slots_without_collections__)
        for i in range(len(__DJobPeriodAbsencePlain_slots_without_collections__)):
            setattr(self, __DJobPeriodAbsencePlain_slots_without_collections__[i], state[i])
__DJobPeriodSubstitutePlain_slots_without_collections__ = ('id', 'd_job_period_id', 'd_substistute_person_id', 'start_date', 'end_date', 'is_backup', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'd_job_period_id__name', 'd_substistute_person_id__name'  )
class DJobPeriodSubstitutePlain(object):
    __slots__ = ('id', 'd_job_period_id', 'd_substistute_person_id', 'start_date', 'end_date', 'is_backup', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'd_job_period_id__name', 'd_substistute_person_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DJobPeriodSubstitutePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DJobPeriodSubstitutePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DJobPeriodSubstitutePlain_slots_without_collections__)
        for i in range(len(__DJobPeriodSubstitutePlain_slots_without_collections__)):
            setattr(self, __DJobPeriodSubstitutePlain_slots_without_collections__[i], state[i])
__DJobtitlePlain_slots_without_collections__ = ('id', 'code', 'name', 'name6', 'description', 'jobrole_id', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'jobrole_id__name'  )
class DJobtitlePlain(object):
    __slots__ = ('id', 'code', 'name', 'name6', 'description', 'jobrole_id', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'jobrole_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DJobtitlePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DJobtitlePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DJobtitlePlain_slots_without_collections__)
        for i in range(len(__DJobtitlePlain_slots_without_collections__)):
            setattr(self, __DJobtitlePlain_slots_without_collections__[i], state[i])
__DMappingRulePlain_slots_without_collections__ = ('id', 'code', 'name', 'description', 'mdm_source_id', 'source_field', 'target_table', 'target_field', 'target_datatype', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'mdm_source_id__name'  )
class DMappingRulePlain(object):
    __slots__ = ('id', 'code', 'name', 'description', 'mdm_source_id', 'source_field', 'target_table', 'target_field', 'target_datatype', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'mdm_source_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DMappingRulePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DMappingRulePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DMappingRulePlain_slots_without_collections__)
        for i in range(len(__DMappingRulePlain_slots_without_collections__)):
            setattr(self, __DMappingRulePlain_slots_without_collections__[i], state[i])
__DPersonPlain_slots_without_collections__ = ('id', 'social_security_number', 'personnel_number', 'name_prefix', 'first_name', 'middle_name', 'last_name', 'preferred_name', 'identity_id', 'permanent', 'starting_date', 'termination_date', 'termination_type', 'information_checked', 'email_active', 'photo', 'username', 'orgunit_id', 'email', 'pupo', 'sv_number', 'other_address', 'language_id', 'status', 'b_phone', 'b_mobile', 'jr_start_date', 'is_manager', 'jobtitle_id', 'jobtitle', 'jobfamily_id', 'jobrole_id', 'job_type', 'manager_id', 'manager_name', 'manager_email', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'exc_location_id', 'remote_office', 'location_info', 'home_street', 'home_street2', 'home_post', 'home_city', 'home_state', 'homecountry_id', 'identity_checked', 'identitysource_id', 'personal_id', 'staff_oper_code', 'full_time', 'birth_date', 'gender', 'nationality_id', 'int_job_title', 'int_job_code', 'int_code_code2', 'mdm_source_id', 'mdm_person_id', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'last_checking_date', 'last_import_date', 'absence_status', 'exc_businessarea_id', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_country_id', 'waiting_manager_approval', 'manager_approved_id', 'manager_approval_timestamp', 'first_email_sent_timestamp', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'identity_id__name', 'orgunit_id__name', 'language_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'manager_id__name', 'subst_manager_id__name', 'exc_location_id__name', 'homecountry_id__name', 'identitysource_id__name', 'nationality_id__name', 'mdm_source_id__name', 'exc_businessarea_id__name', 'exc_legalcompany_id__name', 'exc_costcenter_id__name', 'exc_country_id__name', 'manager_approved_id__name', 'valid', 'valid2'  )
class DPersonPlain(object):
    __slots__ = ('id', 'social_security_number', 'personnel_number', 'name_prefix', 'first_name', 'middle_name', 'last_name', 'preferred_name', 'identity_id', 'permanent', 'starting_date', 'termination_date', 'termination_type', 'information_checked', 'email_active', 'photo', 'username', 'orgunit_id', 'email', 'pupo', 'sv_number', 'other_address', 'language_id', 'status', 'b_phone', 'b_mobile', 'jr_start_date', 'is_manager', 'jobtitle_id', 'jobtitle', 'jobfamily_id', 'jobrole_id', 'job_type', 'manager_id', 'manager_name', 'manager_email', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'exc_location_id', 'remote_office', 'location_info', 'home_street', 'home_street2', 'home_post', 'home_city', 'home_state', 'homecountry_id', 'identity_checked', 'identitysource_id', 'personal_id', 'staff_oper_code', 'full_time', 'birth_date', 'gender', 'nationality_id', 'int_job_title', 'int_job_code', 'int_code_code2', 'mdm_source_id', 'mdm_person_id', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'last_checking_date', 'last_import_date', 'absence_status', 'exc_businessarea_id', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_country_id', 'waiting_manager_approval', 'manager_approved_id', 'manager_approval_timestamp', 'first_email_sent_timestamp', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'identity_id__name', 'orgunit_id__name', 'language_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'manager_id__name', 'subst_manager_id__name', 'exc_location_id__name', 'homecountry_id__name', 'identitysource_id__name', 'nationality_id__name', 'mdm_source_id__name', 'exc_businessarea_id__name', 'exc_legalcompany_id__name', 'exc_costcenter_id__name', 'exc_country_id__name', 'manager_approved_id__name', 'valid', 'valid2' , 'job_periods', 'manager_in_job_periods', 'manager_in_external_job_periods', 'cards', 'keys', 'devices', 'absences', 'authentications', 'user_accounts', 'organization_units', 'education', 'competences' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DPersonPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DPersonPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DPersonPlain_slots_without_collections__)
        for i in range(len(__DPersonPlain_slots_without_collections__)):
            setattr(self, __DPersonPlain_slots_without_collections__[i], state[i])
__DUserAuthPlain_slots_without_collections__ = ('id', 'device_id', 'classification1', 'classification2', 'person_id', 'authmethod_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'authmethod_id__name'  )
class DUserAuthPlain(object):
    __slots__ = ('id', 'device_id', 'classification1', 'classification2', 'person_id', 'authmethod_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'authmethod_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __DUserAuthPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __DUserAuthPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__DUserAuthPlain_slots_without_collections__)
        for i in range(len(__DUserAuthPlain_slots_without_collections__)):
            setattr(self, __DUserAuthPlain_slots_without_collections__[i], state[i])
__EExtOrgPlain_slots_without_collections__ = ('id', 'header_row', 'outsider', 'name', 'alias', 'company_code', 'upper_ext_org_id', 'ext_org_type_id', 'ext_org_profile', 'virtual_org', 'contract_id', 'favorite', 'show_in_student', 'starting_date', 'termination_date', 'status', 'ext_superior_id', 'substitute_active', 'manager_id', 'superior_name', 'superior_email', 'subst_manager_id', 'subst_s_name', 'subst_s_email', 'teamleader_person_id', 'teamleader_name', 'teamleader_email', 'hr_manager_person_id', 'hr_manager_name', 'hr_manager_email', 'ext_contact_name', 'ext_contact_phone', 'ext_contact_email', 'description', 'unit_id_1', 'unit_id_2', 'costcenter_id', 'financial_code_1', 'location_id', 'location_info', 'exc_street', 'exc_street2', 'exc_post', 'exc_city', 'exc_state', 'exc_country', 'exc_office_phone', 'exc_office_fax', 'exc_office_timezone', 'exc_site_category', 'needs_int_contact_approval', 'needs_ext_contact_approval', 'default_language_id', 'default_jobrole_id', 'default_domain', 'distinguishedname', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_ext_org_id__name', 'ext_org_type_id__name', 'ext_superior_id__name', 'manager_id__name', 'subst_manager_id__name', 'teamleader_person_id__name', 'hr_manager_person_id__name', 'costcenter_id__name', 'location_id__name', 'exc_country__name', 'default_language_id__name', 'default_jobrole_id__name', 'valid', 'valid2'  )
class EExtOrgPlain(object):
    __slots__ = ('id', 'header_row', 'outsider', 'name', 'alias', 'company_code', 'upper_ext_org_id', 'ext_org_type_id', 'ext_org_profile', 'virtual_org', 'contract_id', 'favorite', 'show_in_student', 'starting_date', 'termination_date', 'status', 'ext_superior_id', 'substitute_active', 'manager_id', 'superior_name', 'superior_email', 'subst_manager_id', 'subst_s_name', 'subst_s_email', 'teamleader_person_id', 'teamleader_name', 'teamleader_email', 'hr_manager_person_id', 'hr_manager_name', 'hr_manager_email', 'ext_contact_name', 'ext_contact_phone', 'ext_contact_email', 'description', 'unit_id_1', 'unit_id_2', 'costcenter_id', 'financial_code_1', 'location_id', 'location_info', 'exc_street', 'exc_street2', 'exc_post', 'exc_city', 'exc_state', 'exc_country', 'exc_office_phone', 'exc_office_fax', 'exc_office_timezone', 'exc_site_category', 'needs_int_contact_approval', 'needs_ext_contact_approval', 'default_language_id', 'default_jobrole_id', 'default_domain', 'distinguishedname', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_ext_org_id__name', 'ext_org_type_id__name', 'ext_superior_id__name', 'manager_id__name', 'subst_manager_id__name', 'teamleader_person_id__name', 'hr_manager_person_id__name', 'costcenter_id__name', 'location_id__name', 'exc_country__name', 'default_language_id__name', 'default_jobrole_id__name', 'valid', 'valid2' , 'job_periods', 'services', 'service_roles', 'organization_groups' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EExtOrgPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EExtOrgPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EExtOrgPlain_slots_without_collections__)
        for i in range(len(__EExtOrgPlain_slots_without_collections__)):
            setattr(self, __EExtOrgPlain_slots_without_collections__[i], state[i])
__EExtOrgTypePlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class EExtOrgTypePlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EExtOrgTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EExtOrgTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EExtOrgTypePlain_slots_without_collections__)
        for i in range(len(__EExtOrgTypePlain_slots_without_collections__)):
            setattr(self, __EExtOrgTypePlain_slots_without_collections__[i], state[i])
__EExternalPersonPlain_slots_without_collections__ = ('id', 'name_prefix', 'first_name', 'middle_name', 'last_name', 'preferred_name', 'identity_id', 'social_security_number', 'personnel_number', 'information_checked', 'student', 'email_active', 'photo', 'username', 'orig_orgunit_id', 'ext_org_id', 'e_job_role_id', 'contract_id', 'tax_number', 'org_email', 'b_phone', 'b_mobile', 'pupo', 'sv_number', 'other_address', 'ext_email', 'ext_superior', 'ext_superior_email', 'starting_date', 'termination_date', 'termination_type', 'recertification_date', 'ext_phone', 'language_id', 'status', 'e_status1', 'e_status2', 'e_status3', 'e_status4', 'orgunit_id', 'jr_start_date', 'is_manager', 'jobtitle', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'exc_costcenter_id', 'exc_location_id', 'manager_id', 'manager_name', 'manager_email', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'remote_office', 'location_info', 'home_street', 'home_street2', 'home_post', 'home_city', 'home_state', 'homecountry_id', 'home_emergency_contact', 'home_timezone', 'identity_checked', 'identitysource_id', 'personal_id', 'staff_oper_code', 'full_time', 'birth_date', 'gender', 'nationality_id', 'mdm_source_id', 'mdm_person_id', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'last_checking_date', 'last_import_date', 'absence_status', 'exc_businessarea_id', 'exc_legalcompany_id', 'exc_country_id', 'waiting_manager_approval', 'manager_approved_id', 'manager_approval_timestamp', 'first_email_sent_timestamp', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'identity_id__name', 'orig_orgunit_id__name', 'ext_org_id__name', 'e_job_role_id__name', 'language_id__name', 'orgunit_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'exc_costcenter_id__name', 'exc_location_id__name', 'manager_id__name', 'subst_manager_id__name', 'homecountry_id__name', 'identitysource_id__name', 'nationality_id__name', 'mdm_source_id__name', 'exc_businessarea_id__name', 'exc_legalcompany_id__name', 'exc_country_id__name', 'manager_approved_id__name', 'valid', 'valid2'  )
class EExternalPersonPlain(object):
    __slots__ = ('id', 'name_prefix', 'first_name', 'middle_name', 'last_name', 'preferred_name', 'identity_id', 'social_security_number', 'personnel_number', 'information_checked', 'student', 'email_active', 'photo', 'username', 'orig_orgunit_id', 'ext_org_id', 'e_job_role_id', 'contract_id', 'tax_number', 'org_email', 'b_phone', 'b_mobile', 'pupo', 'sv_number', 'other_address', 'ext_email', 'ext_superior', 'ext_superior_email', 'starting_date', 'termination_date', 'termination_type', 'recertification_date', 'ext_phone', 'language_id', 'status', 'e_status1', 'e_status2', 'e_status3', 'e_status4', 'orgunit_id', 'jr_start_date', 'is_manager', 'jobtitle', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'exc_costcenter_id', 'exc_location_id', 'manager_id', 'manager_name', 'manager_email', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'remote_office', 'location_info', 'home_street', 'home_street2', 'home_post', 'home_city', 'home_state', 'homecountry_id', 'home_emergency_contact', 'home_timezone', 'identity_checked', 'identitysource_id', 'personal_id', 'staff_oper_code', 'full_time', 'birth_date', 'gender', 'nationality_id', 'mdm_source_id', 'mdm_person_id', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'last_checking_date', 'last_import_date', 'absence_status', 'exc_businessarea_id', 'exc_legalcompany_id', 'exc_country_id', 'waiting_manager_approval', 'manager_approved_id', 'manager_approval_timestamp', 'first_email_sent_timestamp', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'identity_id__name', 'orig_orgunit_id__name', 'ext_org_id__name', 'e_job_role_id__name', 'language_id__name', 'orgunit_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'exc_costcenter_id__name', 'exc_location_id__name', 'manager_id__name', 'subst_manager_id__name', 'homecountry_id__name', 'identitysource_id__name', 'nationality_id__name', 'mdm_source_id__name', 'exc_businessarea_id__name', 'exc_legalcompany_id__name', 'exc_country_id__name', 'manager_approved_id__name', 'valid', 'valid2' , 'cards', 'keys', 'devices', 'job_periods', 'manager_in_external_job_periods', 'absences', 'user_accounts', 'education', 'competences' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EExternalPersonPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EExternalPersonPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EExternalPersonPlain_slots_without_collections__)
        for i in range(len(__EExternalPersonPlain_slots_without_collections__)):
            setattr(self, __EExternalPersonPlain_slots_without_collections__[i], state[i])
__EJobFamilyPlain_slots_without_collections__ = ('id', 'name', 'int_code', 'description', 'starting_date', 'termination_date', 'jobfamily_class1', 'jobfamily_class2', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class EJobFamilyPlain(object):
    __slots__ = ('id', 'name', 'int_code', 'description', 'starting_date', 'termination_date', 'jobfamily_class1', 'jobfamily_class2', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EJobFamilyPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EJobFamilyPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EJobFamilyPlain_slots_without_collections__)
        for i in range(len(__EJobFamilyPlain_slots_without_collections__)):
            setattr(self, __EJobFamilyPlain_slots_without_collections__[i], state[i])
__EJobPeriodPlain_slots_without_collections__ = ('id', 'external_person_id', 'starting_date', 'termination_date', 'renewal_date', 'job_period_type', 'is_manager', 'student', 'outsider', 'orgunit_id', 'ext_org_id', 'job_title', 'other_job_title', 'specific_job_title', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'organization_association_type', 'status', 'ext_manager_id', 'manager_id', 'manager_email', 'manager_name', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'report_manager_id', 'org_unit_manager_id', 'information_checked', 'contract', 'medicine_right', 'hr_job_type', 'c_pasu', 'full_part_per', 'hr_work_time_type', 'operative_staff', 'int_period_id', 'int_job_title', 'int_job_code', 'int_job_code2', 'hr_profession_code', 'hr_period_character_code', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'pupo', 'phone', 'card_valid_from', 'card_valid_to', 'can_get_credentials', 'absence_active', 'exc_username', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_location_id', 'exc_country_id', 'exc_primary_period', 'inferred_primary_job_period', 'externally_managed', 'exported_to_idm', 'created_by_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'external_person_id__name', 'orgunit_id__name', 'ext_org_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'ext_manager_id__name', 'manager_id__name', 'subst_manager_id__name', 'report_manager_id__name', 'org_unit_manager_id__name', 'exc_legalcompany_id__name', 'exc_costcenter_id__name', 'exc_location_id__name', 'exc_country_id__name', 'created_by_id__name', 'valid', 'valid2', 'valid_to_show'  )
class EJobPeriodPlain(object):
    __slots__ = ('id', 'external_person_id', 'starting_date', 'termination_date', 'renewal_date', 'job_period_type', 'is_manager', 'student', 'outsider', 'orgunit_id', 'ext_org_id', 'job_title', 'other_job_title', 'specific_job_title', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'organization_association_type', 'status', 'ext_manager_id', 'manager_id', 'manager_email', 'manager_name', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'report_manager_id', 'org_unit_manager_id', 'information_checked', 'contract', 'medicine_right', 'hr_job_type', 'c_pasu', 'full_part_per', 'hr_work_time_type', 'operative_staff', 'int_period_id', 'int_job_title', 'int_job_code', 'int_job_code2', 'hr_profession_code', 'hr_period_character_code', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'pupo', 'phone', 'card_valid_from', 'card_valid_to', 'can_get_credentials', 'absence_active', 'exc_username', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_location_id', 'exc_country_id', 'exc_primary_period', 'inferred_primary_job_period', 'externally_managed', 'exported_to_idm', 'created_by_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'external_person_id__name', 'orgunit_id__name', 'ext_org_id__name', 'jobtitle_id__name', 'jobfamily_id__name', 'jobrole_id__name', 'ext_manager_id__name', 'manager_id__name', 'subst_manager_id__name', 'report_manager_id__name', 'org_unit_manager_id__name', 'exc_legalcompany_id__name', 'exc_costcenter_id__name', 'exc_location_id__name', 'exc_country_id__name', 'created_by_id__name', 'valid', 'valid2', 'valid_to_show' , 'absences', 'requested_permissions', 'organization_units' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EJobPeriodPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EJobPeriodPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EJobPeriodPlain_slots_without_collections__)
        for i in range(len(__EJobPeriodPlain_slots_without_collections__)):
            setattr(self, __EJobPeriodPlain_slots_without_collections__[i], state[i])
__EJobPeriodAbsencePlain_slots_without_collections__ = ('e_job_period_id', 'valid_from', 'created_by', 'start_date', 'end_date', 'description'
    , 'id__name', 'e_job_period_id__name', 'created_by__name'  )
class EJobPeriodAbsencePlain(object):
    __slots__ = ('e_job_period_id', 'valid_from', 'created_by', 'start_date', 'end_date', 'description'
    , 'id__name', 'e_job_period_id__name', 'created_by__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EJobPeriodAbsencePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EJobPeriodAbsencePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EJobPeriodAbsencePlain_slots_without_collections__)
        for i in range(len(__EJobPeriodAbsencePlain_slots_without_collections__)):
            setattr(self, __EJobPeriodAbsencePlain_slots_without_collections__[i], state[i])
__EJobPeriodSubstitutePlain_slots_without_collections__ = ('id', 'e_job_period_id', 'e_substistute_person_id', 'start_date', 'end_date', 'is_backup', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'e_job_period_id__name', 'e_substistute_person_id__name'  )
class EJobPeriodSubstitutePlain(object):
    __slots__ = ('id', 'e_job_period_id', 'e_substistute_person_id', 'start_date', 'end_date', 'is_backup', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'e_job_period_id__name', 'e_substistute_person_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EJobPeriodSubstitutePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EJobPeriodSubstitutePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EJobPeriodSubstitutePlain_slots_without_collections__)
        for i in range(len(__EJobPeriodSubstitutePlain_slots_without_collections__)):
            setattr(self, __EJobPeriodSubstitutePlain_slots_without_collections__[i], state[i])
__EJobRolePlain_slots_without_collections__ = ('id', 'name', 'int_code', 'description', 'global_jobrole', 'inheritance', 'orgunit_id', 'org_spec', 'upper_jobrole_id', 'starting_date', 'termination_date', 'provisioning', 'jobrole_class1', 'jobrole_class2', 'jobfamily_id', 'status', 'favorite', 'org_group_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'upper_jobrole_id__name', 'jobfamily_id__name', 'org_group_id__name'  )
class EJobRolePlain(object):
    __slots__ = ('id', 'name', 'int_code', 'description', 'global_jobrole', 'inheritance', 'orgunit_id', 'org_spec', 'upper_jobrole_id', 'starting_date', 'termination_date', 'provisioning', 'jobrole_class1', 'jobrole_class2', 'jobfamily_id', 'status', 'favorite', 'org_group_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'upper_jobrole_id__name', 'jobfamily_id__name', 'org_group_id__name' , 'service_roles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EJobRolePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EJobRolePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EJobRolePlain_slots_without_collections__)
        for i in range(len(__EJobRolePlain_slots_without_collections__)):
            setattr(self, __EJobRolePlain_slots_without_collections__[i], state[i])
__EOrgTypeServicePlain_slots_without_collections__ = ('id', 'ext_org_type_id', 'service_id', 'name', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'ext_org_type_id__name', 'service_id__name'  )
class EOrgTypeServicePlain(object):
    __slots__ = ('id', 'ext_org_type_id', 'service_id', 'name', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'ext_org_type_id__name', 'service_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __EOrgTypeServicePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __EOrgTypeServicePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__EOrgTypeServicePlain_slots_without_collections__)
        for i in range(len(__EOrgTypeServicePlain_slots_without_collections__)):
            setattr(self, __EOrgTypeServicePlain_slots_without_collections__[i], state[i])
__ERequestCartPlain_slots_without_collections__ = ('id', 'person_id', 'job_period_id', 'requestor_id', 'starting_date', 'manager_id', 'request_type', 'reason', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'approval_status', 'approval_comment', 'subst_approver_id', 'subst_approver_email', 'forced_hidden', 'approver_id', 'auto_approved', 'approval_time', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_address', 'reject_email_sent', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'job_period_id__name', 'requestor_id__name', 'manager_id__name', 'preferred_implementor_id__name', 'subst_approver_id__name', 'approver_id__name'  )
class ERequestCartPlain(object):
    __slots__ = ('id', 'person_id', 'job_period_id', 'requestor_id', 'starting_date', 'manager_id', 'request_type', 'reason', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'approval_status', 'approval_comment', 'subst_approver_id', 'subst_approver_email', 'forced_hidden', 'approver_id', 'auto_approved', 'approval_time', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_address', 'reject_email_sent', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'job_period_id__name', 'requestor_id__name', 'manager_id__name', 'preferred_implementor_id__name', 'subst_approver_id__name', 'approver_id__name' , 'permissions' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ERequestCartPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ERequestCartPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ERequestCartPlain_slots_without_collections__)
        for i in range(len(__ERequestCartPlain_slots_without_collections__)):
            setattr(self, __ERequestCartPlain_slots_without_collections__[i], state[i])
__ERequestCartPermissionPlain_slots_without_collections__ = ('id', 'request_cart_id', 'person_id', 'service_role_id', 'requestor_id', 'request_activation_date', 'permission_request_type', 'service_id', 'description', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'start_date', 'end_date', 'period_yr', 'approval_status', 'approver_id', 'auto_approved', 'approval_timestamp', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'email_to_service_manager_sent', 'email_to_requestor_sent', 'reject_email_sent', 'source_system_name', 'source_system_id', 'associated_orgunits_json', 'associated_ext_orgs_json', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'request_cart_id__name', 'person_id__name', 'service_role_id__name', 'requestor_id__name', 'service_id__name', 'preferred_implementor_id__name', 'approver_id__name'  )
class ERequestCartPermissionPlain(object):
    __slots__ = ('id', 'request_cart_id', 'person_id', 'service_role_id', 'requestor_id', 'request_activation_date', 'permission_request_type', 'service_id', 'description', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'start_date', 'end_date', 'period_yr', 'approval_status', 'approver_id', 'auto_approved', 'approval_timestamp', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'email_to_service_manager_sent', 'email_to_requestor_sent', 'reject_email_sent', 'source_system_name', 'source_system_id', 'associated_orgunits_json', 'associated_ext_orgs_json', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'request_cart_id__name', 'person_id__name', 'service_role_id__name', 'requestor_id__name', 'service_id__name', 'preferred_implementor_id__name', 'approver_id__name' , 'informed_persons' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ERequestCartPermissionPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))
        self.associated_orgunits_json = None if db_obj.associated_orgunits_json is None else ujson.loads(db_obj.associated_orgunits_json)
        self.associated_ext_orgs_json = None if db_obj.associated_ext_orgs_json is None else ujson.loads(db_obj.associated_ext_orgs_json)

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ERequestCartPermissionPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ERequestCartPermissionPlain_slots_without_collections__)
        for i in range(len(__ERequestCartPermissionPlain_slots_without_collections__)):
            setattr(self, __ERequestCartPermissionPlain_slots_without_collections__[i], state[i])
__GAccountAttributePlain_slots_without_collections__ = ('id', 'person_useraccount_id', 'value', 'value_p_old', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_useraccount_id__name'  )
class GAccountAttributePlain(object):
    __slots__ = ('id', 'person_useraccount_id', 'value', 'value_p_old', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_useraccount_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GAccountAttributePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GAccountAttributePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GAccountAttributePlain_slots_without_collections__)
        for i in range(len(__GAccountAttributePlain_slots_without_collections__)):
            setattr(self, __GAccountAttributePlain_slots_without_collections__[i], state[i])
__GAcePlain_slots_without_collections__ = ('id', 'name', 'description', 'ace_types', 'value', 'ace_key', 'ace_key_priority', 'attribute_source', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'attribute_source__name'  )
class GAcePlain(object):
    __slots__ = ('id', 'name', 'description', 'ace_types', 'value', 'ace_key', 'ace_key_priority', 'attribute_source', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'attribute_source__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GAcePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GAcePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GAcePlain_slots_without_collections__)
        for i in range(len(__GAcePlain_slots_without_collections__)):
            setattr(self, __GAcePlain_slots_without_collections__[i], state[i])
__GAceAttributePlain_slots_without_collections__ = ('id', 'name', 'description', 'source_entity', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GAceAttributePlain(object):
    __slots__ = ('id', 'name', 'description', 'source_entity', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GAceAttributePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GAceAttributePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GAceAttributePlain_slots_without_collections__)
        for i in range(len(__GAceAttributePlain_slots_without_collections__)):
            setattr(self, __GAceAttributePlain_slots_without_collections__[i], state[i])
__GCountryPlain_slots_without_collections__ = ('id', 'code', 'name', 'region', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'region__name'  )
class GCountryPlain(object):
    __slots__ = ('id', 'code', 'name', 'region', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'region__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GCountryPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GCountryPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GCountryPlain_slots_without_collections__)
        for i in range(len(__GCountryPlain_slots_without_collections__)):
            setattr(self, __GCountryPlain_slots_without_collections__[i], state[i])
__GIdentityPlain_slots_without_collections__ = ('id', 'first_name', 'last_name', 'personal_id', 'id_validity', 'identitysource_id', 'identified_by', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'identitysource_id__name'  )
class GIdentityPlain(object):
    __slots__ = ('id', 'first_name', 'last_name', 'personal_id', 'id_validity', 'identitysource_id', 'identified_by', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'identitysource_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GIdentityPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GIdentityPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GIdentityPlain_slots_without_collections__)
        for i in range(len(__GIdentityPlain_slots_without_collections__)):
            setattr(self, __GIdentityPlain_slots_without_collections__[i], state[i])
__GIdentitySourcePlain_slots_without_collections__ = ('id', 'name', 'description', 'identitysourcetype', 'identitysourceclass', 'source_update', 'resp_name', 'resp_email', 'resp_phone', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GIdentitySourcePlain(object):
    __slots__ = ('id', 'name', 'description', 'identitysourcetype', 'identitysourceclass', 'source_update', 'resp_name', 'resp_email', 'resp_phone', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GIdentitySourcePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GIdentitySourcePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GIdentitySourcePlain_slots_without_collections__)
        for i in range(len(__GIdentitySourcePlain_slots_without_collections__)):
            setattr(self, __GIdentitySourcePlain_slots_without_collections__[i], state[i])
__GLanguagePlain_slots_without_collections__ = ('id', 'code', 'name', 'iso_code', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GLanguagePlain(object):
    __slots__ = ('id', 'code', 'name', 'iso_code', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GLanguagePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GLanguagePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GLanguagePlain_slots_without_collections__)
        for i in range(len(__GLanguagePlain_slots_without_collections__)):
            setattr(self, __GLanguagePlain_slots_without_collections__[i], state[i])
__GMdmRulePlain_slots_without_collections__ = ('id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GMdmRulePlain(object):
    __slots__ = ('id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GMdmRulePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GMdmRulePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GMdmRulePlain_slots_without_collections__)
        for i in range(len(__GMdmRulePlain_slots_without_collections__)):
            setattr(self, __GMdmRulePlain_slots_without_collections__[i], state[i])
__GMdmSourcePlain_slots_without_collections__ = ('id', 'name', 'description', 'source_type', 'source_class', 'update_cycle', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GMdmSourcePlain(object):
    __slots__ = ('id', 'name', 'description', 'source_type', 'source_class', 'update_cycle', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GMdmSourcePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GMdmSourcePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GMdmSourcePlain_slots_without_collections__)
        for i in range(len(__GMdmSourcePlain_slots_without_collections__)):
            setattr(self, __GMdmSourcePlain_slots_without_collections__[i], state[i])
__GNotificationPlain_slots_without_collections__ = ('id', 'name', 'description', 'notification_type', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GNotificationPlain(object):
    __slots__ = ('id', 'name', 'description', 'notification_type', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'email_queues' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GNotificationPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GNotificationPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GNotificationPlain_slots_without_collections__)
        for i in range(len(__GNotificationPlain_slots_without_collections__)):
            setattr(self, __GNotificationPlain_slots_without_collections__[i], state[i])
__GNotificationQueuePlain_slots_without_collections__ = ('id', 'notification_id', 'sender', 'recipients', 'recipient_user', 'recipient_user_group', 'notification_data', 'notification_settings', 'notification_body', 'person_id', 'external_person_id', 'd_job_period_id', 'e_job_period_id', 'notified_at', 'notification_queue_status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'notification_id__name', 'recipient_user__name', 'recipient_user_group__name', 'person_id__name', 'external_person_id__name', 'd_job_period_id__name', 'e_job_period_id__name'  )
class GNotificationQueuePlain(object):
    __slots__ = ('id', 'notification_id', 'sender', 'recipients', 'recipient_user', 'recipient_user_group', 'notification_data', 'notification_settings', 'notification_body', 'person_id', 'external_person_id', 'd_job_period_id', 'e_job_period_id', 'notified_at', 'notification_queue_status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'notification_id__name', 'recipient_user__name', 'recipient_user_group__name', 'person_id__name', 'external_person_id__name', 'd_job_period_id__name', 'e_job_period_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GNotificationQueuePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GNotificationQueuePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GNotificationQueuePlain_slots_without_collections__)
        for i in range(len(__GNotificationQueuePlain_slots_without_collections__)):
            setattr(self, __GNotificationQueuePlain_slots_without_collections__[i], state[i])
__GPermissionPlain_slots_without_collections__ = ('id', 'd_job_period_id', 'e_job_period_id', 'service_role_id', 'start_date', 'end_date', 'period_yr', 'description', 'preferred_implementor_id', 'requested_by_id', 'requested_time', 'accepted_by_id', 'accepted_by_time', 'source_system_name', 'source_system_id', 'username', 'password', 'imported', 'status', 'request_cart_permission_id', 'e_request_cart_permission_id', 'delete_request_cart_permission_id', 'delete_e_request_cart_permission_id', 'd_job_period_substitute_id', 'e_job_period_substitute_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'd_job_period_id__name', 'e_job_period_id__name', 'service_role_id__name', 'preferred_implementor_id__name', 'requested_by_id__name', 'accepted_by_id__name', 'request_cart_permission_id__name', 'e_request_cart_permission_id__name', 'delete_request_cart_permission_id__name', 'delete_e_request_cart_permission_id__name', 'd_job_period_substitute_id__name', 'e_job_period_substitute_id__name', 'valid', 'valid2'  )
class GPermissionPlain(object):
    __slots__ = ('id', 'd_job_period_id', 'e_job_period_id', 'service_role_id', 'start_date', 'end_date', 'period_yr', 'description', 'preferred_implementor_id', 'requested_by_id', 'requested_time', 'accepted_by_id', 'accepted_by_time', 'source_system_name', 'source_system_id', 'username', 'password', 'imported', 'status', 'request_cart_permission_id', 'e_request_cart_permission_id', 'delete_request_cart_permission_id', 'delete_e_request_cart_permission_id', 'd_job_period_substitute_id', 'e_job_period_substitute_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'd_job_period_id__name', 'e_job_period_id__name', 'service_role_id__name', 'preferred_implementor_id__name', 'requested_by_id__name', 'accepted_by_id__name', 'request_cart_permission_id__name', 'e_request_cart_permission_id__name', 'delete_request_cart_permission_id__name', 'delete_e_request_cart_permission_id__name', 'd_job_period_substitute_id__name', 'e_job_period_substitute_id__name', 'valid', 'valid2' , 'associated_organization_units', 'associated_external_organizations' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GPermissionPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GPermissionPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GPermissionPlain_slots_without_collections__)
        for i in range(len(__GPermissionPlain_slots_without_collections__)):
            setattr(self, __GPermissionPlain_slots_without_collections__[i], state[i])
__GPersonUseraccountPlain_slots_without_collections__ = ('id', 'person_id', 'external_person_id', 'username', 'account_name', 'account_uid', 'object_guid', 'dn', 'password', 'service_id', 'system_id', 'inbound_attributes_json', 'outbound_attributes_json', 'old_inbound_attributes_json', 'old_outbound_attributes_json', 'account_created', 'status', 'internal', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'service_id__name', 'system_id__name'  )
class GPersonUseraccountPlain(object):
    __slots__ = ('id', 'person_id', 'external_person_id', 'username', 'account_name', 'account_uid', 'object_guid', 'dn', 'password', 'service_id', 'system_id', 'inbound_attributes_json', 'outbound_attributes_json', 'old_inbound_attributes_json', 'old_outbound_attributes_json', 'account_created', 'status', 'internal', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'service_id__name', 'system_id__name' , 'provisioning_tasks' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GPersonUseraccountPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))
        self.inbound_attributes_json = None if db_obj.inbound_attributes_json is None else ujson.loads(db_obj.inbound_attributes_json)
        self.outbound_attributes_json = None if db_obj.outbound_attributes_json is None else ujson.loads(db_obj.outbound_attributes_json)
        self.old_inbound_attributes_json = None if db_obj.old_inbound_attributes_json is None else ujson.loads(db_obj.old_inbound_attributes_json)
        self.old_outbound_attributes_json = None if db_obj.old_outbound_attributes_json is None else ujson.loads(db_obj.old_outbound_attributes_json)

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GPersonUseraccountPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GPersonUseraccountPlain_slots_without_collections__)
        for i in range(len(__GPersonUseraccountPlain_slots_without_collections__)):
            setattr(self, __GPersonUseraccountPlain_slots_without_collections__[i], state[i])
__GProvisioningTaskPlain_slots_without_collections__ = ('id', 'person_id', 'external_person_id', 'd_job_period_id', 'e_job_period_id', 'service_id', 'task_type', 'value_date', 'service_role_id', 'preferred_implementor_id', 'request_description', 'implementation_description', 'implemented_by_id', 'inform_user', 'inform_superior', 'inform_others', 'provisioning_task_status', 'provisioning_type', 'system_id', 'person_useraccount_id', 'inbound_attributes_json', 'outbound_attributes_json', 'diff_json', 'error_json', 'integration_direction', 'task_settings', 'username', 'password', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'source_system_name', 'source_system_id', 'permission_id', 'request_cart_permission_id', 'e_request_cart_permission_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'd_job_period_id__name', 'e_job_period_id__name', 'service_id__name', 'service_role_id__name', 'preferred_implementor_id__name', 'implemented_by_id__name', 'system_id__name', 'person_useraccount_id__name', 'permission_id__name', 'request_cart_permission_id__name', 'e_request_cart_permission_id__name'  )
class GProvisioningTaskPlain(object):
    __slots__ = ('id', 'person_id', 'external_person_id', 'd_job_period_id', 'e_job_period_id', 'service_id', 'task_type', 'value_date', 'service_role_id', 'preferred_implementor_id', 'request_description', 'implementation_description', 'implemented_by_id', 'inform_user', 'inform_superior', 'inform_others', 'provisioning_task_status', 'provisioning_type', 'system_id', 'person_useraccount_id', 'inbound_attributes_json', 'outbound_attributes_json', 'diff_json', 'error_json', 'integration_direction', 'task_settings', 'username', 'password', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'source_system_name', 'source_system_id', 'permission_id', 'request_cart_permission_id', 'e_request_cart_permission_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'd_job_period_id__name', 'e_job_period_id__name', 'service_id__name', 'service_role_id__name', 'preferred_implementor_id__name', 'implemented_by_id__name', 'system_id__name', 'person_useraccount_id__name', 'permission_id__name', 'request_cart_permission_id__name', 'e_request_cart_permission_id__name' , 'aces' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GProvisioningTaskPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))
        self.inbound_attributes_json = None if db_obj.inbound_attributes_json is None else ujson.loads(db_obj.inbound_attributes_json)
        self.outbound_attributes_json = None if db_obj.outbound_attributes_json is None else ujson.loads(db_obj.outbound_attributes_json)
        self.diff_json = None if db_obj.diff_json is None else ujson.loads(db_obj.diff_json)
        self.error_json = None if db_obj.error_json is None else ujson.loads(db_obj.error_json)

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GProvisioningTaskPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GProvisioningTaskPlain_slots_without_collections__)
        for i in range(len(__GProvisioningTaskPlain_slots_without_collections__)):
            setattr(self, __GProvisioningTaskPlain_slots_without_collections__[i], state[i])
__GRegionPlain_slots_without_collections__ = ('id', 'code', 'name', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GRegionPlain(object):
    __slots__ = ('id', 'code', 'name', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GRegionPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GRegionPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GRegionPlain_slots_without_collections__)
        for i in range(len(__GRegionPlain_slots_without_collections__)):
            setattr(self, __GRegionPlain_slots_without_collections__[i], state[i])
__GServicePlain_slots_without_collections__ = ('id', 'name', 'name6', 'code', 'status', 'service_provider_id', 'starting_date', 'termination_date', 'description', 'service_class', 'service_type_id', 'system_id', 'user_type', 'register', 'upper_service_id', 'externals_allowed', 'service_category', 'approver_id', 'executor_id', 'revoke_type', 'grace_period', 'minimum_period', 'notification_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_provider_id__name', 'service_type_id__name', 'system_id__name', 'upper_service_id__name', 'approver_id__name', 'executor_id__name', 'notification_id__name', 'valid', 'valid2'  )
class GServicePlain(object):
    __slots__ = ('id', 'name', 'name6', 'code', 'status', 'service_provider_id', 'starting_date', 'termination_date', 'description', 'service_class', 'service_type_id', 'system_id', 'user_type', 'register', 'upper_service_id', 'externals_allowed', 'service_category', 'approver_id', 'executor_id', 'revoke_type', 'grace_period', 'minimum_period', 'notification_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_provider_id__name', 'service_type_id__name', 'system_id__name', 'upper_service_id__name', 'approver_id__name', 'executor_id__name', 'notification_id__name', 'valid', 'valid2'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServicePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServicePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServicePlain_slots_without_collections__)
        for i in range(len(__GServicePlain_slots_without_collections__)):
            setattr(self, __GServicePlain_slots_without_collections__[i], state[i])
__GServiceProviderPlain_slots_without_collections__ = ('id', 'name', 'description', 'country_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'country_id__name'  )
class GServiceProviderPlain(object):
    __slots__ = ('id', 'name', 'description', 'country_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'country_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServiceProviderPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServiceProviderPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServiceProviderPlain_slots_without_collections__)
        for i in range(len(__GServiceProviderPlain_slots_without_collections__)):
            setattr(self, __GServiceProviderPlain_slots_without_collections__[i], state[i])
__GServiceRequestPlain_slots_without_collections__ = ('id', 'name', 'description', 'trans_date', 'severity', 'sr_class', 'sr_type', 'reported_by_name', 'reported_by_email', 'reported_by_phone', 'int_resp_uid', 'person_id', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'int_resp_uid__name', 'person_id__name', 'service_id__name'  )
class GServiceRequestPlain(object):
    __slots__ = ('id', 'name', 'description', 'trans_date', 'severity', 'sr_class', 'sr_type', 'reported_by_name', 'reported_by_email', 'reported_by_phone', 'int_resp_uid', 'person_id', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'int_resp_uid__name', 'person_id__name', 'service_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServiceRequestPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServiceRequestPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServiceRequestPlain_slots_without_collections__)
        for i in range(len(__GServiceRequestPlain_slots_without_collections__)):
            setattr(self, __GServiceRequestPlain_slots_without_collections__[i], state[i])
__GServiceRespPlain_slots_without_collections__ = ('id', 'person_name', 'service_id', 'servicerole_id', 'resp_class', 'resp_type', 'resp_name', 'resp_username', 'resp_email', 'resp_phone', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name', 'servicerole_id__name'  )
class GServiceRespPlain(object):
    __slots__ = ('id', 'person_name', 'service_id', 'servicerole_id', 'resp_class', 'resp_type', 'resp_name', 'resp_username', 'resp_email', 'resp_phone', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name', 'servicerole_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServiceRespPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServiceRespPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServiceRespPlain_slots_without_collections__)
        for i in range(len(__GServiceRespPlain_slots_without_collections__)):
            setattr(self, __GServiceRespPlain_slots_without_collections__[i], state[i])
__GServiceRolePlain_slots_without_collections__ = ('id', 'name', 'name6', 'code', 'status', 'description', 'service_id', 'service_role_type', 'starting_date', 'termination_date', 'servicerole_class', 'virtual', 'needs_service_manager_approval', 'authentication_level', 'provisioning_type', 'aces_in_transaction', 'upper_servicerole_id', 'chain_service_role_id', 'executor_id', 'favorite', 'end_date_request', 'period_request', 'description_request', 'associated_organizations_request', 'approver_id', 'subst_approver_id', 'subst_approver_active', 'subst_approver_email', 'needs_superior_approval', 'notification_create', 'notification_update', 'notification_disable', 'notification_delete', 'notification_resetpassword', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name', 'upper_servicerole_id__name', 'chain_service_role_id__name', 'executor_id__name', 'approver_id__name', 'subst_approver_id__name', 'notification_create__name', 'notification_update__name', 'notification_disable__name', 'notification_delete__name', 'notification_resetpassword__name', 'valid', 'valid2'  )
class GServiceRolePlain(object):
    __slots__ = ('id', 'name', 'name6', 'code', 'status', 'description', 'service_id', 'service_role_type', 'starting_date', 'termination_date', 'servicerole_class', 'virtual', 'needs_service_manager_approval', 'authentication_level', 'provisioning_type', 'aces_in_transaction', 'upper_servicerole_id', 'chain_service_role_id', 'executor_id', 'favorite', 'end_date_request', 'period_request', 'description_request', 'associated_organizations_request', 'approver_id', 'subst_approver_id', 'subst_approver_active', 'subst_approver_email', 'needs_superior_approval', 'notification_create', 'notification_update', 'notification_disable', 'notification_delete', 'notification_resetpassword', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_id__name', 'upper_servicerole_id__name', 'chain_service_role_id__name', 'executor_id__name', 'approver_id__name', 'subst_approver_id__name', 'notification_create__name', 'notification_update__name', 'notification_disable__name', 'notification_delete__name', 'notification_resetpassword__name', 'valid', 'valid2' , 'aces', 'job_roles', 'external_job_roles', 'organization_units', 'external_organizations' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServiceRolePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServiceRolePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServiceRolePlain_slots_without_collections__)
        for i in range(len(__GServiceRolePlain_slots_without_collections__)):
            setattr(self, __GServiceRolePlain_slots_without_collections__[i], state[i])
__GServiceTypePlain_slots_without_collections__ = ('id', 'name', 'description', 'owner_id', 'service_type', 'externals_allowed', 'role_inheritance', 'site_collection', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'owner_id__name'  )
class GServiceTypePlain(object):
    __slots__ = ('id', 'name', 'description', 'owner_id', 'service_type', 'externals_allowed', 'role_inheritance', 'site_collection', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'owner_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServiceTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServiceTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServiceTypePlain_slots_without_collections__)
        for i in range(len(__GServiceTypePlain_slots_without_collections__)):
            setattr(self, __GServiceTypePlain_slots_without_collections__[i], state[i])
__GServiceTypeSrolesPlain_slots_without_collections__ = ('id', 'service_type_id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_type_id__name'  )
class GServiceTypeSrolesPlain(object):
    __slots__ = ('id', 'service_type_id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_type_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GServiceTypeSrolesPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GServiceTypeSrolesPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GServiceTypeSrolesPlain_slots_without_collections__)
        for i in range(len(__GServiceTypeSrolesPlain_slots_without_collections__)):
            setattr(self, __GServiceTypeSrolesPlain_slots_without_collections__[i], state[i])
__GSrParametersPlain_slots_without_collections__ = ('id', 'name', 'description', 'orgunit_id', 'resp_name', 'resp_email', 'resp_phone', 'backup_name', 'backup_email', 'backup_phone', 'start_date', 'end_date', 'sla_level', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name'  )
class GSrParametersPlain(object):
    __slots__ = ('id', 'name', 'description', 'orgunit_id', 'resp_name', 'resp_email', 'resp_phone', 'backup_name', 'backup_email', 'backup_phone', 'start_date', 'end_date', 'sla_level', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GSrParametersPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GSrParametersPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GSrParametersPlain_slots_without_collections__)
        for i in range(len(__GSrParametersPlain_slots_without_collections__)):
            setattr(self, __GSrParametersPlain_slots_without_collections__[i], state[i])
__GSrTransPlain_slots_without_collections__ = ('id', 'service_request_id', 'name', 'description', 'trans_date', 'oper_uid', 'oper_status', 'action_type', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_request_id__name', 'oper_uid__name'  )
class GSrTransPlain(object):
    __slots__ = ('id', 'service_request_id', 'name', 'description', 'trans_date', 'oper_uid', 'oper_status', 'action_type', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'service_request_id__name', 'oper_uid__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GSrTransPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GSrTransPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GSrTransPlain_slots_without_collections__)
        for i in range(len(__GSrTransPlain_slots_without_collections__)):
            setattr(self, __GSrTransPlain_slots_without_collections__[i], state[i])
__GSystemPlain_slots_without_collections__ = ('id', 'name', 'system_type', 'identifier', 'description', 'upper_system_id', 'inbound_schema_mapping_id', 'outbound_schema_mapping_id', 'config_json', 'batch_job_path', 'revoke_type', 'code', 'integration_direction', 'system_application_type', 'priority', 'status', 'notification_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_system_id__name', 'inbound_schema_mapping_id__name', 'outbound_schema_mapping_id__name', 'notification_id__name'  )
class GSystemPlain(object):
    __slots__ = ('id', 'name', 'system_type', 'identifier', 'description', 'upper_system_id', 'inbound_schema_mapping_id', 'outbound_schema_mapping_id', 'config_json', 'batch_job_path', 'revoke_type', 'code', 'integration_direction', 'system_application_type', 'priority', 'status', 'notification_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_system_id__name', 'inbound_schema_mapping_id__name', 'outbound_schema_mapping_id__name', 'notification_id__name' , 'services' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GSystemPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))
        self.config_json = None if db_obj.config_json is None else ujson.loads(db_obj.config_json)

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GSystemPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GSystemPlain_slots_without_collections__)
        for i in range(len(__GSystemPlain_slots_without_collections__)):
            setattr(self, __GSystemPlain_slots_without_collections__[i], state[i])
__GSystemSchemaPlain_slots_without_collections__ = ('id', 'name', 'module_path', 'uid', 'description', 'type', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GSystemSchemaPlain(object):
    __slots__ = ('id', 'name', 'module_path', 'uid', 'description', 'type', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GSystemSchemaPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GSystemSchemaPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GSystemSchemaPlain_slots_without_collections__)
        for i in range(len(__GSystemSchemaPlain_slots_without_collections__)):
            setattr(self, __GSystemSchemaPlain_slots_without_collections__[i], state[i])
__GSystemSchemaAttributePlain_slots_without_collections__ = ('id', 'system_schema_id', 'name', 'description', 'datatype', 'source_attribute', 'destination_attribute', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'system_schema_id__name'  )
class GSystemSchemaAttributePlain(object):
    __slots__ = ('id', 'system_schema_id', 'name', 'description', 'datatype', 'source_attribute', 'destination_attribute', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'system_schema_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GSystemSchemaAttributePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GSystemSchemaAttributePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GSystemSchemaAttributePlain_slots_without_collections__)
        for i in range(len(__GSystemSchemaAttributePlain_slots_without_collections__)):
            setattr(self, __GSystemSchemaAttributePlain_slots_without_collections__[i], state[i])
__GUserGroupPlain_slots_without_collections__ = ('id', 'name', 'description', 'usergroup_type', 'email', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class GUserGroupPlain(object):
    __slots__ = ('id', 'name', 'description', 'usergroup_type', 'email', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'users', 'report_subscriptions' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __GUserGroupPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __GUserGroupPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__GUserGroupPlain_slots_without_collections__)
        for i in range(len(__GUserGroupPlain_slots_without_collections__)):
            setattr(self, __GUserGroupPlain_slots_without_collections__[i], state[i])
__HrDesktopSubstPlain_slots_without_collections__ = ('id', 'hr_manager_person_number', 'hr_subst_person_number', 'starting_date', 'termination_date', 'hr_subst_status', 'hr_subst_message', 'hr_source_file', 'hr_source_row', 'created_at', 'manager_person_id', 'subst_person_id', 'manager_org_unit_manager_id', 'substitube_org_unit_manager_id', 'substitute_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'manager_person_id__name', 'subst_person_id__name', 'manager_org_unit_manager_id__name', 'substitube_org_unit_manager_id__name', 'substitute_id__name'  )
class HrDesktopSubstPlain(object):
    __slots__ = ('id', 'hr_manager_person_number', 'hr_subst_person_number', 'starting_date', 'termination_date', 'hr_subst_status', 'hr_subst_message', 'hr_source_file', 'hr_source_row', 'created_at', 'manager_person_id', 'subst_person_id', 'manager_org_unit_manager_id', 'substitube_org_unit_manager_id', 'substitute_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'manager_person_id__name', 'subst_person_id__name', 'manager_org_unit_manager_id__name', 'substitube_org_unit_manager_id__name', 'substitute_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __HrDesktopSubstPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __HrDesktopSubstPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__HrDesktopSubstPlain_slots_without_collections__)
        for i in range(len(__HrDesktopSubstPlain_slots_without_collections__)):
            setattr(self, __HrDesktopSubstPlain_slots_without_collections__[i], state[i])
__HrImportRecordPlain_slots_without_collections__ = ('id', 'entity', 'source', 'row', 'source_entity_id', 'mapped_entity_id', 'system_entity', 'system_entity_id', 'parent_entity', 'parent_source_entity_id', 'parent_record_id', 'parent_system_entity', 'parent_system_entity_id', 'display_name', 'error_code', 'error_json', 'previous_valid_hr_record_json', 'current_hr_record_json', 'fixed_record_json', 'fixed_attributes_json', 'mapped_attributes_json', 'correctable_error', 'imported_to_db', 'hr_status', 'previous_record_version_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'parent_record_id__name'  )
class HrImportRecordPlain(object):
    __slots__ = ('id', 'entity', 'source', 'row', 'source_entity_id', 'mapped_entity_id', 'system_entity', 'system_entity_id', 'parent_entity', 'parent_source_entity_id', 'parent_record_id', 'parent_system_entity', 'parent_system_entity_id', 'display_name', 'error_code', 'error_json', 'previous_valid_hr_record_json', 'current_hr_record_json', 'fixed_record_json', 'fixed_attributes_json', 'mapped_attributes_json', 'correctable_error', 'imported_to_db', 'hr_status', 'previous_record_version_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'parent_record_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __HrImportRecordPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))
        self.error_json = None if db_obj.error_json is None else ujson.loads(db_obj.error_json)
        self.previous_valid_hr_record_json = None if db_obj.previous_valid_hr_record_json is None else ujson.loads(db_obj.previous_valid_hr_record_json)
        self.current_hr_record_json = None if db_obj.current_hr_record_json is None else ujson.loads(db_obj.current_hr_record_json)
        self.fixed_record_json = None if db_obj.fixed_record_json is None else ujson.loads(db_obj.fixed_record_json)
        self.fixed_attributes_json = None if db_obj.fixed_attributes_json is None else ujson.loads(db_obj.fixed_attributes_json)
        self.mapped_attributes_json = None if db_obj.mapped_attributes_json is None else ujson.loads(db_obj.mapped_attributes_json)

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __HrImportRecordPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__HrImportRecordPlain_slots_without_collections__)
        for i in range(len(__HrImportRecordPlain_slots_without_collections__)):
            setattr(self, __HrImportRecordPlain_slots_without_collections__[i], state[i])
__HrIntegrationPlain_slots_without_collections__ = ('id', 'person_id', 'external_person_id', 'internal', 'last_name', 'first_names', 'person_number', 'social_security_number', 'username', 'email', 'jobtitle_id', 'hr_job_title', 'hr_official_job_title', 'orgunit_id', 'ext_org_id', 'legal_company_id', 'cost_center_id', 'location_id', 'hire_start_date', 'job_start_date', 'job_end_date', 'manager_id', 'org_unit_manager_id', 'phone', 'pupo', 'other_address', 'sv_number', 'hr_status', 'preferred_name', 'street_address', 'post_number', 'city', 'hr_profession_code', 'position_type', 'hr_work_time_type', 'job_type', 'hr_job_type', 'full_part_per', 'job_period_character', 'language_id', 'report_area', 'report_manager', 'report_manager_id', 'org_association_type', 'ext_email', 'ext_phone', 'ext_manager_id', 'ext_manager_hetu', 'ext_manager_name', 'ext_org_code', 'ext_org_contract_number', 'ext_org_name', 'orgunit_name', 'manager_hetu', 'manager_name', 'basic_applications', 'other_data', 'iloq_identifier', 'other_key_1', 'other_key_2', 'personnel_card', 'iloq_valid_till', 'additional_admittances', 'additional_admittances_validity', 'additional_information_1', 'identifier', 'valid_till', 'trans_date', 'batch_file_name', 'batch_messages', 'record_source', 'hr_language_lookup', 'hr_language_description', 'hr_job_period_id', 'hr_job_title_id', 'hr_department_id', 'hr_manager_id', 'is_manager', 'job_position_type', 'job_position', 'job_period_type', 'job_period_type_text', 'job_period_character_text', 'person_number2', 'integration_timestamp', 'pass2done', 'c_pasu', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'jobtitle_id__name', 'orgunit_id__name', 'ext_org_id__name', 'legal_company_id__name', 'cost_center_id__name', 'location_id__name', 'manager_id__name', 'org_unit_manager_id__name', 'language_id__name', 'report_manager_id__name', 'ext_manager_id__name'  )
class HrIntegrationPlain(object):
    __slots__ = ('id', 'person_id', 'external_person_id', 'internal', 'last_name', 'first_names', 'person_number', 'social_security_number', 'username', 'email', 'jobtitle_id', 'hr_job_title', 'hr_official_job_title', 'orgunit_id', 'ext_org_id', 'legal_company_id', 'cost_center_id', 'location_id', 'hire_start_date', 'job_start_date', 'job_end_date', 'manager_id', 'org_unit_manager_id', 'phone', 'pupo', 'other_address', 'sv_number', 'hr_status', 'preferred_name', 'street_address', 'post_number', 'city', 'hr_profession_code', 'position_type', 'hr_work_time_type', 'job_type', 'hr_job_type', 'full_part_per', 'job_period_character', 'language_id', 'report_area', 'report_manager', 'report_manager_id', 'org_association_type', 'ext_email', 'ext_phone', 'ext_manager_id', 'ext_manager_hetu', 'ext_manager_name', 'ext_org_code', 'ext_org_contract_number', 'ext_org_name', 'orgunit_name', 'manager_hetu', 'manager_name', 'basic_applications', 'other_data', 'iloq_identifier', 'other_key_1', 'other_key_2', 'personnel_card', 'iloq_valid_till', 'additional_admittances', 'additional_admittances_validity', 'additional_information_1', 'identifier', 'valid_till', 'trans_date', 'batch_file_name', 'batch_messages', 'record_source', 'hr_language_lookup', 'hr_language_description', 'hr_job_period_id', 'hr_job_title_id', 'hr_department_id', 'hr_manager_id', 'is_manager', 'job_position_type', 'job_position', 'job_period_type', 'job_period_type_text', 'job_period_character_text', 'person_number2', 'integration_timestamp', 'pass2done', 'c_pasu', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'jobtitle_id__name', 'orgunit_id__name', 'ext_org_id__name', 'legal_company_id__name', 'cost_center_id__name', 'location_id__name', 'manager_id__name', 'org_unit_manager_id__name', 'language_id__name', 'report_manager_id__name', 'ext_manager_id__name' , 'service_roles', 'other_organization_units', 'key_profiles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __HrIntegrationPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __HrIntegrationPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__HrIntegrationPlain_slots_without_collections__)
        for i in range(len(__HrIntegrationPlain_slots_without_collections__)):
            setattr(self, __HrIntegrationPlain_slots_without_collections__[i], state[i])
__HrIntegrationVaultPlain_slots_without_collections__ = ('id', 'name', 'description', 'loaded', 'dumped', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class HrIntegrationVaultPlain(object):
    __slots__ = ('id', 'name', 'description', 'loaded', 'dumped', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __HrIntegrationVaultPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __HrIntegrationVaultPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__HrIntegrationVaultPlain_slots_without_collections__)
        for i in range(len(__HrIntegrationVaultPlain_slots_without_collections__)):
            setattr(self, __HrIntegrationVaultPlain_slots_without_collections__[i], state[i])
__IBusinessAreaPlain_slots_without_collections__ = ('id', 'code', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class IBusinessAreaPlain(object):
    __slots__ = ('id', 'code', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IBusinessAreaPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IBusinessAreaPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IBusinessAreaPlain_slots_without_collections__)
        for i in range(len(__IBusinessAreaPlain_slots_without_collections__)):
            setattr(self, __IBusinessAreaPlain_slots_without_collections__[i], state[i])
__ICostCenterPlain_slots_without_collections__ = ('id', 'legalcompany_id', 'header_row', 'int_code', 'name', 'description', 'starting_date', 'termination_date', 'status', 'classification1', 'classification2', 'classification3', 'classification4', 'classification5', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'legalcompany_id__name'  )
class ICostCenterPlain(object):
    __slots__ = ('id', 'legalcompany_id', 'header_row', 'int_code', 'name', 'description', 'starting_date', 'termination_date', 'status', 'classification1', 'classification2', 'classification3', 'classification4', 'classification5', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'legalcompany_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ICostCenterPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ICostCenterPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ICostCenterPlain_slots_without_collections__)
        for i in range(len(__ICostCenterPlain_slots_without_collections__)):
            setattr(self, __ICostCenterPlain_slots_without_collections__[i], state[i])
__IJobFamilyPlain_slots_without_collections__ = ('id', 'name', 'int_code', 'description', 'starting_date', 'termination_date', 'jobfamily_class1', 'jobfamily_class2', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class IJobFamilyPlain(object):
    __slots__ = ('id', 'name', 'int_code', 'description', 'starting_date', 'termination_date', 'jobfamily_class1', 'jobfamily_class2', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IJobFamilyPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IJobFamilyPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IJobFamilyPlain_slots_without_collections__)
        for i in range(len(__IJobFamilyPlain_slots_without_collections__)):
            setattr(self, __IJobFamilyPlain_slots_without_collections__[i], state[i])
__IJobRolePlain_slots_without_collections__ = ('id', 'name', 'name6', 'int_code', 'description', 'global_jobrole', 'inheritance', 'orgunit_id', 'org_spec', 'upper_jobrole_id', 'starting_date', 'termination_date', 'jobrole_class1', 'jobrole_class2', 'jobfamily_id', 'status', 'org_group_id', 'favorite', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'upper_jobrole_id__name', 'jobfamily_id__name', 'org_group_id__name', 'valid', 'valid2'  )
class IJobRolePlain(object):
    __slots__ = ('id', 'name', 'name6', 'int_code', 'description', 'global_jobrole', 'inheritance', 'orgunit_id', 'org_spec', 'upper_jobrole_id', 'starting_date', 'termination_date', 'jobrole_class1', 'jobrole_class2', 'jobfamily_id', 'status', 'org_group_id', 'favorite', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'upper_jobrole_id__name', 'jobfamily_id__name', 'org_group_id__name', 'valid', 'valid2' , 'job_titles', 'service_roles', 'requestable_service_roles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IJobRolePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IJobRolePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IJobRolePlain_slots_without_collections__)
        for i in range(len(__IJobRolePlain_slots_without_collections__)):
            setattr(self, __IJobRolePlain_slots_without_collections__[i], state[i])
__ILegalCompanyPlain_slots_without_collections__ = ('id', 'name', 'description', 'official_company_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class ILegalCompanyPlain(object):
    __slots__ = ('id', 'name', 'description', 'official_company_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'services', 'service_roles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ILegalCompanyPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ILegalCompanyPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ILegalCompanyPlain_slots_without_collections__)
        for i in range(len(__ILegalCompanyPlain_slots_without_collections__)):
            setattr(self, __ILegalCompanyPlain_slots_without_collections__[i], state[i])
__ILocationPlain_slots_without_collections__ = ('id', 'name', 'description', 'upper_location_id', 'header_row', 'location_id', 'site_category', 'virtual_location', 'status', 'street', 'street2', 'post', 'city', 'state', 'country', 'office_phone', 'office_fax', 'office_timezone', 'site_manager_id', 'site_manager_name', 'site_manager_email', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_location_id__name', 'country__name', 'site_manager_id__name'  )
class ILocationPlain(object):
    __slots__ = ('id', 'name', 'description', 'upper_location_id', 'header_row', 'location_id', 'site_category', 'virtual_location', 'status', 'street', 'street2', 'post', 'city', 'state', 'country', 'office_phone', 'office_fax', 'office_timezone', 'site_manager_id', 'site_manager_name', 'site_manager_email', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_location_id__name', 'country__name', 'site_manager_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ILocationPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ILocationPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ILocationPlain_slots_without_collections__)
        for i in range(len(__ILocationPlain_slots_without_collections__)):
            setattr(self, __ILocationPlain_slots_without_collections__[i], state[i])
__IManagerPerProfessionPlain_slots_without_collections__ = ('id', 'orgunit_id', 'hr_profession_code', 'i_job_role_id', 'e_job_role_id', 'superior_person_id', 'superior_name', 'superior_email', 'subst_s_person_id', 'subst_s_name', 'subst_s_email', 'substitute_active', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'i_job_role_id__name', 'e_job_role_id__name', 'superior_person_id__name', 'subst_s_person_id__name'  )
class IManagerPerProfessionPlain(object):
    __slots__ = ('id', 'orgunit_id', 'hr_profession_code', 'i_job_role_id', 'e_job_role_id', 'superior_person_id', 'superior_name', 'superior_email', 'subst_s_person_id', 'subst_s_name', 'subst_s_email', 'substitute_active', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'i_job_role_id__name', 'e_job_role_id__name', 'superior_person_id__name', 'subst_s_person_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IManagerPerProfessionPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IManagerPerProfessionPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IManagerPerProfessionPlain_slots_without_collections__)
        for i in range(len(__IManagerPerProfessionPlain_slots_without_collections__)):
            setattr(self, __IManagerPerProfessionPlain_slots_without_collections__[i], state[i])
__IOrgGroupPlain_slots_without_collections__ = ('id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class IOrgGroupPlain(object):
    __slots__ = ('id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'organization_groups' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IOrgGroupPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IOrgGroupPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IOrgGroupPlain_slots_without_collections__)
        for i in range(len(__IOrgGroupPlain_slots_without_collections__)):
            setattr(self, __IOrgGroupPlain_slots_without_collections__[i], state[i])
__IOrgTypePlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class IOrgTypePlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IOrgTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IOrgTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IOrgTypePlain_slots_without_collections__)
        for i in range(len(__IOrgTypePlain_slots_without_collections__)):
            setattr(self, __IOrgTypePlain_slots_without_collections__[i], state[i])
__IOrgUnitPlain_slots_without_collections__ = ('id', 'name', 'name6', 'description', 'upper_orgunit_id', 'unit_id', 'orgtype_id', 'inheritance', 'header_row', 'pilot', 'org_level', 'virtual_unit', 'businessarea', 'legalcompany_id', 'costcenter_id', 'location_id', 'it_support_email', 'favorite', 'starting_date', 'termination_date', 'status', 'org_spec', 'unit_id_1', 'unit_id_2', 'financial_code_1', 'location_info', 'exc_street', 'exc_street2', 'exc_post', 'exc_city', 'exc_state', 'exc_country', 'exc_office_phone', 'exc_office_fax', 'exc_office_timezone', 'exc_site_category', 'manager_id', 'superior_name', 'superior_email', 'subst_manager_id', 'subst_s_name', 'subst_s_email', 'substitute_active', 'teamleader_person_id', 'teamleader_name', 'teamleader_email', 'hr_manager_person_id', 'hr_manager_name', 'hr_manager_email', 'default_language_id', 'default_jobrole_id', 'default_domain', 'provisioning_dirty', 'distinguishedname', 'codeserver_oid', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_orgunit_id__name', 'orgtype_id__name', 'businessarea__name', 'legalcompany_id__name', 'costcenter_id__name', 'location_id__name', 'exc_country__name', 'manager_id__name', 'subst_manager_id__name', 'teamleader_person_id__name', 'hr_manager_person_id__name', 'default_language_id__name', 'default_jobrole_id__name', 'valid', 'valid2'  )
class IOrgUnitPlain(object):
    __slots__ = ('id', 'name', 'name6', 'description', 'upper_orgunit_id', 'unit_id', 'orgtype_id', 'inheritance', 'header_row', 'pilot', 'org_level', 'virtual_unit', 'businessarea', 'legalcompany_id', 'costcenter_id', 'location_id', 'it_support_email', 'favorite', 'starting_date', 'termination_date', 'status', 'org_spec', 'unit_id_1', 'unit_id_2', 'financial_code_1', 'location_info', 'exc_street', 'exc_street2', 'exc_post', 'exc_city', 'exc_state', 'exc_country', 'exc_office_phone', 'exc_office_fax', 'exc_office_timezone', 'exc_site_category', 'manager_id', 'superior_name', 'superior_email', 'subst_manager_id', 'subst_s_name', 'subst_s_email', 'substitute_active', 'teamleader_person_id', 'teamleader_name', 'teamleader_email', 'hr_manager_person_id', 'hr_manager_name', 'hr_manager_email', 'default_language_id', 'default_jobrole_id', 'default_domain', 'provisioning_dirty', 'distinguishedname', 'codeserver_oid', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_orgunit_id__name', 'orgtype_id__name', 'businessarea__name', 'legalcompany_id__name', 'costcenter_id__name', 'location_id__name', 'exc_country__name', 'manager_id__name', 'subst_manager_id__name', 'teamleader_person_id__name', 'hr_manager_person_id__name', 'default_language_id__name', 'default_jobrole_id__name', 'valid', 'valid2' , 'job_periods', 'external_job_periods', 'requestable_services', 'predefined_service_roles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IOrgUnitPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IOrgUnitPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IOrgUnitPlain_slots_without_collections__)
        for i in range(len(__IOrgUnitPlain_slots_without_collections__)):
            setattr(self, __IOrgUnitPlain_slots_without_collections__[i], state[i])
__IOrgUnitManagerPlain_slots_without_collections__ = ('id', 'org_unit_id', 'manager_id', 'manager_type', 'activation_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'org_unit_id__name', 'manager_id__name'  )
class IOrgUnitManagerPlain(object):
    __slots__ = ('id', 'org_unit_id', 'manager_id', 'manager_type', 'activation_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'org_unit_id__name', 'manager_id__name' , 'substitutes' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IOrgUnitManagerPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IOrgUnitManagerPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IOrgUnitManagerPlain_slots_without_collections__)
        for i in range(len(__IOrgUnitManagerPlain_slots_without_collections__)):
            setattr(self, __IOrgUnitManagerPlain_slots_without_collections__[i], state[i])
__IOrgUnitManagerSubstitutePlain_slots_without_collections__ = ('id', 'org_unit_manager_id', 'subst_manager_id', 'start_date', 'end_date', 'hr_desktop_subst', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'org_unit_manager_id__name', 'subst_manager_id__name', 'hr_desktop_subst__name'  )
class IOrgUnitManagerSubstitutePlain(object):
    __slots__ = ('id', 'org_unit_manager_id', 'subst_manager_id', 'start_date', 'end_date', 'hr_desktop_subst', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'org_unit_manager_id__name', 'subst_manager_id__name', 'hr_desktop_subst__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __IOrgUnitManagerSubstitutePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __IOrgUnitManagerSubstitutePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__IOrgUnitManagerSubstitutePlain_slots_without_collections__)
        for i in range(len(__IOrgUnitManagerSubstitutePlain_slots_without_collections__)):
            setattr(self, __IOrgUnitManagerSubstitutePlain_slots_without_collections__[i], state[i])
__OneTimeLinkPlain_slots_without_collections__ = ('id', 'auth_token', 'entity_name', 'entity_id', 'expires', 'created_timestamp', 'used_timestamp', 'zuser_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'zuser_id__name'  )
class OneTimeLinkPlain(object):
    __slots__ = ('id', 'auth_token', 'entity_name', 'entity_id', 'expires', 'created_timestamp', 'used_timestamp', 'zuser_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'zuser_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __OneTimeLinkPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __OneTimeLinkPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__OneTimeLinkPlain_slots_without_collections__)
        for i in range(len(__OneTimeLinkPlain_slots_without_collections__)):
            setattr(self, __OneTimeLinkPlain_slots_without_collections__[i], state[i])
__PRequestCartPlain_slots_without_collections__ = ('id', 'job_period_id', 'e_job_period_id', 'social_security_number', 'person_id', 'external_person_id', 'internal', 'request_ssn', 'requestor_id', 'starting_date', 'manager_ssn', 'description', 'preferred_implementor_ssn', 'inform_user', 'inform_superior', 'inform_others', 'src_trans_date', 'status_in', 'request_cart_id', 'e_request_cart_id', 'hr_job_period_id', 'out_status', 'out_status_error_msg', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'job_period_id__name', 'e_job_period_id__name', 'person_id__name', 'external_person_id__name', 'requestor_id__name', 'request_cart_id__name', 'e_request_cart_id__name'  )
class PRequestCartPlain(object):
    __slots__ = ('id', 'job_period_id', 'e_job_period_id', 'social_security_number', 'person_id', 'external_person_id', 'internal', 'request_ssn', 'requestor_id', 'starting_date', 'manager_ssn', 'description', 'preferred_implementor_ssn', 'inform_user', 'inform_superior', 'inform_others', 'src_trans_date', 'status_in', 'request_cart_id', 'e_request_cart_id', 'hr_job_period_id', 'out_status', 'out_status_error_msg', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'job_period_id__name', 'e_job_period_id__name', 'person_id__name', 'external_person_id__name', 'requestor_id__name', 'request_cart_id__name', 'e_request_cart_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __PRequestCartPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __PRequestCartPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__PRequestCartPlain_slots_without_collections__)
        for i in range(len(__PRequestCartPlain_slots_without_collections__)):
            setattr(self, __PRequestCartPlain_slots_without_collections__[i], state[i])
__PRequestCartRowPlain_slots_without_collections__ = ('id', 'p_request_cart_id', 'permission_request_type', 'service_role_id', 'description', 'preferred_implementor_ssn', 'status_in', 'source_system_name', 'source_system_id', 'out_status', 'out_date', 'request_cart_row_id', 'e_request_cart_row_id', 'out_status_process', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'p_request_cart_id__name', 'service_role_id__name', 'request_cart_row_id__name', 'e_request_cart_row_id__name'  )
class PRequestCartRowPlain(object):
    __slots__ = ('id', 'p_request_cart_id', 'permission_request_type', 'service_role_id', 'description', 'preferred_implementor_ssn', 'status_in', 'source_system_name', 'source_system_id', 'out_status', 'out_date', 'request_cart_row_id', 'e_request_cart_row_id', 'out_status_process', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'p_request_cart_id__name', 'service_role_id__name', 'request_cart_row_id__name', 'e_request_cart_row_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __PRequestCartRowPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __PRequestCartRowPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__PRequestCartRowPlain_slots_without_collections__)
        for i in range(len(__PRequestCartRowPlain_slots_without_collections__)):
            setattr(self, __PRequestCartRowPlain_slots_without_collections__[i], state[i])
__RDynRolePlain_slots_without_collections__ = ('id', 'name', 'description', 'rule', 'approval_status', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class RDynRolePlain(object):
    __slots__ = ('id', 'name', 'description', 'rule', 'approval_status', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'service_roles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RDynRolePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RDynRolePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RDynRolePlain_slots_without_collections__)
        for i in range(len(__RDynRolePlain_slots_without_collections__)):
            setattr(self, __RDynRolePlain_slots_without_collections__[i], state[i])
__ROrgDacPlain_slots_without_collections__ = ('id', 'orgunit_id', 'name', 'dedicated', 'key1_min_value', 'key1_max_value', 'key2_min_value', 'key2_max_value', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name'  )
class ROrgDacPlain(object):
    __slots__ = ('id', 'orgunit_id', 'name', 'dedicated', 'key1_min_value', 'key1_max_value', 'key2_min_value', 'key2_max_value', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ROrgDacPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ROrgDacPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ROrgDacPlain_slots_without_collections__)
        for i in range(len(__ROrgDacPlain_slots_without_collections__)):
            setattr(self, __ROrgDacPlain_slots_without_collections__[i], state[i])
__ROrgServicePlain_slots_without_collections__ = ('id', 'name', 'orgunit_id', 'service_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'service_id__name'  )
class ROrgServicePlain(object):
    __slots__ = ('id', 'name', 'orgunit_id', 'service_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'orgunit_id__name', 'service_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ROrgServicePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ROrgServicePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ROrgServicePlain_slots_without_collections__)
        for i in range(len(__ROrgServicePlain_slots_without_collections__)):
            setattr(self, __ROrgServicePlain_slots_without_collections__[i], state[i])
__ROrgTypeServicePlain_slots_without_collections__ = ('id', 'name', 'org_type_id', 'service_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'org_type_id__name', 'service_id__name'  )
class ROrgTypeServicePlain(object):
    __slots__ = ('id', 'name', 'org_type_id', 'service_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'org_type_id__name', 'service_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ROrgTypeServicePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ROrgTypeServicePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ROrgTypeServicePlain_slots_without_collections__)
        for i in range(len(__ROrgTypeServicePlain_slots_without_collections__)):
            setattr(self, __ROrgTypeServicePlain_slots_without_collections__[i], state[i])
__RSodExceptionPlain_slots_without_collections__ = ('id', 'internal', 'person_id', 'external_person_id', 'sod_rule_id', 'exc_approved', 'exc_approver_id', 'exc_approver_desc', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'sod_rule_id__name', 'exc_approver_id__name'  )
class RSodExceptionPlain(object):
    __slots__ = ('id', 'internal', 'person_id', 'external_person_id', 'sod_rule_id', 'exc_approved', 'exc_approver_id', 'exc_approver_desc', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name', 'sod_rule_id__name', 'exc_approver_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RSodExceptionPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RSodExceptionPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RSodExceptionPlain_slots_without_collections__)
        for i in range(len(__RSodExceptionPlain_slots_without_collections__)):
            setattr(self, __RSodExceptionPlain_slots_without_collections__[i], state[i])
__RSodRulePlain_slots_without_collections__ = ('id', 'name', 'description', 'sod_rule_class_id', 'role1_id', 'role2_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'sod_rule_class_id__name', 'role1_id__name', 'role2_id__name'  )
class RSodRulePlain(object):
    __slots__ = ('id', 'name', 'description', 'sod_rule_class_id', 'role1_id', 'role2_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'sod_rule_class_id__name', 'role1_id__name', 'role2_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RSodRulePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RSodRulePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RSodRulePlain_slots_without_collections__)
        for i in range(len(__RSodRulePlain_slots_without_collections__)):
            setattr(self, __RSodRulePlain_slots_without_collections__[i], state[i])
__RSodRuleClassPlain_slots_without_collections__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class RSodRuleClassPlain(object):
    __slots__ = ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RSodRuleClassPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RSodRuleClassPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RSodRuleClassPlain_slots_without_collections__)
        for i in range(len(__RSodRuleClassPlain_slots_without_collections__)):
            setattr(self, __RSodRuleClassPlain_slots_without_collections__[i], state[i])
__RUserDacPlain_slots_without_collections__ = ('id', 'person_id', 'name', 'dedicated', 'key1_min_value', 'key1_max_value', 'key2_min_value', 'key2_max_value', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name'  )
class RUserDacPlain(object):
    __slots__ = ('id', 'person_id', 'name', 'dedicated', 'key1_min_value', 'key1_max_value', 'key2_min_value', 'key2_max_value', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RUserDacPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RUserDacPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RUserDacPlain_slots_without_collections__)
        for i in range(len(__RUserDacPlain_slots_without_collections__)):
            setattr(self, __RUserDacPlain_slots_without_collections__[i], state[i])
__RequestCartPlain_slots_without_collections__ = ('id', 'person_id', 'job_period_id', 'requestor_id', 'starting_date', 'manager_id', 'request_type', 'reason', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'approval_status', 'approval_comment', 'subst_approver_id', 'subst_approver_email', 'forced_hidden', 'approver_id', 'auto_approved', 'approval_time', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_address', 'reject_email_sent', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'job_period_id__name', 'requestor_id__name', 'manager_id__name', 'preferred_implementor_id__name', 'subst_approver_id__name', 'approver_id__name'  )
class RequestCartPlain(object):
    __slots__ = ('id', 'person_id', 'job_period_id', 'requestor_id', 'starting_date', 'manager_id', 'request_type', 'reason', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'approval_status', 'approval_comment', 'subst_approver_id', 'subst_approver_email', 'forced_hidden', 'approver_id', 'auto_approved', 'approval_time', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_address', 'reject_email_sent', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'job_period_id__name', 'requestor_id__name', 'manager_id__name', 'preferred_implementor_id__name', 'subst_approver_id__name', 'approver_id__name' , 'permissions' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RequestCartPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RequestCartPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RequestCartPlain_slots_without_collections__)
        for i in range(len(__RequestCartPlain_slots_without_collections__)):
            setattr(self, __RequestCartPlain_slots_without_collections__[i], state[i])
__RequestCartPermissionPlain_slots_without_collections__ = ('id', 'request_cart_id', 'person_id', 'service_role_id', 'requestor_id', 'request_activation_date', 'permission_request_type', 'service_id', 'description', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'start_date', 'end_date', 'period_yr', 'approval_status', 'approver_id', 'auto_approved', 'approval_timestamp', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'email_to_service_manager_sent', 'email_to_requestor_sent', 'reject_email_sent', 'source_system_name', 'source_system_id', 'associated_orgunits_json', 'associated_ext_orgs_json', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'request_cart_id__name', 'person_id__name', 'service_role_id__name', 'requestor_id__name', 'service_id__name', 'preferred_implementor_id__name', 'approver_id__name'  )
class RequestCartPermissionPlain(object):
    __slots__ = ('id', 'request_cart_id', 'person_id', 'service_role_id', 'requestor_id', 'request_activation_date', 'permission_request_type', 'service_id', 'description', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'start_date', 'end_date', 'period_yr', 'approval_status', 'approver_id', 'auto_approved', 'approval_timestamp', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'email_to_service_manager_sent', 'email_to_requestor_sent', 'reject_email_sent', 'source_system_name', 'source_system_id', 'associated_orgunits_json', 'associated_ext_orgs_json', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'request_cart_id__name', 'person_id__name', 'service_role_id__name', 'requestor_id__name', 'service_id__name', 'preferred_implementor_id__name', 'approver_id__name' , 'informed_persons' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __RequestCartPermissionPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))
        self.associated_orgunits_json = None if db_obj.associated_orgunits_json is None else ujson.loads(db_obj.associated_orgunits_json)
        self.associated_ext_orgs_json = None if db_obj.associated_ext_orgs_json is None else ujson.loads(db_obj.associated_ext_orgs_json)

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __RequestCartPermissionPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__RequestCartPermissionPlain_slots_without_collections__)
        for i in range(len(__RequestCartPermissionPlain_slots_without_collections__)):
            setattr(self, __RequestCartPermissionPlain_slots_without_collections__[i], state[i])
__SDDepartmentWeekMaxQuantityPlain_slots_without_collections__ = ('id', 'department_id', 'week', 'quantity', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'department_id__name'  )
class SDDepartmentWeekMaxQuantityPlain(object):
    __slots__ = ('id', 'department_id', 'week', 'quantity', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'department_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __SDDepartmentWeekMaxQuantityPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __SDDepartmentWeekMaxQuantityPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__SDDepartmentWeekMaxQuantityPlain_slots_without_collections__)
        for i in range(len(__SDDepartmentWeekMaxQuantityPlain_slots_without_collections__)):
            setattr(self, __SDDepartmentWeekMaxQuantityPlain_slots_without_collections__[i], state[i])
__SDStudyProgrammePlain_slots_without_collections__ = ('id', 'name', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class SDStudyProgrammePlain(object):
    __slots__ = ('id', 'name', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __SDStudyProgrammePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __SDStudyProgrammePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__SDStudyProgrammePlain_slots_without_collections__)
        for i in range(len(__SDStudyProgrammePlain_slots_without_collections__)):
            setattr(self, __SDStudyProgrammePlain_slots_without_collections__[i], state[i])
__SDTraineeshipPlacementPlain_slots_without_collections__ = ('id', 'traineeship_placement_request_id', 'student_slot_number', 'part_number', 'department_id', 'start_date', 'end_date', 'coordinator_id', 'traineeship_type_id', 'responsible_person_id', 'guiding_teacher_id', 'student_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'traineeship_placement_request_id__name', 'department_id__name', 'coordinator_id__name', 'traineeship_type_id__name', 'responsible_person_id__name', 'guiding_teacher_id__name', 'student_id__name'  )
class SDTraineeshipPlacementPlain(object):
    __slots__ = ('id', 'traineeship_placement_request_id', 'student_slot_number', 'part_number', 'department_id', 'start_date', 'end_date', 'coordinator_id', 'traineeship_type_id', 'responsible_person_id', 'guiding_teacher_id', 'student_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'traineeship_placement_request_id__name', 'department_id__name', 'coordinator_id__name', 'traineeship_type_id__name', 'responsible_person_id__name', 'guiding_teacher_id__name', 'student_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __SDTraineeshipPlacementPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __SDTraineeshipPlacementPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__SDTraineeshipPlacementPlain_slots_without_collections__)
        for i in range(len(__SDTraineeshipPlacementPlain_slots_without_collections__)):
            setattr(self, __SDTraineeshipPlacementPlain_slots_without_collections__[i], state[i])
__SDTraineeshipPlacementRequestPlain_slots_without_collections__ = ('id', 'traineeship_request_id', 'office_id', 'division_id', 'department_id', 'semester_information', 'traineeship_type_id', 'traineeship_type_other', 'length_weeks', 'start_date', 'end_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'traineeship_request_id__name', 'office_id__name', 'division_id__name', 'department_id__name', 'traineeship_type_id__name'  )
class SDTraineeshipPlacementRequestPlain(object):
    __slots__ = ('id', 'traineeship_request_id', 'office_id', 'division_id', 'department_id', 'semester_information', 'traineeship_type_id', 'traineeship_type_other', 'length_weeks', 'start_date', 'end_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'traineeship_request_id__name', 'office_id__name', 'division_id__name', 'department_id__name', 'traineeship_type_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __SDTraineeshipPlacementRequestPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __SDTraineeshipPlacementRequestPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__SDTraineeshipPlacementRequestPlain_slots_without_collections__)
        for i in range(len(__SDTraineeshipPlacementRequestPlain_slots_without_collections__)):
            setattr(self, __SDTraineeshipPlacementRequestPlain_slots_without_collections__[i], state[i])
__SDTraineeshipRequestPlain_slots_without_collections__ = ('id', 'school_id', 'study_programme_id', 'course_name', 'includes_skill_test', 'skill_test_type', 'advanced_course', 'international_student', 'international_school_name', 'extra_information', 'quantity_requested', 'request_status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'school_id__name', 'study_programme_id__name'  )
class SDTraineeshipRequestPlain(object):
    __slots__ = ('id', 'school_id', 'study_programme_id', 'course_name', 'includes_skill_test', 'skill_test_type', 'advanced_course', 'international_student', 'international_school_name', 'extra_information', 'quantity_requested', 'request_status', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'school_id__name', 'study_programme_id__name' , 'requests' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __SDTraineeshipRequestPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __SDTraineeshipRequestPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__SDTraineeshipRequestPlain_slots_without_collections__)
        for i in range(len(__SDTraineeshipRequestPlain_slots_without_collections__)):
            setattr(self, __SDTraineeshipRequestPlain_slots_without_collections__[i], state[i])
__SDTraineeshipTypePlain_slots_without_collections__ = ('id', 'name', 'upper_traineeship_type_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_traineeship_type_id__name'  )
class SDTraineeshipTypePlain(object):
    __slots__ = ('id', 'name', 'upper_traineeship_type_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'upper_traineeship_type_id__name'  , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __SDTraineeshipTypePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __SDTraineeshipTypePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__SDTraineeshipTypePlain_slots_without_collections__)
        for i in range(len(__SDTraineeshipTypePlain_slots_without_collections__)):
            setattr(self, __SDTraineeshipTypePlain_slots_without_collections__[i], state[i])
__UserightPlain_slots_without_collections__ = ('id', 'name', 'extra1', 'extra2', 'distinguished_name', 'righttype_lookup', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class UserightPlain(object):
    __slots__ = ('id', 'name', 'extra1', 'extra2', 'distinguished_name', 'righttype_lookup', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'roles' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __UserightPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __UserightPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__UserightPlain_slots_without_collections__)
        for i in range(len(__UserightPlain_slots_without_collections__)):
            setattr(self, __UserightPlain_slots_without_collections__[i], state[i])
__ZreportPlain_slots_without_collections__ = ('id', 'name', 'name5', 'name6', 'description', 'reportfile', 'url', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class ZreportPlain(object):
    __slots__ = ('id', 'name', 'name5', 'name6', 'description', 'reportfile', 'url', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'required_userights' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ZreportPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ZreportPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ZreportPlain_slots_without_collections__)
        for i in range(len(__ZreportPlain_slots_without_collections__)):
            setattr(self, __ZreportPlain_slots_without_collections__[i], state[i])
__ZrolePlain_slots_without_collections__ = ('id', 'name', 'description', 'distinguished_name', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name'  )
class ZrolePlain(object):
    __slots__ = ('id', 'name', 'description', 'distinguished_name', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name' , 'users', 'userights' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ZrolePlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ZrolePlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ZrolePlain_slots_without_collections__)
        for i in range(len(__ZrolePlain_slots_without_collections__)):
            setattr(self, __ZrolePlain_slots_without_collections__[i], state[i])
__ZuserPlain_slots_without_collections__ = ('id', 'username', 'first_names', 'last_name', 'email', 'address', 'phone', 'start_date', 'force_change_password', 'internal', 'person_id', 'external_person_id', 'status', 'liferay_uid', 'password', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name'  )
class ZuserPlain(object):
    __slots__ = ('id', 'username', 'first_names', 'last_name', 'email', 'address', 'phone', 'start_date', 'force_change_password', 'internal', 'person_id', 'external_person_id', 'status', 'liferay_uid', 'password', 'f_version', 'f_changed', 'f_changedby', 'deleted'
    , 'id__name', 'person_id__name', 'external_person_id__name' , 'usergroups', 'roles', 'organizations', 'external_organizations' , '__baseclass__')

    def __init__(self, db_obj):
        for attr in __ZuserPlain_slots_without_collections__:
            setattr(self, attr, getattr(db_obj, attr, None))

    def __getstate__(self):
        return tuple(getattr(self, x) for x in __ZuserPlain_slots_without_collections__)

    def __setstate__(self, state):
        assert len(state) == len(__ZuserPlain_slots_without_collections__)
        for i in range(len(__ZuserPlain_slots_without_collections__)):
            setattr(self, __ZuserPlain_slots_without_collections__[i], state[i])

def populate_fks(context):
    for obj in context[DJobPeriod].values():
        obj.person_id = context[DPerson].get(obj.person_id)
        obj.orgunit_id = context[IOrgUnit].get(obj.orgunit_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        obj.subst_manager_id = context[DPerson].get(obj.subst_manager_id)
        obj.report_manager_id = context[DPerson].get(obj.report_manager_id)
        obj.exc_legalcompany_id = context[ILegalCompany].get(obj.exc_legalcompany_id)
        obj.exc_location_id = context[ILocation].get(obj.exc_location_id)
        pass
    for obj in context[DPerson].values():
        obj.orgunit_id = context[IOrgUnit].get(obj.orgunit_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        obj.subst_manager_id = context[DPerson].get(obj.subst_manager_id)
        obj.exc_location_id = context[ILocation].get(obj.exc_location_id)
        obj.exc_legalcompany_id = context[ILegalCompany].get(obj.exc_legalcompany_id)
        pass
    for obj in context[EExtOrg].values():
        obj.upper_ext_org_id = context[EExtOrg].get(obj.upper_ext_org_id)
        obj.ext_superior_id = context[EExternalPerson].get(obj.ext_superior_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        obj.subst_manager_id = context[DPerson].get(obj.subst_manager_id)
        obj.teamleader_person_id = context[DPerson].get(obj.teamleader_person_id)
        obj.hr_manager_person_id = context[DPerson].get(obj.hr_manager_person_id)
        obj.location_id = context[ILocation].get(obj.location_id)
        pass
    for obj in context[EExternalPerson].values():
        obj.orig_orgunit_id = context[IOrgUnit].get(obj.orig_orgunit_id)
        obj.ext_org_id = context[EExtOrg].get(obj.ext_org_id)
        obj.orgunit_id = context[IOrgUnit].get(obj.orgunit_id)
        obj.exc_location_id = context[ILocation].get(obj.exc_location_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        obj.subst_manager_id = context[DPerson].get(obj.subst_manager_id)
        obj.exc_legalcompany_id = context[ILegalCompany].get(obj.exc_legalcompany_id)
        pass
    for obj in context[EJobPeriod].values():
        obj.external_person_id = context[EExternalPerson].get(obj.external_person_id)
        obj.orgunit_id = context[IOrgUnit].get(obj.orgunit_id)
        obj.ext_org_id = context[EExtOrg].get(obj.ext_org_id)
        obj.ext_manager_id = context[EExternalPerson].get(obj.ext_manager_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        obj.subst_manager_id = context[DPerson].get(obj.subst_manager_id)
        obj.report_manager_id = context[DPerson].get(obj.report_manager_id)
        obj.exc_legalcompany_id = context[ILegalCompany].get(obj.exc_legalcompany_id)
        obj.exc_location_id = context[ILocation].get(obj.exc_location_id)
        pass
    for obj in context[ERequestCart].values():
        obj.person_id = context[EExternalPerson].get(obj.person_id)
        obj.job_period_id = context[EJobPeriod].get(obj.job_period_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        pass
    for obj in context[ERequestCartPermission].values():
        obj.request_cart_id = context[ERequestCart].get(obj.request_cart_id)
        obj.person_id = context[EExternalPerson].get(obj.person_id)
        obj.service_role_id = context[GServiceRole].get(obj.service_role_id)
        obj.service_id = context[GService].get(obj.service_id)
        pass
    for obj in context[GAce].values():
        obj.attribute_source = context[GAceAttribute].get(obj.attribute_source)
        pass
    for obj in context[GAceAttribute].values():
        pass
    for obj in context[GPermission].values():
        obj.d_job_period_id = context[DJobPeriod].get(obj.d_job_period_id)
        obj.e_job_period_id = context[EJobPeriod].get(obj.e_job_period_id)
        obj.service_role_id = context[GServiceRole].get(obj.service_role_id)
        obj.request_cart_permission_id = context[RequestCartPermission].get(obj.request_cart_permission_id)
        obj.e_request_cart_permission_id = context[ERequestCartPermission].get(obj.e_request_cart_permission_id)
        obj.delete_request_cart_permission_id = context[RequestCartPermission].get(obj.delete_request_cart_permission_id)
        obj.delete_e_request_cart_permission_id = context[ERequestCartPermission].get(obj.delete_e_request_cart_permission_id)
        pass
    for obj in context[GPersonUseraccount].values():
        obj.person_id = context[DPerson].get(obj.person_id)
        obj.external_person_id = context[EExternalPerson].get(obj.external_person_id)
        obj.service_id = context[GService].get(obj.service_id)
        obj.system_id = context[GSystem].get(obj.system_id)
        pass
    for obj in context[GService].values():
        obj.system_id = context[GSystem].get(obj.system_id)
        obj.upper_service_id = context[GService].get(obj.upper_service_id)
        pass
    for obj in context[GServiceRole].values():
        obj.service_id = context[GService].get(obj.service_id)
        obj.upper_servicerole_id = context[GServiceRole].get(obj.upper_servicerole_id)
        obj.chain_service_role_id = context[GServiceRole].get(obj.chain_service_role_id)
        pass
    for obj in context[GSystem].values():
        obj.upper_system_id = context[GSystem].get(obj.upper_system_id)
        pass
    for obj in context[ILegalCompany].values():
        pass
    for obj in context[ILocation].values():
        obj.upper_location_id = context[ILocation].get(obj.upper_location_id)
        obj.site_manager_id = context[DPerson].get(obj.site_manager_id)
        pass
    for obj in context[IOrgUnit].values():
        obj.upper_orgunit_id = context[IOrgUnit].get(obj.upper_orgunit_id)
        obj.legalcompany_id = context[ILegalCompany].get(obj.legalcompany_id)
        obj.location_id = context[ILocation].get(obj.location_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        obj.subst_manager_id = context[DPerson].get(obj.subst_manager_id)
        obj.teamleader_person_id = context[DPerson].get(obj.teamleader_person_id)
        obj.hr_manager_person_id = context[DPerson].get(obj.hr_manager_person_id)
        pass
    for obj in context[RequestCart].values():
        obj.person_id = context[DPerson].get(obj.person_id)
        obj.job_period_id = context[DJobPeriod].get(obj.job_period_id)
        obj.manager_id = context[DPerson].get(obj.manager_id)
        pass
    for obj in context[RequestCartPermission].values():
        obj.request_cart_id = context[RequestCart].get(obj.request_cart_id)
        obj.person_id = context[DPerson].get(obj.person_id)
        obj.service_role_id = context[GServiceRole].get(obj.service_role_id)
        obj.service_id = context[GService].get(obj.service_id)
        pass

def populate_backrefs(context):
    pass

def fetch_ties_tables(context):
      D = context
      print(DJobPeriodIOrgUnit)
      D['D_job_period_I_org_unit'] = [tuple(x) for x in db.session.query(
        DJobPeriodIOrgUnit.c.d_job_period_id,
        DJobPeriodIOrgUnit.c.i_org_unit_id,
      )]
      print(DPersonIOrgUnit)
      D['D_person_I_org_unit'] = [tuple(x) for x in db.session.query(
        DPersonIOrgUnit.c.d_person_id,
        DPersonIOrgUnit.c.i_org_unit_id,
      )]
      print(EExtOrgGService)
      D['E_ext_org_G_service'] = [tuple(x) for x in db.session.query(
        EExtOrgGService.c.e_ext_org_id,
        EExtOrgGService.c.g_service_id,
      )]
      print(EExtOrgGServiceRole)
      D['E_ext_org_G_service_role'] = [tuple(x) for x in db.session.query(
        EExtOrgGServiceRole.c.e_ext_org_id,
        EExtOrgGServiceRole.c.g_service_role_id,
      )]
      print(EJobPeriodIOrgUnit)
      D['E_job_period_I_org_unit'] = [tuple(x) for x in db.session.query(
        EJobPeriodIOrgUnit.c.e_job_period_id,
        EJobPeriodIOrgUnit.c.i_org_unit_id,
      )]
      print(ERequestCartPermissionDPerson)
      D['E_request_cart_permission_D_person'] = [tuple(x) for x in db.session.query(
        ERequestCartPermissionDPerson.c.e_request_cart_permission_id,
        ERequestCartPermissionDPerson.c.d_person_id,
      )]
      print(GPermissionAssociatedIOrgUnit)
      D['G_permission_Associated_I_org_unit'] = [tuple(x) for x in db.session.query(
        GPermissionAssociatedIOrgUnit.c.g_permission_id,
        GPermissionAssociatedIOrgUnit.c.i_org_unit_id,
      )]
      print(GPermissionAssociatedEExtOrg)
      D['G_permission_Associated_E_ext_org'] = [tuple(x) for x in db.session.query(
        GPermissionAssociatedEExtOrg.c.g_permission_id,
        GPermissionAssociatedEExtOrg.c.e_ext_org_id,
      )]
      print(GServiceRoleGAce)
      D['G_service_role_G_ace'] = [tuple(x) for x in db.session.query(
        GServiceRoleGAce.c.g_service_role_id,
        GServiceRoleGAce.c.g_ace_id,
      )]
      print(IOrgUnitGServiceRole)
      D['I_org_unit_G_service_role'] = [tuple(x) for x in db.session.query(
        IOrgUnitGServiceRole.c.i_org_unit_id,
        IOrgUnitGServiceRole.c.g_service_role_id,
      )]
      print(EExtOrgGServiceRole)
      D['E_ext_org_G_service_role'] = [tuple(x) for x in db.session.query(
        EExtOrgGServiceRole.c.e_ext_org_id,
        EExtOrgGServiceRole.c.g_service_role_id,
      )]
      print(ILegalCompanyGService)
      D['I_legal_company_G_service'] = [tuple(x) for x in db.session.query(
        ILegalCompanyGService.c.i_legal_company_id,
        ILegalCompanyGService.c.g_service_id,
      )]
      print(ILegalCompanyGServiceRole)
      D['I_legal_company_G_service_role'] = [tuple(x) for x in db.session.query(
        ILegalCompanyGServiceRole.c.i_legal_company_id,
        ILegalCompanyGServiceRole.c.g_service_role_id,
      )]
      print(IOrgUnitGService)
      D['I_org_unit_G_service'] = [tuple(x) for x in db.session.query(
        IOrgUnitGService.c.i_org_unit_id,
        IOrgUnitGService.c.g_service_id,
      )]
      print(IOrgUnitGServiceRole)
      D['I_org_unit_G_service_role'] = [tuple(x) for x in db.session.query(
        IOrgUnitGServiceRole.c.i_org_unit_id,
        IOrgUnitGServiceRole.c.g_service_role_id,
      )]
      print(RequestCartPermissionDPerson)
      D['Request_cart_permission_D_person'] = [tuple(x) for x in db.session.query(
        RequestCartPermissionDPerson.c.request_cart_permission_id,
        RequestCartPermissionDPerson.c.d_person_id,
      )]

def populate_ties(context):
      ### D_job_period / other_organization_units -> D_job_period_I_org_unit (I_org_unit)
      all_by_id = context[DJobPeriod]
      other_by_id = context[IOrgUnit]

      for x in all_by_id.values():
          x.other_organization_units = []

      rows = context['D_job_period_I_org_unit']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].other_organization_units
              S.append(other_id)
      ### D_person / organization_units -> D_person_I_org_unit (I_org_unit)
      all_by_id = context[DPerson]
      other_by_id = context[IOrgUnit]

      for x in all_by_id.values():
          x.organization_units = []

      rows = context['D_person_I_org_unit']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].organization_units
              S.append(other_id)
      ### E_ext_org / services -> E_ext_org_G_service (G_service)
      all_by_id = context[EExtOrg]
      other_by_id = context[GService]

      for x in all_by_id.values():
          x.services = []

      rows = context['E_ext_org_G_service']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].services
              S.append(other_id)
      ### E_ext_org / service_roles -> E_ext_org_G_service_role (G_service_role)
      all_by_id = context[EExtOrg]
      other_by_id = context[GServiceRole]

      for x in all_by_id.values():
          x.service_roles = []

      rows = context['E_ext_org_G_service_role']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].service_roles
              S.append(other_id)
      ### E_job_period / organization_units -> E_job_period_I_org_unit (I_org_unit)
      all_by_id = context[EJobPeriod]
      other_by_id = context[IOrgUnit]

      for x in all_by_id.values():
          x.organization_units = []

      rows = context['E_job_period_I_org_unit']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].organization_units
              S.append(other_id)
      ### E_request_cart_permission / informed_persons -> E_request_cart_permission_D_person (D_person)
      all_by_id = context[ERequestCartPermission]
      other_by_id = context[DPerson]

      for x in all_by_id.values():
          x.informed_persons = []

      rows = context['E_request_cart_permission_D_person']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].informed_persons
              S.append(other_id)
      ### G_permission / associated_organization_units -> G_permission_Associated_I_org_unit (I_org_unit)
      all_by_id = context[GPermission]
      other_by_id = context[IOrgUnit]

      for x in all_by_id.values():
          x.associated_organization_units = []

      rows = context['G_permission_Associated_I_org_unit']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].associated_organization_units
              S.append(other_id)
      ### G_permission / associated_external_organizations -> G_permission_Associated_E_ext_org (E_ext_org)
      all_by_id = context[GPermission]
      other_by_id = context[EExtOrg]

      for x in all_by_id.values():
          x.associated_external_organizations = []

      rows = context['G_permission_Associated_E_ext_org']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].associated_external_organizations
              S.append(other_id)
      ### G_service_role / aces -> G_service_role_G_ace (G_ace)
      all_by_id = context[GServiceRole]
      other_by_id = context[GAce]

      for x in all_by_id.values():
          x.aces = []

      rows = context['G_service_role_G_ace']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].aces
              S.append(other_id)
      ### G_service_role / organization_units -> I_org_unit_G_service_role (I_org_unit)
      all_by_id = context[GServiceRole]
      other_by_id = context[IOrgUnit]

      for x in all_by_id.values():
          x.organization_units = []

      rows = context['I_org_unit_G_service_role']

      for other_id, id_ in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].organization_units
              S.append(other_id)
      ### G_service_role / external_organizations -> E_ext_org_G_service_role (E_ext_org)
      all_by_id = context[GServiceRole]
      other_by_id = context[EExtOrg]

      for x in all_by_id.values():
          x.external_organizations = []

      rows = context['E_ext_org_G_service_role']

      for other_id, id_ in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].external_organizations
              S.append(other_id)
      ### I_legal_company / services -> I_legal_company_G_service (G_service)
      all_by_id = context[ILegalCompany]
      other_by_id = context[GService]

      for x in all_by_id.values():
          x.services = []

      rows = context['I_legal_company_G_service']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].services
              S.append(other_id)
      ### I_legal_company / service_roles -> I_legal_company_G_service_role (G_service_role)
      all_by_id = context[ILegalCompany]
      other_by_id = context[GServiceRole]

      for x in all_by_id.values():
          x.service_roles = []

      rows = context['I_legal_company_G_service_role']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].service_roles
              S.append(other_id)
      ### I_org_unit / requestable_services -> I_org_unit_G_service (G_service)
      all_by_id = context[IOrgUnit]
      other_by_id = context[GService]

      for x in all_by_id.values():
          x.requestable_services = []

      rows = context['I_org_unit_G_service']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].requestable_services
              S.append(other_id)
      ### I_org_unit / predefined_service_roles -> I_org_unit_G_service_role (G_service_role)
      all_by_id = context[IOrgUnit]
      other_by_id = context[GServiceRole]

      for x in all_by_id.values():
          x.predefined_service_roles = []

      rows = context['I_org_unit_G_service_role']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].predefined_service_roles
              S.append(other_id)
      ### Request_cart_permission / informed_persons -> Request_cart_permission_D_person (D_person)
      all_by_id = context[RequestCartPermission]
      other_by_id = context[DPerson]

      for x in all_by_id.values():
          x.informed_persons = []

      rows = context['Request_cart_permission_D_person']

      for id_, other_id in rows:
          if id_ in all_by_id and other_id in other_by_id:
              S = all_by_id[id_].informed_persons
              S.append(other_id)
CCardTuple = namedtuple('CCardTuple',  ('id', 'card_new', 'card_type_id', 'card_type', 'upn_code', 'identity_id', 'person_id', 'external_person_id', 'expiration_date', 'identity_checked', 'identity_checked_by', 'description', 'description2', 'status', 'replacement_card', 'replaced_card_id', 'given_date', 'given_by_id', 'return_date', 'activation_date', 'deactivation_date', 'deactivation_reason_code', 'deactivation_reason', 'card_organization_id', 'card_organization_name', 'user_cn', 'issuer_id', 'issuer_cn', 'last_name', 'first_name', 'valvira_id', 'subject_serial_no', 'sv_number', 'occupation_name', 'email', 'cert_serial1', 'cert_serial2', 'valid_until', 'token_number', 'reg_ra_workstation_id', 'reg_person_id', 'ra_open_cn', 'ap_upn_old', 'ap_pre_win', 'internal_org_id', 'last_name_ad', 'first_name_ad', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CCard(API,CCardMixin, Base, db.Model):
    __tablename__ = 'O_C_CARD'
    __entity_name__ = 'C_card'
    __plain_object__ = CCardPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    card_new = IColumn(CharBool, nullable=False, name='card_new')

    card_type_id = IColumn(BigInt, db.ForeignKey('O_C_CARD_TYPE.id', use_alter=True, name='fk_C_card_card_type_id'), name='card_type_id')
    _card_type = IRelationship(lambda: CCardType, foreign_keys=[card_type_id])

    card_type = IColumn(CardType, name='card_type')

    upn_code = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='upn_code')

    identity_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY.id', use_alter=True, name='fk_C_card_identity_id'), name='identity_id')
    identity = IRelationship(lambda: GIdentity, foreign_keys=[identity_id])

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_card_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_C_card_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    expiration_date = IColumn(db.Date, name='expiration_date')

    identity_checked = IColumn(CharBool, nullable=False, name='identity_checked')

    identity_checked_by = IColumn(IdentityCheckedBy, name='identity_checked_by')

    description = IColumn(db.TEXT, name='description')

    description2 = IColumn(db.TEXT, name='description2')

    status = IColumn(Status, name='status')
    __additional_info = Header(u'additional_info')

    replacement_card = IColumn(CharBool, nullable=False, name='replacement_card')

    replaced_card_id = IColumn(BigInt, db.ForeignKey('O_C_CARD.id', use_alter=True, name='fk_C_card_replaced_card_id'), name='replaced_card_id')
    replaced_card = IRelationship(lambda: CCard, foreign_keys=[replaced_card_id], remote_side=[id])

    given_date = IColumn(db.Date, name='given_date')

    given_by_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_card_given_by_id'), name='given_by_id')
    given_by = IRelationship(lambda: DPerson, foreign_keys=[given_by_id])

    return_date = IColumn(db.Date, name='return_date')

    activation_date = IColumn(db.Date, name='activation_date')

    deactivation_date = IColumn(db.Date, name='deactivation_date')

    deactivation_reason_code = IColumn(CardDeactivationReasonCode, name='deactivation_reason_code')

    deactivation_reason = IColumn(db.VARCHAR(256), name='deactivation_reason')

    card_organization_id = IColumn(BigInt, db.ForeignKey('O_C_CARD_ORGANIZATION.id', use_alter=True, name='fk_C_card_card_organization_id'), name='card_organization_id')
    card_organization = IRelationship(lambda: CCardOrganization, foreign_keys=[card_organization_id])

    card_organization_name = IColumn(db.VARCHAR(128), name='card_organization_name')

    user_cn = IColumn(db.VARCHAR(64), name='user_cn')

    issuer_id = IColumn(BigInt, db.ForeignKey('O_C_CARD_ISSUER.id', use_alter=True, name='fk_C_card_issuer_id'), name='issuer_id')
    issuer = IRelationship(lambda: CCardIssuer, foreign_keys=[issuer_id])

    issuer_cn = IColumn(db.VARCHAR(256), name='issuer_cn')

    last_name = IColumn(db.VARCHAR(32), name='last_name')

    first_name = IColumn(db.VARCHAR(32), name='first_name')

    valvira_id = IColumn(db.VARCHAR(11), name='valvira_id')

    subject_serial_no = IColumn(db.VARCHAR(32), name='subject_serial_no')

    sv_number = IColumn(db.VARCHAR(10), name='sv_number')

    occupation_name = IColumn(db.VARCHAR(64), name='occupation_name')

    email = IColumn(db.VARCHAR(64), name='email')

    cert_serial1 = IColumn(db.VARCHAR(64), name='cert_serial1')

    cert_serial2 = IColumn(db.VARCHAR(64), name='cert_serial2')

    valid_until = IColumn(db.Date, name='valid_until')

    token_number = IColumn(db.VARCHAR(64), name='token_number')
    __registering_person = Header(u'registering_person')

    reg_ra_workstation_id = IColumn(BigInt, db.ForeignKey('O_C_WORKSTATION.id', use_alter=True, name='fk_C_card_reg_ra_workstation_id'), name='reg_ra_workstation_id')
    reg_ra_workstation = IRelationship(lambda: CWorkstation, foreign_keys=[reg_ra_workstation_id])

    reg_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_card_reg_person_id'), name='reg_person_id')
    reg_person = IRelationship(lambda: DPerson, foreign_keys=[reg_person_id])

    ra_open_cn = IColumn(db.VARCHAR(64), name='ra_open_cn')
    __extra_attributes = Header(u'extra_attributes')

    ap_upn_old = IColumn(db.VARCHAR(32), name='ap_upn_old')

    ap_pre_win = IColumn(db.VARCHAR(20), name='ap_pre_win')

    internal_org_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_C_card_internal_org_id'), name='internal_org_id')
    internal_org = IRelationship(lambda: IOrgUnit, foreign_keys=[internal_org_id])

    last_name_ad = IColumn(db.VARCHAR(32), name='last_name_ad')

    first_name_ad = IColumn(db.VARCHAR(32), name='first_name_ad')

    def to_named_tuple(self):
        return CCardTuple(id=self.id,card_new=self.card_new,card_type_id=self.card_type_id,card_type=self.card_type,upn_code=self.upn_code,identity_id=self.identity_id,person_id=self.person_id,external_person_id=self.external_person_id,expiration_date=self.expiration_date,identity_checked=self.identity_checked,identity_checked_by=self.identity_checked_by,description=self.description,description2=self.description2,status=self.status,replacement_card=self.replacement_card,replaced_card_id=self.replaced_card_id,given_date=self.given_date,given_by_id=self.given_by_id,return_date=self.return_date,activation_date=self.activation_date,deactivation_date=self.deactivation_date,deactivation_reason_code=self.deactivation_reason_code,deactivation_reason=self.deactivation_reason,card_organization_id=self.card_organization_id,card_organization_name=self.card_organization_name,user_cn=self.user_cn,issuer_id=self.issuer_id,issuer_cn=self.issuer_cn,last_name=self.last_name,first_name=self.first_name,valvira_id=self.valvira_id,subject_serial_no=self.subject_serial_no,sv_number=self.sv_number,occupation_name=self.occupation_name,email=self.email,cert_serial1=self.cert_serial1,cert_serial2=self.cert_serial2,valid_until=self.valid_until,token_number=self.token_number,reg_ra_workstation_id=self.reg_ra_workstation_id,reg_person_id=self.reg_person_id,ra_open_cn=self.ra_open_cn,ap_upn_old=self.ap_upn_old,ap_pre_win=self.ap_pre_win,internal_org_id=self.internal_org_id,last_name_ad=self.last_name_ad,first_name_ad=self.first_name_ad,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CCardTuple(id=self.id,card_new=self.card_new,card_type_id=self.card_type_id,card_type=self.card_type,upn_code=self.upn_code,identity_id=self.identity_id,person_id=self.person_id,external_person_id=self.external_person_id,expiration_date=self.expiration_date,identity_checked=self.identity_checked,identity_checked_by=self.identity_checked_by,description=self.description,description2=self.description2,status=self.status,replacement_card=self.replacement_card,replaced_card_id=self.replaced_card_id,given_date=self.given_date,given_by_id=self.given_by_id,return_date=self.return_date,activation_date=self.activation_date,deactivation_date=self.deactivation_date,deactivation_reason_code=self.deactivation_reason_code,deactivation_reason=self.deactivation_reason,card_organization_id=self.card_organization_id,card_organization_name=self.card_organization_name,user_cn=self.user_cn,issuer_id=self.issuer_id,issuer_cn=self.issuer_cn,last_name=self.last_name,first_name=self.first_name,valvira_id=self.valvira_id,subject_serial_no=self.subject_serial_no,sv_number=self.sv_number,occupation_name=self.occupation_name,email=self.email,cert_serial1=self.cert_serial1,cert_serial2=self.cert_serial2,valid_until=self.valid_until,token_number=self.token_number,reg_ra_workstation_id=self.reg_ra_workstation_id,reg_person_id=self.reg_person_id,ra_open_cn=self.ra_open_cn,ap_upn_old=self.ap_upn_old,ap_pre_win=self.ap_pre_win,internal_org_id=self.internal_org_id,last_name_ad=self.last_name_ad,first_name_ad=self.first_name_ad,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CCardIssuerTuple = namedtuple('CCardIssuerTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CCardIssuer(API,CCardIssuerMixin, Base, db.Model):
    __tablename__ = 'O_C_CARD_ISSUER'
    __entity_name__ = 'C_card_issuer'
    __plain_object__ = CCardIssuerPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CCardIssuerTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CCardIssuerTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CCardOrganizationTuple = namedtuple('CCardOrganizationTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CCardOrganization(API,CCardOrganizationMixin, Base, db.Model):
    __tablename__ = 'O_C_CARD_ORGANIZATION'
    __entity_name__ = 'C_card_organization'
    __plain_object__ = CCardOrganizationPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CCardOrganizationTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CCardOrganizationTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CCardTypeTuple = namedtuple('CCardTypeTuple',  ('id', 'name', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CCardType(API,CCardTypeMixin, Base, db.Model):
    __tablename__ = 'O_C_CARD_TYPE'
    __entity_name__ = 'C_card_type'
    __plain_object__ = CCardTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_C_card_type_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CCardTypeTuple(id=self.id,name=self.name,service_id=self.service_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CCardTypeTuple(id=self.id,name=self.name,service_id=self.service_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CDeviceTuple = namedtuple('CDeviceTuple',  ('id', 'name', 'device_start_date', 'device_end_date', 'device_type', 'device_subtype', 'serial_no', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CDevice(API,CDeviceMixin, Base, db.Model):
    __tablename__ = 'O_C_DEVICE'
    __entity_name__ = 'C_device'
    __plain_object__ = CDevicePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    device_start_date = IColumn(db.Date, name='device_start_date')

    device_end_date = IColumn(db.Date, name='device_end_date')

    device_type = IColumn(BigInt, db.ForeignKey('O_C_DEVICE_TYPE.id', use_alter=True, name='fk_C_device_device_type'), name='device_type')

    device_subtype = IColumn(BigInt, db.ForeignKey('O_C_DEVICE_SUBTYPE.id', use_alter=True, name='fk_C_device_device_subtype'), name='device_subtype')

    serial_no = IColumn(db.VARCHAR(128), name='serial_no')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CDeviceTuple(id=self.id,name=self.name,device_start_date=self.device_start_date,device_end_date=self.device_end_date,device_type=self.device_type,device_subtype=self.device_subtype,serial_no=self.serial_no,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CDeviceTuple(id=self.id,name=self.name,device_start_date=self.device_start_date,device_end_date=self.device_end_date,device_type=self.device_type,device_subtype=self.device_subtype,serial_no=self.serial_no,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CDevicePersonTuple = namedtuple('CDevicePersonTuple',  ('id', 'device_id', 'identity_id', 'person_id', 'external_person_id', 'given_date', 'given_by_id', 'return_date', 'return_reason_code', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CDevicePerson(API,CDevicePersonMixin, Base, db.Model):
    __tablename__ = 'O_C_DEVICE_PERSON'
    __entity_name__ = 'C_device_person'
    __plain_object__ = CDevicePersonPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    device_id = IColumn(BigInt, db.ForeignKey('O_C_DEVICE.id', use_alter=True, name='fk_C_device_person_device_id'), nullable=False, name='device_id')
    device = IRelationship(lambda: CDevice, foreign_keys=[device_id])

    identity_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY.id', use_alter=True, name='fk_C_device_person_identity_id'), name='identity_id')
    identity = IRelationship(lambda: GIdentity, foreign_keys=[identity_id])

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_device_person_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_C_device_person_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    given_date = IColumn(db.Date, name='given_date')

    given_by_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_device_person_given_by_id'), name='given_by_id')
    given_by = IRelationship(lambda: DPerson, foreign_keys=[given_by_id])

    return_date = IColumn(db.Date, name='return_date')

    return_reason_code = IColumn(ReturnReasonCode, name='return_reason_code')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CDevicePersonTuple(id=self.id,device_id=self.device_id,identity_id=self.identity_id,person_id=self.person_id,external_person_id=self.external_person_id,given_date=self.given_date,given_by_id=self.given_by_id,return_date=self.return_date,return_reason_code=self.return_reason_code,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CDevicePersonTuple(id=self.id,device_id=self.device_id,identity_id=self.identity_id,person_id=self.person_id,external_person_id=self.external_person_id,given_date=self.given_date,given_by_id=self.given_by_id,return_date=self.return_date,return_reason_code=self.return_reason_code,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CDeviceSubtypeTuple = namedtuple('CDeviceSubtypeTuple',  ('id', 'device_type', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CDeviceSubtype(API,CDeviceSubtypeMixin, Base, db.Model):
    __tablename__ = 'O_C_DEVICE_SUBTYPE'
    __entity_name__ = 'C_device_subtype'
    __plain_object__ = CDeviceSubtypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    device_type = IColumn(BigInt, db.ForeignKey('O_C_DEVICE_TYPE.id', use_alter=True, name='fk_C_device_subtype_device_type'), name='device_type')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CDeviceSubtypeTuple(id=self.id,device_type=self.device_type,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CDeviceSubtypeTuple(id=self.id,device_type=self.device_type,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CDeviceTypeTuple = namedtuple('CDeviceTypeTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CDeviceType(API,CDeviceTypeMixin, Base, db.Model):
    __tablename__ = 'O_C_DEVICE_TYPE'
    __entity_name__ = 'C_device_type'
    __plain_object__ = CDeviceTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CDeviceTypeTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CDeviceTypeTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CIloqKeyTuple = namedtuple('CIloqKeyTuple',  ('source_person_id', 'person_id', 'external_person_id', 'key_stamp', 'key_logical_state', 'key_state', 'key_description', 'real_estate_name', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CIloqKey(CIloqKeyMixin, Base, db.Model):
    __tablename__ = 'C_ILOQ_KEY'
    __entity_name__ = 'C_iloq_key'
    __parent_entity__ = None

    source_person_id = IColumn(db.VARCHAR(64), primary_key=True, name='source_person_id')

    source_person_id = IColumn(db.VARCHAR(64), primary_key=True, name='source_person_id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_iloq_key_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_C_iloq_key_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    key_stamp = IColumn(db.VARCHAR(64), name='key_stamp')

    key_logical_state = IColumn(db.Integer, name='key_logical_state')

    key_state = IColumn(db.Integer, name='key_state')

    key_description = IColumn(db.TEXT, name='key_description')

    real_estate_name = IColumn(db.TEXT, name='real_estate_name')

    def to_named_tuple(self):
        return CIloqKeyTuple(source_person_id=self.source_person_id,person_id=self.person_id,external_person_id=self.external_person_id,key_stamp=self.key_stamp,key_logical_state=self.key_logical_state,key_state=self.key_state,key_description=self.key_description,real_estate_name=self.real_estate_name,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CIloqKeyTuple(source_person_id=self.source_person_id,person_id=self.person_id,external_person_id=self.external_person_id,key_stamp=self.key_stamp,key_logical_state=self.key_logical_state,key_state=self.key_state,key_description=self.key_description,real_estate_name=self.real_estate_name,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CKeyTuple = namedtuple('CKeyTuple',  ('id', 'key_new', 'key_type_id', 'key_type', 'key_profile', 'serial_no', 'identity_id', 'person_id', 'external_person_id', 'expiration_date', 'identity_checked', 'identity_checked_by', 'description', 'description2', 'status', 'replacement_key', 'replaced_key_id', 'given_date', 'given_by_id', 'return_date', 'activation_date', 'deactivation_date', 'deactivation_reason_code', 'deactivation_reason', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CKey(API,CKeyMixin, Base, db.Model):
    __tablename__ = 'O_C_KEY'
    __entity_name__ = 'C_key'
    __plain_object__ = CKeyPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    key_new = IColumn(CharBool, nullable=False, name='key_new')

    key_type_id = IColumn(BigInt, db.ForeignKey('O_C_KEY_TYPE.id', use_alter=True, name='fk_C_key_key_type_id'), name='key_type_id')
    _key_type = IRelationship(lambda: CKeyType, foreign_keys=[key_type_id])

    key_type = IColumn(KeyType, name='key_type')

    key_profile = IColumn(BigInt, db.ForeignKey('O_C_KEY_PROFILE.id', use_alter=True, name='fk_C_key_key_profile'), name='key_profile')

    serial_no = IColumn(db.VARCHAR(64), name='serial_no')

    identity_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY.id', use_alter=True, name='fk_C_key_identity_id'), name='identity_id')
    identity = IRelationship(lambda: GIdentity, foreign_keys=[identity_id])

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_key_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_C_key_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    expiration_date = IColumn(db.Date, name='expiration_date')

    identity_checked = IColumn(CharBool, nullable=False, name='identity_checked')

    identity_checked_by = IColumn(IdentityCheckedBy, name='identity_checked_by')

    description = IColumn(db.TEXT, name='description')

    description2 = IColumn(db.TEXT, name='description2')

    status = IColumn(Status, name='status')
    __additional_info = Header(u'additional_info')

    replacement_key = IColumn(CharBool, nullable=False, name='replacement_key')

    replaced_key_id = IColumn(BigInt, db.ForeignKey('O_C_KEY.id', use_alter=True, name='fk_C_key_replaced_key_id'), name='replaced_key_id')
    replaced_key = IRelationship(lambda: CKey, foreign_keys=[replaced_key_id], remote_side=[id])

    given_date = IColumn(db.Date, name='given_date')

    given_by_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_C_key_given_by_id'), name='given_by_id')
    given_by = IRelationship(lambda: DPerson, foreign_keys=[given_by_id])

    return_date = IColumn(db.Date, name='return_date')

    activation_date = IColumn(db.Date, name='activation_date')

    deactivation_date = IColumn(db.Date, name='deactivation_date')

    deactivation_reason_code = IColumn(KeyDeactivationReasonCode, name='deactivation_reason_code')

    deactivation_reason = IColumn(db.VARCHAR(256), name='deactivation_reason')

    def to_named_tuple(self):
        return CKeyTuple(id=self.id,key_new=self.key_new,key_type_id=self.key_type_id,key_type=self.key_type,key_profile=self.key_profile,serial_no=self.serial_no,identity_id=self.identity_id,person_id=self.person_id,external_person_id=self.external_person_id,expiration_date=self.expiration_date,identity_checked=self.identity_checked,identity_checked_by=self.identity_checked_by,description=self.description,description2=self.description2,status=self.status,replacement_key=self.replacement_key,replaced_key_id=self.replaced_key_id,given_date=self.given_date,given_by_id=self.given_by_id,return_date=self.return_date,activation_date=self.activation_date,deactivation_date=self.deactivation_date,deactivation_reason_code=self.deactivation_reason_code,deactivation_reason=self.deactivation_reason,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CKeyTuple(id=self.id,key_new=self.key_new,key_type_id=self.key_type_id,key_type=self.key_type,key_profile=self.key_profile,serial_no=self.serial_no,identity_id=self.identity_id,person_id=self.person_id,external_person_id=self.external_person_id,expiration_date=self.expiration_date,identity_checked=self.identity_checked,identity_checked_by=self.identity_checked_by,description=self.description,description2=self.description2,status=self.status,replacement_key=self.replacement_key,replaced_key_id=self.replaced_key_id,given_date=self.given_date,given_by_id=self.given_by_id,return_date=self.return_date,activation_date=self.activation_date,deactivation_date=self.deactivation_date,deactivation_reason_code=self.deactivation_reason_code,deactivation_reason=self.deactivation_reason,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CKeyProfileTuple = namedtuple('CKeyProfileTuple',  ('id', 'key_type_id', 'key_type', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CKeyProfile(API,CKeyProfileMixin, Base, db.Model):
    __tablename__ = 'O_C_KEY_PROFILE'
    __entity_name__ = 'C_key_profile'
    __plain_object__ = CKeyProfilePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    key_type_id = IColumn(BigInt, db.ForeignKey('O_C_KEY_TYPE.id', use_alter=True, name='fk_C_key_profile_key_type_id'), name='key_type_id')
    _key_type = IRelationship(lambda: CKeyType, foreign_keys=[key_type_id])

    key_type = IColumn(KeyType, name='key_type')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CKeyProfileTuple(id=self.id,key_type_id=self.key_type_id,key_type=self.key_type,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CKeyProfileTuple(id=self.id,key_type_id=self.key_type_id,key_type=self.key_type,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CKeyTypeTuple = namedtuple('CKeyTypeTuple',  ('id', 'name', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CKeyType(API,CKeyTypeMixin, Base, db.Model):
    __tablename__ = 'O_C_KEY_TYPE'
    __entity_name__ = 'C_key_type'
    __plain_object__ = CKeyTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_C_key_type_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CKeyTypeTuple(id=self.id,name=self.name,service_id=self.service_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CKeyTypeTuple(id=self.id,name=self.name,service_id=self.service_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

CWorkstationTuple = namedtuple('CWorkstationTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class CWorkstation(API,CWorkstationMixin, Base, db.Model):
    __tablename__ = 'O_C_WORKSTATION'
    __entity_name__ = 'C_workstation'
    __plain_object__ = CWorkstationPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return CWorkstationTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return CWorkstationTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DAbsenceTuple = namedtuple('DAbsenceTuple',  ('id', 'person_id', 'external_person_id', 'absence_type', 'start_date', 'end_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DAbsence(API,DAbsenceMixin, Base, db.Model):
    __tablename__ = 'D_ABSENCE'
    __entity_name__ = 'D_absence'
    __plain_object__ = DAbsencePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_absence_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_D_absence_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    absence_type = IColumn(AbsenceType, nullable=False, name='absence_type')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DAbsenceTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,absence_type=self.absence_type,start_date=self.start_date,end_date=self.end_date,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DAbsenceTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,absence_type=self.absence_type,start_date=self.start_date,end_date=self.end_date,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DAuthMethodTuple = namedtuple('DAuthMethodTuple',  ('id', 'name', 'description', 'authentication_level', 'starting_date', 'termination_date', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DAuthMethod(API,DAuthMethodMixin, Base, db.Model):
    __tablename__ = 'D_AUTH_METHOD'
    __entity_name__ = 'D_auth_method'
    __plain_object__ = DAuthMethodPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    authentication_level = IColumn(AuthLevel, nullable=False, name='authentication_level')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return DAuthMethodTuple(id=self.id,name=self.name,description=self.description,authentication_level=self.authentication_level,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DAuthMethodTuple(id=self.id,name=self.name,description=self.description,authentication_level=self.authentication_level,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DCompetenceTuple = namedtuple('DCompetenceTuple',  ('id', 'code', 'name', 'description', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DCompetence(API,DCompetenceMixin, Base, db.Model):
    __tablename__ = 'D_COMPETENCE'
    __entity_name__ = 'D_competence'
    __plain_object__ = DCompetencePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(24), name='code')

    name = IColumn(db.VARCHAR(200), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')
    __classification = Header(u'classification')

    classification1 = IColumn(db.VARCHAR(64), name='classification1')

    classification2 = IColumn(db.VARCHAR(64), name='classification2')

    classification3 = IColumn(db.VARCHAR(64), name='classification3')

    def to_named_tuple(self):
        return DCompetenceTuple(id=self.id,code=self.code,name=self.name,description=self.description,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DCompetenceTuple(id=self.id,code=self.code,name=self.name,description=self.description,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DEducationTuple = namedtuple('DEducationTuple',  ('id', 'code', 'name', 'description', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DEducation(API,DEducationMixin, Base, db.Model):
    __tablename__ = 'D_EDUCATION'
    __entity_name__ = 'D_education'
    __plain_object__ = DEducationPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(24), nullable=False, name='code')

    name = IColumn(db.VARCHAR(200), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')
    __classification = Header(u'classification')

    classification1 = IColumn(db.VARCHAR(64), name='classification1')

    classification2 = IColumn(db.VARCHAR(64), name='classification2')

    classification3 = IColumn(db.VARCHAR(64), name='classification3')

    def to_named_tuple(self):
        return DEducationTuple(id=self.id,code=self.code,name=self.name,description=self.description,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DEducationTuple(id=self.id,code=self.code,name=self.name,description=self.description,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DJobPeriodTuple = namedtuple('DJobPeriodTuple',  ('id', 'person_id', 'starting_date', 'termination_date', 'job_period_type', 'is_manager', 'orgunit_id', 'job_title', 'other_job_title', 'specific_job_title', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'organization_association_type', 'status', 'manager_id', 'manager_email', 'manager_name', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'report_manager_id', 'org_unit_manager_id', 'information_checked', 'contract', 'medicine_right', 'absence_active', 'substitute_periods_active', 'hr_job_type', 'c_pasu', 'full_part_per', 'hr_work_time_type', 'operative_staff', 'int_period_id', 'int_job_title', 'int_job_code', 'int_job_code2', 'hr_profession_code', 'hr_period_character_code', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'pupo', 'phone', 'card_valid_from', 'card_valid_to', 'exc_username', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_location_id', 'exc_country_id', 'exc_primary_period', 'inferred_primary_job_period', 'externally_managed', 'exported_to_idm', 'created_by_id', 'is_primary_jobtitle', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DJobPeriod(API,DJobPeriodMixin, Base, db.Model):
    __tablename__ = 'D_JOB_PERIOD'
    __entity_name__ = 'D_job_period'
    __plain_object__ = DJobPeriodPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    __employment = Header(u'employment')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_job_period_person_id'), nullable=False, name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    starting_date = IColumn(db.Date, nullable=False, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    job_period_type = IColumn(JPType, name='jp_type')

    is_manager = IColumn(CharBool, nullable=False, name='is_manager')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_orgunit_id'), nullable=False, name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    job_title = IColumn(db.VARCHAR(64), name='job_title')

    other_job_title = IColumn(db.VARCHAR(64), name='other_job_title')

    specific_job_title = IColumn(db.VARCHAR(64), name='specific_job_title')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_D_job_period_jobtitle_id'), nullable=False, name='jobtitle_id')
    jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    jobfamily_id = IColumn(BigInt, db.ForeignKey('I_JOB_FAMILY.id', use_alter=True, name='fk_D_job_period_jobfamily_id'), name='jobfamily_id')
    jobfamily = IRelationship(lambda: IJobFamily, foreign_keys=[jobfamily_id])

    jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jobrole_id'), name='jobrole_id')
    jobrole = IRelationship(lambda: IJobRole, foreign_keys=[jobrole_id])

    job_type = IColumn(JobType, name='job_type')

    organization_association_type = IColumn(OrgAssociationType, name='org_association_type')

    status = IColumn(Status, name='status')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_job_period_manager_id'), name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    manager_email = IColumn(db.VARCHAR(64), name='manager_email')

    manager_name = IColumn(db.VARCHAR(64), name='manager_name')

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_job_period_subst_manager_id'), name='subst_manager_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id])

    subst_manager_name = IColumn(db.VARCHAR(64), name='subst_manager_name')

    subst_manager_email = IColumn(db.VARCHAR(64), name='subst_manager_email')

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')

    report_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_job_period_report_manager_id'), name='report_manager_id')
    report_manager = IRelationship(lambda: DPerson, foreign_keys=[report_manager_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_D_job_period_org_unit_manager_id'), name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    information_checked = IColumn(CharBool, nullable=False, name='information_checked')

    contract = IColumn(db.VARCHAR(64), name='contract')

    medicine_right = IColumn(MedicineRight, name='medicine_right')
    __absent_periods = Header(u'absent_periods')

    absence_active = IColumn(CharBool, nullable=False, name='absence_active')
    absences = IRelationship(lambda: DJobPeriodAbsence, foreign_keys=lambda: [DJobPeriodAbsence.d_job_period_id], uselist=True)
    __substitute_periods = Header(u'substitute_periods')

    substitute_periods_active = IColumn(CharBool, nullable=False, name='substitute_periods_active')
    substitute_detail = IRelationship(lambda: DJobPeriodSubstitute, foreign_keys=lambda: [DJobPeriodSubstitute.d_job_period_id], uselist=True)
    other_organization_units = IRelationship(lambda: IOrgUnit, secondary=lambda: DJobPeriodIOrgUnit, uselist=True)
    __permissions = Header(u'permissions')

    requested_permissions = IRelationship(lambda: GPermission, foreign_keys=lambda: [GPermission.d_job_period_id], uselist=True)
    __hr_info = Header(u'hr_info')

    hr_job_type = IColumn(HRJobType, name='hr_job_type')

    c_pasu = IColumn(CharBool, nullable=False, name='c_pasu')

    full_part_per = IColumn(db.Float, name='full_part_per')

    hr_work_time_type = IColumn(HRWorkTimeType, name='hr_work_time_type')

    operative_staff = IColumn(CharBool, nullable=False, name='operative_staff')

    int_period_id = IColumn(db.VARCHAR(64), name='int_period_id')

    int_job_title = IColumn(db.VARCHAR(64), name='int_job_title')

    int_job_code = IColumn(db.VARCHAR(64), name='int_job_code')

    int_job_code2 = IColumn(db.VARCHAR(64), name='int_job_code2')

    hr_profession_code = IColumn(HRProfessionCode, name='hr_profession_code')

    hr_period_character_code = IColumn(JpCharacter, name='hr_period_character_code')

    flag1 = IColumn(CharBool, nullable=False, name='flag1')

    flag2 = IColumn(CharBool, nullable=False, name='flag2')

    flag3 = IColumn(CharBool, nullable=False, name='flag3')

    flag4 = IColumn(CharBool, nullable=False, name='flag4')

    flag5 = IColumn(CharBool, nullable=False, name='flag5')

    original_source = IColumn(OriginalSource, name='original_source')

    pupo = IColumn(db.VARCHAR(4), name='pupo')

    phone = IColumn(db.VARCHAR(40), name='phone')

    card_valid_from = IColumn(db.Date, name='card_valid_from')

    card_valid_to = IColumn(db.Date, name='card_valid_to')
    __exceptions = Header(u'exceptions')

    exc_username = IColumn(db.VARCHAR(64), name='exc_username')

    exc_legalcompany_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_D_job_period_exc_legalcompany_id'), name='exc_legalcompany_id')
    exc_legalcompany = IRelationship(lambda: ILegalCompany, foreign_keys=[exc_legalcompany_id])

    exc_costcenter_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_D_job_period_exc_costcenter_id'), name='exc_costcenter_id')
    exc_costcenter = IRelationship(lambda: ICostCenter, foreign_keys=[exc_costcenter_id])

    exc_location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_D_job_period_exc_location_id'), nullable=False, name='exc_location_id')
    exc_location = IRelationship(lambda: ILocation, foreign_keys=[exc_location_id])

    exc_country_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_D_job_period_exc_country_id'), name='exc_country_id')
    exc_country = IRelationship(lambda: GCountry, foreign_keys=[exc_country_id])

    exc_primary_period = IColumn(CharBool, nullable=False, name='exc_primary_period')
    __stuff = Header(u'stuff')

    inferred_primary_job_period = IColumn(CharBool, nullable=False, name='inferred_primary_job_period')

    externally_managed = IColumn(CharBool, nullable=False, name='externally_managed')

    exported_to_idm = IColumn(CharBool, nullable=False, name='exported_to_idm')

    created_by_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_D_job_period_created_by_id'), name='created_by_id')
    created_by = IRelationship(lambda: Zuser, foreign_keys=[created_by_id])

    is_primary_jobtitle = IColumn(CharBool, nullable=False, name='is_primary_jobtitle')

    def to_named_tuple(self):
        return DJobPeriodTuple(id=self.id,person_id=self.person_id,starting_date=self.starting_date,termination_date=self.termination_date,job_period_type=self.job_period_type,is_manager=self.is_manager,orgunit_id=self.orgunit_id,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,jobtitle_id=self.jobtitle_id,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,organization_association_type=self.organization_association_type,status=self.status,manager_id=self.manager_id,manager_email=self.manager_email,manager_name=self.manager_name,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,report_manager_id=self.report_manager_id,org_unit_manager_id=self.org_unit_manager_id,information_checked=self.information_checked,contract=self.contract,medicine_right=self.medicine_right,absence_active=self.absence_active,substitute_periods_active=self.substitute_periods_active,hr_job_type=self.hr_job_type,c_pasu=self.c_pasu,full_part_per=self.full_part_per,hr_work_time_type=self.hr_work_time_type,operative_staff=self.operative_staff,int_period_id=self.int_period_id,int_job_title=self.int_job_title,int_job_code=self.int_job_code,int_job_code2=self.int_job_code2,hr_profession_code=self.hr_profession_code,hr_period_character_code=self.hr_period_character_code,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,pupo=self.pupo,phone=self.phone,card_valid_from=self.card_valid_from,card_valid_to=self.card_valid_to,exc_username=self.exc_username,exc_legalcompany_id=self.exc_legalcompany_id,exc_costcenter_id=self.exc_costcenter_id,exc_location_id=self.exc_location_id,exc_country_id=self.exc_country_id,exc_primary_period=self.exc_primary_period,inferred_primary_job_period=self.inferred_primary_job_period,externally_managed=self.externally_managed,exported_to_idm=self.exported_to_idm,created_by_id=self.created_by_id,is_primary_jobtitle=self.is_primary_jobtitle,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DJobPeriodTuple(id=self.id,person_id=self.person_id,starting_date=self.starting_date,termination_date=self.termination_date,job_period_type=self.job_period_type,is_manager=self.is_manager,orgunit_id=self.orgunit_id,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,jobtitle_id=self.jobtitle_id,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,organization_association_type=self.organization_association_type,status=self.status,manager_id=self.manager_id,manager_email=self.manager_email,manager_name=self.manager_name,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,report_manager_id=self.report_manager_id,org_unit_manager_id=self.org_unit_manager_id,information_checked=self.information_checked,contract=self.contract,medicine_right=self.medicine_right,absence_active=self.absence_active,substitute_periods_active=self.substitute_periods_active,hr_job_type=self.hr_job_type,c_pasu=self.c_pasu,full_part_per=self.full_part_per,hr_work_time_type=self.hr_work_time_type,operative_staff=self.operative_staff,int_period_id=self.int_period_id,int_job_title=self.int_job_title,int_job_code=self.int_job_code,int_job_code2=self.int_job_code2,hr_profession_code=self.hr_profession_code,hr_period_character_code=self.hr_period_character_code,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,pupo=self.pupo,phone=self.phone,card_valid_from=self.card_valid_from,card_valid_to=self.card_valid_to,exc_username=self.exc_username,exc_legalcompany_id=self.exc_legalcompany_id,exc_costcenter_id=self.exc_costcenter_id,exc_location_id=self.exc_location_id,exc_country_id=self.exc_country_id,exc_primary_period=self.exc_primary_period,inferred_primary_job_period=self.inferred_primary_job_period,externally_managed=self.externally_managed,exported_to_idm=self.exported_to_idm,created_by_id=self.created_by_id,is_primary_jobtitle=self.is_primary_jobtitle,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DJobPeriodAbsenceTuple = namedtuple('DJobPeriodAbsenceTuple',  ('d_job_period_id', 'valid_from', 'created_by', 'start_date', 'end_date', 'description'  ))

class DJobPeriodAbsence(API,DJobPeriodAbsenceMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ABSENCE'
    __entity_name__ = 'D_job_period_absence'
    __plain_object__ = DJobPeriodAbsencePlain
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_absence_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_absence_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    created_by = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_D_job_period_absence_created_by'), nullable=False, name='created_by')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    description = IColumn(db.VARCHAR(256), name='description')

    def to_named_tuple(self):
        return DJobPeriodAbsenceTuple(d_job_period_id=self.d_job_period_id,valid_from=self.valid_from,created_by=self.created_by,start_date=self.start_date,end_date=self.end_date,description=self.description,)

    def to_plain_object(self):
        return DJobPeriodAbsenceTuple(d_job_period_id=self.d_job_period_id,valid_from=self.valid_from,created_by=self.created_by,start_date=self.start_date,end_date=self.end_date,description=self.description,)

DJobPeriodAttrPermissionLogTuple = namedtuple('DJobPeriodAttrPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'r_dyn_role_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodAttrPermissionLog(DJobPeriodAttrPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ATTR_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_attr_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_attr_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_attr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    r_dyn_role_id = IColumn(BigInt, db.ForeignKey('O_R_DYN_ROLE.id', use_alter=True, name='fk_D_job_period_attr_permission_log_r_dyn_role_id'), primary_key=True, name='r_dyn_role_id')
    r_dyn_role = IRelationship(lambda: RDynRole, foreign_keys=[r_dyn_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_attr_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_attr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    r_dyn_role_id = IColumn(BigInt, db.ForeignKey('O_R_DYN_ROLE.id', use_alter=True, name='fk_D_job_period_attr_permission_log_r_dyn_role_id'), primary_key=True, name='r_dyn_role_id')
    r_dyn_role = IRelationship(lambda: RDynRole, foreign_keys=[r_dyn_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodAttrPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodAttrPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodAttrPermissionStateTuple = namedtuple('DJobPeriodAttrPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'r_dyn_role_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodAttrPermissionState(DJobPeriodAttrPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ATTR_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_attr_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    r_dyn_role_id = IColumn(BigInt, primary_key=True, name='r_dyn_role_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    r_dyn_role_id = IColumn(BigInt, primary_key=True, name='r_dyn_role_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodAttrPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodAttrPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodGPermissionLogTuple = namedtuple('DJobPeriodGPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'g_permission_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodGPermissionLog(DJobPeriodGPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_G_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_g_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_g_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_g_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_D_job_period_g_permission_log_g_permission_id'), primary_key=True, name='g_permission_id')
    g_permission = IRelationship(lambda: GPermission, foreign_keys=[g_permission_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_g_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_g_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_D_job_period_g_permission_log_g_permission_id'), primary_key=True, name='g_permission_id')
    g_permission = IRelationship(lambda: GPermission, foreign_keys=[g_permission_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodGPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodGPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodGPermissionStateTuple = namedtuple('DJobPeriodGPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'g_permission_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodGPermissionState(DJobPeriodGPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_G_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_g_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_permission_id = IColumn(BigInt, primary_key=True, name='g_permission_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_permission_id = IColumn(BigInt, primary_key=True, name='g_permission_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodGPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodGPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodJrOuPermissionLogTuple = namedtuple('DJobPeriodJrOuPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'i_job_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodJrOuPermissionLog(DJobPeriodJrOuPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_JR_OU_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_jr_ou_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    i_job_role_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_i_job_role_id'), primary_key=True, name='i_job_role_id')
    i_job_role = IRelationship(lambda: IJobRole, foreign_keys=[i_job_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IOrgUnit, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IOrgUnit, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    i_job_role_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_i_job_role_id'), primary_key=True, name='i_job_role_id')
    i_job_role = IRelationship(lambda: IJobRole, foreign_keys=[i_job_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IOrgUnit, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_jr_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IOrgUnit, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodJrOuPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,i_job_role_id=self.i_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodJrOuPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,i_job_role_id=self.i_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodJrOuPermissionStateTuple = namedtuple('DJobPeriodJrOuPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'i_job_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodJrOuPermissionState(DJobPeriodJrOuPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_JR_OU_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_jr_ou_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    i_job_role_id = IColumn(BigInt, primary_key=True, name='i_job_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    i_job_role_id = IColumn(BigInt, primary_key=True, name='i_job_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodJrOuPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,i_job_role_id=self.i_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodJrOuPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,i_job_role_id=self.i_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodJrPermissionLogTuple = namedtuple('DJobPeriodJrPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodJrPermissionLog(DJobPeriodJrPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_JR_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_jr_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_jr_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_jr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jr_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jr_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_jr_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_jr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jr_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jr_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodJrPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodJrPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodJrPermissionStateTuple = namedtuple('DJobPeriodJrPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodJrPermissionState(DJobPeriodJrPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_JR_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_jr_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodJrPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodJrPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodJtPermissionLogTuple = namedtuple('DJobPeriodJtPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'd_jobtitle_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodJtPermissionLog(DJobPeriodJtPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_JT_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_jt_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_jt_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    d_jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_d_jobtitle_id'), primary_key=True, name='d_jobtitle_id')
    d_jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[d_jobtitle_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_jt_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    d_jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_d_jobtitle_id'), primary_key=True, name='d_jobtitle_id')
    d_jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[d_jobtitle_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_jt_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodJtPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodJtPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodJtPermissionStateTuple = namedtuple('DJobPeriodJtPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'd_jobtitle_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodJtPermissionState(DJobPeriodJtPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_JT_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_jt_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_jobtitle_id = IColumn(BigInt, primary_key=True, name='d_jobtitle_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_jobtitle_id = IColumn(BigInt, primary_key=True, name='d_jobtitle_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodJtPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodJtPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodManagerAssignmentQueueTuple = namedtuple('DJobPeriodManagerAssignmentQueueTuple',  ('id', 'job_period_id', 'org_unit_manager_id', 'valid_from', 'status'  ))

class DJobPeriodManagerAssignmentQueue(DJobPeriodManagerAssignmentQueueMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_MANAGER_ASSIGNMENT_QUEUE'
    __entity_name__ = 'D_job_period_manager_assignment_queue'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_manager_assignment_queue_job_period_id'), nullable=False, name='job_period_id')
    job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[job_period_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_D_job_period_manager_assignment_queue_org_unit_manager_id'), nullable=False, name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    valid_from = IColumn(db.DateTime, nullable=False, name='valid_from')

    status = IColumn(Status, nullable=False, name='status')

    def to_named_tuple(self):
        return DJobPeriodManagerAssignmentQueueTuple(id=self.id,job_period_id=self.job_period_id,org_unit_manager_id=self.org_unit_manager_id,valid_from=self.valid_from,status=self.status,)

    def to_plain_object(self):
        return DJobPeriodManagerAssignmentQueueTuple(id=self.id,job_period_id=self.job_period_id,org_unit_manager_id=self.org_unit_manager_id,valid_from=self.valid_from,status=self.status,)

DJobPeriodMergeLogTuple = namedtuple('DJobPeriodMergeLogTuple',  ('preserved', 'removed', 'created_by', 'valid_from'  ))

class DJobPeriodMergeLog(DJobPeriodMergeLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_MERGE_LOG'
    __entity_name__ = 'D_job_period_merge_log'
    __parent_entity__ = None

    preserved = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_merge_log_preserved'), primary_key=True, name='preserved')

    removed = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_merge_log_removed'), primary_key=True, name='removed')

    preserved = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_merge_log_preserved'), primary_key=True, name='preserved')

    removed = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_merge_log_removed'), primary_key=True, name='removed')

    created_by = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_D_job_period_merge_log_created_by'), nullable=False, name='created_by')

    valid_from = IColumn(db.DateTime, nullable=False, name='valid_from')

    def to_named_tuple(self):
        return DJobPeriodMergeLogTuple(preserved=self.preserved,removed=self.removed,created_by=self.created_by,valid_from=self.valid_from,)

    def to_plain_object(self):
        return DJobPeriodMergeLogTuple(preserved=self.preserved,removed=self.removed,created_by=self.created_by,valid_from=self.valid_from,)

DJobPeriodOrgGroupPermissionLogTuple = namedtuple('DJobPeriodOrgGroupPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'valid_from', 'i_job_role_id', 'i_org_group_id', 'start_date', 'end_date'  ))

class DJobPeriodOrgGroupPermissionLog(DJobPeriodOrgGroupPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ORG_GROUP_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_org_group_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_org_group_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_org_group_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_org_group_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_org_group_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    i_job_role_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_org_group_permission_log_i_job_role_id'), name='i_job_role_id')
    i_job_role = IRelationship(lambda: IJobRole, foreign_keys=[i_job_role_id])

    i_org_group_id = IColumn(BigInt, db.ForeignKey('I_ORG_GROUP.id', use_alter=True, name='fk_D_job_period_org_group_permission_log_i_org_group_id'), nullable=False, name='i_org_group_id')
    i_org_group = IRelationship(lambda: IOrgGroup, foreign_keys=[i_org_group_id])

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodOrgGroupPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodOrgGroupPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodOrgGroupPermissionStateTuple = namedtuple('DJobPeriodOrgGroupPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'valid_from', 'i_job_role_id', 'i_org_group_id', 'start_date', 'end_date'  ))

class DJobPeriodOrgGroupPermissionState(DJobPeriodOrgGroupPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ORG_GROUP_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_org_group_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    i_job_role_id = IColumn(BigInt, name='i_job_role_id')

    i_org_group_id = IColumn(BigInt, nullable=False, name='i_org_group_id')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodOrgGroupPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodOrgGroupPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodOrgSpecPermissionLogTuple = namedtuple('DJobPeriodOrgSpecPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'valid_from', 'i_job_role_id', 'org_spec', 'start_date', 'end_date'  ))

class DJobPeriodOrgSpecPermissionLog(DJobPeriodOrgSpecPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ORG_SPEC_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_org_spec_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_org_spec_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_org_spec_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_org_spec_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_org_spec_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    i_job_role_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_job_period_org_spec_permission_log_i_job_role_id'), name='i_job_role_id')
    i_job_role = IRelationship(lambda: IJobRole, foreign_keys=[i_job_role_id])

    org_spec = IColumn(OrgSpec, name='org_spec')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodOrgSpecPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodOrgSpecPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodOrgSpecPermissionStateTuple = namedtuple('DJobPeriodOrgSpecPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'valid_from', 'i_job_role_id', 'org_spec', 'start_date', 'end_date'  ))

class DJobPeriodOrgSpecPermissionState(DJobPeriodOrgSpecPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_ORG_SPEC_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_org_spec_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    i_job_role_id = IColumn(BigInt, name='i_job_role_id')

    org_spec = IColumn(db.Integer, name='org_spec')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodOrgSpecPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodOrgSpecPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,i_job_role_id=self.i_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodOuPermissionLogTuple = namedtuple('DJobPeriodOuPermissionLogTuple',  ('d_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodOuPermissionLog(DJobPeriodOuPermissionLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_OU_PERMISSION_LOG'
    __entity_name__ = 'D_job_period_ou_permission_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_ou_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IOrgUnit, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IOrgUnit, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_ou_permission_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_job_period_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IOrgUnit, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_job_period_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IOrgUnit, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodOuPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodOuPermissionLogTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodOuPermissionStateTuple = namedtuple('DJobPeriodOuPermissionStateTuple',  ('d_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodOuPermissionState(DJobPeriodOuPermissionStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_OU_PERMISSION_STATE'
    __entity_name__ = 'D_job_period_ou_permission_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodOuPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodOuPermissionStateTuple(d_job_period_id=self.d_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodSubstituteTuple = namedtuple('DJobPeriodSubstituteTuple',  ('id', 'd_job_period_id', 'd_substistute_person_id', 'start_date', 'end_date', 'is_backup', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DJobPeriodSubstitute(API,DJobPeriodSubstituteMixin, Base, db.Model):
    __tablename__ = 'D_JOB_PERIOD_SUBSTITUTE'
    __entity_name__ = 'D_job_period_substitute'
    __plain_object__ = DJobPeriodSubstitutePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_substitute_d_job_period_id'), name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    d_substistute_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_job_period_substitute_d_substistute_person_id'), name='d_substistute_person_id')
    d_substistute_person = IRelationship(lambda: DPerson, foreign_keys=[d_substistute_person_id])

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    is_backup = IColumn(CharBool, nullable=False, name='is_backup')

    def to_named_tuple(self):
        return DJobPeriodSubstituteTuple(id=self.id,d_job_period_id=self.d_job_period_id,d_substistute_person_id=self.d_substistute_person_id,start_date=self.start_date,end_date=self.end_date,is_backup=self.is_backup,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DJobPeriodSubstituteTuple(id=self.id,d_job_period_id=self.d_job_period_id,d_substistute_person_id=self.d_substistute_person_id,start_date=self.start_date,end_date=self.end_date,is_backup=self.is_backup,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DJobPeriodSubstitutePermissionsTuple = namedtuple('DJobPeriodSubstitutePermissionsTuple',  ('id', 'd_job_period_substitute_id', 'd_job_period_id', 'status'  ))

class DJobPeriodSubstitutePermissions(DJobPeriodSubstitutePermissionsMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_SUBSTITUTE_PERMISSIONS'
    __entity_name__ = 'D_job_period_substitute_permissions'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    d_job_period_substitute_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD_SUBSTITUTE.id', use_alter=True, name='fk_D_job_period_sub_d_job_period_sub_637bcedf'), name='d_job_period_substitute_id')
    d_job_period_substitute = IRelationship(lambda: DJobPeriodSubstitute, foreign_keys=[d_job_period_substitute_id])

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_substitute_permissions_d_job_period_id'), name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return DJobPeriodSubstitutePermissionsTuple(id=self.id,d_job_period_substitute_id=self.d_job_period_substitute_id,d_job_period_id=self.d_job_period_id,status=self.status,)

    def to_plain_object(self):
        return DJobPeriodSubstitutePermissionsTuple(id=self.id,d_job_period_substitute_id=self.d_job_period_substitute_id,d_job_period_id=self.d_job_period_id,status=self.status,)

DJobPeriodValidityLogTuple = namedtuple('DJobPeriodValidityLogTuple',  ('d_job_period_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodValidityLog(DJobPeriodValidityLogMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_VALIDITY_LOG'
    __entity_name__ = 'D_job_period_validity_log'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_validity_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_D_job_period_validity_log_d_job_period_id'), primary_key=True, name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodValidityLogTuple(d_job_period_id=self.d_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodValidityLogTuple(d_job_period_id=self.d_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobPeriodValidityStateTuple = namedtuple('DJobPeriodValidityStateTuple',  ('d_job_period_id', 'valid_from', 'start_date', 'end_date'  ))

class DJobPeriodValidityState(DJobPeriodValidityStateMixin, db.Model):
    __tablename__ = 'D_JOB_PERIOD_VALIDITY_STATE'
    __entity_name__ = 'D_job_period_validity_state'
    __parent_entity__ = None

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    d_job_period_id = IColumn(BigInt, primary_key=True, name='d_job_period_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return DJobPeriodValidityStateTuple(d_job_period_id=self.d_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return DJobPeriodValidityStateTuple(d_job_period_id=self.d_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

DJobtitleTuple = namedtuple('DJobtitleTuple',  ('id', 'code', 'name', 'name6', 'description', 'jobrole_id', 'status', 'classification1', 'classification2', 'classification3', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DJobtitle(API,DJobtitleMixin, Base, db.Model):
    __tablename__ = 'D_JOBTITLE'
    __entity_name__ = 'D_jobtitle'
    __plain_object__ = DJobtitlePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(24), nullable=False, unique=True, name='code')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    name6 = IColumn(db.VARCHAR(64), name='name6')

    description = IColumn(db.TEXT, name='description')

    jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_jobtitle_jobrole_id'), name='jobrole_id')
    jobrole = IRelationship(lambda: IJobRole, foreign_keys=[jobrole_id])

    status = IColumn(Status, name='status')
    __classification = Header(u'classification')

    classification1 = IColumn(db.VARCHAR(64), name='classification1')

    classification2 = IColumn(db.VARCHAR(64), name='classification2')

    classification3 = IColumn(db.VARCHAR(64), name='classification3')

    def to_named_tuple(self):
        return DJobtitleTuple(id=self.id,code=self.code,name=self.name,name6=self.name6,description=self.description,jobrole_id=self.jobrole_id,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DJobtitleTuple(id=self.id,code=self.code,name=self.name,name6=self.name6,description=self.description,jobrole_id=self.jobrole_id,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DMappingRuleTuple = namedtuple('DMappingRuleTuple',  ('id', 'code', 'name', 'description', 'mdm_source_id', 'source_field', 'target_table', 'target_field', 'target_datatype', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DMappingRule(API,DMappingRuleMixin, Base, db.Model):
    __tablename__ = 'D_MAPPING_RULE'
    __entity_name__ = 'D_mapping_rule'
    __plain_object__ = DMappingRulePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(24), name='code')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    mdm_source_id = IColumn(BigInt, db.ForeignKey('G_MDM_SOURCE.id', use_alter=True, name='fk_D_mapping_rule_mdm_source_id'), name='mdm_source_id')
    mdm_source = IRelationship(lambda: GMdmSource, foreign_keys=[mdm_source_id])

    source_field = IColumn(db.VARCHAR(64), name='source_field')

    target_table = IColumn(db.VARCHAR(64), name='target_table')

    target_field = IColumn(db.VARCHAR(64), name='target_field')

    target_datatype = IColumn(TargetDatatype, name='target_datatype')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return DMappingRuleTuple(id=self.id,code=self.code,name=self.name,description=self.description,mdm_source_id=self.mdm_source_id,source_field=self.source_field,target_table=self.target_table,target_field=self.target_field,target_datatype=self.target_datatype,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DMappingRuleTuple(id=self.id,code=self.code,name=self.name,description=self.description,mdm_source_id=self.mdm_source_id,source_field=self.source_field,target_table=self.target_table,target_field=self.target_field,target_datatype=self.target_datatype,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DPersonTuple = namedtuple('DPersonTuple',  ('id', 'social_security_number', 'personnel_number', 'name_prefix', 'first_name', 'middle_name', 'last_name', 'preferred_name', 'identity_id', 'permanent', 'starting_date', 'termination_date', 'termination_type', 'information_checked', 'email_active', 'photo', 'username', 'orgunit_id', 'email', 'pupo', 'sv_number', 'other_address', 'language_id', 'status', 'b_phone', 'b_mobile', 'jr_start_date', 'is_manager', 'jobtitle_id', 'jobtitle', 'jobfamily_id', 'jobrole_id', 'job_type', 'manager_id', 'manager_name', 'manager_email', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'exc_location_id', 'remote_office', 'location_info', 'home_street', 'home_street2', 'home_post', 'home_city', 'home_state', 'homecountry_id', 'identity_checked', 'identitysource_id', 'personal_id', 'staff_oper_code', 'full_time', 'birth_date', 'gender', 'nationality_id', 'int_job_title', 'int_job_code', 'int_code_code2', 'mdm_source_id', 'mdm_person_id', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'last_checking_date', 'last_import_date', 'absence_status', 'exc_businessarea_id', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_country_id', 'waiting_manager_approval', 'manager_approved_id', 'manager_approval_timestamp', 'first_email_sent_timestamp', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DPerson(API,DPersonMixin, Base, db.Model):
    __tablename__ = 'O_D_PERSON'
    __entity_name__ = 'D_person'
    __plain_object__ = DPersonPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    social_security_number = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='social_security_number')

    personnel_number = IColumn(db.VARCHAR(20), unique=True, name='personnel_no')

    name_prefix = IColumn(NamePrefix, name='name_prefix')

    first_name = IColumn(db.VARCHAR(64), nullable=False, name='first_name')

    middle_name = IColumn(db.VARCHAR(64), name='middle_name')

    last_name = IColumn(db.VARCHAR(64), nullable=False, name='last_name')

    preferred_name = IColumn(db.VARCHAR(64), name='nickname')

    identity_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY.id', use_alter=True, name='fk_D_person_identity_id'), name='identity_id')
    identity = IRelationship(lambda: GIdentity, foreign_keys=[identity_id])

    permanent = IColumn(CharBool, nullable=False, name='permanent')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    termination_type = IColumn(TermType, name='term_type')

    information_checked = IColumn(CharBool, nullable=False, name='information_checked')

    email_active = IColumn(CharBool, nullable=False, name='email_active')
    __user_info = Header(u'user_info')

    photo = IColumn(db.TEXT, name='photo')

    username = IColumn(db.VARCHAR(64), unique=True, name='username')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_D_person_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    email = IColumn(db.VARCHAR(64), name='email')

    pupo = IColumn(db.VARCHAR(4), name='voice_address')

    sv_number = IColumn(db.VARCHAR(64), name='sv_number')

    other_address = IColumn(db.VARCHAR(256), name='other_address')

    language_id = IColumn(BigInt, db.ForeignKey('G_LANGUAGE.id', use_alter=True, name='fk_D_person_language_id'), name='language_id')
    language = IRelationship(lambda: GLanguage, foreign_keys=[language_id])

    status = IColumn(Status, name='status')

    b_phone = IColumn(db.VARCHAR(64), name='b_phone')

    b_mobile = IColumn(db.VARCHAR(64), name='b_mobile')
    __job_periods = Header(u'job_periods')

    job_periods = IRelationship(lambda: DJobPeriod, foreign_keys=lambda: [DJobPeriod.person_id], uselist=True)
    manager_in_job_periods = IRelationship(lambda: DJobPeriod, foreign_keys=lambda: [DJobPeriod.manager_id], uselist=True)
    manager_in_external_job_periods = IRelationship(lambda: EJobPeriod, foreign_keys=lambda: [EJobPeriod.manager_id], uselist=True)
    __card_details = Header(u'card_details')

    cards = IRelationship(lambda: CCard, foreign_keys=lambda: [CCard.person_id], uselist=True)
    __key_details = Header(u'key_details')

    keys = IRelationship(lambda: CKey, foreign_keys=lambda: [CKey.person_id], uselist=True)
    __Device_details = Header(u'Device_details')

    devices = IRelationship(lambda: CDevicePerson, foreign_keys=lambda: [CDevicePerson.person_id], uselist=True)
    __employment = Header(u'employment')

    jr_start_date = IColumn(db.Date, name='jr_start_date')

    is_manager = IColumn(CharBool, nullable=False, name='is_manager')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_D_person_jobtitle_id'), name='jobtitle_id')
    _jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    jobtitle = IColumn(db.VARCHAR(64), name='jobtitle')

    jobfamily_id = IColumn(BigInt, db.ForeignKey('I_JOB_FAMILY.id', use_alter=True, name='fk_D_person_jobfamily_id'), name='jobfamily_id')
    jobfamily = IRelationship(lambda: IJobFamily, foreign_keys=[jobfamily_id])

    jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_D_person_jobrole_id'), name='jobrole_id')
    jobrole = IRelationship(lambda: IJobRole, foreign_keys=[jobrole_id])

    job_type = IColumn(JobType, name='job_type')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_manager_id'), name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id], remote_side=[id])

    manager_name = IColumn(db.VARCHAR(64), name='manager_name')

    manager_email = IColumn(db.VARCHAR(64), name='manager_email')

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_subst_manager_id'), name='subst_manager_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id], remote_side=[id])

    subst_manager_name = IColumn(db.VARCHAR(64), name='subst_manager_name')

    subst_manager_email = IColumn(db.VARCHAR(64), name='subst_manager_email')

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')

    exc_location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_D_person_exc_location_id'), name='exc_location_id')
    exc_location = IRelationship(lambda: ILocation, foreign_keys=[exc_location_id])

    remote_office = IColumn(CharBool, nullable=False, name='remote_office')

    location_info = IColumn(db.VARCHAR(64), name='location_info')

    home_street = IColumn(db.VARCHAR(64), name='home_street')

    home_street2 = IColumn(db.VARCHAR(64), name='home_street2')

    home_post = IColumn(db.VARCHAR(64), name='home_post')

    home_city = IColumn(db.VARCHAR(64), name='home_city')

    home_state = IColumn(db.VARCHAR(64), name='home_state')

    homecountry_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_D_person_homecountry_id'), name='homecountry_id')
    homecountry = IRelationship(lambda: GCountry, foreign_keys=[homecountry_id])
    __hr_info = Header(u'hr_info')

    identity_checked = IColumn(CharBool, nullable=False, name='identity_checked')

    identitysource_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY_SOURCE.id', use_alter=True, name='fk_D_person_identitysource_id'), name='identitysource_id')
    identitysource = IRelationship(lambda: GIdentitySource, foreign_keys=[identitysource_id])

    personal_id = IColumn(db.VARCHAR(64), name='personal_id')

    staff_oper_code = IColumn(StaffOperCode, name='staff_oper_code')

    full_time = IColumn(CharBool, nullable=False, name='full_time')

    birth_date = IColumn(db.Date, name='birth_date')

    gender = IColumn(Gender, name='gender')

    nationality_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_D_person_nationality_id'), name='nationality_id')
    nationality = IRelationship(lambda: GCountry, foreign_keys=[nationality_id])

    int_job_title = IColumn(db.VARCHAR(64), name='int_job_title')

    int_job_code = IColumn(db.VARCHAR(64), name='int_job_code')

    int_code_code2 = IColumn(db.VARCHAR(64), name='int_code_code2')

    mdm_source_id = IColumn(BigInt, db.ForeignKey('G_MDM_SOURCE.id', use_alter=True, name='fk_D_person_mdm_source_id'), name='mdm_source_id')
    mdm_source = IRelationship(lambda: GMdmSource, foreign_keys=[mdm_source_id])

    mdm_person_id = IColumn(db.VARCHAR(64), name='mdm_person_id')

    flag1 = IColumn(CharBool, nullable=False, name='flag1')

    flag2 = IColumn(CharBool, nullable=False, name='flag2')

    flag3 = IColumn(CharBool, nullable=False, name='flag3')

    flag4 = IColumn(CharBool, nullable=False, name='flag4')

    flag5 = IColumn(CharBool, nullable=False, name='flag5')

    original_source = IColumn(OriginalSource, name='original_source')
    __sync_info = Header(u'sync_info')

    attribute1 = IColumn(db.VARCHAR(64), name='attribute1')

    attribute2 = IColumn(db.VARCHAR(64), name='attribute2')

    attribute3 = IColumn(db.VARCHAR(64), name='attribute3')

    attribute4 = IColumn(db.VARCHAR(64), name='attribute4')

    attribute5 = IColumn(db.VARCHAR(64), name='attribute5')

    last_checking_date = IColumn(db.Date, name='last_checking_date')

    last_import_date = IColumn(db.Date, name='last_import_date')
    __absent_periods = Header(u'absent_periods')

    absence_status = IColumn(AbsenceStatus, name='absence_status')
    absences = IRelationship(lambda: DAbsence, foreign_keys=lambda: [DAbsence.person_id], uselist=True)
    __authentication = Header(u'authentication')

    authentications = IRelationship(lambda: DUserAuth, foreign_keys=lambda: [DUserAuth.person_id], uselist=True)
    __exceptions = Header(u'exceptions')

    exc_businessarea_id = IColumn(BigInt, db.ForeignKey('O_I_BUSINESS_AREA.id', use_alter=True, name='fk_D_person_exc_businessarea_id'), name='exc_businessarea_id')
    exc_businessarea = IRelationship(lambda: IBusinessArea, foreign_keys=[exc_businessarea_id])

    exc_legalcompany_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_D_person_exc_legalcompany_id'), name='exc_legalcompany_id')
    exc_legalcompany = IRelationship(lambda: ILegalCompany, foreign_keys=[exc_legalcompany_id])

    exc_costcenter_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_D_person_exc_costcenter_id'), name='exc_costcenter_id')
    exc_costcenter = IRelationship(lambda: ICostCenter, foreign_keys=[exc_costcenter_id])

    exc_country_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_D_person_exc_country_id'), name='exc_country_id')
    exc_country = IRelationship(lambda: GCountry, foreign_keys=[exc_country_id])
    __approvals = Header(u'approvals')

    waiting_manager_approval = IColumn(CharBool, nullable=False, name='waiting_manager_approval')

    manager_approved_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_D_person_manager_approved_id'), name='manager_approved_id')
    manager_approved = IRelationship(lambda: Zuser, foreign_keys=[manager_approved_id])

    manager_approval_timestamp = IColumn(db.DateTime, name='manager_approval_timestamp')

    first_email_sent_timestamp = IColumn(db.DateTime, name='first_email_sent_timestamp')
    __user_accounts = Header(u'user_accounts')

    user_accounts = IRelationship(lambda: GPersonUseraccount, foreign_keys=lambda: [GPersonUseraccount.person_id], uselist=True)
    organization_units = IRelationship(lambda: IOrgUnit, secondary=lambda: DPersonIOrgUnit, uselist=True)
    education = IRelationship(lambda: DEducation, secondary=lambda: DPersonDEducation, uselist=True)
    competences = IRelationship(lambda: DCompetence, secondary=lambda: DPersonDCompetence, uselist=True)

    def to_named_tuple(self):
        return DPersonTuple(id=self.id,social_security_number=self.social_security_number,personnel_number=self.personnel_number,name_prefix=self.name_prefix,first_name=self.first_name,middle_name=self.middle_name,last_name=self.last_name,preferred_name=self.preferred_name,identity_id=self.identity_id,permanent=self.permanent,starting_date=self.starting_date,termination_date=self.termination_date,termination_type=self.termination_type,information_checked=self.information_checked,email_active=self.email_active,photo=self.photo,username=self.username,orgunit_id=self.orgunit_id,email=self.email,pupo=self.pupo,sv_number=self.sv_number,other_address=self.other_address,language_id=self.language_id,status=self.status,b_phone=self.b_phone,b_mobile=self.b_mobile,jr_start_date=self.jr_start_date,is_manager=self.is_manager,jobtitle_id=self.jobtitle_id,jobtitle=self.jobtitle,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,manager_id=self.manager_id,manager_name=self.manager_name,manager_email=self.manager_email,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,exc_location_id=self.exc_location_id,remote_office=self.remote_office,location_info=self.location_info,home_street=self.home_street,home_street2=self.home_street2,home_post=self.home_post,home_city=self.home_city,home_state=self.home_state,homecountry_id=self.homecountry_id,identity_checked=self.identity_checked,identitysource_id=self.identitysource_id,personal_id=self.personal_id,staff_oper_code=self.staff_oper_code,full_time=self.full_time,birth_date=self.birth_date,gender=self.gender,nationality_id=self.nationality_id,int_job_title=self.int_job_title,int_job_code=self.int_job_code,int_code_code2=self.int_code_code2,mdm_source_id=self.mdm_source_id,mdm_person_id=self.mdm_person_id,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,attribute1=self.attribute1,attribute2=self.attribute2,attribute3=self.attribute3,attribute4=self.attribute4,attribute5=self.attribute5,last_checking_date=self.last_checking_date,last_import_date=self.last_import_date,absence_status=self.absence_status,exc_businessarea_id=self.exc_businessarea_id,exc_legalcompany_id=self.exc_legalcompany_id,exc_costcenter_id=self.exc_costcenter_id,exc_country_id=self.exc_country_id,waiting_manager_approval=self.waiting_manager_approval,manager_approved_id=self.manager_approved_id,manager_approval_timestamp=self.manager_approval_timestamp,first_email_sent_timestamp=self.first_email_sent_timestamp,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DPersonTuple(id=self.id,social_security_number=self.social_security_number,personnel_number=self.personnel_number,name_prefix=self.name_prefix,first_name=self.first_name,middle_name=self.middle_name,last_name=self.last_name,preferred_name=self.preferred_name,identity_id=self.identity_id,permanent=self.permanent,starting_date=self.starting_date,termination_date=self.termination_date,termination_type=self.termination_type,information_checked=self.information_checked,email_active=self.email_active,photo=self.photo,username=self.username,orgunit_id=self.orgunit_id,email=self.email,pupo=self.pupo,sv_number=self.sv_number,other_address=self.other_address,language_id=self.language_id,status=self.status,b_phone=self.b_phone,b_mobile=self.b_mobile,jr_start_date=self.jr_start_date,is_manager=self.is_manager,jobtitle_id=self.jobtitle_id,jobtitle=self.jobtitle,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,manager_id=self.manager_id,manager_name=self.manager_name,manager_email=self.manager_email,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,exc_location_id=self.exc_location_id,remote_office=self.remote_office,location_info=self.location_info,home_street=self.home_street,home_street2=self.home_street2,home_post=self.home_post,home_city=self.home_city,home_state=self.home_state,homecountry_id=self.homecountry_id,identity_checked=self.identity_checked,identitysource_id=self.identitysource_id,personal_id=self.personal_id,staff_oper_code=self.staff_oper_code,full_time=self.full_time,birth_date=self.birth_date,gender=self.gender,nationality_id=self.nationality_id,int_job_title=self.int_job_title,int_job_code=self.int_job_code,int_code_code2=self.int_code_code2,mdm_source_id=self.mdm_source_id,mdm_person_id=self.mdm_person_id,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,attribute1=self.attribute1,attribute2=self.attribute2,attribute3=self.attribute3,attribute4=self.attribute4,attribute5=self.attribute5,last_checking_date=self.last_checking_date,last_import_date=self.last_import_date,absence_status=self.absence_status,exc_businessarea_id=self.exc_businessarea_id,exc_legalcompany_id=self.exc_legalcompany_id,exc_costcenter_id=self.exc_costcenter_id,exc_country_id=self.exc_country_id,waiting_manager_approval=self.waiting_manager_approval,manager_approved_id=self.manager_approved_id,manager_approval_timestamp=self.manager_approval_timestamp,first_email_sent_timestamp=self.first_email_sent_timestamp,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

DPersonAbsenceEndedTuple = namedtuple('DPersonAbsenceEndedTuple',  ('d_person_id', 'end_date'  ))

class DPersonAbsenceEnded(DPersonAbsenceEndedMixin, db.Model):
    __tablename__ = 'D_PERSON_ABSENCE_ENDED'
    __entity_name__ = 'D_person_absence_ended'
    __parent_entity__ = None

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_absence_ended_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    end_date = IColumn(db.Date, primary_key=True, name='end_date')

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_absence_ended_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    end_date = IColumn(db.Date, primary_key=True, name='end_date')

    def to_named_tuple(self):
        return DPersonAbsenceEndedTuple(d_person_id=self.d_person_id,end_date=self.end_date,)

    def to_plain_object(self):
        return DPersonAbsenceEndedTuple(d_person_id=self.d_person_id,end_date=self.end_date,)

DPersonAbsenceStartedTuple = namedtuple('DPersonAbsenceStartedTuple',  ('d_person_id', 'start_date'  ))

class DPersonAbsenceStarted(DPersonAbsenceStartedMixin, db.Model):
    __tablename__ = 'D_PERSON_ABSENCE_STARTED'
    __entity_name__ = 'D_person_absence_started'
    __parent_entity__ = None

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_absence_started_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    start_date = IColumn(db.Date, primary_key=True, name='start_date')

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_absence_started_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    start_date = IColumn(db.Date, primary_key=True, name='start_date')

    def to_named_tuple(self):
        return DPersonAbsenceStartedTuple(d_person_id=self.d_person_id,start_date=self.start_date,)

    def to_plain_object(self):
        return DPersonAbsenceStartedTuple(d_person_id=self.d_person_id,start_date=self.start_date,)

DPersonPermissionManualProvisioningLogTuple = namedtuple('DPersonPermissionManualProvisioningLogTuple',  ('d_person_id', 'g_service_role_id', 'provisioned_at', 'g_service_id', 'status'  ))

class DPersonPermissionManualProvisioningLog(DPersonPermissionManualProvisioningLogMixin, db.Model):
    __tablename__ = 'D_PERSON_PERMISSION_MANUAL_PROVISIONING_LOG'
    __entity_name__ = 'D_person_permission_manual_provisioning_log'
    __parent_entity__ = None

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_permission_manual_provisioning_log_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_person_permiss_g_service_role_i_06815d9f'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_permission_manual_provisioning_log_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    g_service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_D_person_permission_manual_provisioning_log_g_service_id'), nullable=False, name='g_service_id')
    g_service = IRelationship(lambda: GService, foreign_keys=[g_service_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_person_permiss_g_service_role_i_06815d9f'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return DPersonPermissionManualProvisioningLogTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return DPersonPermissionManualProvisioningLogTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

DPersonPermissionManualProvisioningStateTuple = namedtuple('DPersonPermissionManualProvisioningStateTuple',  ('d_person_id', 'g_service_role_id', 'provisioned_at', 'g_service_id', 'status'  ))

class DPersonPermissionManualProvisioningState(DPersonPermissionManualProvisioningStateMixin, db.Model):
    __tablename__ = 'D_PERSON_PERMISSION_MANUAL_PROVISIONING_STATE'
    __entity_name__ = 'D_person_permission_manual_provisioning_state'
    __parent_entity__ = None

    d_person_id = IColumn(BigInt, primary_key=True, name='d_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_person_id = IColumn(BigInt, primary_key=True, name='d_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    provisioned_at = IColumn(db.DateTime, name='provisioned_at')

    g_service_id = IColumn(BigInt, nullable=False, name='g_service_id')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return DPersonPermissionManualProvisioningStateTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return DPersonPermissionManualProvisioningStateTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

DPersonPermissionProvisioningLogTuple = namedtuple('DPersonPermissionProvisioningLogTuple',  ('d_person_id', 'g_service_role_id', 'g_system_id', 'provisioned_at', 'g_service_id', 'status'  ))

class DPersonPermissionProvisioningLog(DPersonPermissionProvisioningLogMixin, db.Model):
    __tablename__ = 'D_PERSON_PERMISSION_PROVISIONING_LOG'
    __entity_name__ = 'D_person_permission_provisioning_log'
    __parent_entity__ = None

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_permission_provisioning_log_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_person_permission_provisioning_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_D_person_permission_provisioning_log_g_system_id'), primary_key=True, name='g_system_id')
    g_system = IRelationship(lambda: GSystem, foreign_keys=[g_system_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_person_permission_provisioning_log_d_person_id'), primary_key=True, name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    g_service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_D_person_permission_provisioning_log_g_service_id'), nullable=False, name='g_service_id')
    g_service = IRelationship(lambda: GService, foreign_keys=[g_service_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_D_person_permission_provisioning_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_D_person_permission_provisioning_log_g_system_id'), primary_key=True, name='g_system_id')
    g_system = IRelationship(lambda: GSystem, foreign_keys=[g_system_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return DPersonPermissionProvisioningLogTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return DPersonPermissionProvisioningLogTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

DPersonPermissionProvisioningStateTuple = namedtuple('DPersonPermissionProvisioningStateTuple',  ('d_person_id', 'g_service_role_id', 'g_system_id', 'provisioned_at', 'g_service_id', 'status'  ))

class DPersonPermissionProvisioningState(DPersonPermissionProvisioningStateMixin, db.Model):
    __tablename__ = 'D_PERSON_PERMISSION_PROVISIONING_STATE'
    __entity_name__ = 'D_person_permission_provisioning_state'
    __parent_entity__ = None

    d_person_id = IColumn(BigInt, primary_key=True, name='d_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_system_id = IColumn(BigInt, primary_key=True, name='g_system_id')

    d_person_id = IColumn(BigInt, primary_key=True, name='d_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_system_id = IColumn(BigInt, primary_key=True, name='g_system_id')

    provisioned_at = IColumn(db.DateTime, name='provisioned_at')

    g_service_id = IColumn(BigInt, nullable=False, name='g_service_id')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return DPersonPermissionProvisioningStateTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return DPersonPermissionProvisioningStateTuple(d_person_id=self.d_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

DUserAuthTuple = namedtuple('DUserAuthTuple',  ('id', 'device_id', 'classification1', 'classification2', 'person_id', 'authmethod_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class DUserAuth(API,DUserAuthMixin, Base, db.Model):
    __tablename__ = 'D_USER_AUTH'
    __entity_name__ = 'D_user_auth'
    __plain_object__ = DUserAuthPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    device_id = IColumn(db.VARCHAR(64), name='device_id')

    classification1 = IColumn(db.VARCHAR(64), name='classification1')

    classification2 = IColumn(db.VARCHAR(64), name='classification2')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_D_user_auth_person_id'), nullable=False, name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    authmethod_id = IColumn(BigInt, db.ForeignKey('D_AUTH_METHOD.id', use_alter=True, name='fk_D_user_auth_authmethod_id'), nullable=False, name='authmethod_id')
    authmethod = IRelationship(lambda: DAuthMethod, foreign_keys=[authmethod_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return DUserAuthTuple(id=self.id,device_id=self.device_id,classification1=self.classification1,classification2=self.classification2,person_id=self.person_id,authmethod_id=self.authmethod_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return DUserAuthTuple(id=self.id,device_id=self.device_id,classification1=self.classification1,classification2=self.classification2,person_id=self.person_id,authmethod_id=self.authmethod_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EExtOrgTuple = namedtuple('EExtOrgTuple',  ('id', 'header_row', 'outsider', 'name', 'alias', 'company_code', 'upper_ext_org_id', 'ext_org_type_id', 'ext_org_profile', 'virtual_org', 'contract_id', 'favorite', 'show_in_student', 'starting_date', 'termination_date', 'status', 'ext_superior_id', 'substitute_active', 'manager_id', 'superior_name', 'superior_email', 'subst_manager_id', 'subst_s_name', 'subst_s_email', 'teamleader_person_id', 'teamleader_name', 'teamleader_email', 'hr_manager_person_id', 'hr_manager_name', 'hr_manager_email', 'ext_contact_name', 'ext_contact_phone', 'ext_contact_email', 'description', 'unit_id_1', 'unit_id_2', 'costcenter_id', 'financial_code_1', 'location_id', 'location_info', 'exc_street', 'exc_street2', 'exc_post', 'exc_city', 'exc_state', 'exc_country', 'exc_office_phone', 'exc_office_fax', 'exc_office_timezone', 'exc_site_category', 'needs_int_contact_approval', 'needs_ext_contact_approval', 'default_language_id', 'default_jobrole_id', 'default_domain', 'distinguishedname', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EExtOrg(API,ClosureTableMixin,EExtOrgMixin, Base, db.Model):
    __tablename__ = 'O_E_EXT_ORG'
    __entity_name__ = 'E_ext_org'
    __plain_object__ = EExtOrgPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    header_row = IColumn(CharBool, nullable=False, name='header_row')

    outsider = IColumn(CharBool, nullable=False, name='outsider')

    name = IColumn(db.VARCHAR(256), nullable=False, unique=True, name='name')

    alias = IColumn(db.VARCHAR(256), name='alias')

    company_code = IColumn(db.VARCHAR(64), name='company_code')

    upper_ext_org_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_ext_org_upper_ext_org_id'), name='upper_ext_org_id')
    parent = IRelationship(lambda: EExtOrg, foreign_keys=[upper_ext_org_id], remote_side=[id])

    ext_org_type_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG_TYPE.id', use_alter=True, name='fk_E_ext_org_ext_org_type_id'), name='ext_org_type_id')
    ext_org_type = IRelationship(lambda: EExtOrgType, foreign_keys=[ext_org_type_id])

    ext_org_profile = IColumn(ExtOrgProfile, name='ext_org_profile')

    virtual_org = IColumn(VirtualOrg, name='virtual_org')

    contract_id = IColumn(db.VARCHAR(64), name='contract_id')

    favorite = IColumn(CharBool, nullable=False, name='favorite')

    show_in_student = IColumn(CharBool, nullable=False, name='show_in_student')
    __activation_info = Header(u'activation_info')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    status = IColumn(Status, name='status')
    __responsible_persons = Header(u'responsible_persons')

    ext_superior_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_ext_org_ext_superior_id'), name='ext_superior_id')
    ext_superior = IRelationship(lambda: EExternalPerson, foreign_keys=[ext_superior_id])

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_ext_org_superior_person_id'), name='superior_person_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    superior_name = IColumn(db.VARCHAR(64), name='superior_name')

    superior_email = IColumn(db.VARCHAR(64), name='superior_email')

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_ext_org_subst_s_person_id'), name='subst_s_person_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id])

    subst_s_name = IColumn(db.VARCHAR(64), name='subst_s_name')

    subst_s_email = IColumn(db.VARCHAR(64), name='subst_s_email')

    teamleader_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_ext_org_teamleader_person_id'), name='teamleader_person_id')
    teamleader_person = IRelationship(lambda: DPerson, foreign_keys=[teamleader_person_id])

    teamleader_name = IColumn(db.VARCHAR(64), name='teamleader_name')

    teamleader_email = IColumn(db.VARCHAR(64), name='teamleader_email')

    hr_manager_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_ext_org_hr_manager_person_id'), name='hr_manager_person_id')
    hr_manager_person = IRelationship(lambda: DPerson, foreign_keys=[hr_manager_person_id])

    hr_manager_name = IColumn(db.VARCHAR(64), name='hr_manager_name')

    hr_manager_email = IColumn(db.VARCHAR(64), name='hr_manager_email')

    ext_contact_name = IColumn(db.VARCHAR(64), name='ext_contact_name')

    ext_contact_phone = IColumn(db.VARCHAR(64), name='ext_contact_phone')

    ext_contact_email = IColumn(db.VARCHAR(64), name='ext_contact_email')

    description = IColumn(db.TEXT, name='description')

    unit_id_1 = IColumn(db.VARCHAR(64), name='unit_id_1')

    unit_id_2 = IColumn(db.VARCHAR(64), name='unit_id_2')

    costcenter_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_E_ext_org_costcenter_id'), name='costcenter_id')
    costcenter = IRelationship(lambda: ICostCenter, foreign_keys=[costcenter_id])

    financial_code_1 = IColumn(db.VARCHAR(64), name='financial_code_1')
    __office_info = Header(u'office_info')

    location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_E_ext_org_location_id'), name='location_id')
    location = IRelationship(lambda: ILocation, foreign_keys=[location_id])

    location_info = IColumn(db.VARCHAR(64), name='location_info')

    exc_street = IColumn(db.VARCHAR(64), name='exc_street')

    exc_street2 = IColumn(db.VARCHAR(64), name='exc_street2')

    exc_post = IColumn(db.VARCHAR(64), name='exc_post')

    exc_city = IColumn(db.VARCHAR(64), name='exc_city')

    exc_state = IColumn(db.VARCHAR(64), name='exc_state')

    exc_country = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_E_ext_org_exc_country'), name='exc_country')

    exc_office_phone = IColumn(db.VARCHAR(64), name='exc_office_phone')

    exc_office_fax = IColumn(db.VARCHAR(64), name='exc_office_fax')

    exc_office_timezone = IColumn(db.VARCHAR(64), name='exc_office_timezone')

    exc_site_category = IColumn(SiteCategory, name='exc_site_category')
    __approvals = Header(u'approvals')

    needs_int_contact_approval = IColumn(CharBool, nullable=False, name='needs_int_contact_approval')

    needs_ext_contact_approval = IColumn(CharBool, nullable=False, name='needs_ext_contact_approval')
    __defaults = Header(u'defaults')

    default_language_id = IColumn(BigInt, db.ForeignKey('G_LANGUAGE.id', use_alter=True, name='fk_E_ext_org_default_language_id'), name='default_language_id')
    default_language = IRelationship(lambda: GLanguage, foreign_keys=[default_language_id])

    default_jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_E_ext_org_default_jobrole_id'), name='default_jobrole_id')
    default_jobrole = IRelationship(lambda: IJobRole, foreign_keys=[default_jobrole_id])

    default_domain = IColumn(db.VARCHAR(64), name='default_domain')
    job_periods = IRelationship(lambda: EJobPeriod, foreign_keys=lambda: [EJobPeriod.ext_org_id], uselist=True)

    distinguishedname = IColumn(db.VARCHAR(512), name='distinguishedname')
    services = IRelationship(lambda: GService, secondary=lambda: EExtOrgGService, uselist=True)
    service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: EExtOrgGServiceRole, uselist=True)
    organization_groups = IRelationship(lambda: IOrgGroup, secondary=lambda: EExtOrgIOrgGroup, uselist=True)

    def to_named_tuple(self):
        return EExtOrgTuple(id=self.id,header_row=self.header_row,outsider=self.outsider,name=self.name,alias=self.alias,company_code=self.company_code,upper_ext_org_id=self.upper_ext_org_id,ext_org_type_id=self.ext_org_type_id,ext_org_profile=self.ext_org_profile,virtual_org=self.virtual_org,contract_id=self.contract_id,favorite=self.favorite,show_in_student=self.show_in_student,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,ext_superior_id=self.ext_superior_id,substitute_active=self.substitute_active,manager_id=self.manager_id,superior_name=self.superior_name,superior_email=self.superior_email,subst_manager_id=self.subst_manager_id,subst_s_name=self.subst_s_name,subst_s_email=self.subst_s_email,teamleader_person_id=self.teamleader_person_id,teamleader_name=self.teamleader_name,teamleader_email=self.teamleader_email,hr_manager_person_id=self.hr_manager_person_id,hr_manager_name=self.hr_manager_name,hr_manager_email=self.hr_manager_email,ext_contact_name=self.ext_contact_name,ext_contact_phone=self.ext_contact_phone,ext_contact_email=self.ext_contact_email,description=self.description,unit_id_1=self.unit_id_1,unit_id_2=self.unit_id_2,costcenter_id=self.costcenter_id,financial_code_1=self.financial_code_1,location_id=self.location_id,location_info=self.location_info,exc_street=self.exc_street,exc_street2=self.exc_street2,exc_post=self.exc_post,exc_city=self.exc_city,exc_state=self.exc_state,exc_country=self.exc_country,exc_office_phone=self.exc_office_phone,exc_office_fax=self.exc_office_fax,exc_office_timezone=self.exc_office_timezone,exc_site_category=self.exc_site_category,needs_int_contact_approval=self.needs_int_contact_approval,needs_ext_contact_approval=self.needs_ext_contact_approval,default_language_id=self.default_language_id,default_jobrole_id=self.default_jobrole_id,default_domain=self.default_domain,distinguishedname=self.distinguishedname,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EExtOrgTuple(id=self.id,header_row=self.header_row,outsider=self.outsider,name=self.name,alias=self.alias,company_code=self.company_code,upper_ext_org_id=self.upper_ext_org_id,ext_org_type_id=self.ext_org_type_id,ext_org_profile=self.ext_org_profile,virtual_org=self.virtual_org,contract_id=self.contract_id,favorite=self.favorite,show_in_student=self.show_in_student,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,ext_superior_id=self.ext_superior_id,substitute_active=self.substitute_active,manager_id=self.manager_id,superior_name=self.superior_name,superior_email=self.superior_email,subst_manager_id=self.subst_manager_id,subst_s_name=self.subst_s_name,subst_s_email=self.subst_s_email,teamleader_person_id=self.teamleader_person_id,teamleader_name=self.teamleader_name,teamleader_email=self.teamleader_email,hr_manager_person_id=self.hr_manager_person_id,hr_manager_name=self.hr_manager_name,hr_manager_email=self.hr_manager_email,ext_contact_name=self.ext_contact_name,ext_contact_phone=self.ext_contact_phone,ext_contact_email=self.ext_contact_email,description=self.description,unit_id_1=self.unit_id_1,unit_id_2=self.unit_id_2,costcenter_id=self.costcenter_id,financial_code_1=self.financial_code_1,location_id=self.location_id,location_info=self.location_info,exc_street=self.exc_street,exc_street2=self.exc_street2,exc_post=self.exc_post,exc_city=self.exc_city,exc_state=self.exc_state,exc_country=self.exc_country,exc_office_phone=self.exc_office_phone,exc_office_fax=self.exc_office_fax,exc_office_timezone=self.exc_office_timezone,exc_site_category=self.exc_site_category,needs_int_contact_approval=self.needs_int_contact_approval,needs_ext_contact_approval=self.needs_ext_contact_approval,default_language_id=self.default_language_id,default_jobrole_id=self.default_jobrole_id,default_domain=self.default_domain,distinguishedname=self.distinguishedname,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EExtOrgCtAllTuple = namedtuple('EExtOrgCtAllTuple',  ('ancestor', 'descendant'  ))

class EExtOrgCtAll(EExtOrgCtAllMixin, db.Model):
    __tablename__ = 'E_EXT_ORG_CT_ALL'
    __entity_name__ = 'E_ext_org_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_ext_org_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_ext_org_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_ext_org_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_ext_org_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return EExtOrgCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return EExtOrgCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

EExtOrgTypeTuple = namedtuple('EExtOrgTypeTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EExtOrgType(API,EExtOrgTypeMixin, Base, db.Model):
    __tablename__ = 'O_E_EXT_ORG_TYPE'
    __entity_name__ = 'E_ext_org_type'
    __plain_object__ = EExtOrgTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return EExtOrgTypeTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EExtOrgTypeTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EExternalPersonTuple = namedtuple('EExternalPersonTuple',  ('id', 'name_prefix', 'first_name', 'middle_name', 'last_name', 'preferred_name', 'identity_id', 'social_security_number', 'personnel_number', 'information_checked', 'student', 'email_active', 'photo', 'username', 'orig_orgunit_id', 'ext_org_id', 'e_job_role_id', 'contract_id', 'tax_number', 'org_email', 'b_phone', 'b_mobile', 'pupo', 'sv_number', 'other_address', 'ext_email', 'ext_superior', 'ext_superior_email', 'starting_date', 'termination_date', 'termination_type', 'recertification_date', 'ext_phone', 'language_id', 'status', 'e_status1', 'e_status2', 'e_status3', 'e_status4', 'orgunit_id', 'jr_start_date', 'is_manager', 'jobtitle', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'exc_costcenter_id', 'exc_location_id', 'manager_id', 'manager_name', 'manager_email', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'remote_office', 'location_info', 'home_street', 'home_street2', 'home_post', 'home_city', 'home_state', 'homecountry_id', 'home_emergency_contact', 'home_timezone', 'identity_checked', 'identitysource_id', 'personal_id', 'staff_oper_code', 'full_time', 'birth_date', 'gender', 'nationality_id', 'mdm_source_id', 'mdm_person_id', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'last_checking_date', 'last_import_date', 'absence_status', 'exc_businessarea_id', 'exc_legalcompany_id', 'exc_country_id', 'waiting_manager_approval', 'manager_approved_id', 'manager_approval_timestamp', 'first_email_sent_timestamp', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EExternalPerson(API,EExternalPersonMixin, Base, db.Model):
    __tablename__ = 'O_E_EXTERNAL_PERSON'
    __entity_name__ = 'E_external_person'
    __plain_object__ = EExternalPersonPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name_prefix = IColumn(NamePrefix, name='name_prefix')

    first_name = IColumn(db.VARCHAR(64), nullable=False, name='first_name')

    middle_name = IColumn(db.VARCHAR(64), name='middle_name')

    last_name = IColumn(db.VARCHAR(64), nullable=False, name='last_name')

    preferred_name = IColumn(db.VARCHAR(64), name='nickname')

    identity_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY.id', use_alter=True, name='fk_E_external_person_identity_id'), name='identity_id')
    identity = IRelationship(lambda: GIdentity, foreign_keys=[identity_id])

    social_security_number = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='social_security_number')

    personnel_number = IColumn(db.VARCHAR(20), unique=True, name='personnel_no')

    information_checked = IColumn(CharBool, nullable=False, name='information_checked')

    student = IColumn(CharBool, nullable=False, name='student')

    email_active = IColumn(CharBool, nullable=False, name='email_active')
    __user_info = Header(u'user_info')

    photo = IColumn(db.TEXT, name='photo')

    username = IColumn(db.VARCHAR(64), unique=True, name='username')

    orig_orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_external_person_orig_orgunit_id'), name='orig_orgunit_id')
    orig_orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orig_orgunit_id])

    ext_org_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_external_person_ext_org_id'), name='ext_org_id')
    ext_org = IRelationship(lambda: EExtOrg, foreign_keys=[ext_org_id])

    e_job_role_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_external_person_e_job_role_id'), name='e_job_role_id')
    e_job_role = IRelationship(lambda: EJobRole, foreign_keys=[e_job_role_id])

    contract_id = IColumn(db.VARCHAR(64), name='contract_id')

    tax_number = IColumn(db.VARCHAR(64), name='tax_number')

    org_email = IColumn(db.VARCHAR(64), name='org_email')

    b_phone = IColumn(db.VARCHAR(64), name='b_phone')

    b_mobile = IColumn(db.VARCHAR(64), nullable=False, name='b_mobile')

    pupo = IColumn(db.VARCHAR(4), name='voice_address')

    sv_number = IColumn(db.VARCHAR(64), name='sv_number')

    other_address = IColumn(db.VARCHAR(64), name='other_address')

    ext_email = IColumn(db.VARCHAR(64), name='ext_email')

    ext_superior = IColumn(db.VARCHAR(64), name='ext_superior')

    ext_superior_email = IColumn(db.VARCHAR(64), name='ext_superior_email')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    termination_type = IColumn(TermType, name='term_type')

    recertification_date = IColumn(db.Date, name='recertification_date')

    ext_phone = IColumn(db.VARCHAR(64), name='ext_phone')

    language_id = IColumn(BigInt, db.ForeignKey('G_LANGUAGE.id', use_alter=True, name='fk_E_external_person_language_id'), name='language_id')
    language = IRelationship(lambda: GLanguage, foreign_keys=[language_id])

    status = IColumn(Status, name='status')

    e_status1 = IColumn(CharBool, nullable=False, name='e_status1')

    e_status2 = IColumn(CharBool, nullable=False, name='e_status2')

    e_status3 = IColumn(CharBool, nullable=False, name='e_status3')

    e_status4 = IColumn(CharBool, nullable=False, name='e_status4')
    __card_details = Header(u'card_details')

    cards = IRelationship(lambda: CCard, foreign_keys=lambda: [CCard.external_person_id], uselist=True)
    __key_details = Header(u'key_details')

    keys = IRelationship(lambda: CKey, foreign_keys=lambda: [CKey.external_person_id], uselist=True)
    __device_details = Header(u'device_details')

    devices = IRelationship(lambda: CDevicePerson, foreign_keys=lambda: [CDevicePerson.external_person_id], uselist=True)
    __external_employment = Header(u'external_employment')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_external_person_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    jr_start_date = IColumn(db.Date, name='jr_start_date')

    is_manager = IColumn(CharBool, nullable=False, name='is_manager')

    jobtitle = IColumn(db.VARCHAR(64), name='jobtitle')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_E_external_person_jobtitle_id'), name='jobtitle_id')
    _jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    jobfamily_id = IColumn(BigInt, db.ForeignKey('I_JOB_FAMILY.id', use_alter=True, name='fk_E_external_person_jobfamily_id'), name='jobfamily_id')
    jobfamily = IRelationship(lambda: IJobFamily, foreign_keys=[jobfamily_id])

    jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_E_external_person_jobrole_id'), name='jobrole_id')
    jobrole = IRelationship(lambda: IJobRole, foreign_keys=[jobrole_id])

    job_type = IColumn(JobType, name='job_type')

    exc_costcenter_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_E_external_person_exc_costcenter_id'), name='exc_costcenter_id')
    exc_costcenter = IRelationship(lambda: ICostCenter, foreign_keys=[exc_costcenter_id])

    exc_location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_E_external_person_exc_location_id'), name='exc_location_id')
    exc_location = IRelationship(lambda: ILocation, foreign_keys=[exc_location_id])

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_external_person_manager_id'), name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    manager_name = IColumn(db.VARCHAR(64), name='manager_name')

    manager_email = IColumn(db.VARCHAR(64), name='manager_email')

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_external_person_subst_manager_id'), name='subst_manager_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id])

    subst_manager_name = IColumn(db.VARCHAR(64), name='subst_manager_name')

    subst_manager_email = IColumn(db.VARCHAR(64), name='subst_manager_email')

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')
    __job_periods = Header(u'job_periods')

    job_periods = IRelationship(lambda: EJobPeriod, foreign_keys=lambda: [EJobPeriod.external_person_id], uselist=True)
    manager_in_external_job_periods = IRelationship(lambda: EJobPeriod, foreign_keys=lambda: [EJobPeriod.ext_manager_id], uselist=True)
    __home_address = Header(u'home_address')

    remote_office = IColumn(CharBool, nullable=False, name='remote_office')

    location_info = IColumn(db.VARCHAR(64), name='location_info')

    home_street = IColumn(db.VARCHAR(64), name='home_street')

    home_street2 = IColumn(db.VARCHAR(64), name='home_street2')

    home_post = IColumn(db.VARCHAR(64), name='home_post')

    home_city = IColumn(db.VARCHAR(64), name='home_city')

    home_state = IColumn(db.VARCHAR(64), name='home_state')

    homecountry_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_E_external_person_homecountry_id'), name='homecountry_id')
    homecountry = IRelationship(lambda: GCountry, foreign_keys=[homecountry_id])

    home_emergency_contact = IColumn(db.VARCHAR(64), name='home_emergency_contact')

    home_timezone = IColumn(db.VARCHAR(10), name='home_timezone')
    __hr_info = Header(u'hr_info')

    identity_checked = IColumn(CharBool, nullable=False, name='identity_checked')

    identitysource_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY_SOURCE.id', use_alter=True, name='fk_E_external_person_identitysource_id'), name='identitysource_id')
    identitysource = IRelationship(lambda: GIdentitySource, foreign_keys=[identitysource_id])

    personal_id = IColumn(db.VARCHAR(64), name='personal_id')

    staff_oper_code = IColumn(StaffOperCode, name='staff_oper_code')

    full_time = IColumn(CharBool, nullable=False, name='full_time')

    birth_date = IColumn(db.Date, name='birth_date')

    gender = IColumn(Gender, name='gender')

    nationality_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_E_external_person_nationality_id'), name='nationality_id')
    nationality = IRelationship(lambda: GCountry, foreign_keys=[nationality_id])

    mdm_source_id = IColumn(BigInt, db.ForeignKey('G_MDM_SOURCE.id', use_alter=True, name='fk_E_external_person_mdm_source_id'), name='mdm_source_id')
    mdm_source = IRelationship(lambda: GMdmSource, foreign_keys=[mdm_source_id])

    mdm_person_id = IColumn(db.VARCHAR(64), name='mdm_person_id')

    flag1 = IColumn(CharBool, nullable=False, name='flag1')

    flag2 = IColumn(CharBool, nullable=False, name='flag2')

    flag3 = IColumn(CharBool, nullable=False, name='flag3')

    flag4 = IColumn(CharBool, nullable=False, name='flag4')

    flag5 = IColumn(CharBool, nullable=False, name='flag5')

    original_source = IColumn(OriginalSource, name='original_source')
    __sync_info = Header(u'sync_info')

    attribute1 = IColumn(db.VARCHAR(64), name='attribute1')

    attribute2 = IColumn(db.VARCHAR(64), name='attribute2')

    attribute3 = IColumn(db.VARCHAR(64), name='attribute3')

    attribute4 = IColumn(db.VARCHAR(64), name='attribute4')

    attribute5 = IColumn(db.VARCHAR(64), name='attribute5')

    last_checking_date = IColumn(db.Date, name='last_checking_date')

    last_import_date = IColumn(db.Date, name='last_import_date')
    __absent_periods = Header(u'absent_periods')

    absence_status = IColumn(AbsenceStatus, name='absence_status')
    absences = IRelationship(lambda: DAbsence, foreign_keys=lambda: [DAbsence.external_person_id], uselist=True)
    __exceptions = Header(u'exceptions')

    exc_businessarea_id = IColumn(BigInt, db.ForeignKey('O_I_BUSINESS_AREA.id', use_alter=True, name='fk_E_external_person_exc_businessarea_id'), name='exc_businessarea_id')
    exc_businessarea = IRelationship(lambda: IBusinessArea, foreign_keys=[exc_businessarea_id])

    exc_legalcompany_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_E_external_person_exc_legalcompany_id'), name='exc_legalcompany_id')
    exc_legalcompany = IRelationship(lambda: ILegalCompany, foreign_keys=[exc_legalcompany_id])

    exc_country_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_E_external_person_exc_country_id'), name='exc_country_id')
    exc_country = IRelationship(lambda: GCountry, foreign_keys=[exc_country_id])
    __approvals = Header(u'approvals')

    waiting_manager_approval = IColumn(CharBool, nullable=False, name='waiting_manager_approval')

    manager_approved_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_external_person_manager_approved_id'), name='manager_approved_id')
    manager_approved = IRelationship(lambda: Zuser, foreign_keys=[manager_approved_id])

    manager_approval_timestamp = IColumn(db.DateTime, name='manager_approval_timestamp')

    first_email_sent_timestamp = IColumn(db.DateTime, name='first_email_sent_timestamp')
    __user_accounts = Header(u'user_accounts')

    user_accounts = IRelationship(lambda: GPersonUseraccount, foreign_keys=lambda: [GPersonUseraccount.external_person_id], uselist=True)
    education = IRelationship(lambda: DEducation, secondary=lambda: EPersonDEducation, uselist=True)
    competences = IRelationship(lambda: DCompetence, secondary=lambda: EPersonDCompetence, uselist=True)

    def to_named_tuple(self):
        return EExternalPersonTuple(id=self.id,name_prefix=self.name_prefix,first_name=self.first_name,middle_name=self.middle_name,last_name=self.last_name,preferred_name=self.preferred_name,identity_id=self.identity_id,social_security_number=self.social_security_number,personnel_number=self.personnel_number,information_checked=self.information_checked,student=self.student,email_active=self.email_active,photo=self.photo,username=self.username,orig_orgunit_id=self.orig_orgunit_id,ext_org_id=self.ext_org_id,e_job_role_id=self.e_job_role_id,contract_id=self.contract_id,tax_number=self.tax_number,org_email=self.org_email,b_phone=self.b_phone,b_mobile=self.b_mobile,pupo=self.pupo,sv_number=self.sv_number,other_address=self.other_address,ext_email=self.ext_email,ext_superior=self.ext_superior,ext_superior_email=self.ext_superior_email,starting_date=self.starting_date,termination_date=self.termination_date,termination_type=self.termination_type,recertification_date=self.recertification_date,ext_phone=self.ext_phone,language_id=self.language_id,status=self.status,e_status1=self.e_status1,e_status2=self.e_status2,e_status3=self.e_status3,e_status4=self.e_status4,orgunit_id=self.orgunit_id,jr_start_date=self.jr_start_date,is_manager=self.is_manager,jobtitle=self.jobtitle,jobtitle_id=self.jobtitle_id,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,exc_costcenter_id=self.exc_costcenter_id,exc_location_id=self.exc_location_id,manager_id=self.manager_id,manager_name=self.manager_name,manager_email=self.manager_email,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,remote_office=self.remote_office,location_info=self.location_info,home_street=self.home_street,home_street2=self.home_street2,home_post=self.home_post,home_city=self.home_city,home_state=self.home_state,homecountry_id=self.homecountry_id,home_emergency_contact=self.home_emergency_contact,home_timezone=self.home_timezone,identity_checked=self.identity_checked,identitysource_id=self.identitysource_id,personal_id=self.personal_id,staff_oper_code=self.staff_oper_code,full_time=self.full_time,birth_date=self.birth_date,gender=self.gender,nationality_id=self.nationality_id,mdm_source_id=self.mdm_source_id,mdm_person_id=self.mdm_person_id,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,attribute1=self.attribute1,attribute2=self.attribute2,attribute3=self.attribute3,attribute4=self.attribute4,attribute5=self.attribute5,last_checking_date=self.last_checking_date,last_import_date=self.last_import_date,absence_status=self.absence_status,exc_businessarea_id=self.exc_businessarea_id,exc_legalcompany_id=self.exc_legalcompany_id,exc_country_id=self.exc_country_id,waiting_manager_approval=self.waiting_manager_approval,manager_approved_id=self.manager_approved_id,manager_approval_timestamp=self.manager_approval_timestamp,first_email_sent_timestamp=self.first_email_sent_timestamp,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EExternalPersonTuple(id=self.id,name_prefix=self.name_prefix,first_name=self.first_name,middle_name=self.middle_name,last_name=self.last_name,preferred_name=self.preferred_name,identity_id=self.identity_id,social_security_number=self.social_security_number,personnel_number=self.personnel_number,information_checked=self.information_checked,student=self.student,email_active=self.email_active,photo=self.photo,username=self.username,orig_orgunit_id=self.orig_orgunit_id,ext_org_id=self.ext_org_id,e_job_role_id=self.e_job_role_id,contract_id=self.contract_id,tax_number=self.tax_number,org_email=self.org_email,b_phone=self.b_phone,b_mobile=self.b_mobile,pupo=self.pupo,sv_number=self.sv_number,other_address=self.other_address,ext_email=self.ext_email,ext_superior=self.ext_superior,ext_superior_email=self.ext_superior_email,starting_date=self.starting_date,termination_date=self.termination_date,termination_type=self.termination_type,recertification_date=self.recertification_date,ext_phone=self.ext_phone,language_id=self.language_id,status=self.status,e_status1=self.e_status1,e_status2=self.e_status2,e_status3=self.e_status3,e_status4=self.e_status4,orgunit_id=self.orgunit_id,jr_start_date=self.jr_start_date,is_manager=self.is_manager,jobtitle=self.jobtitle,jobtitle_id=self.jobtitle_id,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,exc_costcenter_id=self.exc_costcenter_id,exc_location_id=self.exc_location_id,manager_id=self.manager_id,manager_name=self.manager_name,manager_email=self.manager_email,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,remote_office=self.remote_office,location_info=self.location_info,home_street=self.home_street,home_street2=self.home_street2,home_post=self.home_post,home_city=self.home_city,home_state=self.home_state,homecountry_id=self.homecountry_id,home_emergency_contact=self.home_emergency_contact,home_timezone=self.home_timezone,identity_checked=self.identity_checked,identitysource_id=self.identitysource_id,personal_id=self.personal_id,staff_oper_code=self.staff_oper_code,full_time=self.full_time,birth_date=self.birth_date,gender=self.gender,nationality_id=self.nationality_id,mdm_source_id=self.mdm_source_id,mdm_person_id=self.mdm_person_id,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,attribute1=self.attribute1,attribute2=self.attribute2,attribute3=self.attribute3,attribute4=self.attribute4,attribute5=self.attribute5,last_checking_date=self.last_checking_date,last_import_date=self.last_import_date,absence_status=self.absence_status,exc_businessarea_id=self.exc_businessarea_id,exc_legalcompany_id=self.exc_legalcompany_id,exc_country_id=self.exc_country_id,waiting_manager_approval=self.waiting_manager_approval,manager_approved_id=self.manager_approved_id,manager_approval_timestamp=self.manager_approval_timestamp,first_email_sent_timestamp=self.first_email_sent_timestamp,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EJobFamilyTuple = namedtuple('EJobFamilyTuple',  ('id', 'name', 'int_code', 'description', 'starting_date', 'termination_date', 'jobfamily_class1', 'jobfamily_class2', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EJobFamily(API,EJobFamilyMixin, Base, db.Model):
    __tablename__ = 'E_JOB_FAMILY'
    __entity_name__ = 'E_job_family'
    __plain_object__ = EJobFamilyPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    int_code = IColumn(db.VARCHAR(32), name='int_code')

    description = IColumn(db.TEXT, name='description')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    jobfamily_class1 = IColumn(db.VARCHAR(64), name='jobfamily_class1')

    jobfamily_class2 = IColumn(db.VARCHAR(64), name='jobfamily_class2')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return EJobFamilyTuple(id=self.id,name=self.name,int_code=self.int_code,description=self.description,starting_date=self.starting_date,termination_date=self.termination_date,jobfamily_class1=self.jobfamily_class1,jobfamily_class2=self.jobfamily_class2,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EJobFamilyTuple(id=self.id,name=self.name,int_code=self.int_code,description=self.description,starting_date=self.starting_date,termination_date=self.termination_date,jobfamily_class1=self.jobfamily_class1,jobfamily_class2=self.jobfamily_class2,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EJobPeriodTuple = namedtuple('EJobPeriodTuple',  ('id', 'external_person_id', 'starting_date', 'termination_date', 'renewal_date', 'job_period_type', 'is_manager', 'student', 'outsider', 'orgunit_id', 'ext_org_id', 'job_title', 'other_job_title', 'specific_job_title', 'jobtitle_id', 'jobfamily_id', 'jobrole_id', 'job_type', 'organization_association_type', 'status', 'ext_manager_id', 'manager_id', 'manager_email', 'manager_name', 'subst_manager_id', 'subst_manager_name', 'subst_manager_email', 'substitute_active', 'report_manager_id', 'org_unit_manager_id', 'information_checked', 'contract', 'medicine_right', 'hr_job_type', 'c_pasu', 'full_part_per', 'hr_work_time_type', 'operative_staff', 'int_period_id', 'int_job_title', 'int_job_code', 'int_job_code2', 'hr_profession_code', 'hr_period_character_code', 'flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'original_source', 'pupo', 'phone', 'card_valid_from', 'card_valid_to', 'can_get_credentials', 'absence_active', 'exc_username', 'exc_legalcompany_id', 'exc_costcenter_id', 'exc_location_id', 'exc_country_id', 'exc_primary_period', 'inferred_primary_job_period', 'externally_managed', 'exported_to_idm', 'created_by_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EJobPeriod(API,EJobPeriodMixin, Base, db.Model):
    __tablename__ = 'E_JOB_PERIOD'
    __entity_name__ = 'E_job_period'
    __plain_object__ = EJobPeriodPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_job_period_external_person_id'), nullable=False, name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    starting_date = IColumn(db.Date, nullable=False, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    renewal_date = IColumn(db.Date, name='renewal_date')

    job_period_type = IColumn(JPType, name='jp_type')

    is_manager = IColumn(CharBool, nullable=False, name='is_manager')

    student = IColumn(CharBool, nullable=False, name='student')

    outsider = IColumn(CharBool, nullable=False, name='outsider')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_job_period_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    ext_org_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_ext_org_id'), nullable=False, name='ext_org_id')
    ext_org = IRelationship(lambda: EExtOrg, foreign_keys=[ext_org_id])

    job_title = IColumn(db.VARCHAR(64), name='job_title')

    other_job_title = IColumn(db.VARCHAR(64), name='other_job_title')

    specific_job_title = IColumn(db.VARCHAR(64), name='specific_job_title')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_E_job_period_jobtitle_id'), nullable=False, name='jobtitle_id')
    jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    jobfamily_id = IColumn(BigInt, db.ForeignKey('E_JOB_FAMILY.id', use_alter=True, name='fk_E_job_period_jobfamily_id'), name='jobfamily_id')
    jobfamily = IRelationship(lambda: EJobFamily, foreign_keys=[jobfamily_id])

    jobrole_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jobrole_id'), name='jobrole_id')
    jobrole = IRelationship(lambda: EJobRole, foreign_keys=[jobrole_id])

    job_type = IColumn(JobType, name='job_type')

    organization_association_type = IColumn(OrgAssociationType, name='org_association_type')

    status = IColumn(Status, name='status')

    ext_manager_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_job_period_ext_manager_id'), name='ext_manager_id')
    ext_manager = IRelationship(lambda: EExternalPerson, foreign_keys=[ext_manager_id])

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_job_period_manager_id'), name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    manager_email = IColumn(db.VARCHAR(64), name='manager_email')

    manager_name = IColumn(db.VARCHAR(64), name='manager_name')

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_job_period_subst_manager_id'), name='subst_manager_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id])

    subst_manager_name = IColumn(db.VARCHAR(64), name='subst_manager_name')

    subst_manager_email = IColumn(db.VARCHAR(64), name='subst_manager_email')

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')

    report_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_job_period_report_manager_id'), name='report_manager_id')
    report_manager = IRelationship(lambda: DPerson, foreign_keys=[report_manager_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_E_job_period_org_unit_manager_id'), name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    information_checked = IColumn(CharBool, nullable=False, name='information_checked')

    contract = IColumn(db.VARCHAR(64), name='contract')

    medicine_right = IColumn(MedicineRight, name='medicine_right')
    __hr_info = Header(u'hr_info')

    hr_job_type = IColumn(HRJobType, name='hr_job_type')

    c_pasu = IColumn(CharBool, nullable=False, name='c_pasu')

    full_part_per = IColumn(db.Float, name='full_part_per')

    hr_work_time_type = IColumn(HRWorkTimeType, name='hr_work_time_type')

    operative_staff = IColumn(CharBool, nullable=False, name='operative_staff')

    int_period_id = IColumn(db.VARCHAR(64), name='int_period_id')

    int_job_title = IColumn(db.VARCHAR(64), name='int_job_title')

    int_job_code = IColumn(db.VARCHAR(64), name='int_job_code')

    int_job_code2 = IColumn(db.VARCHAR(64), name='int_job_code2')

    hr_profession_code = IColumn(HRProfessionCode, name='hr_profession_code')

    hr_period_character_code = IColumn(JpCharacter, name='hr_period_character_code')

    flag1 = IColumn(CharBool, nullable=False, name='flag1')

    flag2 = IColumn(CharBool, nullable=False, name='flag2')

    flag3 = IColumn(CharBool, nullable=False, name='flag3')

    flag4 = IColumn(CharBool, nullable=False, name='flag4')

    flag5 = IColumn(CharBool, nullable=False, name='flag5')

    original_source = IColumn(OriginalSource, name='original_source')

    pupo = IColumn(db.VARCHAR(4), name='pupo')

    phone = IColumn(db.VARCHAR(40), name='phone')

    card_valid_from = IColumn(db.Date, name='card_valid_from')

    card_valid_to = IColumn(db.Date, name='card_valid_to')

    can_get_credentials = IColumn(CharBool, nullable=False, name='can_get_credentials')
    __absent_periods = Header(u'absent_periods')

    absence_active = IColumn(CharBool, nullable=False, name='absence_active')
    absences = IRelationship(lambda: EJobPeriodAbsence, foreign_keys=lambda: [EJobPeriodAbsence.e_job_period_id], uselist=True)
    __permissions = Header(u'permissions')

    requested_permissions = IRelationship(lambda: GPermission, foreign_keys=lambda: [GPermission.e_job_period_id], uselist=True)
    __exceptions = Header(u'exceptions')

    exc_username = IColumn(db.VARCHAR(64), name='exc_username')

    exc_legalcompany_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_E_job_period_exc_legalcompany_id'), name='exc_legalcompany_id')
    exc_legalcompany = IRelationship(lambda: ILegalCompany, foreign_keys=[exc_legalcompany_id])

    exc_costcenter_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_E_job_period_exc_costcenter_id'), name='exc_costcenter_id')
    exc_costcenter = IRelationship(lambda: ICostCenter, foreign_keys=[exc_costcenter_id])

    exc_location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_E_job_period_exc_location_id'), name='exc_location_id')
    exc_location = IRelationship(lambda: ILocation, foreign_keys=[exc_location_id])

    exc_country_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_E_job_period_exc_country_id'), name='exc_country_id')
    exc_country = IRelationship(lambda: GCountry, foreign_keys=[exc_country_id])

    exc_primary_period = IColumn(CharBool, nullable=False, name='exc_primary_period')
    organization_units = IRelationship(lambda: IOrgUnit, secondary=lambda: EJobPeriodIOrgUnit, uselist=True)
    __stuff = Header(u'stuff')

    inferred_primary_job_period = IColumn(CharBool, nullable=False, name='inferred_primary_job_period')

    externally_managed = IColumn(CharBool, nullable=False, name='externally_managed')

    exported_to_idm = IColumn(CharBool, nullable=False, name='exported_to_idm')

    created_by_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_job_period_created_by_id'), name='created_by_id')
    created_by = IRelationship(lambda: Zuser, foreign_keys=[created_by_id])

    def to_named_tuple(self):
        return EJobPeriodTuple(id=self.id,external_person_id=self.external_person_id,starting_date=self.starting_date,termination_date=self.termination_date,renewal_date=self.renewal_date,job_period_type=self.job_period_type,is_manager=self.is_manager,student=self.student,outsider=self.outsider,orgunit_id=self.orgunit_id,ext_org_id=self.ext_org_id,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,jobtitle_id=self.jobtitle_id,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,organization_association_type=self.organization_association_type,status=self.status,ext_manager_id=self.ext_manager_id,manager_id=self.manager_id,manager_email=self.manager_email,manager_name=self.manager_name,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,report_manager_id=self.report_manager_id,org_unit_manager_id=self.org_unit_manager_id,information_checked=self.information_checked,contract=self.contract,medicine_right=self.medicine_right,hr_job_type=self.hr_job_type,c_pasu=self.c_pasu,full_part_per=self.full_part_per,hr_work_time_type=self.hr_work_time_type,operative_staff=self.operative_staff,int_period_id=self.int_period_id,int_job_title=self.int_job_title,int_job_code=self.int_job_code,int_job_code2=self.int_job_code2,hr_profession_code=self.hr_profession_code,hr_period_character_code=self.hr_period_character_code,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,pupo=self.pupo,phone=self.phone,card_valid_from=self.card_valid_from,card_valid_to=self.card_valid_to,can_get_credentials=self.can_get_credentials,absence_active=self.absence_active,exc_username=self.exc_username,exc_legalcompany_id=self.exc_legalcompany_id,exc_costcenter_id=self.exc_costcenter_id,exc_location_id=self.exc_location_id,exc_country_id=self.exc_country_id,exc_primary_period=self.exc_primary_period,inferred_primary_job_period=self.inferred_primary_job_period,externally_managed=self.externally_managed,exported_to_idm=self.exported_to_idm,created_by_id=self.created_by_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EJobPeriodTuple(id=self.id,external_person_id=self.external_person_id,starting_date=self.starting_date,termination_date=self.termination_date,renewal_date=self.renewal_date,job_period_type=self.job_period_type,is_manager=self.is_manager,student=self.student,outsider=self.outsider,orgunit_id=self.orgunit_id,ext_org_id=self.ext_org_id,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,jobtitle_id=self.jobtitle_id,jobfamily_id=self.jobfamily_id,jobrole_id=self.jobrole_id,job_type=self.job_type,organization_association_type=self.organization_association_type,status=self.status,ext_manager_id=self.ext_manager_id,manager_id=self.manager_id,manager_email=self.manager_email,manager_name=self.manager_name,subst_manager_id=self.subst_manager_id,subst_manager_name=self.subst_manager_name,subst_manager_email=self.subst_manager_email,substitute_active=self.substitute_active,report_manager_id=self.report_manager_id,org_unit_manager_id=self.org_unit_manager_id,information_checked=self.information_checked,contract=self.contract,medicine_right=self.medicine_right,hr_job_type=self.hr_job_type,c_pasu=self.c_pasu,full_part_per=self.full_part_per,hr_work_time_type=self.hr_work_time_type,operative_staff=self.operative_staff,int_period_id=self.int_period_id,int_job_title=self.int_job_title,int_job_code=self.int_job_code,int_job_code2=self.int_job_code2,hr_profession_code=self.hr_profession_code,hr_period_character_code=self.hr_period_character_code,flag1=self.flag1,flag2=self.flag2,flag3=self.flag3,flag4=self.flag4,flag5=self.flag5,original_source=self.original_source,pupo=self.pupo,phone=self.phone,card_valid_from=self.card_valid_from,card_valid_to=self.card_valid_to,can_get_credentials=self.can_get_credentials,absence_active=self.absence_active,exc_username=self.exc_username,exc_legalcompany_id=self.exc_legalcompany_id,exc_costcenter_id=self.exc_costcenter_id,exc_location_id=self.exc_location_id,exc_country_id=self.exc_country_id,exc_primary_period=self.exc_primary_period,inferred_primary_job_period=self.inferred_primary_job_period,externally_managed=self.externally_managed,exported_to_idm=self.exported_to_idm,created_by_id=self.created_by_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EJobPeriodAbsenceTuple = namedtuple('EJobPeriodAbsenceTuple',  ('e_job_period_id', 'valid_from', 'created_by', 'start_date', 'end_date', 'description'  ))

class EJobPeriodAbsence(API,EJobPeriodAbsenceMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ABSENCE'
    __entity_name__ = 'E_job_period_absence'
    __plain_object__ = EJobPeriodAbsencePlain
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_absence_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_absence_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    created_by = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_job_period_absence_created_by'), nullable=False, name='created_by')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    description = IColumn(db.VARCHAR(256), name='description')

    def to_named_tuple(self):
        return EJobPeriodAbsenceTuple(e_job_period_id=self.e_job_period_id,valid_from=self.valid_from,created_by=self.created_by,start_date=self.start_date,end_date=self.end_date,description=self.description,)

    def to_plain_object(self):
        return EJobPeriodAbsenceTuple(e_job_period_id=self.e_job_period_id,valid_from=self.valid_from,created_by=self.created_by,start_date=self.start_date,end_date=self.end_date,description=self.description,)

EJobPeriodAttrPermissionLogTuple = namedtuple('EJobPeriodAttrPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'r_dyn_role_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodAttrPermissionLog(EJobPeriodAttrPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ATTR_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_attr_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_attr_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_attr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    r_dyn_role_id = IColumn(BigInt, db.ForeignKey('O_R_DYN_ROLE.id', use_alter=True, name='fk_E_job_period_attr_permission_log_r_dyn_role_id'), primary_key=True, name='r_dyn_role_id')
    r_dyn_role = IRelationship(lambda: RDynRole, foreign_keys=[r_dyn_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_attr_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_attr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    r_dyn_role_id = IColumn(BigInt, db.ForeignKey('O_R_DYN_ROLE.id', use_alter=True, name='fk_E_job_period_attr_permission_log_r_dyn_role_id'), primary_key=True, name='r_dyn_role_id')
    r_dyn_role = IRelationship(lambda: RDynRole, foreign_keys=[r_dyn_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodAttrPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodAttrPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodAttrPermissionStateTuple = namedtuple('EJobPeriodAttrPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'r_dyn_role_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodAttrPermissionState(EJobPeriodAttrPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ATTR_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_attr_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    r_dyn_role_id = IColumn(BigInt, primary_key=True, name='r_dyn_role_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    r_dyn_role_id = IColumn(BigInt, primary_key=True, name='r_dyn_role_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodAttrPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodAttrPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,r_dyn_role_id=self.r_dyn_role_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodGPermissionLogTuple = namedtuple('EJobPeriodGPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'g_permission_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodGPermissionLog(EJobPeriodGPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_G_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_g_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_g_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_g_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_E_job_period_g_permission_log_g_permission_id'), primary_key=True, name='g_permission_id')
    g_permission = IRelationship(lambda: GPermission, foreign_keys=[g_permission_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_g_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_g_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_E_job_period_g_permission_log_g_permission_id'), primary_key=True, name='g_permission_id')
    g_permission = IRelationship(lambda: GPermission, foreign_keys=[g_permission_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodGPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodGPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodGPermissionStateTuple = namedtuple('EJobPeriodGPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'g_permission_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodGPermissionState(EJobPeriodGPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_G_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_g_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_permission_id = IColumn(BigInt, primary_key=True, name='g_permission_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_permission_id = IColumn(BigInt, primary_key=True, name='g_permission_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodGPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodGPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodIouPermissionLogTuple = namedtuple('EJobPeriodIouPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodIouPermissionLog(EJobPeriodIouPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_IOU_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_iou_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_iou_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_iou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_job_period_iou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IOrgUnit, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_job_period_iou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IOrgUnit, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_iou_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_iou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_job_period_iou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: IOrgUnit, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_job_period_iou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: IOrgUnit, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodIouPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodIouPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodIouPermissionStateTuple = namedtuple('EJobPeriodIouPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodIouPermissionState(EJobPeriodIouPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_IOU_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_iou_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodIouPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodIouPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodJrOuPermissionLogTuple = namedtuple('EJobPeriodJrOuPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'e_job_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodJrOuPermissionLog(EJobPeriodJrOuPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_JR_OU_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_jr_ou_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    e_job_role_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_e_job_role_id'), primary_key=True, name='e_job_role_id')
    e_job_role = IRelationship(lambda: EJobRole, foreign_keys=[e_job_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EExtOrg, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EExtOrg, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    e_job_role_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_e_job_role_id'), primary_key=True, name='e_job_role_id')
    e_job_role = IRelationship(lambda: EJobRole, foreign_keys=[e_job_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EExtOrg, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_jr_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EExtOrg, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodJrOuPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,e_job_role_id=self.e_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodJrOuPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,e_job_role_id=self.e_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodJrOuPermissionStateTuple = namedtuple('EJobPeriodJrOuPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'e_job_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodJrOuPermissionState(EJobPeriodJrOuPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_JR_OU_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_jr_ou_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    e_job_role_id = IColumn(BigInt, primary_key=True, name='e_job_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    e_job_role_id = IColumn(BigInt, primary_key=True, name='e_job_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodJrOuPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,e_job_role_id=self.e_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodJrOuPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,e_job_role_id=self.e_job_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodJrPermissionLogTuple = namedtuple('EJobPeriodJrPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodJrPermissionLog(EJobPeriodJrPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_JR_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_jr_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_jr_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_jr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jr_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jr_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_jr_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_jr_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jr_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jr_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodJrPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodJrPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodJrPermissionStateTuple = namedtuple('EJobPeriodJrPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodJrPermissionState(EJobPeriodJrPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_JR_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_jr_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodJrPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodJrPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodJtPermissionLogTuple = namedtuple('EJobPeriodJtPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'd_jobtitle_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodJtPermissionLog(EJobPeriodJtPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_JT_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_jt_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_jt_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    d_jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_d_jobtitle_id'), primary_key=True, name='d_jobtitle_id')
    d_jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[d_jobtitle_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_jt_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    d_jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_d_jobtitle_id'), primary_key=True, name='d_jobtitle_id')
    d_jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[d_jobtitle_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EJobRole, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_jt_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EJobRole, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodJtPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodJtPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodJtPermissionStateTuple = namedtuple('EJobPeriodJtPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'd_jobtitle_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodJtPermissionState(EJobPeriodJtPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_JT_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_jt_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_jobtitle_id = IColumn(BigInt, primary_key=True, name='d_jobtitle_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    d_jobtitle_id = IColumn(BigInt, primary_key=True, name='d_jobtitle_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodJtPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodJtPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,d_jobtitle_id=self.d_jobtitle_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodManagerAssignmentQueueTuple = namedtuple('EJobPeriodManagerAssignmentQueueTuple',  ('id', 'job_period_id', 'org_unit_manager_id', 'valid_from', 'status'  ))

class EJobPeriodManagerAssignmentQueue(EJobPeriodManagerAssignmentQueueMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_MANAGER_ASSIGNMENT_QUEUE'
    __entity_name__ = 'E_job_period_manager_assignment_queue'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_manager_assignment_queue_job_period_id'), nullable=False, name='job_period_id')
    job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[job_period_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_E_job_period_manager_assignment_queue_org_unit_manager_id'), nullable=False, name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    valid_from = IColumn(db.DateTime, nullable=False, name='valid_from')

    status = IColumn(Status, nullable=False, name='status')

    def to_named_tuple(self):
        return EJobPeriodManagerAssignmentQueueTuple(id=self.id,job_period_id=self.job_period_id,org_unit_manager_id=self.org_unit_manager_id,valid_from=self.valid_from,status=self.status,)

    def to_plain_object(self):
        return EJobPeriodManagerAssignmentQueueTuple(id=self.id,job_period_id=self.job_period_id,org_unit_manager_id=self.org_unit_manager_id,valid_from=self.valid_from,status=self.status,)

EJobPeriodMergeLogTuple = namedtuple('EJobPeriodMergeLogTuple',  ('preserved', 'removed', 'created_by', 'valid_from'  ))

class EJobPeriodMergeLog(EJobPeriodMergeLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_MERGE_LOG'
    __entity_name__ = 'E_job_period_merge_log'
    __parent_entity__ = None

    preserved = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_merge_log_preserved'), primary_key=True, name='preserved')

    removed = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_merge_log_removed'), primary_key=True, name='removed')

    preserved = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_merge_log_preserved'), primary_key=True, name='preserved')

    removed = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_merge_log_removed'), primary_key=True, name='removed')

    created_by = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_job_period_merge_log_created_by'), nullable=False, name='created_by')

    valid_from = IColumn(db.DateTime, nullable=False, name='valid_from')

    def to_named_tuple(self):
        return EJobPeriodMergeLogTuple(preserved=self.preserved,removed=self.removed,created_by=self.created_by,valid_from=self.valid_from,)

    def to_plain_object(self):
        return EJobPeriodMergeLogTuple(preserved=self.preserved,removed=self.removed,created_by=self.created_by,valid_from=self.valid_from,)

EJobPeriodOrgGroupPermissionLogTuple = namedtuple('EJobPeriodOrgGroupPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'valid_from', 'e_job_role_id', 'i_org_group_id', 'start_date', 'end_date'  ))

class EJobPeriodOrgGroupPermissionLog(EJobPeriodOrgGroupPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ORG_GROUP_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_org_group_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_org_group_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_org_group_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_org_group_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_org_group_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_role_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_org_group_permission_log_e_job_role_id'), name='e_job_role_id')
    e_job_role = IRelationship(lambda: EJobRole, foreign_keys=[e_job_role_id])

    i_org_group_id = IColumn(BigInt, db.ForeignKey('I_ORG_GROUP.id', use_alter=True, name='fk_E_job_period_org_group_permission_log_i_org_group_id'), nullable=False, name='i_org_group_id')
    i_org_group = IRelationship(lambda: IOrgGroup, foreign_keys=[i_org_group_id])

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodOrgGroupPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodOrgGroupPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodOrgGroupPermissionStateTuple = namedtuple('EJobPeriodOrgGroupPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'valid_from', 'e_job_role_id', 'i_org_group_id', 'start_date', 'end_date'  ))

class EJobPeriodOrgGroupPermissionState(EJobPeriodOrgGroupPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ORG_GROUP_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_org_group_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    e_job_role_id = IColumn(BigInt, name='e_job_role_id')

    i_org_group_id = IColumn(BigInt, nullable=False, name='i_org_group_id')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodOrgGroupPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodOrgGroupPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,i_org_group_id=self.i_org_group_id,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodOrgSpecPermissionLogTuple = namedtuple('EJobPeriodOrgSpecPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'valid_from', 'e_job_role_id', 'org_spec', 'start_date', 'end_date'  ))

class EJobPeriodOrgSpecPermissionLog(EJobPeriodOrgSpecPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ORG_SPEC_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_org_spec_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_org_spec_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_org_spec_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_org_spec_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_org_spec_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_role_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_period_org_spec_permission_log_e_job_role_id'), name='e_job_role_id')
    e_job_role = IRelationship(lambda: EJobRole, foreign_keys=[e_job_role_id])

    org_spec = IColumn(OrgSpec, name='org_spec')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodOrgSpecPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodOrgSpecPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodOrgSpecPermissionStateTuple = namedtuple('EJobPeriodOrgSpecPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'valid_from', 'e_job_role_id', 'org_spec', 'start_date', 'end_date'  ))

class EJobPeriodOrgSpecPermissionState(EJobPeriodOrgSpecPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_ORG_SPEC_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_org_spec_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    e_job_role_id = IColumn(BigInt, name='e_job_role_id')

    org_spec = IColumn(db.Integer, name='org_spec')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodOrgSpecPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodOrgSpecPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,valid_from=self.valid_from,e_job_role_id=self.e_job_role_id,org_spec=self.org_spec,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodOuPermissionLogTuple = namedtuple('EJobPeriodOuPermissionLogTuple',  ('e_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodOuPermissionLog(EJobPeriodOuPermissionLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_OU_PERMISSION_LOG'
    __entity_name__ = 'E_job_period_ou_permission_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_ou_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EExtOrg, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EExtOrg, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_ou_permission_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_job_period_ou_permission_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    ancestor_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_ou_permission_log_ancestor_id'), primary_key=True, name='ancestor_id')
    ancestor = IRelationship(lambda: EExtOrg, foreign_keys=[ancestor_id])

    descendant_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_E_job_period_ou_permission_log_descendant_id'), primary_key=True, name='descendant_id')
    descendant = IRelationship(lambda: EExtOrg, foreign_keys=[descendant_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodOuPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodOuPermissionLogTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodOuPermissionStateTuple = namedtuple('EJobPeriodOuPermissionStateTuple',  ('e_job_period_id', 'g_service_role_id', 'ancestor_id', 'descendant_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodOuPermissionState(EJobPeriodOuPermissionStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_OU_PERMISSION_STATE'
    __entity_name__ = 'E_job_period_ou_permission_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    ancestor_id = IColumn(BigInt, primary_key=True, name='ancestor_id')

    descendant_id = IColumn(BigInt, primary_key=True, name='descendant_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodOuPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodOuPermissionStateTuple(e_job_period_id=self.e_job_period_id,g_service_role_id=self.g_service_role_id,ancestor_id=self.ancestor_id,descendant_id=self.descendant_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodSubstituteTuple = namedtuple('EJobPeriodSubstituteTuple',  ('id', 'e_job_period_id', 'e_substistute_person_id', 'start_date', 'end_date', 'is_backup', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EJobPeriodSubstitute(API,EJobPeriodSubstituteMixin, Base, db.Model):
    __tablename__ = 'E_JOB_PERIOD_SUBSTITUTE'
    __entity_name__ = 'E_job_period_substitute'
    __plain_object__ = EJobPeriodSubstitutePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_substitute_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    e_substistute_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_job_period_substitute_e_substistute_person_id'), name='e_substistute_person_id')
    e_substistute_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_substistute_person_id])

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    is_backup = IColumn(CharBool, nullable=False, name='is_backup')

    def to_named_tuple(self):
        return EJobPeriodSubstituteTuple(id=self.id,e_job_period_id=self.e_job_period_id,e_substistute_person_id=self.e_substistute_person_id,start_date=self.start_date,end_date=self.end_date,is_backup=self.is_backup,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EJobPeriodSubstituteTuple(id=self.id,e_job_period_id=self.e_job_period_id,e_substistute_person_id=self.e_substistute_person_id,start_date=self.start_date,end_date=self.end_date,is_backup=self.is_backup,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EJobPeriodSubstitutePermissionsTuple = namedtuple('EJobPeriodSubstitutePermissionsTuple',  ('id', 'e_job_period_substitute_id', 'e_job_period_id', 'status'  ))

class EJobPeriodSubstitutePermissions(EJobPeriodSubstitutePermissionsMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_SUBSTITUTE_PERMISSIONS'
    __entity_name__ = 'E_job_period_substitute_permissions'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    e_job_period_substitute_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD_SUBSTITUTE.id', use_alter=True, name='fk_E_job_period_sub_e_job_period_sub_3b42cd5c'), name='e_job_period_substitute_id')
    e_job_period_substitute = IRelationship(lambda: EJobPeriodSubstitute, foreign_keys=[e_job_period_substitute_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_substitute_permissions_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return EJobPeriodSubstitutePermissionsTuple(id=self.id,e_job_period_substitute_id=self.e_job_period_substitute_id,e_job_period_id=self.e_job_period_id,status=self.status,)

    def to_plain_object(self):
        return EJobPeriodSubstitutePermissionsTuple(id=self.id,e_job_period_substitute_id=self.e_job_period_substitute_id,e_job_period_id=self.e_job_period_id,status=self.status,)

EJobPeriodValidityLogTuple = namedtuple('EJobPeriodValidityLogTuple',  ('e_job_period_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodValidityLog(EJobPeriodValidityLogMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_VALIDITY_LOG'
    __entity_name__ = 'E_job_period_validity_log'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_validity_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_job_period_validity_log_e_job_period_id'), primary_key=True, name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodValidityLogTuple(e_job_period_id=self.e_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodValidityLogTuple(e_job_period_id=self.e_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobPeriodValidityStateTuple = namedtuple('EJobPeriodValidityStateTuple',  ('e_job_period_id', 'valid_from', 'start_date', 'end_date'  ))

class EJobPeriodValidityState(EJobPeriodValidityStateMixin, db.Model):
    __tablename__ = 'E_JOB_PERIOD_VALIDITY_STATE'
    __entity_name__ = 'E_job_period_validity_state'
    __parent_entity__ = None

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    e_job_period_id = IColumn(BigInt, primary_key=True, name='e_job_period_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return EJobPeriodValidityStateTuple(e_job_period_id=self.e_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return EJobPeriodValidityStateTuple(e_job_period_id=self.e_job_period_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

EJobRoleTuple = namedtuple('EJobRoleTuple',  ('id', 'name', 'int_code', 'description', 'global_jobrole', 'inheritance', 'orgunit_id', 'org_spec', 'upper_jobrole_id', 'starting_date', 'termination_date', 'provisioning', 'jobrole_class1', 'jobrole_class2', 'jobfamily_id', 'status', 'favorite', 'org_group_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EJobRole(API,ClosureTableMixin,EJobRoleMixin, Base, db.Model):
    __tablename__ = 'O_E_JOB_ROLE'
    __entity_name__ = 'E_job_role'
    __plain_object__ = EJobRolePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    int_code = IColumn(db.VARCHAR(32), name='int_code')

    description = IColumn(db.TEXT, name='description')

    global_jobrole = IColumn(CharBool, nullable=False, name='global_jobrole')

    inheritance = IColumn(CharBool, nullable=False, name='inheritance')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_E_job_role_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    org_spec = IColumn(OrgSpec, name='org_spec')

    upper_jobrole_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_role_upper_jobrole_id'), name='upper_jobrole_id')
    parent = IRelationship(lambda: EJobRole, foreign_keys=[upper_jobrole_id], remote_side=[id])

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    provisioning = IColumn(CharBool, nullable=False, name='provisioning')

    jobrole_class1 = IColumn(db.VARCHAR(64), name='jobrole_class1')

    jobrole_class2 = IColumn(db.VARCHAR(64), name='jobrole_class2')

    jobfamily_id = IColumn(BigInt, db.ForeignKey('E_JOB_FAMILY.id', use_alter=True, name='fk_E_job_role_jobfamily_id'), name='jobfamily_id')
    jobfamily = IRelationship(lambda: EJobFamily, foreign_keys=[jobfamily_id])

    status = IColumn(Status, name='status')

    favorite = IColumn(CharBool, nullable=False, name='favorite')

    org_group_id = IColumn(BigInt, db.ForeignKey('I_ORG_GROUP.id', use_alter=True, name='fk_E_job_role_org_group_id'), name='org_group_id')
    org_group = IRelationship(lambda: IOrgGroup, foreign_keys=[org_group_id])
    service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: EJobRoleGServiceRole, uselist=True)

    def to_named_tuple(self):
        return EJobRoleTuple(id=self.id,name=self.name,int_code=self.int_code,description=self.description,global_jobrole=self.global_jobrole,inheritance=self.inheritance,orgunit_id=self.orgunit_id,org_spec=self.org_spec,upper_jobrole_id=self.upper_jobrole_id,starting_date=self.starting_date,termination_date=self.termination_date,provisioning=self.provisioning,jobrole_class1=self.jobrole_class1,jobrole_class2=self.jobrole_class2,jobfamily_id=self.jobfamily_id,status=self.status,favorite=self.favorite,org_group_id=self.org_group_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EJobRoleTuple(id=self.id,name=self.name,int_code=self.int_code,description=self.description,global_jobrole=self.global_jobrole,inheritance=self.inheritance,orgunit_id=self.orgunit_id,org_spec=self.org_spec,upper_jobrole_id=self.upper_jobrole_id,starting_date=self.starting_date,termination_date=self.termination_date,provisioning=self.provisioning,jobrole_class1=self.jobrole_class1,jobrole_class2=self.jobrole_class2,jobfamily_id=self.jobfamily_id,status=self.status,favorite=self.favorite,org_group_id=self.org_group_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EJobRoleCtAllTuple = namedtuple('EJobRoleCtAllTuple',  ('ancestor', 'descendant'  ))

class EJobRoleCtAll(EJobRoleCtAllMixin, db.Model):
    __tablename__ = 'E_JOB_ROLE_CT_ALL'
    __entity_name__ = 'E_job_role_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_role_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_role_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_role_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_E_job_role_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return EJobRoleCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return EJobRoleCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

EOrgTypeServiceTuple = namedtuple('EOrgTypeServiceTuple',  ('id', 'ext_org_type_id', 'service_id', 'name', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class EOrgTypeService(API,EOrgTypeServiceMixin, Base, db.Model):
    __tablename__ = 'O_E_ORG_TYPE_SERVICE'
    __entity_name__ = 'E_org_type_service'
    __plain_object__ = EOrgTypeServicePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    ext_org_type_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG_TYPE.id', use_alter=True, name='fk_E_org_type_service_ext_org_type_id'), nullable=False, name='ext_org_type_id')
    ext_org_type = IRelationship(lambda: EExtOrgType, foreign_keys=[ext_org_type_id])

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_E_org_type_service_service_id'), nullable=False, name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return EOrgTypeServiceTuple(id=self.id,ext_org_type_id=self.ext_org_type_id,service_id=self.service_id,name=self.name,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return EOrgTypeServiceTuple(id=self.id,ext_org_type_id=self.ext_org_type_id,service_id=self.service_id,name=self.name,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

EPersonAbsenceEndedTuple = namedtuple('EPersonAbsenceEndedTuple',  ('e_person_id', 'end_date'  ))

class EPersonAbsenceEnded(EPersonAbsenceEndedMixin, db.Model):
    __tablename__ = 'E_PERSON_ABSENCE_ENDED'
    __entity_name__ = 'E_person_absence_ended'
    __parent_entity__ = None

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_absence_ended_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    end_date = IColumn(db.Date, primary_key=True, name='end_date')

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_absence_ended_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    end_date = IColumn(db.Date, primary_key=True, name='end_date')

    def to_named_tuple(self):
        return EPersonAbsenceEndedTuple(e_person_id=self.e_person_id,end_date=self.end_date,)

    def to_plain_object(self):
        return EPersonAbsenceEndedTuple(e_person_id=self.e_person_id,end_date=self.end_date,)

EPersonAbsenceStartedTuple = namedtuple('EPersonAbsenceStartedTuple',  ('e_person_id', 'start_date'  ))

class EPersonAbsenceStarted(EPersonAbsenceStartedMixin, db.Model):
    __tablename__ = 'E_PERSON_ABSENCE_STARTED'
    __entity_name__ = 'E_person_absence_started'
    __parent_entity__ = None

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_absence_started_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    start_date = IColumn(db.Date, primary_key=True, name='start_date')

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_absence_started_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    start_date = IColumn(db.Date, primary_key=True, name='start_date')

    def to_named_tuple(self):
        return EPersonAbsenceStartedTuple(e_person_id=self.e_person_id,start_date=self.start_date,)

    def to_plain_object(self):
        return EPersonAbsenceStartedTuple(e_person_id=self.e_person_id,start_date=self.start_date,)

EPersonPermissionManualProvisioningLogTuple = namedtuple('EPersonPermissionManualProvisioningLogTuple',  ('e_person_id', 'g_service_role_id', 'provisioned_at', 'g_service_id', 'status'  ))

class EPersonPermissionManualProvisioningLog(EPersonPermissionManualProvisioningLogMixin, db.Model):
    __tablename__ = 'E_PERSON_PERMISSION_MANUAL_PROVISIONING_LOG'
    __entity_name__ = 'E_person_permission_manual_provisioning_log'
    __parent_entity__ = None

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_permission_manual_provisioning_log_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_person_permiss_g_service_role_i_66f94de0'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_permission_manual_provisioning_log_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    g_service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_E_person_permission_manual_provisioning_log_g_service_id'), nullable=False, name='g_service_id')
    g_service = IRelationship(lambda: GService, foreign_keys=[g_service_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_person_permiss_g_service_role_i_66f94de0'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return EPersonPermissionManualProvisioningLogTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return EPersonPermissionManualProvisioningLogTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

EPersonPermissionManualProvisioningStateTuple = namedtuple('EPersonPermissionManualProvisioningStateTuple',  ('e_person_id', 'g_service_role_id', 'provisioned_at', 'g_service_id', 'status'  ))

class EPersonPermissionManualProvisioningState(EPersonPermissionManualProvisioningStateMixin, db.Model):
    __tablename__ = 'E_PERSON_PERMISSION_MANUAL_PROVISIONING_STATE'
    __entity_name__ = 'E_person_permission_manual_provisioning_state'
    __parent_entity__ = None

    e_person_id = IColumn(BigInt, primary_key=True, name='e_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    e_person_id = IColumn(BigInt, primary_key=True, name='e_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    provisioned_at = IColumn(db.DateTime, name='provisioned_at')

    g_service_id = IColumn(BigInt, nullable=False, name='g_service_id')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return EPersonPermissionManualProvisioningStateTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return EPersonPermissionManualProvisioningStateTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

EPersonPermissionProvisioningLogTuple = namedtuple('EPersonPermissionProvisioningLogTuple',  ('e_person_id', 'g_service_role_id', 'g_system_id', 'provisioned_at', 'g_service_id', 'status'  ))

class EPersonPermissionProvisioningLog(EPersonPermissionProvisioningLogMixin, db.Model):
    __tablename__ = 'E_PERSON_PERMISSION_PROVISIONING_LOG'
    __entity_name__ = 'E_person_permission_provisioning_log'
    __parent_entity__ = None

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_permission_provisioning_log_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_person_permission_provisioning_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_E_person_permission_provisioning_log_g_system_id'), primary_key=True, name='g_system_id')
    g_system = IRelationship(lambda: GSystem, foreign_keys=[g_system_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_person_permission_provisioning_log_e_person_id'), primary_key=True, name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    g_service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_E_person_permission_provisioning_log_g_service_id'), nullable=False, name='g_service_id')
    g_service = IRelationship(lambda: GService, foreign_keys=[g_service_id])

    g_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_person_permission_provisioning_log_g_service_role_id'), primary_key=True, name='g_service_role_id')
    g_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[g_service_role_id])

    g_system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_E_person_permission_provisioning_log_g_system_id'), primary_key=True, name='g_system_id')
    g_system = IRelationship(lambda: GSystem, foreign_keys=[g_system_id])

    provisioned_at = IColumn(db.DateTime, primary_key=True, name='provisioned_at')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return EPersonPermissionProvisioningLogTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return EPersonPermissionProvisioningLogTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

EPersonPermissionProvisioningStateTuple = namedtuple('EPersonPermissionProvisioningStateTuple',  ('e_person_id', 'g_service_role_id', 'g_system_id', 'provisioned_at', 'g_service_id', 'status'  ))

class EPersonPermissionProvisioningState(EPersonPermissionProvisioningStateMixin, db.Model):
    __tablename__ = 'E_PERSON_PERMISSION_PROVISIONING_STATE'
    __entity_name__ = 'E_person_permission_provisioning_state'
    __parent_entity__ = None

    e_person_id = IColumn(BigInt, primary_key=True, name='e_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_system_id = IColumn(BigInt, primary_key=True, name='g_system_id')

    e_person_id = IColumn(BigInt, primary_key=True, name='e_person_id')

    g_service_role_id = IColumn(BigInt, primary_key=True, name='g_service_role_id')

    g_system_id = IColumn(BigInt, primary_key=True, name='g_system_id')

    provisioned_at = IColumn(db.DateTime, name='provisioned_at')

    g_service_id = IColumn(BigInt, nullable=False, name='g_service_id')

    status = IColumn(db.SmallInteger, nullable=False, name='status')

    def to_named_tuple(self):
        return EPersonPermissionProvisioningStateTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

    def to_plain_object(self):
        return EPersonPermissionProvisioningStateTuple(e_person_id=self.e_person_id,g_service_role_id=self.g_service_role_id,g_system_id=self.g_system_id,provisioned_at=self.provisioned_at,g_service_id=self.g_service_id,status=self.status,)

ERequestCartTuple = namedtuple('ERequestCartTuple',  ('id', 'person_id', 'job_period_id', 'requestor_id', 'starting_date', 'manager_id', 'request_type', 'reason', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'approval_status', 'approval_comment', 'subst_approver_id', 'subst_approver_email', 'forced_hidden', 'approver_id', 'auto_approved', 'approval_time', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_address', 'reject_email_sent', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ERequestCart(API,ERequestCartMixin, Base, db.Model):
    __tablename__ = 'E_REQUEST_CART'
    __entity_name__ = 'E_request_cart'
    __plain_object__ = ERequestCartPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_request_cart_person_id'), nullable=False, name='person_id')
    person = IRelationship(lambda: EExternalPerson, foreign_keys=[person_id])

    job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_E_request_cart_job_period_id'), nullable=False, name='job_period_id')
    job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[job_period_id])

    requestor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_requestor_id'), nullable=False, name='requestor_id')
    requestor = IRelationship(lambda: Zuser, foreign_keys=[requestor_id])

    starting_date = IColumn(db.Date, nullable=False, name='starting_date')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_E_request_cart_manager_id'), nullable=False, name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    request_type = IColumn(RequestType, name='request_type')

    reason = IColumn(db.VARCHAR(256), name='reason')

    preferred_implementor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_preferred_implementor_id'), name='preferred_implementor_id')
    preferred_implementor = IRelationship(lambda: Zuser, foreign_keys=[preferred_implementor_id])

    inform_user = IColumn(CharBool, nullable=False, name='inform_user')

    inform_superior = IColumn(CharBool, nullable=False, name='inform_superior')

    inform_others = IColumn(CharBool, nullable=False, name='inform_others')
    __permissions = Header(u'permissions')

    permissions = IRelationship(lambda: ERequestCartPermission, foreign_keys=lambda: [ERequestCartPermission.request_cart_id], uselist=True)
    __approval_info = Header(u'approval_info')

    approval_status = IColumn(ApprovalStatus, nullable=False, name='approval_status')

    approval_comment = IColumn(db.VARCHAR(256), name='approval_comment')

    subst_approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_subst_approver_id'), name='subst_approver_id')
    subst_approver = IRelationship(lambda: Zuser, foreign_keys=[subst_approver_id])

    subst_approver_email = IColumn(db.VARCHAR(64), name='subst_approver_email')

    forced_hidden = IColumn(CharBool, nullable=False, name='forced_hidden')

    approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_approver_id'), name='approver_id')
    approver = IRelationship(lambda: Zuser, foreign_keys=[approver_id])

    auto_approved = IColumn(CharBool, nullable=False, name='auto_approved')

    approval_time = IColumn(db.DateTime, name='approval_time')
    __technical_info = Header(u'technical_info')

    first_email_sent = IColumn(db.DateTime, name='first_email_sent')

    last_email_sent = IColumn(db.DateTime, name='last_email_sent')

    email_counter = IColumn(db.Integer, name='email_counter')

    email_address = IColumn(db.VARCHAR(254), name='email_address')

    reject_email_sent = IColumn(db.DateTime, name='reject_email_sent')

    def to_named_tuple(self):
        return ERequestCartTuple(id=self.id,person_id=self.person_id,job_period_id=self.job_period_id,requestor_id=self.requestor_id,starting_date=self.starting_date,manager_id=self.manager_id,request_type=self.request_type,reason=self.reason,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,approval_status=self.approval_status,approval_comment=self.approval_comment,subst_approver_id=self.subst_approver_id,subst_approver_email=self.subst_approver_email,forced_hidden=self.forced_hidden,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_time=self.approval_time,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_address=self.email_address,reject_email_sent=self.reject_email_sent,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ERequestCartTuple(id=self.id,person_id=self.person_id,job_period_id=self.job_period_id,requestor_id=self.requestor_id,starting_date=self.starting_date,manager_id=self.manager_id,request_type=self.request_type,reason=self.reason,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,approval_status=self.approval_status,approval_comment=self.approval_comment,subst_approver_id=self.subst_approver_id,subst_approver_email=self.subst_approver_email,forced_hidden=self.forced_hidden,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_time=self.approval_time,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_address=self.email_address,reject_email_sent=self.reject_email_sent,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ERequestCartPermissionTuple = namedtuple('ERequestCartPermissionTuple',  ('id', 'request_cart_id', 'person_id', 'service_role_id', 'requestor_id', 'request_activation_date', 'permission_request_type', 'service_id', 'description', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'start_date', 'end_date', 'period_yr', 'approval_status', 'approver_id', 'auto_approved', 'approval_timestamp', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'email_to_service_manager_sent', 'email_to_requestor_sent', 'reject_email_sent', 'source_system_name', 'source_system_id', 'associated_orgunits_json', 'associated_ext_orgs_json', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ERequestCartPermission(API,ERequestCartPermissionMixin, Base, db.Model):
    __tablename__ = 'E_REQUEST_CART_PERMISSION'
    __entity_name__ = 'E_request_cart_permission'
    __plain_object__ = ERequestCartPermissionPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    request_cart_id = IColumn(BigInt, db.ForeignKey('E_REQUEST_CART.id', use_alter=True, name='fk_E_request_cart_permission_request_cart_id'), nullable=False, name='request_cart_id')
    request_cart = IRelationship(lambda: ERequestCart, foreign_keys=[request_cart_id])

    person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_E_request_cart_permission_person_id'), nullable=False, name='person_id')
    person = IRelationship(lambda: EExternalPerson, foreign_keys=[person_id])

    service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_E_request_cart_permission_service_role_id'), nullable=False, name='service_role_id')
    service_role = IRelationship(lambda: GServiceRole, foreign_keys=[service_role_id])

    requestor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_permission_requestor_id'), nullable=False, name='requestor_id')
    requestor = IRelationship(lambda: Zuser, foreign_keys=[requestor_id])

    request_activation_date = IColumn(db.DateTime, name='request_activation_date')

    permission_request_type = IColumn(PermissionRequestType, nullable=False, name='permission_request_type')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_E_request_cart_permission_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    description = IColumn(db.TEXT, name='description')

    preferred_implementor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_permission_preferred_implementor_id'), name='preferred_implementor_id')
    preferred_implementor = IRelationship(lambda: Zuser, foreign_keys=[preferred_implementor_id])

    inform_user = IColumn(CharBool, nullable=False, name='inform_user')

    inform_superior = IColumn(CharBool, nullable=False, name='inform_superior')

    inform_others = IColumn(CharBool, nullable=False, name='inform_others')

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    period_yr = IColumn(db.Integer, name='period_yr')
    __approvals = Header(u'approvals')

    approval_status = IColumn(ApprovalStatus, nullable=False, name='approval_status')

    approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_E_request_cart_permission_approver_id'), name='approver_id')
    approver = IRelationship(lambda: Zuser, foreign_keys=[approver_id])

    auto_approved = IColumn(CharBool, nullable=False, name='auto_approved')

    approval_timestamp = IColumn(db.DateTime, name='approval_timestamp')
    __technical_info = Header(u'technical_info')

    first_email_sent = IColumn(db.DateTime, name='first_email_sent')

    last_email_sent = IColumn(db.DateTime, name='last_email_sent')

    email_counter = IColumn(db.Integer, name='email_counter')

    email_to_user_sent = IColumn(db.Integer, name='email_to_user_sent')

    email_to_superior_sent = IColumn(db.Integer, name='email_to_superior_sent')

    email_to_others_sent = IColumn(db.Integer, name='email_to_others_sent')

    email_to_service_manager_sent = IColumn(db.Integer, name='email_to_service_manager_sent')

    email_to_requestor_sent = IColumn(db.Integer, name='email_to_requestor_sent')

    reject_email_sent = IColumn(db.DateTime, name='reject_email_sent')

    source_system_name = IColumn(db.VARCHAR(64), name='source_system_name')

    source_system_id = IColumn(db.VARCHAR(64), name='source_system_id')

    associated_orgunits_json = IColumn(db.TEXT, name='associated_orgunits_json')

    associated_ext_orgs_json = IColumn(db.TEXT, name='associated_ext_orgs_json')
    informed_persons = IRelationship(lambda: DPerson, secondary=lambda: ERequestCartPermissionDPerson, uselist=True)

    def to_named_tuple(self):
        return ERequestCartPermissionTuple(id=self.id,request_cart_id=self.request_cart_id,person_id=self.person_id,service_role_id=self.service_role_id,requestor_id=self.requestor_id,request_activation_date=self.request_activation_date,permission_request_type=self.permission_request_type,service_id=self.service_id,description=self.description,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,start_date=self.start_date,end_date=self.end_date,period_yr=self.period_yr,approval_status=self.approval_status,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_timestamp=self.approval_timestamp,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_to_user_sent=self.email_to_user_sent,email_to_superior_sent=self.email_to_superior_sent,email_to_others_sent=self.email_to_others_sent,email_to_service_manager_sent=self.email_to_service_manager_sent,email_to_requestor_sent=self.email_to_requestor_sent,reject_email_sent=self.reject_email_sent,source_system_name=self.source_system_name,source_system_id=self.source_system_id,associated_orgunits_json=self.associated_orgunits_json,associated_ext_orgs_json=self.associated_ext_orgs_json,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ERequestCartPermissionTuple(id=self.id,request_cart_id=self.request_cart_id,person_id=self.person_id,service_role_id=self.service_role_id,requestor_id=self.requestor_id,request_activation_date=self.request_activation_date,permission_request_type=self.permission_request_type,service_id=self.service_id,description=self.description,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,start_date=self.start_date,end_date=self.end_date,period_yr=self.period_yr,approval_status=self.approval_status,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_timestamp=self.approval_timestamp,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_to_user_sent=self.email_to_user_sent,email_to_superior_sent=self.email_to_superior_sent,email_to_others_sent=self.email_to_others_sent,email_to_service_manager_sent=self.email_to_service_manager_sent,email_to_requestor_sent=self.email_to_requestor_sent,reject_email_sent=self.reject_email_sent,source_system_name=self.source_system_name,source_system_id=self.source_system_id,associated_orgunits_json=self.associated_orgunits_json,associated_ext_orgs_json=self.associated_ext_orgs_json,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

FLangTuple = namedtuple('FLangTuple',  ('name', 'lang', 'text'  ))

class FLang(FLangMixin, db.Model):
    __tablename__ = 'F_LANG'
    __entity_name__ = 'F_lang'
    __parent_entity__ = None

    name = IColumn(db.VARCHAR(200), primary_key=True, name='name')

    lang = IColumn(db.VARCHAR(8), primary_key=True, name='lang')

    name = IColumn(db.VARCHAR(200), primary_key=True, name='name')

    text = IColumn(db.VARCHAR(512), nullable=False, name='text')

    lang = IColumn(db.VARCHAR(8), primary_key=True, name='lang')

    def to_named_tuple(self):
        return FLangTuple(name=self.name,lang=self.lang,text=self.text,)

    def to_plain_object(self):
        return FLangTuple(name=self.name,lang=self.lang,text=self.text,)

FSchemaTuple = namedtuple('FSchemaTuple',  ('table_name', 'column_name', 'referred_table'  ))

class FSchema(FSchemaMixin, db.Model):
    __tablename__ = 'F_SCHEMA'
    __entity_name__ = 'F_schema'
    __parent_entity__ = None

    table_name = IColumn(db.VARCHAR(64), primary_key=True, name='table_name')

    column_name = IColumn(db.VARCHAR(64), primary_key=True, name='column_name')

    table_name = IColumn(db.VARCHAR(64), primary_key=True, name='table_name')

    column_name = IColumn(db.VARCHAR(64), primary_key=True, name='column_name')

    referred_table = IColumn(db.VARCHAR(64), name='referred_table')

    def to_named_tuple(self):
        return FSchemaTuple(table_name=self.table_name,column_name=self.column_name,referred_table=self.referred_table,)

    def to_plain_object(self):
        return FSchemaTuple(table_name=self.table_name,column_name=self.column_name,referred_table=self.referred_table,)

FSchemaTableTuple = namedtuple('FSchemaTableTuple',  ('table_name', 'parent_table'  ))

class FSchemaTable(FSchemaTableMixin, db.Model):
    __tablename__ = 'F_SCHEMA_TABLE'
    __entity_name__ = 'F_schema_table'
    __parent_entity__ = None

    table_name = IColumn(db.VARCHAR(64), primary_key=True, name='table_name')

    table_name = IColumn(db.VARCHAR(64), primary_key=True, name='table_name')

    parent_table = IColumn(db.VARCHAR(64), name='parent_table')

    def to_named_tuple(self):
        return FSchemaTableTuple(table_name=self.table_name,parent_table=self.parent_table,)

    def to_plain_object(self):
        return FSchemaTableTuple(table_name=self.table_name,parent_table=self.parent_table,)

FSystemInfoTuple = namedtuple('FSystemInfoTuple',  ('name', 'value'  ))

class FSystemInfo(FSystemInfoMixin, db.Model):
    __tablename__ = 'F_SYSTEM_INFO'
    __entity_name__ = 'F_system_info'
    __parent_entity__ = None

    name = IColumn(db.VARCHAR(128), primary_key=True, name='name')

    name = IColumn(db.VARCHAR(128), primary_key=True, name='name')

    value = IColumn(db.TEXT, name='value')

    def to_named_tuple(self):
        return FSystemInfoTuple(name=self.name,value=self.value,)

    def to_plain_object(self):
        return FSystemInfoTuple(name=self.name,value=self.value,)

GAccountAttributeTuple = namedtuple('GAccountAttributeTuple',  ('id', 'person_useraccount_id', 'value', 'value_p_old', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GAccountAttribute(API,GAccountAttributeMixin, Base, db.Model):
    __tablename__ = 'G_ACCOUNT_ATTRIBUTE'
    __entity_name__ = 'G_account_attribute'
    __plain_object__ = GAccountAttributePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_useraccount_id = IColumn(BigInt, db.ForeignKey('G_PERSON_USERACCOUNT.id', use_alter=True, name='fk_G_account_attribute_person_useraccount_id'), name='person_useraccount_id')
    person_useraccount = IRelationship(lambda: GPersonUseraccount, foreign_keys=[person_useraccount_id])

    value = IColumn(db.VARCHAR(64), name='value')

    value_p_old = IColumn(db.VARCHAR(64), name='value_p_old')

    def to_named_tuple(self):
        return GAccountAttributeTuple(id=self.id,person_useraccount_id=self.person_useraccount_id,value=self.value,value_p_old=self.value_p_old,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GAccountAttributeTuple(id=self.id,person_useraccount_id=self.person_useraccount_id,value=self.value,value_p_old=self.value_p_old,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GAceTuple = namedtuple('GAceTuple',  ('id', 'name', 'description', 'ace_types', 'value', 'ace_key', 'ace_key_priority', 'attribute_source', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GAce(API,GAceMixin, Base, db.Model):
    __tablename__ = 'O_G_ACE'
    __entity_name__ = 'G_ace'
    __plain_object__ = GAcePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    ace_types = IColumn(ACETypes, nullable=False, name='ace_types')

    value = IColumn(db.TEXT, name='value')

    ace_key = IColumn(db.VARCHAR(64), name='ace_key')

    ace_key_priority = IColumn(CharBool, nullable=False, name='ace_key_priority')

    attribute_source = IColumn(BigInt, db.ForeignKey('O_G_ACE_ATTRIBUTE.id', use_alter=True, name='fk_G_ace_attribute_source'), name='attribute_source')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GAceTuple(id=self.id,name=self.name,description=self.description,ace_types=self.ace_types,value=self.value,ace_key=self.ace_key,ace_key_priority=self.ace_key_priority,attribute_source=self.attribute_source,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GAceTuple(id=self.id,name=self.name,description=self.description,ace_types=self.ace_types,value=self.value,ace_key=self.ace_key,ace_key_priority=self.ace_key_priority,attribute_source=self.attribute_source,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GAceAttributeTuple = namedtuple('GAceAttributeTuple',  ('id', 'name', 'description', 'source_entity', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GAceAttribute(API,GAceAttributeMixin, Base, db.Model):
    __tablename__ = 'O_G_ACE_ATTRIBUTE'
    __entity_name__ = 'G_ace_attribute'
    __plain_object__ = GAceAttributePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    source_entity = IColumn(db.TEXT, name='source_entity')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GAceAttributeTuple(id=self.id,name=self.name,description=self.description,source_entity=self.source_entity,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GAceAttributeTuple(id=self.id,name=self.name,description=self.description,source_entity=self.source_entity,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GCountryTuple = namedtuple('GCountryTuple',  ('id', 'code', 'name', 'region', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GCountry(API,GCountryMixin, Base, db.Model):
    __tablename__ = 'G_COUNTRY'
    __entity_name__ = 'G_country'
    __plain_object__ = GCountryPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(8), nullable=False, name='code')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    region = IColumn(BigInt, db.ForeignKey('G_REGION.id', use_alter=True, name='fk_G_country_region'), name='region')

    def to_named_tuple(self):
        return GCountryTuple(id=self.id,code=self.code,name=self.name,region=self.region,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GCountryTuple(id=self.id,code=self.code,name=self.name,region=self.region,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GEmailLogTuple = namedtuple('GEmailLogTuple',  ('id', 'email_template', 'email_to', 'email_from', 'subject', 'cache_location', 'email_log_id', 'resend_original_email_id', 'body', 'provisioning_task_id', 'person_id', 'external_person_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GEmailLog(GEmailLogMixin, Base, db.Model):
    __tablename__ = 'G_EMAIL_LOG'
    __entity_name__ = 'G_email_log'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    email_template = IColumn(db.VARCHAR(256), name='email_template')

    email_to = IColumn(db.VARCHAR(256), name='email_to')

    email_from = IColumn(db.VARCHAR(256), name='email_from')

    subject = IColumn(db.VARCHAR(512), name='subject')

    cache_location = IColumn(db.VARCHAR(512), name='cache_location')

    email_log_id = IColumn(db.VARCHAR(64), name='email_log_id')

    resend_original_email_id = IColumn(BigInt, db.ForeignKey('G_EMAIL_LOG.id', use_alter=True, name='fk_G_email_log_resend_original_email_id'), name='resend_original_email_id')
    resend_original_email = IRelationship(lambda: GEmailLog, foreign_keys=[resend_original_email_id], remote_side=[id])

    body = IColumn(db.TEXT, name='body')

    provisioning_task_id = IColumn(BigInt, db.ForeignKey('G_PROVISIONING_TASK.id', use_alter=True, name='fk_G_email_log_provisioning_task_id'), name='provisioning_task_id')
    provisioning_task = IRelationship(lambda: GProvisioningTask, foreign_keys=[provisioning_task_id])

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_G_email_log_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_G_email_log_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    def to_named_tuple(self):
        return GEmailLogTuple(id=self.id,email_template=self.email_template,email_to=self.email_to,email_from=self.email_from,subject=self.subject,cache_location=self.cache_location,email_log_id=self.email_log_id,resend_original_email_id=self.resend_original_email_id,body=self.body,provisioning_task_id=self.provisioning_task_id,person_id=self.person_id,external_person_id=self.external_person_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GEmailLogTuple(id=self.id,email_template=self.email_template,email_to=self.email_to,email_from=self.email_from,subject=self.subject,cache_location=self.cache_location,email_log_id=self.email_log_id,resend_original_email_id=self.resend_original_email_id,body=self.body,provisioning_task_id=self.provisioning_task_id,person_id=self.person_id,external_person_id=self.external_person_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GIdentityTuple = namedtuple('GIdentityTuple',  ('id', 'first_name', 'last_name', 'personal_id', 'id_validity', 'identitysource_id', 'identified_by', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GIdentity(API,GIdentityMixin, Base, db.Model):
    __tablename__ = 'G_IDENTITY'
    __entity_name__ = 'G_identity'
    __plain_object__ = GIdentityPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    first_name = IColumn(db.VARCHAR(64), nullable=False, name='first_name')

    last_name = IColumn(db.VARCHAR(64), nullable=False, name='last_name')

    personal_id = IColumn(db.VARCHAR(64), nullable=False, name='personal_id')

    id_validity = IColumn(db.Date, nullable=False, name='id_validity')

    identitysource_id = IColumn(BigInt, db.ForeignKey('G_IDENTITY_SOURCE.id', use_alter=True, name='fk_G_identity_identitysource_id'), nullable=False, name='identitysource_id')
    identitysource = IRelationship(lambda: GIdentitySource, foreign_keys=[identitysource_id])

    identified_by = IColumn(db.VARCHAR(64), name='identified_by')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GIdentityTuple(id=self.id,first_name=self.first_name,last_name=self.last_name,personal_id=self.personal_id,id_validity=self.id_validity,identitysource_id=self.identitysource_id,identified_by=self.identified_by,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GIdentityTuple(id=self.id,first_name=self.first_name,last_name=self.last_name,personal_id=self.personal_id,id_validity=self.id_validity,identitysource_id=self.identitysource_id,identified_by=self.identified_by,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GIdentitySourceTuple = namedtuple('GIdentitySourceTuple',  ('id', 'name', 'description', 'identitysourcetype', 'identitysourceclass', 'source_update', 'resp_name', 'resp_email', 'resp_phone', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GIdentitySource(API,GIdentitySourceMixin, Base, db.Model):
    __tablename__ = 'G_IDENTITY_SOURCE'
    __entity_name__ = 'G_identity_source'
    __plain_object__ = GIdentitySourcePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    description = IColumn(db.TEXT, name='description')

    identitysourcetype = IColumn(IdentitySourceType, nullable=False, name='identitysourcetype')

    identitysourceclass = IColumn(IdentitySourceClass, nullable=False, name='identitysourceclass')

    source_update = IColumn(SourceUpdate, nullable=False, name='source_update')

    resp_name = IColumn(db.VARCHAR(64), name='resp_name')

    resp_email = IColumn(db.VARCHAR(64), name='resp_email')

    resp_phone = IColumn(db.VARCHAR(64), name='resp_phone')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GIdentitySourceTuple(id=self.id,name=self.name,description=self.description,identitysourcetype=self.identitysourcetype,identitysourceclass=self.identitysourceclass,source_update=self.source_update,resp_name=self.resp_name,resp_email=self.resp_email,resp_phone=self.resp_phone,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GIdentitySourceTuple(id=self.id,name=self.name,description=self.description,identitysourcetype=self.identitysourcetype,identitysourceclass=self.identitysourceclass,source_update=self.source_update,resp_name=self.resp_name,resp_email=self.resp_email,resp_phone=self.resp_phone,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GLanguageTuple = namedtuple('GLanguageTuple',  ('id', 'code', 'name', 'iso_code', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GLanguage(API,GLanguageMixin, Base, db.Model):
    __tablename__ = 'G_LANGUAGE'
    __entity_name__ = 'G_language'
    __plain_object__ = GLanguagePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(8), nullable=False, name='code')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    iso_code = IColumn(db.VARCHAR(64), name='iso_code')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GLanguageTuple(id=self.id,code=self.code,name=self.name,iso_code=self.iso_code,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GLanguageTuple(id=self.id,code=self.code,name=self.name,iso_code=self.iso_code,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GMdmRuleTuple = namedtuple('GMdmRuleTuple',  ('id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GMdmRule(API,GMdmRuleMixin, Base, db.Model):
    __tablename__ = 'G_MDM_RULE'
    __entity_name__ = 'G_mdm_rule'
    __plain_object__ = GMdmRulePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    def to_named_tuple(self):
        return GMdmRuleTuple(id=self.id,name=self.name,description=self.description,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GMdmRuleTuple(id=self.id,name=self.name,description=self.description,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GMdmSourceTuple = namedtuple('GMdmSourceTuple',  ('id', 'name', 'description', 'source_type', 'source_class', 'update_cycle', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GMdmSource(API,GMdmSourceMixin, Base, db.Model):
    __tablename__ = 'G_MDM_SOURCE'
    __entity_name__ = 'G_mdm_source'
    __plain_object__ = GMdmSourcePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    source_type = IColumn(MDMSourceType, name='source_type')

    source_class = IColumn(MDMSourceClass, name='source_class')

    update_cycle = IColumn(SourceUpdate, name='update_cycle')

    status = IColumn(Status, nullable=False, name='status')

    def to_named_tuple(self):
        return GMdmSourceTuple(id=self.id,name=self.name,description=self.description,source_type=self.source_type,source_class=self.source_class,update_cycle=self.update_cycle,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GMdmSourceTuple(id=self.id,name=self.name,description=self.description,source_type=self.source_type,source_class=self.source_class,update_cycle=self.update_cycle,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GMdmTableTuple = namedtuple('GMdmTableTuple',  ('name'  ))

class GMdmTable(GMdmTableMixin, db.Model):
    __tablename__ = 'G_MDM_TABLE'
    __entity_name__ = 'G_mdm_table'
    __parent_entity__ = None

    name = IColumn(db.VARCHAR(64), primary_key=True, name='name')

    name = IColumn(db.VARCHAR(64), primary_key=True, name='name')

    def to_named_tuple(self):
        return GMdmTableTuple(name=self.name,)

    def to_plain_object(self):
        return GMdmTableTuple(name=self.name,)

GMdmTableAttributeTuple = namedtuple('GMdmTableAttributeTuple',  ('id', 'g_mdm_table_name', 'name', 'description', 'datatype'  ))

class GMdmTableAttribute(GMdmTableAttributeMixin, db.Model):
    __tablename__ = 'G_MDM_TABLE_ATTRIBUTE'
    __entity_name__ = 'G_mdm_table_attribute'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    g_mdm_table_name = IColumn(db.VARCHAR(64), nullable=False, name='g_mdm_table_name')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    datatype = IColumn(TargetDatatype, nullable=False, name='datatype')

    def to_named_tuple(self):
        return GMdmTableAttributeTuple(id=self.id,g_mdm_table_name=self.g_mdm_table_name,name=self.name,description=self.description,datatype=self.datatype,)

    def to_plain_object(self):
        return GMdmTableAttributeTuple(id=self.id,g_mdm_table_name=self.g_mdm_table_name,name=self.name,description=self.description,datatype=self.datatype,)

GNotificationTuple = namedtuple('GNotificationTuple',  ('id', 'name', 'description', 'notification_type', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GNotification(API,GNotificationMixin, Base, db.Model):
    __tablename__ = 'G_NOTIFICATION'
    __entity_name__ = 'G_notification'
    __plain_object__ = GNotificationPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    description = IColumn(db.TEXT, name='description')

    notification_type = IColumn(NotificationType, name='notification_type')

    status = IColumn(Status, name='status')
    email_queues = IRelationship(lambda: GNotificationQueue, foreign_keys=lambda: [GNotificationQueue.notification_id], uselist=True)

    def to_named_tuple(self):
        return GNotificationTuple(id=self.id,name=self.name,description=self.description,notification_type=self.notification_type,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GNotificationTuple(id=self.id,name=self.name,description=self.description,notification_type=self.notification_type,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GNotificationQueueTuple = namedtuple('GNotificationQueueTuple',  ('id', 'notification_id', 'sender', 'recipients', 'recipient_user', 'recipient_user_group', 'notification_data', 'notification_settings', 'notification_body', 'person_id', 'external_person_id', 'd_job_period_id', 'e_job_period_id', 'notified_at', 'notification_queue_status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GNotificationQueue(API,GNotificationQueueMixin, Base, db.Model):
    __tablename__ = 'G_NOTIFICATION_QUEUE'
    __entity_name__ = 'G_notification_queue'
    __plain_object__ = GNotificationQueuePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    notification_id = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_notification_queue_notification_id'), name='notification_id')
    notification = IRelationship(lambda: GNotification, foreign_keys=[notification_id])

    sender = IColumn(db.VARCHAR(32), name='sender')

    recipients = IColumn(db.VARCHAR(64), name='recipients')

    recipient_user = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_notification_queue_recipient_user'), name='recipient_user')

    recipient_user_group = IColumn(BigInt, db.ForeignKey('G_USER_GROUP.id', use_alter=True, name='fk_G_notification_queue_recipient_user_group'), name='recipient_user_group')

    notification_data = IColumn(db.TEXT, name='notification_data')

    notification_settings = IColumn(db.TEXT, name='notification_settings')

    notification_body = IColumn(db.TEXT, name='notification_body')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_G_notification_queue_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_G_notification_queue_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_G_notification_queue_d_job_period_id'), name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_G_notification_queue_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    notified_at = IColumn(db.DateTime, name='notified_at')

    notification_queue_status = IColumn(NotificationQueueStatus, name='notification_queue_status')

    def to_named_tuple(self):
        return GNotificationQueueTuple(id=self.id,notification_id=self.notification_id,sender=self.sender,recipients=self.recipients,recipient_user=self.recipient_user,recipient_user_group=self.recipient_user_group,notification_data=self.notification_data,notification_settings=self.notification_settings,notification_body=self.notification_body,person_id=self.person_id,external_person_id=self.external_person_id,d_job_period_id=self.d_job_period_id,e_job_period_id=self.e_job_period_id,notified_at=self.notified_at,notification_queue_status=self.notification_queue_status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GNotificationQueueTuple(id=self.id,notification_id=self.notification_id,sender=self.sender,recipients=self.recipients,recipient_user=self.recipient_user,recipient_user_group=self.recipient_user_group,notification_data=self.notification_data,notification_settings=self.notification_settings,notification_body=self.notification_body,person_id=self.person_id,external_person_id=self.external_person_id,d_job_period_id=self.d_job_period_id,e_job_period_id=self.e_job_period_id,notified_at=self.notified_at,notification_queue_status=self.notification_queue_status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GPermissionTuple = namedtuple('GPermissionTuple',  ('id', 'd_job_period_id', 'e_job_period_id', 'service_role_id', 'start_date', 'end_date', 'period_yr', 'description', 'preferred_implementor_id', 'requested_by_id', 'requested_time', 'accepted_by_id', 'accepted_by_time', 'source_system_name', 'source_system_id', 'username', 'password', 'imported', 'status', 'request_cart_permission_id', 'e_request_cart_permission_id', 'delete_request_cart_permission_id', 'delete_e_request_cart_permission_id', 'd_job_period_substitute_id', 'e_job_period_substitute_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GPermission(API,GPermissionMixin, Base, db.Model):
    __tablename__ = 'G_PERMISSION'
    __entity_name__ = 'G_permission'
    __plain_object__ = GPermissionPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_G_permission_d_job_period_id'), name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_G_permission_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_permission_service_role_id'), nullable=False, name='service_role_id')
    service_role = IRelationship(lambda: GServiceRole, foreign_keys=[service_role_id])

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    period_yr = IColumn(db.Integer, name='period_yr')

    description = IColumn(db.TEXT, name='description')

    preferred_implementor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_permission_preferred_implementor_id'), name='preferred_implementor_id')
    preferred_implementor = IRelationship(lambda: Zuser, foreign_keys=[preferred_implementor_id])

    requested_by_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_permission_requested_by_id'), nullable=False, name='requested_by_id')
    requested_by = IRelationship(lambda: Zuser, foreign_keys=[requested_by_id])

    requested_time = IColumn(db.DateTime, nullable=False, name='requested_time')

    accepted_by_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_permission_accepted_by_id'), nullable=False, name='accepted_by_id')
    accepted_by = IRelationship(lambda: Zuser, foreign_keys=[accepted_by_id])

    accepted_by_time = IColumn(db.DateTime, name='accepted_by_time')

    source_system_name = IColumn(db.VARCHAR(64), name='source_system_name')

    source_system_id = IColumn(db.VARCHAR(64), name='source_system_id')

    username = IColumn(db.VARCHAR(64), name='username')

    password = IColumn(db.VARCHAR(128), name='password')

    imported = IColumn(CharBool, nullable=False, name='imported')

    status = IColumn(Status, nullable=False, name='status')

    request_cart_permission_id = IColumn(BigInt, db.ForeignKey('REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_G_permission_request_cart_permission_id'), name='request_cart_permission_id')
    request_cart_permission = IRelationship(lambda: RequestCartPermission, foreign_keys=[request_cart_permission_id])

    e_request_cart_permission_id = IColumn(BigInt, db.ForeignKey('E_REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_G_permission_e_request_cart_permission_id'), name='e_request_cart_permission_id')
    e_request_cart_permission = IRelationship(lambda: ERequestCartPermission, foreign_keys=[e_request_cart_permission_id])

    delete_request_cart_permission_id = IColumn(BigInt, db.ForeignKey('REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_G_permission_delete_request_cart_permission_id'), name='delete_request_cart_permission_id')
    delete_request_cart_permission = IRelationship(lambda: RequestCartPermission, foreign_keys=[delete_request_cart_permission_id])

    delete_e_request_cart_permission_id = IColumn(BigInt, db.ForeignKey('E_REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_G_permission_delete_e_request_cart_permission_id'), name='delete_e_request_cart_permission_id')
    delete_e_request_cart_permission = IRelationship(lambda: ERequestCartPermission, foreign_keys=[delete_e_request_cart_permission_id])
    __associated_organizations = Header(u'associated_organizations')

    associated_organization_units = IRelationship(lambda: IOrgUnit, secondary=lambda: GPermissionAssociatedIOrgUnit, uselist=True)
    associated_external_organizations = IRelationship(lambda: EExtOrg, secondary=lambda: GPermissionAssociatedEExtOrg, uselist=True)
    __generated_by_substitute = Header(u'generated_by_substitute')

    d_job_period_substitute_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD_SUBSTITUTE.id', use_alter=True, name='fk_G_permission_d_job_period_substitute_id'), name='d_job_period_substitute_id')
    d_job_period_substitute = IRelationship(lambda: DJobPeriodSubstitute, foreign_keys=[d_job_period_substitute_id])

    e_job_period_substitute_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD_SUBSTITUTE.id', use_alter=True, name='fk_G_permission_e_job_period_substitute_id'), name='e_job_period_substitute_id')
    e_job_period_substitute = IRelationship(lambda: EJobPeriodSubstitute, foreign_keys=[e_job_period_substitute_id])

    def to_named_tuple(self):
        return GPermissionTuple(id=self.id,d_job_period_id=self.d_job_period_id,e_job_period_id=self.e_job_period_id,service_role_id=self.service_role_id,start_date=self.start_date,end_date=self.end_date,period_yr=self.period_yr,description=self.description,preferred_implementor_id=self.preferred_implementor_id,requested_by_id=self.requested_by_id,requested_time=self.requested_time,accepted_by_id=self.accepted_by_id,accepted_by_time=self.accepted_by_time,source_system_name=self.source_system_name,source_system_id=self.source_system_id,username=self.username,password=self.password,imported=self.imported,status=self.status,request_cart_permission_id=self.request_cart_permission_id,e_request_cart_permission_id=self.e_request_cart_permission_id,delete_request_cart_permission_id=self.delete_request_cart_permission_id,delete_e_request_cart_permission_id=self.delete_e_request_cart_permission_id,d_job_period_substitute_id=self.d_job_period_substitute_id,e_job_period_substitute_id=self.e_job_period_substitute_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GPermissionTuple(id=self.id,d_job_period_id=self.d_job_period_id,e_job_period_id=self.e_job_period_id,service_role_id=self.service_role_id,start_date=self.start_date,end_date=self.end_date,period_yr=self.period_yr,description=self.description,preferred_implementor_id=self.preferred_implementor_id,requested_by_id=self.requested_by_id,requested_time=self.requested_time,accepted_by_id=self.accepted_by_id,accepted_by_time=self.accepted_by_time,source_system_name=self.source_system_name,source_system_id=self.source_system_id,username=self.username,password=self.password,imported=self.imported,status=self.status,request_cart_permission_id=self.request_cart_permission_id,e_request_cart_permission_id=self.e_request_cart_permission_id,delete_request_cart_permission_id=self.delete_request_cart_permission_id,delete_e_request_cart_permission_id=self.delete_e_request_cart_permission_id,d_job_period_substitute_id=self.d_job_period_substitute_id,e_job_period_substitute_id=self.e_job_period_substitute_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GPermissionValidityLogTuple = namedtuple('GPermissionValidityLogTuple',  ('g_permission_id', 'valid_from', 'start_date', 'end_date'  ))

class GPermissionValidityLog(GPermissionValidityLogMixin, db.Model):
    __tablename__ = 'G_PERMISSION_VALIDITY_LOG'
    __entity_name__ = 'G_permission_validity_log'
    __parent_entity__ = None

    g_permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_G_permission_validity_log_g_permission_id'), primary_key=True, name='g_permission_id')
    g_permission = IRelationship(lambda: GPermission, foreign_keys=[g_permission_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    g_permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_G_permission_validity_log_g_permission_id'), primary_key=True, name='g_permission_id')
    g_permission = IRelationship(lambda: GPermission, foreign_keys=[g_permission_id])

    valid_from = IColumn(db.DateTime, primary_key=True, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return GPermissionValidityLogTuple(g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return GPermissionValidityLogTuple(g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

GPermissionValidityStateTuple = namedtuple('GPermissionValidityStateTuple',  ('g_permission_id', 'valid_from', 'start_date', 'end_date'  ))

class GPermissionValidityState(GPermissionValidityStateMixin, db.Model):
    __tablename__ = 'G_PERMISSION_VALIDITY_STATE'
    __entity_name__ = 'G_permission_validity_state'
    __parent_entity__ = None

    g_permission_id = IColumn(BigInt, primary_key=True, name='g_permission_id')

    g_permission_id = IColumn(BigInt, primary_key=True, name='g_permission_id')

    valid_from = IColumn(db.DateTime, name='valid_from')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return GPermissionValidityStateTuple(g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

    def to_plain_object(self):
        return GPermissionValidityStateTuple(g_permission_id=self.g_permission_id,valid_from=self.valid_from,start_date=self.start_date,end_date=self.end_date,)

GPersonUseraccountTuple = namedtuple('GPersonUseraccountTuple',  ('id', 'person_id', 'external_person_id', 'username', 'account_name', 'account_uid', 'object_guid', 'dn', 'password', 'service_id', 'system_id', 'inbound_attributes_json', 'outbound_attributes_json', 'old_inbound_attributes_json', 'old_outbound_attributes_json', 'account_created', 'status', 'internal', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GPersonUseraccount(API,GPersonUseraccountMixin, Base, db.Model):
    __tablename__ = 'G_PERSON_USERACCOUNT'
    __entity_name__ = 'G_person_useraccount'
    __plain_object__ = GPersonUseraccountPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_G_person_useraccount_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_G_person_useraccount_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    username = IColumn(db.TEXT, name='username')

    account_name = IColumn(db.TEXT, name='account_name')

    account_uid = IColumn(db.TEXT, name='account_uid')

    object_guid = IColumn(db.TEXT, name='object_guid')

    dn = IColumn(db.VARCHAR(256), nullable=False, name='dn')

    password = IColumn(db.TEXT, name='password')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_person_useraccount_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_person_useraccount_system_id'), name='system_id')
    system = IRelationship(lambda: GSystem, foreign_keys=[system_id])

    inbound_attributes_json = IColumn(db.TEXT, name='inbound_attributes_json')

    outbound_attributes_json = IColumn(db.TEXT, name='outbound_attributes_json')

    old_inbound_attributes_json = IColumn(db.TEXT, name='old_inbound_attributes_json')

    old_outbound_attributes_json = IColumn(db.TEXT, name='old_outbound_attributes_json')

    account_created = IColumn(CharBool, nullable=False, name='account_created')

    status = IColumn(Status, name='status')

    internal = IColumn(CharBool, nullable=False, name='internal')
    provisioning_tasks = IRelationship(lambda: GProvisioningTask, foreign_keys=lambda: [GProvisioningTask.person_useraccount_id], uselist=True)

    def to_named_tuple(self):
        return GPersonUseraccountTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,username=self.username,account_name=self.account_name,account_uid=self.account_uid,object_guid=self.object_guid,dn=self.dn,password=self.password,service_id=self.service_id,system_id=self.system_id,inbound_attributes_json=self.inbound_attributes_json,outbound_attributes_json=self.outbound_attributes_json,old_inbound_attributes_json=self.old_inbound_attributes_json,old_outbound_attributes_json=self.old_outbound_attributes_json,account_created=self.account_created,status=self.status,internal=self.internal,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GPersonUseraccountTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,username=self.username,account_name=self.account_name,account_uid=self.account_uid,object_guid=self.object_guid,dn=self.dn,password=self.password,service_id=self.service_id,system_id=self.system_id,inbound_attributes_json=self.inbound_attributes_json,outbound_attributes_json=self.outbound_attributes_json,old_inbound_attributes_json=self.old_inbound_attributes_json,old_outbound_attributes_json=self.old_outbound_attributes_json,account_created=self.account_created,status=self.status,internal=self.internal,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GProvisioningTaskTuple = namedtuple('GProvisioningTaskTuple',  ('id', 'person_id', 'external_person_id', 'd_job_period_id', 'e_job_period_id', 'service_id', 'task_type', 'value_date', 'service_role_id', 'preferred_implementor_id', 'request_description', 'implementation_description', 'implemented_by_id', 'inform_user', 'inform_superior', 'inform_others', 'provisioning_task_status', 'provisioning_type', 'system_id', 'person_useraccount_id', 'inbound_attributes_json', 'outbound_attributes_json', 'diff_json', 'error_json', 'integration_direction', 'task_settings', 'username', 'password', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'source_system_name', 'source_system_id', 'permission_id', 'request_cart_permission_id', 'e_request_cart_permission_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GProvisioningTask(API,GProvisioningTaskMixin, Base, db.Model):
    __tablename__ = 'G_PROVISIONING_TASK'
    __entity_name__ = 'G_provisioning_task'
    __plain_object__ = GProvisioningTaskPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_G_provisioning_task_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_G_provisioning_task_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    d_job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_G_provisioning_task_d_job_period_id'), name='d_job_period_id')
    d_job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[d_job_period_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_G_provisioning_task_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_provisioning_task_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    task_type = IColumn(ProvisioningTaskType, name='task_type')

    value_date = IColumn(db.Date, name='value_date')

    service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_provisioning_task_service_role_id'), name='service_role_id')
    service_role = IRelationship(lambda: GServiceRole, foreign_keys=[service_role_id])

    preferred_implementor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_provisioning_task_preferred_implementor_id'), name='preferred_implementor_id')
    preferred_implementor = IRelationship(lambda: Zuser, foreign_keys=[preferred_implementor_id])

    request_description = IColumn(db.VARCHAR(256), name='request_description')

    implementation_description = IColumn(db.VARCHAR(4096), name='implementation_description')

    implemented_by_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_provisioning_task_implemented_by_id'), name='implemented_by_id')
    implemented_by = IRelationship(lambda: Zuser, foreign_keys=[implemented_by_id])

    inform_user = IColumn(CharBool, nullable=False, name='inform_user')

    inform_superior = IColumn(CharBool, nullable=False, name='inform_superior')

    inform_others = IColumn(CharBool, nullable=False, name='inform_others')

    provisioning_task_status = IColumn(ProvisioningTaskStatus, nullable=False, name='provisioning_task_status')

    provisioning_type = IColumn(ProvisioningType, name='provisioning_type')

    system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_provisioning_task_system_id'), name='system_id')
    system = IRelationship(lambda: GSystem, foreign_keys=[system_id])

    person_useraccount_id = IColumn(BigInt, db.ForeignKey('G_PERSON_USERACCOUNT.id', use_alter=True, name='fk_G_provisioning_task_person_useraccount_id'), name='person_useraccount_id')
    person_useraccount = IRelationship(lambda: GPersonUseraccount, foreign_keys=[person_useraccount_id])

    inbound_attributes_json = IColumn(db.TEXT, name='inbound_attributes_json')

    outbound_attributes_json = IColumn(db.TEXT, name='outbound_attributes_json')

    diff_json = IColumn(db.TEXT, name='diff_json')

    error_json = IColumn(db.TEXT, name='error_json')

    integration_direction = IColumn(IntegrationDirection, name='integration_direction')

    task_settings = IColumn(db.TEXT, name='task_settings')
    __technical_information = Header(u'technical_information')

    username = IColumn(db.VARCHAR(64), name='username')

    password = IColumn(db.VARCHAR(128), name='password')

    first_email_sent = IColumn(db.DateTime, name='first_email_sent')

    last_email_sent = IColumn(db.DateTime, name='last_email_sent')

    email_counter = IColumn(db.Integer, name='email_counter')

    email_to_user_sent = IColumn(db.Integer, name='email_to_user_sent')

    email_to_superior_sent = IColumn(db.Integer, name='email_to_superior_sent')

    email_to_others_sent = IColumn(db.Integer, name='email_to_others_sent')

    source_system_name = IColumn(db.VARCHAR(64), name='source_system_name')

    source_system_id = IColumn(db.VARCHAR(64), name='source_system_id')

    permission_id = IColumn(BigInt, db.ForeignKey('G_PERMISSION.id', use_alter=True, name='fk_G_provisioning_task_permission_id'), name='permission_id')
    permission = IRelationship(lambda: GPermission, foreign_keys=[permission_id])

    request_cart_permission_id = IColumn(BigInt, db.ForeignKey('REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_G_provisioning_task_request_cart_permission_id'), name='request_cart_permission_id')
    request_cart_permission = IRelationship(lambda: RequestCartPermission, foreign_keys=[request_cart_permission_id])

    e_request_cart_permission_id = IColumn(BigInt, db.ForeignKey('E_REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_G_provisioning_task_e_request_cart_permission_id'), name='e_request_cart_permission_id')
    e_request_cart_permission = IRelationship(lambda: ERequestCartPermission, foreign_keys=[e_request_cart_permission_id])
    aces = IRelationship(lambda: GAce, secondary=lambda: GProvisioningTaskGAce, uselist=True)

    def to_named_tuple(self):
        return GProvisioningTaskTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,d_job_period_id=self.d_job_period_id,e_job_period_id=self.e_job_period_id,service_id=self.service_id,task_type=self.task_type,value_date=self.value_date,service_role_id=self.service_role_id,preferred_implementor_id=self.preferred_implementor_id,request_description=self.request_description,implementation_description=self.implementation_description,implemented_by_id=self.implemented_by_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,provisioning_task_status=self.provisioning_task_status,provisioning_type=self.provisioning_type,system_id=self.system_id,person_useraccount_id=self.person_useraccount_id,inbound_attributes_json=self.inbound_attributes_json,outbound_attributes_json=self.outbound_attributes_json,diff_json=self.diff_json,error_json=self.error_json,integration_direction=self.integration_direction,task_settings=self.task_settings,username=self.username,password=self.password,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_to_user_sent=self.email_to_user_sent,email_to_superior_sent=self.email_to_superior_sent,email_to_others_sent=self.email_to_others_sent,source_system_name=self.source_system_name,source_system_id=self.source_system_id,permission_id=self.permission_id,request_cart_permission_id=self.request_cart_permission_id,e_request_cart_permission_id=self.e_request_cart_permission_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GProvisioningTaskTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,d_job_period_id=self.d_job_period_id,e_job_period_id=self.e_job_period_id,service_id=self.service_id,task_type=self.task_type,value_date=self.value_date,service_role_id=self.service_role_id,preferred_implementor_id=self.preferred_implementor_id,request_description=self.request_description,implementation_description=self.implementation_description,implemented_by_id=self.implemented_by_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,provisioning_task_status=self.provisioning_task_status,provisioning_type=self.provisioning_type,system_id=self.system_id,person_useraccount_id=self.person_useraccount_id,inbound_attributes_json=self.inbound_attributes_json,outbound_attributes_json=self.outbound_attributes_json,diff_json=self.diff_json,error_json=self.error_json,integration_direction=self.integration_direction,task_settings=self.task_settings,username=self.username,password=self.password,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_to_user_sent=self.email_to_user_sent,email_to_superior_sent=self.email_to_superior_sent,email_to_others_sent=self.email_to_others_sent,source_system_name=self.source_system_name,source_system_id=self.source_system_id,permission_id=self.permission_id,request_cart_permission_id=self.request_cart_permission_id,e_request_cart_permission_id=self.e_request_cart_permission_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GRegionTuple = namedtuple('GRegionTuple',  ('id', 'code', 'name', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GRegion(API,GRegionMixin, Base, db.Model):
    __tablename__ = 'G_REGION'
    __entity_name__ = 'G_region'
    __plain_object__ = GRegionPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(8), nullable=False, name='code')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GRegionTuple(id=self.id,code=self.code,name=self.name,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GRegionTuple(id=self.id,code=self.code,name=self.name,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceTuple = namedtuple('GServiceTuple',  ('id', 'name', 'name6', 'code', 'status', 'service_provider_id', 'starting_date', 'termination_date', 'description', 'service_class', 'service_type_id', 'system_id', 'user_type', 'register', 'upper_service_id', 'externals_allowed', 'service_category', 'approver_id', 'executor_id', 'revoke_type', 'grace_period', 'minimum_period', 'notification_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GService(API,ClosureTableMixin,GServiceMixin, Base, db.Model):
    __tablename__ = 'O_G_SERVICE'
    __entity_name__ = 'G_service'
    __plain_object__ = GServicePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    name6 = IColumn(db.VARCHAR(64), name='name6')

    code = IColumn(db.VARCHAR(64), name='code')

    status = IColumn(Status, name='status')

    service_provider_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_PROVIDER.id', use_alter=True, name='fk_G_service_service_provider_id'), name='service_provider_id')
    service_provider = IRelationship(lambda: GServiceProvider, foreign_keys=[service_provider_id])

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    description = IColumn(db.TEXT, name='description')

    service_class = IColumn(ServiceClass, name='service_class')

    service_type_id = IColumn(BigInt, db.ForeignKey('G_SERVICE_TYPE.id', use_alter=True, name='fk_G_service_service_type_id'), name='service_type_id')
    service_type = IRelationship(lambda: GServiceType, foreign_keys=[service_type_id])

    system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_service_system_id'), name='system_id')
    system = IRelationship(lambda: GSystem, foreign_keys=[system_id])

    user_type = IColumn(SysUserType, name='user_type')

    register = IColumn(CharBool, nullable=False, name='register')

    upper_service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_upper_service_id'), name='upper_service_id')
    parent = IRelationship(lambda: GService, foreign_keys=[upper_service_id], remote_side=[id])

    externals_allowed = IColumn(CharBool, nullable=False, name='externals_allowed')

    service_category = IColumn(ServiceCategory, nullable=False, name='service_category')

    approver_id = IColumn(BigInt, db.ForeignKey('G_USER_GROUP.id', use_alter=True, name='fk_G_service_approver_id'), name='approver_id')
    approver = IRelationship(lambda: GUserGroup, foreign_keys=[approver_id])

    executor_id = IColumn(BigInt, db.ForeignKey('G_USER_GROUP.id', use_alter=True, name='fk_G_service_executor_id'), name='executor_id')
    executor = IRelationship(lambda: GUserGroup, foreign_keys=[executor_id])

    revoke_type = IColumn(RevokeType, name='revoke_type')

    grace_period = IColumn(db.Integer, name='grace_period')

    minimum_period = IColumn(db.Integer, name='minimum_period')

    notification_id = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_service_notification_id'), name='notification_id')
    notification = IRelationship(lambda: GNotification, foreign_keys=[notification_id])

    def to_named_tuple(self):
        return GServiceTuple(id=self.id,name=self.name,name6=self.name6,code=self.code,status=self.status,service_provider_id=self.service_provider_id,starting_date=self.starting_date,termination_date=self.termination_date,description=self.description,service_class=self.service_class,service_type_id=self.service_type_id,system_id=self.system_id,user_type=self.user_type,register=self.register,upper_service_id=self.upper_service_id,externals_allowed=self.externals_allowed,service_category=self.service_category,approver_id=self.approver_id,executor_id=self.executor_id,revoke_type=self.revoke_type,grace_period=self.grace_period,minimum_period=self.minimum_period,notification_id=self.notification_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceTuple(id=self.id,name=self.name,name6=self.name6,code=self.code,status=self.status,service_provider_id=self.service_provider_id,starting_date=self.starting_date,termination_date=self.termination_date,description=self.description,service_class=self.service_class,service_type_id=self.service_type_id,system_id=self.system_id,user_type=self.user_type,register=self.register,upper_service_id=self.upper_service_id,externals_allowed=self.externals_allowed,service_category=self.service_category,approver_id=self.approver_id,executor_id=self.executor_id,revoke_type=self.revoke_type,grace_period=self.grace_period,minimum_period=self.minimum_period,notification_id=self.notification_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceCtAllTuple = namedtuple('GServiceCtAllTuple',  ('ancestor', 'descendant'  ))

class GServiceCtAll(GServiceCtAllMixin, db.Model):
    __tablename__ = 'G_SERVICE_CT_ALL'
    __entity_name__ = 'G_service_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return GServiceCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return GServiceCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

GServiceProviderTuple = namedtuple('GServiceProviderTuple',  ('id', 'name', 'description', 'country_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GServiceProvider(API,GServiceProviderMixin, Base, db.Model):
    __tablename__ = 'O_G_SERVICE_PROVIDER'
    __entity_name__ = 'G_service_provider'
    __plain_object__ = GServiceProviderPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    country_id = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_G_service_provider_country_id'), name='country_id')
    country = IRelationship(lambda: GCountry, foreign_keys=[country_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GServiceProviderTuple(id=self.id,name=self.name,description=self.description,country_id=self.country_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceProviderTuple(id=self.id,name=self.name,description=self.description,country_id=self.country_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceRequestTuple = namedtuple('GServiceRequestTuple',  ('id', 'name', 'description', 'trans_date', 'severity', 'sr_class', 'sr_type', 'reported_by_name', 'reported_by_email', 'reported_by_phone', 'int_resp_uid', 'person_id', 'service_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GServiceRequest(API,GServiceRequestMixin, Base, db.Model):
    __tablename__ = 'G_SERVICE_REQUEST'
    __entity_name__ = 'G_service_request'
    __plain_object__ = GServiceRequestPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    trans_date = IColumn(db.Date, nullable=False, name='trans_date')

    severity = IColumn(SRSeverity, nullable=False, name='severity')

    sr_class = IColumn(SRClass, nullable=False, name='sr_class')

    sr_type = IColumn(SRType, nullable=False, name='sr_type')

    reported_by_name = IColumn(db.VARCHAR(64), nullable=False, name='reported_by_name')

    reported_by_email = IColumn(db.VARCHAR(64), name='reported_by_email')

    reported_by_phone = IColumn(db.VARCHAR(64), name='reported_by_phone')

    int_resp_uid = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_service_request_int_resp_uid'), name='int_resp_uid')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_G_service_request_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_request_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    status = IColumn(SRStatus, nullable=False, name='status')

    def to_named_tuple(self):
        return GServiceRequestTuple(id=self.id,name=self.name,description=self.description,trans_date=self.trans_date,severity=self.severity,sr_class=self.sr_class,sr_type=self.sr_type,reported_by_name=self.reported_by_name,reported_by_email=self.reported_by_email,reported_by_phone=self.reported_by_phone,int_resp_uid=self.int_resp_uid,person_id=self.person_id,service_id=self.service_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceRequestTuple(id=self.id,name=self.name,description=self.description,trans_date=self.trans_date,severity=self.severity,sr_class=self.sr_class,sr_type=self.sr_type,reported_by_name=self.reported_by_name,reported_by_email=self.reported_by_email,reported_by_phone=self.reported_by_phone,int_resp_uid=self.int_resp_uid,person_id=self.person_id,service_id=self.service_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceRespTuple = namedtuple('GServiceRespTuple',  ('id', 'person_name', 'service_id', 'servicerole_id', 'resp_class', 'resp_type', 'resp_name', 'resp_username', 'resp_email', 'resp_phone', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GServiceResp(API,GServiceRespMixin, Base, db.Model):
    __tablename__ = 'G_SERVICE_RESP'
    __entity_name__ = 'G_service_resp'
    __plain_object__ = GServiceRespPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_name = IColumn(db.VARCHAR(64), nullable=False, name='person_name')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_resp_service_id'), nullable=False, name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    servicerole_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_resp_servicerole_id'), name='servicerole_id')
    servicerole = IRelationship(lambda: GServiceRole, foreign_keys=[servicerole_id])

    resp_class = IColumn(RespClass, nullable=False, name='resp_class')

    resp_type = IColumn(RespType, nullable=False, name='resp_type')

    resp_name = IColumn(db.VARCHAR(64), name='resp_name')

    resp_username = IColumn(db.VARCHAR(64), name='resp_username')

    resp_email = IColumn(db.VARCHAR(64), name='resp_email')

    resp_phone = IColumn(db.VARCHAR(64), name='resp_phone')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GServiceRespTuple(id=self.id,person_name=self.person_name,service_id=self.service_id,servicerole_id=self.servicerole_id,resp_class=self.resp_class,resp_type=self.resp_type,resp_name=self.resp_name,resp_username=self.resp_username,resp_email=self.resp_email,resp_phone=self.resp_phone,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceRespTuple(id=self.id,person_name=self.person_name,service_id=self.service_id,servicerole_id=self.servicerole_id,resp_class=self.resp_class,resp_type=self.resp_type,resp_name=self.resp_name,resp_username=self.resp_username,resp_email=self.resp_email,resp_phone=self.resp_phone,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceRoleTuple = namedtuple('GServiceRoleTuple',  ('id', 'name', 'name6', 'code', 'status', 'description', 'service_id', 'service_role_type', 'starting_date', 'termination_date', 'servicerole_class', 'virtual', 'needs_service_manager_approval', 'authentication_level', 'provisioning_type', 'aces_in_transaction', 'upper_servicerole_id', 'chain_service_role_id', 'executor_id', 'favorite', 'end_date_request', 'period_request', 'description_request', 'associated_organizations_request', 'approver_id', 'subst_approver_id', 'subst_approver_active', 'subst_approver_email', 'needs_superior_approval', 'notification_create', 'notification_update', 'notification_disable', 'notification_delete', 'notification_resetpassword', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GServiceRole(API,ClosureTableMixin,GServiceRoleMixin, Base, db.Model):
    __tablename__ = 'O_G_SERVICE_ROLE'
    __entity_name__ = 'G_service_role'
    __plain_object__ = GServiceRolePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    name6 = IColumn(db.VARCHAR(64), name='name6')

    code = IColumn(db.VARCHAR(64), name='code')

    status = IColumn(Status, name='status')

    description = IColumn(db.TEXT, name='description')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_G_service_role_service_id'), nullable=False, name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    service_role_type = IColumn(ServiceRoleType, name='service_role_type')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    servicerole_class = IColumn(ServiceroleClass, name='servicerole_class')

    virtual = IColumn(CharBool, nullable=False, name='virtual')

    needs_service_manager_approval = IColumn(CharBool, nullable=False, name='needs_srv_mgr_approval')

    authentication_level = IColumn(AuthLevel, name='authentication_level')

    provisioning_type = IColumn(ProvisioningType, nullable=False, name='provisioning_type')

    aces_in_transaction = IColumn(CharBool, nullable=False, name='aces_in_transaction')

    upper_servicerole_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_role_upper_servicerole_id'), name='upper_servicerole_id')
    parent = IRelationship(lambda: GServiceRole, foreign_keys=[upper_servicerole_id], remote_side=[id])

    chain_service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_role_chain_service_role_id'), name='chain_service_role_id')
    chain_service_role = IRelationship(lambda: GServiceRole, foreign_keys=[chain_service_role_id], remote_side=[id])

    executor_id = IColumn(BigInt, db.ForeignKey('G_USER_GROUP.id', use_alter=True, name='fk_G_service_role_executor_id'), name='executor_id')
    executor = IRelationship(lambda: GUserGroup, foreign_keys=[executor_id])

    favorite = IColumn(CharBool, nullable=False, name='favorite')
    __Request_requirements = Header(u'Request_requirements')

    end_date_request = IColumn(CharBool, nullable=False, name='end_date_request')

    period_request = IColumn(CharBool, nullable=False, name='period_request')

    description_request = IColumn(CharBool, nullable=False, name='description_request')

    associated_organizations_request = IColumn(CharBool, nullable=False, name='associated_organizations_request')

    approver_id = IColumn(BigInt, db.ForeignKey('G_USER_GROUP.id', use_alter=True, name='fk_G_service_role_approver_id'), name='approver_id')
    approver = IRelationship(lambda: GUserGroup, foreign_keys=[approver_id])

    subst_approver_id = IColumn(BigInt, db.ForeignKey('G_USER_GROUP.id', use_alter=True, name='fk_G_service_role_subst_approver_id'), name='subst_approver_id')
    subst_approver = IRelationship(lambda: GUserGroup, foreign_keys=[subst_approver_id])

    subst_approver_active = IColumn(CharBool, nullable=False, name='subst_approver_active')

    subst_approver_email = IColumn(db.VARCHAR(64), name='subst_approver_email')

    needs_superior_approval = IColumn(CharBool, nullable=False, name='needs_superior_approval')
    aces = IRelationship(lambda: GAce, secondary=lambda: GServiceRoleGAce, uselist=True)
    job_roles = IRelationship(lambda: IJobRole, secondary=lambda: IJobRoleGServiceRole, uselist=True)
    external_job_roles = IRelationship(lambda: EJobRole, secondary=lambda: EJobRoleGServiceRole, uselist=True)
    organization_units = IRelationship(lambda: IOrgUnit, secondary=lambda: IOrgUnitGServiceRole, uselist=True)
    external_organizations = IRelationship(lambda: EExtOrg, secondary=lambda: EExtOrgGServiceRole, uselist=True)
    __Notifications = Header(u'Notifications')

    notification_create = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_service_role_notification_create'), name='notification_create')

    notification_update = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_service_role_notification_update'), name='notification_update')

    notification_disable = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_service_role_notification_disable'), name='notification_disable')

    notification_delete = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_service_role_notification_delete'), name='notification_delete')

    notification_resetpassword = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_service_role_notification_resetpassword'), name='notification_resetpassword')

    def to_named_tuple(self):
        return GServiceRoleTuple(id=self.id,name=self.name,name6=self.name6,code=self.code,status=self.status,description=self.description,service_id=self.service_id,service_role_type=self.service_role_type,starting_date=self.starting_date,termination_date=self.termination_date,servicerole_class=self.servicerole_class,virtual=self.virtual,needs_service_manager_approval=self.needs_service_manager_approval,authentication_level=self.authentication_level,provisioning_type=self.provisioning_type,aces_in_transaction=self.aces_in_transaction,upper_servicerole_id=self.upper_servicerole_id,chain_service_role_id=self.chain_service_role_id,executor_id=self.executor_id,favorite=self.favorite,end_date_request=self.end_date_request,period_request=self.period_request,description_request=self.description_request,associated_organizations_request=self.associated_organizations_request,approver_id=self.approver_id,subst_approver_id=self.subst_approver_id,subst_approver_active=self.subst_approver_active,subst_approver_email=self.subst_approver_email,needs_superior_approval=self.needs_superior_approval,notification_create=self.notification_create,notification_update=self.notification_update,notification_disable=self.notification_disable,notification_delete=self.notification_delete,notification_resetpassword=self.notification_resetpassword,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceRoleTuple(id=self.id,name=self.name,name6=self.name6,code=self.code,status=self.status,description=self.description,service_id=self.service_id,service_role_type=self.service_role_type,starting_date=self.starting_date,termination_date=self.termination_date,servicerole_class=self.servicerole_class,virtual=self.virtual,needs_service_manager_approval=self.needs_service_manager_approval,authentication_level=self.authentication_level,provisioning_type=self.provisioning_type,aces_in_transaction=self.aces_in_transaction,upper_servicerole_id=self.upper_servicerole_id,chain_service_role_id=self.chain_service_role_id,executor_id=self.executor_id,favorite=self.favorite,end_date_request=self.end_date_request,period_request=self.period_request,description_request=self.description_request,associated_organizations_request=self.associated_organizations_request,approver_id=self.approver_id,subst_approver_id=self.subst_approver_id,subst_approver_active=self.subst_approver_active,subst_approver_email=self.subst_approver_email,needs_superior_approval=self.needs_superior_approval,notification_create=self.notification_create,notification_update=self.notification_update,notification_disable=self.notification_disable,notification_delete=self.notification_delete,notification_resetpassword=self.notification_resetpassword,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceRoleCtAllTuple = namedtuple('GServiceRoleCtAllTuple',  ('ancestor', 'descendant'  ))

class GServiceRoleCtAll(GServiceRoleCtAllMixin, db.Model):
    __tablename__ = 'G_SERVICE_ROLE_CT_ALL'
    __entity_name__ = 'G_service_role_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_role_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_role_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_role_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_G_service_role_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return GServiceRoleCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return GServiceRoleCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

GServiceTypeTuple = namedtuple('GServiceTypeTuple',  ('id', 'name', 'description', 'owner_id', 'service_type', 'externals_allowed', 'role_inheritance', 'site_collection', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GServiceType(API,GServiceTypeMixin, Base, db.Model):
    __tablename__ = 'G_SERVICE_TYPE'
    __entity_name__ = 'G_service_type'
    __plain_object__ = GServiceTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    owner_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_G_service_type_owner_id'), name='owner_id')
    owner = IRelationship(lambda: DPerson, foreign_keys=[owner_id])

    service_type = IColumn(ServiceType, name='service_type')

    externals_allowed = IColumn(CharBool, nullable=False, name='externals_allowed')

    role_inheritance = IColumn(CharBool, nullable=False, name='role_inheritance')

    site_collection = IColumn(db.VARCHAR(64), name='site_collection')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GServiceTypeTuple(id=self.id,name=self.name,description=self.description,owner_id=self.owner_id,service_type=self.service_type,externals_allowed=self.externals_allowed,role_inheritance=self.role_inheritance,site_collection=self.site_collection,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceTypeTuple(id=self.id,name=self.name,description=self.description,owner_id=self.owner_id,service_type=self.service_type,externals_allowed=self.externals_allowed,role_inheritance=self.role_inheritance,site_collection=self.site_collection,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GServiceTypeSrolesTuple = namedtuple('GServiceTypeSrolesTuple',  ('id', 'service_type_id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GServiceTypeSroles(API,GServiceTypeSrolesMixin, Base, db.Model):
    __tablename__ = 'G_SERVICE_TYPE_SROLES'
    __entity_name__ = 'G_service_type_sroles'
    __plain_object__ = GServiceTypeSrolesPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    service_type_id = IColumn(BigInt, db.ForeignKey('G_SERVICE_TYPE.id', use_alter=True, name='fk_G_service_type_sroles_service_type_id'), nullable=False, name='service_type_id')
    service_type = IRelationship(lambda: GServiceType, foreign_keys=[service_type_id])

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    def to_named_tuple(self):
        return GServiceTypeSrolesTuple(id=self.id,service_type_id=self.service_type_id,name=self.name,description=self.description,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GServiceTypeSrolesTuple(id=self.id,service_type_id=self.service_type_id,name=self.name,description=self.description,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GSrParametersTuple = namedtuple('GSrParametersTuple',  ('id', 'name', 'description', 'orgunit_id', 'resp_name', 'resp_email', 'resp_phone', 'backup_name', 'backup_email', 'backup_phone', 'start_date', 'end_date', 'sla_level', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GSrParameters(API,GSrParametersMixin, Base, db.Model):
    __tablename__ = 'G_SR_PARAMETERS'
    __entity_name__ = 'G_sr_parameters'
    __plain_object__ = GSrParametersPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_G_sr_parameters_orgunit_id'), nullable=False, name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    resp_name = IColumn(db.VARCHAR(64), name='resp_name')

    resp_email = IColumn(db.VARCHAR(64), name='resp_email')

    resp_phone = IColumn(db.VARCHAR(64), name='resp_phone')

    backup_name = IColumn(db.VARCHAR(64), name='backup_name')

    backup_email = IColumn(db.VARCHAR(64), name='backup_email')

    backup_phone = IColumn(db.VARCHAR(64), name='backup_phone')

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    sla_level = IColumn(SLALevel, nullable=False, name='sla_level')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return GSrParametersTuple(id=self.id,name=self.name,description=self.description,orgunit_id=self.orgunit_id,resp_name=self.resp_name,resp_email=self.resp_email,resp_phone=self.resp_phone,backup_name=self.backup_name,backup_email=self.backup_email,backup_phone=self.backup_phone,start_date=self.start_date,end_date=self.end_date,sla_level=self.sla_level,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GSrParametersTuple(id=self.id,name=self.name,description=self.description,orgunit_id=self.orgunit_id,resp_name=self.resp_name,resp_email=self.resp_email,resp_phone=self.resp_phone,backup_name=self.backup_name,backup_email=self.backup_email,backup_phone=self.backup_phone,start_date=self.start_date,end_date=self.end_date,sla_level=self.sla_level,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GSrTransTuple = namedtuple('GSrTransTuple',  ('id', 'service_request_id', 'name', 'description', 'trans_date', 'oper_uid', 'oper_status', 'action_type', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GSrTrans(API,GSrTransMixin, Base, db.Model):
    __tablename__ = 'G_SR_TRANS'
    __entity_name__ = 'G_sr_trans'
    __plain_object__ = GSrTransPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    service_request_id = IColumn(BigInt, db.ForeignKey('G_SERVICE_REQUEST.id', use_alter=True, name='fk_G_sr_trans_service_request_id'), nullable=False, name='service_request_id')
    service_request = IRelationship(lambda: GServiceRequest, foreign_keys=[service_request_id])

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    trans_date = IColumn(db.Date, nullable=False, name='trans_date')

    oper_uid = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_G_sr_trans_oper_uid'), name='oper_uid')

    oper_status = IColumn(SRStatus, nullable=False, name='oper_status')

    action_type = IColumn(SRActionType, nullable=False, name='action_type')

    def to_named_tuple(self):
        return GSrTransTuple(id=self.id,service_request_id=self.service_request_id,name=self.name,description=self.description,trans_date=self.trans_date,oper_uid=self.oper_uid,oper_status=self.oper_status,action_type=self.action_type,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GSrTransTuple(id=self.id,service_request_id=self.service_request_id,name=self.name,description=self.description,trans_date=self.trans_date,oper_uid=self.oper_uid,oper_status=self.oper_status,action_type=self.action_type,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GSystemTuple = namedtuple('GSystemTuple',  ('id', 'name', 'system_type', 'identifier', 'description', 'upper_system_id', 'inbound_schema_mapping_id', 'outbound_schema_mapping_id', 'config_json', 'batch_job_path', 'revoke_type', 'code', 'integration_direction', 'system_application_type', 'priority', 'status', 'notification_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GSystem(API,ClosureTableMixin,GSystemMixin, Base, db.Model):
    __tablename__ = 'O_G_SYSTEM'
    __entity_name__ = 'G_system'
    __plain_object__ = GSystemPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    system_type = IColumn(SystemType, name='system_type')

    identifier = IColumn(db.VARCHAR(64), name='identifier')

    description = IColumn(db.TEXT, name='description')

    upper_system_id = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_system_upper_system_id'), name='upper_system_id')
    parent = IRelationship(lambda: GSystem, foreign_keys=[upper_system_id], remote_side=[id])

    inbound_schema_mapping_id = IColumn(BigInt, db.ForeignKey('G_SYSTEM_SCHEMA.id', use_alter=True, name='fk_G_system_inbound_schema_mapping_id'), name='inbound_schema_mapping_id')
    inbound_schema_mapping = IRelationship(lambda: GSystemSchema, foreign_keys=[inbound_schema_mapping_id])

    outbound_schema_mapping_id = IColumn(BigInt, db.ForeignKey('G_SYSTEM_SCHEMA.id', use_alter=True, name='fk_G_system_outbound_schema_mapping_id'), name='outbound_schema_mapping_id')
    outbound_schema_mapping = IRelationship(lambda: GSystemSchema, foreign_keys=[outbound_schema_mapping_id])

    config_json = IColumn(db.TEXT, name='config_json')

    batch_job_path = IColumn(db.VARCHAR(256), name='batch_job_path')

    revoke_type = IColumn(RevokeType, name='revoke_type')

    code = IColumn(db.VARCHAR(128), nullable=False, unique=True, name='code')

    integration_direction = IColumn(IntegrationDirection, name='integration_direction')

    system_application_type = IColumn(SystemApplicationType, name='system_application_type')

    priority = IColumn(db.Integer, name='priority')

    status = IColumn(SystemStatus, name='status')
    services = IRelationship(lambda: GService, foreign_keys=lambda: [GService.system_id], uselist=True)

    notification_id = IColumn(BigInt, db.ForeignKey('G_NOTIFICATION.id', use_alter=True, name='fk_G_system_notification_id'), name='notification_id')
    notification = IRelationship(lambda: GNotification, foreign_keys=[notification_id])

    def to_named_tuple(self):
        return GSystemTuple(id=self.id,name=self.name,system_type=self.system_type,identifier=self.identifier,description=self.description,upper_system_id=self.upper_system_id,inbound_schema_mapping_id=self.inbound_schema_mapping_id,outbound_schema_mapping_id=self.outbound_schema_mapping_id,config_json=self.config_json,batch_job_path=self.batch_job_path,revoke_type=self.revoke_type,code=self.code,integration_direction=self.integration_direction,system_application_type=self.system_application_type,priority=self.priority,status=self.status,notification_id=self.notification_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GSystemTuple(id=self.id,name=self.name,system_type=self.system_type,identifier=self.identifier,description=self.description,upper_system_id=self.upper_system_id,inbound_schema_mapping_id=self.inbound_schema_mapping_id,outbound_schema_mapping_id=self.outbound_schema_mapping_id,config_json=self.config_json,batch_job_path=self.batch_job_path,revoke_type=self.revoke_type,code=self.code,integration_direction=self.integration_direction,system_application_type=self.system_application_type,priority=self.priority,status=self.status,notification_id=self.notification_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GSystemCtAllTuple = namedtuple('GSystemCtAllTuple',  ('ancestor', 'descendant'  ))

class GSystemCtAll(GSystemCtAllMixin, db.Model):
    __tablename__ = 'G_SYSTEM_CT_ALL'
    __entity_name__ = 'G_system_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_system_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_system_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_system_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_G_SYSTEM.id', use_alter=True, name='fk_G_system_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return GSystemCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return GSystemCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

GSystemSchemaTuple = namedtuple('GSystemSchemaTuple',  ('id', 'name', 'module_path', 'uid', 'description', 'type', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GSystemSchema(API,GSystemSchemaMixin, Base, db.Model):
    __tablename__ = 'G_SYSTEM_SCHEMA'
    __entity_name__ = 'G_system_schema'
    __plain_object__ = GSystemSchemaPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    module_path = IColumn(db.VARCHAR(256), name='module_path')

    uid = IColumn(db.VARCHAR(256), name='uid')

    description = IColumn(db.TEXT, name='description')

    type = IColumn(MappingType, name='type')

    def to_named_tuple(self):
        return GSystemSchemaTuple(id=self.id,name=self.name,module_path=self.module_path,uid=self.uid,description=self.description,type=self.type,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GSystemSchemaTuple(id=self.id,name=self.name,module_path=self.module_path,uid=self.uid,description=self.description,type=self.type,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GSystemSchemaAttributeTuple = namedtuple('GSystemSchemaAttributeTuple',  ('id', 'system_schema_id', 'name', 'description', 'datatype', 'source_attribute', 'destination_attribute', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GSystemSchemaAttribute(API,GSystemSchemaAttributeMixin, Base, db.Model):
    __tablename__ = 'G_SYSTEM_SCHEMA_ATTRIBUTE'
    __entity_name__ = 'G_system_schema_attribute'
    __plain_object__ = GSystemSchemaAttributePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    system_schema_id = IColumn(BigInt, db.ForeignKey('G_SYSTEM_SCHEMA.id', use_alter=True, name='fk_G_system_schema_attribute_system_schema_id'), nullable=False, name='system_schema_id')
    system_schema = IRelationship(lambda: GSystemSchema, foreign_keys=[system_schema_id])

    name = IColumn(db.VARCHAR(64), name='name')

    description = IColumn(db.TEXT, name='description')

    datatype = IColumn(TargetDatatype, nullable=False, name='datatype')

    source_attribute = IColumn(db.VARCHAR(64), name='source_attribute')

    destination_attribute = IColumn(db.VARCHAR(64), name='destination_attribute')

    def to_named_tuple(self):
        return GSystemSchemaAttributeTuple(id=self.id,system_schema_id=self.system_schema_id,name=self.name,description=self.description,datatype=self.datatype,source_attribute=self.source_attribute,destination_attribute=self.destination_attribute,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GSystemSchemaAttributeTuple(id=self.id,system_schema_id=self.system_schema_id,name=self.name,description=self.description,datatype=self.datatype,source_attribute=self.source_attribute,destination_attribute=self.destination_attribute,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

GUserGroupTuple = namedtuple('GUserGroupTuple',  ('id', 'name', 'description', 'usergroup_type', 'email', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class GUserGroup(API,GUserGroupMixin, Base, db.Model):
    __tablename__ = 'G_USER_GROUP'
    __entity_name__ = 'G_user_group'
    __plain_object__ = GUserGroupPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    usergroup_type = IColumn(UsergroupType, nullable=False, name='usergroup_type')

    email = IColumn(db.VARCHAR(64), name='email')

    status = IColumn(Status, name='status')
    users = IRelationship(lambda: Zuser, secondary=lambda: GUserGroupZuser, uselist=True)
    report_subscriptions = IRelationship(lambda: Zreport, secondary=lambda: GUserGroupZreport, uselist=True)

    def to_named_tuple(self):
        return GUserGroupTuple(id=self.id,name=self.name,description=self.description,usergroup_type=self.usergroup_type,email=self.email,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return GUserGroupTuple(id=self.id,name=self.name,description=self.description,usergroup_type=self.usergroup_type,email=self.email,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

HrDesktopSubstTuple = namedtuple('HrDesktopSubstTuple',  ('id', 'hr_manager_person_number', 'hr_subst_person_number', 'starting_date', 'termination_date', 'hr_subst_status', 'hr_subst_message', 'hr_source_file', 'hr_source_row', 'created_at', 'manager_person_id', 'subst_person_id', 'manager_org_unit_manager_id', 'substitube_org_unit_manager_id', 'substitute_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class HrDesktopSubst(API,HrDesktopSubstMixin, Base, db.Model):
    __tablename__ = 'HR_DESKTOP_SUBST'
    __entity_name__ = 'Hr_desktop_subst'
    __plain_object__ = HrDesktopSubstPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    __Source_info = Header(u'Source_info')

    hr_manager_person_number = IColumn(db.VARCHAR(64), name='hr_manager_person_number')

    hr_subst_person_number = IColumn(db.VARCHAR(64), name='hr_subst_person_number')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    hr_subst_status = IColumn(HRStatus, nullable=False, name='hr_subst_status')

    hr_subst_message = IColumn(db.VARCHAR(64), name='hr_subst_message')

    hr_source_file = IColumn(db.VARCHAR(64), nullable=False, name='hr_source_file')

    hr_source_row = IColumn(db.Integer, nullable=False, name='hr_source_row')

    created_at = IColumn(db.Date, name='created_at')
    __To_update_info = Header(u'To_update_info')

    manager_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Hr_desktop_subst_manager_person_id'), name='manager_person_id')
    manager_person = IRelationship(lambda: DPerson, foreign_keys=[manager_person_id])

    subst_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Hr_desktop_subst_subst_person_id'), name='subst_person_id')
    subst_person = IRelationship(lambda: DPerson, foreign_keys=[subst_person_id])

    manager_org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_Hr_desktop_subst_manager_org_unit_manager_id'), name='manager_org_unit_manager_id')
    manager_org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[manager_org_unit_manager_id])

    substitube_org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_Hr_desktop_subst_substitube_org_unit_manager_id'), name='substitube_org_unit_manager_id')
    substitube_org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[substitube_org_unit_manager_id])

    substitute_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER_SUBST.id', use_alter=True, name='fk_Hr_desktop_subst_substitute_id'), name='substitute_id')
    substitute = IRelationship(lambda: IOrgUnitManagerSubstitute, foreign_keys=[substitute_id])

    def to_named_tuple(self):
        return HrDesktopSubstTuple(id=self.id,hr_manager_person_number=self.hr_manager_person_number,hr_subst_person_number=self.hr_subst_person_number,starting_date=self.starting_date,termination_date=self.termination_date,hr_subst_status=self.hr_subst_status,hr_subst_message=self.hr_subst_message,hr_source_file=self.hr_source_file,hr_source_row=self.hr_source_row,created_at=self.created_at,manager_person_id=self.manager_person_id,subst_person_id=self.subst_person_id,manager_org_unit_manager_id=self.manager_org_unit_manager_id,substitube_org_unit_manager_id=self.substitube_org_unit_manager_id,substitute_id=self.substitute_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return HrDesktopSubstTuple(id=self.id,hr_manager_person_number=self.hr_manager_person_number,hr_subst_person_number=self.hr_subst_person_number,starting_date=self.starting_date,termination_date=self.termination_date,hr_subst_status=self.hr_subst_status,hr_subst_message=self.hr_subst_message,hr_source_file=self.hr_source_file,hr_source_row=self.hr_source_row,created_at=self.created_at,manager_person_id=self.manager_person_id,subst_person_id=self.subst_person_id,manager_org_unit_manager_id=self.manager_org_unit_manager_id,substitube_org_unit_manager_id=self.substitube_org_unit_manager_id,substitute_id=self.substitute_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

HrImportRecordTuple = namedtuple('HrImportRecordTuple',  ('id', 'entity', 'source', 'row', 'source_entity_id', 'mapped_entity_id', 'system_entity', 'system_entity_id', 'parent_entity', 'parent_source_entity_id', 'parent_record_id', 'parent_system_entity', 'parent_system_entity_id', 'display_name', 'error_code', 'error_json', 'previous_valid_hr_record_json', 'current_hr_record_json', 'fixed_record_json', 'fixed_attributes_json', 'mapped_attributes_json', 'correctable_error', 'imported_to_db', 'hr_status', 'previous_record_version_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class HrImportRecord(API,HrImportRecordMixin, Base, db.Model):
    __tablename__ = 'HR_IMPORT_RECORD'
    __entity_name__ = 'Hr_import_record'
    __plain_object__ = HrImportRecordPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    entity = IColumn(db.VARCHAR(32), nullable=False, name='entity')

    source = IColumn(db.VARCHAR(150), nullable=False, name='source')

    row = IColumn(db.Integer, nullable=False, name='row')

    source_entity_id = IColumn(BigInt, name='source_entity_id')

    mapped_entity_id = IColumn(db.TEXT, name='mapped_entity_id')

    system_entity = IColumn(db.TEXT, name='system_entity')

    system_entity_id = IColumn(BigInt, name='system_entity_id')

    parent_entity = IColumn(db.VARCHAR(32), name='parent_entity')

    parent_source_entity_id = IColumn(BigInt, name='parent_source_entity_id')

    parent_record_id = IColumn(BigInt, db.ForeignKey('HR_IMPORT_RECORD.id', use_alter=True, name='fk_Hr_import_record_parent_record_id'), name='parent_record_id')
    parent_record = IRelationship(lambda: HrImportRecord, foreign_keys=[parent_record_id], remote_side=[id])

    parent_system_entity = IColumn(db.TEXT, name='parent_system_entity')

    parent_system_entity_id = IColumn(BigInt, name='parent_system_entity_id')

    display_name = IColumn(db.TEXT, name='display_name')

    error_code = IColumn(db.TEXT, name='error_code')

    error_json = IColumn(db.TEXT, name='error_json')

    previous_valid_hr_record_json = IColumn(db.TEXT, name='previous_valid_hr_record_json')

    current_hr_record_json = IColumn(db.TEXT, name='current_hr_record_json')

    fixed_record_json = IColumn(db.TEXT, name='fixed_record_json')

    fixed_attributes_json = IColumn(db.TEXT, name='fixed_attributes_json')

    mapped_attributes_json = IColumn(db.TEXT, name='mapped_attributes_json')

    correctable_error = IColumn(CharBool, nullable=False, name='correctable_error')

    imported_to_db = IColumn(CharBool, nullable=False, name='imported_to_db')

    hr_status = IColumn(HRStatus, nullable=False, name='hr_status')

    previous_record_version_id = IColumn(BigInt, name='previous_record_version_id')

    def to_named_tuple(self):
        return HrImportRecordTuple(id=self.id,entity=self.entity,source=self.source,row=self.row,source_entity_id=self.source_entity_id,mapped_entity_id=self.mapped_entity_id,system_entity=self.system_entity,system_entity_id=self.system_entity_id,parent_entity=self.parent_entity,parent_source_entity_id=self.parent_source_entity_id,parent_record_id=self.parent_record_id,parent_system_entity=self.parent_system_entity,parent_system_entity_id=self.parent_system_entity_id,display_name=self.display_name,error_code=self.error_code,error_json=self.error_json,previous_valid_hr_record_json=self.previous_valid_hr_record_json,current_hr_record_json=self.current_hr_record_json,fixed_record_json=self.fixed_record_json,fixed_attributes_json=self.fixed_attributes_json,mapped_attributes_json=self.mapped_attributes_json,correctable_error=self.correctable_error,imported_to_db=self.imported_to_db,hr_status=self.hr_status,previous_record_version_id=self.previous_record_version_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return HrImportRecordTuple(id=self.id,entity=self.entity,source=self.source,row=self.row,source_entity_id=self.source_entity_id,mapped_entity_id=self.mapped_entity_id,system_entity=self.system_entity,system_entity_id=self.system_entity_id,parent_entity=self.parent_entity,parent_source_entity_id=self.parent_source_entity_id,parent_record_id=self.parent_record_id,parent_system_entity=self.parent_system_entity,parent_system_entity_id=self.parent_system_entity_id,display_name=self.display_name,error_code=self.error_code,error_json=self.error_json,previous_valid_hr_record_json=self.previous_valid_hr_record_json,current_hr_record_json=self.current_hr_record_json,fixed_record_json=self.fixed_record_json,fixed_attributes_json=self.fixed_attributes_json,mapped_attributes_json=self.mapped_attributes_json,correctable_error=self.correctable_error,imported_to_db=self.imported_to_db,hr_status=self.hr_status,previous_record_version_id=self.previous_record_version_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

HrIntegrationTuple = namedtuple('HrIntegrationTuple',  ('id', 'person_id', 'external_person_id', 'internal', 'last_name', 'first_names', 'person_number', 'social_security_number', 'username', 'email', 'jobtitle_id', 'hr_job_title', 'hr_official_job_title', 'orgunit_id', 'ext_org_id', 'legal_company_id', 'cost_center_id', 'location_id', 'hire_start_date', 'job_start_date', 'job_end_date', 'manager_id', 'org_unit_manager_id', 'phone', 'pupo', 'other_address', 'sv_number', 'hr_status', 'preferred_name', 'street_address', 'post_number', 'city', 'hr_profession_code', 'position_type', 'hr_work_time_type', 'job_type', 'hr_job_type', 'full_part_per', 'job_period_character', 'language_id', 'report_area', 'report_manager', 'report_manager_id', 'org_association_type', 'ext_email', 'ext_phone', 'ext_manager_id', 'ext_manager_hetu', 'ext_manager_name', 'ext_org_code', 'ext_org_contract_number', 'ext_org_name', 'orgunit_name', 'manager_hetu', 'manager_name', 'basic_applications', 'other_data', 'iloq_identifier', 'other_key_1', 'other_key_2', 'personnel_card', 'iloq_valid_till', 'additional_admittances', 'additional_admittances_validity', 'additional_information_1', 'identifier', 'valid_till', 'trans_date', 'batch_file_name', 'batch_messages', 'record_source', 'hr_language_lookup', 'hr_language_description', 'hr_job_period_id', 'hr_job_title_id', 'hr_department_id', 'hr_manager_id', 'is_manager', 'job_position_type', 'job_position', 'job_period_type', 'job_period_type_text', 'job_period_character_text', 'person_number2', 'integration_timestamp', 'pass2done', 'c_pasu', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class HrIntegration(API,HrIntegrationMixin, Base, db.Model):
    __tablename__ = 'HR_INTEGRATION'
    __entity_name__ = 'Hr_integration'
    __plain_object__ = HrIntegrationPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    __block1 = Header(u'block1')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Hr_integration_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_Hr_integration_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    internal = IColumn(CharBool, nullable=False, name='internal')

    last_name = IColumn(db.VARCHAR(64), nullable=False, name='surname')

    first_names = IColumn(db.VARCHAR(64), nullable=False, name='first_names')

    person_number = IColumn(db.VARCHAR(64), name='person_number')

    social_security_number = IColumn(db.VARCHAR(64), name='social_security_number')

    username = IColumn(db.VARCHAR(64), name='username')

    email = IColumn(db.VARCHAR(64), name='email')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_Hr_integration_jobtitle_id'), name='jobtitle_id')
    jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    hr_job_title = IColumn(db.VARCHAR(64), name='hr_job_title')

    hr_official_job_title = IColumn(db.VARCHAR(64), name='hr_official_job_title')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_Hr_integration_org_unit_id'), name='org_unit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    ext_org_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_Hr_integration_ext_org_id'), name='ext_org_id')
    ext_org = IRelationship(lambda: EExtOrg, foreign_keys=[ext_org_id])

    legal_company_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_Hr_integration_legal_company_id'), name='legal_company_id')
    legal_company = IRelationship(lambda: ILegalCompany, foreign_keys=[legal_company_id])

    cost_center_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_Hr_integration_cost_center_id'), name='cost_center_id')
    cost_center = IRelationship(lambda: ICostCenter, foreign_keys=[cost_center_id])

    location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_Hr_integration_location_id'), name='location_id')
    location = IRelationship(lambda: ILocation, foreign_keys=[location_id])

    hire_start_date = IColumn(db.Date, name='hire_start_date')

    job_start_date = IColumn(db.Date, name='job_start_date')

    job_end_date = IColumn(db.Date, name='job_end_date')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Hr_integration_manager_id'), name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_Hr_integration_org_unit_manager_id'), name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    phone = IColumn(db.VARCHAR(64), name='phone')

    pupo = IColumn(db.VARCHAR(4), name='voice_address')

    other_address = IColumn(db.VARCHAR(256), name='other_address')

    sv_number = IColumn(db.VARCHAR(10), name='sv_number')

    hr_status = IColumn(HRStatus, name='hr_status')
    __block2 = Header(u'block2')

    preferred_name = IColumn(db.VARCHAR(64), name='preferred_name')

    street_address = IColumn(db.VARCHAR(64), name='street_address')

    post_number = IColumn(db.VARCHAR(64), name='post_number')

    city = IColumn(db.VARCHAR(64), name='city')

    hr_profession_code = IColumn(HRProfessionCode, name='hr_profession_code')

    position_type = IColumn(PositionType, name='position_type')

    hr_work_time_type = IColumn(HRWorkTimeType, name='hr_work_time_type_lookup')

    job_type = IColumn(JobType, name='job_type')

    hr_job_type = IColumn(HRJobType, name='hr_job_type')

    full_part_per = IColumn(db.Float, name='full_part_per')

    job_period_character = IColumn(JpCharacter, name='jp_character')

    language_id = IColumn(BigInt, db.ForeignKey('G_LANGUAGE.id', use_alter=True, name='fk_Hr_integration_language_id'), name='language_id')
    language = IRelationship(lambda: GLanguage, foreign_keys=[language_id])

    report_area = IColumn(db.VARCHAR(250), name='report_area')

    report_manager = IColumn(db.VARCHAR(64), name='report_manager')

    report_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Hr_integration_report_manager_id'), name='report_manager_id')
    _report_manager = IRelationship(lambda: DPerson, foreign_keys=[report_manager_id])
    __exts = Header(u'exts')

    org_association_type = IColumn(OrgAssociationType, name='org_association_type')

    ext_email = IColumn(db.VARCHAR(64), name='ext_email')

    ext_phone = IColumn(db.VARCHAR(64), name='ext_phone')

    ext_manager_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_Hr_integration_ext_manager_id'), name='ext_manager_id')
    ext_manager = IRelationship(lambda: EExternalPerson, foreign_keys=[ext_manager_id])

    ext_manager_hetu = IColumn(db.VARCHAR(11), name='ext_manager_hetu')

    ext_manager_name = IColumn(db.VARCHAR(256), name='ext_manager_name')

    ext_org_code = IColumn(db.VARCHAR(64), name='ext_org_code')

    ext_org_contract_number = IColumn(db.VARCHAR(64), name='ext_org_contract_number')

    ext_org_name = IColumn(db.VARCHAR(256), name='ext_org_name')

    orgunit_name = IColumn(db.VARCHAR(256), name='orgunit_name')

    manager_hetu = IColumn(db.VARCHAR(11), name='manager_hetu')

    manager_name = IColumn(db.VARCHAR(256), name='manager_name')

    basic_applications = IColumn(CharBool, nullable=False, name='basic_applications')

    other_data = IColumn(db.VARCHAR(1024), name='other_data')
    __admittances = Header(u'admittances')

    iloq_identifier = IColumn(db.VARCHAR(64), name='iloq_identifier')

    other_key_1 = IColumn(db.VARCHAR(64), name='other_key_1')

    other_key_2 = IColumn(db.VARCHAR(64), name='other_key_2')

    personnel_card = IColumn(CharBool, nullable=False, name='personnel_card')

    iloq_valid_till = IColumn(db.Date, name='iloq_valid_till')

    additional_admittances = IColumn(db.VARCHAR(512), name='additional_admittances')

    additional_admittances_validity = IColumn(db.Date, name='additional_admittances_validity')

    additional_information_1 = IColumn(db.VARCHAR(512), name='additional_information_1')

    identifier = IColumn(db.VARCHAR(64), name='identifier')

    valid_till = IColumn(db.Date, name='valid_till')
    __batch_info = Header(u'batch_info')

    trans_date = IColumn(db.Date, name='trans_date')

    batch_file_name = IColumn(db.VARCHAR(64), name='batch_file_name')

    batch_messages = IColumn(db.VARCHAR(4096), name='batch_messages')

    record_source = IColumn(db.VARCHAR(64), name='record_source')

    hr_language_lookup = IColumn(HRLanguageLookup, name='hr_language_lookup')

    hr_language_description = IColumn(db.VARCHAR(64), name='hr_language_description')

    hr_job_period_id = IColumn(db.VARCHAR(64), name='hr_job_period_id')

    hr_job_title_id = IColumn(db.VARCHAR(64), name='hr_job_title_id')

    hr_department_id = IColumn(db.VARCHAR(64), name='hr_department_id')

    hr_manager_id = IColumn(db.VARCHAR(64), name='hr_manager_id')

    is_manager = IColumn(CharBool, nullable=False, name='is_manager')

    job_position_type = IColumn(JobPositionType, name='job_position_type')

    job_position = IColumn(db.VARCHAR(64), name='job_position')

    job_period_type = IColumn(JPType, name='jp_type')

    job_period_type_text = IColumn(db.VARCHAR(64), name='jp_type_text')

    job_period_character_text = IColumn(db.VARCHAR(64), name='jp_character_text')

    person_number2 = IColumn(db.VARCHAR(64), name='person_number2')

    integration_timestamp = IColumn(db.DateTime, name='integration_timestamp')

    pass2done = IColumn(CharBool, nullable=False, name='pass2done')

    c_pasu = IColumn(CharBool, nullable=False, name='c_pasu')
    service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: HrIntegrationGServiceRole, uselist=True)
    other_organization_units = IRelationship(lambda: IOrgUnit, secondary=lambda: HrIntegrationIOrgUnit, uselist=True)
    key_profiles = IRelationship(lambda: CKeyProfile, secondary=lambda: HrIntegrationCKeyProfile, uselist=True)

    def to_named_tuple(self):
        return HrIntegrationTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,internal=self.internal,last_name=self.last_name,first_names=self.first_names,person_number=self.person_number,social_security_number=self.social_security_number,username=self.username,email=self.email,jobtitle_id=self.jobtitle_id,hr_job_title=self.hr_job_title,hr_official_job_title=self.hr_official_job_title,orgunit_id=self.orgunit_id,ext_org_id=self.ext_org_id,legal_company_id=self.legal_company_id,cost_center_id=self.cost_center_id,location_id=self.location_id,hire_start_date=self.hire_start_date,job_start_date=self.job_start_date,job_end_date=self.job_end_date,manager_id=self.manager_id,org_unit_manager_id=self.org_unit_manager_id,phone=self.phone,pupo=self.pupo,other_address=self.other_address,sv_number=self.sv_number,hr_status=self.hr_status,preferred_name=self.preferred_name,street_address=self.street_address,post_number=self.post_number,city=self.city,hr_profession_code=self.hr_profession_code,position_type=self.position_type,hr_work_time_type=self.hr_work_time_type,job_type=self.job_type,hr_job_type=self.hr_job_type,full_part_per=self.full_part_per,job_period_character=self.job_period_character,language_id=self.language_id,report_area=self.report_area,report_manager=self.report_manager,report_manager_id=self.report_manager_id,org_association_type=self.org_association_type,ext_email=self.ext_email,ext_phone=self.ext_phone,ext_manager_id=self.ext_manager_id,ext_manager_hetu=self.ext_manager_hetu,ext_manager_name=self.ext_manager_name,ext_org_code=self.ext_org_code,ext_org_contract_number=self.ext_org_contract_number,ext_org_name=self.ext_org_name,orgunit_name=self.orgunit_name,manager_hetu=self.manager_hetu,manager_name=self.manager_name,basic_applications=self.basic_applications,other_data=self.other_data,iloq_identifier=self.iloq_identifier,other_key_1=self.other_key_1,other_key_2=self.other_key_2,personnel_card=self.personnel_card,iloq_valid_till=self.iloq_valid_till,additional_admittances=self.additional_admittances,additional_admittances_validity=self.additional_admittances_validity,additional_information_1=self.additional_information_1,identifier=self.identifier,valid_till=self.valid_till,trans_date=self.trans_date,batch_file_name=self.batch_file_name,batch_messages=self.batch_messages,record_source=self.record_source,hr_language_lookup=self.hr_language_lookup,hr_language_description=self.hr_language_description,hr_job_period_id=self.hr_job_period_id,hr_job_title_id=self.hr_job_title_id,hr_department_id=self.hr_department_id,hr_manager_id=self.hr_manager_id,is_manager=self.is_manager,job_position_type=self.job_position_type,job_position=self.job_position,job_period_type=self.job_period_type,job_period_type_text=self.job_period_type_text,job_period_character_text=self.job_period_character_text,person_number2=self.person_number2,integration_timestamp=self.integration_timestamp,pass2done=self.pass2done,c_pasu=self.c_pasu,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return HrIntegrationTuple(id=self.id,person_id=self.person_id,external_person_id=self.external_person_id,internal=self.internal,last_name=self.last_name,first_names=self.first_names,person_number=self.person_number,social_security_number=self.social_security_number,username=self.username,email=self.email,jobtitle_id=self.jobtitle_id,hr_job_title=self.hr_job_title,hr_official_job_title=self.hr_official_job_title,orgunit_id=self.orgunit_id,ext_org_id=self.ext_org_id,legal_company_id=self.legal_company_id,cost_center_id=self.cost_center_id,location_id=self.location_id,hire_start_date=self.hire_start_date,job_start_date=self.job_start_date,job_end_date=self.job_end_date,manager_id=self.manager_id,org_unit_manager_id=self.org_unit_manager_id,phone=self.phone,pupo=self.pupo,other_address=self.other_address,sv_number=self.sv_number,hr_status=self.hr_status,preferred_name=self.preferred_name,street_address=self.street_address,post_number=self.post_number,city=self.city,hr_profession_code=self.hr_profession_code,position_type=self.position_type,hr_work_time_type=self.hr_work_time_type,job_type=self.job_type,hr_job_type=self.hr_job_type,full_part_per=self.full_part_per,job_period_character=self.job_period_character,language_id=self.language_id,report_area=self.report_area,report_manager=self.report_manager,report_manager_id=self.report_manager_id,org_association_type=self.org_association_type,ext_email=self.ext_email,ext_phone=self.ext_phone,ext_manager_id=self.ext_manager_id,ext_manager_hetu=self.ext_manager_hetu,ext_manager_name=self.ext_manager_name,ext_org_code=self.ext_org_code,ext_org_contract_number=self.ext_org_contract_number,ext_org_name=self.ext_org_name,orgunit_name=self.orgunit_name,manager_hetu=self.manager_hetu,manager_name=self.manager_name,basic_applications=self.basic_applications,other_data=self.other_data,iloq_identifier=self.iloq_identifier,other_key_1=self.other_key_1,other_key_2=self.other_key_2,personnel_card=self.personnel_card,iloq_valid_till=self.iloq_valid_till,additional_admittances=self.additional_admittances,additional_admittances_validity=self.additional_admittances_validity,additional_information_1=self.additional_information_1,identifier=self.identifier,valid_till=self.valid_till,trans_date=self.trans_date,batch_file_name=self.batch_file_name,batch_messages=self.batch_messages,record_source=self.record_source,hr_language_lookup=self.hr_language_lookup,hr_language_description=self.hr_language_description,hr_job_period_id=self.hr_job_period_id,hr_job_title_id=self.hr_job_title_id,hr_department_id=self.hr_department_id,hr_manager_id=self.hr_manager_id,is_manager=self.is_manager,job_position_type=self.job_position_type,job_position=self.job_position,job_period_type=self.job_period_type,job_period_type_text=self.job_period_type_text,job_period_character_text=self.job_period_character_text,person_number2=self.person_number2,integration_timestamp=self.integration_timestamp,pass2done=self.pass2done,c_pasu=self.c_pasu,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

HrIntegrationVaultTuple = namedtuple('HrIntegrationVaultTuple',  ('id', 'name', 'description', 'loaded', 'dumped', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class HrIntegrationVault(API,HrIntegrationVaultMixin, Base, db.Model):
    __tablename__ = 'HR_INTEGRATION_VAULT'
    __entity_name__ = 'Hr_integration_vault'
    __plain_object__ = HrIntegrationVaultPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    loaded = IColumn(db.VARCHAR(64), name='loaded')

    dumped = IColumn(db.VARCHAR(64), name='dumped')

    def to_named_tuple(self):
        return HrIntegrationVaultTuple(id=self.id,name=self.name,description=self.description,loaded=self.loaded,dumped=self.dumped,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return HrIntegrationVaultTuple(id=self.id,name=self.name,description=self.description,loaded=self.loaded,dumped=self.dumped,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IBusinessAreaTuple = namedtuple('IBusinessAreaTuple',  ('id', 'code', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IBusinessArea(API,IBusinessAreaMixin, Base, db.Model):
    __tablename__ = 'O_I_BUSINESS_AREA'
    __entity_name__ = 'I_business_area'
    __plain_object__ = IBusinessAreaPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    code = IColumn(db.VARCHAR(16), nullable=False, name='code')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return IBusinessAreaTuple(id=self.id,code=self.code,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IBusinessAreaTuple(id=self.id,code=self.code,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ICostCenterTuple = namedtuple('ICostCenterTuple',  ('id', 'legalcompany_id', 'header_row', 'int_code', 'name', 'description', 'starting_date', 'termination_date', 'status', 'classification1', 'classification2', 'classification3', 'classification4', 'classification5', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ICostCenter(API,ICostCenterMixin, Base, db.Model):
    __tablename__ = 'O_I_COST_CENTER'
    __entity_name__ = 'I_cost_center'
    __plain_object__ = ICostCenterPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    legalcompany_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_I_cost_center_legalcompany_id'), name='legalcompany_id')
    legalcompany = IRelationship(lambda: ILegalCompany, foreign_keys=[legalcompany_id])

    header_row = IColumn(CharBool, nullable=False, name='header_row')

    int_code = IColumn(db.VARCHAR(64), name='int_code')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    status = IColumn(Status, name='status')

    classification1 = IColumn(db.VARCHAR(64), name='classification1')

    classification2 = IColumn(db.VARCHAR(64), name='classification2')

    classification3 = IColumn(db.VARCHAR(64), name='classification3')

    classification4 = IColumn(db.VARCHAR(64), name='classification4')

    classification5 = IColumn(db.VARCHAR(64), name='classification5')

    def to_named_tuple(self):
        return ICostCenterTuple(id=self.id,legalcompany_id=self.legalcompany_id,header_row=self.header_row,int_code=self.int_code,name=self.name,description=self.description,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,classification4=self.classification4,classification5=self.classification5,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ICostCenterTuple(id=self.id,legalcompany_id=self.legalcompany_id,header_row=self.header_row,int_code=self.int_code,name=self.name,description=self.description,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,classification1=self.classification1,classification2=self.classification2,classification3=self.classification3,classification4=self.classification4,classification5=self.classification5,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IJobFamilyTuple = namedtuple('IJobFamilyTuple',  ('id', 'name', 'int_code', 'description', 'starting_date', 'termination_date', 'jobfamily_class1', 'jobfamily_class2', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IJobFamily(API,IJobFamilyMixin, Base, db.Model):
    __tablename__ = 'I_JOB_FAMILY'
    __entity_name__ = 'I_job_family'
    __plain_object__ = IJobFamilyPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    int_code = IColumn(db.VARCHAR(32), name='int_code')

    description = IColumn(db.TEXT, name='description')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    jobfamily_class1 = IColumn(db.VARCHAR(64), name='jobfamily_class1')

    jobfamily_class2 = IColumn(db.VARCHAR(64), name='jobfamily_class2')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return IJobFamilyTuple(id=self.id,name=self.name,int_code=self.int_code,description=self.description,starting_date=self.starting_date,termination_date=self.termination_date,jobfamily_class1=self.jobfamily_class1,jobfamily_class2=self.jobfamily_class2,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IJobFamilyTuple(id=self.id,name=self.name,int_code=self.int_code,description=self.description,starting_date=self.starting_date,termination_date=self.termination_date,jobfamily_class1=self.jobfamily_class1,jobfamily_class2=self.jobfamily_class2,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IJobRoleTuple = namedtuple('IJobRoleTuple',  ('id', 'name', 'name6', 'int_code', 'description', 'global_jobrole', 'inheritance', 'orgunit_id', 'org_spec', 'upper_jobrole_id', 'starting_date', 'termination_date', 'jobrole_class1', 'jobrole_class2', 'jobfamily_id', 'status', 'org_group_id', 'favorite', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IJobRole(API,ClosureTableMixin,IJobRoleMixin, Base, db.Model):
    __tablename__ = 'O_I_JOB_ROLE'
    __entity_name__ = 'I_job_role'
    __plain_object__ = IJobRolePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    name6 = IColumn(db.VARCHAR(64), name='name6')

    int_code = IColumn(db.VARCHAR(32), name='int_code')

    description = IColumn(db.TEXT, name='description')

    global_jobrole = IColumn(CharBool, nullable=False, name='global_jobrole')

    inheritance = IColumn(CharBool, nullable=False, name='inheritance')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_job_role_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    org_spec = IColumn(OrgSpec, name='org_spec')

    upper_jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_job_role_upper_jobrole_id'), name='upper_jobrole_id')
    parent = IRelationship(lambda: IJobRole, foreign_keys=[upper_jobrole_id], remote_side=[id])

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    jobrole_class1 = IColumn(db.VARCHAR(64), name='jobrole_class1')

    jobrole_class2 = IColumn(db.VARCHAR(64), name='jobrole_class2')

    jobfamily_id = IColumn(BigInt, db.ForeignKey('I_JOB_FAMILY.id', use_alter=True, name='fk_I_job_role_jobfamily_id'), name='jobfamily_id')
    jobfamily = IRelationship(lambda: IJobFamily, foreign_keys=[jobfamily_id])

    status = IColumn(Status, name='status')

    org_group_id = IColumn(BigInt, db.ForeignKey('I_ORG_GROUP.id', use_alter=True, name='fk_I_job_role_org_group_id'), name='org_group_id')
    org_group = IRelationship(lambda: IOrgGroup, foreign_keys=[org_group_id])

    favorite = IColumn(CharBool, nullable=False, name='favorite')
    service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: IJobRoleGServiceRole, uselist=True)
    requestable_service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: IJobRoleReqGServiceRole, uselist=True)
    job_titles = IRelationship(lambda: DJobtitle, foreign_keys=lambda: [DJobtitle.jobrole_id], uselist=True)

    def to_named_tuple(self):
        return IJobRoleTuple(id=self.id,name=self.name,name6=self.name6,int_code=self.int_code,description=self.description,global_jobrole=self.global_jobrole,inheritance=self.inheritance,orgunit_id=self.orgunit_id,org_spec=self.org_spec,upper_jobrole_id=self.upper_jobrole_id,starting_date=self.starting_date,termination_date=self.termination_date,jobrole_class1=self.jobrole_class1,jobrole_class2=self.jobrole_class2,jobfamily_id=self.jobfamily_id,status=self.status,org_group_id=self.org_group_id,favorite=self.favorite,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IJobRoleTuple(id=self.id,name=self.name,name6=self.name6,int_code=self.int_code,description=self.description,global_jobrole=self.global_jobrole,inheritance=self.inheritance,orgunit_id=self.orgunit_id,org_spec=self.org_spec,upper_jobrole_id=self.upper_jobrole_id,starting_date=self.starting_date,termination_date=self.termination_date,jobrole_class1=self.jobrole_class1,jobrole_class2=self.jobrole_class2,jobfamily_id=self.jobfamily_id,status=self.status,org_group_id=self.org_group_id,favorite=self.favorite,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IJobRoleCtAllTuple = namedtuple('IJobRoleCtAllTuple',  ('ancestor', 'descendant'  ))

class IJobRoleCtAll(IJobRoleCtAllMixin, db.Model):
    __tablename__ = 'I_JOB_ROLE_CT_ALL'
    __entity_name__ = 'I_job_role_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_job_role_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_job_role_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_job_role_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_job_role_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return IJobRoleCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return IJobRoleCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

ILegalCompanyTuple = namedtuple('ILegalCompanyTuple',  ('id', 'name', 'description', 'official_company_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ILegalCompany(API,ILegalCompanyMixin, Base, db.Model):
    __tablename__ = 'O_I_LEGAL_COMPANY'
    __entity_name__ = 'I_legal_company'
    __plain_object__ = ILegalCompanyPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    official_company_id = IColumn(db.VARCHAR(64), name='official_company_id')

    status = IColumn(Status, name='status')
    services = IRelationship(lambda: GService, secondary=lambda: ILegalCompanyGService, uselist=True)
    service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: ILegalCompanyGServiceRole, uselist=True)

    def to_named_tuple(self):
        return ILegalCompanyTuple(id=self.id,name=self.name,description=self.description,official_company_id=self.official_company_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ILegalCompanyTuple(id=self.id,name=self.name,description=self.description,official_company_id=self.official_company_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ILocationTuple = namedtuple('ILocationTuple',  ('id', 'name', 'description', 'upper_location_id', 'header_row', 'location_id', 'site_category', 'virtual_location', 'status', 'street', 'street2', 'post', 'city', 'state', 'country', 'office_phone', 'office_fax', 'office_timezone', 'site_manager_id', 'site_manager_name', 'site_manager_email', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ILocation(API,ClosureTableMixin,ILocationMixin, Base, db.Model):
    __tablename__ = 'O_I_LOCATION'
    __entity_name__ = 'I_location'
    __plain_object__ = ILocationPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    upper_location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_I_location_upper_location_id'), name='upper_location_id')
    parent = IRelationship(lambda: ILocation, foreign_keys=[upper_location_id], remote_side=[id])

    header_row = IColumn(CharBool, nullable=False, name='header_row')

    location_id = IColumn(db.VARCHAR(64), name='location_id')

    site_category = IColumn(SiteCategory, name='site_category')

    virtual_location = IColumn(CharBool, nullable=False, name='virtual_location')

    status = IColumn(Status, name='status')

    street = IColumn(db.VARCHAR(64), name='street')

    street2 = IColumn(db.VARCHAR(64), name='street2')

    post = IColumn(db.VARCHAR(64), name='post')

    city = IColumn(db.VARCHAR(64), name='city')

    state = IColumn(db.VARCHAR(64), name='state')

    country = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_I_location_country'), name='country')

    office_phone = IColumn(db.VARCHAR(64), name='office_phone')

    office_fax = IColumn(db.VARCHAR(64), name='office_fax')

    office_timezone = IColumn(db.VARCHAR(64), name='office_timezone')

    site_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_location_site_manager_id'), name='site_manager_id')
    site_manager = IRelationship(lambda: DPerson, foreign_keys=[site_manager_id])

    site_manager_name = IColumn(db.VARCHAR(64), name='site_manager_name')

    site_manager_email = IColumn(db.VARCHAR(64), name='site_manager_email')

    def to_named_tuple(self):
        return ILocationTuple(id=self.id,name=self.name,description=self.description,upper_location_id=self.upper_location_id,header_row=self.header_row,location_id=self.location_id,site_category=self.site_category,virtual_location=self.virtual_location,status=self.status,street=self.street,street2=self.street2,post=self.post,city=self.city,state=self.state,country=self.country,office_phone=self.office_phone,office_fax=self.office_fax,office_timezone=self.office_timezone,site_manager_id=self.site_manager_id,site_manager_name=self.site_manager_name,site_manager_email=self.site_manager_email,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ILocationTuple(id=self.id,name=self.name,description=self.description,upper_location_id=self.upper_location_id,header_row=self.header_row,location_id=self.location_id,site_category=self.site_category,virtual_location=self.virtual_location,status=self.status,street=self.street,street2=self.street2,post=self.post,city=self.city,state=self.state,country=self.country,office_phone=self.office_phone,office_fax=self.office_fax,office_timezone=self.office_timezone,site_manager_id=self.site_manager_id,site_manager_name=self.site_manager_name,site_manager_email=self.site_manager_email,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ILocationCtAllTuple = namedtuple('ILocationCtAllTuple',  ('ancestor', 'descendant'  ))

class ILocationCtAll(ILocationCtAllMixin, db.Model):
    __tablename__ = 'I_LOCATION_CT_ALL'
    __entity_name__ = 'I_location_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_I_location_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_I_location_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_I_location_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_I_location_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return ILocationCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return ILocationCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

IManagerPerProfessionTuple = namedtuple('IManagerPerProfessionTuple',  ('id', 'orgunit_id', 'hr_profession_code', 'i_job_role_id', 'e_job_role_id', 'superior_person_id', 'superior_name', 'superior_email', 'subst_s_person_id', 'subst_s_name', 'subst_s_email', 'substitute_active', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IManagerPerProfession(API,IManagerPerProfessionMixin, Base, db.Model):
    __tablename__ = 'I_MANAGER_PER_PROFESSION'
    __entity_name__ = 'I_manager_per_profession'
    __plain_object__ = IManagerPerProfessionPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_manager_per_profession_orgunit_id'), nullable=False, name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    hr_profession_code = IColumn(HRProfessionCode, nullable=False, name='hr_profession_code')

    i_job_role_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_manager_per_profession_i_job_role_id'), name='i_job_role_id')
    i_job_role = IRelationship(lambda: IJobRole, foreign_keys=[i_job_role_id])

    e_job_role_id = IColumn(BigInt, db.ForeignKey('O_E_JOB_ROLE.id', use_alter=True, name='fk_I_manager_per_profession_e_job_role_id'), name='e_job_role_id')
    e_job_role = IRelationship(lambda: EJobRole, foreign_keys=[e_job_role_id])

    superior_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_manager_per_profession_superior_person_id'), name='superior_person_id')
    superior_person = IRelationship(lambda: DPerson, foreign_keys=[superior_person_id])

    superior_name = IColumn(db.VARCHAR(64), name='superior_name')

    superior_email = IColumn(db.VARCHAR(64), name='superior_email')

    subst_s_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_manager_per_profession_subst_s_person_id'), name='subst_s_person_id')
    subst_s_person = IRelationship(lambda: DPerson, foreign_keys=[subst_s_person_id])

    subst_s_name = IColumn(db.VARCHAR(64), name='subst_s_name')

    subst_s_email = IColumn(db.VARCHAR(64), name='subst_s_email')

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')

    def to_named_tuple(self):
        return IManagerPerProfessionTuple(id=self.id,orgunit_id=self.orgunit_id,hr_profession_code=self.hr_profession_code,i_job_role_id=self.i_job_role_id,e_job_role_id=self.e_job_role_id,superior_person_id=self.superior_person_id,superior_name=self.superior_name,superior_email=self.superior_email,subst_s_person_id=self.subst_s_person_id,subst_s_name=self.subst_s_name,subst_s_email=self.subst_s_email,substitute_active=self.substitute_active,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IManagerPerProfessionTuple(id=self.id,orgunit_id=self.orgunit_id,hr_profession_code=self.hr_profession_code,i_job_role_id=self.i_job_role_id,e_job_role_id=self.e_job_role_id,superior_person_id=self.superior_person_id,superior_name=self.superior_name,superior_email=self.superior_email,subst_s_person_id=self.subst_s_person_id,subst_s_name=self.subst_s_name,subst_s_email=self.subst_s_email,substitute_active=self.substitute_active,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IOrgGroupTuple = namedtuple('IOrgGroupTuple',  ('id', 'name', 'description', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IOrgGroup(API,IOrgGroupMixin, Base, db.Model):
    __tablename__ = 'I_ORG_GROUP'
    __entity_name__ = 'I_org_group'
    __plain_object__ = IOrgGroupPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    description = IColumn(db.TEXT, name='description')
    organization_groups = IRelationship(lambda: IOrgUnit, secondary=lambda: IOrgUnitIOrgGroup, uselist=True)

    def to_named_tuple(self):
        return IOrgGroupTuple(id=self.id,name=self.name,description=self.description,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IOrgGroupTuple(id=self.id,name=self.name,description=self.description,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IOrgTypeTuple = namedtuple('IOrgTypeTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IOrgType(API,IOrgTypeMixin, Base, db.Model):
    __tablename__ = 'O_I_ORG_TYPE'
    __entity_name__ = 'I_org_type'
    __plain_object__ = IOrgTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return IOrgTypeTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IOrgTypeTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IOrgUnitTuple = namedtuple('IOrgUnitTuple',  ('id', 'name', 'name6', 'description', 'upper_orgunit_id', 'unit_id', 'orgtype_id', 'inheritance', 'header_row', 'pilot', 'org_level', 'virtual_unit', 'businessarea', 'legalcompany_id', 'costcenter_id', 'location_id', 'it_support_email', 'favorite', 'starting_date', 'termination_date', 'status', 'org_spec', 'unit_id_1', 'unit_id_2', 'financial_code_1', 'location_info', 'exc_street', 'exc_street2', 'exc_post', 'exc_city', 'exc_state', 'exc_country', 'exc_office_phone', 'exc_office_fax', 'exc_office_timezone', 'exc_site_category', 'manager_id', 'superior_name', 'superior_email', 'subst_manager_id', 'subst_s_name', 'subst_s_email', 'substitute_active', 'teamleader_person_id', 'teamleader_name', 'teamleader_email', 'hr_manager_person_id', 'hr_manager_name', 'hr_manager_email', 'default_language_id', 'default_jobrole_id', 'default_domain', 'provisioning_dirty', 'distinguishedname', 'codeserver_oid', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IOrgUnit(API,ClosureTableMixin,IOrgUnitMixin, Base, db.Model):
    __tablename__ = 'O_I_ORG_UNIT'
    __entity_name__ = 'I_org_unit'
    __plain_object__ = IOrgUnitPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(256), nullable=False, name='name')

    name6 = IColumn(db.VARCHAR(64), name='name6')

    description = IColumn(db.TEXT, name='description')

    upper_orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_org_unit_upper_orgunit_id'), name='upper_orgunit_id')
    parent = IRelationship(lambda: IOrgUnit, foreign_keys=[upper_orgunit_id], remote_side=[id])

    unit_id = IColumn(db.VARCHAR(64), name='unit_id')

    orgtype_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_TYPE.id', use_alter=True, name='fk_I_org_unit_orgtype_id'), name='orgtype_id')
    orgtype = IRelationship(lambda: IOrgType, foreign_keys=[orgtype_id])

    inheritance = IColumn(CharBool, nullable=False, name='inheritance')
    __org_info = Header(u'org_info')

    header_row = IColumn(CharBool, nullable=False, name='header_row')

    pilot = IColumn(CharBool, nullable=False, name='pilot')

    org_level = IColumn(OrgLevel, name='org_level')

    virtual_unit = IColumn(VirtualUnit, name='virtual_unit')

    businessarea = IColumn(BigInt, db.ForeignKey('O_I_BUSINESS_AREA.id', use_alter=True, name='fk_I_org_unit_businessarea'), name='businessarea')

    legalcompany_id = IColumn(BigInt, db.ForeignKey('O_I_LEGAL_COMPANY.id', use_alter=True, name='fk_I_org_unit_legalcompany_id'), name='legalcompany_id')
    legalcompany = IRelationship(lambda: ILegalCompany, foreign_keys=[legalcompany_id])

    costcenter_id = IColumn(BigInt, db.ForeignKey('O_I_COST_CENTER.id', use_alter=True, name='fk_I_org_unit_costcenter_id'), name='costcenter_id')
    costcenter = IRelationship(lambda: ICostCenter, foreign_keys=[costcenter_id])

    location_id = IColumn(BigInt, db.ForeignKey('O_I_LOCATION.id', use_alter=True, name='fk_I_org_unit_location_id'), name='location_id')
    location = IRelationship(lambda: ILocation, foreign_keys=[location_id])

    it_support_email = IColumn(db.VARCHAR(64), name='it_support_email')

    favorite = IColumn(CharBool, nullable=False, name='favorite')
    __activation_info = Header(u'activation_info')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    status = IColumn(Status, name='status')
    __additional_classification = Header(u'additional_classification')

    org_spec = IColumn(OrgSpec, name='org_spec')

    unit_id_1 = IColumn(db.VARCHAR(64), name='unit_id_1')

    unit_id_2 = IColumn(db.VARCHAR(64), name='unit_id_2')

    financial_code_1 = IColumn(db.VARCHAR(64), name='financial_code_1')
    __office_info = Header(u'office_info')

    location_info = IColumn(db.VARCHAR(64), name='location_info')

    exc_street = IColumn(db.VARCHAR(64), name='exc_street')

    exc_street2 = IColumn(db.VARCHAR(64), name='exc_street2')

    exc_post = IColumn(db.VARCHAR(64), name='exc_post')

    exc_city = IColumn(db.VARCHAR(64), name='exc_city')

    exc_state = IColumn(db.VARCHAR(64), name='exc_state')

    exc_country = IColumn(BigInt, db.ForeignKey('G_COUNTRY.id', use_alter=True, name='fk_I_org_unit_exc_country'), name='exc_country')

    exc_office_phone = IColumn(db.VARCHAR(64), name='exc_office_phone')

    exc_office_fax = IColumn(db.VARCHAR(64), name='exc_office_fax')

    exc_office_timezone = IColumn(db.VARCHAR(64), name='exc_office_timezone')

    exc_site_category = IColumn(SiteCategory, name='exc_site_category')
    __responsible_persons = Header(u'responsible_persons')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_org_unit_superior_person_id'), name='superior_person_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    superior_name = IColumn(db.VARCHAR(64), name='superior_name')

    superior_email = IColumn(db.VARCHAR(64), name='superior_email')

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_org_unit_subst_s_person_id'), name='subst_s_person_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id])

    subst_s_name = IColumn(db.VARCHAR(64), name='subst_s_name')

    subst_s_email = IColumn(db.VARCHAR(64), name='subst_s_email')

    substitute_active = IColumn(CharBool, nullable=False, name='substitute_active')

    teamleader_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_org_unit_teamleader_person_id'), name='teamleader_person_id')
    teamleader_person = IRelationship(lambda: DPerson, foreign_keys=[teamleader_person_id])

    teamleader_name = IColumn(db.VARCHAR(64), name='teamleader_name')

    teamleader_email = IColumn(db.VARCHAR(64), name='teamleader_email')

    hr_manager_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_org_unit_hr_manager_person_id'), name='hr_manager_person_id')
    hr_manager_person = IRelationship(lambda: DPerson, foreign_keys=[hr_manager_person_id])

    hr_manager_name = IColumn(db.VARCHAR(64), name='hr_manager_name')

    hr_manager_email = IColumn(db.VARCHAR(64), name='hr_manager_email')
    __defaults = Header(u'defaults')

    default_language_id = IColumn(BigInt, db.ForeignKey('G_LANGUAGE.id', use_alter=True, name='fk_I_org_unit_default_language_id'), name='default_language_id')
    default_language = IRelationship(lambda: GLanguage, foreign_keys=[default_language_id])

    default_jobrole_id = IColumn(BigInt, db.ForeignKey('O_I_JOB_ROLE.id', use_alter=True, name='fk_I_org_unit_default_jobrole_id'), name='default_jobrole_id')
    default_jobrole = IRelationship(lambda: IJobRole, foreign_keys=[default_jobrole_id])

    default_domain = IColumn(db.VARCHAR(64), name='default_domain')
    job_periods = IRelationship(lambda: DJobPeriod, foreign_keys=lambda: [DJobPeriod.orgunit_id], uselist=True)
    external_job_periods = IRelationship(lambda: EJobPeriod, foreign_keys=lambda: [EJobPeriod.orgunit_id], uselist=True)

    provisioning_dirty = IColumn(CharBool, nullable=False, name='provisioning_dirty')

    distinguishedname = IColumn(db.VARCHAR(512), name='distinguishedname')
    requestable_services = IRelationship(lambda: GService, secondary=lambda: IOrgUnitGService, uselist=True)
    predefined_service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: IOrgUnitGServiceRole, uselist=True)

    codeserver_oid = IColumn(db.VARCHAR(512), name='codeserver_oid')

    def to_named_tuple(self):
        return IOrgUnitTuple(id=self.id,name=self.name,name6=self.name6,description=self.description,upper_orgunit_id=self.upper_orgunit_id,unit_id=self.unit_id,orgtype_id=self.orgtype_id,inheritance=self.inheritance,header_row=self.header_row,pilot=self.pilot,org_level=self.org_level,virtual_unit=self.virtual_unit,businessarea=self.businessarea,legalcompany_id=self.legalcompany_id,costcenter_id=self.costcenter_id,location_id=self.location_id,it_support_email=self.it_support_email,favorite=self.favorite,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,org_spec=self.org_spec,unit_id_1=self.unit_id_1,unit_id_2=self.unit_id_2,financial_code_1=self.financial_code_1,location_info=self.location_info,exc_street=self.exc_street,exc_street2=self.exc_street2,exc_post=self.exc_post,exc_city=self.exc_city,exc_state=self.exc_state,exc_country=self.exc_country,exc_office_phone=self.exc_office_phone,exc_office_fax=self.exc_office_fax,exc_office_timezone=self.exc_office_timezone,exc_site_category=self.exc_site_category,manager_id=self.manager_id,superior_name=self.superior_name,superior_email=self.superior_email,subst_manager_id=self.subst_manager_id,subst_s_name=self.subst_s_name,subst_s_email=self.subst_s_email,substitute_active=self.substitute_active,teamleader_person_id=self.teamleader_person_id,teamleader_name=self.teamleader_name,teamleader_email=self.teamleader_email,hr_manager_person_id=self.hr_manager_person_id,hr_manager_name=self.hr_manager_name,hr_manager_email=self.hr_manager_email,default_language_id=self.default_language_id,default_jobrole_id=self.default_jobrole_id,default_domain=self.default_domain,provisioning_dirty=self.provisioning_dirty,distinguishedname=self.distinguishedname,codeserver_oid=self.codeserver_oid,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IOrgUnitTuple(id=self.id,name=self.name,name6=self.name6,description=self.description,upper_orgunit_id=self.upper_orgunit_id,unit_id=self.unit_id,orgtype_id=self.orgtype_id,inheritance=self.inheritance,header_row=self.header_row,pilot=self.pilot,org_level=self.org_level,virtual_unit=self.virtual_unit,businessarea=self.businessarea,legalcompany_id=self.legalcompany_id,costcenter_id=self.costcenter_id,location_id=self.location_id,it_support_email=self.it_support_email,favorite=self.favorite,starting_date=self.starting_date,termination_date=self.termination_date,status=self.status,org_spec=self.org_spec,unit_id_1=self.unit_id_1,unit_id_2=self.unit_id_2,financial_code_1=self.financial_code_1,location_info=self.location_info,exc_street=self.exc_street,exc_street2=self.exc_street2,exc_post=self.exc_post,exc_city=self.exc_city,exc_state=self.exc_state,exc_country=self.exc_country,exc_office_phone=self.exc_office_phone,exc_office_fax=self.exc_office_fax,exc_office_timezone=self.exc_office_timezone,exc_site_category=self.exc_site_category,manager_id=self.manager_id,superior_name=self.superior_name,superior_email=self.superior_email,subst_manager_id=self.subst_manager_id,subst_s_name=self.subst_s_name,subst_s_email=self.subst_s_email,substitute_active=self.substitute_active,teamleader_person_id=self.teamleader_person_id,teamleader_name=self.teamleader_name,teamleader_email=self.teamleader_email,hr_manager_person_id=self.hr_manager_person_id,hr_manager_name=self.hr_manager_name,hr_manager_email=self.hr_manager_email,default_language_id=self.default_language_id,default_jobrole_id=self.default_jobrole_id,default_domain=self.default_domain,provisioning_dirty=self.provisioning_dirty,distinguishedname=self.distinguishedname,codeserver_oid=self.codeserver_oid,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IOrgUnitCtAllTuple = namedtuple('IOrgUnitCtAllTuple',  ('ancestor', 'descendant'  ))

class IOrgUnitCtAll(IOrgUnitCtAllMixin, db.Model):
    __tablename__ = 'I_ORG_UNIT_CT_ALL'
    __entity_name__ = 'I_org_unit_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_org_unit_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_org_unit_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_org_unit_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_org_unit_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return IOrgUnitCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return IOrgUnitCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

IOrgUnitManagerTuple = namedtuple('IOrgUnitManagerTuple',  ('id', 'org_unit_id', 'manager_id', 'manager_type', 'activation_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IOrgUnitManager(API,IOrgUnitManagerMixin, Base, db.Model):
    __tablename__ = 'I_ORG_UNIT_MANAGER'
    __entity_name__ = 'I_org_unit_manager'
    __plain_object__ = IOrgUnitManagerPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    org_unit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_I_org_unit_manager_org_unit_id'), nullable=False, name='org_unit_id')
    org_unit = IRelationship(lambda: IOrgUnit, foreign_keys=[org_unit_id])

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_org_unit_manager_manager_id'), nullable=False, name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    manager_type = IColumn(ManagerType, nullable=False, name='manager_type')
    substitutes = IRelationship(lambda: IOrgUnitManagerSubstitute, foreign_keys=lambda: [IOrgUnitManagerSubstitute.org_unit_manager_id], uselist=True)

    activation_date = IColumn(db.Date, name='activation_date')

    def to_named_tuple(self):
        return IOrgUnitManagerTuple(id=self.id,org_unit_id=self.org_unit_id,manager_id=self.manager_id,manager_type=self.manager_type,activation_date=self.activation_date,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IOrgUnitManagerTuple(id=self.id,org_unit_id=self.org_unit_id,manager_id=self.manager_id,manager_type=self.manager_type,activation_date=self.activation_date,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

IOrgUnitManagerSubstituteTuple = namedtuple('IOrgUnitManagerSubstituteTuple',  ('id', 'org_unit_manager_id', 'subst_manager_id', 'start_date', 'end_date', 'hr_desktop_subst', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class IOrgUnitManagerSubstitute(API,IOrgUnitManagerSubstituteMixin, Base, db.Model):
    __tablename__ = 'I_ORG_UNIT_MANAGER_SUBST'
    __entity_name__ = 'I_org_unit_manager_subst'
    __plain_object__ = IOrgUnitManagerSubstitutePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_I_org_unit_manager_subst_org_unit_manager_id'), nullable=False, name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    subst_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_I_org_unit_manager_subst_subst_manager_id'), nullable=False, name='subst_manager_id')
    subst_manager = IRelationship(lambda: DPerson, foreign_keys=[subst_manager_id])

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    hr_desktop_subst = IColumn(BigInt, db.ForeignKey('HR_DESKTOP_SUBST.id', use_alter=True, name='fk_I_org_unit_manager_subst_hr_desktop_subst'), name='hr_desktop_subst')

    def to_named_tuple(self):
        return IOrgUnitManagerSubstituteTuple(id=self.id,org_unit_manager_id=self.org_unit_manager_id,subst_manager_id=self.subst_manager_id,start_date=self.start_date,end_date=self.end_date,hr_desktop_subst=self.hr_desktop_subst,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return IOrgUnitManagerSubstituteTuple(id=self.id,org_unit_manager_id=self.org_unit_manager_id,subst_manager_id=self.subst_manager_id,start_date=self.start_date,end_date=self.end_date,hr_desktop_subst=self.hr_desktop_subst,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

LoginChallengeTuple = namedtuple('LoginChallengeTuple',  ('id', 'zuser_id', 'challenge', 'timestamp', 'user_agent', 'url', 'remote_addr', 'status'  ))

class LoginChallenge(LoginChallengeMixin, db.Model):
    __tablename__ = 'LOGIN_CHALLENGE'
    __entity_name__ = 'Login_challenge'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    zuser_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Login_challenge_zuser_id'), name='zuser_id')
    zuser = IRelationship(lambda: Zuser, foreign_keys=[zuser_id])

    challenge = IColumn(db.VARCHAR(256), name='challenge')

    timestamp = IColumn(db.DateTime, name='timestamp')

    user_agent = IColumn(db.TEXT, name='user_agent')

    url = IColumn(db.VARCHAR(2000), name='url')

    remote_addr = IColumn(db.VARCHAR(45), name='remote_addr')

    status = IColumn(db.Integer, name='status')

    def to_named_tuple(self):
        return LoginChallengeTuple(id=self.id,zuser_id=self.zuser_id,challenge=self.challenge,timestamp=self.timestamp,user_agent=self.user_agent,url=self.url,remote_addr=self.remote_addr,status=self.status,)

    def to_plain_object(self):
        return LoginChallengeTuple(id=self.id,zuser_id=self.zuser_id,challenge=self.challenge,timestamp=self.timestamp,user_agent=self.user_agent,url=self.url,remote_addr=self.remote_addr,status=self.status,)

OneTimeLinkTuple = namedtuple('OneTimeLinkTuple',  ('id', 'auth_token', 'entity_name', 'entity_id', 'expires', 'created_timestamp', 'used_timestamp', 'zuser_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class OneTimeLink(API,OneTimeLinkMixin, Base, db.Model):
    __tablename__ = 'ONE_TIME_LINK'
    __entity_name__ = 'One_time_link'
    __plain_object__ = OneTimeLinkPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    auth_token = IColumn(db.VARCHAR(64), name='auth_token')

    entity_name = IColumn(db.VARCHAR(64), name='entity_name')

    entity_id = IColumn(BigInt, name='entity_id')

    expires = IColumn(db.Date, name='expires')

    created_timestamp = IColumn(db.DateTime, name='created_timestamp')

    used_timestamp = IColumn(db.DateTime, name='used_timestamp')

    zuser_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_One_time_link_zuser_id'), name='zuser_id')
    zuser = IRelationship(lambda: Zuser, foreign_keys=[zuser_id])

    def to_named_tuple(self):
        return OneTimeLinkTuple(id=self.id,auth_token=self.auth_token,entity_name=self.entity_name,entity_id=self.entity_id,expires=self.expires,created_timestamp=self.created_timestamp,used_timestamp=self.used_timestamp,zuser_id=self.zuser_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return OneTimeLinkTuple(id=self.id,auth_token=self.auth_token,entity_name=self.entity_name,entity_id=self.entity_id,expires=self.expires,created_timestamp=self.created_timestamp,used_timestamp=self.used_timestamp,zuser_id=self.zuser_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

PRequestCartTuple = namedtuple('PRequestCartTuple',  ('id', 'job_period_id', 'e_job_period_id', 'social_security_number', 'person_id', 'external_person_id', 'internal', 'request_ssn', 'requestor_id', 'starting_date', 'manager_ssn', 'description', 'preferred_implementor_ssn', 'inform_user', 'inform_superior', 'inform_others', 'src_trans_date', 'status_in', 'request_cart_id', 'e_request_cart_id', 'hr_job_period_id', 'out_status', 'out_status_error_msg', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class PRequestCart(API,PRequestCartMixin, Base, db.Model):
    __tablename__ = 'P_REQUEST_CART'
    __entity_name__ = 'P_request_cart'
    __plain_object__ = PRequestCartPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_P_request_cart_job_period_id'), name='job_period_id')
    job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[job_period_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_P_request_cart_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    social_security_number = IColumn(db.VARCHAR(64), name='social_security_number')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_P_request_cart_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_P_request_cart_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    internal = IColumn(CharBool, nullable=False, name='internal')

    request_ssn = IColumn(db.VARCHAR(64), name='request_ssn')

    requestor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_P_request_cart_requestor_id'), name='requestor_id')
    requestor = IRelationship(lambda: Zuser, foreign_keys=[requestor_id])

    starting_date = IColumn(db.Date, name='starting_date')

    manager_ssn = IColumn(db.VARCHAR(64), name='manager_ssn')

    description = IColumn(db.TEXT, name='description')

    preferred_implementor_ssn = IColumn(db.VARCHAR(64), name='preferred_implementor_ssn')

    inform_user = IColumn(CharBool, nullable=False, name='inform_user')

    inform_superior = IColumn(CharBool, nullable=False, name='inform_superior')

    inform_others = IColumn(CharBool, nullable=False, name='inform_others')

    src_trans_date = IColumn(db.Date, name='src_trans_date')

    status_in = IColumn(db.Integer, name='status_in')

    request_cart_id = IColumn(BigInt, db.ForeignKey('REQUEST_CART.id', use_alter=True, name='fk_P_request_cart_request_cart_id'), name='request_cart_id')
    request_cart = IRelationship(lambda: RequestCart, foreign_keys=[request_cart_id])

    e_request_cart_id = IColumn(BigInt, db.ForeignKey('E_REQUEST_CART.id', use_alter=True, name='fk_P_request_cart_e_request_cart_id'), name='e_request_cart_id')
    e_request_cart = IRelationship(lambda: ERequestCart, foreign_keys=[e_request_cart_id])

    hr_job_period_id = IColumn(db.VARCHAR(64), name='hr_job_period_id')

    out_status = IColumn(db.Integer, name='out_status')

    out_status_error_msg = IColumn(db.VARCHAR(4096), name='out_status_error_msg')

    def to_named_tuple(self):
        return PRequestCartTuple(id=self.id,job_period_id=self.job_period_id,e_job_period_id=self.e_job_period_id,social_security_number=self.social_security_number,person_id=self.person_id,external_person_id=self.external_person_id,internal=self.internal,request_ssn=self.request_ssn,requestor_id=self.requestor_id,starting_date=self.starting_date,manager_ssn=self.manager_ssn,description=self.description,preferred_implementor_ssn=self.preferred_implementor_ssn,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,src_trans_date=self.src_trans_date,status_in=self.status_in,request_cart_id=self.request_cart_id,e_request_cart_id=self.e_request_cart_id,hr_job_period_id=self.hr_job_period_id,out_status=self.out_status,out_status_error_msg=self.out_status_error_msg,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return PRequestCartTuple(id=self.id,job_period_id=self.job_period_id,e_job_period_id=self.e_job_period_id,social_security_number=self.social_security_number,person_id=self.person_id,external_person_id=self.external_person_id,internal=self.internal,request_ssn=self.request_ssn,requestor_id=self.requestor_id,starting_date=self.starting_date,manager_ssn=self.manager_ssn,description=self.description,preferred_implementor_ssn=self.preferred_implementor_ssn,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,src_trans_date=self.src_trans_date,status_in=self.status_in,request_cart_id=self.request_cart_id,e_request_cart_id=self.e_request_cart_id,hr_job_period_id=self.hr_job_period_id,out_status=self.out_status,out_status_error_msg=self.out_status_error_msg,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

PRequestCartRowTuple = namedtuple('PRequestCartRowTuple',  ('id', 'p_request_cart_id', 'permission_request_type', 'service_role_id', 'description', 'preferred_implementor_ssn', 'status_in', 'source_system_name', 'source_system_id', 'out_status', 'out_date', 'request_cart_row_id', 'e_request_cart_row_id', 'out_status_process', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class PRequestCartRow(API,PRequestCartRowMixin, Base, db.Model):
    __tablename__ = 'P_REQUEST_CART_ROW'
    __entity_name__ = 'P_request_cart_row'
    __plain_object__ = PRequestCartRowPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    p_request_cart_id = IColumn(BigInt, db.ForeignKey('P_REQUEST_CART.id', use_alter=True, name='fk_P_request_cart_row_p_request_cart_id'), name='p_request_cart_id')
    p_request_cart = IRelationship(lambda: PRequestCart, foreign_keys=[p_request_cart_id])

    permission_request_type = IColumn(PermissionRequestType, nullable=False, name='permission_request_type')

    service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_P_request_cart_row_service_role_id'), name='service_role_id')
    service_role = IRelationship(lambda: GServiceRole, foreign_keys=[service_role_id])

    description = IColumn(db.TEXT, name='description')

    preferred_implementor_ssn = IColumn(db.VARCHAR(64), name='preferred_implementor_ssn')

    status_in = IColumn(db.Integer, name='status_in')

    source_system_name = IColumn(db.VARCHAR(64), name='source_system_name')

    source_system_id = IColumn(db.VARCHAR(64), name='source_system_id')

    out_status = IColumn(db.Integer, name='out_status')

    out_date = IColumn(db.Date, name='out_date')

    request_cart_row_id = IColumn(BigInt, db.ForeignKey('REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_P_request_cart_row_request_cart_row_id'), name='request_cart_row_id')
    request_cart_row = IRelationship(lambda: RequestCartPermission, foreign_keys=[request_cart_row_id])

    e_request_cart_row_id = IColumn(BigInt, db.ForeignKey('E_REQUEST_CART_PERMISSION.id', use_alter=True, name='fk_P_request_cart_row_e_request_cart_row_id'), name='e_request_cart_row_id')
    e_request_cart_row = IRelationship(lambda: ERequestCartPermission, foreign_keys=[e_request_cart_row_id])

    out_status_process = IColumn(db.Integer, name='out_status_process')

    def to_named_tuple(self):
        return PRequestCartRowTuple(id=self.id,p_request_cart_id=self.p_request_cart_id,permission_request_type=self.permission_request_type,service_role_id=self.service_role_id,description=self.description,preferred_implementor_ssn=self.preferred_implementor_ssn,status_in=self.status_in,source_system_name=self.source_system_name,source_system_id=self.source_system_id,out_status=self.out_status,out_date=self.out_date,request_cart_row_id=self.request_cart_row_id,e_request_cart_row_id=self.e_request_cart_row_id,out_status_process=self.out_status_process,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return PRequestCartRowTuple(id=self.id,p_request_cart_id=self.p_request_cart_id,permission_request_type=self.permission_request_type,service_role_id=self.service_role_id,description=self.description,preferred_implementor_ssn=self.preferred_implementor_ssn,status_in=self.status_in,source_system_name=self.source_system_name,source_system_id=self.source_system_id,out_status=self.out_status,out_date=self.out_date,request_cart_row_id=self.request_cart_row_id,e_request_cart_row_id=self.e_request_cart_row_id,out_status_process=self.out_status_process,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RDynRoleTuple = namedtuple('RDynRoleTuple',  ('id', 'name', 'description', 'rule', 'approval_status', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RDynRole(API,RDynRoleMixin, Base, db.Model):
    __tablename__ = 'O_R_DYN_ROLE'
    __entity_name__ = 'R_dyn_role'
    __plain_object__ = RDynRolePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    description = IColumn(db.TEXT, name='description')

    rule = IColumn(db.VARCHAR(1024), nullable=False, name='rule')

    approval_status = IColumn(ApprovalStatus, nullable=False, name='approval_status')

    status = IColumn(Status, name='status')
    service_roles = IRelationship(lambda: GServiceRole, secondary=lambda: RDynRoleGServiceRole, uselist=True)

    def to_named_tuple(self):
        return RDynRoleTuple(id=self.id,name=self.name,description=self.description,rule=self.rule,approval_status=self.approval_status,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RDynRoleTuple(id=self.id,name=self.name,description=self.description,rule=self.rule,approval_status=self.approval_status,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ROrgDacTuple = namedtuple('ROrgDacTuple',  ('id', 'orgunit_id', 'name', 'dedicated', 'key1_min_value', 'key1_max_value', 'key2_min_value', 'key2_max_value', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ROrgDac(API,ROrgDacMixin, Base, db.Model):
    __tablename__ = 'R_ORG_DAC'
    __entity_name__ = 'R_org_dac'
    __plain_object__ = ROrgDacPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_R_org_dac_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    name = IColumn(db.VARCHAR(64), name='name')

    dedicated = IColumn(CharBool, nullable=False, name='dedicated')

    key1_min_value = IColumn(db.VARCHAR(64), name='key1_min_value')

    key1_max_value = IColumn(db.VARCHAR(64), name='key1_max_value')

    key2_min_value = IColumn(db.VARCHAR(64), name='key2_min_value')

    key2_max_value = IColumn(db.VARCHAR(64), name='key2_max_value')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return ROrgDacTuple(id=self.id,orgunit_id=self.orgunit_id,name=self.name,dedicated=self.dedicated,key1_min_value=self.key1_min_value,key1_max_value=self.key1_max_value,key2_min_value=self.key2_min_value,key2_max_value=self.key2_max_value,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ROrgDacTuple(id=self.id,orgunit_id=self.orgunit_id,name=self.name,dedicated=self.dedicated,key1_min_value=self.key1_min_value,key1_max_value=self.key1_max_value,key2_min_value=self.key2_min_value,key2_max_value=self.key2_max_value,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ROrgServiceTuple = namedtuple('ROrgServiceTuple',  ('id', 'name', 'orgunit_id', 'service_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ROrgService(API,ROrgServiceMixin, Base, db.Model):
    __tablename__ = 'O_R_ORG_SERVICE'
    __entity_name__ = 'R_org_service'
    __plain_object__ = ROrgServicePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_R_org_service_orgunit_id'), nullable=False, name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_R_org_service_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    def to_named_tuple(self):
        return ROrgServiceTuple(id=self.id,name=self.name,orgunit_id=self.orgunit_id,service_id=self.service_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ROrgServiceTuple(id=self.id,name=self.name,orgunit_id=self.orgunit_id,service_id=self.service_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ROrgTypeServiceTuple = namedtuple('ROrgTypeServiceTuple',  ('id', 'name', 'org_type_id', 'service_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ROrgTypeService(API,ROrgTypeServiceMixin, Base, db.Model):
    __tablename__ = 'O_R_ORG_TYPE_SERVICE'
    __entity_name__ = 'R_org_type_service'
    __plain_object__ = ROrgTypeServicePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    org_type_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_TYPE.id', use_alter=True, name='fk_R_org_type_service_org_type_id'), nullable=False, name='org_type_id')
    org_type = IRelationship(lambda: IOrgType, foreign_keys=[org_type_id])

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_R_org_type_service_service_id'), nullable=False, name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    def to_named_tuple(self):
        return ROrgTypeServiceTuple(id=self.id,name=self.name,org_type_id=self.org_type_id,service_id=self.service_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ROrgTypeServiceTuple(id=self.id,name=self.name,org_type_id=self.org_type_id,service_id=self.service_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RSodExceptionTuple = namedtuple('RSodExceptionTuple',  ('id', 'internal', 'person_id', 'external_person_id', 'sod_rule_id', 'exc_approved', 'exc_approver_id', 'exc_approver_desc', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RSodException(API,RSodExceptionMixin, Base, db.Model):
    __tablename__ = 'R_SOD_EXCEPTION'
    __entity_name__ = 'R_sod_exception'
    __plain_object__ = RSodExceptionPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    internal = IColumn(CharBool, nullable=False, name='internal')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_R_sod_exception_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_R_sod_exception_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    sod_rule_id = IColumn(BigInt, db.ForeignKey('R_SOD_RULE.id', use_alter=True, name='fk_R_sod_exception_sod_rule_id'), nullable=False, name='sod_rule_id')
    sod_rule = IRelationship(lambda: RSodRule, foreign_keys=[sod_rule_id])

    exc_approved = IColumn(CharBool, nullable=False, name='exc_approved')

    exc_approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_R_sod_exception_exc_approver_id'), name='exc_approver_id')
    exc_approver = IRelationship(lambda: Zuser, foreign_keys=[exc_approver_id])

    exc_approver_desc = IColumn(db.VARCHAR(64), name='exc_approver_desc')

    def to_named_tuple(self):
        return RSodExceptionTuple(id=self.id,internal=self.internal,person_id=self.person_id,external_person_id=self.external_person_id,sod_rule_id=self.sod_rule_id,exc_approved=self.exc_approved,exc_approver_id=self.exc_approver_id,exc_approver_desc=self.exc_approver_desc,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RSodExceptionTuple(id=self.id,internal=self.internal,person_id=self.person_id,external_person_id=self.external_person_id,sod_rule_id=self.sod_rule_id,exc_approved=self.exc_approved,exc_approver_id=self.exc_approver_id,exc_approver_desc=self.exc_approver_desc,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RSodRuleTuple = namedtuple('RSodRuleTuple',  ('id', 'name', 'description', 'sod_rule_class_id', 'role1_id', 'role2_id', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RSodRule(API,RSodRuleMixin, Base, db.Model):
    __tablename__ = 'R_SOD_RULE'
    __entity_name__ = 'R_sod_rule'
    __plain_object__ = RSodRulePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    description = IColumn(db.TEXT, name='description')

    sod_rule_class_id = IColumn(BigInt, db.ForeignKey('R_SOD_RULE_CLASS.id', use_alter=True, name='fk_R_sod_rule_sod_rule_class_id'), nullable=False, name='sod_rule_class_id')
    sod_rule_class = IRelationship(lambda: RSodRuleClass, foreign_keys=[sod_rule_class_id])

    role1_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_R_sod_rule_role1_id'), nullable=False, name='role1_id')
    role1 = IRelationship(lambda: GServiceRole, foreign_keys=[role1_id])

    role2_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_R_sod_rule_role2_id'), nullable=False, name='role2_id')
    role2 = IRelationship(lambda: GServiceRole, foreign_keys=[role2_id])

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return RSodRuleTuple(id=self.id,name=self.name,description=self.description,sod_rule_class_id=self.sod_rule_class_id,role1_id=self.role1_id,role2_id=self.role2_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RSodRuleTuple(id=self.id,name=self.name,description=self.description,sod_rule_class_id=self.sod_rule_class_id,role1_id=self.role1_id,role2_id=self.role2_id,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RSodRuleClassTuple = namedtuple('RSodRuleClassTuple',  ('id', 'name', 'description', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RSodRuleClass(API,RSodRuleClassMixin, Base, db.Model):
    __tablename__ = 'R_SOD_RULE_CLASS'
    __entity_name__ = 'R_sod_rule_class'
    __plain_object__ = RSodRuleClassPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), name='name')

    description = IColumn(db.TEXT, name='description')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return RSodRuleClassTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RSodRuleClassTuple(id=self.id,name=self.name,description=self.description,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RUserDacTuple = namedtuple('RUserDacTuple',  ('id', 'person_id', 'name', 'dedicated', 'key1_min_value', 'key1_max_value', 'key2_min_value', 'key2_max_value', 'status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RUserDac(API,RUserDacMixin, Base, db.Model):
    __tablename__ = 'R_USER_DAC'
    __entity_name__ = 'R_user_dac'
    __plain_object__ = RUserDacPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_R_user_dac_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    name = IColumn(db.VARCHAR(64), name='name')

    dedicated = IColumn(CharBool, nullable=False, name='dedicated')

    key1_min_value = IColumn(db.VARCHAR(64), name='key1_min_value')

    key1_max_value = IColumn(db.VARCHAR(64), name='key1_max_value')

    key2_min_value = IColumn(db.VARCHAR(64), name='key2_min_value')

    key2_max_value = IColumn(db.VARCHAR(64), name='key2_max_value')

    status = IColumn(Status, name='status')

    def to_named_tuple(self):
        return RUserDacTuple(id=self.id,person_id=self.person_id,name=self.name,dedicated=self.dedicated,key1_min_value=self.key1_min_value,key1_max_value=self.key1_max_value,key2_min_value=self.key2_min_value,key2_max_value=self.key2_max_value,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RUserDacTuple(id=self.id,person_id=self.person_id,name=self.name,dedicated=self.dedicated,key1_min_value=self.key1_min_value,key1_max_value=self.key1_max_value,key2_min_value=self.key2_min_value,key2_max_value=self.key2_max_value,status=self.status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RequestCartTuple = namedtuple('RequestCartTuple',  ('id', 'person_id', 'job_period_id', 'requestor_id', 'starting_date', 'manager_id', 'request_type', 'reason', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'approval_status', 'approval_comment', 'subst_approver_id', 'subst_approver_email', 'forced_hidden', 'approver_id', 'auto_approved', 'approval_time', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_address', 'reject_email_sent', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RequestCart(API,RequestCartMixin, Base, db.Model):
    __tablename__ = 'REQUEST_CART'
    __entity_name__ = 'Request_cart'
    __plain_object__ = RequestCartPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Request_cart_person_id'), nullable=False, name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_Request_cart_job_period_id'), nullable=False, name='job_period_id')
    job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[job_period_id])

    requestor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_requestor_id'), nullable=False, name='requestor_id')
    requestor = IRelationship(lambda: Zuser, foreign_keys=[requestor_id])

    starting_date = IColumn(db.Date, nullable=False, name='starting_date')

    manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Request_cart_manager_id'), name='manager_id')
    manager = IRelationship(lambda: DPerson, foreign_keys=[manager_id])

    request_type = IColumn(RequestType, name='request_type')

    reason = IColumn(db.VARCHAR(256), name='reason')

    preferred_implementor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_preferred_implementor_id'), name='preferred_implementor_id')
    preferred_implementor = IRelationship(lambda: Zuser, foreign_keys=[preferred_implementor_id])

    inform_user = IColumn(CharBool, nullable=False, name='inform_user')

    inform_superior = IColumn(CharBool, nullable=False, name='inform_superior')

    inform_others = IColumn(CharBool, nullable=False, name='inform_others')
    __permissions = Header(u'permissions')

    permissions = IRelationship(lambda: RequestCartPermission, foreign_keys=lambda: [RequestCartPermission.request_cart_id], uselist=True)
    __approval_info = Header(u'approval_info')

    approval_status = IColumn(ApprovalStatus, nullable=False, name='approval_status')

    approval_comment = IColumn(db.VARCHAR(256), name='approval_comment')

    subst_approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_subst_approver_id'), name='subst_approver_id')
    subst_approver = IRelationship(lambda: Zuser, foreign_keys=[subst_approver_id])

    subst_approver_email = IColumn(db.VARCHAR(64), name='subst_approver_email')

    forced_hidden = IColumn(CharBool, nullable=False, name='forced_hidden')

    approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_approver_id'), name='approver_id')
    approver = IRelationship(lambda: Zuser, foreign_keys=[approver_id])

    auto_approved = IColumn(CharBool, nullable=False, name='auto_approved')

    approval_time = IColumn(db.DateTime, name='approval_time')
    __technical_info = Header(u'technical_info')

    first_email_sent = IColumn(db.DateTime, name='first_email_sent')

    last_email_sent = IColumn(db.DateTime, name='last_email_sent')

    email_counter = IColumn(db.Integer, name='email_counter')

    email_address = IColumn(db.VARCHAR(254), name='email_address')

    reject_email_sent = IColumn(db.DateTime, name='reject_email_sent')

    def to_named_tuple(self):
        return RequestCartTuple(id=self.id,person_id=self.person_id,job_period_id=self.job_period_id,requestor_id=self.requestor_id,starting_date=self.starting_date,manager_id=self.manager_id,request_type=self.request_type,reason=self.reason,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,approval_status=self.approval_status,approval_comment=self.approval_comment,subst_approver_id=self.subst_approver_id,subst_approver_email=self.subst_approver_email,forced_hidden=self.forced_hidden,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_time=self.approval_time,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_address=self.email_address,reject_email_sent=self.reject_email_sent,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RequestCartTuple(id=self.id,person_id=self.person_id,job_period_id=self.job_period_id,requestor_id=self.requestor_id,starting_date=self.starting_date,manager_id=self.manager_id,request_type=self.request_type,reason=self.reason,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,approval_status=self.approval_status,approval_comment=self.approval_comment,subst_approver_id=self.subst_approver_id,subst_approver_email=self.subst_approver_email,forced_hidden=self.forced_hidden,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_time=self.approval_time,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_address=self.email_address,reject_email_sent=self.reject_email_sent,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

RequestCartPermissionTuple = namedtuple('RequestCartPermissionTuple',  ('id', 'request_cart_id', 'person_id', 'service_role_id', 'requestor_id', 'request_activation_date', 'permission_request_type', 'service_id', 'description', 'preferred_implementor_id', 'inform_user', 'inform_superior', 'inform_others', 'start_date', 'end_date', 'period_yr', 'approval_status', 'approver_id', 'auto_approved', 'approval_timestamp', 'first_email_sent', 'last_email_sent', 'email_counter', 'email_to_user_sent', 'email_to_superior_sent', 'email_to_others_sent', 'email_to_service_manager_sent', 'email_to_requestor_sent', 'reject_email_sent', 'source_system_name', 'source_system_id', 'associated_orgunits_json', 'associated_ext_orgs_json', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class RequestCartPermission(API,RequestCartPermissionMixin, Base, db.Model):
    __tablename__ = 'REQUEST_CART_PERMISSION'
    __entity_name__ = 'Request_cart_permission'
    __plain_object__ = RequestCartPermissionPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    request_cart_id = IColumn(BigInt, db.ForeignKey('REQUEST_CART.id', use_alter=True, name='fk_Request_cart_permission_request_cart_id'), nullable=False, name='request_cart_id')
    request_cart = IRelationship(lambda: RequestCart, foreign_keys=[request_cart_id])

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Request_cart_permission_person_id'), nullable=False, name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    service_role_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE_ROLE.id', use_alter=True, name='fk_Request_cart_permission_service_role_id'), nullable=False, name='service_role_id')
    service_role = IRelationship(lambda: GServiceRole, foreign_keys=[service_role_id])

    requestor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_permission_requestor_id'), nullable=False, name='requestor_id')
    requestor = IRelationship(lambda: Zuser, foreign_keys=[requestor_id])

    request_activation_date = IColumn(db.DateTime, name='request_activation_date')

    permission_request_type = IColumn(PermissionRequestType, nullable=False, name='permission_request_type')

    service_id = IColumn(BigInt, db.ForeignKey('O_G_SERVICE.id', use_alter=True, name='fk_Request_cart_permission_service_id'), name='service_id')
    service = IRelationship(lambda: GService, foreign_keys=[service_id])

    description = IColumn(db.TEXT, name='description')

    preferred_implementor_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_permission_preferred_implementor_id'), name='preferred_implementor_id')
    preferred_implementor = IRelationship(lambda: Zuser, foreign_keys=[preferred_implementor_id])

    inform_user = IColumn(CharBool, nullable=False, name='inform_user')

    inform_superior = IColumn(CharBool, nullable=False, name='inform_superior')

    inform_others = IColumn(CharBool, nullable=False, name='inform_others')

    start_date = IColumn(db.Date, name='start_date')

    end_date = IColumn(db.Date, name='end_date')

    period_yr = IColumn(db.Integer, name='period_yr')
    __approvals = Header(u'approvals')

    approval_status = IColumn(ApprovalStatus, nullable=False, name='approval_status')

    approver_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Request_cart_permission_approver_id'), name='approver_id')
    approver = IRelationship(lambda: Zuser, foreign_keys=[approver_id])

    auto_approved = IColumn(CharBool, nullable=False, name='auto_approved')

    approval_timestamp = IColumn(db.DateTime, name='approval_timestamp')
    __technical_info = Header(u'technical_info')

    first_email_sent = IColumn(db.DateTime, name='first_email_sent')

    last_email_sent = IColumn(db.DateTime, name='last_email_sent')

    email_counter = IColumn(db.Integer, name='email_counter')

    email_to_user_sent = IColumn(db.Integer, name='email_to_user_sent')

    email_to_superior_sent = IColumn(db.Integer, name='email_to_superior_sent')

    email_to_others_sent = IColumn(db.Integer, name='email_to_others_sent')

    email_to_service_manager_sent = IColumn(db.Integer, name='email_to_service_manager_sent')

    email_to_requestor_sent = IColumn(db.Integer, name='email_to_requestor_sent')

    reject_email_sent = IColumn(db.DateTime, name='reject_email_sent')

    source_system_name = IColumn(db.VARCHAR(64), name='source_system_name')

    source_system_id = IColumn(db.VARCHAR(64), name='source_system_id')

    associated_orgunits_json = IColumn(db.TEXT, name='associated_orgunits_json')

    associated_ext_orgs_json = IColumn(db.TEXT, name='associated_ext_orgs_json')
    informed_persons = IRelationship(lambda: DPerson, secondary=lambda: RequestCartPermissionDPerson, uselist=True)

    def to_named_tuple(self):
        return RequestCartPermissionTuple(id=self.id,request_cart_id=self.request_cart_id,person_id=self.person_id,service_role_id=self.service_role_id,requestor_id=self.requestor_id,request_activation_date=self.request_activation_date,permission_request_type=self.permission_request_type,service_id=self.service_id,description=self.description,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,start_date=self.start_date,end_date=self.end_date,period_yr=self.period_yr,approval_status=self.approval_status,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_timestamp=self.approval_timestamp,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_to_user_sent=self.email_to_user_sent,email_to_superior_sent=self.email_to_superior_sent,email_to_others_sent=self.email_to_others_sent,email_to_service_manager_sent=self.email_to_service_manager_sent,email_to_requestor_sent=self.email_to_requestor_sent,reject_email_sent=self.reject_email_sent,source_system_name=self.source_system_name,source_system_id=self.source_system_id,associated_orgunits_json=self.associated_orgunits_json,associated_ext_orgs_json=self.associated_ext_orgs_json,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return RequestCartPermissionTuple(id=self.id,request_cart_id=self.request_cart_id,person_id=self.person_id,service_role_id=self.service_role_id,requestor_id=self.requestor_id,request_activation_date=self.request_activation_date,permission_request_type=self.permission_request_type,service_id=self.service_id,description=self.description,preferred_implementor_id=self.preferred_implementor_id,inform_user=self.inform_user,inform_superior=self.inform_superior,inform_others=self.inform_others,start_date=self.start_date,end_date=self.end_date,period_yr=self.period_yr,approval_status=self.approval_status,approver_id=self.approver_id,auto_approved=self.auto_approved,approval_timestamp=self.approval_timestamp,first_email_sent=self.first_email_sent,last_email_sent=self.last_email_sent,email_counter=self.email_counter,email_to_user_sent=self.email_to_user_sent,email_to_superior_sent=self.email_to_superior_sent,email_to_others_sent=self.email_to_others_sent,email_to_service_manager_sent=self.email_to_service_manager_sent,email_to_requestor_sent=self.email_to_requestor_sent,reject_email_sent=self.reject_email_sent,source_system_name=self.source_system_name,source_system_id=self.source_system_id,associated_orgunits_json=self.associated_orgunits_json,associated_ext_orgs_json=self.associated_ext_orgs_json,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDDepartmentWeekMaxQuantityTuple = namedtuple('SDDepartmentWeekMaxQuantityTuple',  ('id', 'department_id', 'week', 'quantity', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class SDDepartmentWeekMaxQuantity(API,SDDepartmentWeekMaxQuantityMixin, Base, db.Model):
    __tablename__ = 'SD_DEPARTMENT_WEEK_MAX_QUANTITY'
    __entity_name__ = 'SD_department_week_max_quantity'
    __plain_object__ = SDDepartmentWeekMaxQuantityPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    department_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_SD_department_week_max_quantity_department_id'), name='department_id')
    department = IRelationship(lambda: IOrgUnit, foreign_keys=[department_id])

    week = IColumn(db.Date, name='week')

    quantity = IColumn(db.SmallInteger, nullable=False, name='quantity')

    def to_named_tuple(self):
        return SDDepartmentWeekMaxQuantityTuple(id=self.id,department_id=self.department_id,week=self.week,quantity=self.quantity,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return SDDepartmentWeekMaxQuantityTuple(id=self.id,department_id=self.department_id,week=self.week,quantity=self.quantity,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDStudyProgrammeTuple = namedtuple('SDStudyProgrammeTuple',  ('id', 'name', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class SDStudyProgramme(API,SDStudyProgrammeMixin, Base, db.Model):
    __tablename__ = 'SD_STUDY_PROGRAMME'
    __entity_name__ = 'SD_study_programme'
    __plain_object__ = SDStudyProgrammePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(300), nullable=False, name='name')

    def to_named_tuple(self):
        return SDStudyProgrammeTuple(id=self.id,name=self.name,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return SDStudyProgrammeTuple(id=self.id,name=self.name,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDTraineeshipPlacementTuple = namedtuple('SDTraineeshipPlacementTuple',  ('id', 'traineeship_placement_request_id', 'student_slot_number', 'part_number', 'department_id', 'start_date', 'end_date', 'coordinator_id', 'traineeship_type_id', 'responsible_person_id', 'guiding_teacher_id', 'student_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class SDTraineeshipPlacement(API,SDTraineeshipPlacementMixin, Base, db.Model):
    __tablename__ = 'SD_TRAINEESHIP_PLACEMENT'
    __entity_name__ = 'SD_traineeship_placement'
    __plain_object__ = SDTraineeshipPlacementPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    traineeship_placement_request_id = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_PLACEMENT_REQUEST.id', use_alter=True, name='fk_SD_traineeship_placement_traineeship_placement_request_id'), nullable=False, name='traineeship_placement_request_id')
    traineeship_placement_request = IRelationship(lambda: SDTraineeshipPlacementRequest, foreign_keys=[traineeship_placement_request_id])

    student_slot_number = IColumn(db.SmallInteger, nullable=False, name='student_slot_number')

    part_number = IColumn(db.SmallInteger, nullable=False, name='part_number')

    department_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_SD_traineeship_placement_department_id'), nullable=False, name='department_id')
    department = IRelationship(lambda: IOrgUnit, foreign_keys=[department_id])

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    coordinator_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_SD_traineeship_placement_coordinator_id'), nullable=False, name='coordinator_id')
    coordinator = IRelationship(lambda: Zuser, foreign_keys=[coordinator_id])

    traineeship_type_id = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_placement_traineeship_type_id'), name='traineeship_type_id')
    traineeship_type = IRelationship(lambda: SDTraineeshipType, foreign_keys=[traineeship_type_id])

    responsible_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_SD_traineeship_placement_responsible_person_id'), name='responsible_person_id')
    responsible_person = IRelationship(lambda: DPerson, foreign_keys=[responsible_person_id])

    guiding_teacher_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_SD_traineeship_placement_guiding_teacher_id'), name='guiding_teacher_id')
    guiding_teacher = IRelationship(lambda: EExternalPerson, foreign_keys=[guiding_teacher_id])

    student_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_SD_traineeship_placement_student_id'), name='student_id')
    student = IRelationship(lambda: EExternalPerson, foreign_keys=[student_id])

    def to_named_tuple(self):
        return SDTraineeshipPlacementTuple(id=self.id,traineeship_placement_request_id=self.traineeship_placement_request_id,student_slot_number=self.student_slot_number,part_number=self.part_number,department_id=self.department_id,start_date=self.start_date,end_date=self.end_date,coordinator_id=self.coordinator_id,traineeship_type_id=self.traineeship_type_id,responsible_person_id=self.responsible_person_id,guiding_teacher_id=self.guiding_teacher_id,student_id=self.student_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return SDTraineeshipPlacementTuple(id=self.id,traineeship_placement_request_id=self.traineeship_placement_request_id,student_slot_number=self.student_slot_number,part_number=self.part_number,department_id=self.department_id,start_date=self.start_date,end_date=self.end_date,coordinator_id=self.coordinator_id,traineeship_type_id=self.traineeship_type_id,responsible_person_id=self.responsible_person_id,guiding_teacher_id=self.guiding_teacher_id,student_id=self.student_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDTraineeshipPlacementRequestTuple = namedtuple('SDTraineeshipPlacementRequestTuple',  ('id', 'traineeship_request_id', 'office_id', 'division_id', 'department_id', 'semester_information', 'traineeship_type_id', 'traineeship_type_other', 'length_weeks', 'start_date', 'end_date', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class SDTraineeshipPlacementRequest(API,SDTraineeshipPlacementRequestMixin, Base, db.Model):
    __tablename__ = 'SD_TRAINEESHIP_PLACEMENT_REQUEST'
    __entity_name__ = 'SD_traineeship_placement_request'
    __plain_object__ = SDTraineeshipPlacementRequestPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    traineeship_request_id = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_REQUEST.id', use_alter=True, name='fk_SD_traineeship_placement_request_traineeship_request_id'), nullable=False, name='traineeship_request_id')
    traineeship_request = IRelationship(lambda: SDTraineeshipRequest, foreign_keys=[traineeship_request_id])

    office_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_SD_traineeship_placement_request_office_id'), nullable=False, name='office_id')
    office = IRelationship(lambda: IOrgUnit, foreign_keys=[office_id])

    division_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_SD_traineeship_placement_request_division_id'), name='division_id')
    division = IRelationship(lambda: IOrgUnit, foreign_keys=[division_id])

    department_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_SD_traineeship_placement_request_department_id'), name='department_id')
    department = IRelationship(lambda: IOrgUnit, foreign_keys=[department_id])

    semester_information = IColumn(db.VARCHAR(256), name='semester_information')

    traineeship_type_id = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_placement_request_traineeship_type_id'), name='traineeship_type_id')
    traineeship_type = IRelationship(lambda: SDTraineeshipType, foreign_keys=[traineeship_type_id])

    traineeship_type_other = IColumn(db.VARCHAR(400), name='traineeship_type_other')

    length_weeks = IColumn(db.SmallInteger, nullable=False, name='length_weeks')

    start_date = IColumn(db.Date, nullable=False, name='start_date')

    end_date = IColumn(db.Date, nullable=False, name='end_date')

    def to_named_tuple(self):
        return SDTraineeshipPlacementRequestTuple(id=self.id,traineeship_request_id=self.traineeship_request_id,office_id=self.office_id,division_id=self.division_id,department_id=self.department_id,semester_information=self.semester_information,traineeship_type_id=self.traineeship_type_id,traineeship_type_other=self.traineeship_type_other,length_weeks=self.length_weeks,start_date=self.start_date,end_date=self.end_date,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return SDTraineeshipPlacementRequestTuple(id=self.id,traineeship_request_id=self.traineeship_request_id,office_id=self.office_id,division_id=self.division_id,department_id=self.department_id,semester_information=self.semester_information,traineeship_type_id=self.traineeship_type_id,traineeship_type_other=self.traineeship_type_other,length_weeks=self.length_weeks,start_date=self.start_date,end_date=self.end_date,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDTraineeshipRequestTuple = namedtuple('SDTraineeshipRequestTuple',  ('id', 'school_id', 'study_programme_id', 'course_name', 'includes_skill_test', 'skill_test_type', 'advanced_course', 'international_student', 'international_school_name', 'extra_information', 'quantity_requested', 'request_status', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class SDTraineeshipRequest(API,SDTraineeshipRequestMixin, Base, db.Model):
    __tablename__ = 'SD_TRAINEESHIP_REQUEST'
    __entity_name__ = 'SD_traineeship_request'
    __plain_object__ = SDTraineeshipRequestPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    school_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_SD_traineeship_request_school_id'), nullable=False, name='school_id')
    school = IRelationship(lambda: EExtOrg, foreign_keys=[school_id])

    study_programme_id = IColumn(BigInt, db.ForeignKey('SD_STUDY_PROGRAMME.id', use_alter=True, name='fk_SD_traineeship_request_study_programme_id'), nullable=False, name='study_programme_id')
    study_programme = IRelationship(lambda: SDStudyProgramme, foreign_keys=[study_programme_id])

    course_name = IColumn(db.VARCHAR(300), name='course_name')

    includes_skill_test = IColumn(CharBool, nullable=False, name='includes_skill_test')

    skill_test_type = IColumn(SDSkillTestType, name='skill_test_type')

    advanced_course = IColumn(CharBool, nullable=False, name='advanced_course')

    international_student = IColumn(CharBool, nullable=False, name='international_student')

    international_school_name = IColumn(db.VARCHAR(300), name='international_school_name')

    extra_information = IColumn(db.VARCHAR(4000), name='extra_information')

    quantity_requested = IColumn(db.SmallInteger, name='quantity_requested')

    request_status = IColumn(SDRequestStatus, nullable=False, name='request_status')
    requests = IRelationship(lambda: SDTraineeshipPlacementRequest, foreign_keys=lambda: [SDTraineeshipPlacementRequest.traineeship_request_id], uselist=True)

    def to_named_tuple(self):
        return SDTraineeshipRequestTuple(id=self.id,school_id=self.school_id,study_programme_id=self.study_programme_id,course_name=self.course_name,includes_skill_test=self.includes_skill_test,skill_test_type=self.skill_test_type,advanced_course=self.advanced_course,international_student=self.international_student,international_school_name=self.international_school_name,extra_information=self.extra_information,quantity_requested=self.quantity_requested,request_status=self.request_status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return SDTraineeshipRequestTuple(id=self.id,school_id=self.school_id,study_programme_id=self.study_programme_id,course_name=self.course_name,includes_skill_test=self.includes_skill_test,skill_test_type=self.skill_test_type,advanced_course=self.advanced_course,international_student=self.international_student,international_school_name=self.international_school_name,extra_information=self.extra_information,quantity_requested=self.quantity_requested,request_status=self.request_status,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDTraineeshipTypeTuple = namedtuple('SDTraineeshipTypeTuple',  ('id', 'name', 'upper_traineeship_type_id', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class SDTraineeshipType(API,ClosureTableMixin,SDTraineeshipTypeMixin, Base, db.Model):
    __tablename__ = 'SD_TRAINEESHIP_TYPE'
    __entity_name__ = 'SD_traineeship_type'
    __plain_object__ = SDTraineeshipTypePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(300), nullable=False, name='name')

    upper_traineeship_type_id = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_type_upper_traineeship_type_id'), name='upper_traineeship_type_id')
    parent = IRelationship(lambda: SDTraineeshipType, foreign_keys=[upper_traineeship_type_id], remote_side=[id])

    def to_named_tuple(self):
        return SDTraineeshipTypeTuple(id=self.id,name=self.name,upper_traineeship_type_id=self.upper_traineeship_type_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return SDTraineeshipTypeTuple(id=self.id,name=self.name,upper_traineeship_type_id=self.upper_traineeship_type_id,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

SDTraineeshipTypeCtAllTuple = namedtuple('SDTraineeshipTypeCtAllTuple',  ('ancestor', 'descendant'  ))

class SDTraineeshipTypeCtAll(SDTraineeshipTypeCtAllMixin, db.Model):
    __tablename__ = 'SD_TRAINEESHIP_TYPE_CT_ALL'
    __entity_name__ = 'SD_traineeship_type_ct_all'
    __parent_entity__ = None

    ancestor = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_type_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_type_ct_all_descendant'), primary_key=True, name='descendant')

    ancestor = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_type_ct_all_ancestor'), primary_key=True, name='ancestor')

    descendant = IColumn(BigInt, db.ForeignKey('SD_TRAINEESHIP_TYPE.id', use_alter=True, name='fk_SD_traineeship_type_ct_all_descendant'), primary_key=True, name='descendant')

    def to_named_tuple(self):
        return SDTraineeshipTypeCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

    def to_plain_object(self):
        return SDTraineeshipTypeCtAllTuple(ancestor=self.ancestor,descendant=self.descendant,)

TokenBlocklistTuple = namedtuple('TokenBlocklistTuple',  ('id', 'zuser_id', 'jti', 'timestamp'  ))

class TokenBlocklist(TokenBlocklistMixin, db.Model):
    __tablename__ = 'TOKEN_BLOCKLIST'
    __entity_name__ = 'Token_blocklist'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    zuser_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Token_blocklist_zuser_id'), name='zuser_id')
    zuser = IRelationship(lambda: Zuser, foreign_keys=[zuser_id])

    jti = IColumn(db.VARCHAR(36), name='jti')

    timestamp = IColumn(db.DateTime, name='timestamp')

    def to_named_tuple(self):
        return TokenBlocklistTuple(id=self.id,zuser_id=self.zuser_id,jti=self.jti,timestamp=self.timestamp,)

    def to_plain_object(self):
        return TokenBlocklistTuple(id=self.id,zuser_id=self.zuser_id,jti=self.jti,timestamp=self.timestamp,)

UserightTuple = namedtuple('UserightTuple',  ('id', 'name', 'extra1', 'extra2', 'distinguished_name', 'righttype_lookup', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class Useright(API,UserightMixin, Base, db.Model):
    __tablename__ = 'USERIGHT'
    __entity_name__ = 'Useright'
    __plain_object__ = UserightPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    extra1 = IColumn(db.VARCHAR(64), name='extra1')

    extra2 = IColumn(db.VARCHAR(64), name='extra2')

    distinguished_name = IColumn(db.VARCHAR(256), name='dn')

    righttype_lookup = IColumn(Righttype, nullable=False, name='righttype_lookup')
    roles = IRelationship(lambda: Zrole, secondary=lambda: ZroleUseright, uselist=True)

    def to_named_tuple(self):
        return UserightTuple(id=self.id,name=self.name,extra1=self.extra1,extra2=self.extra2,distinguished_name=self.distinguished_name,righttype_lookup=self.righttype_lookup,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return UserightTuple(id=self.id,name=self.name,extra1=self.extra1,extra2=self.extra2,distinguished_name=self.distinguished_name,righttype_lookup=self.righttype_lookup,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ZreportTuple = namedtuple('ZreportTuple',  ('id', 'name', 'name5', 'name6', 'description', 'reportfile', 'url', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class Zreport(API,ZreportMixin, Base, db.Model):
    __tablename__ = 'ZREPORT'
    __entity_name__ = 'Zreport'
    __plain_object__ = ZreportPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, name='name')

    name5 = IColumn(db.VARCHAR(64), name='name5')

    name6 = IColumn(db.VARCHAR(64), name='name6')

    description = IColumn(db.TEXT, name='description')

    reportfile = IColumn(db.VARCHAR(128), nullable=False, name='reportfile')

    url = IColumn(db.VARCHAR(256), nullable=False, name='url')
    required_userights = IRelationship(lambda: Useright, secondary=lambda: ZreportUseright, uselist=True)

    def to_named_tuple(self):
        return ZreportTuple(id=self.id,name=self.name,name5=self.name5,name6=self.name6,description=self.description,reportfile=self.reportfile,url=self.url,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ZreportTuple(id=self.id,name=self.name,name5=self.name5,name6=self.name6,description=self.description,reportfile=self.reportfile,url=self.url,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ZreportParameterTuple = namedtuple('ZreportParameterTuple',  ('id', 'name', 'prompt_code', 'parameter_type', 'zreport_id', 'f_view_id', 'static_value', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ZreportParameter(ZreportParameterMixin, Base, db.Model):
    __tablename__ = 'ZREPORT_PARAMETER'
    __entity_name__ = 'Zreport_parameter'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    prompt_code = IColumn(db.VARCHAR(64), name='prompt_code')

    parameter_type = IColumn(ParameterType, nullable=False, name='parameter_type')

    zreport_id = IColumn(BigInt, db.ForeignKey('ZREPORT.id', use_alter=True, name='fk_Zreport_parameter_zreport_id'), nullable=False, name='zreport_id')
    zreport = IRelationship(lambda: Zreport, foreign_keys=[zreport_id])

    f_view_id = IColumn(BigInt, name='f_view_id')

    static_value = IColumn(db.VARCHAR(64), name='static_value')

    def to_named_tuple(self):
        return ZreportParameterTuple(id=self.id,name=self.name,prompt_code=self.prompt_code,parameter_type=self.parameter_type,zreport_id=self.zreport_id,f_view_id=self.f_view_id,static_value=self.static_value,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ZreportParameterTuple(id=self.id,name=self.name,prompt_code=self.prompt_code,parameter_type=self.parameter_type,zreport_id=self.zreport_id,f_view_id=self.f_view_id,static_value=self.static_value,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ZroleTuple = namedtuple('ZroleTuple',  ('id', 'name', 'description', 'distinguished_name', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class Zrole(API,ZroleMixin, Base, db.Model):
    __tablename__ = 'ZROLE'
    __entity_name__ = 'Zrole'
    __plain_object__ = ZrolePlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    name = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    description = IColumn(db.VARCHAR(1024), name='description')

    distinguished_name = IColumn(db.VARCHAR(256), name='dn')
    users = IRelationship(lambda: Zuser, secondary=lambda: ZuserZrole, uselist=True)
    userights = IRelationship(lambda: Useright, secondary=lambda: ZroleUseright, uselist=True)

    def to_named_tuple(self):
        return ZroleTuple(id=self.id,name=self.name,description=self.description,distinguished_name=self.distinguished_name,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ZroleTuple(id=self.id,name=self.name,description=self.description,distinguished_name=self.distinguished_name,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ZroleEntityScriptTuple = namedtuple('ZroleEntityScriptTuple',  ('id', 'zrole_id', 'entity', 'init_script', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class ZroleEntityScript(ZroleEntityScriptMixin, Base, db.Model):
    __tablename__ = 'ZROLE_ENTITY_SCRIPT'
    __entity_name__ = 'Zrole_entity_script'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    zrole_id = IColumn(BigInt, db.ForeignKey('ZROLE.id', use_alter=True, name='fk_Zrole_entity_script_zrole_id'), nullable=False, name='zrole_id')
    zrole = IRelationship(lambda: Zrole, foreign_keys=[zrole_id])

    entity = IColumn(db.VARCHAR(64), nullable=False, name='entity')

    init_script = IColumn(db.VARCHAR(4096), name='init_script')

    def to_named_tuple(self):
        return ZroleEntityScriptTuple(id=self.id,zrole_id=self.zrole_id,entity=self.entity,init_script=self.init_script,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ZroleEntityScriptTuple(id=self.id,zrole_id=self.zrole_id,entity=self.entity,init_script=self.init_script,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ZuserTuple = namedtuple('ZuserTuple',  ('id', 'username', 'first_names', 'last_name', 'email', 'address', 'phone', 'start_date', 'force_change_password', 'internal', 'person_id', 'external_person_id', 'status', 'liferay_uid', 'password', 'f_version', 'f_changed', 'f_changedby', 'deleted'  ))

class Zuser(API,ZuserMixin, Base, db.Model):
    __tablename__ = 'ZUSER'
    __entity_name__ = 'Zuser'
    __plain_object__ = ZuserPlain
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    username = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='name')

    first_names = IColumn(db.VARCHAR(64), nullable=False, name='firstname')

    last_name = IColumn(db.VARCHAR(64), nullable=False, name='lastname')

    email = IColumn(db.VARCHAR(64), nullable=False, unique=True, name='email')

    address = IColumn(db.VARCHAR(64), name='address')

    phone = IColumn(db.VARCHAR(64), name='phone')

    start_date = IColumn(db.Date, name='startdate')

    force_change_password = IColumn(CharBool, nullable=False, name='force_change_password')

    internal = IColumn(CharBool, nullable=False, name='internal')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_Zuser_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_Zuser_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    status = IColumn(Status, name='status')

    liferay_uid = IColumn(db.VARCHAR(64), name='liferay_uid')

    password = IColumn(db.VARCHAR(256), nullable=False, name='password')
    usergroups = IRelationship(lambda: GUserGroup, secondary=lambda: GUserGroupZuser, uselist=True)
    __system = Header(u'system')

    roles = IRelationship(lambda: Zrole, secondary=lambda: ZuserZrole, uselist=True)
    __orgunit_access = Header(u'orgunit_access')

    organizations = IRelationship(lambda: IOrgUnit, secondary=lambda: ZuserIOrgUnit, uselist=True)
    external_organizations = IRelationship(lambda: EExtOrg, secondary=lambda: ZuserEExtOrg, uselist=True)

    def to_named_tuple(self):
        return ZuserTuple(id=self.id,username=self.username,first_names=self.first_names,last_name=self.last_name,email=self.email,address=self.address,phone=self.phone,start_date=self.start_date,force_change_password=self.force_change_password,internal=self.internal,person_id=self.person_id,external_person_id=self.external_person_id,status=self.status,liferay_uid=self.liferay_uid,password=self.password,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

    def to_plain_object(self):
        return ZuserTuple(id=self.id,username=self.username,first_names=self.first_names,last_name=self.last_name,email=self.email,address=self.address,phone=self.phone,start_date=self.start_date,force_change_password=self.force_change_password,internal=self.internal,person_id=self.person_id,external_person_id=self.external_person_id,status=self.status,liferay_uid=self.liferay_uid,password=self.password,f_version=self.f_version,f_changed=self.f_changed,f_changedby=self.f_changedby,deleted=self.deleted,)

ZuserPasswordTuple = namedtuple('ZuserPasswordTuple',  ('id', 'zuser_id', 'password', 'timestamp'  ))

class ZuserPassword(ZuserPasswordMixin, db.Model):
    __tablename__ = 'ZUSER_PASSWORD'
    __entity_name__ = 'Zuser_password'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    zuser_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_Zuser_password_zuser_id'), name='zuser_id')
    zuser = IRelationship(lambda: Zuser, foreign_keys=[zuser_id])

    password = IColumn(db.VARCHAR(256), name='password')

    timestamp = IColumn(db.DateTime, name='timestamp')

    def to_named_tuple(self):
        return ZuserPasswordTuple(id=self.id,zuser_id=self.zuser_id,password=self.password,timestamp=self.timestamp,)

    def to_plain_object(self):
        return ZuserPasswordTuple(id=self.id,zuser_id=self.zuser_id,password=self.password,timestamp=self.timestamp,)

DisplayNameCacheTuple = namedtuple('DisplayNameCacheTuple',  ('table_name', 'id', 'display_name', 'last_updated'  ))

class DisplayNameCache(DisplayNameCacheMixin, db.Model):
    __tablename__ = 'display_name_cache'
    __entity_name__ = 'display_name_cache'
    __parent_entity__ = None

    table_name = IColumn(db.VARCHAR(64), primary_key=True, name='table_name')

    id = IColumn(BigInt, primary_key=True, name='id')

    table_name = IColumn(db.VARCHAR(64), primary_key=True, name='table_name')

    id = IColumn(BigInt, primary_key=True, name='id')

    display_name = IColumn(db.TEXT, name='display_name')

    last_updated = IColumn(db.DateTime, nullable=False, name='last_updated')

    def to_named_tuple(self):
        return DisplayNameCacheTuple(table_name=self.table_name,id=self.id,display_name=self.display_name,last_updated=self.last_updated,)

    def to_plain_object(self):
        return DisplayNameCacheTuple(table_name=self.table_name,id=self.id,display_name=self.display_name,last_updated=self.last_updated,)

EntityAuditLogTuple = namedtuple('EntityAuditLogTuple',  ('entity_name', 'entity_id', 'timestamp', 'attribute_name', 'parent_id', 'old_value', 'new_value', 'created_by'  ))

class EntityAuditLog(EntityAuditLogMixin, db.Model):
    __tablename__ = 'entity_audit_log'
    __entity_name__ = 'entity_audit_log'
    __parent_entity__ = None

    entity_name = IColumn(db.VARCHAR(64), primary_key=True, name='entity_name')

    entity_id = IColumn(BigInt, primary_key=True, name='entity_id')

    timestamp = IColumn(db.DateTime, primary_key=True, name='timestamp')

    attribute_name = IColumn(db.VARCHAR(64), primary_key=True, name='attribute_name')

    entity_name = IColumn(db.VARCHAR(64), primary_key=True, name='entity_name')

    entity_id = IColumn(BigInt, primary_key=True, name='entity_id')

    timestamp = IColumn(db.DateTime, primary_key=True, name='timestamp')

    attribute_name = IColumn(db.VARCHAR(64), primary_key=True, name='attribute_name')

    parent_id = IColumn(BigInt, name='parent_id')

    old_value = IColumn(db.TEXT, name='old_value')

    new_value = IColumn(db.TEXT, name='new_value')

    created_by = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_entity_audit_log_created_by'), name='created_by')

    def to_named_tuple(self):
        return EntityAuditLogTuple(entity_name=self.entity_name,entity_id=self.entity_id,timestamp=self.timestamp,attribute_name=self.attribute_name,parent_id=self.parent_id,old_value=self.old_value,new_value=self.new_value,created_by=self.created_by,)

    def to_plain_object(self):
        return EntityAuditLogTuple(entity_name=self.entity_name,entity_id=self.entity_id,timestamp=self.timestamp,attribute_name=self.attribute_name,parent_id=self.parent_id,old_value=self.old_value,new_value=self.new_value,created_by=self.created_by,)

EntityTieAuditLogTuple = namedtuple('EntityTieAuditLogTuple',  ('tie_entity_name', 'local_entity', 'remote_entity', 'local_id', 'remote_id', 'operation', 'timestamp', 'created_by'  ))

class EntityTieAuditLog(EntityTieAuditLogMixin, db.Model):
    __tablename__ = 'entity_tie_audit_log'
    __entity_name__ = 'entity_tie_audit_log'
    __parent_entity__ = None

    tie_entity_name = IColumn(db.VARCHAR(64), primary_key=True, name='tie_entity_name')

    local_entity = IColumn(db.VARCHAR(64), primary_key=True, name='local_entity')

    remote_entity = IColumn(db.VARCHAR(64), primary_key=True, name='remote_entity')

    local_id = IColumn(BigInt, primary_key=True, name='local_id')

    remote_id = IColumn(BigInt, primary_key=True, name='remote_id')

    operation = IColumn(db.VARCHAR(64), primary_key=True, name='operation')

    timestamp = IColumn(db.DateTime, primary_key=True, name='timestamp')

    tie_entity_name = IColumn(db.VARCHAR(64), primary_key=True, name='tie_entity_name')

    local_entity = IColumn(db.VARCHAR(64), primary_key=True, name='local_entity')

    remote_entity = IColumn(db.VARCHAR(64), primary_key=True, name='remote_entity')

    local_id = IColumn(BigInt, primary_key=True, name='local_id')

    remote_id = IColumn(BigInt, primary_key=True, name='remote_id')

    operation = IColumn(db.VARCHAR(64), primary_key=True, name='operation')

    timestamp = IColumn(db.DateTime, primary_key=True, name='timestamp')

    created_by = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_entity_tie_audit_log_created_by'), name='created_by')

    def to_named_tuple(self):
        return EntityTieAuditLogTuple(tie_entity_name=self.tie_entity_name,local_entity=self.local_entity,remote_entity=self.remote_entity,local_id=self.local_id,remote_id=self.remote_id,operation=self.operation,timestamp=self.timestamp,created_by=self.created_by,)

    def to_plain_object(self):
        return EntityTieAuditLogTuple(tie_entity_name=self.tie_entity_name,local_entity=self.local_entity,remote_entity=self.remote_entity,local_id=self.local_id,remote_id=self.remote_id,operation=self.operation,timestamp=self.timestamp,created_by=self.created_by,)

EventLogTuple = namedtuple('EventLogTuple',  ('id', 'zuser_id', 'source_ip_address', 'request_metadata', 'timestamp', 'action', 'interaction_identifier', 'interaction_identifier_entity_id', 'event_type', 'severity', 'software_version', 'entity_name', 'entity_id', 'endpoint', 'message', 'attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5'  ))

class EventLog(EventLogMixin, db.Model):
    __tablename__ = 'event_log'
    __entity_name__ = 'event_log'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    zuser_id = IColumn(BigInt, db.ForeignKey('ZUSER.id', use_alter=True, name='fk_event_log_zuser_id'), name='zuser_id')
    zuser = IRelationship(lambda: Zuser, foreign_keys=[zuser_id])

    source_ip_address = IColumn(db.VARCHAR(256), name='source_ip_address')

    request_metadata = IColumn(db.VARCHAR(512), name='request_metadata')

    timestamp = IColumn(db.DateTime, name='timestamp')

    action = IColumn(db.VARCHAR(64), name='action')

    interaction_identifier = IColumn(db.VARCHAR(64), name='interaction_identifier')

    interaction_identifier_entity_id = IColumn(db.VARCHAR(256), name='interaction_identifier_entity_id')

    event_type = IColumn(EventLogType, name='event_type')

    severity = IColumn(EventLogSeverity, name='severity')

    software_version = IColumn(db.VARCHAR(64), name='software_version')

    entity_name = IColumn(db.VARCHAR(64), name='entity_name')

    entity_id = IColumn(db.VARCHAR(256), name='entity_id')

    endpoint = IColumn(db.VARCHAR(512), name='endpoint')

    message = IColumn(db.VARCHAR(512), name='message')

    attribute1 = IColumn(db.VARCHAR(512), name='attribute1')

    attribute2 = IColumn(db.VARCHAR(512), name='attribute2')

    attribute3 = IColumn(db.VARCHAR(512), name='attribute3')

    attribute4 = IColumn(db.VARCHAR(512), name='attribute4')

    attribute5 = IColumn(db.VARCHAR(512), name='attribute5')

    def to_named_tuple(self):
        return EventLogTuple(id=self.id,zuser_id=self.zuser_id,source_ip_address=self.source_ip_address,request_metadata=self.request_metadata,timestamp=self.timestamp,action=self.action,interaction_identifier=self.interaction_identifier,interaction_identifier_entity_id=self.interaction_identifier_entity_id,event_type=self.event_type,severity=self.severity,software_version=self.software_version,entity_name=self.entity_name,entity_id=self.entity_id,endpoint=self.endpoint,message=self.message,attribute1=self.attribute1,attribute2=self.attribute2,attribute3=self.attribute3,attribute4=self.attribute4,attribute5=self.attribute5,)

    def to_plain_object(self):
        return EventLogTuple(id=self.id,zuser_id=self.zuser_id,source_ip_address=self.source_ip_address,request_metadata=self.request_metadata,timestamp=self.timestamp,action=self.action,interaction_identifier=self.interaction_identifier,interaction_identifier_entity_id=self.interaction_identifier_entity_id,event_type=self.event_type,severity=self.severity,software_version=self.software_version,entity_name=self.entity_name,entity_id=self.entity_id,endpoint=self.endpoint,message=self.message,attribute1=self.attribute1,attribute2=self.attribute2,attribute3=self.attribute3,attribute4=self.attribute4,attribute5=self.attribute5,)

JobPeriodQueryTableTuple = namedtuple('JobPeriodQueryTableTuple',  ('id', 'person_id', 'person_id__name', 'external_person_id', 'external_person_id__name', 'last_name', 'preferred_name', 'first_name', 'middle_name', 'email', 'voice_address', 'b_phone', 'social_security_number', 'job_period_id', 'e_job_period_id', 'int_job_title', 'job_title', 'other_job_title', 'specific_job_title', 'hr_job_type', 'starting_date', 'termination_date', 'full_part_per', 'orgunit_id', 'd_person_manager_id', 'manager_id__name', 'manager_id', 'org_unit_manager_id', 'orgunit_id__name', 'ext_org_id', 'ext_org_id__name', 'jobtitle_id', 'jobtitle_id__name', 'information_checked', 'from_hr', 'invalidated', 'internal', 'is_primary_job_period', 'absence_active', 'c_pasu'  ))

class JobPeriodQueryTable(JobPeriodQueryTableMixin, db.Model):
    __tablename__ = 'job_period_query_table'
    __entity_name__ = 'job_period_query_table'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_job_period_query_table_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    person_id__name = IColumn(db.TEXT, name='person_id__name')

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_job_period_query_table_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    external_person_id__name = IColumn(db.TEXT, name='external_person_id__name')

    last_name = IColumn(db.TEXT, name='last_name')

    preferred_name = IColumn(db.TEXT, name='preferred_name')

    first_name = IColumn(db.TEXT, name='first_name')

    middle_name = IColumn(db.TEXT, name='middle_name')

    email = IColumn(db.TEXT, name='email')

    voice_address = IColumn(db.TEXT, name='voice_address')

    b_phone = IColumn(db.TEXT, name='b_phone')

    social_security_number = IColumn(db.TEXT, name='social_security_number')

    job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_job_period_query_table_job_period_id'), name='job_period_id')
    job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[job_period_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_job_period_query_table_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    int_job_title = IColumn(db.TEXT, name='int_job_title')

    job_title = IColumn(db.TEXT, name='job_title')

    other_job_title = IColumn(db.TEXT, name='other_job_title')

    specific_job_title = IColumn(db.TEXT, name='specific_job_title')

    hr_job_type = IColumn(HRJobType, name='hr_job_type')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    full_part_per = IColumn(db.Float, name='full_part_per')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_job_period_query_table_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    d_person_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_job_period_query_table_d_person_manager_id'), name='d_person_manager_id')
    d_person_manager = IRelationship(lambda: DPerson, foreign_keys=[d_person_manager_id])

    manager_id__name = IColumn(db.TEXT, name='manager_id__name')

    manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_job_period_query_table_manager_id'), name='manager_id')
    manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[manager_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_job_period_query_table_org_unit_manager_id'), name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    orgunit_id__name = IColumn(db.TEXT, name='orgunit_id__name')

    ext_org_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_job_period_query_table_ext_org_id'), name='ext_org_id')
    ext_org = IRelationship(lambda: EExtOrg, foreign_keys=[ext_org_id])

    ext_org_id__name = IColumn(db.TEXT, name='ext_org_id__name')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_job_period_query_table_jobtitle_id'), name='jobtitle_id')
    jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    jobtitle_id__name = IColumn(db.TEXT, name='jobtitle_id__name')

    information_checked = IColumn(CharBool, nullable=False, name='information_checked')

    from_hr = IColumn(CharBool, nullable=False, name='from_hr')

    invalidated = IColumn(CharBool, nullable=False, name='invalidated')

    internal = IColumn(CharBool, nullable=False, name='internal')

    is_primary_job_period = IColumn(CharBool, nullable=False, name='is_primary_job_period')

    absence_active = IColumn(CharBool, nullable=False, name='absence_active')

    c_pasu = IColumn(CharBool, nullable=False, name='c_pasu')

    def to_named_tuple(self):
        return JobPeriodQueryTableTuple(id=self.id,person_id=self.person_id,person_id__name=self.person_id__name,external_person_id=self.external_person_id,external_person_id__name=self.external_person_id__name,last_name=self.last_name,preferred_name=self.preferred_name,first_name=self.first_name,middle_name=self.middle_name,email=self.email,voice_address=self.voice_address,b_phone=self.b_phone,social_security_number=self.social_security_number,job_period_id=self.job_period_id,e_job_period_id=self.e_job_period_id,int_job_title=self.int_job_title,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,hr_job_type=self.hr_job_type,starting_date=self.starting_date,termination_date=self.termination_date,full_part_per=self.full_part_per,orgunit_id=self.orgunit_id,d_person_manager_id=self.d_person_manager_id,manager_id__name=self.manager_id__name,manager_id=self.manager_id,org_unit_manager_id=self.org_unit_manager_id,orgunit_id__name=self.orgunit_id__name,ext_org_id=self.ext_org_id,ext_org_id__name=self.ext_org_id__name,jobtitle_id=self.jobtitle_id,jobtitle_id__name=self.jobtitle_id__name,information_checked=self.information_checked,from_hr=self.from_hr,invalidated=self.invalidated,internal=self.internal,is_primary_job_period=self.is_primary_job_period,absence_active=self.absence_active,c_pasu=self.c_pasu,)

    def to_plain_object(self):
        return JobPeriodQueryTableTuple(id=self.id,person_id=self.person_id,person_id__name=self.person_id__name,external_person_id=self.external_person_id,external_person_id__name=self.external_person_id__name,last_name=self.last_name,preferred_name=self.preferred_name,first_name=self.first_name,middle_name=self.middle_name,email=self.email,voice_address=self.voice_address,b_phone=self.b_phone,social_security_number=self.social_security_number,job_period_id=self.job_period_id,e_job_period_id=self.e_job_period_id,int_job_title=self.int_job_title,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,hr_job_type=self.hr_job_type,starting_date=self.starting_date,termination_date=self.termination_date,full_part_per=self.full_part_per,orgunit_id=self.orgunit_id,d_person_manager_id=self.d_person_manager_id,manager_id__name=self.manager_id__name,manager_id=self.manager_id,org_unit_manager_id=self.org_unit_manager_id,orgunit_id__name=self.orgunit_id__name,ext_org_id=self.ext_org_id,ext_org_id__name=self.ext_org_id__name,jobtitle_id=self.jobtitle_id,jobtitle_id__name=self.jobtitle_id__name,information_checked=self.information_checked,from_hr=self.from_hr,invalidated=self.invalidated,internal=self.internal,is_primary_job_period=self.is_primary_job_period,absence_active=self.absence_active,c_pasu=self.c_pasu,)

JobPeriodQueryTablePrimTuple = namedtuple('JobPeriodQueryTablePrimTuple',  ('id', 'person_id', 'person_id__name', 'external_person_id', 'external_person_id__name', 'last_name', 'preferred_name', 'first_name', 'middle_name', 'email', 'voice_address', 'b_phone', 'social_security_number', 'job_period_id', 'e_job_period_id', 'int_job_title', 'job_title', 'other_job_title', 'specific_job_title', 'hr_job_type', 'starting_date', 'termination_date', 'full_part_per', 'orgunit_id', 'd_person_manager_id', 'manager_id__name', 'manager_id', 'org_unit_manager_id', 'orgunit_id__name', 'ext_org_id', 'ext_org_id__name', 'jobtitle_id', 'jobtitle_id__name', 'information_checked', 'from_hr', 'invalidated', 'internal', 'is_primary_job_period', 'absence_active', 'c_pasu'  ))

class JobPeriodQueryTablePrim(JobPeriodQueryTablePrimMixin, db.Model):
    __tablename__ = 'job_period_query_table_prim'
    __entity_name__ = 'job_period_query_table_prim'
    __parent_entity__ = None

    id = IColumn(BigInt, primary_key=True, name='id')

    person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_job_period_query_table_prim_person_id'), name='person_id')
    person = IRelationship(lambda: DPerson, foreign_keys=[person_id])

    person_id__name = IColumn(db.TEXT, name='person_id__name')

    external_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_job_period_query_table_prim_external_person_id'), name='external_person_id')
    external_person = IRelationship(lambda: EExternalPerson, foreign_keys=[external_person_id])

    external_person_id__name = IColumn(db.TEXT, name='external_person_id__name')

    last_name = IColumn(db.TEXT, name='last_name')

    preferred_name = IColumn(db.TEXT, name='preferred_name')

    first_name = IColumn(db.TEXT, name='first_name')

    middle_name = IColumn(db.TEXT, name='middle_name')

    email = IColumn(db.TEXT, name='email')

    voice_address = IColumn(db.TEXT, name='voice_address')

    b_phone = IColumn(db.TEXT, name='b_phone')

    social_security_number = IColumn(db.TEXT, name='social_security_number')

    job_period_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_job_period_query_table_prim_job_period_id'), name='job_period_id')
    job_period = IRelationship(lambda: DJobPeriod, foreign_keys=[job_period_id])

    e_job_period_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_job_period_query_table_prim_e_job_period_id'), name='e_job_period_id')
    e_job_period = IRelationship(lambda: EJobPeriod, foreign_keys=[e_job_period_id])

    int_job_title = IColumn(db.TEXT, name='int_job_title')

    job_title = IColumn(db.TEXT, name='job_title')

    other_job_title = IColumn(db.TEXT, name='other_job_title')

    specific_job_title = IColumn(db.TEXT, name='specific_job_title')

    hr_job_type = IColumn(HRJobType, name='hr_job_type')

    starting_date = IColumn(db.Date, name='starting_date')

    termination_date = IColumn(db.Date, name='termination_date')

    full_part_per = IColumn(db.Float, name='full_part_per')

    orgunit_id = IColumn(BigInt, db.ForeignKey('O_I_ORG_UNIT.id', use_alter=True, name='fk_job_period_query_table_prim_orgunit_id'), name='orgunit_id')
    orgunit = IRelationship(lambda: IOrgUnit, foreign_keys=[orgunit_id])

    d_person_manager_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_job_period_query_table_prim_d_person_manager_id'), name='d_person_manager_id')
    d_person_manager = IRelationship(lambda: DPerson, foreign_keys=[d_person_manager_id])

    manager_id__name = IColumn(db.TEXT, name='manager_id__name')

    manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_job_period_query_table_prim_manager_id'), name='manager_id')
    manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[manager_id])

    org_unit_manager_id = IColumn(BigInt, db.ForeignKey('I_ORG_UNIT_MANAGER.id', use_alter=True, name='fk_job_period_query_table_prim_org_unit_manager_id'), name='org_unit_manager_id')
    org_unit_manager = IRelationship(lambda: IOrgUnitManager, foreign_keys=[org_unit_manager_id])

    orgunit_id__name = IColumn(db.TEXT, name='orgunit_id__name')

    ext_org_id = IColumn(BigInt, db.ForeignKey('O_E_EXT_ORG.id', use_alter=True, name='fk_job_period_query_table_prim_ext_org_id'), name='ext_org_id')
    ext_org = IRelationship(lambda: EExtOrg, foreign_keys=[ext_org_id])

    ext_org_id__name = IColumn(db.TEXT, name='ext_org_id__name')

    jobtitle_id = IColumn(BigInt, db.ForeignKey('D_JOBTITLE.id', use_alter=True, name='fk_job_period_query_table_prim_jobtitle_id'), name='jobtitle_id')
    jobtitle = IRelationship(lambda: DJobtitle, foreign_keys=[jobtitle_id])

    jobtitle_id__name = IColumn(db.TEXT, name='jobtitle_id__name')

    information_checked = IColumn(CharBool, nullable=False, name='information_checked')

    from_hr = IColumn(CharBool, nullable=False, name='from_hr')

    invalidated = IColumn(CharBool, nullable=False, name='invalidated')

    internal = IColumn(CharBool, nullable=False, name='internal')

    is_primary_job_period = IColumn(CharBool, nullable=False, name='is_primary_job_period')

    absence_active = IColumn(CharBool, nullable=False, name='absence_active')

    c_pasu = IColumn(CharBool, nullable=False, name='c_pasu')

    def to_named_tuple(self):
        return JobPeriodQueryTablePrimTuple(id=self.id,person_id=self.person_id,person_id__name=self.person_id__name,external_person_id=self.external_person_id,external_person_id__name=self.external_person_id__name,last_name=self.last_name,preferred_name=self.preferred_name,first_name=self.first_name,middle_name=self.middle_name,email=self.email,voice_address=self.voice_address,b_phone=self.b_phone,social_security_number=self.social_security_number,job_period_id=self.job_period_id,e_job_period_id=self.e_job_period_id,int_job_title=self.int_job_title,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,hr_job_type=self.hr_job_type,starting_date=self.starting_date,termination_date=self.termination_date,full_part_per=self.full_part_per,orgunit_id=self.orgunit_id,d_person_manager_id=self.d_person_manager_id,manager_id__name=self.manager_id__name,manager_id=self.manager_id,org_unit_manager_id=self.org_unit_manager_id,orgunit_id__name=self.orgunit_id__name,ext_org_id=self.ext_org_id,ext_org_id__name=self.ext_org_id__name,jobtitle_id=self.jobtitle_id,jobtitle_id__name=self.jobtitle_id__name,information_checked=self.information_checked,from_hr=self.from_hr,invalidated=self.invalidated,internal=self.internal,is_primary_job_period=self.is_primary_job_period,absence_active=self.absence_active,c_pasu=self.c_pasu,)

    def to_plain_object(self):
        return JobPeriodQueryTablePrimTuple(id=self.id,person_id=self.person_id,person_id__name=self.person_id__name,external_person_id=self.external_person_id,external_person_id__name=self.external_person_id__name,last_name=self.last_name,preferred_name=self.preferred_name,first_name=self.first_name,middle_name=self.middle_name,email=self.email,voice_address=self.voice_address,b_phone=self.b_phone,social_security_number=self.social_security_number,job_period_id=self.job_period_id,e_job_period_id=self.e_job_period_id,int_job_title=self.int_job_title,job_title=self.job_title,other_job_title=self.other_job_title,specific_job_title=self.specific_job_title,hr_job_type=self.hr_job_type,starting_date=self.starting_date,termination_date=self.termination_date,full_part_per=self.full_part_per,orgunit_id=self.orgunit_id,d_person_manager_id=self.d_person_manager_id,manager_id__name=self.manager_id__name,manager_id=self.manager_id,org_unit_manager_id=self.org_unit_manager_id,orgunit_id__name=self.orgunit_id__name,ext_org_id=self.ext_org_id,ext_org_id__name=self.ext_org_id__name,jobtitle_id=self.jobtitle_id,jobtitle_id__name=self.jobtitle_id__name,information_checked=self.information_checked,from_hr=self.from_hr,invalidated=self.invalidated,internal=self.internal,is_primary_job_period=self.is_primary_job_period,absence_active=self.absence_active,c_pasu=self.c_pasu,)

XPrimaryJobPeriodTuple = namedtuple('XPrimaryJobPeriodTuple',  ('x_person_id', 'd_person_id', 'e_person_id', 'inferred_int_jp_id', 'inferred_ext_jp_id', 'manual_int_jp_id', 'manual_ext_jp_id', 'last_updated'  ))

class XPrimaryJobPeriod(XPrimaryJobPeriodMixin, db.Model):
    __tablename__ = 'x_primary_job_period'
    __entity_name__ = 'x_primary_job_period'
    __parent_entity__ = None

    x_person_id = IColumn(db.VARCHAR(64), primary_key=True, name='x_person_id')

    x_person_id = IColumn(db.VARCHAR(64), primary_key=True, name='x_person_id')

    d_person_id = IColumn(BigInt, db.ForeignKey('O_D_PERSON.id', use_alter=True, name='fk_x_primary_job_period_d_person_id'), name='d_person_id')
    d_person = IRelationship(lambda: DPerson, foreign_keys=[d_person_id])

    e_person_id = IColumn(BigInt, db.ForeignKey('O_E_EXTERNAL_PERSON.id', use_alter=True, name='fk_x_primary_job_period_e_person_id'), name='e_person_id')
    e_person = IRelationship(lambda: EExternalPerson, foreign_keys=[e_person_id])

    inferred_int_jp_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_x_primary_job_period_inferred_int_jp_id'), name='inferred_int_jp_id')
    inferred_int_jp = IRelationship(lambda: DJobPeriod, foreign_keys=[inferred_int_jp_id])

    inferred_ext_jp_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_x_primary_job_period_inferred_ext_jp_id'), name='inferred_ext_jp_id')
    inferred_ext_jp = IRelationship(lambda: EJobPeriod, foreign_keys=[inferred_ext_jp_id])

    manual_int_jp_id = IColumn(BigInt, db.ForeignKey('D_JOB_PERIOD.id', use_alter=True, name='fk_x_primary_job_period_manual_int_jp_id'), name='manual_int_jp_id')
    manual_int_jp = IRelationship(lambda: DJobPeriod, foreign_keys=[manual_int_jp_id])

    manual_ext_jp_id = IColumn(BigInt, db.ForeignKey('E_JOB_PERIOD.id', use_alter=True, name='fk_x_primary_job_period_manual_ext_jp_id'), name='manual_ext_jp_id')
    manual_ext_jp = IRelationship(lambda: EJobPeriod, foreign_keys=[manual_ext_jp_id])

    last_updated = IColumn(db.DateTime, name='last_updated')

    def to_named_tuple(self):
        return XPrimaryJobPeriodTuple(x_person_id=self.x_person_id,d_person_id=self.d_person_id,e_person_id=self.e_person_id,inferred_int_jp_id=self.inferred_int_jp_id,inferred_ext_jp_id=self.inferred_ext_jp_id,manual_int_jp_id=self.manual_int_jp_id,manual_ext_jp_id=self.manual_ext_jp_id,last_updated=self.last_updated,)

    def to_plain_object(self):
        return XPrimaryJobPeriodTuple(x_person_id=self.x_person_id,d_person_id=self.d_person_id,e_person_id=self.e_person_id,inferred_int_jp_id=self.inferred_int_jp_id,inferred_ext_jp_id=self.inferred_ext_jp_id,manual_int_jp_id=self.manual_int_jp_id,manual_ext_jp_id=self.manual_ext_jp_id,last_updated=self.last_updated,)

CCardPlain.__baseclass__ = CCard
CCardIssuerPlain.__baseclass__ = CCardIssuer
CCardOrganizationPlain.__baseclass__ = CCardOrganization
CCardTypePlain.__baseclass__ = CCardType
CDevicePlain.__baseclass__ = CDevice
CDevicePersonPlain.__baseclass__ = CDevicePerson
CDeviceSubtypePlain.__baseclass__ = CDeviceSubtype
CDeviceTypePlain.__baseclass__ = CDeviceType
CKeyPlain.__baseclass__ = CKey
CKeyProfilePlain.__baseclass__ = CKeyProfile
CKeyTypePlain.__baseclass__ = CKeyType
CWorkstationPlain.__baseclass__ = CWorkstation
DAbsencePlain.__baseclass__ = DAbsence
DAuthMethodPlain.__baseclass__ = DAuthMethod
DCompetencePlain.__baseclass__ = DCompetence
DEducationPlain.__baseclass__ = DEducation
DJobPeriodPlain.__baseclass__ = DJobPeriod
DJobPeriodAbsencePlain.__baseclass__ = DJobPeriodAbsence
DJobPeriodSubstitutePlain.__baseclass__ = DJobPeriodSubstitute
DJobtitlePlain.__baseclass__ = DJobtitle
DMappingRulePlain.__baseclass__ = DMappingRule
DPersonPlain.__baseclass__ = DPerson
DUserAuthPlain.__baseclass__ = DUserAuth
EExtOrgPlain.__baseclass__ = EExtOrg
EExtOrgTypePlain.__baseclass__ = EExtOrgType
EExternalPersonPlain.__baseclass__ = EExternalPerson
EJobFamilyPlain.__baseclass__ = EJobFamily
EJobPeriodPlain.__baseclass__ = EJobPeriod
EJobPeriodAbsencePlain.__baseclass__ = EJobPeriodAbsence
EJobPeriodSubstitutePlain.__baseclass__ = EJobPeriodSubstitute
EJobRolePlain.__baseclass__ = EJobRole
EOrgTypeServicePlain.__baseclass__ = EOrgTypeService
ERequestCartPlain.__baseclass__ = ERequestCart
ERequestCartPermissionPlain.__baseclass__ = ERequestCartPermission
GAccountAttributePlain.__baseclass__ = GAccountAttribute
GAcePlain.__baseclass__ = GAce
GAceAttributePlain.__baseclass__ = GAceAttribute
GCountryPlain.__baseclass__ = GCountry
GIdentityPlain.__baseclass__ = GIdentity
GIdentitySourcePlain.__baseclass__ = GIdentitySource
GLanguagePlain.__baseclass__ = GLanguage
GMdmRulePlain.__baseclass__ = GMdmRule
GMdmSourcePlain.__baseclass__ = GMdmSource
GNotificationPlain.__baseclass__ = GNotification
GNotificationQueuePlain.__baseclass__ = GNotificationQueue
GPermissionPlain.__baseclass__ = GPermission
GPersonUseraccountPlain.__baseclass__ = GPersonUseraccount
GProvisioningTaskPlain.__baseclass__ = GProvisioningTask
GRegionPlain.__baseclass__ = GRegion
GServicePlain.__baseclass__ = GService
GServiceProviderPlain.__baseclass__ = GServiceProvider
GServiceRequestPlain.__baseclass__ = GServiceRequest
GServiceRespPlain.__baseclass__ = GServiceResp
GServiceRolePlain.__baseclass__ = GServiceRole
GServiceTypePlain.__baseclass__ = GServiceType
GServiceTypeSrolesPlain.__baseclass__ = GServiceTypeSroles
GSrParametersPlain.__baseclass__ = GSrParameters
GSrTransPlain.__baseclass__ = GSrTrans
GSystemPlain.__baseclass__ = GSystem
GSystemSchemaPlain.__baseclass__ = GSystemSchema
GSystemSchemaAttributePlain.__baseclass__ = GSystemSchemaAttribute
GUserGroupPlain.__baseclass__ = GUserGroup
HrDesktopSubstPlain.__baseclass__ = HrDesktopSubst
HrImportRecordPlain.__baseclass__ = HrImportRecord
HrIntegrationPlain.__baseclass__ = HrIntegration
HrIntegrationVaultPlain.__baseclass__ = HrIntegrationVault
IBusinessAreaPlain.__baseclass__ = IBusinessArea
ICostCenterPlain.__baseclass__ = ICostCenter
IJobFamilyPlain.__baseclass__ = IJobFamily
IJobRolePlain.__baseclass__ = IJobRole
ILegalCompanyPlain.__baseclass__ = ILegalCompany
ILocationPlain.__baseclass__ = ILocation
IManagerPerProfessionPlain.__baseclass__ = IManagerPerProfession
IOrgGroupPlain.__baseclass__ = IOrgGroup
IOrgTypePlain.__baseclass__ = IOrgType
IOrgUnitPlain.__baseclass__ = IOrgUnit
IOrgUnitManagerPlain.__baseclass__ = IOrgUnitManager
IOrgUnitManagerSubstitutePlain.__baseclass__ = IOrgUnitManagerSubstitute
OneTimeLinkPlain.__baseclass__ = OneTimeLink
PRequestCartPlain.__baseclass__ = PRequestCart
PRequestCartRowPlain.__baseclass__ = PRequestCartRow
RDynRolePlain.__baseclass__ = RDynRole
ROrgDacPlain.__baseclass__ = ROrgDac
ROrgServicePlain.__baseclass__ = ROrgService
ROrgTypeServicePlain.__baseclass__ = ROrgTypeService
RSodExceptionPlain.__baseclass__ = RSodException
RSodRulePlain.__baseclass__ = RSodRule
RSodRuleClassPlain.__baseclass__ = RSodRuleClass
RUserDacPlain.__baseclass__ = RUserDac
RequestCartPlain.__baseclass__ = RequestCart
RequestCartPermissionPlain.__baseclass__ = RequestCartPermission
SDDepartmentWeekMaxQuantityPlain.__baseclass__ = SDDepartmentWeekMaxQuantity
SDStudyProgrammePlain.__baseclass__ = SDStudyProgramme
SDTraineeshipPlacementPlain.__baseclass__ = SDTraineeshipPlacement
SDTraineeshipPlacementRequestPlain.__baseclass__ = SDTraineeshipPlacementRequest
SDTraineeshipRequestPlain.__baseclass__ = SDTraineeshipRequest
SDTraineeshipTypePlain.__baseclass__ = SDTraineeshipType
UserightPlain.__baseclass__ = Useright
ZreportPlain.__baseclass__ = Zreport
ZrolePlain.__baseclass__ = Zrole
ZuserPlain.__baseclass__ = Zuser
DJobPeriod.__parent_entity__ = DPerson
EJobPeriod.__parent_entity__ = EExternalPerson
GServiceRole.__parent_entity__ = GService
IOrgUnitManager.__parent_entity__ = IOrgUnit
IOrgUnitManagerSubstitute.__parent_entity__ = IOrgUnitManager
EExtOrgCtAll.__parent_entity__ = EExtOrg
EJobRoleCtAll.__parent_entity__ = EJobRole
GServiceCtAll.__parent_entity__ = GService
GServiceRoleCtAll.__parent_entity__ = GServiceRole
GSystemCtAll.__parent_entity__ = GSystem
IJobRoleCtAll.__parent_entity__ = IJobRole
ILocationCtAll.__parent_entity__ = ILocation
IOrgUnitCtAll.__parent_entity__ = IOrgUnit
SDTraineeshipTypeCtAll.__parent_entity__ = SDTraineeshipType
ZuserZrole = db.Table('ZUSER_ZROLE', db.Model.metadata,
    IColumn('zuser_id', BigInt, db.ForeignKey(Zuser.id), primary_key=True),
    IColumn('zrole_id', BigInt, db.ForeignKey(Zrole.id), primary_key=True),
)
ZuserIOrgUnit = db.Table('ZUSER_I_ORG_UNIT', db.Model.metadata,
    IColumn('zuser_id', BigInt, db.ForeignKey(Zuser.id), primary_key=True),
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
)
ZuserEExtOrg = db.Table('ZUSER_E_EXT_ORG', db.Model.metadata,
    IColumn('zuser_id', BigInt, db.ForeignKey(Zuser.id), primary_key=True),
    IColumn('e_ext_org_id', BigInt, db.ForeignKey(EExtOrg.id), primary_key=True),
)
ZreportUseright = db.Table('ZREPORT_USERIGHT', db.Model.metadata,
    IColumn('zreport_id', BigInt, db.ForeignKey(Zreport.id), primary_key=True),
    IColumn('useright_id', BigInt, db.ForeignKey(Useright.id), primary_key=True),
)
ZroleUseright = db.Table('ZROLE_USERIGHT', db.Model.metadata,
    IColumn('zrole_id', BigInt, db.ForeignKey(Zrole.id), primary_key=True),
    IColumn('useright_id', BigInt, db.ForeignKey(Useright.id), primary_key=True),
)
DJobPeriodIOrgUnit = db.Table('D_JOB_PERIOD_I_ORG_UNIT', db.Model.metadata,
    IColumn('d_job_period_id', BigInt, db.ForeignKey(DJobPeriod.id), primary_key=True),
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
)
DPersonIOrgUnit = db.Table('D_PERSON_I_ORG_UNIT', db.Model.metadata,
    IColumn('d_person_id', BigInt, db.ForeignKey(DPerson.id), primary_key=True),
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
)
DPersonDEducation = db.Table('D_PERSON_D_EDUCATION', db.Model.metadata,
    IColumn('d_person_id', BigInt, db.ForeignKey(DPerson.id), primary_key=True),
    IColumn('d_education_id', BigInt, db.ForeignKey(DEducation.id), primary_key=True),
)
DPersonDCompetence = db.Table('D_PERSON_D_COMPETENCE', db.Model.metadata,
    IColumn('d_person_id', BigInt, db.ForeignKey(DPerson.id), primary_key=True),
    IColumn('d_competence_id', BigInt, db.ForeignKey(DCompetence.id), primary_key=True),
)
EPersonDEducation = db.Table('E_PERSON_D_EDUCATION', db.Model.metadata,
    IColumn('e_person_id', BigInt, db.ForeignKey(EExternalPerson.id), primary_key=True),
    IColumn('d_education_id', BigInt, db.ForeignKey(DEducation.id), primary_key=True),
)
EPersonDCompetence = db.Table('E_PERSON_D_COMPETENCE', db.Model.metadata,
    IColumn('e_person_id', BigInt, db.ForeignKey(EExternalPerson.id), primary_key=True),
    IColumn('d_competence_id', BigInt, db.ForeignKey(DCompetence.id), primary_key=True),
)
EExtOrgGService = db.Table('E_EXT_ORG_G_SERVICE', db.Model.metadata,
    IColumn('e_ext_org_id', BigInt, db.ForeignKey(EExtOrg.id), primary_key=True),
    IColumn('g_service_id', BigInt, db.ForeignKey(GService.id), primary_key=True),
)
EExtOrgGServiceRole = db.Table('E_EXT_ORG_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('e_ext_org_id', BigInt, db.ForeignKey(EExtOrg.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
EExtOrgIOrgGroup = db.Table('E_EXT_ORG_I_ORG_GROUP', db.Model.metadata,
    IColumn('e_ext_org_id', BigInt, db.ForeignKey(EExtOrg.id), primary_key=True),
    IColumn('i_org_group_id', BigInt, db.ForeignKey(IOrgGroup.id), primary_key=True),
)
EJobPeriodIOrgUnit = db.Table('E_JOB_PERIOD_I_ORG_UNIT', db.Model.metadata,
    IColumn('e_job_period_id', BigInt, db.ForeignKey(EJobPeriod.id), primary_key=True),
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
)
EJobRoleGServiceRole = db.Table('E_JOB_ROLE_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('e_job_role_id', BigInt, db.ForeignKey(EJobRole.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
GServiceRoleGAce = db.Table('G_SERVICE_ROLE_G_ACE', db.Model.metadata,
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
    IColumn('g_ace_id', BigInt, db.ForeignKey(GAce.id), primary_key=True),
)
HrIntegrationGServiceRole = db.Table('HR_INTEGRATION_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('hr_integration_id', BigInt, db.ForeignKey(HrIntegration.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
HrIntegrationIOrgUnit = db.Table('HR_INTEGRATION_I_ORG_UNIT', db.Model.metadata,
    IColumn('hr_integration_id', BigInt, db.ForeignKey(HrIntegration.id), primary_key=True),
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
)
HrIntegrationCKeyProfile = db.Table('HR_INTEGRATION_C_KEY_PROFILE', db.Model.metadata,
    IColumn('hr_integration_id', BigInt, db.ForeignKey(HrIntegration.id), primary_key=True),
    IColumn('c_key_profile_id', BigInt, db.ForeignKey(CKeyProfile.id), primary_key=True),
)
IJobRoleGServiceRole = db.Table('I_JOB_ROLE_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('i_job_role_id', BigInt, db.ForeignKey(IJobRole.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
IJobRoleReqGServiceRole = db.Table('I_JOB_ROLE_REQ_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('i_job_role_id', BigInt, db.ForeignKey(IJobRole.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
ILegalCompanyGService = db.Table('I_LEGAL_COMPANY_G_SERVICE', db.Model.metadata,
    IColumn('i_legal_company_id', BigInt, db.ForeignKey(ILegalCompany.id), primary_key=True),
    IColumn('g_service_id', BigInt, db.ForeignKey(GService.id), primary_key=True),
)
ILegalCompanyGServiceRole = db.Table('I_LEGAL_COMPANY_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('i_legal_company_id', BigInt, db.ForeignKey(ILegalCompany.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
IOrgUnitGService = db.Table('I_ORG_UNIT_G_SERVICE', db.Model.metadata,
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
    IColumn('g_service_id', BigInt, db.ForeignKey(GService.id), primary_key=True),
)
IOrgUnitReqGServiceRole = db.Table('I_ORG_UNIT_REQ_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
IOrgUnitGServiceRole = db.Table('I_ORG_UNIT_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)
IOrgUnitIOrgGroup = db.Table('I_ORG_UNIT_I_ORG_GROUP', db.Model.metadata,
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
    IColumn('i_org_group_id', BigInt, db.ForeignKey(IOrgGroup.id), primary_key=True),
)
RequestCartPermissionDPerson = db.Table('REQUEST_CART_PERMISSION_D_PERSON', db.Model.metadata,
    IColumn('request_cart_permission_id', BigInt, db.ForeignKey(RequestCartPermission.id), primary_key=True),
    IColumn('d_person_id', BigInt, db.ForeignKey(DPerson.id), primary_key=True),
)
ERequestCartPermissionDPerson = db.Table('E_REQUEST_CART_PERMISSION_D_PERSON', db.Model.metadata,
    IColumn('e_request_cart_permission_id', BigInt, db.ForeignKey(ERequestCartPermission.id), primary_key=True),
    IColumn('d_person_id', BigInt, db.ForeignKey(DPerson.id), primary_key=True),
)
GUserGroupZuser = db.Table('G_USER_GROUP_ZUSER', db.Model.metadata,
    IColumn('g_user_group_id', BigInt, db.ForeignKey(GUserGroup.id), primary_key=True),
    IColumn('zuser_id', BigInt, db.ForeignKey(Zuser.id), primary_key=True),
)
GUserGroupZreport = db.Table('G_USER_GROUP_ZREPORT', db.Model.metadata,
    IColumn('g_user_group_id', BigInt, db.ForeignKey(GUserGroup.id), primary_key=True),
    IColumn('zreport_id', BigInt, db.ForeignKey(Zreport.id), primary_key=True),
)
GProvisioningTaskGAce = db.Table('G_PROVISIONING_TASK_G_ACE', db.Model.metadata,
    IColumn('g_provisioning_task_id', BigInt, db.ForeignKey(GProvisioningTask.id), primary_key=True),
    IColumn('g_ace_id', BigInt, db.ForeignKey(GAce.id), primary_key=True),
)
GPermissionAssociatedIOrgUnit = db.Table('G_PERMISSION_ASSOCIATED_I_ORG_UNIT', db.Model.metadata,
    IColumn('g_permission_id', BigInt, db.ForeignKey(GPermission.id), primary_key=True),
    IColumn('i_org_unit_id', BigInt, db.ForeignKey(IOrgUnit.id), primary_key=True),
)
GPermissionAssociatedEExtOrg = db.Table('G_PERMISSION_ASSOCIATED_E_EXT_ORG', db.Model.metadata,
    IColumn('g_permission_id', BigInt, db.ForeignKey(GPermission.id), primary_key=True),
    IColumn('e_ext_org_id', BigInt, db.ForeignKey(EExtOrg.id), primary_key=True),
)
SDTraineeshipRequestPerson = db.Table('SD_TRAINEESHIP_REQUEST_PERSON', db.Model.metadata,
    IColumn('traineeship_request_id', BigInt, db.ForeignKey(SDTraineeshipRequest.id), primary_key=True),
    IColumn('student_id', BigInt, db.ForeignKey(EExternalPerson.id), primary_key=True),
)
RDynRoleGServiceRole = db.Table('R_DYN_ROLE_G_SERVICE_ROLE', db.Model.metadata,
    IColumn('r_dyn_role_id', BigInt, db.ForeignKey(RDynRole.id), primary_key=True),
    IColumn('g_service_role_id', BigInt, db.ForeignKey(GServiceRole.id), primary_key=True),
)

# SQLAlchemy Mapper events - kind of similar to SQL triggers
# Right now we are only working with tie table insert and delete events

@db.event.listens_for(DJobPeriod.other_organization_units, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_job_period
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'D_job_period'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_job_period_I_org_unit', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DJobPeriod.other_organization_units, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_job_period
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'D_job_period'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_job_period_I_org_unit', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DPerson.organization_units, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_person
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'D_person'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_person_I_org_unit', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DPerson.organization_units, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_person
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'D_person'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_person_I_org_unit', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DPerson.education, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_education
    local_entity = 'D_person'
    local_id = target.id
    remote_entity = 'D_education'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_person_D_education', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DPerson.education, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_education
    local_entity = 'D_person'
    local_id = target.id
    remote_entity = 'D_education'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_person_D_education', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DPerson.competences, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_competence
    local_entity = 'D_person'
    local_id = target.id
    remote_entity = 'D_competence'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_person_D_competence', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(DPerson.competences, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is D_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_competence
    local_entity = 'D_person'
    local_id = target.id
    remote_entity = 'D_competence'
    remote_id = value.id
    audit_log.create_tie_audit_log('D_person_D_competence', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExtOrg.services, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_ext_org
    # The "remove_entity" is the foreign relationship table, in this case it is G_service
    local_entity = 'E_ext_org'
    local_id = target.id
    remote_entity = 'G_service'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_G_service', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExtOrg.services, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_ext_org
    # The "remove_entity" is the foreign relationship table, in this case it is G_service
    local_entity = 'E_ext_org'
    local_id = target.id
    remote_entity = 'G_service'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_G_service', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExtOrg.service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_ext_org
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'E_ext_org'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExtOrg.service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_ext_org
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'E_ext_org'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExtOrg.organization_groups, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_ext_org
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_group
    local_entity = 'E_ext_org'
    local_id = target.id
    remote_entity = 'I_org_group'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_I_org_group', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExtOrg.organization_groups, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_ext_org
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_group
    local_entity = 'E_ext_org'
    local_id = target.id
    remote_entity = 'I_org_group'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_I_org_group', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExternalPerson.education, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_external_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_education
    local_entity = 'E_external_person'
    local_id = target.id
    remote_entity = 'D_education'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_person_D_education', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExternalPerson.education, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_external_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_education
    local_entity = 'E_external_person'
    local_id = target.id
    remote_entity = 'D_education'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_person_D_education', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExternalPerson.competences, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_external_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_competence
    local_entity = 'E_external_person'
    local_id = target.id
    remote_entity = 'D_competence'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_person_D_competence', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EExternalPerson.competences, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_external_person
    # The "remove_entity" is the foreign relationship table, in this case it is D_competence
    local_entity = 'E_external_person'
    local_id = target.id
    remote_entity = 'D_competence'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_person_D_competence', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EJobPeriod.organization_units, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_job_period
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'E_job_period'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_job_period_I_org_unit', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EJobPeriod.organization_units, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_job_period
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'E_job_period'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_job_period_I_org_unit', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EJobRole.service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_job_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'E_job_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_job_role_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(EJobRole.service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_job_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'E_job_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_job_role_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(ERequestCartPermission.informed_persons, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_request_cart_permission
    # The "remove_entity" is the foreign relationship table, in this case it is D_person
    local_entity = 'E_request_cart_permission'
    local_id = target.id
    remote_entity = 'D_person'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_request_cart_permission_D_person', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(ERequestCartPermission.informed_persons, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is E_request_cart_permission
    # The "remove_entity" is the foreign relationship table, in this case it is D_person
    local_entity = 'E_request_cart_permission'
    local_id = target.id
    remote_entity = 'D_person'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_request_cart_permission_D_person', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GPermission.associated_organization_units, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_permission
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'G_permission'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_permission_Associated_I_org_unit', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GPermission.associated_organization_units, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_permission
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'G_permission'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_permission_Associated_I_org_unit', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GPermission.associated_external_organizations, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_permission
    # The "remove_entity" is the foreign relationship table, in this case it is E_ext_org
    local_entity = 'G_permission'
    local_id = target.id
    remote_entity = 'E_ext_org'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_permission_Associated_E_ext_org', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GPermission.associated_external_organizations, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_permission
    # The "remove_entity" is the foreign relationship table, in this case it is E_ext_org
    local_entity = 'G_permission'
    local_id = target.id
    remote_entity = 'E_ext_org'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_permission_Associated_E_ext_org', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GProvisioningTask.aces, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_provisioning_task
    # The "remove_entity" is the foreign relationship table, in this case it is G_ace
    local_entity = 'G_provisioning_task'
    local_id = target.id
    remote_entity = 'G_ace'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_provisioning_task_G_ace', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GProvisioningTask.aces, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_provisioning_task
    # The "remove_entity" is the foreign relationship table, in this case it is G_ace
    local_entity = 'G_provisioning_task'
    local_id = target.id
    remote_entity = 'G_ace'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_provisioning_task_G_ace', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.aces, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_ace
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'G_ace'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_service_role_G_ace', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.aces, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_ace
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'G_ace'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_service_role_G_ace', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.job_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is I_job_role
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'I_job_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_job_role_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.job_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is I_job_role
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'I_job_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_job_role_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.external_job_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is E_job_role
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'E_job_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_job_role_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.external_job_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is E_job_role
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'E_job_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_job_role_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.organization_units, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.organization_units, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.external_organizations, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is E_ext_org
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'E_ext_org'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GServiceRole.external_organizations, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_service_role
    # The "remove_entity" is the foreign relationship table, in this case it is E_ext_org
    local_entity = 'G_service_role'
    local_id = target.id
    remote_entity = 'E_ext_org'
    remote_id = value.id
    audit_log.create_tie_audit_log('E_ext_org_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GUserGroup.users, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_user_group
    # The "remove_entity" is the foreign relationship table, in this case it is Zuser
    local_entity = 'G_user_group'
    local_id = target.id
    remote_entity = 'Zuser'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_user_group_Zuser', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GUserGroup.users, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_user_group
    # The "remove_entity" is the foreign relationship table, in this case it is Zuser
    local_entity = 'G_user_group'
    local_id = target.id
    remote_entity = 'Zuser'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_user_group_Zuser', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GUserGroup.report_subscriptions, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_user_group
    # The "remove_entity" is the foreign relationship table, in this case it is Zreport
    local_entity = 'G_user_group'
    local_id = target.id
    remote_entity = 'Zreport'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_user_group_Zreport', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(GUserGroup.report_subscriptions, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is G_user_group
    # The "remove_entity" is the foreign relationship table, in this case it is Zreport
    local_entity = 'G_user_group'
    local_id = target.id
    remote_entity = 'Zreport'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_user_group_Zreport', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(HrIntegration.service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Hr_integration
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'Hr_integration'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('Hr_integration_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(HrIntegration.service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Hr_integration
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'Hr_integration'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('Hr_integration_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(HrIntegration.other_organization_units, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Hr_integration
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'Hr_integration'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('Hr_integration_I_org_unit', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(HrIntegration.other_organization_units, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Hr_integration
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'Hr_integration'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('Hr_integration_I_org_unit', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(HrIntegration.key_profiles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Hr_integration
    # The "remove_entity" is the foreign relationship table, in this case it is C_key_profile
    local_entity = 'Hr_integration'
    local_id = target.id
    remote_entity = 'C_key_profile'
    remote_id = value.id
    audit_log.create_tie_audit_log('Hr_integration_C_key_profile', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(HrIntegration.key_profiles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Hr_integration
    # The "remove_entity" is the foreign relationship table, in this case it is C_key_profile
    local_entity = 'Hr_integration'
    local_id = target.id
    remote_entity = 'C_key_profile'
    remote_id = value.id
    audit_log.create_tie_audit_log('Hr_integration_C_key_profile', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IJobRole.service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_job_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_job_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_job_role_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IJobRole.service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_job_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_job_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_job_role_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IJobRole.requestable_service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_job_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_job_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_job_role_req_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IJobRole.requestable_service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_job_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_job_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_job_role_req_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(ILegalCompany.services, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_legal_company
    # The "remove_entity" is the foreign relationship table, in this case it is G_service
    local_entity = 'I_legal_company'
    local_id = target.id
    remote_entity = 'G_service'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_legal_company_G_service', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(ILegalCompany.services, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_legal_company
    # The "remove_entity" is the foreign relationship table, in this case it is G_service
    local_entity = 'I_legal_company'
    local_id = target.id
    remote_entity = 'G_service'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_legal_company_G_service', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(ILegalCompany.service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_legal_company
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_legal_company'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_legal_company_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(ILegalCompany.service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_legal_company
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_legal_company'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_legal_company_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IOrgGroup.organization_groups, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_org_group
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'I_org_group'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_I_org_group', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IOrgGroup.organization_groups, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_org_group
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'I_org_group'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_I_org_group', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IOrgUnit.requestable_services, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_org_unit
    # The "remove_entity" is the foreign relationship table, in this case it is G_service
    local_entity = 'I_org_unit'
    local_id = target.id
    remote_entity = 'G_service'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_G_service', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IOrgUnit.requestable_services, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_org_unit
    # The "remove_entity" is the foreign relationship table, in this case it is G_service
    local_entity = 'I_org_unit'
    local_id = target.id
    remote_entity = 'G_service'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_G_service', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IOrgUnit.predefined_service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_org_unit
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_org_unit'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(IOrgUnit.predefined_service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is I_org_unit
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'I_org_unit'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('I_org_unit_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(RDynRole.service_roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is R_dyn_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'R_dyn_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('R_dyn_role_G_service_role', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(RDynRole.service_roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is R_dyn_role
    # The "remove_entity" is the foreign relationship table, in this case it is G_service_role
    local_entity = 'R_dyn_role'
    local_id = target.id
    remote_entity = 'G_service_role'
    remote_id = value.id
    audit_log.create_tie_audit_log('R_dyn_role_G_service_role', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(RequestCartPermission.informed_persons, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Request_cart_permission
    # The "remove_entity" is the foreign relationship table, in this case it is D_person
    local_entity = 'Request_cart_permission'
    local_id = target.id
    remote_entity = 'D_person'
    remote_id = value.id
    audit_log.create_tie_audit_log('Request_cart_permission_D_person', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(RequestCartPermission.informed_persons, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Request_cart_permission
    # The "remove_entity" is the foreign relationship table, in this case it is D_person
    local_entity = 'Request_cart_permission'
    local_id = target.id
    remote_entity = 'D_person'
    remote_id = value.id
    audit_log.create_tie_audit_log('Request_cart_permission_D_person', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Useright.roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Useright
    # The "remove_entity" is the foreign relationship table, in this case it is Zrole
    local_entity = 'Useright'
    local_id = target.id
    remote_entity = 'Zrole'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zrole_Useright', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Useright.roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Useright
    # The "remove_entity" is the foreign relationship table, in this case it is Zrole
    local_entity = 'Useright'
    local_id = target.id
    remote_entity = 'Zrole'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zrole_Useright', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zreport.required_userights, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zreport
    # The "remove_entity" is the foreign relationship table, in this case it is Useright
    local_entity = 'Zreport'
    local_id = target.id
    remote_entity = 'Useright'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zreport_Useright', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zreport.required_userights, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zreport
    # The "remove_entity" is the foreign relationship table, in this case it is Useright
    local_entity = 'Zreport'
    local_id = target.id
    remote_entity = 'Useright'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zreport_Useright', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zrole.users, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zrole
    # The "remove_entity" is the foreign relationship table, in this case it is Zuser
    local_entity = 'Zrole'
    local_id = target.id
    remote_entity = 'Zuser'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_Zrole', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zrole.users, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zrole
    # The "remove_entity" is the foreign relationship table, in this case it is Zuser
    local_entity = 'Zrole'
    local_id = target.id
    remote_entity = 'Zuser'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_Zrole', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zrole.userights, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zrole
    # The "remove_entity" is the foreign relationship table, in this case it is Useright
    local_entity = 'Zrole'
    local_id = target.id
    remote_entity = 'Useright'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zrole_Useright', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zrole.userights, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zrole
    # The "remove_entity" is the foreign relationship table, in this case it is Useright
    local_entity = 'Zrole'
    local_id = target.id
    remote_entity = 'Useright'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zrole_Useright', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.usergroups, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is G_user_group
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'G_user_group'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_user_group_Zuser', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.usergroups, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is G_user_group
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'G_user_group'
    remote_id = value.id
    audit_log.create_tie_audit_log('G_user_group_Zuser', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.roles, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is Zrole
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'Zrole'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_Zrole', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.roles, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is Zrole
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'Zrole'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_Zrole', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.organizations, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_I_org_unit', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.organizations, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is I_org_unit
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'I_org_unit'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_I_org_unit', 'DELETE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.external_organizations, 'append')
def receive_after_append(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is E_ext_org
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'E_ext_org'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_E_ext_org', 'CREATE', local_entity, remote_entity, local_id, remote_id)

@db.event.listens_for(Zuser.external_organizations, 'remove')
def receive_after_remove(target, value, initiator):
    import datamaster.audit_log as audit_log
    # The "local_entity" is the target table class, in this case it is Zuser
    # The "remove_entity" is the foreign relationship table, in this case it is E_ext_org
    local_entity = 'Zuser'
    local_id = target.id
    remote_entity = 'E_ext_org'
    remote_id = value.id
    audit_log.create_tie_audit_log('Zuser_E_ext_org', 'DELETE', local_entity, remote_entity, local_id, remote_id)

ForeignKey = namedtuple('ForeignKey', 'table ref_id name')

db_to_mapper = {
    CCard : {
        'id': 'id',
        'card_new': 'card_new',
        'card_type_id': 'card_type_id',
        'card_type': 'card_type',
        'upn_code': 'upn_code',
        'identity_id': 'identity_id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'expiration_date': 'expiration_date',
        'identity_checked': 'identity_checked',
        'identity_checked_by': 'identity_checked_by',
        'description': 'description',
        'description2': 'description2',
        'status': 'status',
        'replacement_card': 'replacement_card',
        'replaced_card_id': 'replaced_card_id',
        'given_date': 'given_date',
        'given_by_id': 'given_by_id',
        'return_date': 'return_date',
        'activation_date': 'activation_date',
        'deactivation_date': 'deactivation_date',
        'deactivation_reason_code': 'deactivation_reason_code',
        'deactivation_reason': 'deactivation_reason',
        'card_organization_id': 'card_organization_id',
        'card_organization_name': 'card_organization_name',
        'user_cn': 'user_cn',
        'issuer_id': 'issuer_id',
        'issuer_cn': 'issuer_cn',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'valvira_id': 'valvira_id',
        'subject_serial_no': 'subject_serial_no',
        'sv_number': 'sv_number',
        'occupation_name': 'occupation_name',
        'email': 'email',
        'cert_serial1': 'cert_serial1',
        'cert_serial2': 'cert_serial2',
        'valid_until': 'valid_until',
        'token_number': 'token_number',
        'reg_ra_workstation_id': 'reg_ra_workstation_id',
        'reg_person_id': 'reg_person_id',
        'ra_open_cn': 'ra_open_cn',
        'ap_upn_old': 'ap_upn_old',
        'ap_pre_win': 'ap_pre_win',
        'internal_org_id': 'internal_org_id',
        'last_name_ad': 'last_name_ad',
        'first_name_ad': 'first_name_ad',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CCardIssuer : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CCardOrganization : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CCardType : {
        'id': 'id',
        'name': 'name',
        'service_id': 'service_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDevice : {
        'id': 'id',
        'name': 'name',
        'device_start_date': 'device_start_date',
        'device_end_date': 'device_end_date',
        'device_type': 'device_type',
        'device_subtype': 'device_subtype',
        'serial_no': 'serial_no',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDevicePerson : {
        'id': 'id',
        'device_id': 'device_id',
        'identity_id': 'identity_id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'given_date': 'given_date',
        'given_by_id': 'given_by_id',
        'return_date': 'return_date',
        'return_reason_code': 'return_reason_code',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDeviceSubtype : {
        'id': 'id',
        'device_type': 'device_type',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDeviceType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CKey : {
        'id': 'id',
        'key_new': 'key_new',
        'key_type_id': 'key_type_id',
        'key_type': 'key_type',
        'key_profile': 'key_profile',
        'serial_no': 'serial_no',
        'identity_id': 'identity_id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'expiration_date': 'expiration_date',
        'identity_checked': 'identity_checked',
        'identity_checked_by': 'identity_checked_by',
        'description': 'description',
        'description2': 'description2',
        'status': 'status',
        'replacement_key': 'replacement_key',
        'replaced_key_id': 'replaced_key_id',
        'given_date': 'given_date',
        'given_by_id': 'given_by_id',
        'return_date': 'return_date',
        'activation_date': 'activation_date',
        'deactivation_date': 'deactivation_date',
        'deactivation_reason_code': 'deactivation_reason_code',
        'deactivation_reason': 'deactivation_reason',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CKeyProfile : {
        'id': 'id',
        'key_type_id': 'key_type_id',
        'key_type': 'key_type',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CKeyType : {
        'id': 'id',
        'name': 'name',
        'service_id': 'service_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CWorkstation : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DAbsence : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'absence_type': 'absence_type',
        'start_date': 'start_date',
        'end_date': 'end_date',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DAuthMethod : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'authentication_level': 'authentication_level',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DCompetence : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DEducation : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DJobPeriod : {
        'id': 'id',
        'person_id': 'person_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jp_type': 'job_period_type',
        'is_manager': 'is_manager',
        'orgunit_id': 'orgunit_id',
        'job_title': 'job_title',
        'other_job_title': 'other_job_title',
        'specific_job_title': 'specific_job_title',
        'jobtitle_id': 'jobtitle_id',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'org_association_type': 'organization_association_type',
        'status': 'status',
        'manager_id': 'manager_id',
        'manager_email': 'manager_email',
        'manager_name': 'manager_name',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'report_manager_id': 'report_manager_id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'information_checked': 'information_checked',
        'contract': 'contract',
        'medicine_right': 'medicine_right',
        'absence_active': 'absence_active',
        'substitute_periods_active': 'substitute_periods_active',
        'hr_job_type': 'hr_job_type',
        'c_pasu': 'c_pasu',
        'full_part_per': 'full_part_per',
        'hr_work_time_type': 'hr_work_time_type',
        'operative_staff': 'operative_staff',
        'int_period_id': 'int_period_id',
        'int_job_title': 'int_job_title',
        'int_job_code': 'int_job_code',
        'int_job_code2': 'int_job_code2',
        'hr_profession_code': 'hr_profession_code',
        'hr_period_character_code': 'hr_period_character_code',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'pupo': 'pupo',
        'phone': 'phone',
        'card_valid_from': 'card_valid_from',
        'card_valid_to': 'card_valid_to',
        'exc_username': 'exc_username',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_location_id': 'exc_location_id',
        'exc_country_id': 'exc_country_id',
        'exc_primary_period': 'exc_primary_period',
        'inferred_primary_job_period': 'inferred_primary_job_period',
        'externally_managed': 'externally_managed',
        'exported_to_idm': 'exported_to_idm',
        'created_by_id': 'created_by_id',
        'is_primary_jobtitle': 'is_primary_jobtitle',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DJobPeriodAbsence : {
        'd_job_period_id': 'd_job_period_id',
        'valid_from': 'valid_from',
        'created_by': 'created_by',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
    },
    DJobPeriodSubstitute : {
        'id': 'id',
        'd_job_period_id': 'd_job_period_id',
        'd_substistute_person_id': 'd_substistute_person_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'is_backup': 'is_backup',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DJobtitle : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'name6': 'name6',
        'description': 'description',
        'jobrole_id': 'jobrole_id',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DMappingRule : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'mdm_source_id': 'mdm_source_id',
        'source_field': 'source_field',
        'target_table': 'target_table',
        'target_field': 'target_field',
        'target_datatype': 'target_datatype',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DPerson : {
        'id': 'id',
        'social_security_number': 'social_security_number',
        'personnel_no': 'personnel_number',
        'name_prefix': 'name_prefix',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name',
        'nickname': 'preferred_name',
        'identity_id': 'identity_id',
        'permanent': 'permanent',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'term_type': 'termination_type',
        'information_checked': 'information_checked',
        'email_active': 'email_active',
        'photo': 'photo',
        'username': 'username',
        'orgunit_id': 'orgunit_id',
        'email': 'email',
        'voice_address': 'pupo',
        'sv_number': 'sv_number',
        'other_address': 'other_address',
        'language_id': 'language_id',
        'status': 'status',
        'b_phone': 'b_phone',
        'b_mobile': 'b_mobile',
        'jr_start_date': 'jr_start_date',
        'is_manager': 'is_manager',
        'jobtitle_id': 'jobtitle_id',
        'jobtitle': 'jobtitle',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_email': 'manager_email',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'exc_location_id': 'exc_location_id',
        'remote_office': 'remote_office',
        'location_info': 'location_info',
        'home_street': 'home_street',
        'home_street2': 'home_street2',
        'home_post': 'home_post',
        'home_city': 'home_city',
        'home_state': 'home_state',
        'homecountry_id': 'homecountry_id',
        'identity_checked': 'identity_checked',
        'identitysource_id': 'identitysource_id',
        'personal_id': 'personal_id',
        'staff_oper_code': 'staff_oper_code',
        'full_time': 'full_time',
        'birth_date': 'birth_date',
        'gender': 'gender',
        'nationality_id': 'nationality_id',
        'int_job_title': 'int_job_title',
        'int_job_code': 'int_job_code',
        'int_code_code2': 'int_code_code2',
        'mdm_source_id': 'mdm_source_id',
        'mdm_person_id': 'mdm_person_id',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'attribute1': 'attribute1',
        'attribute2': 'attribute2',
        'attribute3': 'attribute3',
        'attribute4': 'attribute4',
        'attribute5': 'attribute5',
        'last_checking_date': 'last_checking_date',
        'last_import_date': 'last_import_date',
        'absence_status': 'absence_status',
        'exc_businessarea_id': 'exc_businessarea_id',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_country_id': 'exc_country_id',
        'waiting_manager_approval': 'waiting_manager_approval',
        'manager_approved_id': 'manager_approved_id',
        'manager_approval_timestamp': 'manager_approval_timestamp',
        'first_email_sent_timestamp': 'first_email_sent_timestamp',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DUserAuth : {
        'id': 'id',
        'device_id': 'device_id',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'person_id': 'person_id',
        'authmethod_id': 'authmethod_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EExtOrg : {
        'id': 'id',
        'header_row': 'header_row',
        'outsider': 'outsider',
        'name': 'name',
        'alias': 'alias',
        'company_code': 'company_code',
        'upper_ext_org_id': 'upper_ext_org_id',
        'ext_org_type_id': 'ext_org_type_id',
        'ext_org_profile': 'ext_org_profile',
        'virtual_org': 'virtual_org',
        'contract_id': 'contract_id',
        'favorite': 'favorite',
        'show_in_student': 'show_in_student',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
        'ext_superior_id': 'ext_superior_id',
        'substitute_active': 'substitute_active',
        'superior_person_id': 'manager_id',
        'superior_name': 'superior_name',
        'superior_email': 'superior_email',
        'subst_s_person_id': 'subst_manager_id',
        'subst_s_name': 'subst_s_name',
        'subst_s_email': 'subst_s_email',
        'teamleader_person_id': 'teamleader_person_id',
        'teamleader_name': 'teamleader_name',
        'teamleader_email': 'teamleader_email',
        'hr_manager_person_id': 'hr_manager_person_id',
        'hr_manager_name': 'hr_manager_name',
        'hr_manager_email': 'hr_manager_email',
        'ext_contact_name': 'ext_contact_name',
        'ext_contact_phone': 'ext_contact_phone',
        'ext_contact_email': 'ext_contact_email',
        'description': 'description',
        'unit_id_1': 'unit_id_1',
        'unit_id_2': 'unit_id_2',
        'costcenter_id': 'costcenter_id',
        'financial_code_1': 'financial_code_1',
        'location_id': 'location_id',
        'location_info': 'location_info',
        'exc_street': 'exc_street',
        'exc_street2': 'exc_street2',
        'exc_post': 'exc_post',
        'exc_city': 'exc_city',
        'exc_state': 'exc_state',
        'exc_country': 'exc_country',
        'exc_office_phone': 'exc_office_phone',
        'exc_office_fax': 'exc_office_fax',
        'exc_office_timezone': 'exc_office_timezone',
        'exc_site_category': 'exc_site_category',
        'needs_int_contact_approval': 'needs_int_contact_approval',
        'needs_ext_contact_approval': 'needs_ext_contact_approval',
        'default_language_id': 'default_language_id',
        'default_jobrole_id': 'default_jobrole_id',
        'default_domain': 'default_domain',
        'distinguishedname': 'distinguishedname',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EExtOrgType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EExternalPerson : {
        'id': 'id',
        'name_prefix': 'name_prefix',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name',
        'nickname': 'preferred_name',
        'identity_id': 'identity_id',
        'social_security_number': 'social_security_number',
        'personnel_no': 'personnel_number',
        'information_checked': 'information_checked',
        'student': 'student',
        'email_active': 'email_active',
        'photo': 'photo',
        'username': 'username',
        'orig_orgunit_id': 'orig_orgunit_id',
        'ext_org_id': 'ext_org_id',
        'e_job_role_id': 'e_job_role_id',
        'contract_id': 'contract_id',
        'tax_number': 'tax_number',
        'org_email': 'org_email',
        'b_phone': 'b_phone',
        'b_mobile': 'b_mobile',
        'voice_address': 'pupo',
        'sv_number': 'sv_number',
        'other_address': 'other_address',
        'ext_email': 'ext_email',
        'ext_superior': 'ext_superior',
        'ext_superior_email': 'ext_superior_email',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'term_type': 'termination_type',
        'recertification_date': 'recertification_date',
        'ext_phone': 'ext_phone',
        'language_id': 'language_id',
        'status': 'status',
        'e_status1': 'e_status1',
        'e_status2': 'e_status2',
        'e_status3': 'e_status3',
        'e_status4': 'e_status4',
        'orgunit_id': 'orgunit_id',
        'jr_start_date': 'jr_start_date',
        'is_manager': 'is_manager',
        'jobtitle': 'jobtitle',
        'jobtitle_id': 'jobtitle_id',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_location_id': 'exc_location_id',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_email': 'manager_email',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'remote_office': 'remote_office',
        'location_info': 'location_info',
        'home_street': 'home_street',
        'home_street2': 'home_street2',
        'home_post': 'home_post',
        'home_city': 'home_city',
        'home_state': 'home_state',
        'homecountry_id': 'homecountry_id',
        'home_emergency_contact': 'home_emergency_contact',
        'home_timezone': 'home_timezone',
        'identity_checked': 'identity_checked',
        'identitysource_id': 'identitysource_id',
        'personal_id': 'personal_id',
        'staff_oper_code': 'staff_oper_code',
        'full_time': 'full_time',
        'birth_date': 'birth_date',
        'gender': 'gender',
        'nationality_id': 'nationality_id',
        'mdm_source_id': 'mdm_source_id',
        'mdm_person_id': 'mdm_person_id',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'attribute1': 'attribute1',
        'attribute2': 'attribute2',
        'attribute3': 'attribute3',
        'attribute4': 'attribute4',
        'attribute5': 'attribute5',
        'last_checking_date': 'last_checking_date',
        'last_import_date': 'last_import_date',
        'absence_status': 'absence_status',
        'exc_businessarea_id': 'exc_businessarea_id',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_country_id': 'exc_country_id',
        'waiting_manager_approval': 'waiting_manager_approval',
        'manager_approved_id': 'manager_approved_id',
        'manager_approval_timestamp': 'manager_approval_timestamp',
        'first_email_sent_timestamp': 'first_email_sent_timestamp',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobFamily : {
        'id': 'id',
        'name': 'name',
        'int_code': 'int_code',
        'description': 'description',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jobfamily_class1': 'jobfamily_class1',
        'jobfamily_class2': 'jobfamily_class2',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobPeriod : {
        'id': 'id',
        'external_person_id': 'external_person_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'renewal_date': 'renewal_date',
        'jp_type': 'job_period_type',
        'is_manager': 'is_manager',
        'student': 'student',
        'outsider': 'outsider',
        'orgunit_id': 'orgunit_id',
        'ext_org_id': 'ext_org_id',
        'job_title': 'job_title',
        'other_job_title': 'other_job_title',
        'specific_job_title': 'specific_job_title',
        'jobtitle_id': 'jobtitle_id',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'org_association_type': 'organization_association_type',
        'status': 'status',
        'ext_manager_id': 'ext_manager_id',
        'manager_id': 'manager_id',
        'manager_email': 'manager_email',
        'manager_name': 'manager_name',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'report_manager_id': 'report_manager_id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'information_checked': 'information_checked',
        'contract': 'contract',
        'medicine_right': 'medicine_right',
        'hr_job_type': 'hr_job_type',
        'c_pasu': 'c_pasu',
        'full_part_per': 'full_part_per',
        'hr_work_time_type': 'hr_work_time_type',
        'operative_staff': 'operative_staff',
        'int_period_id': 'int_period_id',
        'int_job_title': 'int_job_title',
        'int_job_code': 'int_job_code',
        'int_job_code2': 'int_job_code2',
        'hr_profession_code': 'hr_profession_code',
        'hr_period_character_code': 'hr_period_character_code',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'pupo': 'pupo',
        'phone': 'phone',
        'card_valid_from': 'card_valid_from',
        'card_valid_to': 'card_valid_to',
        'can_get_credentials': 'can_get_credentials',
        'absence_active': 'absence_active',
        'exc_username': 'exc_username',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_location_id': 'exc_location_id',
        'exc_country_id': 'exc_country_id',
        'exc_primary_period': 'exc_primary_period',
        'inferred_primary_job_period': 'inferred_primary_job_period',
        'externally_managed': 'externally_managed',
        'exported_to_idm': 'exported_to_idm',
        'created_by_id': 'created_by_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobPeriodAbsence : {
        'e_job_period_id': 'e_job_period_id',
        'valid_from': 'valid_from',
        'created_by': 'created_by',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
    },
    EJobPeriodSubstitute : {
        'id': 'id',
        'e_job_period_id': 'e_job_period_id',
        'e_substistute_person_id': 'e_substistute_person_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'is_backup': 'is_backup',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobRole : {
        'id': 'id',
        'name': 'name',
        'int_code': 'int_code',
        'description': 'description',
        'global_jobrole': 'global_jobrole',
        'inheritance': 'inheritance',
        'orgunit_id': 'orgunit_id',
        'org_spec': 'org_spec',
        'upper_jobrole_id': 'upper_jobrole_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'provisioning': 'provisioning',
        'jobrole_class1': 'jobrole_class1',
        'jobrole_class2': 'jobrole_class2',
        'jobfamily_id': 'jobfamily_id',
        'status': 'status',
        'favorite': 'favorite',
        'org_group_id': 'org_group_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EOrgTypeService : {
        'id': 'id',
        'ext_org_type_id': 'ext_org_type_id',
        'service_id': 'service_id',
        'name': 'name',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ERequestCart : {
        'id': 'id',
        'person_id': 'person_id',
        'job_period_id': 'job_period_id',
        'requestor_id': 'requestor_id',
        'starting_date': 'starting_date',
        'manager_id': 'manager_id',
        'request_type': 'request_type',
        'reason': 'reason',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'approval_status': 'approval_status',
        'approval_comment': 'approval_comment',
        'subst_approver_id': 'subst_approver_id',
        'subst_approver_email': 'subst_approver_email',
        'forced_hidden': 'forced_hidden',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_time': 'approval_time',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_address': 'email_address',
        'reject_email_sent': 'reject_email_sent',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ERequestCartPermission : {
        'id': 'id',
        'request_cart_id': 'request_cart_id',
        'person_id': 'person_id',
        'service_role_id': 'service_role_id',
        'requestor_id': 'requestor_id',
        'request_activation_date': 'request_activation_date',
        'permission_request_type': 'permission_request_type',
        'service_id': 'service_id',
        'description': 'description',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'period_yr': 'period_yr',
        'approval_status': 'approval_status',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_timestamp': 'approval_timestamp',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_to_user_sent': 'email_to_user_sent',
        'email_to_superior_sent': 'email_to_superior_sent',
        'email_to_others_sent': 'email_to_others_sent',
        'email_to_service_manager_sent': 'email_to_service_manager_sent',
        'email_to_requestor_sent': 'email_to_requestor_sent',
        'reject_email_sent': 'reject_email_sent',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'associated_orgunits_json': 'associated_orgunits_json',
        'associated_ext_orgs_json': 'associated_ext_orgs_json',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GAccountAttribute : {
        'id': 'id',
        'person_useraccount_id': 'person_useraccount_id',
        'value': 'value',
        'value_p_old': 'value_p_old',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GAce : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ace_types': 'ace_types',
        'value': 'value',
        'ace_key': 'ace_key',
        'ace_key_priority': 'ace_key_priority',
        'attribute_source': 'attribute_source',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GAceAttribute : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'source_entity': 'source_entity',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GCountry : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'region': 'region',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GIdentity : {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'personal_id': 'personal_id',
        'id_validity': 'id_validity',
        'identitysource_id': 'identitysource_id',
        'identified_by': 'identified_by',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GIdentitySource : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'identitysourcetype': 'identitysourcetype',
        'identitysourceclass': 'identitysourceclass',
        'source_update': 'source_update',
        'resp_name': 'resp_name',
        'resp_email': 'resp_email',
        'resp_phone': 'resp_phone',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GLanguage : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'iso_code': 'iso_code',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GMdmRule : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GMdmSource : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'source_type': 'source_type',
        'source_class': 'source_class',
        'update_cycle': 'update_cycle',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GNotification : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'notification_type': 'notification_type',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GNotificationQueue : {
        'id': 'id',
        'notification_id': 'notification_id',
        'sender': 'sender',
        'recipients': 'recipients',
        'recipient_user': 'recipient_user',
        'recipient_user_group': 'recipient_user_group',
        'notification_data': 'notification_data',
        'notification_settings': 'notification_settings',
        'notification_body': 'notification_body',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'd_job_period_id': 'd_job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'notified_at': 'notified_at',
        'notification_queue_status': 'notification_queue_status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GPermission : {
        'id': 'id',
        'd_job_period_id': 'd_job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'service_role_id': 'service_role_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'period_yr': 'period_yr',
        'description': 'description',
        'preferred_implementor_id': 'preferred_implementor_id',
        'requested_by_id': 'requested_by_id',
        'requested_time': 'requested_time',
        'accepted_by_id': 'accepted_by_id',
        'accepted_by_time': 'accepted_by_time',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'username': 'username',
        'password': 'password',
        'imported': 'imported',
        'status': 'status',
        'request_cart_permission_id': 'request_cart_permission_id',
        'e_request_cart_permission_id': 'e_request_cart_permission_id',
        'delete_request_cart_permission_id': 'delete_request_cart_permission_id',
        'delete_e_request_cart_permission_id': 'delete_e_request_cart_permission_id',
        'd_job_period_substitute_id': 'd_job_period_substitute_id',
        'e_job_period_substitute_id': 'e_job_period_substitute_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GPersonUseraccount : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'username': 'username',
        'account_name': 'account_name',
        'account_uid': 'account_uid',
        'object_guid': 'object_guid',
        'dn': 'dn',
        'password': 'password',
        'service_id': 'service_id',
        'system_id': 'system_id',
        'inbound_attributes_json': 'inbound_attributes_json',
        'outbound_attributes_json': 'outbound_attributes_json',
        'old_inbound_attributes_json': 'old_inbound_attributes_json',
        'old_outbound_attributes_json': 'old_outbound_attributes_json',
        'account_created': 'account_created',
        'status': 'status',
        'internal': 'internal',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GProvisioningTask : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'd_job_period_id': 'd_job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'service_id': 'service_id',
        'task_type': 'task_type',
        'value_date': 'value_date',
        'service_role_id': 'service_role_id',
        'preferred_implementor_id': 'preferred_implementor_id',
        'request_description': 'request_description',
        'implementation_description': 'implementation_description',
        'implemented_by_id': 'implemented_by_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'provisioning_task_status': 'provisioning_task_status',
        'provisioning_type': 'provisioning_type',
        'system_id': 'system_id',
        'person_useraccount_id': 'person_useraccount_id',
        'inbound_attributes_json': 'inbound_attributes_json',
        'outbound_attributes_json': 'outbound_attributes_json',
        'diff_json': 'diff_json',
        'error_json': 'error_json',
        'integration_direction': 'integration_direction',
        'task_settings': 'task_settings',
        'username': 'username',
        'password': 'password',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_to_user_sent': 'email_to_user_sent',
        'email_to_superior_sent': 'email_to_superior_sent',
        'email_to_others_sent': 'email_to_others_sent',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'permission_id': 'permission_id',
        'request_cart_permission_id': 'request_cart_permission_id',
        'e_request_cart_permission_id': 'e_request_cart_permission_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GRegion : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GService : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'code': 'code',
        'status': 'status',
        'service_provider_id': 'service_provider_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'description': 'description',
        'service_class': 'service_class',
        'service_type_id': 'service_type_id',
        'system_id': 'system_id',
        'user_type': 'user_type',
        'register': 'register',
        'upper_service_id': 'upper_service_id',
        'externals_allowed': 'externals_allowed',
        'service_category': 'service_category',
        'approver_id': 'approver_id',
        'executor_id': 'executor_id',
        'revoke_type': 'revoke_type',
        'grace_period': 'grace_period',
        'minimum_period': 'minimum_period',
        'notification_id': 'notification_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceProvider : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'country_id': 'country_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceRequest : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'trans_date': 'trans_date',
        'severity': 'severity',
        'sr_class': 'sr_class',
        'sr_type': 'sr_type',
        'reported_by_name': 'reported_by_name',
        'reported_by_email': 'reported_by_email',
        'reported_by_phone': 'reported_by_phone',
        'int_resp_uid': 'int_resp_uid',
        'person_id': 'person_id',
        'service_id': 'service_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceResp : {
        'id': 'id',
        'person_name': 'person_name',
        'service_id': 'service_id',
        'servicerole_id': 'servicerole_id',
        'resp_class': 'resp_class',
        'resp_type': 'resp_type',
        'resp_name': 'resp_name',
        'resp_username': 'resp_username',
        'resp_email': 'resp_email',
        'resp_phone': 'resp_phone',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceRole : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'code': 'code',
        'status': 'status',
        'description': 'description',
        'service_id': 'service_id',
        'service_role_type': 'service_role_type',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'servicerole_class': 'servicerole_class',
        'virtual': 'virtual',
        'needs_srv_mgr_approval': 'needs_service_manager_approval',
        'authentication_level': 'authentication_level',
        'provisioning_type': 'provisioning_type',
        'aces_in_transaction': 'aces_in_transaction',
        'upper_servicerole_id': 'upper_servicerole_id',
        'chain_service_role_id': 'chain_service_role_id',
        'executor_id': 'executor_id',
        'favorite': 'favorite',
        'end_date_request': 'end_date_request',
        'period_request': 'period_request',
        'description_request': 'description_request',
        'associated_organizations_request': 'associated_organizations_request',
        'approver_id': 'approver_id',
        'subst_approver_id': 'subst_approver_id',
        'subst_approver_active': 'subst_approver_active',
        'subst_approver_email': 'subst_approver_email',
        'needs_superior_approval': 'needs_superior_approval',
        'notification_create': 'notification_create',
        'notification_update': 'notification_update',
        'notification_disable': 'notification_disable',
        'notification_delete': 'notification_delete',
        'notification_resetpassword': 'notification_resetpassword',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'owner_id': 'owner_id',
        'service_type': 'service_type',
        'externals_allowed': 'externals_allowed',
        'role_inheritance': 'role_inheritance',
        'site_collection': 'site_collection',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceTypeSroles : {
        'id': 'id',
        'service_type_id': 'service_type_id',
        'name': 'name',
        'description': 'description',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSrParameters : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'orgunit_id': 'orgunit_id',
        'resp_name': 'resp_name',
        'resp_email': 'resp_email',
        'resp_phone': 'resp_phone',
        'backup_name': 'backup_name',
        'backup_email': 'backup_email',
        'backup_phone': 'backup_phone',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'sla_level': 'sla_level',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSrTrans : {
        'id': 'id',
        'service_request_id': 'service_request_id',
        'name': 'name',
        'description': 'description',
        'trans_date': 'trans_date',
        'oper_uid': 'oper_uid',
        'oper_status': 'oper_status',
        'action_type': 'action_type',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSystem : {
        'id': 'id',
        'name': 'name',
        'system_type': 'system_type',
        'identifier': 'identifier',
        'description': 'description',
        'upper_system_id': 'upper_system_id',
        'inbound_schema_mapping_id': 'inbound_schema_mapping_id',
        'outbound_schema_mapping_id': 'outbound_schema_mapping_id',
        'config_json': 'config_json',
        'batch_job_path': 'batch_job_path',
        'revoke_type': 'revoke_type',
        'code': 'code',
        'integration_direction': 'integration_direction',
        'system_application_type': 'system_application_type',
        'priority': 'priority',
        'status': 'status',
        'notification_id': 'notification_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSystemSchema : {
        'id': 'id',
        'name': 'name',
        'module_path': 'module_path',
        'uid': 'uid',
        'description': 'description',
        'type': 'type',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSystemSchemaAttribute : {
        'id': 'id',
        'system_schema_id': 'system_schema_id',
        'name': 'name',
        'description': 'description',
        'datatype': 'datatype',
        'source_attribute': 'source_attribute',
        'destination_attribute': 'destination_attribute',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GUserGroup : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'usergroup_type': 'usergroup_type',
        'email': 'email',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrDesktopSubst : {
        'id': 'id',
        'hr_manager_person_number': 'hr_manager_person_number',
        'hr_subst_person_number': 'hr_subst_person_number',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'hr_subst_status': 'hr_subst_status',
        'hr_subst_message': 'hr_subst_message',
        'hr_source_file': 'hr_source_file',
        'hr_source_row': 'hr_source_row',
        'created_at': 'created_at',
        'manager_person_id': 'manager_person_id',
        'subst_person_id': 'subst_person_id',
        'manager_org_unit_manager_id': 'manager_org_unit_manager_id',
        'substitube_org_unit_manager_id': 'substitube_org_unit_manager_id',
        'substitute_id': 'substitute_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrImportRecord : {
        'id': 'id',
        'entity': 'entity',
        'source': 'source',
        'row': 'row',
        'source_entity_id': 'source_entity_id',
        'mapped_entity_id': 'mapped_entity_id',
        'system_entity': 'system_entity',
        'system_entity_id': 'system_entity_id',
        'parent_entity': 'parent_entity',
        'parent_source_entity_id': 'parent_source_entity_id',
        'parent_record_id': 'parent_record_id',
        'parent_system_entity': 'parent_system_entity',
        'parent_system_entity_id': 'parent_system_entity_id',
        'display_name': 'display_name',
        'error_code': 'error_code',
        'error_json': 'error_json',
        'previous_valid_hr_record_json': 'previous_valid_hr_record_json',
        'current_hr_record_json': 'current_hr_record_json',
        'fixed_record_json': 'fixed_record_json',
        'fixed_attributes_json': 'fixed_attributes_json',
        'mapped_attributes_json': 'mapped_attributes_json',
        'correctable_error': 'correctable_error',
        'imported_to_db': 'imported_to_db',
        'hr_status': 'hr_status',
        'previous_record_version_id': 'previous_record_version_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrIntegration : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'internal': 'internal',
        'surname': 'last_name',
        'first_names': 'first_names',
        'person_number': 'person_number',
        'social_security_number': 'social_security_number',
        'username': 'username',
        'email': 'email',
        'jobtitle_id': 'jobtitle_id',
        'hr_job_title': 'hr_job_title',
        'hr_official_job_title': 'hr_official_job_title',
        'org_unit_id': 'orgunit_id',
        'ext_org_id': 'ext_org_id',
        'legal_company_id': 'legal_company_id',
        'cost_center_id': 'cost_center_id',
        'location_id': 'location_id',
        'hire_start_date': 'hire_start_date',
        'job_start_date': 'job_start_date',
        'job_end_date': 'job_end_date',
        'manager_id': 'manager_id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'phone': 'phone',
        'voice_address': 'pupo',
        'other_address': 'other_address',
        'sv_number': 'sv_number',
        'hr_status': 'hr_status',
        'preferred_name': 'preferred_name',
        'street_address': 'street_address',
        'post_number': 'post_number',
        'city': 'city',
        'hr_profession_code': 'hr_profession_code',
        'position_type': 'position_type',
        'hr_work_time_type_lookup': 'hr_work_time_type',
        'job_type': 'job_type',
        'hr_job_type': 'hr_job_type',
        'full_part_per': 'full_part_per',
        'jp_character': 'job_period_character',
        'language_id': 'language_id',
        'report_area': 'report_area',
        'report_manager': 'report_manager',
        'report_manager_id': 'report_manager_id',
        'org_association_type': 'org_association_type',
        'ext_email': 'ext_email',
        'ext_phone': 'ext_phone',
        'ext_manager_id': 'ext_manager_id',
        'ext_manager_hetu': 'ext_manager_hetu',
        'ext_manager_name': 'ext_manager_name',
        'ext_org_code': 'ext_org_code',
        'ext_org_contract_number': 'ext_org_contract_number',
        'ext_org_name': 'ext_org_name',
        'orgunit_name': 'orgunit_name',
        'manager_hetu': 'manager_hetu',
        'manager_name': 'manager_name',
        'basic_applications': 'basic_applications',
        'other_data': 'other_data',
        'iloq_identifier': 'iloq_identifier',
        'other_key_1': 'other_key_1',
        'other_key_2': 'other_key_2',
        'personnel_card': 'personnel_card',
        'iloq_valid_till': 'iloq_valid_till',
        'additional_admittances': 'additional_admittances',
        'additional_admittances_validity': 'additional_admittances_validity',
        'additional_information_1': 'additional_information_1',
        'identifier': 'identifier',
        'valid_till': 'valid_till',
        'trans_date': 'trans_date',
        'batch_file_name': 'batch_file_name',
        'batch_messages': 'batch_messages',
        'record_source': 'record_source',
        'hr_language_lookup': 'hr_language_lookup',
        'hr_language_description': 'hr_language_description',
        'hr_job_period_id': 'hr_job_period_id',
        'hr_job_title_id': 'hr_job_title_id',
        'hr_department_id': 'hr_department_id',
        'hr_manager_id': 'hr_manager_id',
        'is_manager': 'is_manager',
        'job_position_type': 'job_position_type',
        'job_position': 'job_position',
        'jp_type': 'job_period_type',
        'jp_type_text': 'job_period_type_text',
        'jp_character_text': 'job_period_character_text',
        'person_number2': 'person_number2',
        'integration_timestamp': 'integration_timestamp',
        'pass2done': 'pass2done',
        'c_pasu': 'c_pasu',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrIntegrationVault : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'loaded': 'loaded',
        'dumped': 'dumped',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IBusinessArea : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ICostCenter : {
        'id': 'id',
        'legalcompany_id': 'legalcompany_id',
        'header_row': 'header_row',
        'int_code': 'int_code',
        'name': 'name',
        'description': 'description',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
        'classification4': 'classification4',
        'classification5': 'classification5',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IJobFamily : {
        'id': 'id',
        'name': 'name',
        'int_code': 'int_code',
        'description': 'description',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jobfamily_class1': 'jobfamily_class1',
        'jobfamily_class2': 'jobfamily_class2',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IJobRole : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'int_code': 'int_code',
        'description': 'description',
        'global_jobrole': 'global_jobrole',
        'inheritance': 'inheritance',
        'orgunit_id': 'orgunit_id',
        'org_spec': 'org_spec',
        'upper_jobrole_id': 'upper_jobrole_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jobrole_class1': 'jobrole_class1',
        'jobrole_class2': 'jobrole_class2',
        'jobfamily_id': 'jobfamily_id',
        'status': 'status',
        'org_group_id': 'org_group_id',
        'favorite': 'favorite',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ILegalCompany : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'official_company_id': 'official_company_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ILocation : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'upper_location_id': 'upper_location_id',
        'header_row': 'header_row',
        'location_id': 'location_id',
        'site_category': 'site_category',
        'virtual_location': 'virtual_location',
        'status': 'status',
        'street': 'street',
        'street2': 'street2',
        'post': 'post',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'office_phone': 'office_phone',
        'office_fax': 'office_fax',
        'office_timezone': 'office_timezone',
        'site_manager_id': 'site_manager_id',
        'site_manager_name': 'site_manager_name',
        'site_manager_email': 'site_manager_email',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IManagerPerProfession : {
        'id': 'id',
        'orgunit_id': 'orgunit_id',
        'hr_profession_code': 'hr_profession_code',
        'i_job_role_id': 'i_job_role_id',
        'e_job_role_id': 'e_job_role_id',
        'superior_person_id': 'superior_person_id',
        'superior_name': 'superior_name',
        'superior_email': 'superior_email',
        'subst_s_person_id': 'subst_s_person_id',
        'subst_s_name': 'subst_s_name',
        'subst_s_email': 'subst_s_email',
        'substitute_active': 'substitute_active',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgGroup : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgUnit : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'description': 'description',
        'upper_orgunit_id': 'upper_orgunit_id',
        'unit_id': 'unit_id',
        'orgtype_id': 'orgtype_id',
        'inheritance': 'inheritance',
        'header_row': 'header_row',
        'pilot': 'pilot',
        'org_level': 'org_level',
        'virtual_unit': 'virtual_unit',
        'businessarea': 'businessarea',
        'legalcompany_id': 'legalcompany_id',
        'costcenter_id': 'costcenter_id',
        'location_id': 'location_id',
        'it_support_email': 'it_support_email',
        'favorite': 'favorite',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
        'org_spec': 'org_spec',
        'unit_id_1': 'unit_id_1',
        'unit_id_2': 'unit_id_2',
        'financial_code_1': 'financial_code_1',
        'location_info': 'location_info',
        'exc_street': 'exc_street',
        'exc_street2': 'exc_street2',
        'exc_post': 'exc_post',
        'exc_city': 'exc_city',
        'exc_state': 'exc_state',
        'exc_country': 'exc_country',
        'exc_office_phone': 'exc_office_phone',
        'exc_office_fax': 'exc_office_fax',
        'exc_office_timezone': 'exc_office_timezone',
        'exc_site_category': 'exc_site_category',
        'superior_person_id': 'manager_id',
        'superior_name': 'superior_name',
        'superior_email': 'superior_email',
        'subst_s_person_id': 'subst_manager_id',
        'subst_s_name': 'subst_s_name',
        'subst_s_email': 'subst_s_email',
        'substitute_active': 'substitute_active',
        'teamleader_person_id': 'teamleader_person_id',
        'teamleader_name': 'teamleader_name',
        'teamleader_email': 'teamleader_email',
        'hr_manager_person_id': 'hr_manager_person_id',
        'hr_manager_name': 'hr_manager_name',
        'hr_manager_email': 'hr_manager_email',
        'default_language_id': 'default_language_id',
        'default_jobrole_id': 'default_jobrole_id',
        'default_domain': 'default_domain',
        'provisioning_dirty': 'provisioning_dirty',
        'distinguishedname': 'distinguishedname',
        'codeserver_oid': 'codeserver_oid',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgUnitManager : {
        'id': 'id',
        'org_unit_id': 'org_unit_id',
        'manager_id': 'manager_id',
        'manager_type': 'manager_type',
        'activation_date': 'activation_date',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgUnitManagerSubstitute : {
        'id': 'id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'subst_manager_id': 'subst_manager_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'hr_desktop_subst': 'hr_desktop_subst',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    OneTimeLink : {
        'id': 'id',
        'auth_token': 'auth_token',
        'entity_name': 'entity_name',
        'entity_id': 'entity_id',
        'expires': 'expires',
        'created_timestamp': 'created_timestamp',
        'used_timestamp': 'used_timestamp',
        'zuser_id': 'zuser_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    PRequestCart : {
        'id': 'id',
        'job_period_id': 'job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'social_security_number': 'social_security_number',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'internal': 'internal',
        'request_ssn': 'request_ssn',
        'requestor_id': 'requestor_id',
        'starting_date': 'starting_date',
        'manager_ssn': 'manager_ssn',
        'description': 'description',
        'preferred_implementor_ssn': 'preferred_implementor_ssn',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'src_trans_date': 'src_trans_date',
        'status_in': 'status_in',
        'request_cart_id': 'request_cart_id',
        'e_request_cart_id': 'e_request_cart_id',
        'hr_job_period_id': 'hr_job_period_id',
        'out_status': 'out_status',
        'out_status_error_msg': 'out_status_error_msg',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    PRequestCartRow : {
        'id': 'id',
        'p_request_cart_id': 'p_request_cart_id',
        'permission_request_type': 'permission_request_type',
        'service_role_id': 'service_role_id',
        'description': 'description',
        'preferred_implementor_ssn': 'preferred_implementor_ssn',
        'status_in': 'status_in',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'out_status': 'out_status',
        'out_date': 'out_date',
        'request_cart_row_id': 'request_cart_row_id',
        'e_request_cart_row_id': 'e_request_cart_row_id',
        'out_status_process': 'out_status_process',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RDynRole : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'rule': 'rule',
        'approval_status': 'approval_status',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ROrgDac : {
        'id': 'id',
        'orgunit_id': 'orgunit_id',
        'name': 'name',
        'dedicated': 'dedicated',
        'key1_min_value': 'key1_min_value',
        'key1_max_value': 'key1_max_value',
        'key2_min_value': 'key2_min_value',
        'key2_max_value': 'key2_max_value',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ROrgService : {
        'id': 'id',
        'name': 'name',
        'orgunit_id': 'orgunit_id',
        'service_id': 'service_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ROrgTypeService : {
        'id': 'id',
        'name': 'name',
        'org_type_id': 'org_type_id',
        'service_id': 'service_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RSodException : {
        'id': 'id',
        'internal': 'internal',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'sod_rule_id': 'sod_rule_id',
        'exc_approved': 'exc_approved',
        'exc_approver_id': 'exc_approver_id',
        'exc_approver_desc': 'exc_approver_desc',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RSodRule : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'sod_rule_class_id': 'sod_rule_class_id',
        'role1_id': 'role1_id',
        'role2_id': 'role2_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RSodRuleClass : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RUserDac : {
        'id': 'id',
        'person_id': 'person_id',
        'name': 'name',
        'dedicated': 'dedicated',
        'key1_min_value': 'key1_min_value',
        'key1_max_value': 'key1_max_value',
        'key2_min_value': 'key2_min_value',
        'key2_max_value': 'key2_max_value',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RequestCart : {
        'id': 'id',
        'person_id': 'person_id',
        'job_period_id': 'job_period_id',
        'requestor_id': 'requestor_id',
        'starting_date': 'starting_date',
        'manager_id': 'manager_id',
        'request_type': 'request_type',
        'reason': 'reason',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'approval_status': 'approval_status',
        'approval_comment': 'approval_comment',
        'subst_approver_id': 'subst_approver_id',
        'subst_approver_email': 'subst_approver_email',
        'forced_hidden': 'forced_hidden',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_time': 'approval_time',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_address': 'email_address',
        'reject_email_sent': 'reject_email_sent',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RequestCartPermission : {
        'id': 'id',
        'request_cart_id': 'request_cart_id',
        'person_id': 'person_id',
        'service_role_id': 'service_role_id',
        'requestor_id': 'requestor_id',
        'request_activation_date': 'request_activation_date',
        'permission_request_type': 'permission_request_type',
        'service_id': 'service_id',
        'description': 'description',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'period_yr': 'period_yr',
        'approval_status': 'approval_status',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_timestamp': 'approval_timestamp',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_to_user_sent': 'email_to_user_sent',
        'email_to_superior_sent': 'email_to_superior_sent',
        'email_to_others_sent': 'email_to_others_sent',
        'email_to_service_manager_sent': 'email_to_service_manager_sent',
        'email_to_requestor_sent': 'email_to_requestor_sent',
        'reject_email_sent': 'reject_email_sent',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'associated_orgunits_json': 'associated_orgunits_json',
        'associated_ext_orgs_json': 'associated_ext_orgs_json',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDDepartmentWeekMaxQuantity : {
        'id': 'id',
        'department_id': 'department_id',
        'week': 'week',
        'quantity': 'quantity',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDStudyProgramme : {
        'id': 'id',
        'name': 'name',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipPlacement : {
        'id': 'id',
        'traineeship_placement_request_id': 'traineeship_placement_request_id',
        'student_slot_number': 'student_slot_number',
        'part_number': 'part_number',
        'department_id': 'department_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'coordinator_id': 'coordinator_id',
        'traineeship_type_id': 'traineeship_type_id',
        'responsible_person_id': 'responsible_person_id',
        'guiding_teacher_id': 'guiding_teacher_id',
        'student_id': 'student_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipPlacementRequest : {
        'id': 'id',
        'traineeship_request_id': 'traineeship_request_id',
        'office_id': 'office_id',
        'division_id': 'division_id',
        'department_id': 'department_id',
        'semester_information': 'semester_information',
        'traineeship_type_id': 'traineeship_type_id',
        'traineeship_type_other': 'traineeship_type_other',
        'length_weeks': 'length_weeks',
        'start_date': 'start_date',
        'end_date': 'end_date',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipRequest : {
        'id': 'id',
        'school_id': 'school_id',
        'study_programme_id': 'study_programme_id',
        'course_name': 'course_name',
        'includes_skill_test': 'includes_skill_test',
        'skill_test_type': 'skill_test_type',
        'advanced_course': 'advanced_course',
        'international_student': 'international_student',
        'international_school_name': 'international_school_name',
        'extra_information': 'extra_information',
        'quantity_requested': 'quantity_requested',
        'request_status': 'request_status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipType : {
        'id': 'id',
        'name': 'name',
        'upper_traineeship_type_id': 'upper_traineeship_type_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Useright : {
        'id': 'id',
        'name': 'name',
        'extra1': 'extra1',
        'extra2': 'extra2',
        'dn': 'distinguished_name',
        'righttype_lookup': 'righttype_lookup',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Zreport : {
        'id': 'id',
        'name': 'name',
        'name5': 'name5',
        'name6': 'name6',
        'description': 'description',
        'reportfile': 'reportfile',
        'url': 'url',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Zrole : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'dn': 'distinguished_name',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Zuser : {
        'id': 'id',
        'name': 'username',
        'firstname': 'first_names',
        'lastname': 'last_name',
        'email': 'email',
        'address': 'address',
        'phone': 'phone',
        'startdate': 'start_date',
        'force_change_password': 'force_change_password',
        'internal': 'internal',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'status': 'status',
        'liferay_uid': 'liferay_uid',
        'password': 'password',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
}
mapper_to_db = {
    CCard : {
        'id': 'id',
        'card_new': 'card_new',
        'card_type_id': 'card_type_id',
        'card_type': 'card_type',
        'upn_code': 'upn_code',
        'identity_id': 'identity_id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'expiration_date': 'expiration_date',
        'identity_checked': 'identity_checked',
        'identity_checked_by': 'identity_checked_by',
        'description': 'description',
        'description2': 'description2',
        'status': 'status',
        'replacement_card': 'replacement_card',
        'replaced_card_id': 'replaced_card_id',
        'given_date': 'given_date',
        'given_by_id': 'given_by_id',
        'return_date': 'return_date',
        'activation_date': 'activation_date',
        'deactivation_date': 'deactivation_date',
        'deactivation_reason_code': 'deactivation_reason_code',
        'deactivation_reason': 'deactivation_reason',
        'card_organization_id': 'card_organization_id',
        'card_organization_name': 'card_organization_name',
        'user_cn': 'user_cn',
        'issuer_id': 'issuer_id',
        'issuer_cn': 'issuer_cn',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'valvira_id': 'valvira_id',
        'subject_serial_no': 'subject_serial_no',
        'sv_number': 'sv_number',
        'occupation_name': 'occupation_name',
        'email': 'email',
        'cert_serial1': 'cert_serial1',
        'cert_serial2': 'cert_serial2',
        'valid_until': 'valid_until',
        'token_number': 'token_number',
        'reg_ra_workstation_id': 'reg_ra_workstation_id',
        'reg_person_id': 'reg_person_id',
        'ra_open_cn': 'ra_open_cn',
        'ap_upn_old': 'ap_upn_old',
        'ap_pre_win': 'ap_pre_win',
        'internal_org_id': 'internal_org_id',
        'last_name_ad': 'last_name_ad',
        'first_name_ad': 'first_name_ad',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CCardIssuer : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CCardOrganization : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CCardType : {
        'id': 'id',
        'name': 'name',
        'service_id': 'service_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDevice : {
        'id': 'id',
        'name': 'name',
        'device_start_date': 'device_start_date',
        'device_end_date': 'device_end_date',
        'device_type': 'device_type',
        'device_subtype': 'device_subtype',
        'serial_no': 'serial_no',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDevicePerson : {
        'id': 'id',
        'device_id': 'device_id',
        'identity_id': 'identity_id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'given_date': 'given_date',
        'given_by_id': 'given_by_id',
        'return_date': 'return_date',
        'return_reason_code': 'return_reason_code',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDeviceSubtype : {
        'id': 'id',
        'device_type': 'device_type',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CDeviceType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CKey : {
        'id': 'id',
        'key_new': 'key_new',
        'key_type_id': 'key_type_id',
        'key_type': 'key_type',
        'key_profile': 'key_profile',
        'serial_no': 'serial_no',
        'identity_id': 'identity_id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'expiration_date': 'expiration_date',
        'identity_checked': 'identity_checked',
        'identity_checked_by': 'identity_checked_by',
        'description': 'description',
        'description2': 'description2',
        'status': 'status',
        'replacement_key': 'replacement_key',
        'replaced_key_id': 'replaced_key_id',
        'given_date': 'given_date',
        'given_by_id': 'given_by_id',
        'return_date': 'return_date',
        'activation_date': 'activation_date',
        'deactivation_date': 'deactivation_date',
        'deactivation_reason_code': 'deactivation_reason_code',
        'deactivation_reason': 'deactivation_reason',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CKeyProfile : {
        'id': 'id',
        'key_type_id': 'key_type_id',
        'key_type': 'key_type',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CKeyType : {
        'id': 'id',
        'name': 'name',
        'service_id': 'service_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    CWorkstation : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DAbsence : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'absence_type': 'absence_type',
        'start_date': 'start_date',
        'end_date': 'end_date',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DAuthMethod : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'authentication_level': 'authentication_level',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DCompetence : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DEducation : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DJobPeriod : {
        'id': 'id',
        'person_id': 'person_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'job_period_type': 'jp_type',
        'is_manager': 'is_manager',
        'orgunit_id': 'orgunit_id',
        'job_title': 'job_title',
        'other_job_title': 'other_job_title',
        'specific_job_title': 'specific_job_title',
        'jobtitle_id': 'jobtitle_id',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'organization_association_type': 'org_association_type',
        'status': 'status',
        'manager_id': 'manager_id',
        'manager_email': 'manager_email',
        'manager_name': 'manager_name',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'report_manager_id': 'report_manager_id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'information_checked': 'information_checked',
        'contract': 'contract',
        'medicine_right': 'medicine_right',
        'absence_active': 'absence_active',
        'substitute_periods_active': 'substitute_periods_active',
        'hr_job_type': 'hr_job_type',
        'c_pasu': 'c_pasu',
        'full_part_per': 'full_part_per',
        'hr_work_time_type': 'hr_work_time_type',
        'operative_staff': 'operative_staff',
        'int_period_id': 'int_period_id',
        'int_job_title': 'int_job_title',
        'int_job_code': 'int_job_code',
        'int_job_code2': 'int_job_code2',
        'hr_profession_code': 'hr_profession_code',
        'hr_period_character_code': 'hr_period_character_code',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'pupo': 'pupo',
        'phone': 'phone',
        'card_valid_from': 'card_valid_from',
        'card_valid_to': 'card_valid_to',
        'exc_username': 'exc_username',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_location_id': 'exc_location_id',
        'exc_country_id': 'exc_country_id',
        'exc_primary_period': 'exc_primary_period',
        'inferred_primary_job_period': 'inferred_primary_job_period',
        'externally_managed': 'externally_managed',
        'exported_to_idm': 'exported_to_idm',
        'created_by_id': 'created_by_id',
        'is_primary_jobtitle': 'is_primary_jobtitle',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DJobPeriodAbsence : {
        'd_job_period_id': 'd_job_period_id',
        'valid_from': 'valid_from',
        'created_by': 'created_by',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
    },
    DJobPeriodSubstitute : {
        'id': 'id',
        'd_job_period_id': 'd_job_period_id',
        'd_substistute_person_id': 'd_substistute_person_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'is_backup': 'is_backup',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DJobtitle : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'name6': 'name6',
        'description': 'description',
        'jobrole_id': 'jobrole_id',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DMappingRule : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'mdm_source_id': 'mdm_source_id',
        'source_field': 'source_field',
        'target_table': 'target_table',
        'target_field': 'target_field',
        'target_datatype': 'target_datatype',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DPerson : {
        'id': 'id',
        'social_security_number': 'social_security_number',
        'personnel_number': 'personnel_no',
        'name_prefix': 'name_prefix',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name',
        'preferred_name': 'nickname',
        'identity_id': 'identity_id',
        'permanent': 'permanent',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'termination_type': 'term_type',
        'information_checked': 'information_checked',
        'email_active': 'email_active',
        'photo': 'photo',
        'username': 'username',
        'orgunit_id': 'orgunit_id',
        'email': 'email',
        'pupo': 'voice_address',
        'sv_number': 'sv_number',
        'other_address': 'other_address',
        'language_id': 'language_id',
        'status': 'status',
        'b_phone': 'b_phone',
        'b_mobile': 'b_mobile',
        'jr_start_date': 'jr_start_date',
        'is_manager': 'is_manager',
        'jobtitle_id': 'jobtitle_id',
        'jobtitle': 'jobtitle',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_email': 'manager_email',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'exc_location_id': 'exc_location_id',
        'remote_office': 'remote_office',
        'location_info': 'location_info',
        'home_street': 'home_street',
        'home_street2': 'home_street2',
        'home_post': 'home_post',
        'home_city': 'home_city',
        'home_state': 'home_state',
        'homecountry_id': 'homecountry_id',
        'identity_checked': 'identity_checked',
        'identitysource_id': 'identitysource_id',
        'personal_id': 'personal_id',
        'staff_oper_code': 'staff_oper_code',
        'full_time': 'full_time',
        'birth_date': 'birth_date',
        'gender': 'gender',
        'nationality_id': 'nationality_id',
        'int_job_title': 'int_job_title',
        'int_job_code': 'int_job_code',
        'int_code_code2': 'int_code_code2',
        'mdm_source_id': 'mdm_source_id',
        'mdm_person_id': 'mdm_person_id',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'attribute1': 'attribute1',
        'attribute2': 'attribute2',
        'attribute3': 'attribute3',
        'attribute4': 'attribute4',
        'attribute5': 'attribute5',
        'last_checking_date': 'last_checking_date',
        'last_import_date': 'last_import_date',
        'absence_status': 'absence_status',
        'exc_businessarea_id': 'exc_businessarea_id',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_country_id': 'exc_country_id',
        'waiting_manager_approval': 'waiting_manager_approval',
        'manager_approved_id': 'manager_approved_id',
        'manager_approval_timestamp': 'manager_approval_timestamp',
        'first_email_sent_timestamp': 'first_email_sent_timestamp',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    DUserAuth : {
        'id': 'id',
        'device_id': 'device_id',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'person_id': 'person_id',
        'authmethod_id': 'authmethod_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EExtOrg : {
        'id': 'id',
        'header_row': 'header_row',
        'outsider': 'outsider',
        'name': 'name',
        'alias': 'alias',
        'company_code': 'company_code',
        'upper_ext_org_id': 'upper_ext_org_id',
        'ext_org_type_id': 'ext_org_type_id',
        'ext_org_profile': 'ext_org_profile',
        'virtual_org': 'virtual_org',
        'contract_id': 'contract_id',
        'favorite': 'favorite',
        'show_in_student': 'show_in_student',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
        'ext_superior_id': 'ext_superior_id',
        'substitute_active': 'substitute_active',
        'manager_id': 'superior_person_id',
        'superior_name': 'superior_name',
        'superior_email': 'superior_email',
        'subst_manager_id': 'subst_s_person_id',
        'subst_s_name': 'subst_s_name',
        'subst_s_email': 'subst_s_email',
        'teamleader_person_id': 'teamleader_person_id',
        'teamleader_name': 'teamleader_name',
        'teamleader_email': 'teamleader_email',
        'hr_manager_person_id': 'hr_manager_person_id',
        'hr_manager_name': 'hr_manager_name',
        'hr_manager_email': 'hr_manager_email',
        'ext_contact_name': 'ext_contact_name',
        'ext_contact_phone': 'ext_contact_phone',
        'ext_contact_email': 'ext_contact_email',
        'description': 'description',
        'unit_id_1': 'unit_id_1',
        'unit_id_2': 'unit_id_2',
        'costcenter_id': 'costcenter_id',
        'financial_code_1': 'financial_code_1',
        'location_id': 'location_id',
        'location_info': 'location_info',
        'exc_street': 'exc_street',
        'exc_street2': 'exc_street2',
        'exc_post': 'exc_post',
        'exc_city': 'exc_city',
        'exc_state': 'exc_state',
        'exc_country': 'exc_country',
        'exc_office_phone': 'exc_office_phone',
        'exc_office_fax': 'exc_office_fax',
        'exc_office_timezone': 'exc_office_timezone',
        'exc_site_category': 'exc_site_category',
        'needs_int_contact_approval': 'needs_int_contact_approval',
        'needs_ext_contact_approval': 'needs_ext_contact_approval',
        'default_language_id': 'default_language_id',
        'default_jobrole_id': 'default_jobrole_id',
        'default_domain': 'default_domain',
        'distinguishedname': 'distinguishedname',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EExtOrgType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EExternalPerson : {
        'id': 'id',
        'name_prefix': 'name_prefix',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name',
        'preferred_name': 'nickname',
        'identity_id': 'identity_id',
        'social_security_number': 'social_security_number',
        'personnel_number': 'personnel_no',
        'information_checked': 'information_checked',
        'student': 'student',
        'email_active': 'email_active',
        'photo': 'photo',
        'username': 'username',
        'orig_orgunit_id': 'orig_orgunit_id',
        'ext_org_id': 'ext_org_id',
        'e_job_role_id': 'e_job_role_id',
        'contract_id': 'contract_id',
        'tax_number': 'tax_number',
        'org_email': 'org_email',
        'b_phone': 'b_phone',
        'b_mobile': 'b_mobile',
        'pupo': 'voice_address',
        'sv_number': 'sv_number',
        'other_address': 'other_address',
        'ext_email': 'ext_email',
        'ext_superior': 'ext_superior',
        'ext_superior_email': 'ext_superior_email',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'termination_type': 'term_type',
        'recertification_date': 'recertification_date',
        'ext_phone': 'ext_phone',
        'language_id': 'language_id',
        'status': 'status',
        'e_status1': 'e_status1',
        'e_status2': 'e_status2',
        'e_status3': 'e_status3',
        'e_status4': 'e_status4',
        'orgunit_id': 'orgunit_id',
        'jr_start_date': 'jr_start_date',
        'is_manager': 'is_manager',
        'jobtitle': 'jobtitle',
        'jobtitle_id': 'jobtitle_id',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_location_id': 'exc_location_id',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_email': 'manager_email',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'remote_office': 'remote_office',
        'location_info': 'location_info',
        'home_street': 'home_street',
        'home_street2': 'home_street2',
        'home_post': 'home_post',
        'home_city': 'home_city',
        'home_state': 'home_state',
        'homecountry_id': 'homecountry_id',
        'home_emergency_contact': 'home_emergency_contact',
        'home_timezone': 'home_timezone',
        'identity_checked': 'identity_checked',
        'identitysource_id': 'identitysource_id',
        'personal_id': 'personal_id',
        'staff_oper_code': 'staff_oper_code',
        'full_time': 'full_time',
        'birth_date': 'birth_date',
        'gender': 'gender',
        'nationality_id': 'nationality_id',
        'mdm_source_id': 'mdm_source_id',
        'mdm_person_id': 'mdm_person_id',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'attribute1': 'attribute1',
        'attribute2': 'attribute2',
        'attribute3': 'attribute3',
        'attribute4': 'attribute4',
        'attribute5': 'attribute5',
        'last_checking_date': 'last_checking_date',
        'last_import_date': 'last_import_date',
        'absence_status': 'absence_status',
        'exc_businessarea_id': 'exc_businessarea_id',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_country_id': 'exc_country_id',
        'waiting_manager_approval': 'waiting_manager_approval',
        'manager_approved_id': 'manager_approved_id',
        'manager_approval_timestamp': 'manager_approval_timestamp',
        'first_email_sent_timestamp': 'first_email_sent_timestamp',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobFamily : {
        'id': 'id',
        'name': 'name',
        'int_code': 'int_code',
        'description': 'description',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jobfamily_class1': 'jobfamily_class1',
        'jobfamily_class2': 'jobfamily_class2',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobPeriod : {
        'id': 'id',
        'external_person_id': 'external_person_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'renewal_date': 'renewal_date',
        'job_period_type': 'jp_type',
        'is_manager': 'is_manager',
        'student': 'student',
        'outsider': 'outsider',
        'orgunit_id': 'orgunit_id',
        'ext_org_id': 'ext_org_id',
        'job_title': 'job_title',
        'other_job_title': 'other_job_title',
        'specific_job_title': 'specific_job_title',
        'jobtitle_id': 'jobtitle_id',
        'jobfamily_id': 'jobfamily_id',
        'jobrole_id': 'jobrole_id',
        'job_type': 'job_type',
        'organization_association_type': 'org_association_type',
        'status': 'status',
        'ext_manager_id': 'ext_manager_id',
        'manager_id': 'manager_id',
        'manager_email': 'manager_email',
        'manager_name': 'manager_name',
        'subst_manager_id': 'subst_manager_id',
        'subst_manager_name': 'subst_manager_name',
        'subst_manager_email': 'subst_manager_email',
        'substitute_active': 'substitute_active',
        'report_manager_id': 'report_manager_id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'information_checked': 'information_checked',
        'contract': 'contract',
        'medicine_right': 'medicine_right',
        'hr_job_type': 'hr_job_type',
        'c_pasu': 'c_pasu',
        'full_part_per': 'full_part_per',
        'hr_work_time_type': 'hr_work_time_type',
        'operative_staff': 'operative_staff',
        'int_period_id': 'int_period_id',
        'int_job_title': 'int_job_title',
        'int_job_code': 'int_job_code',
        'int_job_code2': 'int_job_code2',
        'hr_profession_code': 'hr_profession_code',
        'hr_period_character_code': 'hr_period_character_code',
        'flag1': 'flag1',
        'flag2': 'flag2',
        'flag3': 'flag3',
        'flag4': 'flag4',
        'flag5': 'flag5',
        'original_source': 'original_source',
        'pupo': 'pupo',
        'phone': 'phone',
        'card_valid_from': 'card_valid_from',
        'card_valid_to': 'card_valid_to',
        'can_get_credentials': 'can_get_credentials',
        'absence_active': 'absence_active',
        'exc_username': 'exc_username',
        'exc_legalcompany_id': 'exc_legalcompany_id',
        'exc_costcenter_id': 'exc_costcenter_id',
        'exc_location_id': 'exc_location_id',
        'exc_country_id': 'exc_country_id',
        'exc_primary_period': 'exc_primary_period',
        'inferred_primary_job_period': 'inferred_primary_job_period',
        'externally_managed': 'externally_managed',
        'exported_to_idm': 'exported_to_idm',
        'created_by_id': 'created_by_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobPeriodAbsence : {
        'e_job_period_id': 'e_job_period_id',
        'valid_from': 'valid_from',
        'created_by': 'created_by',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
    },
    EJobPeriodSubstitute : {
        'id': 'id',
        'e_job_period_id': 'e_job_period_id',
        'e_substistute_person_id': 'e_substistute_person_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'is_backup': 'is_backup',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EJobRole : {
        'id': 'id',
        'name': 'name',
        'int_code': 'int_code',
        'description': 'description',
        'global_jobrole': 'global_jobrole',
        'inheritance': 'inheritance',
        'orgunit_id': 'orgunit_id',
        'org_spec': 'org_spec',
        'upper_jobrole_id': 'upper_jobrole_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'provisioning': 'provisioning',
        'jobrole_class1': 'jobrole_class1',
        'jobrole_class2': 'jobrole_class2',
        'jobfamily_id': 'jobfamily_id',
        'status': 'status',
        'favorite': 'favorite',
        'org_group_id': 'org_group_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    EOrgTypeService : {
        'id': 'id',
        'ext_org_type_id': 'ext_org_type_id',
        'service_id': 'service_id',
        'name': 'name',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ERequestCart : {
        'id': 'id',
        'person_id': 'person_id',
        'job_period_id': 'job_period_id',
        'requestor_id': 'requestor_id',
        'starting_date': 'starting_date',
        'manager_id': 'manager_id',
        'request_type': 'request_type',
        'reason': 'reason',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'approval_status': 'approval_status',
        'approval_comment': 'approval_comment',
        'subst_approver_id': 'subst_approver_id',
        'subst_approver_email': 'subst_approver_email',
        'forced_hidden': 'forced_hidden',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_time': 'approval_time',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_address': 'email_address',
        'reject_email_sent': 'reject_email_sent',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ERequestCartPermission : {
        'id': 'id',
        'request_cart_id': 'request_cart_id',
        'person_id': 'person_id',
        'service_role_id': 'service_role_id',
        'requestor_id': 'requestor_id',
        'request_activation_date': 'request_activation_date',
        'permission_request_type': 'permission_request_type',
        'service_id': 'service_id',
        'description': 'description',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'period_yr': 'period_yr',
        'approval_status': 'approval_status',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_timestamp': 'approval_timestamp',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_to_user_sent': 'email_to_user_sent',
        'email_to_superior_sent': 'email_to_superior_sent',
        'email_to_others_sent': 'email_to_others_sent',
        'email_to_service_manager_sent': 'email_to_service_manager_sent',
        'email_to_requestor_sent': 'email_to_requestor_sent',
        'reject_email_sent': 'reject_email_sent',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'associated_orgunits_json': 'associated_orgunits_json',
        'associated_ext_orgs_json': 'associated_ext_orgs_json',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GAccountAttribute : {
        'id': 'id',
        'person_useraccount_id': 'person_useraccount_id',
        'value': 'value',
        'value_p_old': 'value_p_old',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GAce : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ace_types': 'ace_types',
        'value': 'value',
        'ace_key': 'ace_key',
        'ace_key_priority': 'ace_key_priority',
        'attribute_source': 'attribute_source',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GAceAttribute : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'source_entity': 'source_entity',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GCountry : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'region': 'region',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GIdentity : {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'personal_id': 'personal_id',
        'id_validity': 'id_validity',
        'identitysource_id': 'identitysource_id',
        'identified_by': 'identified_by',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GIdentitySource : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'identitysourcetype': 'identitysourcetype',
        'identitysourceclass': 'identitysourceclass',
        'source_update': 'source_update',
        'resp_name': 'resp_name',
        'resp_email': 'resp_email',
        'resp_phone': 'resp_phone',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GLanguage : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'iso_code': 'iso_code',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GMdmRule : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GMdmSource : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'source_type': 'source_type',
        'source_class': 'source_class',
        'update_cycle': 'update_cycle',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GNotification : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'notification_type': 'notification_type',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GNotificationQueue : {
        'id': 'id',
        'notification_id': 'notification_id',
        'sender': 'sender',
        'recipients': 'recipients',
        'recipient_user': 'recipient_user',
        'recipient_user_group': 'recipient_user_group',
        'notification_data': 'notification_data',
        'notification_settings': 'notification_settings',
        'notification_body': 'notification_body',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'd_job_period_id': 'd_job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'notified_at': 'notified_at',
        'notification_queue_status': 'notification_queue_status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GPermission : {
        'id': 'id',
        'd_job_period_id': 'd_job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'service_role_id': 'service_role_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'period_yr': 'period_yr',
        'description': 'description',
        'preferred_implementor_id': 'preferred_implementor_id',
        'requested_by_id': 'requested_by_id',
        'requested_time': 'requested_time',
        'accepted_by_id': 'accepted_by_id',
        'accepted_by_time': 'accepted_by_time',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'username': 'username',
        'password': 'password',
        'imported': 'imported',
        'status': 'status',
        'request_cart_permission_id': 'request_cart_permission_id',
        'e_request_cart_permission_id': 'e_request_cart_permission_id',
        'delete_request_cart_permission_id': 'delete_request_cart_permission_id',
        'delete_e_request_cart_permission_id': 'delete_e_request_cart_permission_id',
        'd_job_period_substitute_id': 'd_job_period_substitute_id',
        'e_job_period_substitute_id': 'e_job_period_substitute_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GPersonUseraccount : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'username': 'username',
        'account_name': 'account_name',
        'account_uid': 'account_uid',
        'object_guid': 'object_guid',
        'dn': 'dn',
        'password': 'password',
        'service_id': 'service_id',
        'system_id': 'system_id',
        'inbound_attributes_json': 'inbound_attributes_json',
        'outbound_attributes_json': 'outbound_attributes_json',
        'old_inbound_attributes_json': 'old_inbound_attributes_json',
        'old_outbound_attributes_json': 'old_outbound_attributes_json',
        'account_created': 'account_created',
        'status': 'status',
        'internal': 'internal',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GProvisioningTask : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'd_job_period_id': 'd_job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'service_id': 'service_id',
        'task_type': 'task_type',
        'value_date': 'value_date',
        'service_role_id': 'service_role_id',
        'preferred_implementor_id': 'preferred_implementor_id',
        'request_description': 'request_description',
        'implementation_description': 'implementation_description',
        'implemented_by_id': 'implemented_by_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'provisioning_task_status': 'provisioning_task_status',
        'provisioning_type': 'provisioning_type',
        'system_id': 'system_id',
        'person_useraccount_id': 'person_useraccount_id',
        'inbound_attributes_json': 'inbound_attributes_json',
        'outbound_attributes_json': 'outbound_attributes_json',
        'diff_json': 'diff_json',
        'error_json': 'error_json',
        'integration_direction': 'integration_direction',
        'task_settings': 'task_settings',
        'username': 'username',
        'password': 'password',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_to_user_sent': 'email_to_user_sent',
        'email_to_superior_sent': 'email_to_superior_sent',
        'email_to_others_sent': 'email_to_others_sent',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'permission_id': 'permission_id',
        'request_cart_permission_id': 'request_cart_permission_id',
        'e_request_cart_permission_id': 'e_request_cart_permission_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GRegion : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GService : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'code': 'code',
        'status': 'status',
        'service_provider_id': 'service_provider_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'description': 'description',
        'service_class': 'service_class',
        'service_type_id': 'service_type_id',
        'system_id': 'system_id',
        'user_type': 'user_type',
        'register': 'register',
        'upper_service_id': 'upper_service_id',
        'externals_allowed': 'externals_allowed',
        'service_category': 'service_category',
        'approver_id': 'approver_id',
        'executor_id': 'executor_id',
        'revoke_type': 'revoke_type',
        'grace_period': 'grace_period',
        'minimum_period': 'minimum_period',
        'notification_id': 'notification_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceProvider : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'country_id': 'country_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceRequest : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'trans_date': 'trans_date',
        'severity': 'severity',
        'sr_class': 'sr_class',
        'sr_type': 'sr_type',
        'reported_by_name': 'reported_by_name',
        'reported_by_email': 'reported_by_email',
        'reported_by_phone': 'reported_by_phone',
        'int_resp_uid': 'int_resp_uid',
        'person_id': 'person_id',
        'service_id': 'service_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceResp : {
        'id': 'id',
        'person_name': 'person_name',
        'service_id': 'service_id',
        'servicerole_id': 'servicerole_id',
        'resp_class': 'resp_class',
        'resp_type': 'resp_type',
        'resp_name': 'resp_name',
        'resp_username': 'resp_username',
        'resp_email': 'resp_email',
        'resp_phone': 'resp_phone',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceRole : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'code': 'code',
        'status': 'status',
        'description': 'description',
        'service_id': 'service_id',
        'service_role_type': 'service_role_type',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'servicerole_class': 'servicerole_class',
        'virtual': 'virtual',
        'needs_service_manager_approval': 'needs_srv_mgr_approval',
        'authentication_level': 'authentication_level',
        'provisioning_type': 'provisioning_type',
        'aces_in_transaction': 'aces_in_transaction',
        'upper_servicerole_id': 'upper_servicerole_id',
        'chain_service_role_id': 'chain_service_role_id',
        'executor_id': 'executor_id',
        'favorite': 'favorite',
        'end_date_request': 'end_date_request',
        'period_request': 'period_request',
        'description_request': 'description_request',
        'associated_organizations_request': 'associated_organizations_request',
        'approver_id': 'approver_id',
        'subst_approver_id': 'subst_approver_id',
        'subst_approver_active': 'subst_approver_active',
        'subst_approver_email': 'subst_approver_email',
        'needs_superior_approval': 'needs_superior_approval',
        'notification_create': 'notification_create',
        'notification_update': 'notification_update',
        'notification_disable': 'notification_disable',
        'notification_delete': 'notification_delete',
        'notification_resetpassword': 'notification_resetpassword',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'owner_id': 'owner_id',
        'service_type': 'service_type',
        'externals_allowed': 'externals_allowed',
        'role_inheritance': 'role_inheritance',
        'site_collection': 'site_collection',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GServiceTypeSroles : {
        'id': 'id',
        'service_type_id': 'service_type_id',
        'name': 'name',
        'description': 'description',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSrParameters : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'orgunit_id': 'orgunit_id',
        'resp_name': 'resp_name',
        'resp_email': 'resp_email',
        'resp_phone': 'resp_phone',
        'backup_name': 'backup_name',
        'backup_email': 'backup_email',
        'backup_phone': 'backup_phone',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'sla_level': 'sla_level',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSrTrans : {
        'id': 'id',
        'service_request_id': 'service_request_id',
        'name': 'name',
        'description': 'description',
        'trans_date': 'trans_date',
        'oper_uid': 'oper_uid',
        'oper_status': 'oper_status',
        'action_type': 'action_type',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSystem : {
        'id': 'id',
        'name': 'name',
        'system_type': 'system_type',
        'identifier': 'identifier',
        'description': 'description',
        'upper_system_id': 'upper_system_id',
        'inbound_schema_mapping_id': 'inbound_schema_mapping_id',
        'outbound_schema_mapping_id': 'outbound_schema_mapping_id',
        'config_json': 'config_json',
        'batch_job_path': 'batch_job_path',
        'revoke_type': 'revoke_type',
        'code': 'code',
        'integration_direction': 'integration_direction',
        'system_application_type': 'system_application_type',
        'priority': 'priority',
        'status': 'status',
        'notification_id': 'notification_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSystemSchema : {
        'id': 'id',
        'name': 'name',
        'module_path': 'module_path',
        'uid': 'uid',
        'description': 'description',
        'type': 'type',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GSystemSchemaAttribute : {
        'id': 'id',
        'system_schema_id': 'system_schema_id',
        'name': 'name',
        'description': 'description',
        'datatype': 'datatype',
        'source_attribute': 'source_attribute',
        'destination_attribute': 'destination_attribute',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    GUserGroup : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'usergroup_type': 'usergroup_type',
        'email': 'email',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrDesktopSubst : {
        'id': 'id',
        'hr_manager_person_number': 'hr_manager_person_number',
        'hr_subst_person_number': 'hr_subst_person_number',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'hr_subst_status': 'hr_subst_status',
        'hr_subst_message': 'hr_subst_message',
        'hr_source_file': 'hr_source_file',
        'hr_source_row': 'hr_source_row',
        'created_at': 'created_at',
        'manager_person_id': 'manager_person_id',
        'subst_person_id': 'subst_person_id',
        'manager_org_unit_manager_id': 'manager_org_unit_manager_id',
        'substitube_org_unit_manager_id': 'substitube_org_unit_manager_id',
        'substitute_id': 'substitute_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrImportRecord : {
        'id': 'id',
        'entity': 'entity',
        'source': 'source',
        'row': 'row',
        'source_entity_id': 'source_entity_id',
        'mapped_entity_id': 'mapped_entity_id',
        'system_entity': 'system_entity',
        'system_entity_id': 'system_entity_id',
        'parent_entity': 'parent_entity',
        'parent_source_entity_id': 'parent_source_entity_id',
        'parent_record_id': 'parent_record_id',
        'parent_system_entity': 'parent_system_entity',
        'parent_system_entity_id': 'parent_system_entity_id',
        'display_name': 'display_name',
        'error_code': 'error_code',
        'error_json': 'error_json',
        'previous_valid_hr_record_json': 'previous_valid_hr_record_json',
        'current_hr_record_json': 'current_hr_record_json',
        'fixed_record_json': 'fixed_record_json',
        'fixed_attributes_json': 'fixed_attributes_json',
        'mapped_attributes_json': 'mapped_attributes_json',
        'correctable_error': 'correctable_error',
        'imported_to_db': 'imported_to_db',
        'hr_status': 'hr_status',
        'previous_record_version_id': 'previous_record_version_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrIntegration : {
        'id': 'id',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'internal': 'internal',
        'last_name': 'surname',
        'first_names': 'first_names',
        'person_number': 'person_number',
        'social_security_number': 'social_security_number',
        'username': 'username',
        'email': 'email',
        'jobtitle_id': 'jobtitle_id',
        'hr_job_title': 'hr_job_title',
        'hr_official_job_title': 'hr_official_job_title',
        'orgunit_id': 'org_unit_id',
        'ext_org_id': 'ext_org_id',
        'legal_company_id': 'legal_company_id',
        'cost_center_id': 'cost_center_id',
        'location_id': 'location_id',
        'hire_start_date': 'hire_start_date',
        'job_start_date': 'job_start_date',
        'job_end_date': 'job_end_date',
        'manager_id': 'manager_id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'phone': 'phone',
        'pupo': 'voice_address',
        'other_address': 'other_address',
        'sv_number': 'sv_number',
        'hr_status': 'hr_status',
        'preferred_name': 'preferred_name',
        'street_address': 'street_address',
        'post_number': 'post_number',
        'city': 'city',
        'hr_profession_code': 'hr_profession_code',
        'position_type': 'position_type',
        'hr_work_time_type': 'hr_work_time_type_lookup',
        'job_type': 'job_type',
        'hr_job_type': 'hr_job_type',
        'full_part_per': 'full_part_per',
        'job_period_character': 'jp_character',
        'language_id': 'language_id',
        'report_area': 'report_area',
        'report_manager': 'report_manager',
        'report_manager_id': 'report_manager_id',
        'org_association_type': 'org_association_type',
        'ext_email': 'ext_email',
        'ext_phone': 'ext_phone',
        'ext_manager_id': 'ext_manager_id',
        'ext_manager_hetu': 'ext_manager_hetu',
        'ext_manager_name': 'ext_manager_name',
        'ext_org_code': 'ext_org_code',
        'ext_org_contract_number': 'ext_org_contract_number',
        'ext_org_name': 'ext_org_name',
        'orgunit_name': 'orgunit_name',
        'manager_hetu': 'manager_hetu',
        'manager_name': 'manager_name',
        'basic_applications': 'basic_applications',
        'other_data': 'other_data',
        'iloq_identifier': 'iloq_identifier',
        'other_key_1': 'other_key_1',
        'other_key_2': 'other_key_2',
        'personnel_card': 'personnel_card',
        'iloq_valid_till': 'iloq_valid_till',
        'additional_admittances': 'additional_admittances',
        'additional_admittances_validity': 'additional_admittances_validity',
        'additional_information_1': 'additional_information_1',
        'identifier': 'identifier',
        'valid_till': 'valid_till',
        'trans_date': 'trans_date',
        'batch_file_name': 'batch_file_name',
        'batch_messages': 'batch_messages',
        'record_source': 'record_source',
        'hr_language_lookup': 'hr_language_lookup',
        'hr_language_description': 'hr_language_description',
        'hr_job_period_id': 'hr_job_period_id',
        'hr_job_title_id': 'hr_job_title_id',
        'hr_department_id': 'hr_department_id',
        'hr_manager_id': 'hr_manager_id',
        'is_manager': 'is_manager',
        'job_position_type': 'job_position_type',
        'job_position': 'job_position',
        'job_period_type': 'jp_type',
        'job_period_type_text': 'jp_type_text',
        'job_period_character_text': 'jp_character_text',
        'person_number2': 'person_number2',
        'integration_timestamp': 'integration_timestamp',
        'pass2done': 'pass2done',
        'c_pasu': 'c_pasu',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    HrIntegrationVault : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'loaded': 'loaded',
        'dumped': 'dumped',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IBusinessArea : {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ICostCenter : {
        'id': 'id',
        'legalcompany_id': 'legalcompany_id',
        'header_row': 'header_row',
        'int_code': 'int_code',
        'name': 'name',
        'description': 'description',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
        'classification1': 'classification1',
        'classification2': 'classification2',
        'classification3': 'classification3',
        'classification4': 'classification4',
        'classification5': 'classification5',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IJobFamily : {
        'id': 'id',
        'name': 'name',
        'int_code': 'int_code',
        'description': 'description',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jobfamily_class1': 'jobfamily_class1',
        'jobfamily_class2': 'jobfamily_class2',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IJobRole : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'int_code': 'int_code',
        'description': 'description',
        'global_jobrole': 'global_jobrole',
        'inheritance': 'inheritance',
        'orgunit_id': 'orgunit_id',
        'org_spec': 'org_spec',
        'upper_jobrole_id': 'upper_jobrole_id',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'jobrole_class1': 'jobrole_class1',
        'jobrole_class2': 'jobrole_class2',
        'jobfamily_id': 'jobfamily_id',
        'status': 'status',
        'org_group_id': 'org_group_id',
        'favorite': 'favorite',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ILegalCompany : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'official_company_id': 'official_company_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ILocation : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'upper_location_id': 'upper_location_id',
        'header_row': 'header_row',
        'location_id': 'location_id',
        'site_category': 'site_category',
        'virtual_location': 'virtual_location',
        'status': 'status',
        'street': 'street',
        'street2': 'street2',
        'post': 'post',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'office_phone': 'office_phone',
        'office_fax': 'office_fax',
        'office_timezone': 'office_timezone',
        'site_manager_id': 'site_manager_id',
        'site_manager_name': 'site_manager_name',
        'site_manager_email': 'site_manager_email',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IManagerPerProfession : {
        'id': 'id',
        'orgunit_id': 'orgunit_id',
        'hr_profession_code': 'hr_profession_code',
        'i_job_role_id': 'i_job_role_id',
        'e_job_role_id': 'e_job_role_id',
        'superior_person_id': 'superior_person_id',
        'superior_name': 'superior_name',
        'superior_email': 'superior_email',
        'subst_s_person_id': 'subst_s_person_id',
        'subst_s_name': 'subst_s_name',
        'subst_s_email': 'subst_s_email',
        'substitute_active': 'substitute_active',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgGroup : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgType : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgUnit : {
        'id': 'id',
        'name': 'name',
        'name6': 'name6',
        'description': 'description',
        'upper_orgunit_id': 'upper_orgunit_id',
        'unit_id': 'unit_id',
        'orgtype_id': 'orgtype_id',
        'inheritance': 'inheritance',
        'header_row': 'header_row',
        'pilot': 'pilot',
        'org_level': 'org_level',
        'virtual_unit': 'virtual_unit',
        'businessarea': 'businessarea',
        'legalcompany_id': 'legalcompany_id',
        'costcenter_id': 'costcenter_id',
        'location_id': 'location_id',
        'it_support_email': 'it_support_email',
        'favorite': 'favorite',
        'starting_date': 'starting_date',
        'termination_date': 'termination_date',
        'status': 'status',
        'org_spec': 'org_spec',
        'unit_id_1': 'unit_id_1',
        'unit_id_2': 'unit_id_2',
        'financial_code_1': 'financial_code_1',
        'location_info': 'location_info',
        'exc_street': 'exc_street',
        'exc_street2': 'exc_street2',
        'exc_post': 'exc_post',
        'exc_city': 'exc_city',
        'exc_state': 'exc_state',
        'exc_country': 'exc_country',
        'exc_office_phone': 'exc_office_phone',
        'exc_office_fax': 'exc_office_fax',
        'exc_office_timezone': 'exc_office_timezone',
        'exc_site_category': 'exc_site_category',
        'manager_id': 'superior_person_id',
        'superior_name': 'superior_name',
        'superior_email': 'superior_email',
        'subst_manager_id': 'subst_s_person_id',
        'subst_s_name': 'subst_s_name',
        'subst_s_email': 'subst_s_email',
        'substitute_active': 'substitute_active',
        'teamleader_person_id': 'teamleader_person_id',
        'teamleader_name': 'teamleader_name',
        'teamleader_email': 'teamleader_email',
        'hr_manager_person_id': 'hr_manager_person_id',
        'hr_manager_name': 'hr_manager_name',
        'hr_manager_email': 'hr_manager_email',
        'default_language_id': 'default_language_id',
        'default_jobrole_id': 'default_jobrole_id',
        'default_domain': 'default_domain',
        'provisioning_dirty': 'provisioning_dirty',
        'distinguishedname': 'distinguishedname',
        'codeserver_oid': 'codeserver_oid',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgUnitManager : {
        'id': 'id',
        'org_unit_id': 'org_unit_id',
        'manager_id': 'manager_id',
        'manager_type': 'manager_type',
        'activation_date': 'activation_date',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    IOrgUnitManagerSubstitute : {
        'id': 'id',
        'org_unit_manager_id': 'org_unit_manager_id',
        'subst_manager_id': 'subst_manager_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'hr_desktop_subst': 'hr_desktop_subst',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    OneTimeLink : {
        'id': 'id',
        'auth_token': 'auth_token',
        'entity_name': 'entity_name',
        'entity_id': 'entity_id',
        'expires': 'expires',
        'created_timestamp': 'created_timestamp',
        'used_timestamp': 'used_timestamp',
        'zuser_id': 'zuser_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    PRequestCart : {
        'id': 'id',
        'job_period_id': 'job_period_id',
        'e_job_period_id': 'e_job_period_id',
        'social_security_number': 'social_security_number',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'internal': 'internal',
        'request_ssn': 'request_ssn',
        'requestor_id': 'requestor_id',
        'starting_date': 'starting_date',
        'manager_ssn': 'manager_ssn',
        'description': 'description',
        'preferred_implementor_ssn': 'preferred_implementor_ssn',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'src_trans_date': 'src_trans_date',
        'status_in': 'status_in',
        'request_cart_id': 'request_cart_id',
        'e_request_cart_id': 'e_request_cart_id',
        'hr_job_period_id': 'hr_job_period_id',
        'out_status': 'out_status',
        'out_status_error_msg': 'out_status_error_msg',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    PRequestCartRow : {
        'id': 'id',
        'p_request_cart_id': 'p_request_cart_id',
        'permission_request_type': 'permission_request_type',
        'service_role_id': 'service_role_id',
        'description': 'description',
        'preferred_implementor_ssn': 'preferred_implementor_ssn',
        'status_in': 'status_in',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'out_status': 'out_status',
        'out_date': 'out_date',
        'request_cart_row_id': 'request_cart_row_id',
        'e_request_cart_row_id': 'e_request_cart_row_id',
        'out_status_process': 'out_status_process',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RDynRole : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'rule': 'rule',
        'approval_status': 'approval_status',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ROrgDac : {
        'id': 'id',
        'orgunit_id': 'orgunit_id',
        'name': 'name',
        'dedicated': 'dedicated',
        'key1_min_value': 'key1_min_value',
        'key1_max_value': 'key1_max_value',
        'key2_min_value': 'key2_min_value',
        'key2_max_value': 'key2_max_value',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ROrgService : {
        'id': 'id',
        'name': 'name',
        'orgunit_id': 'orgunit_id',
        'service_id': 'service_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    ROrgTypeService : {
        'id': 'id',
        'name': 'name',
        'org_type_id': 'org_type_id',
        'service_id': 'service_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RSodException : {
        'id': 'id',
        'internal': 'internal',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'sod_rule_id': 'sod_rule_id',
        'exc_approved': 'exc_approved',
        'exc_approver_id': 'exc_approver_id',
        'exc_approver_desc': 'exc_approver_desc',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RSodRule : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'sod_rule_class_id': 'sod_rule_class_id',
        'role1_id': 'role1_id',
        'role2_id': 'role2_id',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RSodRuleClass : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RUserDac : {
        'id': 'id',
        'person_id': 'person_id',
        'name': 'name',
        'dedicated': 'dedicated',
        'key1_min_value': 'key1_min_value',
        'key1_max_value': 'key1_max_value',
        'key2_min_value': 'key2_min_value',
        'key2_max_value': 'key2_max_value',
        'status': 'status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RequestCart : {
        'id': 'id',
        'person_id': 'person_id',
        'job_period_id': 'job_period_id',
        'requestor_id': 'requestor_id',
        'starting_date': 'starting_date',
        'manager_id': 'manager_id',
        'request_type': 'request_type',
        'reason': 'reason',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'approval_status': 'approval_status',
        'approval_comment': 'approval_comment',
        'subst_approver_id': 'subst_approver_id',
        'subst_approver_email': 'subst_approver_email',
        'forced_hidden': 'forced_hidden',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_time': 'approval_time',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_address': 'email_address',
        'reject_email_sent': 'reject_email_sent',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    RequestCartPermission : {
        'id': 'id',
        'request_cart_id': 'request_cart_id',
        'person_id': 'person_id',
        'service_role_id': 'service_role_id',
        'requestor_id': 'requestor_id',
        'request_activation_date': 'request_activation_date',
        'permission_request_type': 'permission_request_type',
        'service_id': 'service_id',
        'description': 'description',
        'preferred_implementor_id': 'preferred_implementor_id',
        'inform_user': 'inform_user',
        'inform_superior': 'inform_superior',
        'inform_others': 'inform_others',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'period_yr': 'period_yr',
        'approval_status': 'approval_status',
        'approver_id': 'approver_id',
        'auto_approved': 'auto_approved',
        'approval_timestamp': 'approval_timestamp',
        'first_email_sent': 'first_email_sent',
        'last_email_sent': 'last_email_sent',
        'email_counter': 'email_counter',
        'email_to_user_sent': 'email_to_user_sent',
        'email_to_superior_sent': 'email_to_superior_sent',
        'email_to_others_sent': 'email_to_others_sent',
        'email_to_service_manager_sent': 'email_to_service_manager_sent',
        'email_to_requestor_sent': 'email_to_requestor_sent',
        'reject_email_sent': 'reject_email_sent',
        'source_system_name': 'source_system_name',
        'source_system_id': 'source_system_id',
        'associated_orgunits_json': 'associated_orgunits_json',
        'associated_ext_orgs_json': 'associated_ext_orgs_json',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDDepartmentWeekMaxQuantity : {
        'id': 'id',
        'department_id': 'department_id',
        'week': 'week',
        'quantity': 'quantity',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDStudyProgramme : {
        'id': 'id',
        'name': 'name',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipPlacement : {
        'id': 'id',
        'traineeship_placement_request_id': 'traineeship_placement_request_id',
        'student_slot_number': 'student_slot_number',
        'part_number': 'part_number',
        'department_id': 'department_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'coordinator_id': 'coordinator_id',
        'traineeship_type_id': 'traineeship_type_id',
        'responsible_person_id': 'responsible_person_id',
        'guiding_teacher_id': 'guiding_teacher_id',
        'student_id': 'student_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipPlacementRequest : {
        'id': 'id',
        'traineeship_request_id': 'traineeship_request_id',
        'office_id': 'office_id',
        'division_id': 'division_id',
        'department_id': 'department_id',
        'semester_information': 'semester_information',
        'traineeship_type_id': 'traineeship_type_id',
        'traineeship_type_other': 'traineeship_type_other',
        'length_weeks': 'length_weeks',
        'start_date': 'start_date',
        'end_date': 'end_date',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipRequest : {
        'id': 'id',
        'school_id': 'school_id',
        'study_programme_id': 'study_programme_id',
        'course_name': 'course_name',
        'includes_skill_test': 'includes_skill_test',
        'skill_test_type': 'skill_test_type',
        'advanced_course': 'advanced_course',
        'international_student': 'international_student',
        'international_school_name': 'international_school_name',
        'extra_information': 'extra_information',
        'quantity_requested': 'quantity_requested',
        'request_status': 'request_status',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    SDTraineeshipType : {
        'id': 'id',
        'name': 'name',
        'upper_traineeship_type_id': 'upper_traineeship_type_id',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Useright : {
        'id': 'id',
        'name': 'name',
        'extra1': 'extra1',
        'extra2': 'extra2',
        'distinguished_name': 'dn',
        'righttype_lookup': 'righttype_lookup',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Zreport : {
        'id': 'id',
        'name': 'name',
        'name5': 'name5',
        'name6': 'name6',
        'description': 'description',
        'reportfile': 'reportfile',
        'url': 'url',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Zrole : {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'distinguished_name': 'dn',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
    Zuser : {
        'id': 'id',
        'username': 'name',
        'first_names': 'firstname',
        'last_name': 'lastname',
        'email': 'email',
        'address': 'address',
        'phone': 'phone',
        'start_date': 'startdate',
        'force_change_password': 'force_change_password',
        'internal': 'internal',
        'person_id': 'person_id',
        'external_person_id': 'external_person_id',
        'status': 'status',
        'liferay_uid': 'liferay_uid',
        'password': 'password',
    'f_version': 'f_version',
    'f_changed': 'f_changed',
    'f_changedby': 'f_changedby',
    'deleted': 'deleted',
    },
}
fk_attributes = {
    'C_card' : {
        'card_type_id': ForeignKey('C_card_type', 'id', 'card_type_id'),
        'identity_id': ForeignKey('G_identity', 'id', 'identity_id'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'replaced_card_id': ForeignKey('C_card', 'id', 'replaced_card_id'),
        'given_by_id': ForeignKey('D_person', 'id', 'given_by_id'),
        'card_organization_id': ForeignKey('C_card_organization', 'id', 'card_organization_id'),
        'issuer_id': ForeignKey('C_card_issuer', 'id', 'issuer_id'),
        'reg_ra_workstation_id': ForeignKey('C_workstation', 'id', 'reg_ra_workstation_id'),
        'reg_person_id': ForeignKey('D_person', 'id', 'reg_person_id'),
        'internal_org_id': ForeignKey('I_org_unit', 'id', 'internal_org_id'),
    },
    'C_card_issuer' : {
    },
    'C_card_organization' : {
    },
    'C_card_type' : {
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
    },
    'C_device' : {
        'device_type': ForeignKey('C_device_type', 'id', 'device_type'),
        'device_subtype': ForeignKey('C_device_subtype', 'id', 'device_subtype'),
    },
    'C_device_person' : {
        'device_id': ForeignKey('C_device', 'id', 'device_id'),
        'identity_id': ForeignKey('G_identity', 'id', 'identity_id'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'given_by_id': ForeignKey('D_person', 'id', 'given_by_id'),
    },
    'C_device_subtype' : {
        'device_type': ForeignKey('C_device_type', 'id', 'device_type'),
    },
    'C_device_type' : {
    },
    'C_key' : {
        'key_type_id': ForeignKey('C_key_type', 'id', 'key_type_id'),
        'key_profile': ForeignKey('C_key_profile', 'id', 'key_profile'),
        'identity_id': ForeignKey('G_identity', 'id', 'identity_id'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'replaced_key_id': ForeignKey('C_key', 'id', 'replaced_key_id'),
        'given_by_id': ForeignKey('D_person', 'id', 'given_by_id'),
    },
    'C_key_profile' : {
        'key_type_id': ForeignKey('C_key_type', 'id', 'key_type_id'),
    },
    'C_key_type' : {
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
    },
    'C_workstation' : {
    },
    'D_absence' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
    },
    'D_auth_method' : {
    },
    'D_competence' : {
    },
    'D_education' : {
    },
    'D_job_period' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'jobtitle_id': ForeignKey('D_jobtitle', 'id', 'jobtitle_id'),
        'jobfamily_id': ForeignKey('I_job_family', 'id', 'jobfamily_id'),
        'jobrole_id': ForeignKey('I_job_role', 'id', 'jobrole_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_manager_id'),
        'report_manager_id': ForeignKey('D_person', 'id', 'report_manager_id'),
        'org_unit_manager_id': ForeignKey('I_org_unit_manager', 'id', 'org_unit_manager_id'),
        'exc_legalcompany_id': ForeignKey('I_legal_company', 'id', 'exc_legalcompany_id'),
        'exc_costcenter_id': ForeignKey('I_cost_center', 'id', 'exc_costcenter_id'),
        'exc_location_id': ForeignKey('I_location', 'id', 'exc_location_id'),
        'exc_country_id': ForeignKey('G_country', 'id', 'exc_country_id'),
        'created_by_id': ForeignKey('Zuser', 'id', 'created_by_id'),
    },
    'D_job_period_absence' : {
        'd_job_period_id': ForeignKey('D_job_period', 'id', 'd_job_period_id'),
        'created_by': ForeignKey('Zuser', 'id', 'created_by'),
    },
    'D_job_period_substitute' : {
        'd_job_period_id': ForeignKey('D_job_period', 'id', 'd_job_period_id'),
        'd_substistute_person_id': ForeignKey('D_person', 'id', 'd_substistute_person_id'),
    },
    'D_jobtitle' : {
        'jobrole_id': ForeignKey('I_job_role', 'id', 'jobrole_id'),
    },
    'D_mapping_rule' : {
        'mdm_source_id': ForeignKey('G_mdm_source', 'id', 'mdm_source_id'),
    },
    'D_person' : {
        'identity_id': ForeignKey('G_identity', 'id', 'identity_id'),
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'language_id': ForeignKey('G_language', 'id', 'language_id'),
        'jobtitle_id': ForeignKey('D_jobtitle', 'id', 'jobtitle_id'),
        'jobfamily_id': ForeignKey('I_job_family', 'id', 'jobfamily_id'),
        'jobrole_id': ForeignKey('I_job_role', 'id', 'jobrole_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_manager_id'),
        'exc_location_id': ForeignKey('I_location', 'id', 'exc_location_id'),
        'homecountry_id': ForeignKey('G_country', 'id', 'homecountry_id'),
        'identitysource_id': ForeignKey('G_identity_source', 'id', 'identitysource_id'),
        'nationality_id': ForeignKey('G_country', 'id', 'nationality_id'),
        'mdm_source_id': ForeignKey('G_mdm_source', 'id', 'mdm_source_id'),
        'exc_businessarea_id': ForeignKey('I_business_area', 'id', 'exc_businessarea_id'),
        'exc_legalcompany_id': ForeignKey('I_legal_company', 'id', 'exc_legalcompany_id'),
        'exc_costcenter_id': ForeignKey('I_cost_center', 'id', 'exc_costcenter_id'),
        'exc_country_id': ForeignKey('G_country', 'id', 'exc_country_id'),
        'manager_approved_id': ForeignKey('Zuser', 'id', 'manager_approved_id'),
    },
    'D_user_auth' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'authmethod_id': ForeignKey('D_auth_method', 'id', 'authmethod_id'),
    },
    'E_ext_org' : {
        'upper_ext_org_id': ForeignKey('E_ext_org', 'id', 'upper_ext_org_id'),
        'ext_org_type_id': ForeignKey('E_ext_org_type', 'id', 'ext_org_type_id'),
        'ext_superior_id': ForeignKey('E_external_person', 'id', 'ext_superior_id'),
        'manager_id': ForeignKey('D_person', 'id', 'superior_person_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_s_person_id'),
        'teamleader_person_id': ForeignKey('D_person', 'id', 'teamleader_person_id'),
        'hr_manager_person_id': ForeignKey('D_person', 'id', 'hr_manager_person_id'),
        'costcenter_id': ForeignKey('I_cost_center', 'id', 'costcenter_id'),
        'location_id': ForeignKey('I_location', 'id', 'location_id'),
        'exc_country': ForeignKey('G_country', 'id', 'exc_country'),
        'default_language_id': ForeignKey('G_language', 'id', 'default_language_id'),
        'default_jobrole_id': ForeignKey('I_job_role', 'id', 'default_jobrole_id'),
    },
    'E_ext_org_type' : {
    },
    'E_external_person' : {
        'identity_id': ForeignKey('G_identity', 'id', 'identity_id'),
        'orig_orgunit_id': ForeignKey('I_org_unit', 'id', 'orig_orgunit_id'),
        'ext_org_id': ForeignKey('E_ext_org', 'id', 'ext_org_id'),
        'e_job_role_id': ForeignKey('E_job_role', 'id', 'e_job_role_id'),
        'language_id': ForeignKey('G_language', 'id', 'language_id'),
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'jobtitle_id': ForeignKey('D_jobtitle', 'id', 'jobtitle_id'),
        'jobfamily_id': ForeignKey('I_job_family', 'id', 'jobfamily_id'),
        'jobrole_id': ForeignKey('I_job_role', 'id', 'jobrole_id'),
        'exc_costcenter_id': ForeignKey('I_cost_center', 'id', 'exc_costcenter_id'),
        'exc_location_id': ForeignKey('I_location', 'id', 'exc_location_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_manager_id'),
        'homecountry_id': ForeignKey('G_country', 'id', 'homecountry_id'),
        'identitysource_id': ForeignKey('G_identity_source', 'id', 'identitysource_id'),
        'nationality_id': ForeignKey('G_country', 'id', 'nationality_id'),
        'mdm_source_id': ForeignKey('G_mdm_source', 'id', 'mdm_source_id'),
        'exc_businessarea_id': ForeignKey('I_business_area', 'id', 'exc_businessarea_id'),
        'exc_legalcompany_id': ForeignKey('I_legal_company', 'id', 'exc_legalcompany_id'),
        'exc_country_id': ForeignKey('G_country', 'id', 'exc_country_id'),
        'manager_approved_id': ForeignKey('Zuser', 'id', 'manager_approved_id'),
    },
    'E_job_family' : {
    },
    'E_job_period' : {
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'ext_org_id': ForeignKey('E_ext_org', 'id', 'ext_org_id'),
        'jobtitle_id': ForeignKey('D_jobtitle', 'id', 'jobtitle_id'),
        'jobfamily_id': ForeignKey('E_job_family', 'id', 'jobfamily_id'),
        'jobrole_id': ForeignKey('E_job_role', 'id', 'jobrole_id'),
        'ext_manager_id': ForeignKey('E_external_person', 'id', 'ext_manager_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_manager_id'),
        'report_manager_id': ForeignKey('D_person', 'id', 'report_manager_id'),
        'org_unit_manager_id': ForeignKey('I_org_unit_manager', 'id', 'org_unit_manager_id'),
        'exc_legalcompany_id': ForeignKey('I_legal_company', 'id', 'exc_legalcompany_id'),
        'exc_costcenter_id': ForeignKey('I_cost_center', 'id', 'exc_costcenter_id'),
        'exc_location_id': ForeignKey('I_location', 'id', 'exc_location_id'),
        'exc_country_id': ForeignKey('G_country', 'id', 'exc_country_id'),
        'created_by_id': ForeignKey('Zuser', 'id', 'created_by_id'),
    },
    'E_job_period_absence' : {
        'e_job_period_id': ForeignKey('E_job_period', 'id', 'e_job_period_id'),
        'created_by': ForeignKey('Zuser', 'id', 'created_by'),
    },
    'E_job_period_substitute' : {
        'e_job_period_id': ForeignKey('E_job_period', 'id', 'e_job_period_id'),
        'e_substistute_person_id': ForeignKey('E_external_person', 'id', 'e_substistute_person_id'),
    },
    'E_job_role' : {
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'upper_jobrole_id': ForeignKey('E_job_role', 'id', 'upper_jobrole_id'),
        'jobfamily_id': ForeignKey('E_job_family', 'id', 'jobfamily_id'),
        'org_group_id': ForeignKey('I_org_group', 'id', 'org_group_id'),
    },
    'E_org_type_service' : {
        'ext_org_type_id': ForeignKey('E_ext_org_type', 'id', 'ext_org_type_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
    },
    'E_request_cart' : {
        'person_id': ForeignKey('E_external_person', 'id', 'person_id'),
        'job_period_id': ForeignKey('E_job_period', 'id', 'job_period_id'),
        'requestor_id': ForeignKey('Zuser', 'id', 'requestor_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'preferred_implementor_id': ForeignKey('Zuser', 'id', 'preferred_implementor_id'),
        'subst_approver_id': ForeignKey('Zuser', 'id', 'subst_approver_id'),
        'approver_id': ForeignKey('Zuser', 'id', 'approver_id'),
    },
    'E_request_cart_permission' : {
        'request_cart_id': ForeignKey('E_request_cart', 'id', 'request_cart_id'),
        'person_id': ForeignKey('E_external_person', 'id', 'person_id'),
        'service_role_id': ForeignKey('G_service_role', 'id', 'service_role_id'),
        'requestor_id': ForeignKey('Zuser', 'id', 'requestor_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
        'preferred_implementor_id': ForeignKey('Zuser', 'id', 'preferred_implementor_id'),
        'approver_id': ForeignKey('Zuser', 'id', 'approver_id'),
    },
    'G_account_attribute' : {
        'person_useraccount_id': ForeignKey('G_person_useraccount', 'id', 'person_useraccount_id'),
    },
    'G_ace' : {
        'attribute_source': ForeignKey('G_ace_attribute', 'id', 'attribute_source'),
    },
    'G_ace_attribute' : {
    },
    'G_country' : {
        'region': ForeignKey('G_region', 'id', 'region'),
    },
    'G_identity' : {
        'identitysource_id': ForeignKey('G_identity_source', 'id', 'identitysource_id'),
    },
    'G_identity_source' : {
    },
    'G_language' : {
    },
    'G_mdm_rule' : {
    },
    'G_mdm_source' : {
    },
    'G_notification' : {
    },
    'G_notification_queue' : {
        'notification_id': ForeignKey('G_notification', 'id', 'notification_id'),
        'recipient_user': ForeignKey('Zuser', 'id', 'recipient_user'),
        'recipient_user_group': ForeignKey('G_user_group', 'id', 'recipient_user_group'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'd_job_period_id': ForeignKey('D_job_period', 'id', 'd_job_period_id'),
        'e_job_period_id': ForeignKey('E_job_period', 'id', 'e_job_period_id'),
    },
    'G_permission' : {
        'd_job_period_id': ForeignKey('D_job_period', 'id', 'd_job_period_id'),
        'e_job_period_id': ForeignKey('E_job_period', 'id', 'e_job_period_id'),
        'service_role_id': ForeignKey('G_service_role', 'id', 'service_role_id'),
        'preferred_implementor_id': ForeignKey('Zuser', 'id', 'preferred_implementor_id'),
        'requested_by_id': ForeignKey('Zuser', 'id', 'requested_by_id'),
        'accepted_by_id': ForeignKey('Zuser', 'id', 'accepted_by_id'),
        'request_cart_permission_id': ForeignKey('Request_cart_permission', 'id', 'request_cart_permission_id'),
        'e_request_cart_permission_id': ForeignKey('E_request_cart_permission', 'id', 'e_request_cart_permission_id'),
        'delete_request_cart_permission_id': ForeignKey('Request_cart_permission', 'id', 'delete_request_cart_permission_id'),
        'delete_e_request_cart_permission_id': ForeignKey('E_request_cart_permission', 'id', 'delete_e_request_cart_permission_id'),
        'd_job_period_substitute_id': ForeignKey('D_job_period_substitute', 'id', 'd_job_period_substitute_id'),
        'e_job_period_substitute_id': ForeignKey('E_job_period_substitute', 'id', 'e_job_period_substitute_id'),
    },
    'G_person_useraccount' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
        'system_id': ForeignKey('G_system', 'id', 'system_id'),
    },
    'G_provisioning_task' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'd_job_period_id': ForeignKey('D_job_period', 'id', 'd_job_period_id'),
        'e_job_period_id': ForeignKey('E_job_period', 'id', 'e_job_period_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
        'service_role_id': ForeignKey('G_service_role', 'id', 'service_role_id'),
        'preferred_implementor_id': ForeignKey('Zuser', 'id', 'preferred_implementor_id'),
        'implemented_by_id': ForeignKey('Zuser', 'id', 'implemented_by_id'),
        'system_id': ForeignKey('G_system', 'id', 'system_id'),
        'person_useraccount_id': ForeignKey('G_person_useraccount', 'id', 'person_useraccount_id'),
        'permission_id': ForeignKey('G_permission', 'id', 'permission_id'),
        'request_cart_permission_id': ForeignKey('Request_cart_permission', 'id', 'request_cart_permission_id'),
        'e_request_cart_permission_id': ForeignKey('E_request_cart_permission', 'id', 'e_request_cart_permission_id'),
    },
    'G_region' : {
    },
    'G_service' : {
        'service_provider_id': ForeignKey('G_service_provider', 'id', 'service_provider_id'),
        'service_type_id': ForeignKey('G_service_type', 'id', 'service_type_id'),
        'system_id': ForeignKey('G_system', 'id', 'system_id'),
        'upper_service_id': ForeignKey('G_service', 'id', 'upper_service_id'),
        'approver_id': ForeignKey('G_user_group', 'id', 'approver_id'),
        'executor_id': ForeignKey('G_user_group', 'id', 'executor_id'),
        'notification_id': ForeignKey('G_notification', 'id', 'notification_id'),
    },
    'G_service_provider' : {
        'country_id': ForeignKey('G_country', 'id', 'country_id'),
    },
    'G_service_request' : {
        'int_resp_uid': ForeignKey('Zuser', 'id', 'int_resp_uid'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
    },
    'G_service_resp' : {
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
        'servicerole_id': ForeignKey('G_service_role', 'id', 'servicerole_id'),
    },
    'G_service_role' : {
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
        'upper_servicerole_id': ForeignKey('G_service_role', 'id', 'upper_servicerole_id'),
        'chain_service_role_id': ForeignKey('G_service_role', 'id', 'chain_service_role_id'),
        'executor_id': ForeignKey('G_user_group', 'id', 'executor_id'),
        'approver_id': ForeignKey('G_user_group', 'id', 'approver_id'),
        'subst_approver_id': ForeignKey('G_user_group', 'id', 'subst_approver_id'),
        'notification_create': ForeignKey('G_notification', 'id', 'notification_create'),
        'notification_update': ForeignKey('G_notification', 'id', 'notification_update'),
        'notification_disable': ForeignKey('G_notification', 'id', 'notification_disable'),
        'notification_delete': ForeignKey('G_notification', 'id', 'notification_delete'),
        'notification_resetpassword': ForeignKey('G_notification', 'id', 'notification_resetpassword'),
    },
    'G_service_type' : {
        'owner_id': ForeignKey('D_person', 'id', 'owner_id'),
    },
    'G_service_type_sroles' : {
        'service_type_id': ForeignKey('G_service_type', 'id', 'service_type_id'),
    },
    'G_sr_parameters' : {
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
    },
    'G_sr_trans' : {
        'service_request_id': ForeignKey('G_service_request', 'id', 'service_request_id'),
        'oper_uid': ForeignKey('Zuser', 'id', 'oper_uid'),
    },
    'G_system' : {
        'upper_system_id': ForeignKey('G_system', 'id', 'upper_system_id'),
        'inbound_schema_mapping_id': ForeignKey('G_system_schema', 'id', 'inbound_schema_mapping_id'),
        'outbound_schema_mapping_id': ForeignKey('G_system_schema', 'id', 'outbound_schema_mapping_id'),
        'notification_id': ForeignKey('G_notification', 'id', 'notification_id'),
    },
    'G_system_schema' : {
    },
    'G_system_schema_attribute' : {
        'system_schema_id': ForeignKey('G_system_schema', 'id', 'system_schema_id'),
    },
    'G_user_group' : {
    },
    'Hr_desktop_subst' : {
        'manager_person_id': ForeignKey('D_person', 'id', 'manager_person_id'),
        'subst_person_id': ForeignKey('D_person', 'id', 'subst_person_id'),
        'manager_org_unit_manager_id': ForeignKey('I_org_unit_manager', 'id', 'manager_org_unit_manager_id'),
        'substitube_org_unit_manager_id': ForeignKey('I_org_unit_manager', 'id', 'substitube_org_unit_manager_id'),
        'substitute_id': ForeignKey('I_org_unit_manager_subst', 'id', 'substitute_id'),
    },
    'Hr_import_record' : {
        'parent_record_id': ForeignKey('Hr_import_record', 'id', 'parent_record_id'),
    },
    'Hr_integration' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'jobtitle_id': ForeignKey('D_jobtitle', 'id', 'jobtitle_id'),
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'org_unit_id'),
        'ext_org_id': ForeignKey('E_ext_org', 'id', 'ext_org_id'),
        'legal_company_id': ForeignKey('I_legal_company', 'id', 'legal_company_id'),
        'cost_center_id': ForeignKey('I_cost_center', 'id', 'cost_center_id'),
        'location_id': ForeignKey('I_location', 'id', 'location_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'org_unit_manager_id': ForeignKey('I_org_unit_manager', 'id', 'org_unit_manager_id'),
        'language_id': ForeignKey('G_language', 'id', 'language_id'),
        'report_manager_id': ForeignKey('D_person', 'id', 'report_manager_id'),
        'ext_manager_id': ForeignKey('E_external_person', 'id', 'ext_manager_id'),
    },
    'Hr_integration_vault' : {
    },
    'I_business_area' : {
    },
    'I_cost_center' : {
        'legalcompany_id': ForeignKey('I_legal_company', 'id', 'legalcompany_id'),
    },
    'I_job_family' : {
    },
    'I_job_role' : {
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'upper_jobrole_id': ForeignKey('I_job_role', 'id', 'upper_jobrole_id'),
        'jobfamily_id': ForeignKey('I_job_family', 'id', 'jobfamily_id'),
        'org_group_id': ForeignKey('I_org_group', 'id', 'org_group_id'),
    },
    'I_legal_company' : {
    },
    'I_location' : {
        'upper_location_id': ForeignKey('I_location', 'id', 'upper_location_id'),
        'country': ForeignKey('G_country', 'id', 'country'),
        'site_manager_id': ForeignKey('D_person', 'id', 'site_manager_id'),
    },
    'I_manager_per_profession' : {
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'i_job_role_id': ForeignKey('I_job_role', 'id', 'i_job_role_id'),
        'e_job_role_id': ForeignKey('E_job_role', 'id', 'e_job_role_id'),
        'superior_person_id': ForeignKey('D_person', 'id', 'superior_person_id'),
        'subst_s_person_id': ForeignKey('D_person', 'id', 'subst_s_person_id'),
    },
    'I_org_group' : {
    },
    'I_org_type' : {
    },
    'I_org_unit' : {
        'upper_orgunit_id': ForeignKey('I_org_unit', 'id', 'upper_orgunit_id'),
        'orgtype_id': ForeignKey('I_org_type', 'id', 'orgtype_id'),
        'businessarea': ForeignKey('I_business_area', 'id', 'businessarea'),
        'legalcompany_id': ForeignKey('I_legal_company', 'id', 'legalcompany_id'),
        'costcenter_id': ForeignKey('I_cost_center', 'id', 'costcenter_id'),
        'location_id': ForeignKey('I_location', 'id', 'location_id'),
        'exc_country': ForeignKey('G_country', 'id', 'exc_country'),
        'manager_id': ForeignKey('D_person', 'id', 'superior_person_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_s_person_id'),
        'teamleader_person_id': ForeignKey('D_person', 'id', 'teamleader_person_id'),
        'hr_manager_person_id': ForeignKey('D_person', 'id', 'hr_manager_person_id'),
        'default_language_id': ForeignKey('G_language', 'id', 'default_language_id'),
        'default_jobrole_id': ForeignKey('I_job_role', 'id', 'default_jobrole_id'),
    },
    'I_org_unit_manager' : {
        'org_unit_id': ForeignKey('I_org_unit', 'id', 'org_unit_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
    },
    'I_org_unit_manager_subst' : {
        'org_unit_manager_id': ForeignKey('I_org_unit_manager', 'id', 'org_unit_manager_id'),
        'subst_manager_id': ForeignKey('D_person', 'id', 'subst_manager_id'),
        'hr_desktop_subst': ForeignKey('Hr_desktop_subst', 'id', 'hr_desktop_subst'),
    },
    'One_time_link' : {
        'zuser_id': ForeignKey('Zuser', 'id', 'zuser_id'),
    },
    'P_request_cart' : {
        'job_period_id': ForeignKey('D_job_period', 'id', 'job_period_id'),
        'e_job_period_id': ForeignKey('E_job_period', 'id', 'e_job_period_id'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'requestor_id': ForeignKey('Zuser', 'id', 'requestor_id'),
        'request_cart_id': ForeignKey('Request_cart', 'id', 'request_cart_id'),
        'e_request_cart_id': ForeignKey('E_request_cart', 'id', 'e_request_cart_id'),
    },
    'P_request_cart_row' : {
        'p_request_cart_id': ForeignKey('P_request_cart', 'id', 'p_request_cart_id'),
        'service_role_id': ForeignKey('G_service_role', 'id', 'service_role_id'),
        'request_cart_row_id': ForeignKey('Request_cart_permission', 'id', 'request_cart_row_id'),
        'e_request_cart_row_id': ForeignKey('E_request_cart_permission', 'id', 'e_request_cart_row_id'),
    },
    'R_dyn_role' : {
    },
    'R_org_dac' : {
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
    },
    'R_org_service' : {
        'orgunit_id': ForeignKey('I_org_unit', 'id', 'orgunit_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
    },
    'R_org_type_service' : {
        'org_type_id': ForeignKey('I_org_type', 'id', 'org_type_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
    },
    'R_sod_exception' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
        'sod_rule_id': ForeignKey('R_sod_rule', 'id', 'sod_rule_id'),
        'exc_approver_id': ForeignKey('Zuser', 'id', 'exc_approver_id'),
    },
    'R_sod_rule' : {
        'sod_rule_class_id': ForeignKey('R_sod_rule_class', 'id', 'sod_rule_class_id'),
        'role1_id': ForeignKey('G_service_role', 'id', 'role1_id'),
        'role2_id': ForeignKey('G_service_role', 'id', 'role2_id'),
    },
    'R_sod_rule_class' : {
    },
    'R_user_dac' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
    },
    'Request_cart' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'job_period_id': ForeignKey('D_job_period', 'id', 'job_period_id'),
        'requestor_id': ForeignKey('Zuser', 'id', 'requestor_id'),
        'manager_id': ForeignKey('D_person', 'id', 'manager_id'),
        'preferred_implementor_id': ForeignKey('Zuser', 'id', 'preferred_implementor_id'),
        'subst_approver_id': ForeignKey('Zuser', 'id', 'subst_approver_id'),
        'approver_id': ForeignKey('Zuser', 'id', 'approver_id'),
    },
    'Request_cart_permission' : {
        'request_cart_id': ForeignKey('Request_cart', 'id', 'request_cart_id'),
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'service_role_id': ForeignKey('G_service_role', 'id', 'service_role_id'),
        'requestor_id': ForeignKey('Zuser', 'id', 'requestor_id'),
        'service_id': ForeignKey('G_service', 'id', 'service_id'),
        'preferred_implementor_id': ForeignKey('Zuser', 'id', 'preferred_implementor_id'),
        'approver_id': ForeignKey('Zuser', 'id', 'approver_id'),
    },
    'SD_department_week_max_quantity' : {
        'department_id': ForeignKey('I_org_unit', 'id', 'department_id'),
    },
    'SD_study_programme' : {
    },
    'SD_traineeship_placement' : {
        'traineeship_placement_request_id': ForeignKey('SD_traineeship_placement_request', 'id', 'traineeship_placement_request_id'),
        'department_id': ForeignKey('I_org_unit', 'id', 'department_id'),
        'coordinator_id': ForeignKey('Zuser', 'id', 'coordinator_id'),
        'traineeship_type_id': ForeignKey('SD_traineeship_type', 'id', 'traineeship_type_id'),
        'responsible_person_id': ForeignKey('D_person', 'id', 'responsible_person_id'),
        'guiding_teacher_id': ForeignKey('E_external_person', 'id', 'guiding_teacher_id'),
        'student_id': ForeignKey('E_external_person', 'id', 'student_id'),
    },
    'SD_traineeship_placement_request' : {
        'traineeship_request_id': ForeignKey('SD_traineeship_request', 'id', 'traineeship_request_id'),
        'office_id': ForeignKey('I_org_unit', 'id', 'office_id'),
        'division_id': ForeignKey('I_org_unit', 'id', 'division_id'),
        'department_id': ForeignKey('I_org_unit', 'id', 'department_id'),
        'traineeship_type_id': ForeignKey('SD_traineeship_type', 'id', 'traineeship_type_id'),
    },
    'SD_traineeship_request' : {
        'school_id': ForeignKey('E_ext_org', 'id', 'school_id'),
        'study_programme_id': ForeignKey('SD_study_programme', 'id', 'study_programme_id'),
    },
    'SD_traineeship_type' : {
        'upper_traineeship_type_id': ForeignKey('SD_traineeship_type', 'id', 'upper_traineeship_type_id'),
    },
    'Useright' : {
    },
    'Zreport' : {
    },
    'Zrole' : {
    },
    'Zuser' : {
        'person_id': ForeignKey('D_person', 'id', 'person_id'),
        'external_person_id': ForeignKey('E_external_person', 'id', 'external_person_id'),
    },
}
name_to_class = {
    'C_card': CCard,
    'C_card_issuer': CCardIssuer,
    'C_card_organization': CCardOrganization,
    'C_card_type': CCardType,
    'C_device': CDevice,
    'C_device_person': CDevicePerson,
    'C_device_subtype': CDeviceSubtype,
    'C_device_type': CDeviceType,
    'C_key': CKey,
    'C_key_profile': CKeyProfile,
    'C_key_type': CKeyType,
    'C_workstation': CWorkstation,
    'D_absence': DAbsence,
    'D_auth_method': DAuthMethod,
    'D_competence': DCompetence,
    'D_education': DEducation,
    'D_job_period': DJobPeriod,
    'D_job_period_absence': DJobPeriodAbsence,
    'D_job_period_substitute': DJobPeriodSubstitute,
    'D_jobtitle': DJobtitle,
    'D_mapping_rule': DMappingRule,
    'D_person': DPerson,
    'D_user_auth': DUserAuth,
    'E_ext_org': EExtOrg,
    'E_ext_org_type': EExtOrgType,
    'E_external_person': EExternalPerson,
    'E_job_family': EJobFamily,
    'E_job_period': EJobPeriod,
    'E_job_period_absence': EJobPeriodAbsence,
    'E_job_period_substitute': EJobPeriodSubstitute,
    'E_job_role': EJobRole,
    'E_org_type_service': EOrgTypeService,
    'E_request_cart': ERequestCart,
    'E_request_cart_permission': ERequestCartPermission,
    'G_account_attribute': GAccountAttribute,
    'G_ace': GAce,
    'G_ace_attribute': GAceAttribute,
    'G_country': GCountry,
    'G_identity': GIdentity,
    'G_identity_source': GIdentitySource,
    'G_language': GLanguage,
    'G_mdm_rule': GMdmRule,
    'G_mdm_source': GMdmSource,
    'G_notification': GNotification,
    'G_notification_queue': GNotificationQueue,
    'G_permission': GPermission,
    'G_person_useraccount': GPersonUseraccount,
    'G_provisioning_task': GProvisioningTask,
    'G_region': GRegion,
    'G_service': GService,
    'G_service_provider': GServiceProvider,
    'G_service_request': GServiceRequest,
    'G_service_resp': GServiceResp,
    'G_service_role': GServiceRole,
    'G_service_type': GServiceType,
    'G_service_type_sroles': GServiceTypeSroles,
    'G_sr_parameters': GSrParameters,
    'G_sr_trans': GSrTrans,
    'G_system': GSystem,
    'G_system_schema': GSystemSchema,
    'G_system_schema_attribute': GSystemSchemaAttribute,
    'G_user_group': GUserGroup,
    'Hr_desktop_subst': HrDesktopSubst,
    'Hr_import_record': HrImportRecord,
    'Hr_integration': HrIntegration,
    'Hr_integration_vault': HrIntegrationVault,
    'I_business_area': IBusinessArea,
    'I_cost_center': ICostCenter,
    'I_job_family': IJobFamily,
    'I_job_role': IJobRole,
    'I_legal_company': ILegalCompany,
    'I_location': ILocation,
    'I_manager_per_profession': IManagerPerProfession,
    'I_org_group': IOrgGroup,
    'I_org_type': IOrgType,
    'I_org_unit': IOrgUnit,
    'I_org_unit_manager': IOrgUnitManager,
    'I_org_unit_manager_subst': IOrgUnitManagerSubstitute,
    'One_time_link': OneTimeLink,
    'P_request_cart': PRequestCart,
    'P_request_cart_row': PRequestCartRow,
    'R_dyn_role': RDynRole,
    'R_org_dac': ROrgDac,
    'R_org_service': ROrgService,
    'R_org_type_service': ROrgTypeService,
    'R_sod_exception': RSodException,
    'R_sod_rule': RSodRule,
    'R_sod_rule_class': RSodRuleClass,
    'R_user_dac': RUserDac,
    'Request_cart': RequestCart,
    'Request_cart_permission': RequestCartPermission,
    'SD_department_week_max_quantity': SDDepartmentWeekMaxQuantity,
    'SD_study_programme': SDStudyProgramme,
    'SD_traineeship_placement': SDTraineeshipPlacement,
    'SD_traineeship_placement_request': SDTraineeshipPlacementRequest,
    'SD_traineeship_request': SDTraineeshipRequest,
    'SD_traineeship_type': SDTraineeshipType,
    'Useright': Useright,
    'Zreport': Zreport,
    'Zrole': Zrole,
    'Zuser': Zuser,
}

def get_column_aliases(cls):
    return db_to_mapper[cls], mapper_to_db[cls]

def get_aliased_columns(cls, request_json):
    "Return a dict of 'real' column names from aliased ones from request.json"
    return {mapper_to_db[cls][k]: v for k,v in request_json.items()}

TaggedClasses = {
  'ENUM' : [
  ],
  'HISTORIZED' : [
    Zuser,
    Zreport,
    Zrole,
    Useright,
    CCard,
    CCardIssuer,
    CCardOrganization,
    CCardType,
    CDevice,
    CDevicePerson,
    CDeviceSubtype,
    CDeviceType,
    CKey,
    CKeyProfile,
    CKeyType,
    CWorkstation,
    DAbsence,
    DAuthMethod,
    DCompetence,
    DEducation,
    DJobPeriod,
    DJobtitle,
    DMappingRule,
    DPerson,
    DUserAuth,
    EExtOrg,
    EExtOrgType,
    EExternalPerson,
    EJobFamily,
    EJobPeriod,
    EJobRole,
    EOrgTypeService,
    GAce,
    GAceAttribute,
    GCountry,
    GIdentity,
    GIdentitySource,
    GLanguage,
    GRegion,
    GService,
    GServiceProvider,
    GServiceRole,
    GMdmRule,
    GMdmSource,
    GServiceRequest,
    GServiceResp,
    GServiceType,
    GServiceTypeSroles,
    GSrParameters,
    GSrTrans,
    GSystem,
    HrIntegration,
    HrIntegrationVault,
    IBusinessArea,
    ICostCenter,
    HrDesktopSubst,
    IJobFamily,
    IJobRole,
    ILegalCompany,
    ILocation,
    IOrgType,
    IOrgUnit,
    ROrgDac,
    ROrgService,
    ROrgTypeService,
    RUserDac,
    RequestCart,
    ERequestCart,
    RequestCartPermission,
    ERequestCartPermission,
    GUserGroup,
    IOrgUnitManager,
    IOrgUnitManagerSubstitute,
    IManagerPerProfession,
    GPermission,
    GProvisioningTask,
    GPersonUseraccount,
    GAccountAttribute,
    PRequestCart,
    PRequestCartRow,
    OneTimeLink,
    IOrgGroup,
    GSystemSchema,
    GSystemSchemaAttribute,
    RSodRuleClass,
    RSodRule,
    RSodException,
    ZuserZrole,
    ZuserIOrgUnit,
    ZuserEExtOrg,
    ZreportUseright,
    ZroleUseright,
    DJobPeriodIOrgUnit,
    DPersonIOrgUnit,
    DPersonDEducation,
    DPersonDCompetence,
    EPersonDEducation,
    EPersonDCompetence,
    EExtOrgGService,
    EExtOrgGServiceRole,
    EExtOrgIOrgGroup,
    EJobPeriodIOrgUnit,
    EJobRoleGServiceRole,
    GServiceRoleGAce,
    HrIntegrationGServiceRole,
    HrIntegrationIOrgUnit,
    HrIntegrationCKeyProfile,
    IJobRoleGServiceRole,
    IJobRoleReqGServiceRole,
    ILegalCompanyGService,
    ILegalCompanyGServiceRole,
    IOrgUnitGService,
    IOrgUnitReqGServiceRole,
    IOrgUnitGServiceRole,
    IOrgUnitIOrgGroup,
    RequestCartPermissionDPerson,
    ERequestCartPermissionDPerson,
    GUserGroupZuser,
    GUserGroupZreport,
    GProvisioningTaskGAce,
    GPermissionAssociatedIOrgUnit,
    GPermissionAssociatedEExtOrg,
    GNotification,
    GNotificationQueue,
    HrImportRecord,
    SDStudyProgramme,
    SDTraineeshipType,
    SDTraineeshipRequest,
    SDTraineeshipRequestPerson,
    SDTraineeshipPlacementRequest,
    SDTraineeshipPlacement,
    SDDepartmentWeekMaxQuantity,
    RDynRole,
    RDynRoleGServiceRole,
    DJobPeriodSubstitute,
    EJobPeriodSubstitute,
  ],
  'LOCALIZED' : [
  ],
  'LOCALIZED, CLASS' : [
  ],
  'ATTR_LOG' : [
    Zuser,
    CCard,
    DAbsence,
    DJobPeriod,
    DJobtitle,
    DPerson,
    EExtOrg,
    EExternalPerson,
    EJobPeriod,
    EJobRole,
    GAce,
    GAceAttribute,
    GService,
    GServiceRole,
    GSystem,
    IJobRole,
    IOrgUnit,
    IOrgUnitManager,
    IOrgUnitManagerSubstitute,
    GPermission,
    GPersonUseraccount,
    GNotification,
    GNotificationQueue,
  ],
  'CLASS' : [
    Zuser,
    Zreport,
    Zrole,
    DJobPeriod,
    DJobtitle,
    DPerson,
    EExtOrg,
    EExtOrgType,
    EExternalPerson,
    EJobPeriod,
    EJobRole,
    GSystem,
    HrIntegration,
    IJobRole,
    IOrgType,
    IOrgUnit,
    RequestCart,
    ERequestCart,
    RequestCartPermission,
    ERequestCartPermission,
    GProvisioningTask,
    GPersonUseraccount,
    GAccountAttribute,
    PRequestCart,
    PRequestCartRow,
    OneTimeLink,
    IOrgGroup,
  ],
  'API' : [
    Zuser,
    Zreport,
    Zrole,
    Useright,
    CCard,
    CCardIssuer,
    CCardOrganization,
    CCardType,
    CDevice,
    CDevicePerson,
    CDeviceSubtype,
    CDeviceType,
    CKey,
    CKeyProfile,
    CKeyType,
    CWorkstation,
    DAbsence,
    DAuthMethod,
    DCompetence,
    DEducation,
    DJobPeriod,
    DJobtitle,
    DMappingRule,
    DPerson,
    DUserAuth,
    EExtOrg,
    EExtOrgType,
    EExternalPerson,
    EJobFamily,
    EJobPeriod,
    EJobRole,
    EOrgTypeService,
    GAce,
    GAceAttribute,
    GCountry,
    GIdentity,
    GIdentitySource,
    GLanguage,
    GRegion,
    GService,
    GServiceProvider,
    GServiceRole,
    GMdmRule,
    GMdmSource,
    GServiceRequest,
    GServiceResp,
    GServiceType,
    GServiceTypeSroles,
    GSrParameters,
    GSrTrans,
    GSystem,
    HrIntegration,
    HrIntegrationVault,
    IBusinessArea,
    ICostCenter,
    HrDesktopSubst,
    IJobFamily,
    IJobRole,
    ILegalCompany,
    ILocation,
    IOrgType,
    IOrgUnit,
    ROrgDac,
    ROrgService,
    ROrgTypeService,
    RUserDac,
    RequestCart,
    ERequestCart,
    RequestCartPermission,
    ERequestCartPermission,
    GUserGroup,
    IOrgUnitManager,
    IOrgUnitManagerSubstitute,
    IManagerPerProfession,
    GPermission,
    GProvisioningTask,
    GPersonUseraccount,
    GAccountAttribute,
    PRequestCart,
    PRequestCartRow,
    OneTimeLink,
    IOrgGroup,
    GSystemSchema,
    GSystemSchemaAttribute,
    RSodRuleClass,
    RSodRule,
    RSodException,
    GNotification,
    GNotificationQueue,
    HrImportRecord,
    SDStudyProgramme,
    SDTraineeshipType,
    SDTraineeshipRequest,
    SDTraineeshipPlacementRequest,
    SDTraineeshipPlacement,
    SDDepartmentWeekMaxQuantity,
    DJobPeriodAbsence,
    EJobPeriodAbsence,
    RDynRole,
    DJobPeriodSubstitute,
    EJobPeriodSubstitute,
  ],
  'NO_PK' : [
  ],
  'MATERIALIZED_STATE' : [
  ],
  'NO_AUDIT' : [
    HrIntegration,
    HrIntegrationVault,
    HrDesktopSubst,
    PRequestCart,
    PRequestCartRow,
  ],
  'SIMULATED' : [
    CCard,
    CCardIssuer,
    CCardOrganization,
    CCardType,
    CDevice,
    CDevicePerson,
    CDeviceSubtype,
    CDeviceType,
    CKey,
    CKeyProfile,
    CKeyType,
    CWorkstation,
    DPerson,
    EExtOrg,
    EExtOrgType,
    EExternalPerson,
    EJobRole,
    EOrgTypeService,
    GAce,
    GAceAttribute,
    GService,
    GServiceProvider,
    GServiceRole,
    GSystem,
    IBusinessArea,
    ICostCenter,
    IJobRole,
    ILegalCompany,
    ILocation,
    IOrgType,
    IOrgUnit,
    ROrgService,
    ROrgTypeService,
    RDynRole,
  ],
  'BACKREF' : [
    CCard,
  ],
  'INTERFACE' : [
    DJobPeriod,
    DPerson,
    EExtOrg,
    EExternalPerson,
    EJobPeriod,
    EJobRole,
    IJobRole,
    IOrgUnit,
    RequestCart,
    ERequestCart,
    RequestCartPermission,
    ERequestCartPermission,
  ],
  'VALIDITY_STATE' : [
    DJobPeriod,
    EJobPeriod,
    GPermission,
  ],
  'GLOBAL_CONTEXT' : [
    DJobPeriod,
    DPerson,
    EExtOrg,
    EExternalPerson,
    EJobPeriod,
    GAce,
    GAceAttribute,
    GService,
    GServiceRole,
    GSystem,
    ILegalCompany,
    ILocation,
    IOrgUnit,
    RequestCart,
    ERequestCart,
    RequestCartPermission,
    ERequestCartPermission,
    GPermission,
    GPersonUseraccount,
  ],
  'CLOSURE_TABLE' : [
    EExtOrg,
    EJobRole,
    GService,
    GServiceRole,
    GSystem,
    IJobRole,
    ILocation,
    IOrgUnit,
    SDTraineeshipType,
  ],
  'COMPARE' : [
    GIdentity,
    HrIntegration,
  ],
  'first_names)' : [
    HrIntegration,
  ],
  'PYCLASS' : [
    IOrgUnitManagerSubstitute,
  ],
  'TIE' : [
    ZuserZrole,
    ZuserIOrgUnit,
    ZuserEExtOrg,
    ZreportUseright,
    ZroleUseright,
    DJobPeriodIOrgUnit,
    DPersonIOrgUnit,
    DPersonDEducation,
    DPersonDCompetence,
    EPersonDEducation,
    EPersonDCompetence,
    EExtOrgGService,
    EExtOrgGServiceRole,
    EExtOrgIOrgGroup,
    EJobPeriodIOrgUnit,
    EJobRoleGServiceRole,
    GServiceRoleGAce,
    HrIntegrationGServiceRole,
    HrIntegrationIOrgUnit,
    HrIntegrationCKeyProfile,
    IJobRoleGServiceRole,
    IJobRoleReqGServiceRole,
    ILegalCompanyGService,
    ILegalCompanyGServiceRole,
    IOrgUnitGService,
    IOrgUnitReqGServiceRole,
    IOrgUnitGServiceRole,
    IOrgUnitIOrgGroup,
    RequestCartPermissionDPerson,
    ERequestCartPermissionDPerson,
    GUserGroupZuser,
    GUserGroupZreport,
    GProvisioningTaskGAce,
    GPermissionAssociatedIOrgUnit,
    GPermissionAssociatedEExtOrg,
    SDTraineeshipRequestPerson,
    RDynRoleGServiceRole,
  ],
  'PERM_LOG' : [
  ],
  'MYSQL_ENGINE' : [
    EExtOrgCtAll,
    EJobRoleCtAll,
    GServiceCtAll,
    GServiceRoleCtAll,
    GSystemCtAll,
    IJobRoleCtAll,
    ILocationCtAll,
    IOrgUnitCtAll,
    SDTraineeshipTypeCtAll,
  ],
  'IS_CLOSURE_TABLE' : [
    EExtOrgCtAll,
    EJobRoleCtAll,
    GServiceCtAll,
    GServiceRoleCtAll,
    GSystemCtAll,
    IJobRoleCtAll,
    ILocationCtAll,
    IOrgUnitCtAll,
    SDTraineeshipTypeCtAll,
  ],
  'IS_ATTR_LOG' : [
  ],
}
from datamaster.model_events import *
