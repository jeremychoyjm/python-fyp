Final Year Project
--

Dataset
--
https://universe.roboflow.com/fyp-xa0nw/fyp-no4lf/dataset/1

Example
--
```
yolo segment train data=data.yaml model=jeremy.pt epochs=100 imgsz=640
yolo segment predict model=jeremy.pt source=test.jpg save=true
yolo export model=jeremy.pt format=onnx
``` 

| Export Format                                                      | `format=`     | Model                         | Metadata |
|--------------------------------------------------------------------|---------------|-------------------------------|----------|
| [PyTorch](https://pytorch.org/)                                    | -             | `yolov8n-seg.pt`              | ✅        |
| [TorchScript](https://pytorch.org/docs/stable/jit.html)            | `torchscript` | `yolov8n-seg.torchscript`     | ✅        |
| [ONNX](https://onnx.ai/)                                           | `onnx`        | `yolov8n-seg.onnx`            | ✅        |
| [OpenVINO](https://docs.openvino.ai/latest/index.html)             | `openvino`    | `yolov8n-seg_openvino_model/` | ✅        |
| [TensorRT](https://developer.nvidia.com/tensorrt)                  | `engine`      | `yolov8n-seg.engine`          | ✅        |
| [CoreML](https://github.com/apple/coremltools)                     | `coreml`      | `yolov8n-seg.mlmodel`         | ✅        |
| [TF SavedModel](https://www.tensorflow.org/guide/saved_model)      | `saved_model` | `yolov8n-seg_saved_model/`    | ✅        |
| [TF GraphDef](https://www.tensorflow.org/api_docs/python/tf/Graph) | `pb`          | `yolov8n-seg.pb`              | ❌        |
| [TF Lite](https://www.tensorflow.org/lite)                         | `tflite`      | `yolov8n-seg.tflite`          | ✅        |
| [TF Edge TPU](https://coral.ai/docs/edgetpu/models-intro/)         | `edgetpu`     | `yolov8n-seg_edgetpu.tflite`  | ✅        |
| [TF.js](https://www.tensorflow.org/js)                             | `tfjs`        | `yolov8n-seg_web_model/`      | ✅        |
| [PaddlePaddle](https://github.com/PaddlePaddle)                    | `paddle`      | `yolov8n-seg_paddle_model/`   | ✅        |

Reference
--
https://github.com/ultralytics/ultralytics
