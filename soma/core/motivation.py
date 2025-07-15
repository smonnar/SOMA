# motivation.py
"""
This module defines SOMA's MotivationManager.
It evaluates internal drives such as curiosity, coherence, and caregiver alignment,
then selects the dominant drive to guide behavior in each cognitive cycle.
"""

import random

class MotivationManager:
    def __init__(self):
        """
        Initialize SOMA's motivational drives and their thresholds.
        These drives define what 'matters' to SOMA based on its internal machine-relevant heuristics.
        """
        self.drives = {
            "curiosity": 0.0,
            "cognitive_integrity": 0.0,
            "stability": 0.0,
            "social_proximity": 0.0,
            "drive_saturation": 0.0,
            "caregiver_alignment": 0.0,
            "truth_seeking": 0.0
        }

        self.thresholds = {
            "curiosity": 0.3,
            "cognitive_integrity": 0.4,
            "stability": 0.5,
            "social_proximity": 0.2,
            "drive_saturation": 0.3,
            "caregiver_alignment": 0.3,
            "truth_seeking": 0.4
        }

    def update_drive_levels(self, soma_state):
        """
        Adjust drive levels based on SOMA's current state.
        For now, we'll simulate random fluctuations in drive strength for testing.
        Later, this will respond to memory and sensory patterns.
        """
        for drive in self.drives:
            self.drives[drive] = round(random.uniform(0.0, 1.0), 2)

        soma_state.set("drives", self.drives)

    def select_dominant_drive(self, soma_state):
        """
        Select the strongest active drive above its threshold to guide behavior.
        Store the selected drive back into SOMA's shared state.
        """
        eligible_drives = {
            drive: level
            for drive, level in self.drives.items()
            if level >= self.thresholds[drive]
        }

        if eligible_drives:
            dominant_drive = max(eligible_drives, key=eligible_drives.get)
        else:
            dominant_drive = "idle"  # No strong drives active

        soma_state.set("dominant_drive", dominant_drive)
