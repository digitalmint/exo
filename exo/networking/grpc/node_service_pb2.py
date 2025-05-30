# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: node_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'node_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12node_service.proto\x12\x0cnode_service\"S\n\x05Shard\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x13\n\x0bstart_layer\x18\x02 \x01(\x05\x12\x11\n\tend_layer\x18\x03 \x01(\x05\x12\x10\n\x08n_layers\x18\x04 \x01(\x05\"\x97\x01\n\x11GenerationOptions\x12\"\n\x15max_completion_tokens\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04stop\x18\x02 \x03(\t\x12\x1f\n\x12grammar_definition\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x18\n\x16_max_completion_tokensB\x15\n\x13_grammar_definition\"\x94\x02\n\rPromptRequest\x12\"\n\x05shard\x18\x01 \x01(\x0b\x32\x13.node_service.Shard\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x17\n\nrequest_id\x18\x03 \x01(\tH\x00\x88\x01\x01\x12:\n\x0finference_state\x18\x04 \x01(\x0b\x32\x1c.node_service.InferenceStateH\x01\x88\x01\x01\x12@\n\x12generation_options\x18\x05 \x01(\x0b\x32\x1f.node_service.GenerationOptionsH\x02\x88\x01\x01\x42\r\n\x0b_request_idB\x12\n\x10_inference_stateB\x15\n\x13_generation_options\"\xaa\x02\n\rTensorRequest\x12\"\n\x05shard\x18\x01 \x01(\x0b\x32\x13.node_service.Shard\x12$\n\x06tensor\x18\x02 \x01(\x0b\x32\x14.node_service.Tensor\x12\x17\n\nrequest_id\x18\x03 \x01(\tH\x00\x88\x01\x01\x12:\n\x0finference_state\x18\x04 \x01(\x0b\x32\x1c.node_service.InferenceStateH\x01\x88\x01\x01\x12@\n\x12generation_options\x18\x05 \x01(\x0b\x32\x1f.node_service.GenerationOptionsH\x02\x88\x01\x01\x42\r\n\x0b_request_idB\x12\n\x10_inference_stateB\x15\n\x13_generation_options\"\xde\x01\n\x0e\x45xampleRequest\x12\"\n\x05shard\x18\x01 \x01(\x0b\x32\x13.node_service.Shard\x12%\n\x07\x65xample\x18\x02 \x01(\x0b\x32\x14.node_service.Tensor\x12$\n\x06target\x18\x03 \x01(\x0b\x32\x14.node_service.Tensor\x12$\n\x06length\x18\x04 \x01(\x0b\x32\x14.node_service.Tensor\x12\r\n\x05train\x18\x05 \x01(\x08\x12\x17\n\nrequest_id\x18\x06 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_request_id\"H\n\x04Loss\x12\x0c\n\x04loss\x18\x01 \x01(\x02\x12(\n\x05grads\x18\x02 \x01(\x0b\x32\x14.node_service.TensorH\x00\x88\x01\x01\x42\x08\n\x06_grads\";\n\x06Tensor\x12\x13\n\x0btensor_data\x18\x01 \x01(\x0c\x12\r\n\x05shape\x18\x02 \x03(\x05\x12\r\n\x05\x64type\x18\x03 \x01(\t\"3\n\nTensorList\x12%\n\x07tensors\x18\x01 \x03(\x0b\x32\x14.node_service.Tensor\"\xd2\x02\n\x0eInferenceState\x12\x41\n\x0btensor_data\x18\x01 \x03(\x0b\x32,.node_service.InferenceState.TensorDataEntry\x12J\n\x10tensor_list_data\x18\x02 \x03(\x0b\x32\x30.node_service.InferenceState.TensorListDataEntry\x12\x17\n\x0fother_data_json\x18\x03 \x01(\t\x1aG\n\x0fTensorDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.node_service.Tensor:\x02\x38\x01\x1aO\n\x13TensorListDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.node_service.TensorList:\x02\x38\x01\"<\n\x16\x43ollectTopologyRequest\x12\x0f\n\x07visited\x18\x01 \x03(\t\x12\x11\n\tmax_depth\x18\x02 \x01(\x05\"\x98\x02\n\x08Topology\x12\x30\n\x05nodes\x18\x01 \x03(\x0b\x32!.node_service.Topology.NodesEntry\x12\x39\n\npeer_graph\x18\x02 \x03(\x0b\x32%.node_service.Topology.PeerGraphEntry\x1aN\n\nNodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .node_service.DeviceCapabilities:\x02\x38\x01\x1aO\n\x0ePeerGraphEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.node_service.PeerConnections:\x02\x38\x01\"I\n\x0ePeerConnection\x12\r\n\x05to_id\x18\x01 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"D\n\x0fPeerConnections\x12\x31\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32\x1c.node_service.PeerConnection\"7\n\x0b\x44\x65viceFlops\x12\x0c\n\x04\x66p32\x18\x01 \x01(\x01\x12\x0c\n\x04\x66p16\x18\x02 \x01(\x01\x12\x0c\n\x04int8\x18\x03 \x01(\x01\"k\n\x12\x44\x65viceCapabilities\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0c\n\x04\x63hip\x18\x02 \x01(\t\x12\x0e\n\x06memory\x18\x03 \x01(\x05\x12(\n\x05\x66lops\x18\x04 \x01(\x0b\x32\x19.node_service.DeviceFlops\"\xb0\x01\n\x11SendResultRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x03(\x05\x12)\n\x06tensor\x18\x03 \x01(\x0b\x32\x14.node_service.TensorH\x00\x88\x01\x01\x12\x13\n\x0bis_finished\x18\x04 \x01(\x08\x12\x1a\n\rfinish_reason\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_tensorB\x10\n\x0e_finish_reason\"=\n\x17SendOpaqueStatusRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x14\n\x12HealthCheckRequest\")\n\x13HealthCheckResponse\x12\x12\n\nis_healthy\x18\x01 \x01(\x08\"\x07\n\x05\x45mpty2\x97\x04\n\x0bNodeService\x12\x41\n\nSendPrompt\x12\x1b.node_service.PromptRequest\x1a\x14.node_service.Tensor\"\x00\x12\x41\n\nSendTensor\x12\x1b.node_service.TensorRequest\x1a\x14.node_service.Tensor\"\x00\x12\x41\n\x0bSendExample\x12\x1c.node_service.ExampleRequest\x1a\x12.node_service.Loss\"\x00\x12Q\n\x0f\x43ollectTopology\x12$.node_service.CollectTopologyRequest\x1a\x16.node_service.Topology\"\x00\x12\x44\n\nSendResult\x12\x1f.node_service.SendResultRequest\x1a\x13.node_service.Empty\"\x00\x12P\n\x10SendOpaqueStatus\x12%.node_service.SendOpaqueStatusRequest\x1a\x13.node_service.Empty\"\x00\x12T\n\x0bHealthCheck\x12 .node_service.HealthCheckRequest\x1a!.node_service.HealthCheckResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'node_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INFERENCESTATE_TENSORDATAENTRY']._loaded_options = None
  _globals['_INFERENCESTATE_TENSORDATAENTRY']._serialized_options = b'8\001'
  _globals['_INFERENCESTATE_TENSORLISTDATAENTRY']._loaded_options = None
  _globals['_INFERENCESTATE_TENSORLISTDATAENTRY']._serialized_options = b'8\001'
  _globals['_TOPOLOGY_NODESENTRY']._loaded_options = None
  _globals['_TOPOLOGY_NODESENTRY']._serialized_options = b'8\001'
  _globals['_TOPOLOGY_PEERGRAPHENTRY']._loaded_options = None
  _globals['_TOPOLOGY_PEERGRAPHENTRY']._serialized_options = b'8\001'
  _globals['_SHARD']._serialized_start=36
  _globals['_SHARD']._serialized_end=119
  _globals['_GENERATIONOPTIONS']._serialized_start=122
  _globals['_GENERATIONOPTIONS']._serialized_end=273
  _globals['_PROMPTREQUEST']._serialized_start=276
  _globals['_PROMPTREQUEST']._serialized_end=552
  _globals['_TENSORREQUEST']._serialized_start=555
  _globals['_TENSORREQUEST']._serialized_end=853
  _globals['_EXAMPLEREQUEST']._serialized_start=856
  _globals['_EXAMPLEREQUEST']._serialized_end=1078
  _globals['_LOSS']._serialized_start=1080
  _globals['_LOSS']._serialized_end=1152
  _globals['_TENSOR']._serialized_start=1154
  _globals['_TENSOR']._serialized_end=1213
  _globals['_TENSORLIST']._serialized_start=1215
  _globals['_TENSORLIST']._serialized_end=1266
  _globals['_INFERENCESTATE']._serialized_start=1269
  _globals['_INFERENCESTATE']._serialized_end=1607
  _globals['_INFERENCESTATE_TENSORDATAENTRY']._serialized_start=1455
  _globals['_INFERENCESTATE_TENSORDATAENTRY']._serialized_end=1526
  _globals['_INFERENCESTATE_TENSORLISTDATAENTRY']._serialized_start=1528
  _globals['_INFERENCESTATE_TENSORLISTDATAENTRY']._serialized_end=1607
  _globals['_COLLECTTOPOLOGYREQUEST']._serialized_start=1609
  _globals['_COLLECTTOPOLOGYREQUEST']._serialized_end=1669
  _globals['_TOPOLOGY']._serialized_start=1672
  _globals['_TOPOLOGY']._serialized_end=1952
  _globals['_TOPOLOGY_NODESENTRY']._serialized_start=1793
  _globals['_TOPOLOGY_NODESENTRY']._serialized_end=1871
  _globals['_TOPOLOGY_PEERGRAPHENTRY']._serialized_start=1873
  _globals['_TOPOLOGY_PEERGRAPHENTRY']._serialized_end=1952
  _globals['_PEERCONNECTION']._serialized_start=1954
  _globals['_PEERCONNECTION']._serialized_end=2027
  _globals['_PEERCONNECTIONS']._serialized_start=2029
  _globals['_PEERCONNECTIONS']._serialized_end=2097
  _globals['_DEVICEFLOPS']._serialized_start=2099
  _globals['_DEVICEFLOPS']._serialized_end=2154
  _globals['_DEVICECAPABILITIES']._serialized_start=2156
  _globals['_DEVICECAPABILITIES']._serialized_end=2263
  _globals['_SENDRESULTREQUEST']._serialized_start=2266
  _globals['_SENDRESULTREQUEST']._serialized_end=2442
  _globals['_SENDOPAQUESTATUSREQUEST']._serialized_start=2444
  _globals['_SENDOPAQUESTATUSREQUEST']._serialized_end=2505
  _globals['_HEALTHCHECKREQUEST']._serialized_start=2507
  _globals['_HEALTHCHECKREQUEST']._serialized_end=2527
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=2529
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=2570
  _globals['_EMPTY']._serialized_start=2572
  _globals['_EMPTY']._serialized_end=2579
  _globals['_NODESERVICE']._serialized_start=2582
  _globals['_NODESERVICE']._serialized_end=3117
# @@protoc_insertion_point(module_scope)
