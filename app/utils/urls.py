"""Shared URL helpers."""

from typing import Optional

from app.config import get_tracer_base_url


def get_investigation_url(
    organization_slug: Optional[str],
    investigation_id: Optional[str],
) -> Optional[str]:
    if not organization_slug or not investigation_id:
        return None

    base_url = get_tracer_base_url().rstrip("/")
    return f"{base_url}/o/{organization_slug}/investigations/{investigation_id}"