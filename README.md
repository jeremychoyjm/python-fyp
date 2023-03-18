Final Year Project
--

Dataset (Labelled)
--
https://universe.roboflow.com/fyp-xa0nw/fyp-no4lf

Example
--
```
yolo segment train data=data.yaml model=jeremy.pt epochs=100 imgsz=640

yolo segment predict model=jeremy.pt source=test.jpg save=true

yolo export model=jeremy.pt format=onnx
``` 

| Export Format                                                      | `format=`     | Metadata |
|--------------------------------------------------------------------|---------------|----------|
| [TorchScript](https://pytorch.org/docs/stable/jit.html)            | `torchscript` |     ✅      |
| [ONNX](https://onnx.ai/)                                           | `onnx`        |     ✅      |
| [OpenVINO](https://docs.openvino.ai/latest/index.html)             | `openvino`    |     ✅      |
| [TensorRT](https://developer.nvidia.com/tensorrt)                  | `engine`      |     ✅      |
| [CoreML](https://github.com/apple/coremltools)                     | `coreml`      |     ✅      |
| [TF SavedModel](https://www.tensorflow.org/guide/saved_model)      | `saved_model` |     ✅      |
| [TF GraphDef](https://www.tensorflow.org/api_docs/python/tf/Graph) | `pb`          |     ❌      |
| [TF Lite](https://www.tensorflow.org/lite)                         | `tflite`      |     ✅      |
| [TF Edge TPU](https://coral.ai/docs/edgetpu/models-intro/)         | `edgetpu`     |     ✅      |
| [TF.js](https://www.tensorflow.org/js)                             | `tfjs`        |     ✅      |
| [PaddlePaddle](https://github.com/PaddlePaddle)                    | `paddle`      |     ✅      |

Reference
--
https://github.com/ultralytics/ultralytics
