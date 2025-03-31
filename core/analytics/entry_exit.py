# analytics/entry_exit.py
class EntryExitCounter:
    def __init__(self, entry_lines):
        # entry_lines: list of dicts with line endpoints and orientation
        self.lines = entry_lines
        self.last_positions = {}  # { object_id: "inside"/"outside" }

    def process_object(self, obj_id, foot_point):
        # Determine side of each line
        for line in self.lines:
            side = self._point_side_of_line(foot_point, line)
            if obj_id not in self.last_positions:
                self.last_positions[obj_id] = side
            prev_side = self.last_positions[obj_id]
            if prev_side != side and prev_side is not None:
                # Crossing happened
                if side == "inside":
                    line['entries'] += 1
                    log_event("entry", obj_id, line['id'])
                elif side == "outside":
                    line['exits'] += 1
                    log_event("exit", obj_id, line['id'])
            self.last_positions[obj_id] = side

    def _point_side_of_line(self, point, line):
        # Compute which side of the line the point is on (e.g., using cross product)
        # returns "inside", "outside", or None if exactly on the line
        ...
