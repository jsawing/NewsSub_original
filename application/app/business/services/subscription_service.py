import re
from datetime import datetime, timezone

class SubscriptionService:
    """Service för affärslogik gällande prenumerationer."""
    
    # Regex för e-postvalidering
    EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def validate_email(self, email: str) -> tuple[bool, str]:
        """Validerar e-postformatet. Returnerar (is_valid, error_message)."""
        if not email or not email.strip():
            return False, "Email is required"
        if not re.match(self.EMAIL_PATTERN, email.strip()):
            return False, "Invalid email format"
        return True, ""

    def normalize_email(self, email: str) -> str:
        """Gör om till små bokstäver och tar bort mellanslag."""
        return email.lower().strip()

    def normalize_name(self, name: str | None) -> str:
        """Tar bort mellanslag eller returnerar standardvärde."""
        if not name or not name.strip():
            return "Subscriber"
        return name.strip()

    def process_subscription(self, email: str, name: str | None) -> dict:
        """Validerar, normaliserar och paketerar data."""
        is_valid, error = self.validate_email(email)
        if not is_valid:
            raise ValueError(error)

        return {
            "email": self.normalize_email(email),
            "name": self.normalize_name(name),
            "subscribed_at": datetime.now(timezone.utc).isoformat(),
        }