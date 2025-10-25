import cv2
import numpy as np
import mss
import threading
import time
from pathlib import Path

class ScreenRecorder:
    """Screen recorder utility for capturing test execution."""
    
    def __init__(self, output_path, fps=30.0):
        """
        Initialize screen recorder.
        
        Args:
            output_path: Path to save the video file
            fps: Frames per second for recording
        """
        self.output_path = output_path
        self.fps = fps
        self.recording = False
        self.thread = None
        self.out = None
        self.sct = None
        
    def start(self):
        """Start recording."""
        if self.recording:
            print("Recording already in progress")
            return
            
        self.recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()
        print(f"Screen recording started: {self.output_path}")
        
    def stop(self):
        """Stop recording."""
        if not self.recording:
            return
            
        self.recording = False
        if self.thread:
            self.thread.join()
        if self.out:
            self.out.release()
        print(f"Screen recording stopped: {self.output_path}")
        
    def _record(self):
        """Internal recording loop."""
        self.sct = mss.mss()
        monitor = self.sct.monitors[1]  # Primary monitor
        
        # Get screen dimensions
        width = monitor["width"]
        height = monitor["height"]
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(
            str(self.output_path),
            fourcc,
            self.fps,
            (width, height)
        )
        
        # Recording loop
        while self.recording:
            # Capture screen
            img = self.sct.grab(monitor)
            frame = np.array(img)
            
            # Convert BGRA to BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            
            # Write frame
            self.out.write(frame)
            
            # Control frame rate
            time.sleep(1.0 / self.fps)

def get_video_path(test_name):
    """
    Generate video file path for a test.
    
    Args:
        test_name: Name of the test
        
    Returns:
        Path object for the video file
    """
    video_dir = Path(__file__).parent.parent / "artifacts" / "videos"
    video_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filename = f"{test_name}_{timestamp}.mp4"
    
    return video_dir / filename
