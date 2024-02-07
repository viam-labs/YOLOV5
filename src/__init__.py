"""
This file registers the model with the Python SDK.
"""

from viam.services.vision import Vision
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .YOLOv5 import YOLOv5

Registry.register_resource_creator(Vision.SUBTYPE, YOLOv5.MODEL, ResourceCreatorRegistration(YOLOv5.new, YOLOv5.validate))
