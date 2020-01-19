import os
from collections import OrderedDict
import json

# file_path = os.getcwd() + '/' + 'some_file.dat'
# # print file_path
# key = 'a'
# value = '2'

# if not os.path.exists(file_path):
# 	# print 'file not present.'
# 	event_dict = OrderedDict()
# 	event_dict.update({key: value})
# 	f = open('some_file.dat', 'w')
# 	f.write('%s' % event_dict)
# 	f.close()
# else:
# 	# print 'file present.'
# 	f = open('some_file.dat')
# 	event_dict = eval(f.read())
# 	# print event_dict
# 	event_dict.update({key: value})
# 	f1 = open('some_file.dat', 'w')
# 	f1.write('%s' % event_dict)
# 	f1.close()
# 	f.close()

data = {'action': 'create', 'type': 'EVENT', 'subscriptionId': '239eccaf-a663-4f9f-9ec9-b9058e51cade', 'data': {'mc_tool_uri': '', 'itsm_location': '', 'mc_parameter_unit': 'i336', 'mc_propagations': '[]', 'mc_tool_suggestion': '', 'mc_cause': '0', 'mc_relationships': '0/0', 'mc_client_address': '10.1.128.30', 'mc_long_msg': 'BGP Peer Not Established on BGUR-NL003-WNRT02.cisco (peer to 172.17.31.2) - Now in the idle state', 'class_name': 'EYE_EVENT', 'mc_smc_priority': '0', 'mc_incident_time': '1578372454', 'mc_collectors': "['1.1', '3.1.1', '4.1', '5.1']", 'mc_local_reception_time': '1578372454', 'mc_event_relations': '[]', 'mc_tool_rule': '', 'mc_host_address': '172.20.56.34', 'mc_service': '', 'itsm_type': '', 'event_handle': '37198', 'cell_name': 'pncell_BMBIDC0APNM23', 'adapter_host': '', 'mc_tool_address': '10.1.128.140', 'mc_smc_causes': '[]', 'CLASS': 'MC_CELL_UNDEFINED_CLASS', 'mc_parameter': 'BGP Peer Not Established', 'mc_host_id': '0', 'mc_relation_source': '', 'mc_abstraction': '[]', 'status': 'OPEN', 'mc_origin_class': '', 'mc_acl': '[]', 'itsm_operational_category1': '', 'itsm_operational_category3': '', 'itsm_category': '', 'pn_device_name': '', 'mc_origin_sev': '', 'duration': '0', 'mc_smc_impact': 'NOT_ELECTED', 'mc_object_class': 'StormWorks', 'mc_incident_report_time': '0', 'mc_modhist': '[pncell_BMBIDC0APNM23]', 'mc_event_category': 'OPERATIONS_MANAGEMENT', 'mc_smc_effects': '[]', 'mc_priority': 'PRIORITY_5', 'mc_timeout': '0', 'mc_using_organization': '', 'mc_date_modification': '1578372454', 'itsm_incident_id': '', 'mc_history': "['pncell_BMBIDC0APNM23:37198', 'ENR:15476']", 'mc_tool_sev': '10', 'mc_origin_key': '', 'mc_host': 'bgur-nl003-wnrt02.cisco', 'mc_object': 'BGUR-NL003-WNRT02.cisco (peer to 172.17.31.2)', 'itsm_item': '', 'pn_detail_diag_count': '0', 'mc_associations': '[]', 'mc_object_owner': '', 'mc_effects': '[]', 'mc_abstracted': '[]', 'mc_parameter_value': '1', 'itsm_incident_status': '', 'mc_tool_key': '336', 'mc_tool': 'Eye of the Storm', 'mc_account': '', 'msg': 'BGP Peer Not Established on BGUR-NL003-WNRT02.cisco (peer to 172.17.31.2)', 'mc_tool_time': '0', 'mc_original_severity': 'CRITICAL', 'mc_owner': '', 'mc_bad_slot_names': '[eye_userId, eye_stormworks_id, eye_comp_id, eye_event_group, eye_event_id, eye_view]', 'itsm_operational_category2': '', 'mc_object_uri': 'https://bmbidc0apnm30.nausena.mil/webUI/main.do?url=/webUI/objectSummary.do%3Fserver%3D5582f0bb-a892-4b89-a57c-0d7595d79b12%26id%3D78678', 'mc_parameter_threshold': '', 'mc_smc_id': '', 'pn_detail_diag': '0', 'mc_arrival_time': '1578372454', 'mc_notification_history': '[]', 'mc_original_priority': 'PRIORITY_5', 'mc_smc_alias': '', 'mc_host_class': '', 'itsm_manufacturer': '', 'repeat_count': '0', 'cell_location': '10.1.128.170/1828', 'mc_action_count': '0', 'severity': 'CRITICAL', 'mc_event_subcategory': 'OTHER', 'mc_ueid': 'EYE.BMBIDC0APNM30.nausena.mil.AllObjects.i336.8078', 'itsm_product_name': '', 'date_reception': '1578372454', 'mc_tool_class': 'Windows Server 2016', 'administrator': '', 'mc_using_organization_id': '', 'mc_operations': "[0x5e140d66, 'refine_multiple_server_events.mrl:refine initialize_core_event', '', 'Initialized CORE_EVENT slots specific to CI association', '']", 'itsm_company': '', 'itsm_model_version': '', 'mc_event_model_version': '1.1.00', 'date': '20200107101734.000000+330', 'mc_origin': '', 'mc_tool_id': 'BMBIDC0APNM30.nausena.mil', 'mc_bad_slot_values': "[admin, 78678, '''2147483648.78678.0.0''', 1, i128, '''All Objects''']", 'mc_notes': '[]', 'mc_location': 'cisco', 'mc_smc_type': ''}, 'nativeProbableCause': 'BGP Peer Not Established on BGUR-NL003-WNRT02.cisco (peer to 172.17.31.2)'}

print (json.dumps(data))