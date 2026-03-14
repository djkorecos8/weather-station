class WeatherClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_current_temperature(self, location: str) -> float:
        """Fetch current temperature for a location. Placeholder implementation."""
        # TODO: integrate with real weather API
        return 0.0
