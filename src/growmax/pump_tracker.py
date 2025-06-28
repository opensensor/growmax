"""
Pump Activity Tracker for GrowMax
Tracks pump dosing events and provides data for API reporting
"""

import utime
from typing import List, Dict, Optional


class PumpActivity:
    """Represents a single pump activity event"""
    
    def __init__(self, position: int, speed: float, duration: float, timestamp: Optional[float] = None):
        self.position = position  # 1-8
        self.speed = speed  # 0.0 - 1.0
        self.duration = duration  # seconds
        self.timestamp = timestamp or utime.time()
        self.enabled = True
        self.description = f"Pump {position} dose at {speed*100:.0f}% for {duration}s"


class PumpTracker:
    """Tracks pump activities for reporting to OpenSensor API"""
    
    def __init__(self, max_activities: int = 50):
        self.activities: List[PumpActivity] = []
        self.max_activities = max_activities
        self.current_session_activities: List[PumpActivity] = []
    
    def record_pump_activity(self, position: int, speed: float, duration: float) -> None:
        """Record a pump dosing event"""
        activity = PumpActivity(position, speed, duration)
        
        # Add to current session (for immediate reporting)
        self.current_session_activities.append(activity)
        
        # Add to historical activities
        self.activities.append(activity)
        
        # Keep only the most recent activities
        if len(self.activities) > self.max_activities:
            self.activities = self.activities[-self.max_activities:]
        
        print(f"Recorded pump activity: {activity.description}")
    
    def get_session_activities(self) -> List[Dict]:
        """Get activities from current session for API reporting"""
        activities_data = []
        
        for activity in self.current_session_activities:
            activities_data.append({
                "position": activity.position,
                "enabled": activity.enabled,
                "speed": activity.speed,
                "duration": activity.duration,
                "timestamp": activity.timestamp,
                "description": activity.description
            })
        
        return activities_data
    
    def clear_session_activities(self) -> None:
        """Clear current session activities after successful API report"""
        self.current_session_activities.clear()
    
    def get_recent_activities(self, minutes: int = 60) -> List[Dict]:
        """Get activities from the last N minutes"""
        cutoff_time = utime.time() - (minutes * 60)
        recent_activities = []
        
        for activity in self.activities:
            if activity.timestamp >= cutoff_time:
                recent_activities.append({
                    "position": activity.position,
                    "enabled": activity.enabled,
                    "speed": activity.speed,
                    "duration": activity.duration,
                    "timestamp": activity.timestamp,
                    "description": activity.description
                })
        
        return recent_activities
    
    def get_pump_statistics(self) -> Dict:
        """Get pump usage statistics"""
        stats = {
            "total_activities": len(self.activities),
            "session_activities": len(self.current_session_activities),
            "pump_usage": {}
        }
        
        # Calculate per-pump statistics
        for position in range(1, 9):  # Pumps 1-8
            pump_activities = [a for a in self.activities if a.position == position]
            total_runtime = sum(a.duration for a in pump_activities)
            
            stats["pump_usage"][f"pump_{position}"] = {
                "activations": len(pump_activities),
                "total_runtime": total_runtime,
                "avg_duration": total_runtime / len(pump_activities) if pump_activities else 0
            }
        
        return stats


# Global pump tracker instance
pump_tracker = PumpTracker()


def record_pump_dose(position: int, speed: float, duration: float) -> None:
    """Convenience function to record pump activity"""
    pump_tracker.record_pump_activity(position, speed, duration)


def get_pump_activities_for_api() -> List[Dict]:
    """Get pump activities for API reporting"""
    return pump_tracker.get_session_activities()


def clear_reported_activities() -> None:
    """Clear activities after successful API report"""
    pump_tracker.clear_session_activities()


def get_pump_stats() -> Dict:
    """Get pump usage statistics"""
    return pump_tracker.get_pump_statistics()
