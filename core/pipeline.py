import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
import pyds  # DeepStream Python bindings

Gst.init(None)

pipeline = Gst.Pipeline()

# Source example (RTSP input)
source = Gst.ElementFactory.make("uridecodebin", "source-decoder")
source.set_property("uri", rtsp_uri)  # rtsp_uri from config

# Stream muxer for batch processing
streammux = Gst.ElementFactory.make("nvstreammux", "StreamMux")
streammux.set_property("batch-size", num_sources)
streammux.set_property("width", 1280)
streammux.set_property("height", 720)
streammux.set_property("batched-push-timeout", 40000)

# Primary inference (PGIE)
pgie = Gst.ElementFactory.make("nvinfer", "primary-inference")
pgie.set_property("config-file-path", model_config_path)  # e.g., configs/models/config_infer_primary_peoplenet.txt

# Tracker
tracker = Gst.ElementFactory.make("nvtracker", "tracker")
tracker_config = parse_tracker_config("configs/tracker_config.txt")
for key, value in tracker_config.items():
    tracker.set_property(key, value)

# Analytics plugin for ROI, line-crossing, etc.
analytics = Gst.ElementFactory.make("nvdsanalytics", "analytics")
analytics.set_property("config-file", "configs/analytics_config.txt")
analytics.set_property("enable", True)

# OSD and Sink
osd = Gst.ElementFactory.make("nvdsosd", "onscreendisplay")
sink = Gst.ElementFactory.make("nveglglessink", "videosink")  # display on screen (for development)
sink.set_property("sync", False)

# Add and link elements in pipeline
for elem in [streammux, pgie, tracker, analytics, osd, sink]:
    pipeline.add(elem)
# (We link them after source pads are connected, see below)
