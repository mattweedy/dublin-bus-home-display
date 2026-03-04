from datetime import datetime


def time_convert(time_str):
    if time_str is None:
        return None
    dt = datetime.fromisoformat(time_str)
    return dt.strftime("%H:%M")


class Arrival:
    def __init__(
        self,
        route,
        headsign,
        agency,
        scheduled_arrival,
        real_time_arrival=None,
        stop_id=None,
        stop_name=None,
    ):
        self.route = route
        self.headsign = headsign
        self.agency = agency
        self.scheduled_arrival = scheduled_arrival
        self.real_time_arrival = real_time_arrival
        self.stop_id = stop_id
        self.stop_name = stop_name

    @property
    def minutes_until(self):
        time_str = self.real_time_arrival or self.scheduled_arrival
        if time_str is None:
            return 999

        try:
            now = datetime.now()
            bus_time = datetime.fromisoformat(time_str)
            return int((bus_time - now).total_seconds() / 60)
        except (ValueError, TypeError, AttributeError):
            return 999

    @property
    def display_time(self):
        """Return the real-time arrival in HH:MM format, or None if not available"""
        if self.real_time_arrival:
            return time_convert(self.real_time_arrival)
        return None

    @property
    def scheduled_display_time(self):
        """Return the scheduled arrival in HH:MM format"""
        return time_convert(self.scheduled_arrival)

    def __repr__(self):
        mins = self.minutes_until
        if mins == 999:
            return f"Arrival(route={self.route}, to={self.headsign}, time=unknown)"
        elif mins < 0:
            return f"Arrival(route={self.route}, to={self.headsign}, passed {abs(mins)} min ago)"
        else:
            return f"Arrival(route={self.route}, to={self.headsign}, in {mins} min)"

    def __str__(self):
        return f"{self.route} to {self.headsign} at {self.stop_name} in {self.minutes_until} min"
