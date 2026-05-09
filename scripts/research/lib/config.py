"""Loads research-toolkit credentials and model defaults from ~/.config/ces-second-brain/.env"""

from pathlib import Path
from dotenv import load_dotenv
import os

CONFIG_DIR = Path.home() / ".config" / "ces-second-brain"
ENV_PATH = CONFIG_DIR / ".env"

load_dotenv(ENV_PATH)


def get_required(name: str) -> str:
    val = os.environ.get(name, "").strip()
    if not val:
        raise SystemExit(
            f"\n{name} not configured.\n"
            f"Add it to {ENV_PATH}\n"
            f"Or run install.sh from the ces-second-brain repo to set it up.\n"
        )
    return val


def get_optional(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip() or default


XAI_API_KEY = lambda: get_required("XAI_API_KEY")
PERPLEXITY_API_KEY = lambda: get_required("PERPLEXITY_API_KEY")
YOUTUBE_API_KEY = lambda: get_optional("YOUTUBE_API_KEY", "")

GROK_MODEL = get_optional("GROK_MODEL", "grok-4")
PERPLEXITY_RESEARCH_MODEL = get_optional("PERPLEXITY_RESEARCH_MODEL", "sonar-pro")
PERPLEXITY_DEEP_MODEL = get_optional("PERPLEXITY_DEEP_MODEL", "sonar-deep-research")

VAULT_PATH = Path.home() / "Projects" / "personal" / "obsinian" / "Eugeniu's Vault"
USAGE_LOG = Path.home() / ".research-toolkit" / "usage.log"
