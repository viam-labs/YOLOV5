# YOLOv5 modular service

This module implements the [rdk vision API](https://github.com/rdk/vision-api) in a viam-labs:vision:yolov5 model.

This model leverages the [Ultralytics YOLOv5 inference library](https://pypi.org/project/yolov5/) to allow for object detection from YOLOv5 models.

Both locally deployed YOLOv5 models and models from web sources like [HuggingFace](https://huggingface.co/models?other=yolov5) can be used (HuggingFace models will be downloaded and used locally).

Note that classification models are not currently supported due to author being unable to find a usable example model.

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `viam-labs:vision:yolov5` model from the [viam-labs YOLOv5 module](https://app.viam.com/module/viam-labs/yolov5).

## Configure your vision

> [!NOTE]  
> Before configuring your vision, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your robot’s page in [the Viam app](https://app.viam.com/).
Click on the **Components** subtab and click **Create component**.
Select the `vision` type, then select the `viam-labs:vision:yolov5` model.
Enter a name for your vision and click **Create**.

On the new component panel, copy and paste the following attribute template into your vision service's **Attributes** box:

```json
{
  "model_location": "<model_path>"
}
```

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `viam-labs:vision:yolov5` model:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `model_location` | string | **Required** |  Local path or HuggingFace model identifier |

### Example Configurations

[HuggingFace model](https://huggingface.co/keremberke/yolov5n-construction-safety):

```json
{
  "model_location": "keremberke/yolov5n-construction-safety"
}
```

Local YOLOv5 model:

```json
{
  "model_location": "/path/to/yolov5s.pt"
}
```

## API

The YOLOv5 resource provides the following methods from Viam's built-in [rdk:service:vision API](https://python.viam.dev/autoapi/viam/services/vision/client/index.html)

### get_detections(image=*binary*)

### get_detections_from_camera(camera_name=*string*)

Note: if using this method, any cameras you are using must be set in the `depends_on` array for the service configuration, for example:

```json
      "depends_on": [
        "cam"
      ]
```
