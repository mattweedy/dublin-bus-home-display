from datetime import datetime


class Arrival:
    def __init__(
        self,
        route,
        headsign,
        agency,
        scheduled_arrival,
        real_time_arrival=None,
        stop_id=None,  # Added
        stop_name=None,  # Added
    ):
        self.route = route
        self.headsign = headsign
        self.agency = agency
        self.scheduled_arrival = scheduled_arrival
        self.real_time_arrival = real_time_arrival
        self.stop_id = stop_id  # Store which stop this is for
        self.stop_name = stop_name  # Store the stop name

    @property
    def minutes_until(self):
        time_str = self.real_time_arrival or self.scheduled_arrival
        if time_str is None:
            return 999

        try:
            now = datetime.now()
            bus_time = datetime.fromisoformat(time_str)
            return int((bus_time - now).total_seconds() / 60)
        except (ValueError, TypeError):
            return 999

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
