class DwellTimeAnalyzer:
    def __init__(self, rois):
        self.rois = rois  # list of ROI polygons with IDs
        self.inside_times = {}  # {(obj_id, roi_id): entry_timestamp}
    
    def update_object(self, obj_id, position, current_time):
        for roi in self.rois:
            if roi.contains(position):
                key = (obj_id, roi.id)
                if key not in self.inside_times:
                    # person entered ROI
                    self.inside_times[key] = current_time
                else:
                    # person already inside, calculate dwell so far if needed
                    entry_time = self.inside_times[key]
                    dwell = current_time - entry_time
                    # We could update a live metric or trigger event if dwell exceeds threshold
                    if dwell > roi.dwell_threshold:
                        # e.g., send alert or mark as interested customer
                        pass
            else:
                # If person was in this ROI but now left, finalize dwell time
                key = (obj_id, roi.id)
                if key in self.inside_times:
                    entry_time = self.inside_times.pop(key)
                    dwell_duration = current_time - entry_time
                    log_dwell_time(obj_id, roi.id, dwell_duration)
